# tests/lib_test.py
from mlproject.distance import haversine

def test_haversine_non_zero():
  assert haversine(1, 3, 5, 7) != 0
