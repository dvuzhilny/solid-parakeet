import json

INPUT_FILE = "input.json"


def sum_products_from_dict_lists(input_data: dict) -> float:
    result = sum([dict_["score"] * dict_["weight"] for dict_ in input_data])
    return round(result, 3)


if __name__ == "__main__":
    with open(INPUT_FILE, 'r') as file:
        data = json.load(file)

    print(sum_products_from_dict_lists(data))