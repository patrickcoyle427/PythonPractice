import csv

with open('latin_vocabulary_list.csv', encoding='utf-8', newline = '') as to_import:

    to_read = csv.reader(to_import)
    this = [row for row in to_read]

    possible_words = [word for word in this[1:] if int(word[4]) < 25]
    # The first row of this CSV file is the column headers, so row 0
    # is skipped.

for row in possible_words:

    print(row)
