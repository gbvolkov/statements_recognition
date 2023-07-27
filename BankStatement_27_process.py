from datetime import datetime
from io import TextIOWrapper
import pandas as pd
from const import COLUMNS

#номерстроки|датапроводки|видоперации|номердокументаклиента|номердокументабанканомердокументавсмфр|счетплательщикаполучателя|суммадебет|суммакредит|назначениеплатежа
#номерстроки|датапроводки|видоперации|номердокументаклиента|номердокументабанканомердокументавсмфр|счетплательщикаполучателя|наименованиекорреспондирующегосчета|суммадебет|суммакредит|назначениеплатежа
#COLUMNS = ["clientID", "clientBIC", "clientBank", "clientAcc", "clientName", "stmtDate", "stmtFrom", "stmtTo", "openBalance", "totalDebet", "totalCredit", "closingBalance",
#           "entryDate", "cpBIC", "cpBank", "cpAcc", "cpTaxCode", "cpName", "Debet", "Credit", "Comment",
#           "filename"]
def BankStatement_27_process(header: pd.DataFrame, data: pd.DataFrame, footer: pd.DataFrame, inname: str, clientid: str, params: dict, sheet: str, logf: TextIOWrapper) -> pd.DataFrame:
    df = pd.DataFrame(columns = COLUMNS)

    df["entryDate"] = data["датапроводки"]
    #df["cpBIC"] = data["БИК банка корр."]
    #df["cpBank"] = data["Банк контрагента"]
    df["cpAcc"] = data["счетплательщикаполучателя"]
    if "наименованиекорреспондирующегосчета" in data.columns:
        df["cpName"] = data["наименованиекорреспондирующегосчета"]
    df["Debet"] = data['суммадебет']
    df["Credit"] = data['суммакредит']
    df["Comment"] = data["назначениеплатежа"]

    if len(header.axes[0]) >= 1:
        acc = header[header.iloc[:,0].fillna("").str.startswith('Счет:')].dropna(axis=1,how='all')
        if acc.size > 1:
            df["clientAcc"] = acc.iloc[:,1].values[0]
        clname = header[header.iloc[:,0].fillna("").str.startswith('Наименование:')].dropna(axis=1,how='all')
        if clname.size > 1:
            df["clientName"] = clname.iloc[:,1].values[0]
        df["clientBank"] = header.iloc[1,0]

        obalance = header[header.iloc[:,0].fillna("").str.startswith('Входящий остаток')].dropna(axis=1,how='all')
        if obalance.size > 2:
            df["openBalance"] = obalance.iloc[:,2].values[0]
    if len(footer.axes[0]) >= 1:
        cbalance = footer[footer.iloc[:,0].fillna("").str.startswith('Исходящий остаток')].dropna(axis=1,how='all')
        if cbalance.size > 2:
            df["closingBalance"] = cbalance.iloc[:,2].values[0]
        turnovers = footer[footer.iloc[:,0].fillna("").str.startswith('Итого обороты:')].dropna(axis=1,how='all')
        if turnovers.size > 1:
            df["totalDebet"] = turnovers.iloc[:,1].values[0]
        if turnovers.size > 2:
            df["totalCredit"] = turnovers.iloc[:,2].values[0]

    
    return df
