import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def testingFunc():
    df = pd.read_csv("titanic.csv")
    df = df[['PassengerId', 'Survived', 'Pclass', 'Name', 'Sex', 'Age', 'SibSp',
        'Parch', 'Ticket', 'Fare', 'Cabin', 'Embarked']]
    cor = df.corr()
    print(cor)
    sns.heatmap(data = cor)