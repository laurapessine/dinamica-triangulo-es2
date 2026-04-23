import sys
from dataclasses import dataclass
from enum import Enum, auto

from rich.console import Console


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    RIGHT = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: int
    side2: int
    side3: int

    def __post_init__(self):
        # FAIL-FAST: Impede que triângulos impossíveis sejam criados
        a, b, c = self.side1, self.side2, self.side3
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError('The sides do not form a valid triangle because all sides must be strictly positive.')
        # Verifica a desigualdade triangular especificando quem falhou
        if a >= b + c:
            condition = 'equal to' if a == b + c else 'greater than'
            raise ValueError(
                f'The sides do not form a valid triangle because {a} is {condition} the sum of {b} and {c}.')
        if b >= a + c:
            condition = 'equal to' if b == a + c else 'greater than'
            raise ValueError(
                f'The sides do not form a valid triangle because {b} is {condition} the sum of {a} and {c}.')
        if c >= a + b:
            condition = 'equal to' if c == a + b else 'greater than'
            raise ValueError(
                f'The sides do not form a valid triangle because {c} is {condition} the sum of {a} and {b}.')

    @property
    def type(self) -> TriangleType:
        a, b, c = self.side1, self.side2, self.side3
        if a == b == c:
            return TriangleType.EQUILATERAL
        # Checa o retângulo antes de classificar como isósceles/escaleno
        if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
            return TriangleType.RIGHT
        if a == b or a == c or b == c:
            return TriangleType.ISOSCELES
        return TriangleType.SCALENE

    @property
    def explanation(self) -> str:
        a, b, c = self.side1, self.side2, self.side3
        t = self.type
        if t == TriangleType.EQUILATERAL:
            return f'The sides form an equilateral triangle because all sides are equal ({a} = {b} = {c}).'
        if t == TriangleType.RIGHT:
            if a ** 2 == b ** 2 + c ** 2: return f'The sides form a rectangular triangle because {a}² = {b}² + {c}².'
            if b ** 2 == a ** 2 + c ** 2: return f'The sides form a rectangular triangle because {b}² = {a}² + {c}².'
            if c ** 2 == a ** 2 + b ** 2: return f'The sides form a rectangular triangle because {c}² = {a}² + {b}².'
        if t == TriangleType.ISOSCELES:
            return 'The sides form an isosceles triangle because two sides are equal.'
        return 'The sides form a scalene triangle because all sides are different.'


if __name__ == '__main__':
    console = Console()
    if len(sys.argv) != 4:
        console.print('[bold yellow]⚠️  Uso correto: python triangle.py <lado1> <lado2> <lado3>[/bold yellow]')
    else:
        try:
            l1 = int(sys.argv[1])
            l2 = int(sys.argv[2])
            l3 = int(sys.argv[3])
            triangulo = Triangle(l1, l2, l3)
            console.print(f'[bold green]✅ Sucesso![/bold green] [cyan]{triangulo.explanation}[/cyan]')
        except ValueError as e:
            if 'invalid literal' in str(e):
                console.print(
                    '[bold red]❌ Erro:[/bold red] [red]Por favor, insira apenas valores numéricos inteiros.[/red]')
            else:
                console.print(f'[bold red]🚫 Triângulo inválido:[/bold red] [red]{e}[/red]')
