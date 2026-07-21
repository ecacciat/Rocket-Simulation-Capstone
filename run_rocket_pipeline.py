import os
import sys
import subprocess


def run_step(command, description):
    """Executes a terminal command, streams output, and checks for errors."""
    print(f"\n=========================================")
    print(f"    [PIPELINE] {description}")
    print(f"========================================")

    result = subprocess.run(command, shell=True)

    if result.returncode != 0:
        print(
            f"\n[FATAL ERROR] Step failed: '{description}' (Exit code: {result.returncode})")
        sys.exit(result.returncode)

    print(f"[SUCCESS] {description} complete.")


def main():
    cpp_source = "rocket_trajectory.cpp"

    if sys.platform.startswith("win"):
        executable = "rocket_sim.exe"
        run_command = executable
    else:
        executable = "./rocket_sim"
        run_command = executable

    compile_cmd = f"g++ -O3 {cpp_source} -o {executable}"
    run_step(compile_cmd, "Compiling C++ Physics Core (g++)")

    run_step(run_command, "Running Rocket Physics Simulation")

    validate_cmd = f'"{sys.executable}" validator.py'
    run_step(validate_cmd, "Executing Physics Data Validation Suite")

    plot_cmd = f'"{sys.executable}" rocket_trajectory.py'
    run_step(plot_cmd, "Generating Trajectory & Phase Plots")

    print("\n==============================================")
    print("     FULL PIPELINE EXECUTION COMPLETED SUCCESSFULLY!")
    print("==============================================\n")


if __name__ == "__main__":
    main()
