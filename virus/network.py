import requests
class NetworkWriter:
    def send_data(self, data: str, machine_name: str) -> None:
        requests.post(machine_name, data=data)