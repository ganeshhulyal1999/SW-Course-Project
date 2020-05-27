import os
from operator import itemgetter
files=[]
files=os.listdir("D:/SW Project/sw-data-set/")
files.sort()
mainDict=[]

def makeDict():
    for file in files:
        d = {}
        with open("sw-data-set/"+file,) as f:
            for line in f:
                try:
                    (key, val) = line.split()
                    d[key] = val
                except:
                    pass
        mainDict.append(d)

def getAllModels():
    entry=raw_input("Enter All to get all the Mobile Models: ")
    if entry.lower()=="all":
        for i in range(0,len(mainDict)):
            try:
                if mainDict[i]["domain"]=="Mobile":
                    try:
                        print(mainDict[i]["model-name"])
                        print(mainDict[i]["model-number"])
                        print("----------------")
                    except:
                        pass
            except:
                pass


def searchByBrand():
    res=[]
    print("Search by Models: ")
    modelName=raw_input("Enter Brand Name or Model Name or Mobile to get all Brands:")
    for i in range(len(mainDict)):
        str=(dict(filter(lambda item: modelName.lower() in item[1].lower(), mainDict[i].items())))
        if(str!={}):
            res.append(mainDict[i])
    if(len(res)==0):
        print("--------------------------")
        print("Sorry :( No Products found")
        print("--------------------------")
    else:
        for i in range(0, len(res)):
            try:
                print("Model Name: " + res[i]['model-name'])
                print("RAM: " + res[i]['ram'])
                print("Internal Storage:" + res[i]['internal-storage'])
                print("Processor Core: " + res[i]['processor-core'])
                print("-----------------------------------------")
            except:
                pass


def searchBySpecs():
    filteredByRAM = []
    filteredByProcessor=[]
    filteredByPrimaryCam=[]
    print("Search By Specifications: ")
    ram = raw_input("Enter RAM size: ")
    ram+"-GB"
    for i in range(len(mainDict)):
        str = (dict(filter(lambda item: ram.lower() in item[1].lower(), mainDict[i].items())))
        if (str != {}):
            filteredByRAM.append(mainDict[i])
        else:
            pass
    processor = raw_input("Enter Processor Name: ")
    for i in range(len(filteredByRAM)):
        str1 = (dict(filter(lambda item: processor.lower() in item[1].lower(), filteredByRAM[i].items())))
        if (str1 != {}):
            filteredByProcessor.append(filteredByRAM[i])
        else:
            pass
    cam = raw_input("Enter Primary Camera in MP ")
    cam+"-megapixel"
    for i in range(len(filteredByProcessor)):
        str2 = (dict(filter(lambda item: processor.lower() in item[1].lower(), filteredByProcessor[i].items())))
        if (str2 != {}):
            filteredByPrimaryCam.append(filteredByProcessor[i])
        else:
            pass
    for i in range(0,len(filteredByPrimaryCam)):
        print("----------------------------")
        print("Model Name: "+filteredByPrimaryCam[i]['model-name'])
        print("Processor Name: " + filteredByPrimaryCam[i]['model-name'])
        print("Primary Camera: " + filteredByPrimaryCam[i]['processor-type'])
        print("Brand Name " + filteredByPrimaryCam[i]['product-name'])

if __name__ == '__main__':
    makeDict()
    items=mainDict[0].items()
    print(items[2])
    while True:
        print("Mobile Phones Recomondation System")
        print("\n 1. Get all the Models \n 2. Search Brands by Model \n 3. Search by Specifications")
        choice = raw_input("Enter your choice: ")
        if choice == str(1) or choice.lower() == "one":
            getAllModels()
            choice = ""
        elif choice == str(2) or choice.lower() == "two":
            searchByBrand()
            choice = ""
        elif choice == str(3) or choice.lower() == "three":
            searchBySpecs()
            choice = ""
        else:
            print("Oops Something went wrong try Again!")
