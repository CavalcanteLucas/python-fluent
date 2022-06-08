import csv

with inplace(csvfilename, 'r', newline='') as (infh, outfh):
    reader = csv.reader(infh)
    write = csv.write(outfh)

    for row in reader:
        row += ['new', 'columns']
        write.writerow(row)