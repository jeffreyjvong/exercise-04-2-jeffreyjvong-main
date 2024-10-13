#!/usr/bin/env python3
# GitHub 04.2: Days in a Month

# Import Modules
import main as app, random
from calendar import monthrange

# Global Variable for input() of user values
value_input = []

# Global Variable for output of Actual Result of the Program
value_actual = []

def mock_input(prompt):
    "Mock the Input Process"
    global value_input, value_actual
    value_actual.append(prompt)
    return str(value_input.pop(0))

def test_case1():
    "Case 1: Test for Valid Known Months (16pt)"

    # Setup IO Variables
    global value_input, value_actual
    value_actual = []
    value_expected = []
    for m in range(1,13):
        value_expected.append("> ")
        value_expected.append(monthrange(2020, m)[1])

    # Run the Main App
    app.input = mock_input
    app.print = lambda arg1 : value_actual.extend([arg1])
    for m in range(1,13):
        value_input = [m]
        app.main()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected

def test_case2():
    "Case 2: Test for Invalid Month Input (16pt)"

    # Setup IO Variables
    global value_input, value_actual
    value_actual = []
    value_expected = ["> ", "Invalid month"] * 12

    # Run the Main App
    app.input = mock_input
    app.print = lambda arg1 : value_actual.extend([arg1])
    for m in range(0,12):
        if m % 2 == 0:
            value_input = [random.randint(-100,0)]
        else:
            value_input = [random.randint(13,100)]
        app.main()

    # Test the Actual result equal to the Expected result
    assert value_actual == value_expected