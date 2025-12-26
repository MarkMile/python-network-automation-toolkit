# network/executor.py
# This module provides functionality to execute commands on network devices.

from network.connector import NetworkConnector


class DeviceExecutor:
    """
    Class to execute commands on network devices.
    """

    def __init__(self, devices: list[dict[str, str]]):
        """
        Initialize the DeviceExecutor with a list of devices.

        Args:
            devices (list[dict[str, str]]): A list of dictionaries containing device connection details.
        """
        self.devices = devices

    def run_command(self, command: str) -> dict[str, dict]:
        """
        Execute a command on all devices and return the results.

        Args:
            command (str): The command to execute on the devices.
        """
        results = {}

        for device in self.devices:
            name = device["name"]
            connector = NetworkConnector(device)

            # Attempt to connect and run the command
            try:
                connector.connect()
                output = connector.send_command(command)
                results[name] = {"status": "success", "output": output}
            # Catch all exceptions to log errors
            except Exception as e:
                results[name] = {"status": "error", "error": str(e)}
            finally:
                connector.disconnect()

        return results
