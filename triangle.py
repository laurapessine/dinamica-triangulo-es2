import sys
from dataclasses import dataclass
from enum import Enum, auto


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: int
    side2: int
    side3: int

    @property
    def type(self) -> TriangleType:
        a, b, c = self.side1, self.side2, self.side3
        if a <= 0 or b <= 0 or c <= 0:
            return TriangleType.INVALID
        if a == b == c:
            return TriangleType.EQUILATERAL
        if a >= b + c or b >= a + c or c >= a + b:
            return TriangleType.INVALID
        if a == b or a == c or b == c:
            return TriangleType.ISOSCELES
        return TriangleType.SCALENE


if __name__ == '__main__':
    if len(sys.argv) != 4:
        print('Uso correto: python triangle.py <lado1> <lado2> <lado3>')
    else:
        try:
            l1 = int(sys.argv[1])
            l2 = int(sys.argv[2])
            l3 = int(sys.argv[3])
            triangulo = Triangle(l1, l2, l3)
            print(f'O triângulo é {triangulo.type.name}')
        except ValueError:
            print('Erro: Por favor, insira apenas valores numéricos inteiros.')
