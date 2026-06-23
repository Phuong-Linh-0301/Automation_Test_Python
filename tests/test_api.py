import pytest
from utils.api_helper import APIHelper
from utils.config_reader import ConfigReader

class TestDummyJSONProductsAPI:
    """API tests for the DummyJSON products resource."""
    
    @pytest.fixture(autouse=True)
    def setup(self):
        self.api_helper = APIHelper(base_url=ConfigReader.get_api_base_url())
        yield
        self.api_helper.close_session()
        
    @pytest.mark.get
    def test_get_product(self):
        # call api voi endpoint la "/products/1" de lay thong tin san pham co id = 1
        response = self.api_helper.get("/product/1")
        print("Response JSON:", response)  # Debugging line to print the response JSON
        
        # response = self.api_helper.get("/products",params={"limit":2},)
        assert response.status_code == 200
        product = response.json()
        assert product["id"] == 1
        assert product["title"] == 'Essence Mascara Lash Princess'