# Batch Processing Library

## Overview

This Python library is designed to process an array of records of variable sizes and split them into batches suitable for delivery to a system. Each batch is optimized according to predefined limits on the size and number of records, ensuring compatibility with system constraints.

## Features

- **Record Size Limitation**: Discards any record larger than 1 MB.
- **Batch Size Limitation**: Limits the total size of any batch to 5 MB.
- **Record Count Limitation**: Restricts the number of records within a batch to a maximum of 500.

The input for the library is a list of records, and the output is a list of batches, where each batch itself is a list of records.

## Project Structure

/project_root
│
├── /src
│ ├── init.py
│ ├── config.py # Configuration file for setting limits for records.
│ ├── utils.py # Utility functions for record validation and processing.
│ └── batch_processor.py # Main module to process records into batches.
│
├── /tests # Test directory for unit tests.
│ ├── TODO
│ 
│
├── main.py # Example script demonstrating how to use the library.
└── requirements.txt # Required Python packages. (TODO)