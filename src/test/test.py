import pytest
from src.hw2_fixed import merge_sort

def test_empty_list():
    assert merge_sort([]) == []

def test_sort():
    assert merge_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_sorted_duplicates():
    assert merge_sort([5, 4, 3, 3, 1]) == [1, 3, 3, 4, 5]