#/usr/bin/python

"""
This is a converter, taking the CSV exported from clinicaltrials.gov,
and returning an RIS file which can be imported into reference
management software or systematic review screening tools.
"""

import csv
import datetime
import sys


def no_newline(my_string):
    new_str = str(my_string).replace("\n"," ")

    return new_str

def convertCSVtoRIS(csv_filename, ris_filename):
    my_csv = []
    with open(csv_filename, encoding="utf8") as csvfile:
        reader = csv.reader(csvfile)
        header = next(reader)
        header = header # This is just to quiet the linter
        #print(header)
        for row in reader:
            pruned_row = [row[0],row[1],row[2],row[4],row[5],row[8],row[20],row[24],row[29]]
            my_csv.append(pruned_row)
    ris_tags = ['DOI - ','TI - ','UR - ','J2 - ','AB - ','U1 - ','U2 - ','YR - ','L1 - ']
    whole_file = ""

    today = datetime.datetime.strftime(datetime.datetime.now(), "%Y/%m/%d")

    for trial in my_csv:
        ris_str = "TY  - JOUR\n"
        tags_and_values = zip(ris_tags, trial)
        for pair in tags_and_values:
            ris_str += f"{pair[0]}{no_newline(pair[1])}\n"
        ris_str += "DB - clinicaltrials.gov\n"
        ris_str += f"RD - {today}\n"
        ris_str += "ER - \n"
        #print(ris_str)
        whole_file += ris_str
    
    with open(ris_filename,"w", encoding="utf8") as wf:
        wf.write(whole_file)
    
    finished = f"Conversion finished, the RIS file is {ris_filename}"

    return finished


if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("USAGE: ctg2ris.py CSVFILENAME RISFILENAME")
    elif len(sys.argv) == 3:
        finished = convertCSVtoRIS(sys.argv[1], sys.argv[2])
        print(finished)
    else:
        print("Wrong number of arguments.\nUSAGE: ctg2ris.py CSVFILENAME RISFILENAME")
