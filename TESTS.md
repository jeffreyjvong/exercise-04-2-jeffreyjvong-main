# GitHub 04.2: Days in a Month

You will need to test your solution using two methods, manual testing and via a unit test. We will be using pytest for all Unit Tests as it integrates well with GitHub Classroom. Points will be awarded based on passing the unit test.

## Task 1. Manual Testing in the Terminal

Before you submit your assignment to GitHub, make sure you run the two example test cases below to verify you get the same result. To execute a manual test in the terminal, use one of the following commands:

* Linux / Unix / Mac OS: `python3 main.py`
* Windows: `py main.py`
* Alternative: `python main.py`

Note, your install may differ so you may need to research how to execute your manual python command for your computer.

### Example Case 1 (7pt)

**Case 1 Input**

```text
6
```

**Case 1 Output**

```text
30
```

### Example Case 2 (7pt)

**Case 2 Input**

```text
7
```

**Case 2 Output**

```text
31
```

### Example Case 3 (7pt)

**Case 3 Input**

```text
17
```

**Case 3 Output**

```text
Invalid month
```

### Example Case 4 (7pt)

**Case 4 Input**

```text
-6
```

**Case 4 Output**

```text
Invalid month
```

## Task 2. Execute the Unit Test in the Terminal

After pip and pytest are installed, you can run the command to execute all the tests. These are the same tests that GitHub Classroom uses so do not modify the test_main.py file:

* Linux / Unix / Mac OS: `python3 -m pytest`
* Windows: `py -m pytest`
* Alternative 1: `pytest`
* Alternative 2: `python -m pytest`

Note, your install may differ so you may need to research how to execute your pytest command.
