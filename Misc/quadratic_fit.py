import numpy as np
import matplotlib.pyplot as plt

# Data points: (-3, -85), (0, -1), (1, -1), (2, -15)
x_data = np.array([-3, 0, 1, 2])
y_data = np.array([-85, -1, -1, -15])

# Part (a): Set up the matrices X and y
# For f(x) = c₁ + c₂x², X will have columns [1, x²]
X = np.column_stack((np.ones_like(x_data), x_data**2))
print("Matrix X:")
print(X)
print("\nVector y:")
print(y_data)

# Part (b): Solve the normal equations (X^T X) c = X^T y
# Method 1: Direct calculation
XTX = X.T @ X
XTy = X.T @ y_data
print("\nX^T X:")
print(XTX)
print("\nX^T y:")
print(XTy)

# Solve the system
c = np.linalg.solve(XTX, XTy)
print("\nCoefficients c = [c₁, c₂]:")
print(c)

# Verify the answer - convert to fraction representation
c1_exact = c[0]
c2_exact = c[1]
print(f"\nExact values:")
print(f"c₁ = {c1_exact}")
print(f"c₂ = {c2_exact}")

# Calculate approximate fraction for c₂
# We know from manual calculation that c₂ = -469/49
c2_fraction = "-469/49"
print(f"c₂ ≈ {c2_fraction} ≈ {-469/49}")

# Verify by calculating predicted values
def model(x, c1, c2):
    return c1 + c2 * x**2

y_pred = model(x_data, c[0], c[1])
residuals = y_data - y_pred
sse = np.sum(residuals**2)

print("\nVerification:")
print("x\ty_actual\ty_predicted\tresidual")
for i in range(len(x_data)):
    print(f"{x_data[i]}\t{y_data[i]}\t{y_pred[i]:.2f}\t\t{residuals[i]:.2f}")
print(f"\nSum of squared errors: {sse:.2f}")

# Plot the data and fitted curve
plt.figure(figsize=(10, 6))
plt.scatter(x_data, y_data, color='red', label='Data points')
x_fit = np.linspace(min(x_data)-0.5, max(x_data)+0.5, 100)
y_fit = model(x_fit, c[0], c[1])
plt.plot(x_fit, y_fit, color='blue', label=f'f(x) = {c[0]:.2f} {c[1]:.2f}x²')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Least Squares Quadratic Fit: f(x) = c₁ + c₂x²')
plt.legend()
plt.grid(True)
plt.savefig('quadratic_fit.png')
plt.close()

# Alternative approach - using numpy's least squares solver
c_alt, residuals, rank, s = np.linalg.lstsq(X, y_data, rcond=None)
print("\nUsing np.linalg.lstsq:")
print(f"c₁ = {c_alt[0]}")
print(f"c₂ = {c_alt[1]}")

print("\nFinal answer:")
print(f"c₁ = 8")
print(f"c₂ = -469/49 ≈ {-469/49:.6f}") 