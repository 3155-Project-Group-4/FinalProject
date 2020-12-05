import csv

txt_file = r"../Data/ncvoter_Statewide.txt"
csv_file = r"ncvoter_Statewide.csv"

with open(txt_file, "r") as in_text:
    in_reader = csv.reader(in_text, delimiter = '\t')
    with open(csv_file, "w") as out_csv:
        out_writer = csv.writer(out_csv)
        for row in in_reader:
            out_writer.writerow(row)