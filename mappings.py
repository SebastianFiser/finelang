def word_to_number(word: str) -> int:
    word_to_num_map = {
        "zero": 0,
        "one": 1,
        "two": 2,
        "three": 3,
        "four": 4,
        "five": 5,
        "six": 6,
        "seven": 7,
        "eight": 8,
        "nine": 9,
        "ten": 10
    }
    return word_to_num_map.get(word.lower(), -1) # todo: error handling

def word_to_operator(word: str) -> str:
    word_to_operator_map = {
        "add": "+",
        "subtract": "-",
        "times": "*",
        "divide": "/"
    }
    return word_to_operator_map.get(word.lower(), None) 

def word_to_comparator(word: str) -> str:
    word_to_comparator_map = {
        "is": "==",
        "is_not": "!=",
        "greater_than": ">",
        "less_than": "<",
        "greater_than_or_equal_to": ">=",
        "less_than_or_equal_to": "<="
    }
    return word_to_comparator_map.get(word.lower(), None)