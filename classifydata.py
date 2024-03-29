import pandas as pd
from datetime import datetime
import os
from argparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
    BooleanOptionalAction,
)
import sys
from io import TextIOWrapper
from BankStatement_NO_process import NoneHDR_process, DATATYPES

from excelutils import get_excel_sheet_kind
from parsing_utils import (
    cleanup_raw_data,
    get_file_ext_list,
    get_header_values,
    get_table_range,
    process_data_from_preanalysis,
    process_other,
    set_data_columns,
)
from pdfutils import get_head_lines_pdf, get_pdf_data

# using this (type: ignore) since camelot does not have stubs
from const import REGEX_ACCOUNT, REGEX_AMOUNT, REGEX_BIC, REGEX_INN, get_active_types, set_active_types
from process_map import HDRSIGNATURES
from utils import print_exception, split_list

import warnings

warnings.filterwarnings("ignore", "This pattern has match groups")


def process_data(
    df: pd.DataFrame,
    headerstr: str,
    inname: str,
    clientid: str,
    sheet: str,
    logf: TextIOWrapper,
) -> pd.DataFrame:
    # sourcery skip: extract-method
    # outdata = pd.DataFrame(columns=["file", "clientid", "sheet", "function", "signature", "header"])
    header, data, footer = get_table_range(df)
    if data.empty:
        return pd.DataFrame(
            [["EMPTY", clientid, inname, sheet, "", "", "", ""]],
            columns=[
                "status",
                "clientid",
                "file",
                "sheet",
                "function",
                "params",
                "signature",
                "header",
            ],
        )
    data = set_data_columns(data)
    data = cleanup_raw_data(data)
    signature = "|".join(data.columns).replace("\n", " ")
    if not headerstr and len(header != 0):
        headerstr = "|".join(
            header[:].apply(lambda x: "|".join(x.dropna().astype(str)), axis=1)
        )
    params = get_header_values(headerstr, signature)

    funcs = list(
        filter(
            lambda item: item is not None, [sig.get(signature) for sig in HDRSIGNATURES]
        )
    )
    func = funcs[0] if funcs else NoneHDR_process
    return pd.DataFrame(
        [["PROCESSED", clientid, inname, sheet, func.__name__, str({k: v for k, v in params.items() if k in ("bic", "account", "inn", "amount")}), signature, headerstr]],  # type: ignore
        columns=[
            "status",
            "clientid",
            "file",
            "sheet",
            "function",
            "params",
            "signature",
            "header",
        ],
    )


def process_excel(
    inname: str, clientid: str, logf: TextIOWrapper
) -> tuple[pd.DataFrame, int, bool]:
    berror = False
    df = pd.DataFrame()
    result = pd.DataFrame()

    sheets = pd.read_excel(inname, header=None, sheet_name=None)
    if len(sheets) > 1:
        print(f"{datetime.now()}:{inname}:WARNING:{len(sheets)} sheets found")
    for sheet in sheets:
        try:
            df = sheets[sheet].dropna(axis=1, how="all")
            if not df.empty:
                kind, header = get_excel_sheet_kind(df)
                if kind in get_active_types():
                    outdata = process_data(
                        df, "|".join(header), inname, clientid, str(sheet), logf
                    )
                    if not outdata.empty:
                        result = pd.concat([result, outdata])
                else:
                    logstr = f"{datetime.now()}:PASSED:{clientid}:{os.path.basename(inname)}:{sheet}:0:{kind}\n"
                    logf.write(logstr)
        except Exception as err:
            berror = True
            print_exception(err, inname, clientid, str(sheet), logf)
    return (result, len(sheets), berror)


def process_pdf(
    inname: str, clientid: str, logf: TextIOWrapper
) -> tuple[pd.DataFrame, int, bool]:
    berror = False
    result = pd.DataFrame()

    try:
        df = get_pdf_data(inname, 1)
        if not df.empty:
            header = get_head_lines_pdf(inname, 30)
            outdata = process_data(df, "|".join(header), inname, clientid, "pdf", logf)
            if not outdata.empty:
                result = pd.concat([result, outdata])
    except Exception as err:
        berror = True
        print_exception(err, inname, clientid, "pdf", logf)
    return (result, 1, berror)


def process(
    inname: str, clientid: str, logf: TextIOWrapper
) -> tuple[pd.DataFrame, int, bool]:
    processFunc = process_other

    if inname.lower().endswith(".xls") or inname.lower().endswith(".xlsx"):
        processFunc = process_excel
    elif inname.lower().endswith(".pdf"):
        processFunc = process_pdf

    df, pages, berror = processFunc(inname, clientid, logf)
    return (df, pages, berror)


def main():
    sys.stdout.reconfigure(encoding="utf-8")  # type: ignore
    (
        preanalysislog,
        logname,
        outbasename,
        bSplit,
        maxFiles,
        doneFolder,
        FILEEXT,
        start,
        end,
        types,
    ) = get_parameters()
    set_active_types(types)
    process_data_from_preanalysis(
        process,
        preanalysislog,
        logname,
        outbasename,
        bSplit,
        maxFiles,
        doneFolder,
        FILEEXT,
        start,
        end,
        get_active_types(),
        #["выписка", "карточка счета 51", "карточка счёта 51"]
    )


def get_arguments():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument(
        "-d", "--data", default="./data/test_preanalysis.csv", help="Data folder"
    )
    parser.add_argument("-r", "--done", default="./data/Done", help="Done folder")
    parser.add_argument(
        "-l", "--logfile", default="./data/test_classify_log.txt", help="Log file"
    )
    parser.add_argument(
        "-o",
        "--output",
        default="./data/test_classify",
        help="Resulting file name (no extension)",
    )
    parser.add_argument(
        "--split",
        default=False,
        action=BooleanOptionalAction,
        help="Weather splitting resulting file required (--no-spilt opposite option)",
    )
    parser.add_argument(
        "-m",
        "--maxinput",
        default=500,
        type=int,
        help="Maximum files sored in one resulting file",
    )
    parser.add_argument(
        "--pdf",
        default=True,
        action=BooleanOptionalAction,
        help="Weather to include pdf (--no-pdf opposite option)",
    )
    parser.add_argument(
        "--excel",
        default=True,
        action=BooleanOptionalAction,
        help="Weather to include excel files (--no-excel opposite option)",
    )
    parser.add_argument(
        "-s", "--start", default=-1, type=int, help="Starting position in data file"
    )
    parser.add_argument(
        "-e",
        "--end",
        default=-1,
        type=int,
        help="Ending position in data file (not included)",
    )
    parser.add_argument(
        "-t",
        "--types",
        default=["карточка счета 51"],
        type=split_list,
        help="List of document types to process",
    )
    return vars(parser.parse_args())


def get_parameters():
    args = get_arguments()

    preanalysislog = args["data"]
    logname = args["logfile"]
    outbasename = args["output"]
    bSplit = args["split"]
    maxFiles = args["maxinput"]
    doneFolder = args["done"] + "/"
    FILEEXT = get_file_ext_list(args["excel"], args["pdf"])
    start = args["start"]
    end = args["end"]
    types = args["types"]
    return (
        preanalysislog,
        logname,
        outbasename,
        bSplit,
        maxFiles,
        doneFolder,
        FILEEXT,
        start,
        end,
        types,
    )


if __name__ == "__main__":
    DATATYPES = []
    main()
