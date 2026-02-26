# DollarImport

DollarImport allows you to use `$`-style variable substitution (`${var}`) in your Python code.  

## Installation

```bash
pip install dollarimport
```

## Usage

To safely run code with `${…}` syntax, you should import `dollarimport` in your package’s `__init__.py` **before importing your own code**.

### Example Structure

```
my_package/
├─ __init__.py
├─ my_module.py
```

### `__init__.py`

```
import dollarimport
dollarimport.enable()   # enable $ syntax

# now import your own modules
from . import my_module
```

### `my_module.py`

```
x = 42
#$ print(${x})   # use $ syntax on lines starting with #$
y = 10
#$ print(${y} + 5)
```

### Notes

- Only lines prefixed with `#$` are transformed by DollarImport.  
- Regular Python code works normally.  
- Always enable DollarImport **before importing your own modules** so that the `$` syntax is processed.  

Now you can simply import your package as usual:

```
import my_package
```
