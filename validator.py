import os
import mappings
import rules

def take_fine_filepath(filepath: str) -> dict:
    if (filepath.endswith(".fine") and filepath != "" and os.path.isfile(filepath)):
        suffer_number = suffer_validate(filepath)
        return rules.get_rules_for_level(suffer_number)
    elif (filepath.endswith(".fine") and filepath != "" and not os.path.isfile(filepath)):
        raise FileNotFoundError(f"File '{filepath}' does not exist.")
    elif (not filepath.endswith(".fine") and filepath != "" and os.path.isfile(filepath)):
        raise ValueError(f"File '{filepath}' is not a .fine file.")
    elif (not filepath.endswith(".fine") and filepath != "" and not os.path.isfile(filepath)):
        raise FileNotFoundError(f"File '{filepath}' does not exist and is not a .fine file.")


def suffer_validate(filepath: str) -> int:
    with open(filepath, 'r') as f:
        suffer_line = f.readline().strip()
        suffer_line_splitted = suffer_line.split(":")
        suffer_line_splitted = [s.strip() for s in suffer_line_splitted]
        if (suffer_line_splitted[0] != "SUFFER"):
            raise ValueError(f"File '{filepath}' does not start with 'SUFFER:'")
        suffer_level = suffer_line_splitted[1].strip()
        suffer_level_numbered =  mappings.word_to_number(suffer_level)
        return suffer_level_numbered