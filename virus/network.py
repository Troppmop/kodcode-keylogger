import requests
class NetworkWriter:
    def send_data(self, data: str, url: str, machine: str = "default") -> None:
        try:
            payload = {"machine": machine, "data": data}
            response = requests.post(url, json=payload)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"Failed to send data: {e}")