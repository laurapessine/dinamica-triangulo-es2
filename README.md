# Triangle Problem (Python + pytest)

This repository contains a Python implementation of the classic **Triangle Problem**, commonly used in software testing.

## Problem

Given three integers representing the sides of a triangle, the program must classify it as:

- **EQUILATERAL** — all sides equal  
- **ISOSCELES** — two sides equal  
- **SCALENE** — all sides different  
- **INVALID** — does not form a valid triangle  

---

## Setup

Create a virtual environment and install dependencies:

```bash
# 1. Create the virtual environment
python -m venv venv

# 2. Activate the virtual environment
# For Windows (Command Prompt):
venv\Scripts\activate
# For Windows (PowerShell):
venv\Scripts\Activate.ps1
# For Linux/macOS:
source venv/bin/activate

# 3. Install dependencies
pip install pytest
```

## How to run

The program accepts three integer values from the command line representing the sides of the triangle. To classify a triangle, run the script:

```bash
python triangle.py 3 4 5
```

## How to test

To execute the automated test suite and validate the edge cases, run:

```bash
pytest -v
```