open_file = open("CupcakeInvoices.csv")
total_flavor = 0
each_total = 0



for line in open_file:
    line = line.strip()
    values = line.split(',')
#     # print(values)
#     # print(values[2: 3])
    # print(values[4: 5])
    type = int(values[3])
    cost = float(values[4])
    each_total = each_total + (type * cost)
    each_total = round(each_total, 2)
print(each_total)


open_file.close()