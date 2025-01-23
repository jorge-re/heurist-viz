from setuptools import setup, find_packages

# Read README.md for long description
from pathlib import Path
this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

setup(
    name="heurist-viz",
    version="0.1.0",
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        "click>=8.0.0",
        "openai>=1.0.0",
        "python-dotenv>=0.19.0",
        "tiktoken>=0.3.0",
        "fvalues>=0.0.4",
        "transformers>=4.0.0",
        "structlog>=22.1.0",
        "nest-asyncio>=1.5.6",
        "questionary>=1.10.0",
        "rich>=12.0.0",
        "diskcache>=5.4.0",
        "aiohttp>=3.8.0",
        "pydantic<2",
        #"pydantic_settings>=2.0.0",
        "typing-extensions>=4.0.0",
        "numpy>=1.20.0",
        "torch>=1.8.0",
        "accelerate>=0.20.0",
        "python-ulid>=1.1.0",
        "fastapi>=0.68.0",
        "uvicorn>=0.15.0",
        "websockets>=10.0",
        "watchfiles>=0.18.0",
        "more-itertools>=8.0.0",
        "httpx>=0.24.0",
        "jinja2>=3.0.0",
        "python-multipart>=0.0.5",
        "typing-inspect>=0.8.0",
        "defopt>=6.0.0",
        "backoff>=2.0.0",
        "docstring-parser>=0.15",
        "ipython>=8.0.0",
        "termcolor>=2.0.0",
        "pandas>=1.0.0",
        "tenacity>=8.0.0",
        "cattrs>=22.2.0",
        "dataclasses-json>=0.5.7",
        "types-requests>=2.28.0",
        "merge-args>=0.1.4",
        "gorilla>=0.4.0",
        "faker>=18.0.0",
        "matplotlib>=3.7.0",
        "nltk>=3.8.0",
        "numerizer>=0.2.0",
        "python-Levenshtein>=0.21.0",
        "rouge-metric>=1.0.1",
        "ruamel.yaml>=0.17.0",
        "scikit-learn>=1.2.0",
        "thefuzz>=0.19.0",
        "tqdm>=4.65.0",
        "protobuf>=4.22.0",
        "sentencepiece>=0.1.97",
        "requests>=2.28.0",
        "pyyaml>=6.0.0",
    ],
    extras_require={
        'dev': [
            "pytest>=7.0.0",
            "black>=22.0.0",
            "flake8>=4.0.0",
            "mypy>=0.900",
            "isort>=5.10.0",
            "pytest-asyncio>=0.20.0",
            "pytest-cov>=4.0.0",
            "pytest-timeout>=2.1.0",
            "autoflake",
            "pre-commit",
            "pylint",
            "pytest-mock",
        ]
    },
    author="Jorge RE",
    author_email="jorge@heurist.ai",
    description="Heurist Trace Visualizer",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/jorge-re/heurist-viz",
    project_urls={
        "Bug Tracker": "https://github.com/jorge-re/heurist-viz/issues",
        "Documentation": "https://github.com/jorge-re/heurist-viz#readme",
        "Source Code": "https://github.com/jorge-re/heurist-viz",
    },
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Topic :: Software Development :: Testing",
        "Topic :: Software Development :: Debuggers",
    ],
    keywords="visualization, tracing, debugging, agents, llm",
    python_requires=">=3.7",
) 