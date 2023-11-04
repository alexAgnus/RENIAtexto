import pandas as pd


class DatasetListMapper:

    def __init__(self):
        pass

    def execute(self, filepath: str):
        df = pd.read_csv(filepath)
        list_of_text = []
        for index, row in df.iterrows():
            text = ""
            for column in df.columns:
                if column != "id" and column != "date":
                    text += str(row[column]) + ", "
            list_of_text.append(text)
        return list_of_text
