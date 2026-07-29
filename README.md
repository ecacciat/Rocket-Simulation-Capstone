This collection of rocket simulation files is an independent capstone project that I completed to become
more comfortable with applying my academic physics knowledge to real, theorized programming projects of 
my own making with the hope of more in the future! In this repository, you will find the foundational 
physics engine for the system, made in C++ (rocket_trajectory.cpp). You will also find three Python files: 
the physics validator (validator.py), the visuals creator file (rocket_trajectory.py), and the pipeline file 
that runs through each step with one press of a button (run_rocket_pipeline.py). 

To initialize the flight conditions for your rocket, you will need its body's mass, fuel mass, thrust, and 
fuel burn rate. The rocket's drag is calculated using the follow equation with air density (rho), current 
velocity (v), drag coefficient (cd), and its area: drag = 0.5 * rho * v^2 * cd * area. 
The physics engine calculates the rocket's velocity (v) and acceleration (a) using basic kinematic 
equations with a set change in time (dt): v = v0 + (a * dt), and the rocket's calculated acceleration will  
depend on the direction of its velocity, a = (current_thrust - (total_mass * 9.81) +/- drag) / total_mass. 

The physics validator runs through several validation sequences including a tunneling detection test, 
negative fuel mass test, detections for relativity issues, g-force analysis, and a search for time 
continuity errors. The tunneling test analyzes whether the rocket fell below the ground altitude 
tolerance, the fuel mass test simply prints whether the fuel mass drops below zero, the relativity test 
makes sure that the rocket does not exceed the speed of light, peak acceleration of the rocket is looked 
at, and the last step is looking at if there are any duplicate timestamps. 

For the C++ physics file, it is compiled using g++ with a -O3 optimization flag. 

To help the master pipeline script (run_rocket_pipeline.py) run on multiple platforms, 
sys.platform was used to detect what operating system the user has, while managing binary extensions. 

For efficiency optimization, Python's subprocess system was put into place to prevent any errors in 
validation scripts from using illogical outputs. 

C++ was specifically used for its propensity at high functioning mathematical equations, while Python 
was used to handle graphing the data using matplotlib. This simulation draws on live data from the csv
file in order to create two different graphs: one for the rocket's position (Altitude vs. Time), and its 
flight dynamics (Velocity vs. Altitude). Flight milestones can be seen on the graphs, such as when the 
rocket reaches its apogee and begins descent. 

After the script is run, the data visuals will automatically be saved into the coding workspace in 
.pdf/.png figures. 
