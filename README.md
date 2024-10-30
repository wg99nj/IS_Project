# Calculator Project

## Overview

This project is an interactive command-line calculator supporting basic arithmetic and statistical operations, such as addition, subtraction, division, mean, and median. With history management provided by Pandas, environment variable configuration, and a plugin-based architecture, it is both flexible and extendable.

## Features

- **Basic Calculator Operations**: Addition, subtraction, division, mean, and median calculations.
- **History Management**: Uses Pandas to store and manage a calculation history.
- **Environment Configuration**: Configurable settings through environment variables.
- **REPL Interface**: Command-line interface for user-friendly interactions.
- **Plugin Architecture**: Commands are implemented as plugins for modularity.
- **Testing**: High coverage with Pytest.
- **Logging**: Tracks and logs operations and errors.

## Setup Instructions

### Prerequisites

- Python 3.8 or higher
- Pip
- Virtual environment setup recommended

### Installation 

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/yourusername/calculator_project.git
   cd calculator_project
   ```

2. **Set up Virtual Environment**:
```bash
python -m venv env
source env/bin/activate
```

3. **Install Dependencies**:
```bash
pip install -r requirements.txt
```

4. **create a env.**:
```plaintext
ENVIRONMENT=development
```
### Usage 
1. **Run the calculator in interactive mode**:
```plaintext
python main.py
```

2. **enter commands like**:
```plaintext
> add 3 5
> mean 5 10 15
> history
> exit
```

## Design Patterns

### Design Commands

The Command Pattern is used to encapsulate calculator operations into separate command classes, making the application easily extensible for new operations. Each command (e.g., add, subtract) implements an execute() method, enabling consistent invocation from the REPL interface.

### Plugin Architecture

A plugin-based design is employed to dynamically load calculator commands, allowing commands to be modular and the program to auto-detect and integrate them. This setup simplifies adding new functionality without modifying the core code.

## Testing

This project includes comprehensive testing using pytest to ensure functionality and maintain code quality. Run the following command to execute tests:
```bash
pytest --cov=calculator --cov-report=term-missing
```

## Logging 

Logging is configured to capture important events, including errors and usage information. Logs are output to calculator.log for analysis and debugging purposes.

## Configuration

Application configurations are managed through environment variables stored in the .env file, which can control behavior across different environments (development, production, etc.).

## Commit History 

To ensure traceable development progress, commit messages are structured to be informative and grouped logically by feature or fix. Code quality is maintained with linting and adherence to standard Python coding practices.

















