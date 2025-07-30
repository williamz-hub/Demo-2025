#!/usr/bin/env python3
"""
Simple tests for the Demo-2025 demos.
This ensures the demo implementations work as expected.
"""

import sys
import os

# Add the parent directory to the path so we can import demo
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import demo
    print("✓ Demo module imports successfully")
except ImportError as e:
    print(f"✗ Failed to import demo module: {e}")
    sys.exit(1)

def test_demo_functions():
    """Test that all demo functions can be called without errors."""
    try:
        # Test welcome_message (should not raise exceptions)
        demo.welcome_message()
        print("✓ welcome_message() works")
        
        # Test demo_info (should not raise exceptions)
        demo.demo_info()
        print("✓ demo_info() works")
        
        return True
    except Exception as e:
        print(f"✗ Demo function error: {e}")
        return False

def test_html_file():
    """Test that the HTML file exists and contains expected content."""
    try:
        with open('index.html', 'r') as f:
            content = f.read()
        
        # Check for essential HTML elements
        required_elements = [
            '<html',
            '<head>',
            '<body>',
            'Demo-2025',
            'javascript',
            'function',
            'calculator'
        ]
        
        missing_elements = []
        for element in required_elements:
            if element.lower() not in content.lower():
                missing_elements.append(element)
        
        if missing_elements:
            print(f"✗ HTML file missing elements: {missing_elements}")
            return False
        else:
            print("✓ HTML file contains all required elements")
            return True
            
    except FileNotFoundError:
        print("✗ index.html file not found")
        return False
    except Exception as e:
        print(f"✗ Error reading HTML file: {e}")
        return False

def test_readme_file():
    """Test that the README file has been updated properly."""
    try:
        with open('README.md', 'r') as f:
            content = f.read()
        
        # Check for expected sections
        required_sections = [
            'Demo-2025',
            'Features',
            'How to Run',
            'Python Demo',
            'Web Demo'
        ]
        
        missing_sections = []
        for section in required_sections:
            if section not in content:
                missing_sections.append(section)
        
        if missing_sections:
            print(f"✗ README missing sections: {missing_sections}")
            return False
        else:
            print("✓ README contains all required sections")
            return True
            
    except FileNotFoundError:
        print("✗ README.md file not found")
        return False
    except Exception as e:
        print(f"✗ Error reading README file: {e}")
        return False

def main():
    """Run all tests."""
    print("Running Demo-2025 Tests")
    print("=" * 25)
    
    tests_passed = 0
    total_tests = 0
    
    # Test demo functions
    total_tests += 1
    if test_demo_functions():
        tests_passed += 1
    
    # Test HTML file
    total_tests += 1
    if test_html_file():
        tests_passed += 1
    
    # Test README file
    total_tests += 1
    if test_readme_file():
        tests_passed += 1
    
    print("\n" + "=" * 25)
    print(f"Tests Results: {tests_passed}/{total_tests} passed")
    
    if tests_passed == total_tests:
        print("✓ All tests passed! Demo implementation is working correctly.")
        return 0
    else:
        print("✗ Some tests failed. Please check the implementation.")
        return 1

if __name__ == "__main__":
    sys.exit(main())