import pytest
from Funciones2_test import text

def test_text_reversed_text():
    #Arrange
    first_text= "Hello Daniel"
    
    #Act
    result = text(first_text)
    
    #Assert
    assert result == "leinaD olleH"
    
def test_text_reversed_text2():
    #Arrange
    first_text= "Hello Sofía"
    
    #Act
    result = text(first_text)
    
    #Assert
    assert result == "aífoS olleH" 
    
def test_text_reversed_text3():
    #Arrange
    first_text= "Hello Diego"
    
    #Act
    result = text(first_text)
    
    #Assert
    assert result == "ogeiD olleH"         