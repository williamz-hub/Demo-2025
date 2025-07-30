#!/usr/bin/env python3
"""
Demo-2025 - Basic Demo Script

This is a simple demonstration script for the Demo-2025 repository.
It showcases basic functionality that can be extended for more complex demos.
"""

import sys
from datetime import datetime


def welcome_message():
    """Display a welcome message for the demo."""
    print("=" * 50)
    print("Welcome to Demo-2025!")
    print("=" * 50)
    print(f"Current time: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    print()


def basic_calculator():
    """Simple calculator demonstration."""
    print("Basic Calculator Demo:")
    print("---------------------")
    
    try:
        a = float(input("Enter first number: "))
        b = float(input("Enter second number: "))
        
        print(f"\nResults:")
        print(f"{a} + {b} = {a + b}")
        print(f"{a} - {b} = {a - b}")
        print(f"{a} * {b} = {a * b}")
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print(f"{a} / {b} = Cannot divide by zero!")
            
    except ValueError:
        print("Please enter valid numbers.")
    except KeyboardInterrupt:
        print("\nDemo interrupted by user.")


def demo_info():
    """Display information about this demo."""
    print("\nDemo Information:")
    print("-" * 20)
    print("This is a basic demo for the Demo-2025 repository.")
    print("It demonstrates:")
    print("- Basic Python scripting")
    print("- User input handling")
    print("- Simple arithmetic operations")
    print("- Error handling")
    print("\nThis can be extended with more complex functionality!")


def main():
    """Main demo function."""
    welcome_message()
    
    print("What would you like to do?")
    print("1. Run calculator demo")
    print("2. Show demo info")
    print("3. Exit")
    
    try:
        choice = input("\nEnter your choice (1-3): ").strip()
        
        if choice == "1":
            basic_calculator()
        elif choice == "2":
            demo_info()
        elif choice == "3":
            print("Thanks for trying Demo-2025!")
        else:
            print("Invalid choice. Please run the demo again.")
            
    except KeyboardInterrupt:
        print("\nDemo interrupted. Goodbye!")
    except Exception as e:
        print(f"An error occurred: {e}")


if __name__ == "__main__":
    main()