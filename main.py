import time

def main():
    print("\nACC Simulation Started (Day 4: Smooth Proportional Control)\n")

    # Simulation parameters
    dt = 0.02      # 50 Hz
    steps = 200

    # ACC parameters
    desired_distance = 15.0
    max_acc = 1.5
    max_brake = -3.0

    # Proportional gain
    Kp = 0.4

    # Target Vehicle
    target_position = 30.0
    target_velocity = 8.0

    # Controlled Vehicle
    controlled_position = 0.0
    controlled_velocity = 6.0
    controlled_acc = 0.0

    for step in range(1, steps + 1):

        # Target vehicle slows down after some time
        if step > 120:
            target_velocity = 4.0

        # Update target vehicle
        target_position += target_velocity * dt

        # Calculate distance and error
        distance = target_position - controlled_position
        error = distance - desired_distance

        # Proportional control
        controlled_acc = Kp * error

        # Apply acceleration limits
        if controlled_acc > max_acc:
            controlled_acc = max_acc
        if controlled_acc < max_brake:
            controlled_acc = max_brake

        # Update controlled vehicle
        controlled_velocity += controlled_acc * dt

        # Prevent negative velocity
        if controlled_velocity < 0:
            controlled_velocity = 0

        controlled_position += controlled_velocity * dt

        print(
            f"Step {step:03d} | "
            f"Distance: {distance:.2f} m | "
            f"Error: {error:.2f} m | "
            f"Target Pos: {target_position:.2f} m | "
            f"Ctrl Pos: {controlled_position:.2f} m | "
            f"Ctrl Vel: {controlled_velocity:.2f} m/s | "
            f"Ctrl Acc: {controlled_acc:.2f} m/s^2"
        )

        time.sleep(dt)

    print("\nSimulation Ended\n")

if __name__ == "__main__":
    main()
