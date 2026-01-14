# An Explainable Spatial–Temporal Transformer Framework with Time-Stretch Encoding for Cross-Dataset Sleep Apnea Detection

**CN-T Spatial–Temporal Network (TCN + Transformer) with Time-Stretch Encoding** for robust, explainable, cross-dataset obstructive sleep apnea (OSA) detection from multimodal physiological signals.

> This repository will contain the full implementation (model code, training/evaluation scripts, configs) for reproducible research (subject to dataset access constraints).

---

## Authors

- **Shih-Chung Chen**  
- **Irawan Dwi Wahyono** (Corresponding Author)

**Affiliation:** Department of Electrical Engineering, Southern Taiwan University of Science and Technology (STUST), Tainan, Taiwan.  
**Contact:** Irawan Dwi Wahyono — db02b201@stust.edu.tw

---

## Summary (Paper Overview)

Obstructive sleep apnea (OSA) detection models often suffer from poor generalization across datasets due to temporal heterogeneity and domain shift. This work proposes a hybrid deep-learning architecture—**CN-T Spatial–Temporal**—that combines **Temporal Convolutional Networks (TCN)** for local temporal/morphological patterns and **Transformer attention** for long-range dependencies, enhanced by:

- **Time-stretch preprocessing** using an **STFT phase-vocoder** with stretch factor **S = 0.5** (standardizing ~30 s epochs into ~15 s windows while preserving spectral content).
- **Modified relative positional encoding** blending absolute + relative temporal information to improve cross-dataset robustness.
- **Explainability** via attention distribution analysis and Grad-CAM-style visualization.

The framework is evaluated on three public datasets (Sleep-EDF, Apnea-ECG, ISRUC-Sleep) in both within-dataset and cross-dataset settings using clinically relevant metrics (ACC, SEN, SPEC, AUC).

---

## Key Results (from manuscript)

- **Average performance:** Accuracy **97.3%**, F1-score **0.94**, AUC **0.978**.
- **Cross-dataset generalization:** strong transfer performance across heterogeneous datasets (e.g., Sleep-EDF → Apnea-ECG, Apnea-ECG → ISRUC, ISRUC → Sleep-EDF).
- **Efficiency:** **8.3M parameters** and real-time inference (~**8.7 ms per 30-s epoch** on the reported GPU setup).
- **Interpretability:** attention concentrates on physiologically meaningful bands (e.g., respiration-related 0.2–0.4 Hz and EEG alpha 8–12 Hz).

---

## Datasets

This study uses three publicly available datasets:
- **Sleep-EDF Expanded (v1–v2)** (EEG/EOG/EMG + airflow/SpO₂; 100 Hz)
- **Apnea-ECG** (single-lead ECG; 100 Hz)
- **ISRUC-Sleep** (EEG/EOG/EMG + airflow/SpO₂; 200 Hz)

**Access links (as listed in the manuscript):**
```text
Sleep-EDF Expanded — https://doi.org/10.13026/C2X676
PhysioNet page      — https://physionet.org/content/sleep-edf/1.0.0/

Apnea-ECG Database  — https://physionet.org/content/apnea-ecg/1.0.0/

ISRUC-Sleep Dataset — https://sleeptight.isr.uc.pt/
