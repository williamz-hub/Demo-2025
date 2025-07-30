#!/usr/bin/env python3
"""
2025 Year Facts Utility
A simple demo utility providing interesting facts about the year 2025.
"""

import random
from datetime import datetime


class Year2025Facts:
    """A utility class for 2025 year facts and information."""
    
    def __init__(self):
        self.facts = [
            "2025 is the first year of the second quarter of the 21st century.",
            "2025 marks 30 years since the release of Windows 95.",
            "In 2025, Generation Alpha (born after 2010) will be in their teens.",
            "2025 will be 80 years since the end of World War II.",
            "The year 2025 has 365 days (not a leap year).",
            "2025 is an odd number and the square of 45 (45² = 2025).",
            "Many companies have set sustainability goals to achieve by 2025.",
            "2025 will mark 60 years since the first commercial email was sent.",
            "In Roman numerals, 2025 is written as MMXXV.",
            "2025 is exactly 25 years after the millennium celebrations of 2000."
        ]
        
        self.historical_context = [
            "25 years ago (2000): Y2K concerns, dot-com boom",
            "50 years ago (1975): Microsoft founded, Vietnam War ended",
            "75 years ago (1950): Korean War began, first credit card issued",
            "100 years ago (1925): Television was demonstrated publicly for the first time"
        ]
    
    def get_random_fact(self):
        """Return a random fact about 2025."""
        return random.choice(self.facts)
    
    def get_all_facts(self):
        """Return all facts about 2025."""
        return self.facts.copy()
    
    def get_historical_context(self):
        """Return historical context for perspective."""
        return self.historical_context.copy()
    
    def get_math_properties(self):
        """Return mathematical properties of 2025."""
        return {
            "square_root": 45,
            "is_perfect_square": True,
            "factors": self._get_factors(2025),
            "is_prime": False,
            "binary": bin(2025)[2:],
            "hexadecimal": hex(2025)[2:].upper()
        }
    
    def _get_factors(self, n):
        """Get all factors of a number."""
        factors = []
        for i in range(1, int(n**0.5) + 1):
            if n % i == 0:
                factors.append(i)
                if i != n // i:
                    factors.append(n // i)
        return sorted(factors)
    
    def days_until_2025(self):
        """Calculate days until 2025 (or days since if we're past it)."""
        now = datetime.now()
        year_2025 = datetime(2025, 1, 1)
        
        if now < year_2025:
            diff = year_2025 - now
            return f"Days until 2025: {diff.days}"
        else:
            diff = now - year_2025
            return f"Days since 2025 began: {diff.days}"


def main():
    """Main function for command-line interface."""
    facts = Year2025Facts()
    
    print("=" * 50)
    print("       2025 YEAR FACTS UTILITY")
    print("=" * 50)
    print()
    
    while True:
        print("Choose an option:")
        print("1. Get a random fact about 2025")
        print("2. Show all facts")
        print("3. Show historical context")
        print("4. Show mathematical properties")
        print("5. Days until/since 2025")
        print("6. Exit")
        print()
        
        try:
            choice = input("Enter your choice (1-6): ").strip()
            print()
            
            if choice == '1':
                print("Random Fact:")
                print("-" * 20)
                print(facts.get_random_fact())
                
            elif choice == '2':
                print("All Facts About 2025:")
                print("-" * 25)
                for i, fact in enumerate(facts.get_all_facts(), 1):
                    print(f"{i}. {fact}")
                    
            elif choice == '3':
                print("Historical Context:")
                print("-" * 20)
                for context in facts.get_historical_context():
                    print(f"• {context}")
                    
            elif choice == '4':
                print("Mathematical Properties of 2025:")
                print("-" * 35)
                props = facts.get_math_properties()
                print(f"Square root: {props['square_root']}")
                print(f"Perfect square: {props['is_perfect_square']}")
                print(f"Factors: {props['factors']}")
                print(f"Prime number: {props['is_prime']}")
                print(f"Binary: {props['binary']}")
                print(f"Hexadecimal: {props['hexadecimal']}")
                
            elif choice == '5':
                print(facts.days_until_2025())
                
            elif choice == '6':
                print("Thank you for using the 2025 Year Facts Utility!")
                break
                
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")
                
        except KeyboardInterrupt:
            print("\n\nGoodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
            
        print("\n" + "-" * 50 + "\n")


if __name__ == "__main__":
    main()