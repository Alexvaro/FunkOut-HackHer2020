# -*- coding: utf-8 -*-
#----------------------------- REWARDS PAGE ----------------------------------
import random
#----------------------------- IMPORTING CSV ----------------------------------
import pandas as pd
import math
#Loading the CSV file of the user usage & reinforcement/fact phrases
usage_df = pd.read_csv('https://raw.githubusercontent.com/tan-ts/Hack_Her1/main/UserHours.csv?token=AQL6IYLBMFYESFW3G6E4X6S7U5RVE')
#Library of mental health facts to encourage the user to continue on the activity
reinforce_df = pd.read_csv('https://raw.githubusercontent.com/tan-ts/Hack_Her1/main/Facts%2BPositive%20reinforcements.csv')
col_name = reinforce_df.keys()
#Method that informs the user of their usage on the app
#Takes the user's usage info and outputs their hours spent on each activity
class PointsPerActivity:
    def __init__(self, activity, hours):
        self.activity = activity - 1
        self.hours = hours
            
    def displayActivityFact(self):
        if(self.activity == 0):
            print(reinforce_df.iloc[(random.randint(0,2)),0])
        if(self.activity == 1):
            print(reinforce_df.iloc[(random.randint(0,2)),1])
        if(self.activity == 2):
            print(reinforce_df.iloc[(random.randint(0,2)),2])
        if(self.activity == 3):
            print(reinforce_df.iloc[(random.randint(0,2)),3])
        if(self.activity == 4):
            print(reinforce_df.iloc[(random.randint(0,2)),4])
        if(self.activity == 5):
            print(reinforce_df.iloc[(random.randint(0,2)),5])

    def displayHoursPerActivity(self):
        strActivity = col_name[self.activity]
        print("You have spent " + str(self.hours) + " hours on " + strActivity + ".")



class PointsSummary:
    def __init__(self, total_hours):
        self.total_hours = total_hours        
        
    def displayTotalHrs(self):
        print("You have spent " + str(self.total_hours) + " hours on Funk Out.")
        points = math.floor(self.total_hours/2)
        print("You have " + str(points) + " points.")
        #CONVERT HOURS TO POINTS AND SUBTRACT POINTS WHEN THEY ARE REDEEMED
        #PRINT: YOUR TOTAL POINTS ARE ...
        if self.total_hours < 20:
            print("You are a SUPERSTAR!")
            
        elif self.total_hours >= 20  and self.total_hours < 50:
            print("You are a MERRY MAKER!")
                
        elif self.total_hours >= 50 and self.total_hours < 100:
            print("You are a SUPER SOCIALIZER!")

        else:
            print("You are a SOCIAL BUTTERFLY!")


        
def findUser(target, usage_df):
    #Declare a list of names in the CSV file
    names = usage_df.loc[:, 'Name']
    #Finding the corresponding key identifier # to the name
    x = 0
    directory_num = 0
    for i in names: #Iterates through names and finds a match. Assumes the name exists in the file.
        if(target == i):
            directory_num = x
            return directory_num
        x = x + 1

def totalAppHours(usage_df): #Shows the total amount of hours spent on the app
    total_hours = 0
    for z in range(1, len(usage_df.keys())): #Calls on the user and returns their rewards level     
        hr = usage_df.iloc[directory_num,z]
        total_hours += hr
    return total_hours

def detailedActivitiesAndFacts(usage_df, directory_num):
    #Shows the amount of hours per each activity & a corresponding mental health fact
    total_hours = 0
    for z in range(1, len(usage_df.keys())): #Calls on the user and returns their rewards level     
        act = z
        hr = usage_df.iloc[directory_num,z]
        total_hours += hr
        prize = PointsPerActivity(act, hr)
        print("")
        prize.displayHoursPerActivity()
        prize.displayActivityFact()
        

#Setting the person to be searched and saving their row number in the CSV file as a variable
target = input("Enter the name of the person you are looking for: ")
print("")
directory_num = findUser(target, usage_df)
print("")

#Displaying the total points/hours associated with the target
general_hours = PointsSummary(totalAppHours(usage_df))

general_hours.displayTotalHrs()
print("")

#Displaying the time spent on each activity and a positive reinforcement fact to complement it
detailedActivitiesAndFacts(usage_df, directory_num)
