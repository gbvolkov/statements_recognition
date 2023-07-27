from datetime import datetime
from io import TextIOWrapper
import pandas as pd
from const import COLUMNS

#дата|nдок|во|названиекорр|иннкорр|бикбанкакорр|счеткорр|дебет|кредит|назначение
#COLUMNS = ["clientID", "clientBIC", "clientBank", "clientAcc", "clientName", "stmtDate", "stmtFrom", "stmtTo", "openBalance", "totalDebet", "totalCredit", "closingBalance",
#           "entryDate", "cpBIC", "cpBank", "cpAcc", "cpTaxCode", "cpName", "Debet", "Credit", "Comment",
#           "filename"]
def BankStatement_47_process(header: pd.DataFrame, data: pd.DataFrame, footer: pd.DataFrame, inname: str, clientid: str, params: dict, sheet: str, logf: TextIOWrapper) -> pd.DataFrame:
    
    df = pd.DataFrame(columns = COLUMNS)

    df["entryDate"] = data["дата"]
    df["cpBIC"] = data["бикбанкакорр"]
    #df["cpBank"] = data["контрагент.банк(бик,наименование)"]
    df["cpAcc"] = data["счеткорр"]
    df["cpTaxCode"] = data["иннкорр"]
    df["cpName"] = data["названиекорр"]

    df["Debet"] = data["дебет"]
    df["Credit"] = data["кредит"]
    df["Comment"] = data["назначение"]

    
    return df
