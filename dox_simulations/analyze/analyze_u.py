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
        results_file = results_folder / "3DSlab/Results_Files/results_healthy_female_3D/results.h5"
        #print(results_file)
        
    elif PoMm == 3:
        print(f"Analyzing Male Healthy (model {PoMm})")
        results_file = results_folder / "3DSlab/Results_Files/results_healthy_male_3D/results.h5"
        #print(results_file)
        
    elif PoMm == 4:
        print(f"Analyzing Baseline DOX (model {PoMm})")
        results_file = results_folder / "SteadyStateSingleBeat/Results_Files/results_DOXM1_baseline_steadystate/results.h5"
        #print(results_file)
        
    elif PoMm == 5:
        print(f"Analyzing Female DOX (model {PoMm})")
        results_file = results_folder / "3DSlab/Results_Files/results_DOXM1_female_3D/results.h5"
        #print(results_file)
        
    elif PoMm == 6:
        print(f"Analyzing Male DOX (model {PoMm})")
        results_file = results_folder / "3DSlab/Results_Files/results_DOXM1_male_3D/results.h5"

    if not results_file.is_file():
        #results_file = population_folder.joinpath(f"m{PoMm}/results.h5")
        if not results_file.is_file():
            raise FileNotFoundError(f"File {results_file} does not exist")

    loader = simcardems.DataLoader(results_file)
    results[f"m{PoMm}"] = simcardems.postprocess.extract_traces(loader=loader, reduction="center", names=[("mechanics", "u")])


# Analyze data
outdir = results_folder / "AllModels"
print("------------------------------------------")
print("Start analysis of results")
#biomarker_dict = simcardems.postprocess.get_biomarkers(results, outdir, num_models)
print("------------------------------------------")
print("Start plotting")
#simcardems.postprocess.plot_population(results, outdir , num_models)

# Extract time and voltage data
#times_basehealthy = np.array(results["m1"]["time"], dtype=float)
#voltage_basehealthy = np.array(results["m1"]["mechanics"]["u"], dtype=float)
times_femalehealthy = np.array(results["m2"]["time"], dtype=float)
displacement_femalehealthy = np.array(results["m2"]["mechanics"]["u"], dtype=float)
times_malehealthy = np.array(results["m3"]["time"], dtype=float)
displacement_malehealthy = np.array(results["m3"]["mechanics"]["u"], dtype=float)
#times_basedox = np.array(results["m4"]["time"], dtype=float)
#voltage_basedox = np.array(results["m4"]["mechanics"]["u"], dtype=float)
times_femaledox = np.array(results["m5"]["time"], dtype=float)
displacement_femaledox = np.array(results["m5"]["mechanics"]["u"], dtype=float)
times_maledox = np.array(results["m6"]["time"], dtype=float)
displacement_maledox = np.array(results["m6"]["mechanics"]["u"], dtype=float)

# Align the DOX time to start at 0
#times_dox_aligned = times_dox - times_dox.min()

# Plot the data
fig, (ax1) = plt.subplots(1, 1, figsize=(10, 12))

# Increase font size for labels and ticks
label_fontsize = 16
tick_fontsize = 14
line_thickness = 2.5
legend_size = 20


# displacement vs. Time
#ax1.plot(times_basehealthy, voltage_basehealthy, label="Baseline", color="blue", linewidth=line_thickness)
#ax1.plot(times_femalehealthy, displacement_femalehealthy, label="Female", color="red", linewidth=line_thickness)
ax1.plot(times_femalehealthy, displacement_femalehealthy[:,0], label="Female dx", color="red", linewidth=line_thickness, linestyle='-')
ax1.plot(times_femalehealthy, displacement_femalehealthy[:,1], label="Female dy", color="red", linewidth=line_thickness, linestyle='--')
ax1.plot(times_femalehealthy, displacement_femalehealthy[:,2], label="Female dz", color="red", linewidth=line_thickness, linestyle=':')
#ax1.plot(times_basedox, displacement_basedox, label="Baseline+DOX", color="orange", linewidth=line_thickness)
#ax1.plot(times_maledox, displacement_maledox[:,0], label="Male DOX dx", color="purple", linewidth=line_thickness, linestyle='-')
#ax1.plot(times_maledox, displacement_maledox[:,1], label="Male DOX dx", color="purple", linewidth=line_thickness, linestyle='--')
#ax1.plot(times_maledox, displacement_maledox[:,2], label="Male DOX dz", color="purple", linewidth=line_thickness, linestyle=':')
#ax1.plot(times_femaledox, displacement_femaledox, label="Female DOX", color="magenta", linewidth=line_thickness)
ax1.plot(times_femaledox, displacement_femaledox[:,0], label="Female DOX dx", color="magenta", linewidth=line_thickness, linestyle='-')
ax1.plot(times_femaledox, displacement_femaledox[:,1], label="Female DOX dy", color="magenta", linewidth=line_thickness, linestyle='--')
ax1.plot(times_femaledox, displacement_femaledox[:,2], label="Female DOX dz", color="magenta", linewidth=line_thickness, linestyle=':')

ax1.set_xlabel("Time (ms)", fontsize=label_fontsize)
ax1.set_ylabel("Displacement (..)", fontsize=label_fontsize)
#ax1.set_title("Voltage Traces", fontsize=label_fontsize)
ax1.legend(fontsize=legend_size)
ax1.tick_params(axis='both', which='major', labelsize=tick_fontsize)
#ax1.set_xlim(0, 600)  # Set x-axis limits

# Calcium vs. Time
#ax2.plot(times_basehealthy, calcium_basehealthy*1000, label="Baseline", color="blue", linewidth=line_thickness)
#ax2.plot(times_femalehealthy-50000, calcium_femalehealthy*1000, label="Female", color="red", linewidth=line_thickness)
#ax2.plot(times_malehealthy-50000, calcium_malehealthy*1000, label="Male", color="green", linewidth=line_thickness)
#ax2.plot(times_basedox-50000, calcium_basedox*1000, label="Baseline+DOX", color="orange", linewidth=line_thickness)
#ax2.plot(times_maledox-50000, calcium_maledox*1000, label="Male DOX", color="purple", linewidth=line_thickness)
#ax2.plot(times_femaledox-50000, calcium_femaledox*1000, label="Female DOX", color="magenta", linewidth=line_thickness)

#ax2.set_xlabel("Time (ms)", fontsize=label_fontsize)
#ax2.set_ylabel(r"Calcium (µM)", fontsize=label_fontsize)
#ax2.set_title("Calcium Traces", fontsize=label_fontsize)
#ax2.legend(fontsize=legend_size)
#ax2.tick_params(axis='both', which='major', labelsize=tick_fontsize)
#ax2.set_xlim(0, 600)  # Set x-axis limits


plt.tight_layout()
plt.show()

# Save the plot
outdir = results_folder / "PlotsforPresentation"
outdir.mkdir(parents=True, exist_ok=True)
fig.savefig(outdir.joinpath("FemaleDOX_displacement_traces_comparison.png"), dpi=300)
fig.savefig(outdir.joinpath("FemaleDOX_displacement_traces_comparison.svg"), format="svg")

print("Plotting completed and files saved.")


# Analyze displacement
d = {}
u_norm = np.linalg.norm(displacement_femaledox, axis=1)
ux, uy, uz = displacement_femaledox.T
time = times_femaledox
for name, arr in zip(["norm", "x", "y", "z"], [u_norm, ux, uy, uz]):
    d[f"max_displacement_{name}"] = np.max(arr)
    d[f"min_displacement_{name}"] = np.min(arr)
    d[f"time_to_max_displacement_{name}"] = apf.features.time_to_peak(
        y=arr,
        x=time,
        )
    d[f"time_to_min_displacement_{name}"] = apf.features.time_to_peak(
        y=-arr,
        x=time,
    )
with open(outdir.joinpath("displacement_feature_female_dox.json"), 'w') as json_file:
    json.dump(d, json_file, indent=4)

d = {}
u_norm = np.linalg.norm(displacement_femalehealthy, axis=1)
ux, uy, uz = displacement_femalehealthy.T
time = times_femalehealthy
for name, arr in zip(["norm", "x", "y", "z"], [u_norm, ux, uy, uz]):
    d[f"max_displacement_{name}"] = np.max(arr)
    d[f"min_displacement_{name}"] = np.min(arr)
    d[f"time_to_max_displacement_{name}"] = apf.features.time_to_peak(
        y=arr,
        x=time,
        )
    d[f"time_to_min_displacement_{name}"] = apf.features.time_to_peak(
        y=-arr,
        x=time,
    )
with open(outdir.joinpath("displacement_feature_female_healthy.json"), 'w') as json_file:
    json.dump(d, json_file, indent=4)