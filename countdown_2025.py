#!/usr/bin/env python3
"""
2025 Countdown Utility
A simple tool to calculate time relative to the year 2025 and provide interesting facts.
"""

import datetime
import random
from typing import Dict, List

class Countdown2025:
    """A utility class for 2025-related calculations and facts."""
    
    def __init__(self):
        self.target_year = 2025
        self.target_date = datetime.date(2025, 1, 1)
        self.current_date = datetime.date.today()
        self.facts_2025 = [
            "2025 is the International Year of Peace and Trust as declared by the UN.",
            "2025 marks 80 years since the end of World War II.",
            "The World Expo 2025 will be held in Osaka, Japan.",
            "2025 is expected to be a significant year for AI and technology advancement.",
            "Many countries plan to achieve carbon neutrality goals by 2025.",
            "2025 is a perfect square year (45²).",
            "The next leap year after 2025 will be 2028.",
            "2025 in Roman numerals is MMXXV."
        ]
    
    def days_calculation(self) -> Dict[str, int]:
        """Calculate days until or since 2025."""
        delta = (self.target_date - self.current_date).days
        
        if delta > 0:
            return {
                "days_until_2025": delta,
                "days_since_2025": 0,
                "is_future": True
            }
        else:
            return {
                "days_until_2025": 0,
                "days_since_2025": abs(delta),
                "is_future": False
            }
    
    def get_random_fact(self) -> str:
        """Get a random fact about 2025."""
        return random.choice(self.facts_2025)
    
    def get_year_info(self) -> Dict[str, any]:
        """Get comprehensive information about the current year and 2025."""
        current_year = self.current_date.year
        days_info = self.days_calculation()
        
        return {
            "current_year": current_year,
            "current_date": self.current_date.strftime("%Y-%m-%d"),
            "target_year": self.target_year,
            "days_info": days_info,
            "random_fact": self.get_random_fact(),
            "all_facts": self.facts_2025
        }
    
    def format_output(self) -> str:
        """Format the output for command line display."""
        info = self.get_year_info()
        days_info = info["days_info"]
        
        output = []
        output.append("=" * 50)
        output.append("🎯 2025 COUNTDOWN UTILITY 🎯")
        output.append("=" * 50)
        output.append(f"📅 Current Date: {info['current_date']}")
        output.append(f"🎯 Target Year: {info['target_year']}")
        output.append("")
        
        if days_info["is_future"]:
            output.append(f"⏰ Days until 2025: {days_info['days_until_2025']} days")
            output.append("🚀 2025 is coming!")
        else:
            if days_info["days_since_2025"] == 0:
                output.append("🎉 Welcome to 2025! 🎉")
            else:
                output.append(f"📈 Days since 2025 began: {days_info['days_since_2025']} days")
                output.append("🌟 We're living in the future!")
        
        output.append("")
        output.append("💡 Did you know?")
        output.append(f"   {info['random_fact']}")
        output.append("")
        output.append("=" * 50)
        
        return "\n".join(output)

def main():
    """Main function to run the countdown utility."""
    countdown = Countdown2025()
    print(countdown.format_output())
    
    # Interactive mode
    while True:
        print("\nOptions:")
        print("1. Show another fact")
        print("2. Show all facts")
        print("3. Refresh countdown")
        print("4. Exit")
        
        try:
            choice = input("\nEnter your choice (1-4): ").strip()
            
            if choice == "1":
                print(f"\n💡 {countdown.get_random_fact()}")
            elif choice == "2":
                print("\n📚 All 2025 Facts:")
                for i, fact in enumerate(countdown.facts_2025, 1):
                    print(f"   {i}. {fact}")
            elif choice == "3":
                # Refresh with current date
                countdown = Countdown2025()
                print(countdown.format_output())
            elif choice == "4":
                print("\n👋 Thank you for using 2025 Countdown! See you in the future!")
                break
            else:
                print("❌ Invalid choice. Please enter 1-4.")
                
        except KeyboardInterrupt:
            print("\n\n👋 Goodbye!")
            break
        except Exception as e:
            print(f"❌ Error: {e}")

if __name__ == "__main__":
    main()