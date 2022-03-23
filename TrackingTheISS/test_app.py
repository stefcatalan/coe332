from app import specificEpoch
from app import specificCountry
from app import regions
from app import specificRegion
from app import cities
from app import specificCity
import pytest

def test_specificEpoch():
    with pytest.raises(NameError):
        specificEpoch(blah)

def test_specificCountry():
    with pytest.raises(NameError):
        specificCountry(japan)

def test_regions():
    with pytest.raises(NameError):
        regions(japan)

def test_specificRegion():
    with pytest.raises(NameError):
        specificRegion(canada)

def test_cities():
    with pytest.raises(TypeError):
        cities(20)

def test_specificCity():
    with pytest.raises(NameError):
        specificCity(atlanta)

