"""
File: package_sort.py
Author: Jerry Walton (jerrywalton333@gmail.com | 951-348-6959)

### Objective

Imagine you work in Thoughtful’s robotic automation factory, and your objective is to write a function for one of its robotic arms that will dispatch the packages to the correct stack according to their volume and mass.

### Rules

Sort the packages using the following criteria:

- A package is **bulky** if its volume (Width x Height x Length) is greater than or equal to 1,000,000 cm³ or when one of its dimensions is greater or equal to 150 cm.
- A package is **heavy** when its mass is greater or equal to 20 kg.

You must dispatch the packages in the following stacks:

- **STANDARD**: standard packages (those that are not bulky or heavy) can be handled normally.
- **SPECIAL**: packages that are either heavy or bulky can't be handled automatically.
- **REJECTED**: packages that are **both** heavy and bulky are rejected.

### Implementation

Implement the function **`sort(width, height, length, mass)`** (units are centimeters for the dimensions and kilogram for the mass). This function must return a string: the name of the stack where the package should go.

### Submission Guidance

1. **Time Management**: Allocate no more than 30 minutes to complete this challenge. 
2. **Programming Language**: You may use any programming language you're comfortable with. This is an opportunity to showcase your skills in a language you are proficient in.
3. **Submission Format**:
    - **Option 1**: Submit a public GitHub repository with clear README instructions.
    - **Option 2 (Preferred)**: Host your solution on an online IDE like [Repl.it](http://repl.it/) or CodePen for immediate code review. Ensure the link is accessible for direct execution.
4. **Evaluation Criteria**: Submissions will be assessed on:
    - Correct sorting logic.
    - Code quality.
    - Handling edge cases and inputs.
    - Test coverage.
"""
# the required sort function
# accepts dimensions and mass of the package
def sort(width: float, height: float, length: float, mass: float) -> str:
    """
    Determines the correct stack for a package based on its dimensions and mass.
    Units:
      - width, height, length: centimeters
      - mass: kilograms
    Returns:
      - "STANDARD"
      - "SPECIAL"
      - "REJECTED"
    """
    print(f"\nsort(width: {width} height: {height} length: {length} mass: {mass})")

    # V = W x H x L
    volume = width * height * length
    print(f"volumn: {volume}")

    # test for bulky as defined by spec.
    bulky = volume >= 1_000_000 or any(d >= 150 for d in (width, height, length))
    print(f"bulky: {bulky} -> (volume >= 1 MIL) or (W or H or L > 150)")

    # test for heavy as defined by spec.
    heavy = mass >= 20
    print(f"heavy: {heavy} -> mass: {mass} >= 20")

    # simple if/else to determine stack for given package
    if bulky and heavy:
        print(f"bulky AND heavy => bulky: {bulky} heavy: {heavy}")
        print("returning REJECTED")
        return "REJECTED"
    elif bulky or heavy:
        print(f"bulky OR heavy => bulky: {bulky} heavy: {heavy}")
        print("returning SPECIAL")
        return "SPECIAL"
    else:
        print("returning STANDARD")
        return "STANDARD"


# example test
if __name__ == "__main__":
    
    tests = [
        (100, 100, 100, 100),   # Bulky, not heavy → SPECIAL
        (100, 300, 100, 100),   # Bulky, not heavy → SPECIAL
        (200, 50, 50, 10),     # Bulky (dimension ≥150) → SPECIAL
        (100, 100, 100, 25),   # Heavy → SPECIAL
        (200, 200, 200, 25),   # Bulky + Heavy → REJECTED
        (75, 50, 30, 10),      # STANDARD
        (50, 50, 50, 19)       # STANDARD
    ]

    for t in tests:
        print(f"Input: {t} → Stack: {sort(*t)}")
