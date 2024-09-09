import cmath

# Number to find the 4th roots of
number = -9

# Calculate the 4th roots using cmath (for handling complex numbers)
roots = [cmath.exp((2j * cmath.pi * k) / 4) * cmath.sqrt(cmath.sqrt(number)) for k in range(4)]

# Display the results
print(roots)

