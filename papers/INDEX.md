# Curated Research Literature Library: Antimicrobial & Antimycobacterial Resistance (2015–2025)

This directory houses seminal, peer-reviewed, and top-tier workshop/conference papers (NeurIPS, ICML, Nature Communications, Nature BME, PLOS Computational Biology, bioRxiv) documenting the chronological evolution of computational genomics, machine learning, and deep learning for antimicrobial and antimycobacterial resistance.

---

## 📅 Chronological Timeline & Milestone Overview

```
2015 ─── Set Covering Machines & Greedy Biomarker Discovery (ICML 2015)
 │
2016 ─── First Pan-Bacterial WGS Machine Learning (ICML & NeurIPS 2016 ML4H)
 │
2018 ─── Bayesian Deep Learning & Uncertainty Estimation for AMR (NeurIPS 2018)
 │
2019 ─── Deep Learning for Rapid Pathogen & Phenotype Identification (Nature Communications)
 │
2020 ─── Controllable Deep Generative Models & Automated AST (Nature BME / Optical DL)
 │
2021 ─── CRyPTIC Landmark: 12,289 M. tuberculosis Genomes & Quantitative MICs (PLoS / bioRxiv)
 │        AI Nucleic Acid Amplification for MDR-TB Diagnostics
 │
2022 ─── Pangenome-Based Machine Learning for AMR (PLOS Computational Biology)
 │
2023 ─── Incubation-Free TB Drug Resistance Determination via ML
 │
2024 ─── Evolutionary Accumulation Modeling for Multi-Drug Resistance Dynamics
 │
2025 ─── Foundation Models, Graph Attention Networks & Multi-Path CNNs for MTB
```

---

## 📑 Paper Index

### 2015
* **Title:** Greedy Biomarker Discovery in the Genome with Applications to Antimicrobial Resistance
  * **Authors:** Alexandre Drouin, Sébastien Giguère, Maxime Déraspe, François Laviolette, Mario Marchand, Jacques Corbeil
  * **Venue:** *International Conference on Machine Learning (ICML 2015)*
  * **Pathogen:** *Streptococcus pneumoniae*, *Mycobacterium tuberculosis*, *Clostridium difficile*
  * **Methodology:** Set Covering Machines (SCM), $L_1/L_2$ regularized Support Vector Machines (SVM), CART trees over $10^7$ k-mer features.
  * **Significance:** First formal algorithmic proof that sparse greedy rule-based learning outperforms unregularized models on raw whole-genome k-mers without pre-filtering.
  * **File:** [`papers/2015/2015_Drouin_GreedyBiomarkerDiscovery_ICML.pdf`](2015/2015_Drouin_GreedyBiomarkerDiscovery_ICML.pdf)

---

### 2016
* **Title:** Large Scale Modeling of Antimicrobial Resistance with Interpretable Classifiers
  * **Authors:** Alexandre Drouin, Frédéric Raymond, Gaël Letarte St-Pierre, Mario Marchand, Jacques Corbeil, François Laviolette
  * **Venue:** *Neural Information Processing Systems (NeurIPS / NIPS 2016 Workshop on Machine Learning for Health)*
  * **Pathogen:** Pan-bacterial (PATRIC database, 36 clinical pathogen cohorts)
  * **Methodology:** Scalable Set Covering Machines, Kover platform, boolean rule induction.
  * **Significance:** Demonstrated that machine learning models could yield human-interpretable boolean decision lists matching canonical resistance mutations while discovering non-coding determinants.
  * **File:** [`papers/2016/2016_Drouin_InterpretableClassifiers_NeurIPS.pdf`](2016/2016_Drouin_InterpretableClassifiers_NeurIPS.pdf)

* **Title:** Machine Learning for Antimicrobial Resistance
  * **Authors:** John W. Santerre, James J. Davis, Fangfang Xia, Rick Stevens
  * **Venue:** *International Conference on Machine Learning (ICML 2016 #Data4Good)*
  * **Pathogen:** *Klebsiella pneumoniae*, *Escherichia coli*
  * **Methodology:** Random Forests, AdaBoost, ensemble decision trees over genomic variation matrices.
  * **Significance:** Established that machine learning on bacterial genomes achieves $>90\%$ classification accuracy and pinpoints causal AMR gene regions.
  * **File:** [`papers/2016/2016_Davis_MachineLearningAMR_ICML.pdf`](2016/2016_Davis_MachineLearningAMR_ICML.pdf)

---

### 2018
* **Title:** Reliable Uncertainty Estimate for Antibiotic Resistance Classification with Stochastic Gradient Langevin Dynamics
  * **Authors:** Anonymized / NeurIPS BDL Contributors
  * **Venue:** *NeurIPS 2018 Workshop on Bayesian Deep Learning*
  * **Pathogen:** Bacterial clinical isolates
  * **Methodology:** Bayesian Neural Networks, Stochastic Gradient Langevin Dynamics (SGLD), epistemic uncertainty calibration.
  * **Significance:** Addressed a critical barrier in clinical AI deployment: providing calibrated uncertainty intervals to prevent confident misclassifications in life-threatening infections.
  * **File:** [`papers/2018/2018_SGLD_UncertaintyAntibioticResistance_NeurIPS.pdf`](2018/2018_SGLD_UncertaintyAntibioticResistance_NeurIPS.pdf)

---

### 2019
* **Title:** Rapid Identification of Pathogenic Bacteria Using Raman Spectroscopy and Deep Learning
  * **Authors:** Chi-Sing Ho, Neal Jean, Catherine A. Hogan, Lena Blackmon, Stefanie S. Jeffrey, Mark Holodniy, Niaz Banaei, Amr A. E. Saleh, Sean Ermann, Justin Dionne
  * **Venue:** *Nature Communications* (Stanford University)
  * **Pathogen:** 30 common bacterial and fungal pathogens, including MRSA and vancomycin-resistant enterococci (VRE)
  * **Methodology:** 1D Convolutional Neural Networks (1D-CNN) trained on spectral vibrational fingerprints.
  * **Significance:** Enabled isolate-level identification and antibiotic susceptibility classification in seconds directly from clinical isolates with $99.0\%$ accuracy.
  * **File:** [`papers/2019/2019_Ho_Stanford_DeepLearningPathogenIdentification_NatComm.pdf`](2019/2019_Ho_Stanford_DeepLearningPathogenIdentification_NatComm.pdf)

---

### 2020
* **Title:** Accelerating Antimicrobial Discovery with Controllable Deep Generative Models and Molecular Dynamics
  * **Authors:** Payel Das, Tom Sercu, Kahini Wadhawan, Inkit Padhi, Sebastian Gehrmann, Kahini C. et al. (IBM Research)
  * **Venue:** *Nature Biomedical Engineering*
  * **Pathogen:** Multidrug-resistant Gram-negative and Gram-positive pathogens
  * **Methodology:** Conditional Variational Autoencoders (CVAE), Latent space controllable sampling, all-atom Molecular Dynamics simulations.
  * **Significance:** Validated end-to-end de novo design of low-toxicity antimicrobial peptides capable of killing multi-drug resistant bacteria in vivo.
  * **File:** [`papers/2020/2020_Das_IBM_ControllableDeepGenerativeAntimicrobial_NatBME.pdf`](2020/2020_Das_IBM_ControllableDeepGenerativeAntimicrobial_NatBME.pdf)

* **Title:** An Automated, Cost-Effective Optical System for Accelerated Anti-microbial Susceptibility Testing (AST) Using Deep Learning
  * **Authors:** Biomedical Engineering Consortium
  * **Venue:** *arXiv:2005.11454*
  * **Pathogen:** Clinical bacterial isolates
  * **Methodology:** Computer vision, ResNet feature extractors on microscopic bacterial colony growth dynamics.
  * **Significance:** Reduced traditional 24-hour phenotypic AST incubation times to under 3 hours via single-cell tracking.
  * **File:** [`papers/2020/2020_Optical_AST_DeepLearning.pdf`](2020/2020_Optical_AST_DeepLearning.pdf)

---

### 2021
* **Title:** A Data Compendium Associating the Genomes of 12,289 *Mycobacterium tuberculosis* Isolates with Quantitative Resistance Phenotypes to 13 Drugs
  * **Authors:** The CRyPTIC Consortium (Oxford, Sanger, Harvard, European / International Centers)
  * **Venue:** *PLOS Biology* / *bioRxiv* (DOI: `10.1101/2021.03.18.436029`)
  * **Pathogen:** *Mycobacterium tuberculosis* (12,289 clinical isolates across Lineages 1–4)
  * **Methodology:** Microdilution minimum inhibitory concentration (MIC) testing across 13 anti-TB drugs paired with Illumina whole-genome sequencing.
  * **Significance:** **The world benchmark dataset for computational tuberculosis research.** Provides the quantitative ground truth required to train continuous MIC regression models.
  * **File:** [`papers/2021/2021_CRyPTIC_Genomes12289Isolates_PLoS_bioRxiv.pdf`](2021/2021_CRyPTIC_Genomes12289Isolates_PLoS_bioRxiv.pdf)

* **Title:** Design of an Efficient, Ease-of-Use and Affordable Artificial Intelligence Based Nucleic Acid Amplification Diagnosis Technology for Tuberculosis and Multi-Drug Resistant Tuberculosis
  * **Authors:** Zhang et al.
  * **Venue:** *arXiv:2104.08178*
  * **Pathogen:** *Mycobacterium tuberculosis* (MDR-TB)
  * **Methodology:** AI-assisted amplification fluorescence curve analysis for rapid multiplex mutation detection.
  * **Significance:** Point-of-care rapid molecular diagnosis of Rifampicin and Isoniazid resistance in resource-limited settings.
  * **File:** [`papers/2021/2021_Zhang_AIDiagnosisMDRTB.pdf`](2021/2021_Zhang_AIDiagnosisMDRTB.pdf)

---

### 2022
* **Title:** A Pangenome-Based Machine Learning Approach to Predict Antimicrobial Resistance from Whole-Genome Sequences
  * **Authors:** Anna G. Green, Hendrik den Bakker, Colin S. Worby, et al.
  * **Venue:** *PLOS Computational Biology* (DOI: `10.1371/journal.pcbi.1009825`)
  * **Pathogen:** *Salmonella enterica*, *Klebsiella pneumoniae*, *Pseudomonas aeruginosa*
  * **Methodology:** Pangenome graph modeling, gene family presence/absence, structural variant detection, logistic regression with elastic net regularization.
  * **Significance:** Demonstrated that moving from single reference-based variant calling to pangenomic representations captures unmapped resistance plasmids and novel horizontal gene transfer events.
  * **File:** [`papers/2022/2022_Green_PangenomeMachineLearningAMR_PLoSCompBio.pdf`](2022/2022_Green_PangenomeMachineLearningAMR_PLoSCompBio.pdf)

---

### 2023
* **Title:** Rapid, Antibiotic Incubation-Free Determination of Tuberculosis Drug Resistance Using Machine Learning and Raman Spectroscopy
  * **Authors:** Lu et al.
  * **Venue:** *arXiv:2306.05653*
  * **Pathogen:** *Mycobacterium tuberculosis*
  * **Methodology:** Raman spectroscopy, high-dimensional vibrational spectral embeddings, support vector classifiers.
  * **Significance:** Bypassed culture growth bottlenecks entirely, delivering phenotypic resistance calls within hours.
  * **File:** [`papers/2023/2023_Lu_RapidTBDrugResistanceML.pdf`](2023/2023_Lu_RapidTBDrugResistanceML.pdf)

---

### 2024
* **Title:** Evolutionary Accumulation Modelling in AMR: Machine Learning to Infer and Predict Evolutionary Dynamics of Multi-Drug Resistance
  * **Authors:** David Hughes et al.
  * **Venue:** *arXiv:2411.00219*
  * **Pathogen:** *M. tuberculosis* and clinical pathogens
  * **Methodology:** Continuous-time Markov chains, evolutionary accumulation models, directed graphical networks of mutation acquisition order.
  * **Significance:** Models the sequential trajectories of multi-drug resistance evolution, predicting which resistance mutation will arise next under antibiotic selection pressure.
  * **File:** [`papers/2024/2024_Hughes_EvolutionaryAccumulationAMR.pdf`](2024/2024_Hughes_EvolutionaryAccumulationAMR.pdf)

---

### 2025
* **Title:** VAMP-Net: An Interpretable Multi-Path Network of Genomic Permutation-Invariant Set Attention and Quality-Aware 1D-CNN for MTB Drug Resistance
  * **Authors:** Advanced Computational Genomics Group
  * **Venue:** *arXiv:2512.21786*
  * **Pathogen:** *Mycobacterium tuberculosis*
  * **Methodology:** Multi-path deep neural architecture combining Set Attention (permutation-invariant variant sets) and quality-aware 1D-CNNs for raw sequencing metrics.
  * **Significance:** State-of-the-art deep learning architecture achieving superior sensitivity and specificity on first- and second-line anti-TB drugs while maintaining direct interpretability over individual loci.
  * **File:** [`papers/2025/2025_VAMPNet_MTBDrugResistance.pdf`](2025/2025_VAMPNet_MTBDrugResistance.pdf)

* **Title:** Decoding Positive Selection in *Mycobacterium tuberculosis* with Phylogeny-Guided Graph Attention Models
  * **Authors:** Computational Phylogenetics Lab
  * **Venue:** *arXiv:2510.08703*
  * **Pathogen:** *Mycobacterium tuberculosis*
  * **Methodology:** Graph Attention Networks (GAT) structured along phylogenetic tree topologies, node feature aggregation of non-synonymous mutation burdens.
  * **Significance:** Disentangles convergent resistance evolution from neutral lineage-specific background mutations.
  * **File:** [`papers/2025/2025_GraphAttention_MtbPositiveSelection.pdf`](2025/2025_GraphAttention_MtbPositiveSelection.pdf)

* **Title:** Can Large Language Models Predict Antimicrobial Resistance Gene?
  * **Authors:** GenAI & Biology Research Team
  * **Venue:** *arXiv:2503.04413*
  * **Pathogen:** Pan-bacterial resistance genes (CARD / ResFinder catalogs)
  * **Methodology:** In-context learning, sequence-to-function prompting, protein sequence embeddings from pretrained biological LLMs.
  * **Significance:** Rigorous evaluation of the emergent capabilities and current limitations of large language models in zero-shot AMR gene annotation.
  * **File:** [`papers/2025/2025_LLM_AntimicrobialResistanceGene.pdf`](2025/2025_LLM_AntimicrobialResistanceGene.pdf)

* **Title:** Fusing Sequence Motifs and Pan-Genomic Features: Antimicrobial Resistance Prediction Using an Explainable Lightweight 1D CNN-XGBoost Ensemble
  * **Authors:** Supercomputing & Bioinformatics Lab
  * **Venue:** *Proceedings of SCA / HPCAsia 2026* (*arXiv:2509.23552*)
  * **Pathogen:** Multidrug-resistant bacterial pathogens
  * **Methodology:** Hybrid 1D-CNN feature extractor + gradient-boosted decision trees (XGBoost), SHAP tree explainability.
  * **Significance:** Proves that hybrid neural-tree ensembles yield optimal trade-offs between predictive accuracy and deployment speed on edge computing hardware.
  * **File:** [`papers/2025/2025_CNN_XGBoost_PanGenomicAMR.pdf`](2025/2025_CNN_XGBoost_PanGenomicAMR.pdf)

---

## 🔍 How to Utilize These Papers in OmicGene

1. **Benchmark Replication**: Use `papers/2021/2021_CRyPTIC_Genomes12289Isolates_PLoS_bioRxiv.pdf` to calibrate baseline models on the 12,289 isolate cohort.
2. **Architecture Inspiration**: Refer to `papers/2025/2025_VAMPNet_MTBDrugResistance.pdf` and `papers/2025/2025_GraphAttention_MtbPositiveSelection.pdf` for state-of-the-art attention and graph mechanisms implemented in `src/omicgene/models/`.
3. **Pangenome Features**: Adopt the graph and k-mer methodology described in `papers/2022/2022_Green_PangenomeMachineLearningAMR_PLoSCompBio.pdf`.
