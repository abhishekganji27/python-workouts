from main import pig_latin_v4
import pytest

@pytest.mark.parametrize("word,expected", [
    # Basic cases
    ("wine", "wineway"),
    ("wind", "indway"),
    ("apple", "appleway"),
    ("dog", "ogday"),
    ("sky", "kysay"),

    # Same vowel repeated
    ("loop", "ooplay"),
    ("meet", "eetmay"),

    # Multiple different vowels
    ("education", "educationway"),
    ("audio", "audioway"),

    # Capitalization
    ("Wine", "Wineway"),
    ("Wind", "Indway"),
    ("Apple", "Appleway"),
    ("Loop", "Ooplay"),

    # Edge cases
    ("a", "aay"),
    ("aa", "aaay"),
    ("ae", "aeway"),
    ("b", "bay"),

    # Tricky
    ("queue", "queueway"),
])
def test_pig_latin_v4(word, expected):
    assert pig_latin_v4(word) == expected
