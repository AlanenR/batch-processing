# Batch Processing Library

## Table of Contents
1. [Overview](#overview)
2. [Features](#features)
3. [Project Structure](#project-structure)
4. [Getting Started](#getting-started)
    - [Clone the Repository](#step-1-clone-the-repo)
    - [Install Dependencies](#step-2-install-the-required-packages)
    - [Running the Application](#step-3-running-the-application)
5. [Testing](#testing)
    - [Running the Tests](#running-the-tests)

## Overview

This Python library is designed to process an array of records of variable sizes and split them into batches suitable for delivery to a system. Each batch is optimized according to predefined limits on the size and number of records, ensuring compatibility with system constraints.

## Features

- **Record Size Limitation**: Discards any record larger than 1 MB.
- **Batch Size Limitation**: Limits the total size of any batch to 5 MB.
- **Record Count Limitation**: Restricts the number of records within a batch to a maximum of 500.

The input for the library is a list of records, and the output is a list of batches, where each batch itself is a list of records.

## Project Structure

- **src/**: Source code for the library.
  - `__init__.py`:
  - `config.py`: Configuration file for record and batch limits.
  - `utils.py`: Utility functions for record validation and processing.
  - `batch_processor.py`: Main module to process records into batches.

- **tests/**: 
  - `__init__.py`:
  - `test_batch_process`: Tests for batch_processor
  - `utils.py`: Tests for utils
  - `test_data.py`: Mock data for testing.

- **main.py**: Example script demonstrating how to use the library.

- **requirements.txt**: Required Python packages.

## Getting Started

Before you begin, ensure you have Python installed on your system.

**Step 1: Clone the repo**

```
$ git clone https://github.com/AlanenR/batch-processing

$ cd ./batch-processing

```

**Step 2: Install the required packages by running:**
  
    - $ pip install -r requirements.txt

**Step 3: Running the application:**

    - $ Run python main.py to start the application.


## Testing

The project is using `pytest` to run automated tests.

**Running the Tests:**

To run all tests, navigate to the project directory and simply use the `pytest` command:

    $ pytest

This command will discover and execute all test cases in the `tests/` directory.

For example, to run tests in the `test_batch_processor.py` file, use:

    $ pytest tests/test_batch_processor.py

## Future improvements

More comprehensive testing, improve performance, and additional error handling scenarios.
