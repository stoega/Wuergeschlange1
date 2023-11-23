import os

def merge_csv_files(*paths: str, delimiter = ';': str, only_shared_columns = False: bool)
    for path in paths:
        with open(path) as f:
            