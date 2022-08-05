"""
We will use this script to learn Python to absolute beginners
The script is an example of BMI_Calculator implemented in Python
The BMI_Calculator: 
    # Get the weight(Kg) of the user
    # Get the height(cm) of the user
    # Caculate the BMI using the formula
        BMI=weight in kg/height in centimeters/100)**2

Exercise 5:
        Write a program to calculate the BMI by accepting user input from the keyboard and check whether the user comes
        in underweight ,normal weight or obesity by creating a class. Read the CSV files which contains player data 
        and compare your BMI with a player.Create functions for getting input from the user,calculating BMI and check 
        the user category.While getting input check the value you entered is of correct type if not 
        your program should not get crashed.
       
            i)Get user weight in kg 
            ii)Get user height in centimeter
            iii) Use this formula to calculate the BMI
                    BMI = weight_of_the_user/(height_of_the_user/100)**2 
            iv)Use this level to check user category
                #)Less than or equal to 18.5 is represents underweight
                #)Between 18.5 -24.9 indicate normal weight
                #)Between 25 -29.9 denotes over weight
                #)Greater than 30 denotes obese
        # Hint
            i)Create a function to get the input from the user 
            ii)Use exceptional handling to check user input's type
            ii)Calculate the BMI
            iii)Check the BMI with player BMI by reading the CSV file

"""

import os
import csv

def get_input_to_calculate_bmi():
    "This function gets the input from the user"
    print("enter the weight of user in kg")
    weight_of_the_user = float(input())
    print("enter the height of user in cm")
    height_of_the_user = float(input())
    return weight_of_the_user,height_of_the_user
    
def calculate_bmi(weight_of_the_user,height_of_the_user):
    "This function calculates the bmi"
    # Calculate the BMI of the user according to height and weight
    bmi_of_the_user = round(weight_of_the_user/(height_of_the_user/100)**2,2)

    # Return the BMI of the user to the called function
    return bmi_of_the_user
            
def calculate_bmi(weight_of_the_user,height_of_the_user):
    "This function calculates the bmi"
    # Calculate the BMI of the user according to height and weight
    bmi_of_the_user = round(weight_of_the_user/(height_of_the_user/100)**2)

    # Return the BMI of the user to the called function
    return bmi_of_the_user

def check_user_bmi_category(bmi):
    "This function checks if the user is underweight, normal, overweight or obese"    
    if bmi <= 18.5:
         print("The user is considered as underweight")
    elif bmi > 18.5 and bmi < 24.9:
         print("The user is considered as normal weight")
    elif bmi > 25 and bmi <= 29.9:
        print("The user is considered as overweight")
    elif bmi >=30:
        print("The user is considered as obese")

def compare_user_bmi_with_celebrity_csv(bmi_of_the_user):
    "This functions reads the csv file and compare the BMI value with celebrity and returns the celebrity name"
    filename = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','data',"celebrity.csv"))
    with open(filename,"r") as fp:
        csv_file = csv.reader(fp)
        next(csv_file)
        for i, row in enumerate(csv_file):
            bmi_value = row[3]
            celebrity_name = row[0]    
            if float(bmi_value) == bmi_of_the_user:
                print("Your BMI is matching with:",celebrity_name)
            else:

                 print("your bmi is not matching with any celebrity")
                 break
                 
        
# Program starts here
if __name__ == "__main__":
    # This calling function gets the input from the user
    weight_of_the_user,height_of_the_user = get_input_to_calculate_bmi()     
    
    # This calling function calculates the BMI of the user
    bmi_value = calculate_bmi(weight_of_the_user,height_of_the_user)
    print("BMI of the user is :",bmi_value)
   
    # This function is used to calculate the user's criteria
    check_user_bmi_category(bmi_value)

    # This function is used to read the CSV file and compare the BMI value
    compare_user_bmi_with_celebrity_csv(bmi_value)