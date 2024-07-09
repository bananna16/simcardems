from pathlib import Path
import matplotlib.pyplot as plt
import simcardems
import numpy as np

here = Path(__file__).absolute().parent
path_results = here.parent / "results/figures"


# Function with array of output directories and path to results and labels as input: loops through the arrays

def plot_multiple_state_traces(
    outdir_arr,
    label_arr,
    path_results,
    reduction: str = "center",
):
    
    fig, axs = plt.subplots(2, 2, figsize=(10, 8), sharex=True)

    for outdir, label in zip(outdir_arr, label_arr):
        loader = simcardems.DataLoader(outdir / "results.h5")
        values = simcardems.postprocess.extract_traces(loader, reduction=reduction)
        times = np.array(loader.time_stamps, dtype=float)

        for i, (group, key) in enumerate(
            (("ep", "lambda"), ("mechanics", "Ta"), ("ep", "V"), ("ep", "Ca")),
        ):
            ax = axs.flatten()[i]
            try:
                y = values[group][key]
            except KeyError:
                # Just skip it
                continue
            ax.plot(times, y, label = label)
            if key == "lambda":
                ax.set_title(r"$\lambda$")
                #ax.set_ylim(min(0.9, min(y)), max(1.1, max(y)))
            else:
                ax.set_title(key)
            #ax.grid()
            ax.grid(True, which='both', linestyle='--', linewidth=0.5)

    # Add legends to all subplots
    for ax in axs.flatten():
        ax.legend()

    axs[1, 0].set_xlabel("Time [ms]")
    axs[1, 1].set_xlabel("Time [ms]")
    axs[0, 0].set_ylabel("Active stretch")
    axs[0, 1].set_ylabel("Active tension (kPa)")
    axs[1, 0].set_ylabel("Voltage (mV)")
    axs[1, 1].set_ylabel(r"Intracellular calcium concentration ($\mu$M)")

    fig.savefig(path_results.joinpath(f"state_traces_center_loop.png"), dpi=300)

# Call function to plot multiple simulation results in one plot
outdir_arr = [here.parent / "demos/results_DOX_M1", here.parent / "demos/results_healthy"]
label_arr = ["DOX", "Healthy"]
reduction =  "center"

plot_multiple_state_traces(outdir_arr, label_arr, path_results, "center")
