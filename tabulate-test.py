from tabulate import tabulate

category = ["phone","phone","phone","phone","phone","phone","tablet","tablet","tablet"]

itemcode = ["BPCM","BPSH","RPSS","RPLL","YPLS","YPLL","RTMS","RTLM","YTLM","YTLL"]

description = ["compact","clam shell","robophone-5inch screen and 64GB memory","robophone-6inc screen and 256GB memory","y-phone standard-6inch screen and 64GB memory","y-phone deluxe - 6inch screen and 256GB memory","robotab - 8inch screen and 64GB memory","robotab - 10inch screen and 128GB memory","y-tab standard - 10inch screen and 128GB memory","y-tab deluxe - 10inch screen and 256GB memory"]

price = ["29.99","49.99","199.99","499.99","549.99","649.99","149.99","299.99","499.99","599.99"]



def printPTtable():

    data =[]

    for i in range(0,len(category)):

        if category[i]=="phone" or category[i]=="tablet":
            array = [category[i],itemcode[i],description[i],price[i]]
            data.append(array)
    print(tabulate(data,headers=["TYPE","CODE","DESCRIPTION","COST"],tablefmt = "fancy_grid",numalign = "right"))
    print("")

def main():
    printPTtable()

if __name__ == '__main__':
    main()