import pytest


# Пример с использованием параметризации
@pytest.mark.parametrize("input_val, expected", [
    ("hello", 5),
    ("world", 5),
    ("pytest", 6)
])
def test_length(input_val: str, expected: int):
    assert len(input_val) == expected


# Пример тестов с использованием фикстур
@pytest.fixture
def numbers() -> list:
    return [1, 2, 3]


def test_length_2(numbers: list):
    assert len(numbers) == 3


def test_sum(numbers: list):
    assert sum(numbers) == 6
