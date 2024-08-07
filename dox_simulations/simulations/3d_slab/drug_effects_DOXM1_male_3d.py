# -*- coding: utf-8 -*-
# # Drug effects demo
#
# In this demo we show how to modulate the cell model with pharmacological effects
#
#

import pprint
from pathlib import Path

import dolfin
import simcardems

# Create configurations with custom output directory
here = Path(__file__).absolute().parent
outdir = here.parent.parent / "results/3DSlab/Results_Files/results_DOXM1_male_3D"

# Specify paths to the geometry that we will use
geometry_path = here.parent.parent / "data/geometries/big_3d_slab/slab.h5"
geometry_schema_path = here.parent.parent / "data/geometries/big_3d_slab/slab.json"

# Specify path to the file containing drug scaling factors
drug_factors_path = here.parent.parent / "data/drug_factors/DOX_FactorsM1.json"

# Specify path to the initial conditions for the cell model
#initial_conditions_path = here.parent.parent / "data/initial_conditions/DOX/initDOXbaseline_50beats.json"

# Specify path to the file containing population scaling factors
popu_factors_path = here.parent.parent / "data/population_factors/representative_male.json"

# The scaling factors in this file are applied to the corresponding ion currents as a modulator of the ion channel conductance. The example file reduces the sodium current to 10%.

config = simcardems.Config(
    outdir=outdir,
    geometry_path=geometry_path,
    geometry_schema_path=geometry_schema_path,
    coupling_type = "fully_coupled_ORdmm_Land",
    T=51000,
    drug_factors_file=drug_factors_path,
    popu_factors_file = popu_factors_path,
    load_state = True,
    #cell_init_file = initial_conditions_path,
)

# Print current configuration
pprint.pprint(config.as_dict())

runner = simcardems.Runner(config)
runner.solve(T=config.T, save_freq=config.save_freq, show_progress_bar=True)


# This will create the output directory `results_drug_demo` with the following output
#
# ```
# results_simple_demo
# ├── results.h5
# ├── state.h5
# ```
# The file `state.h5` contains the final state which can be used if you want use the final state as a starting point for the next simulation.
# The file `results.h5` contains the Displacement ($u$), active tension ($T_a$), voltage ($V$) and calcium ($Ca$) for each time step.
# We can also plot the traces using the postprocess module
#
#

simcardems.postprocess.plot_state_traces(outdir.joinpath("results.h5"), "center")

#plot_state_traces = plots only trace, not needed for our analysis

#
# Here we also specify that we want the trace from the center of the slab
#

# This will create a figure in the output directory called `state_traces.png` which in this case is shown in {numref}`Figure {number} <drug_demo_state_traces>` we see the resulting state traces.
#
# ```{figure} figures/drug_demo_state_traces.png
# ---
# name: drug_demo_state_traces
# ---
# Traces of the stretch ($\lambda$), the active tension ($T_a$), the membrane potential ($V$) and the intercellular calcium concentration ($Ca$) at the center of the geometry.
# ```

#
# We can also save the output to xdmf-files that can be viewed in Paraview
#

simcardems.postprocess.make_xdmffiles(outdir.joinpath("results.h5"))
#will be used later for paraview analysis

#
# The `xdmf` files are can be opened in [Paraview](https://www.paraview.org/download/) to visualize the different variables.
#
