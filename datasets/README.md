# Datasets

This directory contains datasets and data-related resources for the course.

## Important Notes
⚠️ **Large data files are NOT stored in this repository**  
- The `.gitignore` excludes common data formats
- Download links are provided instead
- Processed/cleaned datasets may be included if small enough

## Dataset Categories

### 1. Image Datasets
- **MNIST** - Handwritten digits (lectures & labs)
- **CIFAR-10/100** - Small natural images
- **ImageNet subset** - For transfer learning
- **Fashion-MNIST** - Fashion product images
- **Custom datasets** - Domain-specific images

### 2. Text Datasets
- **IMDB Reviews** - Sentiment analysis
- **20 Newsgroups** - Text classification
- **Penn Treebank** - Language modeling
- **WikiText** - Large-scale text corpus
- **Custom corpora** - Domain-specific text

### 3. Tabular Datasets
- **Titanic** - Binary classification
- **Boston Housing** - Regression
- **Wine Quality** - Multi-class classification
- **Credit Card Fraud** - Imbalanced classification
- **Customer Churn** - Business analytics

### 4. Time Series
- **Stock Prices** - Financial forecasting
- **Weather Data** - Climate prediction
- **Sensor Readings** - Anomaly detection
- **Energy Consumption** - Demand forecasting

## Data Sources

### Public Repositories
- [Kaggle Datasets](https://www.kaggle.com/datasets)
- [UCI Machine Learning Repository](https://archive.ics.uci.edu/ml/)
- [Google Dataset Search](https://datasetsearch.research.google.com/)
- [Papers with Code Datasets](https://paperswithcode.com/datasets)
- [HuggingFace Datasets](https://huggingface.co/datasets)
- [TensorFlow Datasets](https://www.tensorflow.org/datasets)
- [PyTorch Datasets](https://pytorch.org/vision/stable/datasets.html)

### Academic Sources
- [OpenML](https://www.openml.org/)
- [Data.gov](https://www.data.gov/)
- [AWS Open Data](https://registry.opendata.aws/)
- [Microsoft Research Open Data](https://msropendata.com/)

## Dataset Download Instructions

### Using TensorFlow Datasets
```python
import tensorflow_datasets as tfds

# Load dataset
dataset, info = tfds.load('mnist', with_info=True)
train_data, test_data = dataset['train'], dataset['test']
```

### Using PyTorch
```python
from torchvision import datasets, transforms

# Download and load dataset
train_dataset = datasets.CIFAR10(
    root='./data',
    train=True,
    download=True,
    transform=transforms.ToTensor()
)
```

### Using scikit-learn
```python
from sklearn.datasets import load_digits, fetch_openml

# Load built-in dataset
digits = load_digits()

# Fetch from OpenML
mnist = fetch_openml('mnist_784', version=1)
```

### Manual Download
For large or custom datasets:
1. Download from source (link provided in assignment/lab)
2. Extract to appropriate directory
3. Verify file integrity (checksums if provided)
4. Update paths in code

## Dataset Structure

```
datasets/
├── README.md (this file)
├── processed/          # Small processed datasets
│   ├── sample_data.csv
│   └── README.md
├── raw/               # Raw data (gitignored)
│   └── .gitkeep
├── external/          # External data links
│   └── download_links.md
└── scripts/           # Data processing scripts
    ├── download_data.py
    ├── preprocess.py
    └── augment.py
```

## Data Processing Guidelines

### Data Preprocessing
Common preprocessing steps:
- Handle missing values
- Remove duplicates
- Normalize/standardize features
- Encode categorical variables
- Split into train/validation/test sets

### Data Augmentation
For image data:
- Random rotations, flips, crops
- Color jittering
- Mixup/CutMix

For text data:
- Synonym replacement
- Back translation
- Random insertion/deletion

### Best Practices
✅ Document data sources and licenses  
✅ Keep raw data separate from processed data  
✅ Use reproducible preprocessing scripts  
✅ Validate data quality and distributions  
✅ Create data dictionaries explaining features  
✅ Version your datasets  
✅ Include sample data for testing  

## Dataset Licenses

Always check and respect dataset licenses:
- Some datasets are for academic use only
- Commercial use may require permission
- Cite datasets in your work
- Follow attribution requirements

## Data Ethics

When working with data:
- Respect privacy and confidentiality
- Be aware of potential biases
- Consider fairness implications
- Anonymize sensitive information
- Follow institutional review board (IRB) requirements

## Creating Your Own Dataset

For projects requiring custom data:
1. Define clear data requirements
2. Identify data sources
3. Collect data ethically and legally
4. Document collection process
5. Clean and validate data
6. Create comprehensive documentation
7. Consider sharing (with proper licensing)

## Troubleshooting

**Download fails?**
- Check internet connection
- Try alternative mirrors
- Download manually from source

**Out of memory?**
- Use data generators/loaders
- Process in batches
- Use smaller subset for testing
- Optimize data types (float32 vs float64)

**Data format issues?**
- Check file encoding
- Verify delimiter for CSV files
- Validate file integrity
- Read documentation carefully

## Need Help?
- Check FAQ.md
- Search course discussion forum
- Ask in office hours
- Email instructor/TA with specific questions

Remember: Good data is the foundation of good machine learning!
