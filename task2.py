import json
import csv

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def convert_csv_to_json() -> None:
    with open(INPUT_FILENAME, "r") as csv_file:
        csv_data = list(csv.DictReader(csv_file,
                                       delimiter=',',
                                       lineterminator='\n'))

    with open(OUTPUT_FILENAME, "w") as json_file:
        json.dump(csv_data, json_file, indent=4)


if __name__ == '__main__':
    convert_csv_to_json()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")