import csv
from ex_15_8_a__inplace import inplace

csvfilename = 'dev/null' # placeholder
with inplace(csvfilename, 'r', newline='') as (infh, outfh):
    reader = csv.reader(infh)
    write = csv.write(outfh)

    for row in reader:
        row += ['new', 'columns']
        write.writerow(row)