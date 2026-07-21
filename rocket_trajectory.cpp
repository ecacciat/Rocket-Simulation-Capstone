#include <iostream>
#include <string>
#include <cmath>
#include <fstream>

class rocket
{
public:
    std::string name;
    double fuel_mass;
    double rocket_thrust;
    double rocket_mass;
    double fuel_burn;

    rocket(std::string rocket_name, double dry_mass, double initial_fuel, double thrust, double burn_rate)
    {
        name = rocket_name;
        rocket_mass = dry_mass;
        fuel_mass = initial_fuel;
        rocket_thrust = thrust;
        fuel_burn = burn_rate;

        std::cout << "[SYSTEM] " << name << " beginning launch..." << std::endl;
    }
    ~rocket()
    {
        std::cout << "[SYSTEM] " << name << " has reached end of trajectory." << std::endl;
    }
    double get_total_mass()
    {
        return fuel_mass + rocket_mass;
    }
    bool is_burning(double current_time)
    {
        if (fuel_mass > 0)
        {
            return true;
        }
        else
        {
            return false;
        }
    }
};

int main()
{
    double time = 0.0;
    double dt = 0.01;
    double velocity = 0.0;
    double altitude = 0.001;
    double acceleration = 0.0;

    std::cout << "---Trajectory Simulator Architecture Test---" << std::endl;
    rocket star_sailor("Artemis X", 5000.0, 50000.0, 750000.0, 250.0);
    star_sailor.get_total_mass();

    if (star_sailor.is_burning(0.0))
    {
        std::cout << "Engine Status: ACTIVE PROPULSION MOTION" << std::endl;
    }

    std::ofstream data_file("trajectory.csv");
    data_file << "Time,Altitude,Velocity,FuelMass\n";
    std::cout << "DEBUG: Fuel Mass right before loop is: " << star_sailor.fuel_mass << "kg" << std::endl;

    while (altitude >= 0.0 || time < dt)
    {
        double current_thrust = 0.0;

        if (star_sailor.is_burning(time))
        {
            current_thrust = star_sailor.rocket_thrust;
            star_sailor.fuel_mass -= star_sailor.fuel_burn * dt;

            if (star_sailor.fuel_mass < 0.0)
            {
                star_sailor.fuel_mass = 0.0;
            }
        }

        double total_mass = star_sailor.get_total_mass();

        double rho = 1.225 * std::exp(-altitude / 8500.0);
        double cd = 0.5;
        double area = 0.2;
        double drag = 0.5 * rho * (velocity * velocity) * cd * area;

        if (velocity < 0)
        {
            acceleration = (current_thrust - (total_mass * 9.81) + drag) / total_mass;
        }
        else
        {
            acceleration = (current_thrust - (total_mass * 9.81) - drag) / total_mass;
        }
        velocity = velocity + (acceleration * dt);
        altitude = altitude + (velocity * dt);
        time += dt;

        if (std::fmod(time, 1.0) < dt)
        {
            std::cout << "Time elapsed: " << time << " seconds." << std::endl;
            std::cout << "Altitude achieved: " << altitude << " meters." << std::endl;
            std::cout << "remaining fuel mass: " << star_sailor.fuel_mass << " kg." << std::endl;
            std::cout << "----------------------------------------------" << std::endl;
        }
        data_file << time << "," << altitude << "," << velocity << "," << star_sailor.fuel_mass << "\n";
    }
    std::cout << "--- Trajectory Complete ---" << std::endl;
    data_file.close();
    std::cout << "[SYSTEM] Trajectory data successfully saved to trajectory.csv" << std::endl;
    return 0;
}