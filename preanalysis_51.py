import pandas as pd
from pathlib import Path
import os
from argparse import (
    ArgumentParser,
    ArgumentDefaultsHelpFormatter,
    BooleanOptionalAction,
)
import sys
from const import DOCTYPES
from collections import namedtuple

from excelutils import get_excel_sheet_kind, get_head_lines_excel

from pdfutils import get_head_lines_pdf

def process_pdf(pdfname, clientid, fdate, logf):
    kinds = []
    berror = False
    try:
        headers = get_head_lines_pdf(pdfname, 30)
        if suitable := [
            kind
            for kind in DOCTYPES
            if len([row for row in headers if kind in row.lower()]) > 0
        ]:
            kinds.append(suitable[0])
        print(pdfname, "::KIND:", kinds)
    except Exception as err:
        berror = True
        print(pdfname, "_", "ND", ":ERROR:", err)
        fileext = Path(pdfname).suffix
        logstr = f"ERROR|{clientid}|{os.path.basename(pdfname)}|ND|UNDEFINED|{fileext}|{fdate}|{type(err).__name__} {err}\n"
        logf.write(logstr)
    return (kinds[0], berror) if kinds else ("UNDEFINED", berror)


def process_excel(xlsname, clientid, fdate, logf):
    Result = namedtuple('Result', 'kind error')
    kind = "UNDEFINED"
    berror = False
    sheets = pd.read_excel(xlsname, header=None, sheet_name=None)
    if len(sheets) > 1:
        print(f"{xlsname}:WARNING: {len(sheets)} sheets found")
    for sheet in sheets:
        try:
            kind, _ = get_excel_sheet_kind(sheets[sheet])
            print(f"{xlsname}:{sheet}:KIND:{kind}")
            if kind != "UNDEFINED":
                return Result(kind, False)
        except Exception as err:
            berror = True
            print(f"{xlsname}_{sheet}:ERROR:{err}")
            fileext = Path(xlsname).suffix
            logstr = f"ERROR|{clientid}|{os.path.basename(xlsname)}|{sheet}|UNDEFINED|{fileext}|{fdate}|{type(err).__name__} {err}\n"
            logf.write(logstr)
    return Result(kind, berror)



def process(inname, clientid, fdate, logf):
    lower_inname = inname.lower()
    if lower_inname.endswith((".xls", ".xlsx")):
        return process_excel(inname, clientid, fdate, logf)
    elif lower_inname.endswith(".pdf"):
        return process_pdf(inname, clientid, fdate, logf)
    return ("", False)


from pathlib import Path
import os
from argparse import ArgumentParser, ArgumentDefaultsHelpFormatter

def main():
    parser = ArgumentParser(formatter_class=ArgumentDefaultsHelpFormatter)
    parser.add_argument("-d", "--data", default="../Data/", help="Data folder")
    parser.add_argument("-l", "--logfile", default="./data/preanalys_202409.txt", help="Log file")
    args = vars(parser.parse_args())

    DIRPATH = args["data"]
    logname = args["logfile"]

    with open(logname, "w", encoding="utf-8", buffering=1) as logf:
        FILEEXT = (".xls", ".xlsx", ".xlsm", ".pdf")
        sys.stdout.reconfigure(encoding="utf-8", line_buffering=True)  # type: ignore

        for _, ftypes, names in sorted(os.walk(DIRPATH)):
            for ftype in ftypes:
                folder = os.path.join(DIRPATH, ftype)
                for root_l1, clientids, _ in sorted(os.walk(folder)):
                    for clientid in clientids:
                        folder = os.path.join(root_l1, clientid)
                        for root_l2, fdates, _ in sorted(os.walk(folder)):
                            for fdate in fdates:
                                folder = os.path.join(root_l2, fdate)
                                for root, dirs, files in sorted(os.walk(folder)):
                                    for name in sorted(files):
                                        if name.lower().endswith(FILEEXT):
                                            inname = os.path.join(root, name)
                                            #clientid = os.path.basename(root)
                                            fileext = Path(name).suffix
                                            try:
                                                kind, _ = process(inname, clientid, fdate, logf)
                                                if kind:
                                                    logstr = f"PROCESSED|{clientid}|{inname}|ALL|{kind}|{fileext}|{fdate}|OUT\n"
                                                else:
                                                    logstr = f"FILE_ERROR|{clientid}|{inname}||UNDEFINED|{fileext}|{fdate}|TYPE CANNOT BE DEFINED\n"
                                                logf.write(logstr)
                                            except Exception as err:
                                                print(inname, ":ERROR:", err)
                                                logstr = f"FILE_ERROR|{clientid}|{inname}||UNDEFINED|{fileext}|{fdate}|{type(err).__name__} {err}\n"
                                                logf.write(logstr)


main()
