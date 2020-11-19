#Source(s): 
#https://realpython.com/python-csv/
#https://www.studyusa.com/en/a/2029/american-slang-words-you-need-to-know-in-2020

import csv

print("Welcome to the Slang Translator!")
print()

print("You want to add a new word?")
print("yes or no?")
answer = input().lower()
print()

if "yes" in answer:
  print("It will continue to ask you for word ", end="")
  print("until you type in stop")
  print()
  while True:
    slang = input("Word in English slang: ")
    language = input("Word in another language: ")
    if slang == "stop" or language == "stop":
      break;
    with open("Slang:EtoM.csv", "a") as file:
      writer = csv.writer(file)
      writer.writerow((slang, language))
print()

print("Want to show the list of slang words?")
print("yes or no?")
listWords = input().lower()
print()

if "yes" in listWords:
  print("The List of Slang Words:")
  with open("Slang:EtoM.csv") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
        else:
            print(f"{row[0]}")
            line_count += 1
  print()

  print("Want to find the translation of one of these words?")
  print("yes or no?")
  listDef = input().lower()
  print()

  if "yes" in listDef:
    defination = input("Type in the word: ").lower()
    with open("Slang:EtoM.csv") as csv_file:
      csv_reader = csv.reader(csv_file, delimiter=',')
      for row in csv_reader:
            if line_count == 0:
                line_count += 1
            elif defination in row:
                print(f"Translation: {row[1]}")
            else:
                line_count += 1



