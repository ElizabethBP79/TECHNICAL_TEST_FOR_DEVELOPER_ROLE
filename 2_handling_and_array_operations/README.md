# DICOM and CSV File Processor

# What are DICOM and CSV files?

    DICOM Files

        * DICOM (Digital Imaging and Communications in Medicine) is a standard format for medical imaging.

        * Widely used in hospitals and clinics to store X-rays, MRIs, CT scans, and more.

        * These files not only contain images but also essential metadata like patient names, study dates, and modality types.

    CSV Files

        * CSV (Comma-Separated Values) is a simple format for storing tabular data.

        * Each line represents a record, with values separated by commas. Example:
            Name,Age,Weight
            John,30,70
            Mary,25,60

# What does this project do?

    Main Features:

        1. List folder contents:
            Displays the files in a folder along with their size and last modification date.

        2. Process CSV files:

            Analyzes numeric and non-numeric data.
            Generates reports with statistics like averages and standard deviations.

        3. Process DICOM files:

            Extracts metadata such as:
                Patient Name.
                Study Date.
                Modality (e.g., X-ray, MRI).

            Converts medical images to PNG format for easy viewing.

# How to Use This Project?

    1. Prerequisites

        You need:

            * Python: Download it here.
            * Required Libraries:
                pydicom, pandas, numpy, matplotlib.

                Install libraries by running:

                    pip install pydicom pandas numpy matplotlib

    2. Download the Project

        Download or clone this repository to your computer.
        Place your DICOM and CSV files in the "data" folder.

    3. Project Structure

        * file_processor.py: Main script for processing files.
        * TEST.py: Test script with usage examples.
        * data/: Folder for your input files.
        * reports/: Folder for generated reports.
        * log.txt: File for logging errors and events.

    4. Run the Project
        * Clone this repository:

             git clone https://github.com/ElizabethBP79/TECHNICAL_TEST_FOR_DEVELOPER_ROLE
                cd TECHNICAL_TEST_FOR_DEVELOPER_ROLE/2_handling_and_array_operations

        * Navigate to the project folder and run the test script:

            python TEST.py

                In addition to uploading the DICOM and CSV files to the /data folder, remember to update the "base_path" variable with the path of your /data folder location in the TEST.py file line 4

# Key Methods

    1. list_folder_contents
        Purpose: Lists all files in a folder with details like size and modification date.
        Usage: processor.list_folder_contents(folder_name="data", details=True)
    
    2. read_csv
        Purpose: Processes a CSV file, analyzes data, and generates a statistical report.
        Usage: processor.read_csv(filename="sample.csv", report_path="reports", summary=True)
    
    3. read_dicom
    Purpose: Reads a DICOM file, extracts metadata, and optionally converts the image to PNG.
    Usage:

    processor.read_dicom(
        filename="sample.dcm",
        tags=[(0x0010, 0x0010), (0x0008, 0x0060)],
        extract_image=True
    )
# Example Functions

    1. List Folder Contents

        processor.list_folder_contents(folder_name="data", details=True)

        Output: Displays file details like name, size, and last modification date.

    2. Analyze CSV Files

        processor.read_csv(filename="sample.csv", report_path="reports", summary=True)

        Output: Generates a summary with statistics and saves a report in the reports/ folder.

    3. Process DICOM Files

        processor.read_dicom(filename="sample.dcm",tags=[(0x0010, 0x0010), (0x0008, 0x0060)], extract_image=False)

        Output: Extracts metadata.

# Troubleshooting
    * "File not found": Verify the file is in the data folder.
    * "Unsupported image dimensions": Ensure the DICOM file is supported. Only the central slice is saved.
    * "No module named 'pydicom'": Ensure the required libraries are installed.