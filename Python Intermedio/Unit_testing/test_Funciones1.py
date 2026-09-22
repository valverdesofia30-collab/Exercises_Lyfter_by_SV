import pytest
from Funciones1_test import sum_numbers

def test_sum_numbers_sum_list_of_numbers():
    #Arrange
    numbers_list= [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    
    #Act
    result = sum_numbers(numbers_list)
    
    #Assert
    assert result == 550

def test_sum_numbers_sum_list_of_numbers2():
    #Arrange
    numbers_list= [5, 8, 10, 102, 25, 60, 40]
    
    #Act
    result = sum_numbers(numbers_list)
    
    #Assert
    assert result == 250
    
def test_sum_numbers_sum_list_of_numbers2():
    #Arrange
    numbers_list= [20, 80, 70, 66, 91, 20]
    
    #Act
    result = sum_numbers(numbers_list)
    
    #Assert
    assert result == 347
    
def test_sum_numbers_sum_list_of_numbers2():
    #Arrange
    numbers_list= [25, 3, 20, 250, 69, 70, 81]
    
    #Act
    result = sum_numbers(numbers_list)
    
    #Assert
    assert result == 518        