from triangle import Triangle, TriangleType


def test_equilateral():
    t = Triangle(7, 7, 7)
    assert t.type == TriangleType.EQUILATERAL


def test_isosceles():
    t1 = Triangle(2, 2, 3)
    assert t1.type == TriangleType.ISOSCELES
    t2 = Triangle(2, 3, 2)
    assert t2.type == TriangleType.ISOSCELES
    t3 = Triangle(3, 2, 2)
    assert t3.type == TriangleType.ISOSCELES


def test_escalene():
    t = Triangle(3, 4, 5)
    assert t.type == TriangleType.SCALENE


def test_full_zero():
    t = Triangle(0, 0, 0)
    assert t.type == TriangleType.INVALID


def test_negative():
    t1 = Triangle(-3, 4, 5)
    assert t1.type == TriangleType.INVALID
    t2 = Triangle(3, -4, 5)
    assert t2.type == TriangleType.INVALID
    t3 = Triangle(3, 4, -5)
    assert t3.type == TriangleType.INVALID


def test_escalene_invalid():
    t = Triangle(1, 2, 3)
    assert t.type == TriangleType.INVALID


def test_isosceles_invalid():
    t = Triangle(5, 5, 10)
    assert t.type == TriangleType.INVALID


def test_zero_mixed():
    t1 = Triangle(5, 0, 3)
    assert t1.type == TriangleType.INVALID
    t2 = Triangle(0, 5, 3)
    assert t2.type == TriangleType.INVALID
    t3 = Triangle(3, 5, 0)
    assert t3.type == TriangleType.INVALID
