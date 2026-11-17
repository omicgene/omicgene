# Model Zoo & Neural Architecture Specifications

This directory contains neural network specifications, model checkpoint loaders, and baseline benchmarks for predicting antimicrobial resistance phenotypes.

---

## Supported Architectures

1. **Tree-Based Ensembles (Baselines)**:
   - XGBoost / LightGBM / Random Forest on sparse binary variant matrices (SNPs + indels) and k-mer frequency vectors ($k \in \{11, 21, 31\}$).
2. **Convolutional Neural Networks (1D-CNN / ResNet)**:
   - Gene-level sequence encoders for known resistance determinants (e.g. *rpoB*, *katG*, *inhA*, *pncA*, *gyrA*, *embB*).
3. **Graph Neural Networks (GNN)**:
   - Variation graphs / Pangenome graphs where nodes represent sequence segments and edges represent genomic bifurcations/structural variations.
4. **Genomic Transformers & Foundation Models**:
   - Zero-shot and fine-tuned protein language models (ESM-2, ProtBERT) and nucleotide foundation models (DNABERT-2, HyenaDNA).
   - Multi-task heads predicting both binary resistance (Susceptible/Resistant) and continuous $\log_2(\text{MIC})$.

---

## Evaluation Standard

All models are evaluated using:
- **AUROC / AUPRC** (imbalanced resistance classifications)
- **Very Major Error (VME)**: Target $< 1.5\%$ (FDA/EUCAST clinical concordance)
- **Major Error (ME)**: Target $< 3.0\%$
- **Essential Agreement (EA)**: Target $> 90\%$ within $\pm 1$ doubling dilution for MIC regression.
