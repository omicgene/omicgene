"""Scientific utility functions: metrics, seeds, and clinical error rates."""

import random
from typing import Dict, Any
import numpy as np

def set_seed(seed: int = 42) -> None:
    """Sets random seeds for reproducibility."""
    random.seed(seed)
    np.random.seed(seed)

def compute_clinical_errors(y_true: np.ndarray, y_pred: np.ndarray) -> Dict[str, float]:
    """Computes Very Major Error (VME) and Major Error (ME) rates.
    
    Very Major Error (VME): True Resistant (1) classified as Susceptible (0) -> False Susceptible.
    Major Error (ME): True Susceptible (0) classified as Resistant (1) -> False Resistant.
    """
    y_true = np.asarray(y_true)
    y_pred = np.asarray(y_pred)
    
    total_resistant = np.sum(y_true == 1)
    total_susceptible = np.sum(y_true == 0)
    
    vme = np.sum((y_true == 1) & (y_pred == 0)) / max(total_resistant, 1)
    me = np.sum((y_true == 0) & (y_pred == 1)) / max(total_susceptible, 1)
    
    return {
        "vme_rate": float(vme),
        "me_rate": float(me),
        "accuracy": float(np.mean(y_true == y_pred)),
    }
