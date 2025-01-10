# Linear Prediction Signal Processing Project

## Overview
This project demonstrates the implementation of a linear prediction algorithm for signal processing. It uses auto-correlation, matrix computation, and inverse filtering to predict signal behavior and evaluate prediction error. The project is written in Python and processes signal data from an input file.

## Features
1. **Signal Auto-Correlation**: Computes the auto-correlation of a signal to analyze dependencies across time lags.
2. **Matrix Operations**: Constructs and inverts the auto-correlation matrix to calculate predictor coefficients.
3. **Inverse Filtering**: Applies linear prediction to filter and reconstruct the signal.
4. **Error Calculation**: Evaluates the prediction error to analyze model performance.
5. **Signal Reconstruction**: Predicts new signal values based on computed coefficients and error.

## Code Explanation

### Signal Auto-Correlation
The `signal` function computes the auto-correlation of the signal over a specified time lag.
```python
rxx = np.zeros(timelag)
for i in range(timelag):
    sum = 0
    for j in range(Ndata):
        sum += S[j]*S[j-i]
    rxx[i] = sum
    rxx[-i] = rxx[i]
```

### Auto-Correlation Matrix
The `Main` function computes the auto-correlation matrix and its inverse to calculate predictor coefficients.
```python
Matrix1[i][j] = rxx[(i-1) - (j-1)]
InvMatrix1 = np.linalg.inv(Matrix1)
```

### Predictor Coefficients
The predictor coefficients are computed using the inverse matrix and auto-correlation values.
```python
for j in range(MatrixSize2):
    result += InvMatrix1[j][i]*rxx[j]
a[i] = result
```

### Error Calculation
Inverse filtering is applied to calculate the prediction error.
```python
for j in range(timelag):
    x_hat += (a_inv[j]*S[i-j])
e[i] = S[i]+x_hat
```

### Linear Prediction
The `LinierPrediction` function uses the computed coefficients and error to reconstruct the signal.
```python
for j in range(timelag):
    sum2 += a[j]*S[i-j]
x_baru[i] = sum2 + e[i]
```

## How to Run
1. Place `DataSuara.txt` in the same directory as the script.
2. Run the script and provide the desired time lag when prompted.
3. The script will compute and output the auto-correlation, predictor coefficients, and reconstructed signal.

### Example
1. Run the script:
   ```bash
   python linear_prediction.py
   ```
2. Enter a time lag (e.g., `5`) when prompted.
3. View the computed auto-correlation values and reconstructed signal.

## Outputs
- Auto-Correlation Matrix
- Predictor Coefficients
- Prediction Error
- Reconstructed Signal Plot

## Visualization
The script uses Matplotlib to visualize the signal and reconstructed output.
```python
plt.plot(jmlh, x_baru)
plt.show()
```

## Notes
- Ensure `DataSuara.txt` contains numeric data in two columns for processing.
- The time lag value significantly impacts the quality of prediction.
