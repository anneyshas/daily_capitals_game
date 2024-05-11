import pandas as pd
import random

data = pd.read_csv("country-list.csv")
num = random.randint(0,247)

country = data.iloc[num].country
capital = data.iloc[num].capital

quiz = random.randint(0,1)
correct = False

if quiz == 0:
    print(f"{capital} is the capital of _________.")
    response = input("Enter country name: ")
    if response == country:
        correct = True
elif quiz == 1:
    print(f"The capital of {country} is __________.")
    response = input("Enter capital city name: ")
    if response == capital:
        correct = True

if correct:
    print("Correct answer.")
else:
    print("Incorrect answer.")

print(f"The capital of {country} is {capital}.")