import csv

library = []
with open('books.csv','r',encoding='utf-8') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        library.append(row)

# print(row)
# print(library)

print(library[0].items())
print(library[1].items())
print(library[2].items())
#

# class Book: {
# }
#
# class Member: {
#
# }
#
#
# booklist = {"" :"",
#             "" : ""}
