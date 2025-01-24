# Recursion and Colors
This project contains a Python solution of the classic Tower of Hanoi problem, the goal is to move `n` disks from one rod to another using an auxiliary rod, without violating the basic rules: you can only move one disk at a time and you cannot place a larger disk on top of a smaller one. However, in this modified version of the problem, an additional constraint is also introduced: you cannot stack discs of the same color on top of each other, even if they are of different sizes. This constraint adds additional complexity to the solution.

 # Input
An integer n (1 ≤ n ≤ 8), representing the number of disks.
A list of tuples where each tuple contains the size and color of a disk, sorted in descending order of size.

 # Output
A list of moves required to transfer all disks from the source rod to the target rod.
If the transfer is impossible due to the constraints, the program will return -1.

 # Project Structure

    1_recursion_and_colors/
        │
        ├── tower_of_hanoi.py        # Main solution script
        ├── test_tower_of_hanoi.py   # Unit tests for the solution
        └── README.md                # Documentation

# How to Run
1. Ensure Python 3 is installed on your system.
2. Clone this repository:

      git clone https://github.com/ElizabethBP79/TECHNICAL_TEST_FOR_DEVELOPER_ROLE
      cd TECHNICAL_TEST_FOR_DEVELOPER_ROLE/1_recursion_and_colors

3. Run the script:

    python tower_of_hanoi.py

      Code Description
        *Validate_disks function: Verifies that the disks are sorted by descending size.
        *Move_disk function: Moves a disk from one rod to another, verifying constraints:
                Do not place large disks on top of small ones.
                Do not place disks of the same color directly on top of each other.
        *Hanoi_with_constraints function: Applies recursion to move disks between rods following the rules.
        *Solve_tower_of_hanoi function: Orchestrates the solution by validating the input and handling the constraints.

4. The program will prompt you for the number of disks and their details.

# Example Input/Output

Input
     n = 3
     disks = [(3, "red"), (2, "blue"), (1, "red")]

Output
If valid moves are possible:

    [
        (1, "A", "C"),
        (2, "A", "B"),
        (1, "C", "B"),
        (3, "A", "C"),
        (1, "B", "A"),
        (2, "B", "C"),
        (1, "A", "C")
    ]

If moves are impossible due to constraints:

    -1

# How to Test
To verify the correctness of the implementation, unit tests are provided. Run the following command in the terminal:


    python -m unittest test_tower_of_hanoi.py
        Code Description
            1. test_valid_input: 
                Input:  n = 3: Three disks.
                        disks = [(3, “red”), (2, “blue”), (1, “red”)]: List of disks with size and color.
                
                Validation:
                        self.assertIsInstance(result, list): check that the output is a list.
                        self.assertGreater(len(result), 0): Confirms that the list is not empty (it should contain transactions).

            2. test_invalid_input:
                Input:  n = 3
                        disks = [(3, “red”), (2, “red”), (1, “blue”)]: Two disks have the same consecutive color, which is invalid.
                
                Validation:
                        self.assertEqual(result, -1): Check that the output is -1, which indicates that the transfer is impossible.
            
            3. test_edge_case_single_disk:
                Input:  n = 1
                        disks = [(1, "blue")]: Single disk, simplest case.
                
                Validation:
                        self.assertIsInstance(result, list): The output must be a list.
                        self.assertEqual(len(result), 1): There must be a single transaction.
            
              

This will execute the tests and display the results.

# Requirements
    Python 3.x

# Notes
   1. Ensure the input disks are provided in descending order of size.
   2. The implementation uses recursion, so be mindful of the recursion limit for larger values of n.
   3. If the file is executed directly (test_tower_of_hanoi.py), all tests within the class will be executed.
