# Data Governance & Storage Architecture

This directory houses preprocessing scripts, schemas, and references for genomic datasets and minimum inhibitory concentration (MIC) cohorts.

---

## Data Hierarchy

```
data/
├── raw/             # Raw FASTA/FASTQ/VCF files or symlinks (gitignored)
├── processed/       # Curated variant tables, k-mer counts, embeddings (gitignored)
├── references/      # Standard reference genomes (e.g. H37Rv for M. tuberculosis NC_000962.3)
└── schemas/         # Data validation schemas (Pydantic models for isolate metadata)
```

---

## Reference Genomes & AMR Databases

1. ***Mycobacterium tuberculosis* H37Rv**: Reference accession `NC_000962.3` / `AL123456.3`.
2. **Comprehensive Antibiotic Resistance Database (CARD)**: Resistance genes, mutations, and Antibiotic Resistance Ontology (ARO).
3. **ResFinder**: Curated database for acquired AMR genes and chromosomal point mutations.
4. **CRyPTIC Consortium Data**: Comprehensive Resistance Prediction for Tuberculosis: an International Consortium (10,000+ clinical isolates with microdilution MIC measurements across 14 anti-TB drugs).
5. **BV-BRC (Bacterial and Viral Bioinformatics Resource Center)**: Pan-bacterial AMR isolates and matched AST phenotypes.

---

## Ethical & Privacy Standards

- No patient identifiable records or private human sequences are stored.
- All genomic isolates must reference publicly accessible database accessions (NCBI BioProject, ENA Study Accession, or CRyPTIC).
