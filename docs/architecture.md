# OmicGene System Architecture

```mermaid
flowchart TD
    subgraph Ingestion ["1. Data Ingestion & Quality Control"]
        SRA["NCBI SRA / ENA Raw FASTQ"] --> FastQC["FastQC / Trimmomatic"]
        VCF["Pre-called VCFs / CRyPTIC"] --> VCFQC["VCF Filtering (DP >= 10, AF >= 0.75)"]
    end

    subgraph Genomics ["2. Genomic Feature Engineering"]
        FastQC --> Align["BWA-MEM / Minimap2<br/>(Ref: H37Rv)"]
        Align --> Call["FreeBayes / GATK / Snippy"]
        Call --> Annotate["SnpEff / VEP Annotation"]
        VCFQC --> Annotate
        Annotate --> Matrix["Sparse Variant Matrix<br/>(SNPs, Indels, Promoters)"]
        Annotate --> Kmers["Unitigs & K-mer Encoders"]
        Annotate --> Embeddings["Protein Language Embeddings<br/>(ESM-2 / ProtBERT)"]
    end

    subgraph Modeling ["3. Multi-Tier Predictive Modeling"]
        Matrix --> Baselines["Baseline Classifiers<br/>(L2-Logistic, XGBoost, Random Forest)"]
        Embeddings --> DeepModels["Deep Multitask Transformer / CNN"]
        Kmers --> PangenomeGNN["Pangenome Graph Neural Network"]
    end

    subgraph Evaluation ["4. Clinical & Benchmark Evaluation"]
        Baselines --> Metrics["Clinical Metrics Evaluator<br/>- VME (False Susceptibility)<br/>- ME (False Resistance)<br/>- AUROC & log2(MIC) RMSE"]
        DeepModels --> Metrics
        PangenomeGNN --> Metrics
        Metrics --> Explainability["SHAP Attribution & Mutation Discovery"]
    end
```

---

## Technical Specifications

1. **Alignment & Reference**:
   - For *Mycobacterium tuberculosis*, reads are aligned to the H37Rv reference genome (`NC_000962.3`).
   - Repetitive regions (PPE/PE-PGRS gene families) and mobile genetic elements are flagged to avoid false-positive variant calls.
2. **Phenotypic Targets**:
   - First-line anti-TB agents: Isoniazid (INH), Rifampicin (RIF), Ethambutol (EMB), Pyrazinamide (PZA).
   - Second-line fluoroquinolones: Moxifloxacin (MFX), Levofloxacin (LFX), Ofloxacin (OFX).
   - Second-line injectables: Amikacin (AMI), Kanamycin (KAN), Capreomycin (CAP).
   - Novel/repurposed: Bedaquiline (BDQ), Linezolid (LZD), Clofazimine (CFZ), Delamanid (DLM).
3. **Loss Functions**:
   - Combined multi-task objective:
     $$\mathcal{L} = \alpha \mathcal{L}_{\text{BCE}}(\hat{y}_{\text{class}}, y_{\text{class}}) + (1 - \alpha) \mathcal{L}_{\text{Huber}}(\hat{y}_{\text{MIC}}, y_{\text{MIC}})$$
     where $\alpha$ is a dynamic balancing hyperparameter.
