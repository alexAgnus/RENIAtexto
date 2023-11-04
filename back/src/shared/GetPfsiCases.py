import pandas as pd
from src.pfsi.pfsi_case import PfsiCase


class GetPfsiCases:

    def execute(self, filepath: str):
        df = pd.read_csv(filepath)
        psfi_cases: [PfsiCase] = []
        for index, row in df.iterrows():
            description = ""
            for column in df.columns:
                if column != "id" and column != "date":
                    description += str(row[column]) + ", "
            pfsi_case = PfsiCase(description=description, id=index, similarity=0)
            psfi_cases.append(pfsi_case)
        return psfi_cases
