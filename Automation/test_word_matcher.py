import pytest
from word_matcher import count_word_matches

# -----------------------------
# Exercise 1: Basic Parameterized Tests
# -----------------------------

@pytest.mark.parametrize(
    "text, target, expected",
    [
        ("The cat sat on the mat", "cat", 1), # Expect 1 (Only "cat" matches, not "cat" in "concatenate").
        ("Dog dog DOG dOg", "dog", 4), # Expect 4 (Case-insensitive matches)
        ("Hello world", "world", 1), # Expect 1
        ("hello hello HELLO", "hello", 3), # Expect 3
        ("No matches here", "yes", 0), #Expect 0 (No matches).
        ("catcat cat catdog", "cat", 1), # Expect 2 (Only standalone "cat" counts, not "cat" in "catcat"). i think Expect would be 1.
        ("a a a", "a", 3), # Expect 3.
    ]
)
def test_count_word_matches(text, target, expected):
    assert count_word_matches(text, target) == expected

# -----------------------------
# Exercise 2: Edge Case Tests
# -----------------------------

@pytest.mark.parametrize("text, target, expected", [
    ("", "word", 0),                      # Empty text
    ("hello world", "", 0),              # Empty target
    ("", "", 0),                         # Both empty
    ("hello  world", "world", 1),        # Multiple spaces
    (" cat ", "cat", 1),                 # Leading/trailing spaces
    ("cat,dog cat", "cat", 1),           # Punctuation not handled,   ---- hier expected value will be 1
    ("x y z", "x", 1),                   # Single character word
])
def test_edge_cases(text, target, expected):
    assert count_word_matches(text, target) == expected

# -----------------------------
# Exercise 3: Negative Testing
# -----------------------------

@pytest.mark.parametrize("text, target", [
    (None, "word"),               # None text
    ("hello world", None),        # None target
    (123, "word"),                # Integer text
    ("hello world", 456),         # Integer target
    (["hello", "world"], "world"), # List text
    ("hello world", ["world"]),   # List target
])
def test_invalid_inputs_raise_typeerror(text, target):
    with pytest.raises(TypeError):
        count_word_matches(text, target)

