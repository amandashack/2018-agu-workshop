import numpy as np

from .data_analysis import moving_avg

def test_movingavg():
    avg = moving_avg(np.ones(10), 2)
    assert np.all(np.isnan(avg[-2:]))
    assert np.all(np.isnan(avg[0:2]))
    assert np.allclose(avg[2:-2], 1)