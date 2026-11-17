# Contributing to OmicGene

Thank you for your interest in contributing to **OmicGene**! We are building open-source computational genomics and machine learning tools to combat antimicrobial resistance (AMR). Whether you are developing novel neural architectures, optimizing variant-calling pipelines, integrating clinical datasets, or curating literature, your contributions are invaluable.

---

## Table of Contents

1. [Code of Conduct](#code-of-conduct)
2. [Getting Started](#getting-started)
3. [Development Environment Setup](#development-environment-setup)
4. [Scientific Reproducibility Standards](#scientific-reproducibility-standards)
5. [Git Workflow & Branching Strategy](#git-workflow--branching-strategy)
6. [Commit Message Conventions](#commit-message-conventions)
7. [Code Style & Quality](#code-style--quality)
8. [Data Handling & Privacy Guidelines](#data-handling--privacy-guidelines)
9. [Submitting a Pull Request](#submitting-a-pull-request)
10. [Review & Release Protocol](#review--release-protocol)

---

## Code of Conduct

All contributors are expected to uphold the [OmicGene Code of Conduct](CODE_OF_CONDUCT.md). Please read it before participating in discussions or submitting pull requests.

---

## Getting Started

1. **Find or open an issue**: Before writing significant code, please check existing [Issues](https://github.com/omicgene/omicgene/issues) or start a [Discussion](https://github.com/omicgene/omicgene/discussions).
2. **Fork and clone**:
   ```bash
   git clone https://github.com/omicgene/omicgene.git
   cd omicgene
   ```

---

## Development Environment Setup

We recommend using Python 3.10+ and a dedicated virtual environment or `uv`:

```bash
# Using Python venv
python3 -m venv .venv
source .venv/bin/activate

# Install development dependencies
pip install --upgrade pip
pip install -r requirements.txt
pip install -e ".[dev]"
```

Verify your setup by running the test suite:
```bash
pytest tests/
```

---

## Scientific Reproducibility Standards

As an enterprise research repository, any contribution that involves machine learning or statistical modeling must adhere to strict reproducibility guidelines:

1. **Explicit Random Seeds**: All stochastic processes (data splits, model weight initialization, sampling) must expose and set deterministic seeds:
   ```python
   import random
   import numpy as np
   import torch

   def set_seed(seed: int = 42) -> None:
       random.seed(seed)
       np.random.seed(seed)
       torch.manual_seed(seed)
       if torch.cuda.is_available():
           torch.cuda.manual_seed_all(seed)
   ```
2. **Fixed Train/Validation/Test Splits**: Models predicting AMR phenotypes must use stratified or phylogenetic (lineage-aware / strain-aware) data splits to avoid data leakage between genetically identical clones.
3. **Standard Benchmark Metrics**:
   - Classification (Susceptible vs. Resistant): Sensitivity, Specificity, Very Major Error (VME, false susceptibility), Major Error (ME, false resistance), AUROC, F1-Score.
   - Regression (log2 Minimum Inhibitory Concentration): Root Mean Squared Error (RMSE), Pearson's $r$, and Essential Agreement ($\pm 1$ two-fold dilution).

---

## Git Workflow & Branching Strategy

We follow a modified **GitHub Flow** with descriptive branch prefixes:

- `feat/<feature-name>`: New functionality or model architectures.
- `fix/<issue-name>`: Bug fixes and performance patches.
- `data/<dataset-name>`: Integration of new genomic isolate datasets or benchmark cohorts.
- `reproduce/<paper-citation>`: Benchmark reproduction or literature replication scripts.
- `docs/<doc-topic>`: Improvements to documentation, tutorials, or literature index.

---

## Commit Message Conventions

We adhere to the [Conventional Commits](https://www.conventionalcommits.org/) specification:

```
<type>(<scope>): <short summary>

[optional body]

[optional footer(s)]
```

### Types:
- `feat`: A new feature or machine learning algorithm.
- `fix`: A bug fix.
- `docs`: Documentation, literature catalog updates, or notebooks.
- `data`: Dataset ingestion, curation, or preprocessing.
- `benchmark`: Reproducibility runs or benchmark evaluations.
- `test`: Adding or updating test suites.
- `ci`: Changes to GitHub Actions or build scripts.

---

## Code Style & Quality

All Python code must pass automated linting:

- **Linter**: `ruff check .`
- **Formatter**: `black .`
- **Type Checker**: `mypy src/`
- **Type Hints**: Fully annotate all public functions, classes, and method signatures.
- **Docstrings**: Google-style docstrings explaining arguments, returns, and mathematical formulations.

---

## Data Handling & Privacy Guidelines

- **Zero PHI Tolerance**: Under no circumstances should protected health information, hospital patient identifiers, or raw human genomic reads be committed.
- **Only Open Bacterial Accessions**: Always reference public accessions from NCBI SRA, ENA, BV-BRC, or CRyPTIC.
- **Large Files**: Model checkpoints ($>50\text{MB}$) and large genomic BAM/CRAM/FASTQ files should not be stored directly in Git. Use Git LFS, Hugging Face Hub, or Zenodo DOIs.

---

## Submitting a Pull Request

1. Ensure your branch is rebased on the latest `main`.
2. Verify all tests pass locally: `pytest tests/`.
3. Fill out the [Pull Request Template](.github/PULL_REQUEST_TEMPLATE.md) completely.
4. Request review from the maintainers.

---

## Review & Release Protocol

1. Every PR requires at least one approving review from a core maintainer.
2. All CI checks (linting, tests, citation validation) must be green.
3. Releases follow [Semantic Versioning](https://semver.org/) (`vMAJOR.MINOR.PATCH`).
