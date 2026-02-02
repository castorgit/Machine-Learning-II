# Setup Guide for Machine Learning II

This guide will help you set up your development environment for the Machine Learning II course.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Verification](#verification)
4. [Troubleshooting](#troubleshooting)
5. [IDE Setup](#ide-setup)
6. [GPU Configuration](#gpu-configuration)

## Prerequisites

### Required Software
- **Python 3.8 or higher** (3.9 or 3.10 recommended)
- **Git** for version control
- **pip** (Python package installer)
- 8GB+ RAM recommended
- 20GB+ free disk space

### Optional but Recommended
- **Anaconda** or **Miniconda** for package management
- **GPU** (NVIDIA) for faster training (not required)
- **CUDA** and **cuDNN** (if using GPU)

## Installation Steps

### Option 1: Using pip (Recommended)

#### 1. Install Python
**macOS:**
```bash
brew install python@3.9
```

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3.9 python3.9-venv python3-pip
```

**Windows:**
Download from [python.org](https://www.python.org/downloads/) and run installer.
Make sure to check "Add Python to PATH"!

#### 2. Clone Repository
```bash
git clone https://github.com/castorgit/Machine-Learning-II.git
cd Machine-Learning-II
```

#### 3. Create Virtual Environment
**macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

You should see `(venv)` in your terminal prompt.

#### 4. Install Dependencies
```bash
# Upgrade pip first
pip install --upgrade pip

# Install all requirements
pip install -r requirements.txt
```

This will install:
- NumPy, Pandas, SciPy (data manipulation)
- scikit-learn (traditional ML)
- TensorFlow & Keras (deep learning)
- PyTorch & torchvision (deep learning)
- Matplotlib, Seaborn, Plotly (visualization)
- Jupyter Lab (notebooks)
- And more...

#### 5. Install Jupyter Extensions (Optional)
```bash
pip install jupyter_contrib_nbextensions
jupyter contrib nbextension install --user
```

### Option 2: Using Conda

#### 1. Install Anaconda/Miniconda
Download from [anaconda.com](https://www.anaconda.com/products/distribution) or [conda.io](https://docs.conda.io/en/latest/miniconda.html)

#### 2. Create Conda Environment
```bash
# Clone repository
git clone https://github.com/castorgit/Machine-Learning-II.git
cd Machine-Learning-II

# Create environment with Python 3.9
conda create -n ml2 python=3.9

# Activate environment
conda activate ml2
```

#### 3. Install Dependencies
```bash
# Install from requirements.txt
pip install -r requirements.txt

# Or use conda for main packages
conda install numpy pandas scipy scikit-learn matplotlib seaborn jupyter

# Then pip for ML frameworks
pip install tensorflow torch torchvision
```

### Option 3: Using Google Colab (No Installation)

If you don't want to set up locally, use Google Colab:

1. Go to [colab.research.google.com](https://colab.research.google.com/)
2. Sign in with Google account
3. Upload notebooks or connect to GitHub
4. Install additional packages as needed:
   ```python
   !pip install package-name
   ```

**Pros**: Free GPU access, no setup  
**Cons**: Session timeouts, file management

## Verification

### Test Your Installation

#### 1. Check Python Version
```bash
python --version
# Should show Python 3.8.x or higher
```

#### 2. Test Package Imports
Create a test script `test_setup.py`:

```python
#!/usr/bin/env python3
"""Test script to verify ML environment setup."""

import sys
print(f"Python version: {sys.version}")

packages = {
    'numpy': 'np',
    'pandas': 'pd',
    'scipy': 'scipy',
    'sklearn': 'sklearn',
    'tensorflow': 'tf',
    'torch': 'torch',
    'matplotlib': 'plt',
    'seaborn': 'sns',
    'jupyter': None,
}

print("\nChecking package imports...")
errors = []

for package, alias in packages.items():
    try:
        if alias:
            exec(f"import {package} as {alias}")
        else:
            exec(f"import {package}")
        print(f"✓ {package}")
    except ImportError as e:
        print(f"✗ {package}: {e}")
        errors.append(package)

if errors:
    print(f"\n⚠️  Failed to import: {', '.join(errors)}")
    print("Please install missing packages.")
else:
    print("\n✅ All packages successfully imported!")
    
# Check versions
print("\nPackage versions:")
import numpy as np
import pandas as pd
import sklearn
import tensorflow as tf
import torch

print(f"NumPy: {np.__version__}")
print(f"Pandas: {pd.__version__}")
print(f"scikit-learn: {sklearn.__version__}")
print(f"TensorFlow: {tf.__version__}")
print(f"PyTorch: {torch.__version__}")

# Check GPU availability
print("\nGPU Status:")
print(f"TensorFlow GPU available: {len(tf.config.list_physical_devices('GPU')) > 0}")
print(f"PyTorch GPU available: {torch.cuda.is_available()}")
if torch.cuda.is_available():
    print(f"PyTorch GPU device: {torch.cuda.get_device_name(0)}")
```

Run the test:
```bash
python test_setup.py
```

#### 3. Launch Jupyter
```bash
jupyter lab
# or
jupyter notebook
```

Your browser should open with Jupyter interface.

## Troubleshooting

### Common Issues

#### "pip not found"
```bash
# macOS/Linux
python3 -m ensurepip --upgrade

# Windows
python -m ensurepip --upgrade
```

#### "Permission denied" when installing packages
Don't use `sudo` with pip! Use virtual environment instead.
```bash
# Create and activate venv
python3 -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

#### TensorFlow installation fails
```bash
# Install CPU-only version
pip install tensorflow-cpu

# Or specific version
pip install tensorflow==2.13.0
```

#### PyTorch installation fails
Visit [pytorch.org](https://pytorch.org/get-started/locally/) for platform-specific instructions.

For CPU only:
```bash
pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu
```

#### Jupyter kernel not found
```bash
python -m ipykernel install --user --name=ml2
```

#### Out of memory errors
- Reduce batch size in code
- Use Google Colab with GPU
- Close other applications
- Use data generators instead of loading all data

#### Import errors in Jupyter
Make sure Jupyter is using the correct kernel:
- Kernel → Change Kernel → Select your environment

### Platform-Specific Issues

#### macOS M1/M2 (Apple Silicon)
TensorFlow and PyTorch have special builds:

```bash
# TensorFlow for M1/M2
pip install tensorflow-macos
pip install tensorflow-metal  # GPU acceleration

# PyTorch for M1/M2
pip install torch torchvision
```

#### Windows
If you encounter DLL errors:
- Install [Microsoft Visual C++ Redistributable](https://aka.ms/vs/17/release/vc_redist.x64.exe)
- Use Anaconda (handles dependencies better on Windows)

#### Linux
Make sure you have development tools:
```bash
sudo apt install build-essential python3-dev
```

## IDE Setup

### VS Code (Recommended)

1. **Install VS Code**: [code.visualstudio.com](https://code.visualstudio.com/)

2. **Install Extensions**:
   - Python (Microsoft)
   - Jupyter (Microsoft)
   - Pylance (Microsoft)
   - GitLens

3. **Configure Python Interpreter**:
   - Ctrl/Cmd + Shift + P
   - "Python: Select Interpreter"
   - Choose your virtual environment

4. **Useful Settings**:
```json
{
    "python.linting.enabled": true,
    "python.linting.pylintEnabled": true,
    "python.formatting.provider": "black",
    "editor.formatOnSave": true
}
```

### PyCharm

1. **Install PyCharm**: [jetbrains.com/pycharm](https://www.jetbrains.com/pycharm/)
2. **Open Project**: File → Open → Select repository folder
3. **Configure Interpreter**: Settings → Project → Python Interpreter
4. **Add virtual environment** created earlier

### Jupyter Lab Extensions
```bash
# Install extensions
pip install jupyterlab-git
pip install jupyterlab-code-formatter
pip install black isort

# Enable extensions
jupyter labextension install @jupyterlab/toc
```

## GPU Configuration

### NVIDIA GPU Setup (Optional)

#### Check GPU
```bash
# Linux/Windows
nvidia-smi
```

#### Install CUDA & cuDNN

**Ubuntu:**
```bash
# CUDA Toolkit
wget https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/cuda-ubuntu2004.pin
sudo mv cuda-ubuntu2004.pin /etc/apt/preferences.d/cuda-repository-pin-600
sudo apt-key adv --fetch-keys https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/3bf863cc.pub
sudo add-apt-repository "deb https://developer.download.nvidia.com/compute/cuda/repos/ubuntu2004/x86_64/ /"
sudo apt update
sudo apt install cuda
```

**Windows:**
Download from [NVIDIA CUDA Toolkit](https://developer.nvidia.com/cuda-downloads)

#### Verify GPU in TensorFlow
```python
import tensorflow as tf
print("Num GPUs Available: ", len(tf.config.list_physical_devices('GPU')))
```

#### Verify GPU in PyTorch
```python
import torch
print(f"CUDA available: {torch.cuda.is_available()}")
print(f"CUDA version: {torch.version.cuda}")
print(f"GPU device: {torch.cuda.get_device_name(0)}")
```

## Next Steps

✅ Environment is set up!  
✅ All packages installed  
✅ Jupyter is working  

Now you can:
1. Explore `notebooks/tutorials/` for introductory material
2. Start working on `labs/` exercises
3. Review `lectures/` content
4. Begin `assignments/` when assigned

## Getting Help

If you're still having issues:
1. Check [FAQ.md](FAQ.md)
2. Search course discussion forum
3. Attend office hours
4. Email instructor/TA with:
   - Your OS and version
   - Python version (`python --version`)
   - Error messages (full output)
   - What you've tried

---

**Happy Learning! 🚀**
