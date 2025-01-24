from file_processor import FileProcessor

processor = FileProcessor(
    base_path="C:/Users/eliza/OneDrive/Escritorio/Imexhs/TECHNICAL_TEST_FOR_DEVELOPER_ROLE/2_handling_and_array_operations/data", 
    log_file="log"
)

# List folder contents
processor.list_folder_contents(folder_name="test_folder", details=True)

# Analyze a CSV file
processor.read_csv(
    filename="sample-02-csv.csv",
    report_path="reports",
    summary=True
)

# Analyze a DICOM file
processor.read_dicom(
    filename="sample-02-dicom.dcm",
    tags=[(0x0010, 0x0010), (0x0008, 0x0060)],
    extract_image=True
)
