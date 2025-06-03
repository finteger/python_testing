from main import get_weather, add, divide
import pytest

def test_get_weather():
    assert get_weather(19) == "cold"
    assert get_weather(31) == "hot"
    
def test_divide():
    with pytest.raises(ValueError, match='Cannot divide by zero'):
        divide(10, 0)
    
    