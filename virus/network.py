import requests
import base64

class NetworkWriter:
    def send_data(self, data: bytes, url: str, machine: str = "default") -> None:
        try:
            # data is now bytes, not string
            encoded_data = base64.b64encode(data).decode('utf-8')
            payload = {"machine": machine, "data": encoded_data}
            response = requests.post(url, json=payload)
            response.raise_for_status()
            
        except requests.RequestException as e:
            print(f"Failed to send data: {e}")