import sqlite3

con = sqlite3.connect('example.db')
print(type(con))