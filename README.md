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

  

