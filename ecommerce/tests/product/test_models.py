import pytest

pytestmark = pytest.mark.django_db

class TestCategoryModel:
    
    def test_str_method(self, category_factory):
        #Arrange
        
        #Act
        obj = category_factory(name = 'test-cat')
        
        #Assert
        assert obj.__str__() == "test-cat"
        
              
        
class TestBrandModel:
    
    def test_str_method(self, brand_factory):
        #Arrange
        
        #Act
        obj = brand_factory(name = 'test-brand')
        
        #Assert
        assert obj.__str__() == "test-brand"
        
        
        
class TestProductModel:
    
    def test_str_method(self, product_factory):
        #Arrange
        
        #Act
        obj = product_factory(name = 'test-prod')
        
        #Assert
        assert obj.__str__() == "test-prod"