from ml_data_analysis import compute_average_mass
from ml_data_analysis import check_hemisphere
from ml_data_analysis import count_classes
import pytest

def test_compute_average_mass():
    assert(compute_average_mass([{'a': 1}, {'a': 2}], 'a') == 1.5)
    assert(compute_average_mass([{'a': 1}, {'a': 2}, {'a': 3}], 'a') == 2)
    assert isinstance(compute_average_mass([{'a': 1}, {'a': 2}], 'a'), float) == True
    # testing exceptions
    with pytest.raises(ZeroDivisionError):
        compute_average_mass([], 'a')
    with pytest.raises(KeyError):
        compute_average_mass([{'a': 1}, {'b': 1}], 'a')


def test_check_hemisphere():
    assert(check_hemisphere(1.0, 1.0) == 'Northern & Eastern')
    assert(check_hemisphere(-1.0, -1.0) == 'Southern & Western')
    assert isinstance(check_hemisphere(1.0, 1.0), str) == True
    # testing exceptions
    with pytest.raises(TypeError):
        check_hemisphere('blah', 10.0)
    with pytest.raises(ValueError):
        check_hemisphere(0.0, 0.0)

def test_count_classes():
    assert isinstance(count_classes([{'a': 1}, {'a': 2}], 'a'), str) == False
    assert isinstance(count_classes([{'a': 1}, {'a': 2}], 'a'), dict) == True
    # testing exceptions
    with pytest.raises(TypeError):
        count_classes(10.0, 'a')
    with pytest.raises(KeyError):
        count_classes([{'a': 1}, {'b': 2}], 'a')
    with pytest.raises(NameError):
        count_classes([{'a': 1}, {'a': x}], 'a')


