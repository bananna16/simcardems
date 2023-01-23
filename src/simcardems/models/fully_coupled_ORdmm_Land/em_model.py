from __future__ import annotations

from typing import Tuple
from typing import TYPE_CHECKING

import dolfin

from ... import utils
from ...geometry import BaseGeometry
from ..em_model import BaseEMCoupling

if TYPE_CHECKING:
    from ...mechanics_model import MechanicsProblem


logger = utils.getLogger(__name__)


class EMCoupling(BaseEMCoupling):
    def __init__(
        self,
        geometry: BaseGeometry,
        **state_params,
    ) -> None:
        super().__init__(geometry=geometry, **state_params)

        self.V_mech = dolfin.FunctionSpace(self.mech_mesh, "CG", 1)
        self.XS_mech = dolfin.Function(self.V_mech, name="XS_mech")
        self.XW_mech = dolfin.Function(self.V_mech, name="XW_mech")
        self.lmbda_mech = dolfin.Function(self.V_mech, name="lambda_mech")
        self.Zetas_mech = dolfin.Function(self.V_mech, name="Zetas_mech")
        self.Zetaw_mech = dolfin.Function(self.V_mech, name="Zetaw_mech")

        self.V_ep = dolfin.FunctionSpace(self.ep_mesh, "CG", 1)
        self.XS_ep = dolfin.Function(self.V_ep, name="XS_ep")
        self.XW_ep = dolfin.Function(self.V_ep, name="XW_ep")
        self.lmbda_ep = dolfin.Function(self.V_ep, name="lambda_ep")
        self.Zetas_ep = dolfin.Function(self.V_ep, name="Zetas_ep")
        self.Zetaw_ep = dolfin.Function(self.V_ep, name="Zetaw_ep")

    @property
    def coupling_type(self):
        return "fully_coupled_ORdmm_Land"

    @property
    def mech_mesh(self):
        return self.geometry.mechanics_mesh

    @property
    def ep_mesh(self):
        return self.geometry.ep_mesh

    def register_ep_model(self, solver):
        logger.debug("Registering EP model")
        self.ep_solver = solver
        self.vs = solver.solution_fields()[0]
        self.XS_ep, self.XS_ep_assigner = utils.setup_assigner(self.vs, 40)
        self.XW_ep, self.XW_ep_assigner = utils.setup_assigner(self.vs, 41)
        self.coupling_to_mechanics()
        logger.debug("Done registering EP model")

    def register_mech_model(self, solver: MechanicsProblem):
        logger.debug("Registering mech model")
        self.mech_solver = solver

        self.Zetas_mech = solver.material.active.Zetas_prev
        self.Zetaw_mech = solver.material.active.Zetaw_prev
        self.lmbda_mech = solver.material.active.lmbda_prev

        # Note sure why we need to do this for the LV?
        self.lmbda_mech.set_allow_extrapolation(True)
        self.Zetas_mech.set_allow_extrapolation(True)
        self.Zetaw_mech.set_allow_extrapolation(True)

        self.mechanics_to_coupling()
        logger.debug("Done registering EP model")

    def ep_to_coupling(self):
        logger.debug("Update mechanics")
        self.XS_ep_assigner.assign(self.XS_ep, utils.sub_function(self.vs, 40))
        self.XW_ep_assigner.assign(self.XW_ep, utils.sub_function(self.vs, 41))
        logger.debug("Done updating mechanics")

    def coupling_to_mechanics(self):
        logger.debug("Interpolate mechanics")
        self.XS_mech.interpolate(self.XS_ep)
        self.XW_mech.interpolate(self.XW_ep)
        logger.debug("Done interpolating mechanics")

    def mechanics_to_coupling(self):
        logger.debug("Interpolate EP")
        self.lmbda_ep.interpolate(self.lmbda_mech)
        self.Zetas_ep.interpolate(self.Zetas_mech)
        self.Zetaw_ep.interpolate(self.Zetaw_mech)
        logger.debug("Done interpolating EP")

    def coupling_to_ep(self):
        logger.debug("Update EP")
        logger.debug("Done updating EP")

    def solve_mechanics(self) -> None:
        self.mech_solver.solve()

    def solve_ep(self, interval: Tuple[float, float]) -> None:
        self.ep_solver.step(interval)

    def update_prev_mechanics(self):
        pass

    def update_prev_ep(self):
        self.ep_solver.vs_.assign(self.ep_solver.vs)

    def print_mechanics_info(self):
        total_dofs = self.mech_tate.function_space().dim()
        utils.print_mesh_info(self.mech_mesh, total_dofs)
        logger.info("Mechanics model")

    def print_ep_info(self):
        # Output some degrees of freedom
        total_dofs = self.vs.function_space().dim()
        logger.info("EP model")
        utils.print_mesh_info(self.ep_mesh, total_dofs)

    def cell_params(self):
        return self.ep_solver.ode_solver._model.parameters()
