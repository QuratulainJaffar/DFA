
#!/usr/bin/python
# -*- coding: UTF-8 -*-

# __modification time__ = 2025-05-15
# __author__ = Quratulain Jaffar, GFZ Helmholtz Centre for Geosciences
# __find me__ = quratulain.jfr@gmail.com

#!/usr/bin/python
# -*- coding: UTF-8 -*-txt')





from obspy import read
import numpy as np
from datetime import datetime, timedelta
from typing import List
from functions import dfa_exponent
from plotting import plot_results

def main() -> None:
    """
    Main function to perform DFA on seismic data and plot the results.
    """
    # File paths - update to your local files
    file_path = "/.." ## input file path SAC format
    output_path = "/.." ## output file path txt format
    
    # Read seismic data using ObsPy
    st = read(file_path)
    tr = st[0]
    
    # Concatenate data from all traces if multiple
    data: np.ndarray = np.concatenate([trace.data for trace in st])
    sampling_rate: float = tr.stats.sampling_rate
    starttime: datetime = tr.stats.starttime.datetime

    # Create time axis for waveform in datetime format
    time_axis: np.ndarray = np.array([
        starttime + timedelta(seconds=i / sampling_rate) for i in range(len(data))
    ])

    # Prepare signal profile for DFA (integrated signal)
    mean_value: float = np.mean(data)
    signal_profile: np.ndarray = np.cumsum(data - mean_value)

    # Define DFA segment size (e.g., 60 seconds)
    window_duration: int = 60  # seconds
    segment_size: int = int(sampling_rate * window_duration)

    # Compute DFA Hurst exponent and fractal dimension
    hurst_exponent, fractal_dimensions = dfa_exponent(signal_profile, segment_size)

    # Generate segment center times for output and plotting
    segment_times: List[datetime] = [
        starttime + timedelta(seconds=(i + 0.5) * window_duration)
        for i in range(len(hurst_exponent))
    ]

    # Save results to a text file
    with open(output_path, "w") as f:
        f.write("Time\tHurst Exponent\tFractal Dimension\n")
        for i in range(len(hurst_exponent)):
            f.write(f"{segment_times[i]}\t{hurst_exponent[i]:.3f}\t{fractal_dimensions[i]:.3f}\n")

    print(f"Results saved to {output_path}")

    # Plot results using plotting.py utilities
    plot_results(time_axis, data, segment_times, hurst_exponent, fractal_dimensions)

if __name__ == "__main__":
    main()
