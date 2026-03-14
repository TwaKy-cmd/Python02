#!/usr/bin/env python3

def garden_operations() -> None:
    print("=== Garden Error Types Demo ===\n")

    print("Testing ValueError...")
    try:
        int("abc")
    except ValueError as e:
        print(f"Caught ValueError: {e}\n")

    print("Testing ZeroDivisionError...")
    try:
        1 / 0
    except ZeroDivisionError as e:
        print(f"Caught ZeroDivisionError: {e}\n")

    print("Testing FileNotFoundError...")
    try:
        f = open("missing.txt")
        f.close()
    except FileNotFoundError as e:
        print(f"Caught FileNotFoundError: {e}\n")

    print("Testing KeyError...")
    try:
        mon_dico = {"tomate": 10}
        plante = mon_dico["missing_plant"]
        print(f"{plante}")
    except KeyError as e:
        print(f"Caught KeyError: {e}\n")

    print("Testing multiple errors together...")
    try:
        int("xyz")
    except (ValueError, ZeroDivisionError, KeyError, FileNotFoundError):
        print("Caught an error, but program continues!\n")


def test_error_types() -> None:
    garden_operations()
    print("All error types tested successfully!")


if __name__ == "__main__":
    test_error_types()
