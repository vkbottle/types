import yaml


def get_config(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = yaml.load(f, Loader=yaml.Loader)
        return data
