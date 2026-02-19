# Adaptive Cruise Control (ACC) using Model Predictive Control

## Problem Statement
Road accidents often occur due to delayed human reaction during sudden braking or speed changes of the front vehicle.
Adaptive Cruise Control (ACC) is an advanced driver assistance feature that automatically adjusts a vehicle’s speed to maintain a safe distance from the vehicle ahead.

## Our Solution
This project implements an **Adaptive Cruise Control (ACC)** system using **Model Predictive Control (MPC)**.  
The system predicts the future behavior of the front vehicle and finds optimal acceleration/deceleration commands to ensure safety, smoothness, and real-time performance.

This project is fully **open-source**, **reproducible**, and designed to run in **real-time (50 Hz)**.

## Key Features
- Two-vehicle simulation ( Target Vehicle + Controlled Vehicle)
- Safe distance maintenance
- Anticipatory braking using MPC
- Real-time control loop (10–100 ms)
- Fully open-source implementation

## Tech Stack
- Python 3
- NumPy
- CVXPY + OSQP (for MPC optimization)
- Matplotlib (visualization)

## System Architecture
-Vehicle motion model (longitudinal dynamics)
-Distance measurement between vehicles
-Prediction of target vehicle behavior
-Model Predictive Controller for acceleration computation
-Real‑time simulation loop
-Visualization and performance monitoring

## Repository Structure
-src/
  -models/ → vehicle dynamics
  -controllers/ → MPC controller
  -simulation/ → simulation logic
-docs/ → documentation
-main.py → entry point
-requirements.txt → dependencies
-README.md → project documentation
-LICENSE → MIT License

## How to Run (to be updated)
-Clone the repository
-Install dependencies using pip
-Run the main simulation file
-Detailed instructions will be added as development progresses.

## Real‑Time Performance
-The controller runs inside a fixed‑time loop (≈20 ms per iteration).
-Loop execution time and solver performance are logged and measured to ensure real‑time feasibility.

## Project Status
This project is under active development for FOSS Hack 2026.
Core simulation and control logic are currently being implemented.

## Open‑Source License
This project is released under the **MIT License**, allowing free use, modification, and distribution with attribution.


  

