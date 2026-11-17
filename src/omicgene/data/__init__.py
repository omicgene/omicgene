"""Data loading, preprocessing, and variant featurization modules."""

from typing import List, Dict, Any

class VariantFeaturizer:
    """Extracts and standardizes genomic variants for AMR prediction."""
    def __init__(self, target_genes: List[str] | None = None) -> None:
        self.target_genes = target_genes or ["rpoB", "katG", "inhA", "pncA", "gyrA", "embB"]

    def featurize(self, variant_list: List[Dict[str, Any]]) -> Dict[str, Any]:
        """Convert a list of raw variants into a standardized model feature dictionary."""
        filtered = [v for v in variant_list if v.get("gene") in self.target_genes]
        return {
            "num_variants": len(filtered),
            "genes_covered": list(set(v.get("gene") for v in filtered if "gene" in v)),
            "variants": filtered,
        }
