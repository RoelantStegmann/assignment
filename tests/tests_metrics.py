import pytest
import numpy as np

from metrics import mse


class TestMetrics:
    def test_mse_all_wrong(self):
        assert 0 == mse(np.array([0, 0, 1, 1]), np.array([0, 0, 1, 1]))

    def test_mse_all_right(self):
        assert 1 == mse(np.array([0, 0, 1, 1]), np.array([1, 1, 0, 0]))

    def test_mse_large_values(self):
        assert 1e18 == mse(np.array([0, 1e9]), np.array([1e9, 0]))

