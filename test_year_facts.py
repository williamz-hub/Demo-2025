#!/usr/bin/env python3
"""
Simple test for the 2025 Year Facts Utility
"""

import sys
import os

# Add the current directory to Python path to import our module
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from year_facts_2025 import Year2025Facts

def test_year_facts():
    """Test the Year2025Facts class functionality."""
    print("Testing 2025 Year Facts Utility...")
    
    facts = Year2025Facts()
    
    # Test 1: Random fact
    random_fact = facts.get_random_fact()
    assert isinstance(random_fact, str) and len(random_fact) > 0
    print("✓ Random fact generation works")
    
    # Test 2: All facts
    all_facts = facts.get_all_facts()
    assert isinstance(all_facts, list) and len(all_facts) == 10
    print("✓ All facts retrieval works")
    
    # Test 3: Historical context
    context = facts.get_historical_context()
    assert isinstance(context, list) and len(context) == 4
    print("✓ Historical context works")
    
    # Test 4: Math properties
    math_props = facts.get_math_properties()
    expected_keys = {'square_root', 'is_perfect_square', 'factors', 'is_prime', 'binary', 'hexadecimal'}
    assert set(math_props.keys()) == expected_keys
    assert math_props['square_root'] == 45
    assert math_props['is_perfect_square'] == True
    assert math_props['is_prime'] == False
    print("✓ Mathematical properties calculation works")
    
    # Test 5: Days calculation
    days_info = facts.days_until_2025()
    assert isinstance(days_info, str) and "Days" in days_info
    print("✓ Days calculation works")
    
    print("\n🎉 All tests passed! The 2025 Year Facts Utility is working correctly.")
    return True

if __name__ == "__main__":
    try:
        test_year_facts()
        print("\n✅ Test suite completed successfully!")
    except Exception as e:
        print(f"\n❌ Test failed: {e}")
        sys.exit(1)