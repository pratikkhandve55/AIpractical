import numpy as np

digits = []

for i in range(10):
    d = input(f"Enter digit {i+1} (0-9): ")
    
    if d.isdigit() and len(d) == 1:
        digits.append(d)
    else:
        print("Invalid input! Storing 0 instead.")
        digits.append('0')

# Convert digits to ASCII values
ascii_values = [ord(d) for d in digits]

# Convert ASCII to 8-bit binary
X = []
for val in ascii_values:
    binary = [int(b) for b in format(val, '08b')]
    X.append(binary)

X = np.array(X)

# Labels: 1 for even, 0 for odd
y = np.array([1 if int(d) % 2 == 0 else 0 for d in digits])

# --- Step 2: Initialize Perceptron ---
weights = np.random.rand(8)
bias = np.random.rand()
lr = 0.1
epochs = 10

# --- Step 3: Train Perceptron ---
for epoch in range(epochs):
    for i in range(len(X)):
        total = np.dot(X[i], weights) + bias
        output = 1 if total >= 0 else 0
        error = y[i] - output
        
        weights += lr * error * X[i]
        bias += lr * error

# --- Step 4: Test Perceptron ---
print("\nDigit | Predicted | Actual")
for i in range(len(X)):
    total = np.dot(X[i], weights) + bias
    output = 1 if total >= 0 else 0
    
    print(f"  {digits[i]}   | {'Even' if output==1 else 'Odd'}      | {'Even' if y[i]==1 else 'Odd'}")