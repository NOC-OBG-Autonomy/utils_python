import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def slide(x, k=1, w=None, n=1, na_rm=True):
    """
    Apply a function over a sliding window with optional weights.

    Parameters:
    - x: Array or list of the variable of interest.
    - k: The window size for the sliding operation.
    - w: Weights for weighted operations (default is None).
    - n: Number of times to smooth the data.
    - na_rm: Whether to remove NaN values (default is True).

    Returns:
    - Smoothed array after applying the sliding function.

    Author:
    Flavien Petit
    """
    if na_rm:
        x = pd.Series(x).fillna(np.nan).dropna().values
    
    smoothed = np.copy(x)
    
    for _ in range(n):
        result = []
        for i in range(len(smoothed)):
            start = max(0, i - k)
            end = min(len(smoothed), i + k + 1)
            window = smoothed[start:end]
            
            if w is not None:
                weights = w[max(0, k - i):min(len(w), k + (len(smoothed) - i))]
                result.append(np.average(window, weights=weights))
            else:
                result.append(np.mean(window))
        
        smoothed = np.array(result)
    
    return smoothed


if __name__ == '__main__':
    # Example usage
    # Sample data (chla and depth)
    depth = np.linspace(0, 10, 100)
    chla = np.sin(depth) + np.random.normal(0, 0.1, len(depth))

    plt.plot(-depth, chla, label='Original')
    plt.plot(-depth, slide(chla), label='k=1, n=1', color='red')
    plt.plot(-depth, slide(chla, k=2, n=5), label='k=2, n=5', color='blue')

    plt.legend()
    plt.show()