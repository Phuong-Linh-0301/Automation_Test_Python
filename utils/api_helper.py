import logging
from typing import Any, Dict, Optional
import requests
from utils.config_reader import ConfigReader


class APIHelper:
    
    def __init__(
        self,
        base_url=None,
        timeout: float = 10,
        headers: Optional[Dict[str, str]] = None,):
        
        self.base_url = base_url
        self.timeout = timeout
        self.session = requests.Session()
        self.session.headers.update(headers or {"Accept": "application/json"})
        
    # This is the main method that all other HTTP methods will call
    def request(self, method, endpoint, params=None, json_data=None, headers=None, timeout=None):
        # 1. Tạo URL đầy đủ
        endpoint = endpoint.lstrip("/")
        url = self.base_url + "/" + endpoint
        
        # 2. Gửi request
        response = self.session.request(
            method = method,
            url = url,
            params = params,
            json = json_data,
            headers = headers,
            timeout = timeout
        )
        # 3. Ghi log status code trả về
        print("Response status: %s", response.status_code)
        
        # 4. Trả response về cho test case xử lý
        return response

    def get(self, endpoint, params=None):
        response = self.request(
            method="GET",
            endpoint=endpoint,
            params=params
        )
        return response
    
    def close_session(self):
        self.session.close()