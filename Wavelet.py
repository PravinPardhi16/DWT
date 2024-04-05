import pywt
import numpy as np

# Example signal
signal = np.random.randn(100)
print(signal)
# Choose a wavelet
wavelet = 'db1'  # Daubechies wavelet

# Compute the Wavelet Transform
coeffs = pywt.dwt(signal, wavelet)
print(coeffs)
# coeffs is a tuple (cA, cD), where cA are approximation coefficients
# and cD are detail coefficients
approximation, details = coeffs

# To reconstruct the signal
reconstructed_signal = pywt.idwt(approximation, details, wavelet)
print(reconstructed_signal)