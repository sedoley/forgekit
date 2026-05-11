"""Test suite for forgekit."""
from src.app import greet, process_data

def test_greet():
    assert "Hello" in greet()
    assert "forgekit" in greet()

def test_process_data():
    result = process_data([10, 20, 30])
    assert result["count"] == 3
    assert result["average"] == 20

# Helper added in commit #23
def helper_23():
    return "real-change-23"
