import json
import pandas as pd


def read_skills_dict_from_json():
    with open('app/data/skills_idx_dict.json', 'r') as f:
        dct = json.load(f)
    return dct


def read_association_rules():
    return pd.read_csv("app/data/association_rules.csv", index_col=0)


def read_skills():
    return pd.read_csv('app/data/skills_with_occurences.csv')
