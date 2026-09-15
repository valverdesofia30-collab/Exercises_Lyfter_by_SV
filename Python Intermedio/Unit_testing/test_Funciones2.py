import pytest
from Funciones2_test import text

def test_text_reversed_text():
    #Arrange
    first_text= "Hello Daniel"
    
    #Act
    result = text(first_text)
    
    #Assert
    assert result == "leinaD olleH"