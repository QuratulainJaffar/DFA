import matplotlib.pyplot as plt
from datetime import datetime
from typing import List
import numpy as np

def plot_results(
    time_axis: np.ndarray,
    data: np.ndarray,
    segment_times: List[datetime],
    hurst_exponent: np.ndarray,
    fractal_dimensions: np.ndarray
) -> None:
    """
    Plot seismic waveform, Hurst exponent, and fractal dimension.

    Args:
        time_axis: Array of datetime objects corresponding to data points.
        data: Seismic amplitude data as numpy array.
        segment_times: List of datetime objects for segment centers.
        hurst_exponent: Hurst exponent values for segments.
        fractal_dimensions: Fractal dimension values for segments.
    """
    fig, axs = plt.subplots(3, 1, figsize=(14, 10), sharex=True)

    # Plot seismic waveform
    axs[0].plot(time_axis, data, color="blue")
    axs[0].set_title("Seismic Waveform")
    axs[0].set_ylabel("Amplitude")
    axs[0].grid(True)
    axs[0].tick_params(labelbottom=False)  # Hide x-axis labels on this plot

    # Plot Hurst exponent
    axs[1].plot(segment_times, hurst_exponent, marker='o', color="red")
    axs[1].set_title("Hurst Exponent Over Time")
    axs[1].set_ylabel("Hurst Exponent")
    axs[1].set_ylim(0, 1)
    axs[1].grid(True)
    axs[1].tick_params(labelbottom=False)

    # Plot fractal dimension
    axs[2].plot(segment_times, fractal_dimensions, marker='o', color="green")
    axs[2].set_title("Fractal Dimension Over Time")
    axs[2].set_ylabel("Fractal Dimension")
    axs[2].set_ylim(1, 2)
    axs[2].set_xlabel("Time")
    axs[2].grid(True)

    plt.tight_layout()
    plt.show()
