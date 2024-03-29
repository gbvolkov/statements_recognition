from datetime import datetime
from io import TextIOWrapper
import pandas as pd
from const import COLUMNS


# дата|видопер|nдок|бик|банкконтрагента|контрагент|иннконтрагента|счетконтрагента|дебетrub|кредитrub|операция
# COLUMNS = ["clientID", "clientBIC", "clientBank", "clientAcc", "clientName", "stmtDate", "stmtFrom", "stmtTo", "openBalance", "totalDebet", "totalCredit", "closingBalance",
#           "entryDate", "cpBIC", "cpBank", "cpAcc", "cpTaxCode", "cpName", "Debet", "Credit", "Comment",
#           "filename"]
def BankStatement_10_process(
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

    df["entryDate"] = data["дата"]
    df["cpBIC"] = data["бик"]
    df["cpBank"] = data["банкконтрагента"]
    df["cpAcc"] = data["счетконтрагента"]
    df["cpTaxCode"] = data["иннконтрагента"]
    df["cpName"] = data["контрагент"]
    df["Debet"] = data["дебетrub"]
    df["Credit"] = data["кредитrub"]
    df["Comment"] = data["операция"]

    # header: За период,c 22.06.2020 по 22.06.2021,,,,
    if len(header.axes[0]) >= 1:
        set_header_fields(header, df)

    if len(footer.axes[0]) >= 1:
        set_footer_fields(footer, df)

    return df

def set_footer_fields(footer, df):
    cbalance = footer[
            footer.iloc[:, 0].fillna("").str.startswith("Исходящий остаток")
        ].dropna(axis=1, how="all")
    if cbalance.size > 1:
        df["closingBalance"] = cbalance.iloc[:, 1].values[0]
    turnovers = footer[footer.iloc[:, 0] == "ИТОГО ОБОРОТЫ"].dropna(
            axis=1, how="all"
        )
    if turnovers.size > 1:
        df["totalDebet"] = turnovers.iloc[:, 1].values[0]
    if turnovers.size > 2:
        df["totalCredit"] = turnovers.iloc[:, 2].values[0]

def set_header_fields(header, df):
    clientName = header[header.iloc[:, 0] == "Владелец счета"].dropna(
            axis=1, how="all"
        )
    if clientName.size > 1:
        df["clientName"] = clientName.iloc[:, 1].values[0]
        # df["clientBIC"] = data["Клиент.БИК"]
    df["clientBank"] = header.iloc[0, 0]
    clientAcc = header[header.iloc[:, 0] == "Счет"].dropna(axis=1, how="all")
    if clientAcc.size > 1:
        df["clientAcc"] = clientAcc.iloc[:, 1].values[0]

    obalance = header[
            header.iloc[:, 0] == "Остаток на конец предыдущего периода:"
        ].dropna(axis=1, how="all")
    if obalance.size > 1:
        df["openBalance"] = obalance.iloc[:, 1].values[0]
