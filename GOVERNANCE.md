# OmicGene Project Governance & Scientific Steering

## Purpose & Scope

The **OmicGene** organization is structured as an open scientific collaboration model designed to foster cutting-edge research in computational biology, pathogen genomics, and antimicrobial resistance (AMR). 

This document defines the decision-making framework, role responsibilities, and RFC (Request for Comments) protocol.

---

## Organizational Structure

```
                  ┌───────────────────────────────────────────┐
                  │        Scientific Advisory Board          │
                  │    (Domain Experts, Clinicians, PIs)      │
                  └─────────────────────┬─────────────────────┘
                                        │
                  ┌─────────────────────▼─────────────────────┐
                  │       Core Maintainers & Steering         │
                  │   (Architecture, Merges, Releases, Infra) │
                  └─────────────────────┬─────────────────────┘
                                        │
           ┌────────────────────────────┼────────────────────────────┐
           ▼                            ▼                            ▼
┌──────────────────────┐    ┌──────────────────────┐    ┌──────────────────────┐
│   Genomics Working   │    │  Machine Learning &  │    │  Data Governance &   │
│        Group         │    │ Foundation Models WG │    │    Benchmarking WG   │
└──────────────────────┘    └──────────────────────┘    └──────────────────────┘
```

---

## Roles & Responsibilities

### 1. Scientific Advisory Board (SAB)
- Provides strategic vision on priority pathogens (e.g. *M. tuberculosis*, WHO critical priority list).
- Evaluates clinical relevance, epidemiological benchmarks, and alignment with international guidelines (WHO, CDC, EUCAST, CLSI).

### 2. Core Maintainers
- Manage repository administration, branch protection rules, CI/CD runners, and security advisories.
- Review and approve pull requests for code quality, security, and algorithmic soundness.
- Coordinate software releases and documentation updates.

### 3. Working Groups
- **Genomics Working Group**: Focuses on variant calling pipelines (SNPs, indels, SVs), pangenome graph tools (`vg`, `minigraph-cactus`), and lineage determination.
- **Machine Learning & Foundation Models WG**: Focuses on deep learning architectures (Transformers, GNNs, CNNs), self-supervised pre-training, and MIC regression.
- **Data Governance & Benchmarking WG**: Manages dataset standardization (CARD, ResFinder, BV-BRC, CRyPTIC) and FAIR data compliance.

---

## Decision-Making Process & RFC Protocol

Major architectural or methodological changes require a **Request for Comments (RFC)**:

1. **RFC Proposal**: The author creates an issue or discussion tagged `RFC` outlining the scientific motivation, mathematical formulation, API design, and alternative approaches.
2. **Review Period**: A minimum 14-day comment period is provided for community feedback and review by the working group.
3. **Consensus**: Decisions are made through lazy consensus among maintainers. If substantial contention exists, the Core Steering Committee votes by simple majority.
