# network/connector.py
# This module provides functionality to connect to network devices using Netmiko.

from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException


class NetworkConnector:
    """
    Class to manage connections to network devices using Netmiko.
    """

    def __init__(self, device: dict):
        """
        Initialize the NetworkConnector with device details.

        Args:
            device (dict): A dictionary containing device connection details.
        """
        self.device = device
        self.connection = None

    def connect(self):
        """
        Establish a connection to the network device.
        """
        try:
            self.connection = ConnectHandler(
                device_type=self.device["device_type"],
                host=self.device["host"],
                username=self.device["username"],
                password=self.device["password"],
            )
        except NetMikoTimeoutException as e:
            raise ConnectionError(f"Timeout connecting to {self.device["host"]}.")
        except NetMikoAuthenticationException as e:
            raise PermissionError(f"Authentication failed for {self.device["host"]}.")

    def disconnect(self):
        """
        Disconnect from the network device.
        """
        if self.connection:
            self.connection.disconnect()

    def send_command(self, command: str) -> str:
        """
        Send a command to the connected network device.

        Args:
            command (str): The command to send to the device.
        """
        if not self.connection:
            raise RuntimeError("Not connected to any device.")

        return self.connection.send_command(command)
