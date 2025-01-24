import os
import logging
import pandas as pd
import numpy as np
import pydicom
from datetime import datetime
from pydicom.pixel_data_handlers.util import apply_modality_lut
import matplotlib.pyplot as plt
from typing import Optional, List, Tuple

class FileProcessor:
    def __init__(self, base_path: str, log_file: str):
        self.base_path = base_path
        os.makedirs(self.base_path, exist_ok=True)

        logging.basicConfig(
            filename=log_file,
            level=logging.ERROR,
            format='%(asctime)s - %(levelname)s - %(message)s'
        )
        self.logger = logging.getLogger(__name__)

    def list_folder_contents(self, folder_name: str, details: bool = False) -> None:
        folder_path = os.path.join(self.base_path, folder_name)

        if not os.path.exists(folder_path):
            self.logger.error(f"Folder not found: {folder_path}")
            print(f"Error: Folder not found: {folder_name}")
            return

        elements = os.listdir(folder_path)
        print(f"Folder: {folder_path}")
        print(f"Number of elements: {len(elements)}")

        for element in elements:
            element_path = os.path.join(folder_path, element)
            if os.path.isfile(element_path):
                size_mb = os.path.getsize(element_path) / (1024 * 1024)
                last_modified_timestamp = os.path.getmtime(element_path)
                last_modified = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
                print(f"File: {element} ({size_mb:.2f} MB, Last Modified: {last_modified})")
            elif os.path.isdir(element_path):
                last_modified_timestamp = os.path.getmtime(element_path)
                last_modified = datetime.fromtimestamp(last_modified_timestamp).strftime('%Y-%m-%d %H:%M:%S')
                print(f"Folder: {element} (Last Modified: {last_modified})")

    def read_csv(self, filename: str, report_path: Optional[str] = None, summary: bool = False) -> None:
        file_path = os.path.join(self.base_path, filename)

        if not os.path.exists(file_path):
            self.logger.error(f"File not found: {file_path}")
            print(f"Error: File not found: {filename}")
            return

        try:
            df = pd.read_csv(file_path)
            print(f"Columns: {list(df.columns)}")
            print(f"Rows: {len(df)}")

            numeric_stats = {}
            for col in df.select_dtypes(include=np.number).columns:
                numeric_stats[col] = {
                    "Average": df[col].mean(),
                    "Std Dev": df[col].std()
                }

            print(f"Numeric Columns: {numeric_stats}")

            if report_path:
                os.makedirs(report_path, exist_ok=True)
                report_file = os.path.join(report_path, "analysis_report.txt")
                with open(report_file, "w") as report:
                    for col, stats in numeric_stats.items():
                        report.write(f"{col}: Average = {stats['Average']}, Std Dev = {stats['Std Dev']}\n")
                print(f"Saved summary report to {report_file}")

            if summary:
                non_numeric_summary = {}
                for col in df.select_dtypes(exclude=np.number).columns:
                    non_numeric_summary[col] = df[col].value_counts().to_dict()
                print(f"Non-Numeric Summary: {non_numeric_summary}")
        except Exception as e:
            self.logger.error(f"Error processing CSV file: {str(e)}")
            print(f"Error: {str(e)}")

    def read_dicom(self, filename: str, tags: Optional[List[Tuple[int, int]]] = None, extract_image: bool = False) -> None:
        file_path = os.path.join(self.base_path, filename)

        if not os.path.exists(file_path):
            self.logger.error(f"File not found: {file_path}")
            print(f"Error: File not found: {filename}")
            return

        try:
            ds = pydicom.dcmread(file_path)
            print(f"Patient Name: {ds.get((0x0010, 0x0010), 'Unknown')}")
            print(f"Study Date: {ds.get((0x0008, 0x0020), 'Unknown')}")
            print(f"Modality: {ds.get((0x0008, 0x0060), 'Unknown')}")

            if tags:
                for tag in tags:
                    print(f"Tag {tag}: {ds.get(tag, 'Unknown')}")

            if extract_image and hasattr(ds, 'pixel_array'):
                image = ds.pixel_array

                if image.ndim == 3:
                    middle_index = image.shape[0] // 2
                    slice_image = image[middle_index, :, :]
                    plt.imsave(f"{self.base_path}/{os.path.splitext(filename)[0]}_slice_middle.png", slice_image, cmap='gray')
                    print(f"Extracted middle slice saved to {self.base_path}")

                if image.ndim == 2:
                    plt.imsave(f"{self.base_path}/{os.path.splitext(filename)[0]}.png", image, cmap='gray')
                    print(f"Extracted image saved to {self.base_path}")
                else:
                    print(f"Unsupported image dimensions: {image.shape}")
            else:
                print(f"No image data found in the DICOM file.")
            
        except Exception as e:
            self.logger.error(f"Error processing DICOM file: {str(e)}")
            print(f"Error: {str(e)}")