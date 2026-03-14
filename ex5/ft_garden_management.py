#!/usr/bin/env python3

class GardenError(Exception):
    pass


class PlantError(GardenError):
    pass


class WaterError(GardenError):
    pass


class GardenManager:
    def __init__(self) -> None:
        self.plants = []

    def add_plant(self, plant_name: str) -> None:
        if not plant_name:
            raise ValueError("Plant name cannot be empty!")
        self.plants.append(plant_name)
        print(f"Added {plant_name} successfully")

    def water_plants(self, plant_list: str) -> None:
        print("Opening watering system")
        try:
            for plant in plant_list:
                print(f"Watering {plant} - success")
        finally:
            print("Closing watering system (cleanup)")

    def check_health(self, plant_name: str, water_level: int,
                     sunlight_hours: int) -> None:
        if water_level > 10:
            raise ValueError(f"Water level {water_level} is too high (max 10)")
        print(f"{plant_name}: healthy (water: {water_level},"
              f" sun: {sunlight_hours})")

    def trigger_system_failure(self) -> None:
        raise WaterError("Not enough water in tank")


def test_garden_management() -> None:
    print("=== Garden Management System ===")
    manager = GardenManager()

    print("Adding plants to garden...")
    try:
        manager.add_plant("tomato")
        manager.add_plant("lettuce")
        manager.add_plant("")
    except ValueError as e:
        print(f"Error adding plant: {e}")

    print("Watering plants...")
    manager.water_plants(["tomato", "lettuce"])

    print("Checking plant health...")
    try:
        manager.check_health("tomato", 5, 8)
    except ValueError as e:
        print(f"Error checking tomato: {e}")

    try:
        manager.check_health("lettuce", 15, 8)
    except ValueError as e:
        print(f"Error checking lettuce: {e}")

    print("Testing error recovery...")
    try:
        manager.trigger_system_failure()
    except GardenError as e:
        print(f"Caught GardenError: {e}")
        print("System recovered and continuing...")

    print("Garden management system test complete!")


if __name__ == "__main__":
    test_garden_management()
