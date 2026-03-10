# smartTechAutomation
Imagine you work in Smarter Technology’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

# Package Sorting System

# Overview:
This project implements a Python function that simulates part of a robotic automation system used in a factory. The system classifies packages into different stacks depending on their dimensions and mass.

The goal is to determine whether a package should be handled normally, requires special handling, or should be rejected.

# Problem Description
The robotic arm must sort packages based on two properties:
1. Bulky
2. Heavy

Depending on these conditions, the package is dispatched to one of three stacks.

# Classification Rules
1. Bulky Package
    A package is considered bulky if:
        i. Any dimension is greater than or equal to 150 cm
                OR
        ii.Its volume is greater than or equal to                                    1,000,000 cm³, volume = width × height × length

2. Heavy Package
    A package is considered heavy if:
        Mass is greater than or equal to 20 kg

# Stack Assignment
Condition	-> Result
Not bulky AND not heavy	-> STANDARD
Bulky OR heavy	-> SPECIAL
Bulky AND heavy	-> REJECTED

# Implementation: Refer to main.py file

# Time Complexity
    The algorithm performs a constant number of comparisons and arithmetic operations.
    Time Complexity:O(1)
    Space Complexity:O(1)

No additional memory structures are required.

# Example Usage
print(sort(100, 100, 10, 10))
print(sort(100, 100, 100, 10))
print(sort(100, 100, 10, 20))
print(sort(100, 100, 100, 100))

# Expected Output
STANDARD
SPECIAL
SPECIAL
REJECTED

# Edge Cases Considered
The implementation correctly handles:
Packages exactly at the dimension threshold (150 cm)
Packages exactly at the mass threshold (20 kg)
Packages where volume alone triggers bulky classification
Packages that satisfy both bulky and heavy conditions
Example:

sort(150, 10, 10, 10)    # SPECIAL (dimension threshold)
sort(10, 10, 10, 20) # SPECIAL (mass threshold)

# How to Run: 
python main.py
