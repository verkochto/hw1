import pytest
import requests
import random
import string


class ConfigManager:
    
    @staticmethod
    def get_api_settings():
        return {
            "base_url": "https://api.yougile.com",
            "token": "YOUR_TOKEN"  
        }


@pytest.fixture(scope="session")
def api_settings():
    return ConfigManager.get_api_settings()


@pytest.fixture(scope="session")
def random_generator():
    class RandomGenerator:
        @staticmethod
        def generate_string(prefix="", length=8):
            random_suffix = ''.join(random.choices(string.ascii_lowercase + string.digits, k=length))
            return f"{prefix}{random_suffix}"
            
        @staticmethod
        def generate_project_name():
            return RandomGenerator.generate_string("Test Project ")
    
    return RandomGenerator()
