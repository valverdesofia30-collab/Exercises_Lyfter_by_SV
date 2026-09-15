import pytest
from Funciones1_test import sum_numbers

def test_sum_numbers_sum_list_of_numbers():
    #Arrange
    numbers_list= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    #Act
    result = sum_numbers(numbers_list)
    
    #Assert
    assert result == 550

