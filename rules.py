def get_rules_for_level(level: int) -> dict:
    rules = { }

    if level in (1, 2):
        rules = {
            "numbers": False,
            "indentation": "spaces_4"
        }
    elif level in (3, 4):
        rules = {
            "numbers": True,
            "indentation": "spaces_3"
        }
    elif level in (5, 6, 7, 8, 9, 10):
        rules = {
            "numbers": True,
            "indentation": "emdash"
        }


    return rules