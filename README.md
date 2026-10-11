# dollarimport

Enables `${var}` syntax in Python using `exec` and `globals`.

## Architecture Overview

The `dollarimport` repository is a Python package designed to extend the capabilities of Python's import system. It introduces a custom loader (`DollarLoader`) and finder (`DollarFinder`) that modify how Python source files are processed during the import phase. Specifically, it allows for the execution of code embedded within comments prefixed with `#$`, enabling dynamic variable interpolation similar to shell scripting.

- **`dollarimport/__init__.py`**: This file serves as the entry point for the package, providing a single function `enable()` that activates the custom loader and finder.
  
- **`dollarimport/loader.py`**: Contains the implementation of `DollarLoader` and `DollarFinder`. The `DollarLoader` class overrides the `source_to_code` method to preprocess source files by replacing lines starting with `#$` with equivalent `exec` statements. The `DollarFinder` class is responsible for identifying Python modules that should be processed using the custom loader.

- **`pyproject.toml`**: Configuration file for building and distributing the package, specifying dependencies, metadata, and build settings.

- **`tests/test_basic.py`**: A basic test suite to verify the functionality of the `dollarimport` package.

## Tech Stack

- **Programming Language**: Python
- **Build System**: setuptools
- **Package Management**: pyproject.toml
- **Testing Framework**: unittest (via `tests/test_basic.py`)

## Getting Started / Setup Guide

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/dollarimport.git
   cd dollarimport
   ```

2. **Install Dependencies**:
   Ensure you have Python 3.8 or higher installed. Then, install the package using pip:
   ```bash
   python -m pip install .
   ```

3. **Enable the Custom Loader**:
   In your Python script, import and enable the custom loader:
   ```python
   import dollarimport
   dollarimport.enable()
   ```

4. **Use `${var}` Syntax in Your Code**:
   You can now use `#$` comments to execute code dynamically. For example:
   ```python
   # Define a variable
   my_var = "Hello, World!"

   #$ print(my_var)
   ```

5. **Run Tests**:
   To verify the functionality, run the test suite:
   ```bash
   python -m unittest discover tests
   ```

This setup allows you to leverage dynamic code execution within your Python modules, enhancing flexibility and potentially simplifying certain development tasks.