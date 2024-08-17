#!/bin/bash

# Prompt for the type of test (folder name)
read -p "Enter the test type (folder name): " TEST_TYPE

# Define the base directory for the files
BASE_DIR="./test/samples"

# Create the test type directory if it doesn't exist
mkdir -p "$BASE_DIR/$TEST_TYPE"

# Prompt for the file name
read -p "Enter the file name (with .mth extension): " FILE_NAME

# Define the full path to the test file
TEST_FILE="$BASE_DIR/$TEST_TYPE/$FILE_NAME"

# Create an empty file with the specified name
touch "$TEST_FILE"

echo "Blank test file $TEST_FILE created."
