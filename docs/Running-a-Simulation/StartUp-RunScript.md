## StartUp with an run-script
The simulation startup with a run-script allows testing of multiple parameters for a given simulation without executing every service singly.
This allows an easy way to test the simulation and execute simulation studies on it.

Now we can start the run-script without manually starting any container:
  * set your current working directory to `$CROWNET_HOME/crownet/simulations/testSim`
  * run the run-script with following arguments:
   `(crownet_user) python3 run_script.py --opp.-c sumo_crossing_peds_cars --override-host-config --create-sumo-container`

If you want more examples of how the run_script is configured for the simulation studies, check out the [guiding_crowds.yaml file in the fingerprint tests](https://sam-dev.cs.hm.edu/rover/crownet/-/blob/master/crownet/tests/fingerprint/guiding_crowds.yml).

# Possible configurations
Be aware that there are multiple configurations, and they are mutually exclusive, meaning you can't run an omnet simulation with both vadere and sumo at the same time.
The possible configurations are as follows:
* OmnetSumo = OMNET & SUMO
* OmnetVadere = OMNET & VADERE
* OmnetVadereControl = OMNET & VADERE &CONTROL
* VadereControl = VADERE & CONTROL