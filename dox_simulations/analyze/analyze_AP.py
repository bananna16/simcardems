from pathlib import Path
import matplotlib.pyplot as plt
import simcardems
import numpy as np
import json
import ap_features as apf

# Define pathes here
here = Path(__file__).absolute().parent
folder = here.parent 
results_folder =  folder / "results"
num_models = 6

# Generate dictionary for results
results = {}
for PoMm in range(1, num_models + 1):
    #print(f"Analyzing model {PoMm}")
    #results_file = population_folder.joinpath("results.h5")

    # workaround for healthy vs. DOX
    if PoMm == 1:
        print(f"Analyzing Baseline (model {PoMm})")
        results_file = results_folder/"SteadyStateSingleBeat/Results_Files/results_healthy_baseline_steadystate/results.h5"
        #print(results_file)

    elif PoMm == 2:
        print(f"Analyzing Female Healthy (model {PoMm})")
        results_file = results_folder / "SteadyStateSingleBeat/Results_Files/results_healthy_female_steadystate/results.h5"
        #print(results_file)
        
    elif PoMm == 3:
        print(f"Analyzing Male Healthy (model {PoMm})")
        results_file = results_folder / "SteadyStateSingleBeat/Results_Files/results_healthy_male_steadystate/results.h5"
        #print(results_file)
        
    elif PoMm == 4:
        print(f"Analyzing Baseline DOX (model {PoMm})")
        results_file = results_folder / "SteadyStateSingleBeat/Results_Files/results_DOXM1_baseline_steadystate/results.h5"
        #print(results_file)
        
    elif PoMm == 5:
        print(f"Analyzing Female DOX (model {PoMm})")
        results_file = results_folder / "SteadyStateSingleBeat/Results_Files/results_DOXM1_female_steadystate/results.h5"
        #print(results_file)
        
    elif PoMm == 6:
        print(f"Analyzing Male DOX (model {PoMm})")
        results_file = results_folder / "SteadyStateSingleBeat/Results_Files/results_DOXM1_male_steadystate/results.h5"

    if not results_file.is_file():
        #results_file = population_folder.joinpath(f"m{PoMm}/results.h5")
        if not results_file.is_file():
            raise FileNotFoundError(f"File {results_file} does not exist")

    loader = simcardems.DataLoader(results_file)
    results[f"m{PoMm}"] = simcardems.postprocess.extract_traces(loader=loader, reduction="center", names=[("ep", "V"),("ep", "Ca")])


# Analyze data
outdir = results_folder / "AllModels"
print("------------------------------------------")
print("Start analysis of results")
#biomarker_dict = simcardems.postprocess.get_biomarkers(results, outdir, num_models)
print("------------------------------------------")
print("Start plotting")
#simcardems.postprocess.plot_population(results, outdir , num_models)

# Extract time and voltage data
times_basehealthy = np.array(results["m1"]["time"], dtype=float)
voltage_basehealthy = np.array(results["m1"]["ep"]["V"], dtype=float)
times_femalehealthy = np.array(results["m2"]["time"], dtype=float)
voltage_femalehealthy = np.array(results["m2"]["ep"]["V"], dtype=float)
times_malehealthy = np.array(results["m3"]["time"], dtype=float)
voltage_malehealthy = np.array(results["m3"]["ep"]["V"], dtype=float)
times_basedox = np.array(results["m4"]["time"], dtype=float)
voltage_basedox = np.array(results["m4"]["ep"]["V"], dtype=float)
times_femaledox = np.array(results["m5"]["time"], dtype=float)
voltage_femaledox = np.array(results["m5"]["ep"]["V"], dtype=float)
times_maledox = np.array(results["m6"]["time"], dtype=float)
voltage_maledox = np.array(results["m6"]["ep"]["V"], dtype=float)

#Extract Calcium
calcium_basehealthy = np.array(results["m1"]["ep"]["Ca"], dtype=float)
calcium_femalehealthy = np.array(results["m2"]["ep"]["Ca"], dtype=float)
calcium_malehealthy = np.array(results["m3"]["ep"]["Ca"], dtype=float)
calcium_basedox = np.array(results["m4"]["ep"]["Ca"], dtype=float)
calcium_femaledox = np.array(results["m5"]["ep"]["Ca"], dtype=float)
calcium_maledox = np.array(results["m6"]["ep"]["Ca"], dtype=float)

# Align the DOX time to start at 0
#times_dox_aligned = times_dox - times_dox.min()

# Plot the data
fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 12))

# Increase font size for labels and ticks
label_fontsize = 16
tick_fontsize = 14
line_thickness = 2.5
legend_size = 20


# Voltage vs. Time
#ax1.plot(times_basehealthy, voltage_basehealthy, label="Baseline", color="blue", linewidth=line_thickness)
ax1.plot(times_femalehealthy-50000, voltage_femalehealthy, label="Female", color="red", linewidth=line_thickness)
#ax1.plot(times_malehealthy-50000, voltage_malehealthy, label="Male", color="green", linewidth=line_thickness)
#ax1.plot(times_basedox-50000, voltage_basedox, label="Baseline+DOX", color="orange", linewidth=line_thickness)
#ax1.plot(times_maledox-50000, voltage_maledox, label="Male DOX", color="purple", linewidth=line_thickness)
ax1.plot(times_femaledox-50000, voltage_femaledox, label="Female DOX", color="magenta", linewidth=line_thickness)

ax1.set_xlabel("Time (ms)", fontsize=label_fontsize)
ax1.set_ylabel("Voltage (mV)", fontsize=label_fontsize)
#ax1.set_title("Voltage Traces", fontsize=label_fontsize)
#ax1.legend(fontsize=legend_size)
ax1.tick_params(axis='both', which='major', labelsize=tick_fontsize)
#ax1.set_xlim(0, 600)  # Set x-axis limits

# Calcium vs. Time
#ax2.plot(times_basehealthy, calcium_basehealthy*1000, label="Baseline", color="blue", linewidth=line_thickness)
ax2.plot(times_femalehealthy-50000, calcium_femalehealthy*1000, label="Female", color="red", linewidth=line_thickness)
#ax2.plot(times_malehealthy-50000, calcium_malehealthy*1000, label="Male", color="green", linewidth=line_thickness)
#ax2.plot(times_basedox-50000, calcium_basedox*1000, label="Baseline+DOX", color="orange", linewidth=line_thickness)
#ax2.plot(times_maledox-50000, calcium_maledox*1000, label="Male DOX", color="purple", linewidth=line_thickness)
ax2.plot(times_femaledox-50000, calcium_femaledox*1000, label="Female DOX", color="magenta", linewidth=line_thickness)

ax2.set_xlabel("Time (ms)", fontsize=label_fontsize)
ax2.set_ylabel(r"Calcium (µM)", fontsize=label_fontsize)
#ax2.set_title("Calcium Traces", fontsize=label_fontsize)
ax2.legend(fontsize=legend_size)
ax2.tick_params(axis='both', which='major', labelsize=tick_fontsize)
#ax2.set_xlim(0, 600)  # Set x-axis limits


plt.tight_layout()
plt.show()

# Save the plot
outdir = results_folder / "PlotsforPresentation"
outdir.mkdir(parents=True, exist_ok=True)
fig.savefig(outdir.joinpath("FemaleBaseDOX_voltagecalcium_traces_comparison.png"), dpi=300)
fig.savefig(outdir.joinpath("FemaleBaseDOX_voltagecalcium_traces_comparison.svg"), format="svg")

print("Plotting completed and files saved.")


# Compare healthy vs. DOX
##outfile = outdir / "biomarkers_PoMcontrol.json"
#print("------------------------------------------")
#print("Start analyis of changes healthy vs. DOX")
#with open(outfile) as f:
    #biomarkers = simcardems.postprocess.numpyfy(json.load(f))
#biomarker_comparison = {}
#change_DOX_dict = {}
#for biomarker in biomarker_dict["m1"].keys(): #loop through all biomarkers
    #biomarker_comparison[biomarker] = []
    #change_DOX_dict[biomarker] = []
    #for PoMm in biomarker_dict.keys():
    #    biomarker_comparison[biomarker].append(biomarker_dict[PoMm][biomarker]) #store data from all models for the current biomarker
    #print("{} healthy: {}".format(biomarker, biomarker_dict["m1"][biomarker]))
    #print("{} DOX: {}".format(biomarker, biomarker_dict["m2"][biomarker]))
    #change_DOX_dict[biomarker] = biomarker_dict["m2"][biomarker] / biomarker_dict["m1"][biomarker]
    #change_DOX_dict[biomarker] = np.round((change_DOX_dict[biomarker]-1) *100) # convert to increase / decrease in % and round
    #if np.isnan(change_DOX_dict[biomarker]):
       # print("Change for {} from healthy to DOX: {:+}% ".format(biomarker, change_DOX_dict[biomarker]))
    #else:
       # print("Change for {} from healthy to DOX: {:+}% ".format(biomarker, int(change_DOX_dict[biomarker])))

#with open(outdir.joinpath("changes_biomarkers_PoMcontrol.json"), "w") as f:
        #json.dump(change_DOX_dict, f)






""" 
PREVIOUS VERSION TO PLOT FUNCTION --> DO NOT DELETE YET 
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

"""
