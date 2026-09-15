import pytest
from Funciones3_test import my_favorite_restaurant

def test_my_favorite_restaurant_count_upper_letters():
    #Arrange
    uppercase_count = 0
    restaurant= "I love Today Sushi"
    
    #Act
    result = my_favorite_restaurant(uppercase_count)
    
    #Assert
    assert result[0] == 3
    
def test_my_favorite_restaurant_count_lower_letters():
    #Arrange
    lowercase_count = 0
    
    #Act
    result = my_favorite_restaurant(lowercase_count)
    
    #Assert
    assert result[1] == 12