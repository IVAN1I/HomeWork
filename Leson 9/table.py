data = ''' id,name,segment,state,city
CG-12520,Claire Gute,Consumer,Kentucky,Henderson
DV-13045,Darrin Van Huff,Corporate,California,Los Angeles
SO-20335,Sean O'Donnell,Consumer,Florida,Fort Lauderdale
BH-11710,Brosina Hoffman,Consumer,California,Los Angeles
AA-10480,Andrew Allen,Consumer,North Carolina,Concord
IM-15070,Irene Maddox,Consumer,Washington,Seattle
HP-14815,Harold Pawlan,Home Office,Texas,Fort Worth
PK-19075,Pete Kriz,Consumer,Wisconsin,Madison
AG-10270,Alejandro Grove,Consumer,Utah,West Jordan
ZD-21925,Zuschuss Donatelli,Consumer,California,San Francisco
KB-16585,Ken Black,Corporate,Nebraska,Fremont
SF-20065,Sandra Flanagan,Consumer,Pennsylvania,Philadelphia
EB-13870,Emily Burns,Consumer,Utah,Orem
EH-13945,Eric Hoffmann,Consumer,California,Los Angeles
TB-21520,Tracy Blumstein,Consumer,Pennsylvania,Philadelphia
MA-17560,Matt Abelman,Home Office,Texas,Houston '''



rows = [line.split(',') for line in data.split('\n')]

max_lengths = [max(len(row[i]) for row in rows) for i in range(len(rows[0]))]

for row in rows:
    formatted_row = ' '.join(f'{value.ljust(length)}' for value, length in zip(row, max_lengths))
    print(formatted_row)