import time

def main():
    print("Adaptive Cruise Control Simulation Started")
    dt = 0.02  # 50 Hz loop
    position = 0.0
    velocity = 5.0  # m/s

    for step in range(100):
        position += velocity * dt
        print(f"Step {step}: Position = {position:.2f} m")
        time.sleep(dt)

    print("Simulation Finished")

if __name__ == "__main__":
    main()
