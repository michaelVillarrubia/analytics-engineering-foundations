import csv
from collections import Counter

def count_column_values(file_path, column_name):
    counts = Counter()

    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            value = row[column_name]
            counts[value] += 1

    return counts


def main():
    #splice 
    word = "splice"
    print(word[0:2])

    #list practice
    languages = ['sql', 'c#', 'java', 'javascript', 'c']
    print(languages)
    #append
    languages.append('python')
    print(languages)
    #slice
    languages[1:3] = []
    print(languages)
    languages.append('c#')
    languages.append('java')
    print(languages)

if __name__ == "__main__":
    main()
