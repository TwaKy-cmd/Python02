#!/usr/bin/env python3


class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


def Plant_error() -> None:
    print("Testing PlantError...")
    raise PlantError("The tomato plant is wilting!")


def Water_error() -> None:
    print("Testing WaterError...")
    raise WaterError("Not enough water in the tank!")


def ft_custom_errors() -> None:
    print("=== Custom Garden Errors Demo ===\n")

    try:
        Plant_error()
    except PlantError as e:
        print(f"Caught PlantError: {e}\n")

    try:
        Water_error()
    except WaterError as e:
        print(f"Caught WaterError: {e}\n")

    print("Testing catching all garden errors...")

    try:
        Plant_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    try:
        Water_error()
    except GardenError as e:
        print(f"Caught a garden error: {e}\n")

    print("All custom error types work correctly!")


if __name__ == "__main__":
    ft_custom_errors()
