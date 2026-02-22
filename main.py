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
