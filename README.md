# Heurist Viz

A tool for visualizing agent interactions, code derived from the ICE repo. This package provides visualization and tracing capabilities for LLM-based agents.

## Installation

You can install the package directly from GitHub:

```bash
pip install git+https://github.com/jorge-re/heurist-viz.git
```

For development installation with additional tools:

```bash
pip install git+https://github.com/jorge-re/heurist-viz.git#egg=heurist-viz[dev]
```

## Usage

Basic usage example:

```python
from heurist_viz import visualize

@visualize
async def run_agent():
    # Your agent code here
    pass

# Run the visualized agent
result = run_agent()
```

## Requirements

- Python 3.7 or higher
- Dependencies are automatically installed with pip
- For development, install with [dev] extras

## Development

To set up for development:

1. Clone the repository
```bash
git clone https://github.com/jorge-re/heurist-viz.git
cd heurist-viz
```

2. Install development dependencies
```bash
pip install -e .[dev]
```

3. Install pre-commit hooks
```bash
pre-commit install
```

## License

This project is licensed under the MIT License - see the LICENSE file for details. 