import pytest
import requests
import random
import string


class ProjectAPI:
    def __init__(self, base_url, token):
        self.base_url = base_url
        self.headers = {"Authorization": f"Bearer {token}"}
        
    def create_project(self, name, description=None):
        url = f"{self.base_url}/api-v2/projects"
        payload = {"name": name}
        if description:
            payload["description"] = description
            
        response = requests.post(url, json=payload, headers=self.headers)
        return response
    
    def update_project(self, project_id, name=None, description=None):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        payload = {}
        if name:
            payload["name"] = name
        if description:
            payload["description"] = description
            
        response = requests.put(url, json=payload, headers=self.headers)
        return response
    
    def get_project(self, project_id):
        url = f"{self.base_url}/api-v2/projects/{project_id}"
        response = requests.get(url, headers=self.headers)
        return response


@pytest.fixture
def api():
    # Токен и URL нужно будет заменить при запуске тестов
    base_url = "https://api.yougile.com"
    token = "YOURTOKEN"  #подставить свой токен
    return ProjectAPI(base_url=base_url, token=token)


@pytest.fixture
def random_project_name():
    random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=8))
    return f"Test Project {random_suffix}"


@pytest.fixture
def created_project(api, random_project_name):
    response = api.create_project(name=random_project_name)
    project_data = response.json()
    project_id = project_data["id"]
    
    yield project_id, project_data
    


class TestProjectsAPI:
        
    def test_create_project_positive(self, api, random_project_name):
        response = api.create_project(name=random_project_name)
        
        assert response.status_code == 201, f"Ожидался код 201, получен {response.status_code}"
        
        project_data = response.json()
        assert project_data["name"] == random_project_name, "Имя проекта не соответствует отправленному"
        assert "id" in project_data, "В ответе отсутствует ID проекта"
    
    def test_update_project_positive(self, api, created_project):
        project_id, _ = created_project
        new_name = f"Updated Project {random.randint(1000, 9999)}"
        new_description = "Updated description for testing"
        
        response = api.update_project(project_id, name=new_name, description=new_description)
        
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        
        updated_data = response.json()
        assert updated_data["name"] == new_name, "Имя проекта не обновилось"
        assert updated_data["description"] == new_description, "Описание проекта не обновилось"
    
    def test_get_project_positive(self, api, created_project):
        project_id, original_data = created_project
        
        response = api.get_project(project_id)
        
        assert response.status_code == 200, f"Ожидался код 200, получен {response.status_code}"
        
        project_data = response.json()
        assert project_data["id"] == project_id, "ID проекта не соответствует ожидаемому"
        assert project_data["name"] == original_data["name"], "Имя проекта не соответствует ожидаемому"
    
    
    def test_create_project_negative_empty_name(self, api):
        response = api.create_project(name="")
        
        assert response.status_code == 400, f"Ожидался код 400, получен {response.status_code}"
    
    def test_update_project_negative_invalid_id(self, api):
        invalid_id = "nonexistent_id_12345"
        
        response = api.update_project(invalid_id, name="New Name")
        
        assert response.status_code == 404, f"Ожидался код 404, получен {response.status_code}"
    
    def test_get_project_negative_invalid_id(self, api):
        invalid_id = "nonexistent_id_12345"
        
        response = api.get_project(invalid_id)
        

        assert response.status_code == 404, f"Ожидался код 404, получен {response.status_code}"





