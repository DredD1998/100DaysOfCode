from prettytable import PrettyTable

table = PrettyTable()
table.add_column("Name",["Hirak","Supriya","Nargish"])
table.add_column("Position",["CEO","Manager","HR"])
table.border = False
print(table)



