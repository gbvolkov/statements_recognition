from datetime import datetime
from io import TextIOWrapper
import pandas as pd
from const import COLUMNS


# датапроводки|во|nдок|банккорр|корреспондент|счетконтрагента|дебет|кредит|назначениеплатежа
# датапроводки|датапроводки.1|во|nдок|nдок.1|банккорр|корреспондент|счетконтрагента|дебет|кредит|кредит.1|назначениеплатежа
# датапроводки|датапроводки.1|во|nдок|nдок.1|банккорр|иннконтрагента|наименованиеконтрагента|счетконтрагента|дебет|дебет.1|кредит|назначениеплатежа
# COLUMNS = ["clientID", "clientBIC", "clientBank", "clientAcc", "clientName", "stmtDate", "stmtFrom", "stmtTo", "openBalance", "totalDebet", "totalCredit", "closingBalance",
#           "entryDate", "cpBIC", "cpBank", "cpAcc", "cpTaxCode", "cpName", "Debet", "Credit", "Comment",
#           "filename"]
def BankStatement_30_process(
    header: pd.DataFrame,
    data: pd.DataFrame,
    footer: pd.DataFrame,
    inname: str,
    clientid: str,
    params: dict,
    sheet: str,
    logf: TextIOWrapper,
) -> pd.DataFrame:
    df = pd.DataFrame(columns=COLUMNS)

    df["entryDate"] = data["датапроводки"]
    # df["cpBIC"] = data["БИК банка корр."]
    df["cpBank"] = data["банккорр"]
    df["cpAcc"] = data["счетконтрагента"]
    
    if "иннконтрагента" in data.columns:
        df["cpTaxCode"] = data["иннконтрагента"]
    if "корреспондент" in data.columns:
        df["cpName"] = data["корреспондент"]
    if "наименованиеконтрагента" in data.columns:
        df["cpName"] = data["наименованиеконтрагента"]
    df["Debet"] = data["дебет"]
    df["Credit"] = data["кредит"]
    df["Comment"] = data["назначениеплатежа"]

    if len(header.axes[0]) >= 1:
        set_header_fields(header, footer, df)
    if len(footer.axes[0]) >= 1:
        set_footer_fields(footer, df)

    return df

def set_footer_fields(footer, df):
    cbalance = footer[footer.iloc[:, 0] == "Исходящий остаток"].dropna(
            axis=1, how="all"
        )
    if cbalance.size > 2:
        df["closingBalance"] = cbalance.iloc[:, 2].values[0]
    turnovers = footer[footer.iloc[:, 0] == "Итого обороты"].dropna(
            axis=1, how="all"
        )
    if turnovers.size > 1:
        df["totalDebet"] = turnovers.iloc[:, 1].values[0]
    if turnovers.size > 2:
        df["totalCredit"] = turnovers.iloc[:, 2].values[0]

def set_header_fields(header, footer, df):
    acc = header[header.iloc[:, 0] == "СЧЕТ"].dropna(axis=1, how="all")
    if acc.size > 1:
        df["clientAcc"] = acc.iloc[:, 1].values[0]
    cname = header[header.iloc[:, 0] == "НАЗВАНИЕ"].dropna(axis=1, how="all")
    if cname.size > 1:
        df["clientName"] = cname.iloc[:, 1].values[0]
    cbic = footer[footer.iloc[:, 0] == "БИК"].dropna(axis=1, how="all")
    if cbic.size > 1:
        df["clientBIC"] = cbic.iloc[:, 1].values[0]
    df["clientBank"] = header.iloc[0, 0]

    obalance = header[header.iloc[:, 0] == "Входящий остаток"].dropna(
            axis=1, how="all"
        )
    if obalance.size > 0:
        df["openBalance"] = obalance.iloc[:, obalance.size-1].values[0]
