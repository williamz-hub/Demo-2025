# Demo-2025

A collection of interactive demos and utilities for 2025.

## Password Generator Demo

A secure password generator with both command-line and web interfaces.

### Features

- **Customizable Length**: Generate passwords from 4 to 50 characters
- **Character Set Options**: Choose from uppercase, lowercase, digits, and special characters
- **Strength Analysis**: Real-time password strength scoring and feedback
- **Multiple Interfaces**: Both Python CLI and HTML web interface
- **Copy to Clipboard**: Easy copying in the web interface

### Usage

#### Command Line Interface (Python)

```bash
python3 password_generator.py
```

Interactive menu with options to:
1. Generate password with default settings
2. Generate password with custom settings  
3. Check password strength of existing passwords
4. Exit

#### Web Interface

Open `password_generator.html` in any web browser for a modern, interactive interface.

Or serve it with Python:
```bash
python3 -m http.server 8000
# Then visit: http://localhost:8000/password_generator.html
```

### Example Usage

```python
from password_generator import PasswordGenerator

gen = PasswordGenerator()

# Generate a 16-character password with all character types
password = gen.generate_password(16, True, True, True)
print(f"Generated: {password}")

# Check password strength
strength = gen.calculate_strength(password)
print(f"Strength: {strength['strength']} (Score: {strength['score']}/100)")
```

### Demo Features

- **Secure Generation**: Uses cryptographically secure random number generation
- **Strength Scoring**: Comprehensive password strength analysis
- **User-Friendly**: Clear feedback and suggestions for improvement
- **Responsive Design**: Works on desktop and mobile devices
- **No Dependencies**: Pure Python and vanilla JavaScript

This demo addresses "Blank Issue 6" by providing a practical, well-designed utility that demonstrates good software development practices.