# EpochCLI

A command-line tool for timestamp operations, including creating files with timestamp prefixes and converting Unix timestamps to readable dates.

## Installation

### Requirements
Python version >= 3.10

### Development Installation

To install and uninstall the package in development mode:

```bash
# Clone the repository
git clone https://github.com/ElyasAguiar/epochcli.git
cd epochcli

# Install in development mode
pip install -e .

# Uninstall in development mode
pip uninstall epochcli
```

## Usage

After installation, you can use the following commands:

### Creating Files with Timestamp Prefix

```bash
# Create a file with timestamp prefix
epochcli create filename.txt

# Create a file in a specific directory
epochcli create filename.txt --dir /path/to/directory
```

### Converting Unix Timestamps

```bash
# Convert a Unix timestamp (in seconds)
epochcli convert 1630000000

# Convert a Unix timestamp in milliseconds
epochcli convert 1630000000000 --ms
```

## Features

- Creates files with Unix timestamp prefixes using GMT-03:00 (America/Sao_Paulo) timezone
- Converts Unix timestamps to human-readable dates
- Supports both seconds and milliseconds timestamp formats
