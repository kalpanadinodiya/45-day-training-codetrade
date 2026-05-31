# JSON Config Manager

import json

def save_config(data: dict, filename: str):
    with open(filename, "w") as file:
        json.dump(data, file, indent=4)

def load_config(filename: str) -> dict:
    with open(filename, "r") as file:
        return json.load(file)

def update_config(filename: str, key: str, value):
    config = load_config(filename)
    config[key] = value
    save_config(config, filename)


config_data = {
    "model": "GPT",
    "learning_rate": 0.01,
    "epochs": 10
}

save_config(config_data, "config.json")

update_config("config.json", "epochs", 20)

print(load_config("config.json"))

# Difference:
# json.dump() writes JSON directly to a file.
# json.dumps() converts Python object into a JSON string.