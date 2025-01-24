This repository contains a collection of projects designed to evaluate technical skills in various areas of programming and software development.
Each folder addresses a specific problem or topic, ranging from recursive algorithms and file handling to RESTful API implementation and image area estimation.

To run the included projects, ensure you have the following tools and libraries installed:
# Requirements
         Python 3.x
         pydicom
         pandas
         numpy
         matplotlib
         PostgreSQL (database connection)
         Pillow

# Repository Structure
      Technical_Test_For_Developer_Role/
      │
      ├── 1_recursion_and_colors/
      │    ├── tower_of_hanoi.py         # Solution for the Tower of Hanoi problem with color constraints.
      │    ├── test_tower_of_hanoi.py    # Unit tests for the algorithm.
      │    └── README.md                 # Detailed description of the problem and solution.
      │
      ├── 2_handling_and_array_operations/
      │    ├── file_processor.py         # DICOM and CSV file processor.
      │    ├── TEST.py                   # Tests and demonstration of the processor.
      │    ├── data/                     # Input files and test data.
      │    ├── reports/                  # Reports generated during processing.
      │    ├── requirements.txt          # Module dependencies.
      │    └── README.md                 # Details about file processing.
      │
      ├── 3_Restful_API/
      │    ├── App/                      # Implementation of the RESTful API for medical results.
      │    ├── data/                     # Input data for API testing.
      │    ├── requirements.txt          # Module dependencies.
      │    └── README.md                 # Details about file processing.
      │
      ├── 4_Create_angular_app/
      │    ├── Area_calculator.py        # Probabilistic stain area estimation in binary images.
      │    ├── requirements.txt          # Module dependencies.
      │    └── README.md                 # Details about file processing.
      │
      ├── README.md                      # This file.


# Recursion and Colors

This project contains a Python solution of the classic Tower of Hanoi problem, the goal is to move `n` disks from one rod to another using an auxiliary rod, without violating the basic rules: you can only move one disk at a time and you cannot place a larger disk on top of a smaller one. However, in this modified version of the problem, an additional constraint is also introduced: you cannot stack discs of the same color on top of each other, even if they are of different sizes. This constraint adds additional complexity to the solution.

 * Input
An integer n (1 ≤ n ≤ 8), representing the number of disks.
A list of tuples where each tuple contains the size and color of a disk, sorted in descending order of size.

 * Output
A list of moves required to transfer all disks from the source rod to the target rod.
If the transfer is impossible due to the constraints, the program will return -1.



# DICOM and CSV File Processor

  DICOM Files
    * DICOM (Digital Imaging and Communications in Medicine) is a standard format for medical imaging.
    * Widely used in hospitals and clinics to store X-rays, MRIs, CT scans, and more.
    * These files not only contain images but also essential metadata like patient names, study dates, and modality types.

  CSV Files
     * CSV (Comma-Separated Values) is a simple format for storing tabular data.
     * Each line represents a record, with values separated by commas. Example:
            Name,Age,Weight
            John,30,70
            Mary,25,6

  
  # Medical_Api
  
  Medical_Api is a RESTful API built with FastAPI that is designed to manage the results of medical image processing.
  It allows performing CRUD (Create, Read, Update, Delete) operations on processing results, storing the data in a PostgreSQL database. 
  The API receives data in JSON format, validates and normalizes the values, and computes averages before and after normalization.

  1. Create elements (POST)
     * Endpoint: /api/elements/
     * Description: This endpoint accepts a JSON payload representing the elements and stores them in the database after processing (normalization and calculations).
     * Response: A list of the created elements with details such as the average before and after normalization.
       
  2. List elements (GET)
    * Endpoint: /api/elements/
    * Description: Retrieves all elements from the database. You can filter the elements by created_date.
    * Response: A list of elements with details.

  3. Get a specific element (GET)
    * Endpoint: /api/elements/{id}/
    * Description: Retrieves a single element by its id.
    * Response: Element details.

  4. Update an element (PUT/PATCH)
    * Endpoint: /api/elements/{id}/
    * Description: Updates the device_name or id of an existing element.
    * Response: The updated element.

  5. Delete an element (DELETE)
    * Endpoint: /api/elements/{id}/
    * Description: Deletes an element by its id.
    * Response: A confirmation message for deletion.


# Estimation of a Stain's Area in Binary Images

This project is a Python script that estimates the area of a stain in a binary image using a probabilistic method based on random point generation.


Features
  * Converts images to grayscale and then to binary format.
  * Generates random points within the image.
  * Counts how many of those points fall inside the stain.
  * Calculates the estimated area of the stain based on the number of random points and their distribution.
