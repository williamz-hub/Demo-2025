#!/usr/bin/env python3
"""
Password Generator Demo - Simple utility for generating secure passwords
Part of Demo-2025 repository - addressing Blank Issue 6
"""

import random
import string
import sys
from typing import List, Dict


class PasswordGenerator:
    """A simple password generator with customizable options."""
    
    def __init__(self):
        self.character_sets = {
            'lowercase': string.ascii_lowercase,
            'uppercase': string.ascii_uppercase,
            'digits': string.digits,
            'special': '!@#$%^&*()_+-=[]{}|;:,.<>?'
        }
    
    def generate_password(self, length: int = 12, include_uppercase: bool = True, 
                         include_digits: bool = True, include_special: bool = True) -> str:
        """Generate a password with specified criteria."""
        if length < 4:
            raise ValueError("Password length must be at least 4 characters")
        
        # Build character pool
        char_pool = self.character_sets['lowercase']  # Always include lowercase
        required_chars = [random.choice(self.character_sets['lowercase'])]
        
        if include_uppercase:
            char_pool += self.character_sets['uppercase']
            required_chars.append(random.choice(self.character_sets['uppercase']))
        
        if include_digits:
            char_pool += self.character_sets['digits']
            required_chars.append(random.choice(self.character_sets['digits']))
        
        if include_special:
            char_pool += self.character_sets['special']
            required_chars.append(random.choice(self.character_sets['special']))
        
        # Generate remaining characters
        remaining_length = length - len(required_chars)
        password_chars = required_chars + [random.choice(char_pool) for _ in range(remaining_length)]
        
        # Shuffle to avoid predictable patterns
        random.shuffle(password_chars)
        
        return ''.join(password_chars)
    
    def calculate_strength(self, password: str) -> Dict[str, any]:
        """Calculate password strength and provide feedback."""
        score = 0
        feedback = []
        
        # Length scoring
        if len(password) >= 12:
            score += 25
        elif len(password) >= 8:
            score += 15
            feedback.append("Consider using at least 12 characters")
        else:
            score += 5
            feedback.append("Password is too short - use at least 8 characters")
        
        # Character variety scoring
        has_lower = any(c.islower() for c in password)
        has_upper = any(c.isupper() for c in password)
        has_digit = any(c.isdigit() for c in password)
        has_special = any(c in self.character_sets['special'] for c in password)
        
        variety_count = sum([has_lower, has_upper, has_digit, has_special])
        score += variety_count * 15
        
        if variety_count < 3:
            feedback.append("Use a mix of uppercase, lowercase, digits, and special characters")
        
        # Determine strength level
        if score >= 80:
            strength = "Strong"
        elif score >= 60:
            strength = "Medium"
        else:
            strength = "Weak"
        
        return {
            'score': score,
            'strength': strength,
            'feedback': feedback,
            'character_types': {
                'lowercase': has_lower,
                'uppercase': has_upper,
                'digits': has_digit,
                'special': has_special
            }
        }


def main():
    """Main function for command-line interface."""
    generator = PasswordGenerator()
    
    print("🔐 Password Generator Demo")
    print("=" * 30)
    
    while True:
        print("\nOptions:")
        print("1. Generate password with default settings")
        print("2. Generate password with custom settings")
        print("3. Check password strength")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == '1':
            # Generate with defaults
            password = generator.generate_password()
            print(f"\nGenerated password: {password}")
            strength_info = generator.calculate_strength(password)
            print(f"Strength: {strength_info['strength']} (Score: {strength_info['score']}/100)")
        
        elif choice == '2':
            # Custom settings
            try:
                length = int(input("Password length (default 12): ") or 12)
                include_upper = input("Include uppercase letters? (Y/n): ").lower() != 'n'
                include_digits = input("Include digits? (Y/n): ").lower() != 'n'
                include_special = input("Include special characters? (Y/n): ").lower() != 'n'
                
                password = generator.generate_password(
                    length=length,
                    include_uppercase=include_upper,
                    include_digits=include_digits,
                    include_special=include_special
                )
                print(f"\nGenerated password: {password}")
                strength_info = generator.calculate_strength(password)
                print(f"Strength: {strength_info['strength']} (Score: {strength_info['score']}/100)")
                if strength_info['feedback']:
                    print("Suggestions:", "; ".join(strength_info['feedback']))
                    
            except ValueError as e:
                print(f"Error: {e}")
        
        elif choice == '3':
            # Check password strength
            password = input("Enter password to check: ")
            strength_info = generator.calculate_strength(password)
            print(f"\nPassword strength: {strength_info['strength']} (Score: {strength_info['score']}/100)")
            if strength_info['feedback']:
                print("Suggestions:", "; ".join(strength_info['feedback']))
            
            print("\nCharacter types found:")
            for char_type, present in strength_info['character_types'].items():
                status = "✓" if present else "✗"
                print(f"  {status} {char_type.title()}")
        
        elif choice == '4':
            print("Thank you for using Password Generator Demo!")
            break
        
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()