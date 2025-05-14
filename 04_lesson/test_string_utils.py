import pytest
from string_utils import StringUtils

utils = StringUtils()

# --- capitalize ---
def test_capitalize_positive():
    assert utils.capitalize("skypro") == "Skypro"

def test_capitalize_negative():
    assert utils.capitalize("") == ""


# --- trim ---
def test_trim_positive():
    assert utils.trim("   skypro") == "skypro"

def test_trim_negative():
    assert utils.trim("nospace") == "nospace"


# --- contains ---
def test_contains_positive():
    assert utils.contains("SkyPro", "S") is True

def test_contains_negative():
    assert utils.contains("SkyPro", "Z") is False


# --- delete_symbol ---
def test_delete_symbol_positive():
    assert utils.delete_symbol("SkyPro", "k") == "SyPro"

def test_delete_symbol_negative():
    assert utils.delete_symbol("SkyPro", "X") == "SkyPro"
