import requests

class ApiClient:
    
    def __init__(self, base_url, token):        

        self.base_url = base_url
        self.token = token
        self.headers = {"Authorization": f"Bearer {token}"}
    
    def _request(self, method, endpoint, payload=None, params=None):
       
        url = f"{self.base_url}{endpoint}"
        
        if method.upper() == "GET":
            return requests.get(url, headers=self.headers, params=params)
        elif method.upper() == "POST":
            return requests.post(url, headers=self.headers, json=payload, params=params)
        elif method.upper() == "PUT":
            return requests.put(url, headers=self.headers, json=payload, params=params)
        elif method.upper() == "DELETE":
            return requests.delete(url, headers=self.headers, params=params)
        else:
            raise ValueError(f"Неподдерживаемый HTTP метод: {method}")
