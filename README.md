# Demo-2025

A demonstration repository showcasing various utilities and projects for 2025.

## Features

### Math Utilities
The `utils` package includes a comprehensive math utilities module with common mathematical functions:
- Basic arithmetic operations (add, multiply, power)
- Factorial calculation with error handling
- Number property checks (even/odd)
- Comparison utilities (max of three numbers)

## Usage

### Math Utilities Example
```python
from utils import add, multiply, factorial, is_even

# Basic calculations
result = add(5, 3)          # Returns 8
product = multiply(4, 7)     # Returns 28
fact = factorial(5)          # Returns 120
check = is_even(8)          # Returns True
```

### Running the Demo
You can run the math utilities demo directly:
```bash
python utils/math_utils.py
```

## Project Structure
```
Demo-2025/
├── README.md
└── utils/
    ├── __init__.py
    └── math_utils.py
```