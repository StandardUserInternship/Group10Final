# This class role is to read through a file, depending on what the user wants
import csv


class readTitanicFile:
    # Attribute1 => the column you want to get the data for
    # Attribute2 => the column you are comparing with the first column
    # stringData => the given condition of column 2
    def __init__(self, attribute1, attribute2, stringData: str) -> None:
        self.attribute1 = attribute1
        self.attribute2 = attribute2
        self.stringData = stringData

    # Prints a column of the given attribute
    def getAttribute(self) -> list:
        newList = []
        with open("titanic.csv", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                newList.append(line[self.attribute1])
        return newList

    # Prints out the selected column1 that matches with conditions of column2
    def getAttributeByNum(self):
        newList = []
        with open("titanic.csv", mode="r") as csv_file:
            csv_reader = csv.DictReader(csv_file)
            for line in csv_reader:
                if line[self.attribute2] == self.stringData:
                    newList.append(line[self.attribute1])
        return newList
