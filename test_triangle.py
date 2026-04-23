import pytest
from triangle import Triangle, TriangleType


@pytest.mark.parametrize("a,b,c", [
    (7, 7, 7),
])
def test_equilateral(a, b, c):
    assert Triangle(a, b, c).type == TriangleType.EQUILATERAL


@pytest.mark.parametrize("a,b,c", [
    (2, 2, 3),
    (2, 3, 2),
    (3, 2, 2),
])
def test_isosceles(a, b, c):
    assert Triangle(a, b, c).type == TriangleType.ISOSCELES


@pytest.mark.parametrize("a,b,c", [
    (3, 4, 6),
    (4, 3, 6),
    (6, 4, 3),
])
def test_scalene(a, b, c):
    assert Triangle(a, b, c).type == TriangleType.SCALENE


@pytest.mark.parametrize("a,b,c", [
    (3, 4, 5),
    (4, 3, 5),
    (5, 4, 3),
    (5, 3, 4),
    (5, 12, 13),
])
def test_right(a, b, c):
    assert Triangle(a, b, c).type == TriangleType.RIGHT

@pytest.mark.parametrize("a,b,c,expected_msg", [
    (0, 0, 0, "strictly positive"),
    (5, 0, 3, "strictly positive"),
    (1, 2, 3, "equal to the sum"),
    (5, 2, 2, "greater than the sum"),
])
def test_invalid_cases(a, b, c, expected_msg):
    t = Triangle(a, b, c)
    assert t.type == TriangleType.INVALID
    assert expected_msg in t.explanation

@pytest.mark.parametrize("a,b,c,expected", [
    (3, 3, 3, "all sides are equal"),
    (2, 2, 3, "two sides are equal"),
    (3, 4, 6, "all sides are different"),
])
def test_basic_explanations(a, b, c, expected):
    assert expected in Triangle(a, b, c).explanation


@pytest.mark.parametrize("a,b,c", [
    (3, 4, 5),
    (5, 3, 4),
    (4, 5, 3),
])
def test_right_explanation(a, b, c):
    t = Triangle(a, b, c)
    assert "rectangular" in t.explanation
    assert "²" in t.explanation


def test_explanation_not_empty():
    assert Triangle(3, 4, 5).explanation.strip() != ""


def test_explanation_consistency():
    assert "equilateral" in Triangle(3, 3, 3).explanation.lower()
