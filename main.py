import time

def main():

    print("\nACC Simulation Started (Day 3: Safety Rule)\n")

    # Simulation parameters
    dt = 0.02     # 50 Hz
    steps = 150

    # Safety parameters
    max_acc = 1.5
    max_brake = -3.0
    safe_distance = 15.0

    # Target Vehicle
    target_position = 30.0
    target_velocity = 8.0

    # Controlled Vehicle
    controlled_position = 0.0
    controlled_velocity = 6.0
    controlled_acc = 0.0

    for step in range(1, steps + 1):

        # Target vehicle slows down
        if step > 120:
            target_velocity = 4.0

        # Update target vehicle
        target_position += target_velocity * dt

        # Distance between vehicles
        distance = target_position - controlled_position

        # Safety Rule (ACC logic)
        if distance < safe_distance:
            controlled_acc = max_brake
        else:
            controlled_acc = max_acc

        # Update controlled vehicle
        controlled_velocity += controlled_acc * dt

        if controlled_velocity < 0:
            controlled_velocity = 0

        controlled_position += controlled_velocity * dt

        print(
            f"Step {step:03d} | "
            f"Distance: {distance:.2f} m | "
            f"Target Pos: {target_position:.2f} m | "
            f"Ctrl Vel: {controlled_velocity:.2f} m/s | "
            f"Ctrl Acc: {controlled_acc:.2f} m/s²"
        )

        time.sleep(dt)

    print("\nSimulation Ended\n")


if __name__ == "__main__":
    main()
