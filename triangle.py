import sys
from dataclasses import dataclass
from enum import Enum, auto

from rich.console import Console


class TriangleType(Enum):
    EQUILATERAL = auto()
    ISOSCELES = auto()
    SCALENE = auto()
    RIGHT = auto()
    INVALID = auto()


@dataclass(frozen=True, slots=True)
class Triangle:
    side1: int
    side2: int
    side3: int

    @property
    def type(self) -> TriangleType:
        a, b, c = self.side1, self.side2, self.side3
        # Validação básica
        if a <= 0 or b <= 0 or c <= 0 or a >= b + c or b >= a + c or c >= a + b:
            return TriangleType.INVALID
        if a == b == c:
            return TriangleType.EQUILATERAL
        # Checa retângulo (teorema de Pitágoras)
        if a ** 2 == b ** 2 + c ** 2 or b ** 2 == a ** 2 + c ** 2 or c ** 2 == a ** 2 + b ** 2:
            return TriangleType.RIGHT
        if a == b or a == c or b == c:
            return TriangleType.ISOSCELES
        return TriangleType.SCALENE

    @property
    def explanation(self) -> str:
        a, b, c = self.side1, self.side2, self.side3
        t = self.type
        # Mensagens de erro informativas
        if t == TriangleType.INVALID:
            if a <= 0 or b <= 0 or c <= 0:
                return "The sides do not form a valid triangle because all sides must be strictly positive."
            if a >= b + c:
                cond = "equal to" if a == b + c else "greater than"
                return f"The sides do not form a valid triangle because {a} is {cond} the sum of {b} and {c}."
            if b >= a + c:
                cond = "equal to" if b == a + c else "greater than"
                return f"The sides do not form a valid triangle because {b} is {cond} the sum of {a} and {c}."
            if c >= a + b:
                cond = "equal to" if c == a + b else "greater than"
                return f"The sides do not form a valid triangle because {c} is {cond} the sum of {a} and {b}."
        # Mensagens de classificação
        if t == TriangleType.EQUILATERAL:
            return f"The sides form an equilateral triangle because all sides are equal ({a}={b}={c})."
        if t == TriangleType.RIGHT:
            # Lógica para mostrar qual lado é a hipotenusa na explicação
            if a ** 2 == b ** 2 + c ** 2:
                math_str = f"{a}² = {b}² + {c}²"
            elif b ** 2 == a ** 2 + c ** 2:
                math_str = f"{b}² = {a}² + {c}²"
            else:
                math_str = f"{c}² = {a}² + {b}²"
            return f"The sides form a rectangular scalene triangle because {math_str}."
        if t == TriangleType.ISOSCELES:
            return "The sides form an isosceles triangle because two sides are equal."
        return "The sides form a scalene triangle because all sides are different."


if __name__ == "__main__":
    console = Console()
    if len(sys.argv) != 4:
        console.print("[bold yellow]⚠️  Usage: python triangle.py <side1> <side2> <side3>[/bold yellow]")
    else:
        try:
            # Conversão e chamada
            sides = [int(x) for x in sys.argv[1:4]]
            t = Triangle(*sides)
            if t.type == TriangleType.INVALID:
                console.print(f"[bold red]🚫 Invalid triangle:[/bold red] [red]{t.explanation}[/red]")
            else:
                console.print(f"[bold green]✅ Success![/bold green] [cyan]{t.explanation}[/cyan]")
        except ValueError:
            console.print("[bold red]❌ Error:[/bold red] [red]Please enter only integer numerical values.[/red]")
