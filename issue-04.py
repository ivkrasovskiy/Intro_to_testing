from issues.one_hot_encoder import fit_transform
import pytest


def test_tf():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]

    assert (actual == expected)


def test_empty():
    actual = fit_transform([])
    expected = []
    assert (actual == expected)


def test_len():
    actual = fit_transform(['Moscow', 'New York', 'Moscow', 'London'])
    expected = [
        ('Moscow', [0, 0, 1]),
        ('New York', [0, 1, 0]),
        ('Moscow', [0, 0, 1]),
        ('London', [1, 0, 0]),
    ]
    assert (len(actual) == len(expected))


def test_features_len():
    actual = len(set(['Moscow', 'New York', 'Moscow', 'London']))
    expected = len([
                       ('Moscow', [0, 0, 1]),
                       ('New York', [0, 1, 0]),
                       ('Moscow', [0, 0, 1]),
                       ('London', [1, 0, 0]),
                   ][0][1])
    assert (actual == expected)


def test_exceptions():
    actual = all(isinstance(city, str) for city in ['Moscow', 'New York', 'Moscow', 1])

    if actual:
        pytest.raises(ValueError)
