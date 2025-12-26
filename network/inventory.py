# network/inventory.py
# This module provides functionality to load and parse network device inventory from a YAML file.

import yaml
from pathlib import Path


class InventoryLoader:
    """
    Class to load and parse network device inventory from a YAML file.
    """

    def __init__(self, inventory_path: str):
        """
        Initialize the InventoryLoader with the path to the inventory file.

        Args:
            inventory_path (str): Path to the YAML inventory file.
        """
        self.inventory_path = Path(inventory_path)

    def load_inventory(self) -> list[dict]:
        """
        Load and parse the inventory file.
        """
        # Check if the inventory file exists
        if not self.inventory_path.exists():
            raise FileNotFoundError(f"Inventory file not found: {self.inventory_path}")

        # Load and parse the YAML inventory file
        with open(self.inventory_path, "r") as file:
            try:
                inventory_data: dict[str:str] = yaml.safe_load(file)
            except yaml.YAMLError as e:
                raise ValueError(f"Error parsing YAML file: {e}")

        return inventory_data.get("devices", [])
