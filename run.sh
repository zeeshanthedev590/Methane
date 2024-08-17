#!/bin/bash

# Prompt for the type of test (folder name)
read -p "Enter the test type (folder name): " TEST_TYPE

# Define the base directory for the files
BASE_DIR="./test/samples"

# Prompt for the file name
read -p "Enter the file name (with .mth extension): " FILE_NAME

# Define the full path to the input file
INPUT_FILE="$BASE_DIR/$TEST_TYPE/$FILE_NAME"



# Run the Python command with the provided inputs
python3 main.py "$INPUT_FILE"
