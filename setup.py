"""
Setup configuration for ARTHEON-SAST package
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="artheon-sast",
    version="1.0.0",
    author="Dorian Tituana",
    author_email="dorian.tituana@epn.edu.ec",
    description="Static Application Security Testing con Google Gemini",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/DorianTitu/SAST-IA-Robusto",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Security",
    ],
    python_requires=">=3.8",
    install_requires=[
        "fastapi==0.104.1",
        "uvicorn==0.24.0",
        "pydantic==2.5.0",
        "python-multipart==0.0.6",
        "google-genai==0.3.0",
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "pytest-cov>=3.0",
            "black>=22.0",
            "flake8>=4.0",
            "mypy>=0.900",
        ],
        "mongodb": ["pymongo>=4.0"],
    },
    entry_points={
        "console_scripts": [
            "artheon-sast=artheon_sast.cli:main",
        ],
    },
)
