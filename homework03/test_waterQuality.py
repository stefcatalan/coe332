from waterQuality import calculateTurbidity
from waterQuality import minTime
import pytest

def test_calculateTurbidity():
    assert calculateTurbidity([{'calibration_constant': 1, 'detector_current': 2}]) == 0.4
    assert calculateTurbidity([{'calibration_constant': 1, 'detector_current': 0}]) == 0
    with pytest.raises(TypeError):
        calculateTurbidity(['a'])
    with pytest.raises(KeyError):
        calculateTurbidity([{'a': 1}])
    with pytest.raises(TypeError):
        calculateTurbidity([{'calibration_constant': 'x', 'detector_current': 1}])

def test_minTime():
    assert minTime(1) == 0
    assert isinstance(minTime(2), float) == True
    with pytest.raises(TypeError):
        minTime('a')
    with pytest.raises(ZeroDivisionError):
        minTime(0)
    with pytest.raises(NameError):
        minTime(b)

