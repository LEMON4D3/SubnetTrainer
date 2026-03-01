# Subnet Trainer

A subnet training application that helps users learn and practice subnetting concepts. The application uses a C++ backend with a Python (PyQt6) frontend.

## Requirements

- Python 3.x
- PyQt6
- pybind11
- CMake 3.15+
- C++ Compiler (MSVC on Windows)

## Installation

### Python Dependencies
```bash
pip install PyQt6 pybind11
```

### Building the C++ Backend
```bash
mkdir build
cd build
cmake ..
cmake --build . --config Release
```

## Usage

> [!IMPORTANT]
> **`main.py` must be placed in the same directory as the `.exe` file.**
> The C++ executable calls Python functions at runtime and will not work otherwise.

1. Build the project
2. Copy `main.py` to the same directory as the executable
3. Run `main.exe`

## Project Structure
```
Subnet Trainer/
├── CMakeLists.txt
├── main.cpp
├── main.py
├── README.md
└── bin/
    └── main.exe
```

## Features

- Random IP address generation
- Subnet mask calculation
- Network address calculation
- Broadcast address calculation

## How It Works

The C++ executable embeds a Python interpreter using **pybind11** and calls functions defined in `main.py`. The UI is built with **PyQt6**.

## License

MIT License