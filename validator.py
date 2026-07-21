import pandas as pd
import numpy as np


def run_validation_suite(filepath):
    print("=" * 50)
    print(f"    AEROSPACE DATA VALIDATION SUITE: {filepath}")
    print("=" * 50)

    try:
        data = pd.read_csv(filepath)
        data.columns = data.columns.str.strip()
    except Exception as e:
        print(f"[FATAL] Failed to load file: {e}")
        return False

    failures = 0
    warnings = 0

    ground_tolerance = -0.1
    tunneling_incidents = data[data['Altitude'] < ground_tolerance]
    if not tunneling_incidents.empty:
        print(f"[FAIL] Ground Tunneling Detected!")
        print(
            f"    -> Rocket fell below ground level {len(tunneling_incidents)} times.")
        print(
            f"    -> Worst offense: {tunneling_incidents['Altitude'].min():.2f} meters.")
        failures += 1
    else:
        print("[PASS] Ground Integrity: No ground tunneling detected.")

    negative_fuel = data[data['FuelMass'] < 0]
    if not negative_fuel.empty:
        print(f"[FAIL] Law of Mass Conservation Violated!")
        print(
            f"    -> Fuel mass dropped below zero {len(negative_fuel)} times.")
        print(
            f"    -> Lowest fuel recorded: {negative_fuel['FuelMass'].min():.2f} kg.")
        failures += 1
    else:
        print("[PASS] Mass Conservation: Fuel mass remained non-negative.")

    c = 299792458  # meters per second (speed of light)
    relativistic_incidents = data[data['Velocity'].abs() > c]
    if not relativistic_incidents.empty:
        print(f"[FAIL] Special Relativity Broken!")
        print(f"    -> Rocket exceeded the speed of light.")
        failures += 1
    else:
        print("[PASS] Relativistic Limits: Flight speeds remained sub-luminal.")

    dt = data['Time'].diff()
    dv = data['Velocity'].diff()
    calculated_accel = dv / dt
    max_g = (calculated_accel.abs().max()) / 9.81

    if max_g > 50.0:
        print(f"[WARN] Extreme G-Forces Detected!")
        print(f"    -> Peak acceleration reached {max_g:.1f} Gs.")
        print(f"    Check your engine thrust or time step (dt) resolution.")
        warnings += 1
    else:
        print(
            f"[PASS] Structural Load: Peak acceleration was safe ({max_g:.1f} Gs).")

    time_deltas = data['Time'].diff().dropna()
    if (time_deltas <= 0).any():
        print("[FAIL] Time Continuity Broken!")
        print("     -> Detected non-chronological or duplicate timestamps.")
        failures += 1
    else:
        print("[PASS] Time Continuity: Timeline flows forward normally.")

    print('-' * 50)
    print(f"Validation Finished: {failures} Failures, {warnings} Warnings.")
    print("=" * 50)

    return failures == 0


run_validation_suite('trajectory.csv')
