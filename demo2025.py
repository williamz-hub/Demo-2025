#!/usr/bin/env python3
"""
Demo 2025 - A simple utility for 2025-themed calculations and facts
"""

import datetime
import calendar

def days_until_new_year_2025():
    """Calculate days until New Year 2025"""
    today = datetime.date.today()
    new_year_2025 = datetime.date(2025, 1, 1)
    
    if today >= new_year_2025:
        # If we're already in 2025 or past it
        next_new_year = datetime.date(today.year + 1, 1, 1)
        diff = next_new_year - today
        return f"New Year 2025 has passed! Days until next New Year: {diff.days}"
    else:
        diff = new_year_2025 - today
        return f"Days until New Year 2025: {diff.days}"

def days_since_2025_started():
    """Calculate days since 2025 started"""
    today = datetime.date.today()
    start_2025 = datetime.date(2025, 1, 1)
    
    if today < start_2025:
        return "2025 hasn't started yet!"
    else:
        diff = today - start_2025
        return f"Days since 2025 started: {diff.days + 1}"

def year_2025_facts():
    """Return interesting facts about the year 2025"""
    facts = [
        "🗓️  2025 is not a leap year",
        "📅  2025 starts on a Wednesday",
        "🔢  2025 = 5² × 3⁴ (factorization: 5² × 81)",
        "🌟  2025 is a perfect square (45²)",
        "📖  The Chinese zodiac animal for 2025 is the Snake",
        "🎯  2025 marks 25 years since the year 2000"
    ]
    return facts

def is_date_in_2025(month, day):
    """Check if a given date falls in 2025 and return day of week"""
    try:
        date_2025 = datetime.date(2025, month, day)
        day_name = calendar.day_name[date_2025.weekday()]
        return f"{calendar.month_name[month]} {day}, 2025 falls on a {day_name}"
    except ValueError:
        return "Invalid date"

def main():
    """Main interactive function"""
    print("🎉 Welcome to Demo 2025! 🎉")
    print("=" * 40)
    
    while True:
        print("\nChoose an option:")
        print("1. Days until/since New Year 2025")
        print("2. Days since 2025 started")
        print("3. Interesting facts about 2025")
        print("4. Check what day of week a date falls in 2025")
        print("5. Exit")
        
        choice = input("\nEnter your choice (1-5): ").strip()
        
        if choice == '1':
            print(days_until_new_year_2025())
        elif choice == '2':
            print(days_since_2025_started())
        elif choice == '3':
            print("\n📚 Interesting Facts About 2025:")
            for fact in year_2025_facts():
                print(f"  {fact}")
        elif choice == '4':
            try:
                month = int(input("Enter month (1-12): "))
                day = int(input("Enter day (1-31): "))
                print(is_date_in_2025(month, day))
            except ValueError:
                print("Please enter valid numbers")
        elif choice == '5':
            print("Thanks for using Demo 2025! 🎊")
            break
        else:
            print("Invalid choice. Please enter 1-5.")

if __name__ == "__main__":
    main()