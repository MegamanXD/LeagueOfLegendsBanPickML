from bs4 import BeautifulSoup
import csv

with open('Champion Best with_Best against stats - League of Legends.html', 'r') as f:
    contents = f.read()
soup = BeautifulSoup(contents, 'lxml')
champion_table = soup.find("table")
# print(champion_table.prettify())
champion_table.find_all()

output_rows = []

for e in soup.findAll('br'):
    e.extract()

for table_row in champion_table.findAll('tr'):
    columns = table_row.findAll('td')
    output_row = []
    for column in columns:
        output_row.append(column.text.replace('\n', '').strip())
    output_rows.append(output_row)

row_index = 0
for row in output_rows:
    if len(row) <= 1:
        del output_rows[row_index]
    else:
        row[0] = row[0].replace('  ', '').replace('AD Carry', '').replace('Mid', '').replace('Top', '').replace('Support', '').replace('Jungler', "").replace('   ', '').replace(',', '').strip()
        row[1] = row[1].replace('%', '')
        row[2] = row[2].replace('  ', '').replace('AD Carry', '').replace('Mid', '').replace('Top', '').replace('Support', '').replace('Jungler', "").replace('   ', '').replace(',', '').replace('%', '').strip().split('+')
        row[3] = row[3].replace('  ', '').replace('AD Carry', '').replace('Mid', '').replace('Top', '').replace('Support', '').replace('Jungler', "").replace('   ', '').replace(',', '').replace('%', '').strip().split('+')
        row[4] = row[4].replace('  ', '').replace('AD Carry', '').replace('Mid', '').replace('Top', '').replace('Support', '').replace('Jungler', "").replace('   ', '').replace(',', '').replace('%', '').strip().split('-')
        for element in row[2]:
            row.append(element)
        for element in row[3]:
            row.append(element)
        for element in row[4]:
            row.append(element)
        row.pop(2)
        row.pop(2)
        row.pop(2)
    row_index += 1
with open('champion-bestwith-counters-bestagainst.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    # Because the first row has error so I will put it in another file then add it again
    for row in output_rows[1:]:
        print(row)
        writer.writerow(row)
