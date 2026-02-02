# Notebooks

This directory contains Jupyter notebooks for tutorials, examples, and demonstrations.

## Directory Structure

### `tutorials/`
Step-by-step learning notebooks covering fundamental concepts:
- Introduction to deep learning frameworks
- Data preprocessing techniques
- Model building and training
- Evaluation and visualization
- Deployment basics

### `examples/`
Complete working examples demonstrating:
- End-to-end ML pipelines
- Real-world applications
- Best practices
- Common patterns and solutions

## How to Use Notebooks

### Setup
1. Ensure Jupyter is installed: `pip install jupyter`
2. Start Jupyter: `jupyter notebook` or `jupyter lab`
3. Navigate to the desired notebook
4. Run cells sequentially

### Running in Google Colab
1. Upload notebook to Google Drive
2. Open with Google Colab
3. Enable GPU if needed: Runtime → Change runtime type → GPU
4. Install additional packages as needed

### Best Practices
- Run cells in order (top to bottom)
- Restart kernel if encountering issues
- Clear outputs before committing: Cell → All Output → Clear
- Add markdown cells to document your thought process
- Save frequently

## Notebook Topics

### Tutorials
1. **PyTorch Basics**
   - Tensors and operations
   - Autograd and backpropagation
   - Building neural networks
   - Training loops

2. **TensorFlow/Keras Basics**
   - Sequential and Functional API
   - Custom layers and models
   - Callbacks and training
   - Model saving and loading

3. **Data Preprocessing**
   - Data cleaning techniques
   - Feature engineering
   - Handling imbalanced data
   - Data augmentation

4. **Model Evaluation**
   - Cross-validation strategies
   - Metrics selection
   - Visualization techniques
   - Error analysis

5. **Hyperparameter Tuning**
   - Grid search
   - Random search
   - Bayesian optimization
   - Using Optuna

### Examples
1. **Image Classification**
   - CIFAR-10 with CNN
   - Transfer learning with ResNet
   - Data augmentation strategies
   - Model interpretation

2. **Text Classification**
   - Sentiment analysis with RNN
   - LSTM for sequence modeling
   - Using pre-trained embeddings
   - Attention mechanisms

3. **Time Series Forecasting**
   - Stock price prediction
   - LSTM for sequences
   - Feature engineering
   - Evaluation metrics

4. **Generative Models**
   - VAE implementation
   - Simple GAN
   - Training tips and tricks
   - Result visualization

5. **Model Deployment**
   - Saving and loading models
   - Creating REST API
   - Serving predictions
   - Performance optimization

## Creating Your Own Notebooks

### Structure
```python
# 1. Imports and Setup
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# 2. Load and Explore Data
# Load your data
# Visualize and understand

# 3. Preprocess Data
# Clean, transform, split

# 4. Build Model
# Define architecture
# Compile/configure

# 5. Train Model
# Fit on training data
# Monitor validation metrics

# 6. Evaluate Model
# Test set performance
# Visualize results

# 7. Conclusions
# Summarize findings
# Discuss improvements
```

### Documentation
- Use markdown cells for explanations
- Add comments in code cells
- Include visualizations
- Document assumptions and decisions
- Provide references

### Code Quality
- Follow PEP 8 style guidelines
- Use meaningful variable names
- Keep cells focused and small
- Avoid very long cells
- Modularize repeated code

## Tips for Effective Notebooks

### Organization
✅ Clear section headers  
✅ Logical flow from start to finish  
✅ Balance code and explanation  
✅ Include data exploration  
✅ Show intermediate results  

### Visualization
✅ Label axes and add titles  
✅ Use appropriate plot types  
✅ Include legends  
✅ Choose readable color schemes  
✅ Show multiple perspectives  

### Experimentation
✅ Try different hyperparameters  
✅ Compare multiple models  
✅ Visualize learning curves  
✅ Analyze errors and failures  
✅ Document what works and why  

## Common Issues

**Kernel Dies**
- Reduce batch size or model size
- Clear variables: `del variable_name`
- Restart kernel and clear output

**Import Errors**
- Install missing packages
- Check package versions
- Restart kernel after installation

**Slow Execution**
- Use GPU if available
- Reduce data size for testing
- Optimize data loading
- Profile code to find bottlenecks

**Reproducibility Issues**
- Set random seeds
- Document package versions
- Use virtual environments
- Test in clean environment

## Resources

### Learning Resources
- [Jupyter Notebook Documentation](https://jupyter-notebook.readthedocs.io/)
- [JupyterLab Documentation](https://jupyterlab.readthedocs.io/)
- [Google Colab Guide](https://colab.research.google.com/)

### Extensions
- jupyterlab-toc: Table of contents
- jupyterlab-git: Git integration
- jupyterlab-code-formatter: Auto-formatting
- nbdime: Notebook diffing

### Tips
- Use `%time` and `%%time` for timing
- Use `%debug` for debugging
- Use `%load_ext` for extensions
- Use `!command` for shell commands

## Contributing
Students: Share interesting notebooks via pull requests  
Instructors: Add new tutorials and examples following the structure above

Happy coding! 🎉
