"""
Data loading utilities for Machine Learning II course.

This module provides helper functions for loading and preprocessing datasets.
"""

import numpy as np
import pandas as pd
from typing import Tuple, Optional


def load_csv_dataset(filepath: str, 
                     target_column: str,
                     test_size: float = 0.2,
                     random_state: int = 42) -> Tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    """
    Load a CSV dataset and split into train/test sets.
    
    Args:
        filepath: Path to the CSV file
        target_column: Name of the target variable column
        test_size: Proportion of data to use for testing (default: 0.2)
        random_state: Random seed for reproducibility (default: 42)
    
    Returns:
        Tuple of (X_train, X_test, y_train, y_test)
    
    Example:
        >>> X_train, X_test, y_train, y_test = load_csv_dataset(
        ...     'data.csv', 
        ...     target_column='label'
        ... )
    """
    from sklearn.model_selection import train_test_split
    
    # Load data
    df = pd.read_csv(filepath)
    
    # Split features and target
    X = df.drop(columns=[target_column]).values
    y = df[target_column].values
    
    # Split into train/test
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state
    )
    
    return X_train, X_test, y_train, y_test


def normalize_features(X_train: np.ndarray, 
                       X_test: np.ndarray,
                       method: str = 'standard') -> Tuple[np.ndarray, np.ndarray]:
    """
    Normalize features using specified method.
    
    Args:
        X_train: Training features
        X_test: Test features
        method: Normalization method - 'standard' or 'minmax' (default: 'standard')
    
    Returns:
        Tuple of (X_train_normalized, X_test_normalized)
    
    Example:
        >>> X_train_norm, X_test_norm = normalize_features(X_train, X_test, method='standard')
    """
    if method == 'standard':
        from sklearn.preprocessing import StandardScaler
        scaler = StandardScaler()
    elif method == 'minmax':
        from sklearn.preprocessing import MinMaxScaler
        scaler = MinMaxScaler()
    else:
        raise ValueError(f"Unknown method: {method}. Use 'standard' or 'minmax'")
    
    X_train_normalized = scaler.fit_transform(X_train)
    X_test_normalized = scaler.transform(X_test)
    
    return X_train_normalized, X_test_normalized


def load_image_dataset(directory: str,
                       image_size: Tuple[int, int] = (224, 224),
                       batch_size: int = 32,
                       validation_split: float = 0.2):
    """
    Load image dataset from directory structure.
    
    Args:
        directory: Root directory containing class subdirectories
        image_size: Target size for images (height, width)
        batch_size: Batch size for data loading
        validation_split: Proportion of data for validation
    
    Returns:
        Training and validation data generators
    
    Example:
        >>> train_gen, val_gen = load_image_dataset('path/to/images')
    """
    from tensorflow.keras.preprocessing.image import ImageDataGenerator
    
    datagen = ImageDataGenerator(
        rescale=1./255,
        validation_split=validation_split
    )
    
    train_generator = datagen.flow_from_directory(
        directory,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='training'
    )
    
    validation_generator = datagen.flow_from_directory(
        directory,
        target_size=image_size,
        batch_size=batch_size,
        class_mode='categorical',
        subset='validation'
    )
    
    return train_generator, validation_generator


def create_sequences(data: np.ndarray,
                     sequence_length: int,
                     target_offset: int = 1) -> Tuple[np.ndarray, np.ndarray]:
    """
    Create sequences for time series or sequential data.
    
    Args:
        data: Input data array
        sequence_length: Length of input sequences
        target_offset: Offset for target values (default: 1 for next-step prediction)
    
    Returns:
        Tuple of (sequences, targets)
    
    Example:
        >>> sequences, targets = create_sequences(time_series_data, sequence_length=10)
    """
    sequences = []
    targets = []
    
    for i in range(len(data) - sequence_length - target_offset + 1):
        seq = data[i:i + sequence_length]
        target = data[i + sequence_length + target_offset - 1]
        sequences.append(seq)
        targets.append(target)
    
    return np.array(sequences), np.array(targets)


if __name__ == '__main__':
    # Example usage
    print("Data loader utilities for ML-II course")
    print(f"Available functions: {[f for f in dir() if not f.startswith('_')]}")
