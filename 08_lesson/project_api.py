from api_client import ApiClient


class ProjectAPI(ApiClient):    
    def create_project(self, name, description=None):
        
        payload = {"name": name}
        if description:
            payload["description"] = description
            
        return self._request("POST", "/api-v2/projects", payload=payload)
    
    def update_project(self, project_id, name=None, description=None):
       
        payload = {}
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
            
        return self._request("PUT", f"/api-v2/projects/{project_id}", payload=payload)
    
    def get_project(self, project_id):
       
        return self._request("GET", f"/api-v2/projects/{project_id}")
