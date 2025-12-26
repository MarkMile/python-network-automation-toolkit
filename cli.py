#!/usr/bin/env python3
# cli.py
# This is the main CLI entry point for the Network Automation Toolkit.

import argparse

from network.inventory import InventoryLoader
from network.executor import DeviceExecutor
from utils.logger import setup_logger


logger = setup_logger()


def parse_arguments():
    """Parse command-line arguments."""

    # Create the argument parser
    parser = argparse.ArgumentParser(description="Network Automation Toolkit")

    # Required arguments
    parser.add_argument(
        "-c",
        "--command",
        required=True,
        help="Command to execute on the network devices",
    )
    parser.add_argument(
        "-i",
        "--inventory",
        default="inventory/devices.yaml",
        help="Path to the inventory file (YAML format)",
    )

    return parser.parse_args()

def main():
    args = parse_arguments()

    logger.info("Loading inventory...")
    loader = InventoryLoader(args.inventory)
    devices = loader.load_inventory()

    logger.info(f"Loaded {len(devices)} devices from inventory.")

    executor  = DeviceExecutor(devices)
    results = executor.run_command(args.command)

    for device, result in results.items():
        print(f"\n{device.upper()}")
        if result["status"] == "success":
            print(result["output"][:200])  # Print first 200 characters of output
        else:
            print(f"ERROR: {result["error"]}")

# Entry point
if __name__ == "__main__":
    main()