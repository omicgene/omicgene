import unittest
import numpy as np
from omicgene.data import VariantFeaturizer
from omicgene.models import BaselineAMRPredictor
from omicgene.utils import set_seed, compute_clinical_errors

class TestSmoke(unittest.TestCase):
    def test_set_seed(self):
        set_seed(123)
        val1 = np.random.rand()
        set_seed(123)
        val2 = np.random.rand()
        self.assertEqual(val1, val2)

    def test_variant_featurizer(self):
        featurizer = VariantFeaturizer()
        variants = [
            {"gene": "rpoB", "pos": 450, "ref": "S", "alt": "L"},
            {"gene": "unknown_gene", "pos": 10, "ref": "A", "alt": "T"},
        ]
        features = featurizer.featurize(variants)
        self.assertEqual(features["num_variants"], 1)
        self.assertIn("rpoB", features["genes_covered"])

    def test_baseline_predictor(self):
        predictor = BaselineAMRPredictor(drug_name="Rifampicin")
        predictor.fit(None, None)
        features = {"num_variants": 1, "genes_covered": ["rpoB"]}
        result = predictor.predict_resistance(features)
        self.assertEqual(result["drug"], "Rifampicin")
        self.assertTrue(result["resistant"])
        self.assertGreater(result["probability"], 0.9)

    def test_clinical_errors(self):
        y_true = np.array([1, 1, 0, 0])
        y_pred = np.array([1, 0, 0, 1])  # 1 VME, 1 ME
        metrics = compute_clinical_errors(y_true, y_pred)
        self.assertEqual(metrics["vme_rate"], 0.5)
        self.assertEqual(metrics["me_rate"], 0.5)
        self.assertEqual(metrics["accuracy"], 0.5)

if __name__ == "__main__":
    unittest.main()
