"""Simple, robust calculator.

Improvements over the original:
- Clear separation between parsing, calculation, and I/O
- Handles invalid numeric input without crashing
- Handles invalid operators cleanly
- Handles division-by-zero and other errors
- Exposes `calculate(a, op, b)` so the logic can be unit-tested
- Interactive loop supports 'q'/'quit' to exit
"""

from __future__ import annotations
from typing import Union


Number = Union[int, float]


def calculate(a: Number, op: str, b: Number) -> float:
    """Perform calculation and return result as float.

    Supported operations: +, -, *, x, X, /, // (floor), %, **

    Raises
    ------
    ValueError: if op is not supported
    ZeroDivisionError: if division by zero occurs
    """
    op = op.strip()
    if op in {"+"}:
        return float(a + b)
    if op in {"-"}:
        return float(a - b)
    if op in {"*", "x", "X"}:
        return float(a * b)
    if op == "/":
        if b == 0:
            raise ZeroDivisionError("division by zero")
        return float(a / b)
    if op == "//":
        if b == 0:
            raise ZeroDivisionError("integer division by zero")
        return float(a // b)
    if op == "%":
        if b == 0:
            raise ZeroDivisionError("modulo by zero")
        return float(a % b)
    if op == "**":
        return float(a**b)
    raise ValueError(f"unsupported operator: {op!r}")


def _read_number(prompt: str) -> float:
    while True:
        raw = input(prompt).strip()
        if raw.lower() in {"q", "quit", "exit"}:
            raise KeyboardInterrupt
        try:
            # Accept ints and floats
            return float(raw) if ("." in raw or "e" in raw.lower()) else float(int(raw))
        except ValueError:
            print("Invalid number — please try again (or type 'q' to quit).")


def _read_operator(prompt: str) -> str:
    while True:
        raw = input(prompt).strip()
        if raw.lower() in {"q", "quit", "exit"}:
            raise KeyboardInterrupt
        if raw in {"+", "-", "*", "x", "X", "/", "//", "%", "**"}:
            return raw
        print(
            "Invalid operator — supported: +, -, *, x, /, //, %, ** (or type 'q' to quit)"
        )


def main() -> None:
    print("Simple Calculator — enter numbers and an operator. Type 'q' to quit.")
    try:
        while True:
            a = _read_number("Enter the first number: ")
            op = _read_operator("Enter an operator (+, -, *, /, //, %, **): ")
            b = _read_number("Enter the second number: ")

            try:
                result = calculate(a, op, b)
            except ZeroDivisionError as e:
                print("Error:", e)
                continue
            except ValueError as e:
                print("Error:", e)
                continue

            # Display integer-looking floats without excessive decimals
            if result.is_integer():
                result_display = int(result)
            else:
                result_display = round(result, 10)

            print(f"{a} {op} {b} = {result_display}")
            print("---")

    except KeyboardInterrupt:
        print("\nCalculator exit — goodbye!")


if __name__ == "__main__":
    main()
