import csv


with open('POLICIA_2015.csv') as fh:
    dictreader = csv.DictReader(fh)
    pfa = [x for x in dictreader]


duplicados = [x for x in pfa if x['Filas de siniestros de más de una fila'] == '1']

for x in duplicados:
    print(x)