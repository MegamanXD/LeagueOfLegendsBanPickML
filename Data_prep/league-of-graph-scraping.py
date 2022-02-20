from bs4 import BeautifulSoup
import csv

# This HTML file is from this website: https://www.leagueofgraphs.com/champions/builds
# I went into the website and press Ctrl + S to save the HTML code

with open('Champions stats - League of Legends.html', 'r') as f:
    contents = f.read()
soup = BeautifulSoup(contents, 'lxml')
# print(soup.prettify())
champion_table = soup.find("table", {"class": "data_table with_sortable_column"})
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
        row[0] = row[0].replace('.', '')
        row[1] = row[1].replace('AD Carry', '').replace('Mid', '').replace('Top', '').replace('Support', '').replace('Jungler', "").replace('   ', '').replace(' , ', '').strip()
        row[5] = row[5].replace('   ', '').split(' / ')
        for element in row[5]:
            row.append(element)
        row.pop(5)
    row_index += 1

for row in output_rows:
    print(row)

with open('output2.csv', 'w') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerows(output_rows)

# Don't know why but after csv file is generated,
# I have to open excel to tweak some wrong rows and delete empty lines :))
