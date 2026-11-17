# Contributing to omicgene

Thank you for your interest in contributing to **omicgene**! We welcome contributions from researchers, bioinformaticians, machine learning practitioners, and open-source developers working at the intersection of computational genomics and antimicrobial resistance (AMR).

---

## Table of Contents

- [Code of Conduct](#code-of-conduct)
- [How You Can Contribute](#how-you-can-contribute)
  - [1. Curating Research Literature](#1-curating-research-literature)
  - [2. Code and Model Development](#2-code-and-model-development)
  - [3. Bug Reports and Feature Requests](#3-bug-reports-and-feature-requests)
  - [4. Documentation and Tutorials](#4-documentation-and-tutorials)
- [Getting Started with Development](#getting-started-with-development)
  - [Forking and Branching](#forking-and-branching)
  - [Environment Setup](#environment-setup)
- [Contribution Standards](#contribution-standards)
  - [Code Quality and Style](#code-quality-and-style)
  - [Scientific Reproducibility](#scientific-reproducibility)
  - [Commit Message Guidelines](#commit-message-guidelines)
- [Pull Request Process](#pull-request-process)
- [Questions and Discussion](#questions-and-discussion)

---

## Code of Conduct

All contributors and participants are expected to adhere to our [Code of Conduct](CODE_OF_CONDUCT.md). Please review it to help maintain a welcoming and inclusive environment.

---

## How You Can Contribute

### 1. Curating Research Literature
`omicgene` maintains an indexed library of pivotal studies on antimicrobial and antimycobacterial resistance (`papers/INDEX.md`). If you wish to suggest or add new literature:
- Ensure the paper is peer-reviewed or a recognized preprint (e.g., bioRxiv, arXiv, medRxiv).
- Place documents in their respective chronological subfolder (`papers/<year>/`).
- Update `papers/INDEX.md` with:
  - Title, authors, venue, and year
  - Pathogens studied (e.g., *M. tuberculosis*, *K. pneumoniae*)
  - Methodological summary (algorithms, feature representations, data scale)
  - Scientific significance and relative links to the document

### 2. Code and Model Development
We welcome contributions involving:
- Genomic sequence preprocessing, k-mer tokenization, and variant calling pipelines.
- Predictive machine learning algorithms (e.g., tree ensembles, GNNs, CNNs, genomic foundation models).
- Evaluation suites measuring sensitivity, specificity, and minimum inhibitory concentration (MIC) concordance.
- Benchmarking scripts and dataset loaders.

### 3. Bug Reports and Feature Requests
- Check the [issue tracker](https://github.com/omicgene/omicgene/issues) to verify if the issue has already been reported.
- When filing a bug report, include:
  - A clear and descriptive title.
  - Minimal reproducible example or command log.
  - OS version, Python version, package dependencies, and hardware specifications (e.g., GPU/CUDA where applicable).
  - Expected behavior versus actual behavior.

### 4. Documentation and Tutorials
Improvements to docstrings, walkthroughs, pipeline architectural diagrams, and notebook tutorials are highly appreciated.

---

## Getting Started with Development

### Forking and Branching

1. Fork the repository to your own GitHub account.
2. Clone your fork locally:
   ```bash
   git clone https://github.com/<your-username>/omicgene.git
   cd omicgene
   ```
3. Set upstream remote:
   ```bash
   git remote add upstream https://github.com/omicgene/omicgene.git
   ```
4. Create a dedicated topic branch:
   ```bash
   git checkout -b feature/your-feature-name
   # or
   git checkout -b fix/your-bugfix-name
   ```

### Environment Setup

We recommend using a virtual environment (e.g., `venv` or `conda`):

```bash
python3 -m venv .venv
source .venv/bin/activate
pip install --upgrade pip
```

When dependencies are specified, install them in editable/development mode:
```bash
pip install -e ".[dev]"
```

---

## Contribution Standards

### Code Quality and Style
- **Python Formatting:** Follow PEP 8 guidelines. Format code using `black` or `ruff` and sort imports with `isort`.
- **Type Annotations:** Use Python type hints wherever practical.
- **Documentation:** Provide informative docstrings for public functions and classes following Google or NumPy docstring conventions.
- **Testing:** Include unit or integration tests for new modules, utility functions, or parsers. Verify tests pass prior to submitting a PR.

### Scientific Reproducibility
- Fix random seeds where stochastic methods are used in training or evaluation.
- Document reference genome versions (e.g., H37Rv accession NC_000962.3) and annotation releases clearly.
- Note hardware requirements, batch sizes, and training epochs when proposing new model baselines.

### Commit Message Guidelines
Use concise, conventional commit prefixes:
- `feat:` for new capabilities, algorithms, or pipelines
- `fix:` for bug fixes
- `docs:` for documentation and literature updates
- `refactor:` for code restructuring without behavioral alterations
- `test:` for adding or improving test coverage
- `chore:` for repository maintenance or configuration updates

Example:
```text
feat(tokenizer): add variable-length k-mer extraction for fasta sequences
```

---

## Pull Request Process

1. Ensure your branch is synced with the latest `main` branch from `upstream`.
2. Verify that all tests, linters, and formatting checks pass locally.
3. Open a Pull Request on GitHub against `main`.
4. Provide a clear PR description explaining:
   - Motivation and context for the change.
   - Summary of modifications made.
   - Any related issues closed (e.g., `Closes #12`).
5. Participate constructively in the code review process. Address review comments promptly.

---

## Questions and Discussion

If you have questions before opening a PR or want to discuss a major architectural change, please open a GitHub Discussion or Issue to align with maintainers.
