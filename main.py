import time

def main():
    print("\nAdaptive Cruise Control Simulation Started:\n ")

    position=0.0
    dt=0.02 #50 Hz
    Velocity = 5.0

    for step in range(1,101):

        position+=Velocity*dt
        print(f"Step {step}--> Position= {position:.3f}m")
        time.sleep(dt)

    print("\nSimulation Finished\n")

if __name__=="__main__":
    main()

import time

def main():

    print("\nACC Simulation for Two Vehicles Started\n")

    # -------------------------
    # Simulation parameters
    # -------------------------
    dt = 0.02      # 50 Hz control loop
    steps = 150

    # -------------------------
    # Target Vehicle (front car)
    # -------------------------
    target_position = 30.0     # meters ahead
    target_velocity = 8.0      # m/s

    # -------------------------
    # Controlled Vehicle (our car)
    # -------------------------
    controlled_position = 0.0
    controlled_velocity = 5.0

    for step in range(1, steps + 1):

        # Target vehicle slows down suddenly
        if step > 80:
            target_velocity = 4.0

        # Update positions
        target_position += target_velocity * dt
        controlled_position += controlled_velocity * dt

        # Distance between vehicles
        distance = target_position - controlled_position

        print(
            f"Step {step:03d}   "
            f"Distance: {distance:6.2f} m   "
            f"Target Pos: {target_position:6.2f} m   "
            f"Controlled Pos: {controlled_position:6.2f} m"
        )

        time.sleep(dt)

    print("\nSimulation Ended\n")


if __name__ == "__main__":
    main()