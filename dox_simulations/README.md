### dox_simulations
This folder contains all the scripts and data used during the SSCP Project 2024 for the project **"Sex-Specific Effects of Doxorubicin on Cardiac Electromechanical Function: A Simulation-Based Study​"** by Anna Qi, Jule Bender, Hannah Zukowski​ and project Mentor Hermenegild Arevalo​.

To run a simulation: 

1. Start Docker 
2. Open the simulation folder and select between 3d_slab (5mmx2mmx1mm) to analyze contraction and small_2d_slab (1nm x 1nm x 1nm) to reach steady state.
3. Open python script to specify the following inputs: 
geometry_path -- specifies which geometry to use, find goemetry files in data>geometries
drug_factors_path -- specifies which drug factors, find drug factors files in data>drug_factors
popu_factors_path -- specifies which population (male/female/baseline), find population factors in data>population_factors
initial_conditions_path -- use if you would like to start from steady state (or a specified initial conditions .json file), find in data>initial_conditions 
Outdir -- specify where to save the results 

In Config : specify which parameters to use, set time to desired time (CL = 1000, ex: if you want to run for 2 beats T = 2000)
To start from previous state.h file (or a state from a previous simulation), set load_state=True and put state.h and state.json files into Outdir folder 

For post-processing, the plot_state_traces will plot the last beat at the center of the mesh. 
Make_xdmffiles will make .xdmf files for each parameter that can be visualized in paraview 

4. Run python script through docker 

To analyze simulation: 

1. Open analyze folder -- always specify paths for results.h files before running any analysis code! 
Current scripts: 
- analyze_AP.py : this script will analyze a single action potential and plot the voltage vs time trace and calcium transient 
- analyze_steadystate.py : this script will analyze for steady state, it will calculate the APD90 of each beat in the output file and plot voltage vs time and APD90 vs time 
- analyze_U.py : will analyze the contraction, use this on the big 3D tissue slab, will export and print relevant contraction biomarkers 
- analyze.py : this will give the biomarkers for a small 2d slab simulation, it will also calculate the changes between baseline and DOX cases 
- movie_example>paraview_generate_ep_em_movie.py : this file will take the xdmf output files and generate a movie in paraview, this script needs to be run from python shell in paraview 
