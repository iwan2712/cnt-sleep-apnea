from dataclasses import dataclass
import numpy as np
from sklearn.metrics import roc_auc_score

@dataclass
class Metrics:
    acc: float
    sen: float
    spec: float
    auc: float

def confusion_to_metrics(tp: int, tn: int, fp: int, fn: int, y_true=None, y_score=None) -> Metrics:
    # Accuracy
    total = tp + tn + fp + fn
    acc = (tp + tn) / total if total else 0.0

    # Sensitivity (Recall positive)
    sen = tp / (tp + fn) if (tp + fn) else 0.0

    # Specificity (Recall negative)
    spec = tn / (tn + fp) if (tn + fp) else 0.0

    # AUC (requires scores)
    auc = 0.0
    if y_true is not None and y_score is not None:
        try:
            auc = float(roc_auc_score(y_true, y_score))
        except Exception:
            auc = 0.0

    return Metrics(acc=acc, sen=sen, spec=spec, auc=auc)
