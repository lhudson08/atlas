from unittest import TestCase

from atlas.schema import VariantCall
from atlas.schema import Variant

from atlas.pheno.amr import TBPredictor


class AMRPredictTest(TestCase):

    def setUp(self):
        self.variant_snp = Variant.create(start=0, end=1, reference_bases="A",
                                          alternate_bases=["T"])

        self.predictor = TBPredictor(variant_calls={},
                                       called_genes={})

    def teardown(self):
        pass

    def test_wt_vars(self):
        call = VariantCall.create(
            variant=self.variant_snp,
            genotype=[
                0,
                1],
            genotype_likelihoods=[
                0.1,
                0.9,
                0.12],
            info={
                "contamination_depths": [],
                "coverage": {
                    "alternate": {
                        "percent_coverage": 100.0,
                        "median_depth": 15,
                        "min_depth": 2},
                    "reference": {
                        "percent_coverage": 100.0,
                        "median_depth": 139,
                        "min_depth": 128}},
                "expected_depths": [152]})

        assert self.predictor._coverage_greater_than_threshold(call) == False