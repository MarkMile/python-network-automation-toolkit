from netmiko import ConnectHandler
from netmiko.exceptions import NetMikoTimeoutException, NetMikoAuthenticationException

class NetworkConnector:
    def __init__(self, device: dict[str, str]):
        self.device = device
        self.connection = None

    def connect(self):
        try:
            self.connection = ConnectHandler(
                device_type=self.device["device_type"],
                host=self.device["host"],
                username=self.device["username"],
                password=self.device["password"]
            )
        except NetMikoTimeoutException as e:
            raise ConnectionError(f"Timeout connecting to {self.device["host"]}.")
        except NetMikoAuthenticationException as e:
            raise PermissionError(f"Authentication failed for {self.device["host"]}.")
        
    def disconnect(self):
        if self.connection:
            self.connection.disconnect()

    def send_command(self, command: str) -> str:
        if not self.connection:
            raise RuntimeError("Not connected to any device.")
        
        return self.connection.send_command(command)