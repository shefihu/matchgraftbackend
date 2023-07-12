import datetime
import json


def format_datetime_to_iso(date_time: datetime.datetime) -> str:
    return date_time.replace(tzinfo=datetime.timezone.utc).isoformat().replace("+00:00", "Z")


def snake_to_camel(string: str) -> str:
    return "".join(word if idx == 0 else word.capitalize() for idx, word in enumerate(string.split(sep="_")))


def store_json_data(file_path: str, json_content: dict[str, str | int | float | bool] | list[dict[str, str | int | float | bool]]):
    try:
        with open(file_path, "r+") as fp:
            if len(fp.read(0)) == 0:
                fp.write(json.dumps(json_content, sort_keys=True, indent=4))
            else:
                fp.write(",\n" + json.dumps(json_content, sort_keys=True, indent=4))
    except Exception as err:
        raise err


def retrieve_json_data(file_path: str):
    try:
        with open(file_path, "r") as f:
            try:
                return json.load(f)
            except json.JSONDecodeError as err:
                print(err)
                return None
    except Exception as err:
        print(err)
        return None
