import csv
from collections import Counter

def count_column_values(file_path, column_name):
    counts = Counter()

    with open(file_path, newline="") as f:
        reader = csv.DictReader(f)
        for row in reader:
            value = row[column_name]
<<<<<<< HEAD
            counts[value] += int(row["amount"])
=======
            counts[value] += 1
>>>>>>> 89fcb8c9a444bb5cc9adc5a802850b9a2b54df28

    return counts

def create_csv_file(filename, content):
    with open("data/raw/" + filename + ".csv", 'w') as file:
        file.write(content)
    print(f"File '{filename}' created and written successfully.")

def gettingBackIntoIt():
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

<<<<<<< HEAD

def main():
    gettingBackIntoIt()
    results = count_column_values("data/raw/sample.csv", "category")
    print(results)
=======
def main():
    gettingBackIntoIt()
    results = count_column_values("data/raw/sample.csv", "category")
    print(results.items)
    create_csv_file("sample2", "id, category, num\n1,A,24\n2,B,37 ")
>>>>>>> 89fcb8c9a444bb5cc9adc5a802850b9a2b54df28

if __name__ == "__main__":
    main()
