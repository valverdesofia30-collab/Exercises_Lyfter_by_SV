import pytest
from Funciones3_test import my_favorite_restaurant

def test_my_favorite_restaurant_count_upper_letters():
    #Arrange
    
    #Act
    result = my_favorite_restaurant()
    
    #Assert
    assert result[0] == 3
    
def test_my_favorite_restaurant_count_lower_letters():
    #Arrange
    
    #Act
    result = my_favorite_restaurant()
    
    #Assert
    assert result[1] == 12
    
def test_my_favorite_restaurant_count_all_letters():
    #Arrange
   
    
    #Act
    result = my_favorite_restaurant()
    
    #Assert
    assert result[2] == 15    