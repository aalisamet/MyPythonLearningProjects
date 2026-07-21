import numpy as np
import pandas as pd

salaryData = pd.read_excel("SalarySheet.xlsx")

#Depertman salary Avarage
salaryGroupByDepertmans = salaryData.groupby("Department")
print(salaryGroupByDepertmans.mean(numeric_only=True))


 #Title avarge Salary
print ("\n ================================================\n")
salaryGroupByTitles = salaryData.groupby("Title")
print(salaryGroupByTitles.mean(numeric_only=True))


# software developer salary average
print ("\n ================================================\n")
softwaredevelopersSalaryData = salaryData.loc[salaryData["Department"] == "Software Development"].groupby("Title")

print (softwaredevelopersSalaryData.mean(numeric_only=True))


# salary gap between software developer and marketing departments
print ("\n ================================================\n")

marketingSalaryData = salaryData.loc[salaryData["Department"] == "Marketing"].groupby("Title")

print (marketingSalaryData.mean(numeric_only=True))


#marketing and software developers count
print ("\n ================================================\n")

print(softwaredevelopersSalaryData.count())
print (marketingSalaryData.count())

print ("\n ================================================\n")




print ("\n ================================================\n")



print ("\n ================================================\n")