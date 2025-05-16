import numpy as np
from typing import Tuple

def detrend_segment(segment: np.ndarray) -> np.ndarray:
    """
    Detrend a segment using linear regression.

    Args:
        segment: 1D numpy array of signal values.

    Returns:
        Detrended segment as numpy array.
    """
    x = np.arange(len(segment))
    slope, intercept = np.polyfit(x, segment, 1)
    detrended_segment = segment - (slope * x + intercept)
    return detrended_segment

def dfa_exponent(signal_profile: np.ndarray, segment_size: int) -> Tuple[np.ndarray, np.ndarray]:
    """
    Compute DFA Hurst exponent and fractal dimension for a signal profile.

    Args:
        signal_profile: Integrated signal (profile) as 1D numpy array.
        segment_size: Number of samples per segment.

    Returns:
        Tuple of two numpy arrays:
            - hurst_exponent: Hurst exponents for each segment.
            - fractal_dimensions: Corresponding fractal dimensions.
    """
    n_segments = len(signal_profile) // segment_size
    segments = signal_profile[:n_segments * segment_size].reshape(n_segments, segment_size)

    hurst_exponent = []
    fractal_dimensions = []

    for i in range(n_segments):
        segment_data = segments[i]
        fluctuation_function = []

        min_segment_size = 6
        max_segment_size = len(segment_data)
        segment_sizes = 2 ** np.arange(int(np.log2(min_segment_size)), int(np.log2(max_segment_size)) + 1)

        for seg_size in segment_sizes:
            # Reshape into smaller segments of length seg_size
            segment_subsets = segment_data[:seg_size * (len(segment_data) // seg_size)]
            reshaped_segments = segment_subsets.reshape(len(segment_subsets) // seg_size, seg_size)
            
            # Detrend each smaller segment
            detrended_segments = np.apply_along_axis(detrend_segment, 1, reshaped_segments)
            
            # Calculate root mean square fluctuation for each smaller segment
            segment_rms = np.sqrt(np.mean(detrended_segments ** 2, axis=1))
            
            # Append mean RMS fluctuation normalized by length
            fluctuation_function.append(np.mean(segment_rms) / len(segment_subsets))

        # Linear fit in log-log scale gives the DFA exponent slope
        m, _ = np.polyfit(np.log(segment_sizes), np.log(fluctuation_function), 1)
        segment_alpha = m / 2
        hurst_exponent.append(segment_alpha)
        fractal_dimensions.append(2 - segment_alpha)

    return np.array(hurst_exponent), np.array(fractal_dimensions)

