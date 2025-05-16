# Seismic Fractal Dimension Analysis

This Python project calculates the fractal dimension of seismic signals using a variogram estimator method.

## Features

- Reads seismic `.SAC` files  
- Computes variograms and fractal dimensions in sliding time windows  
- Plots both seismic waveform and fractal dimensions over time  
- Saves results to `output.txt`

## Requirements

- Python 3.7+  
- ObsPy  
- NumPy  
- Matplotlib

Install dependencies with:

```bash
pip install obspy numpy matplotlib
