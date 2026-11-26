import pandas as pd
import numpy as np

data = {
    "Employee_ID": [101,102,103,104,105,105,106,107,108,109],
    "Name": ["Arun","Priya","Rahul","Divya","Kumar","Kumar","Anu","Ravi","Meena","John"],
    "Department": ["IT","HR","Sales","IT","HR","HR","Sales","IT","Finance","Finance"],
    "Age": [25,30,28,np.nan,35,35,27,40,32,29],
    "Salary": [25000,30000,28000,40000,np.nan,np.nan,32000,50000,45000,35000],
    "Gender": ["Male","Female","Male","Female","Male","Male","Female","Male","Female","Male"],
    "City": ["Chennai","Mumbai","Chennai","Delhi","Mumbai","Mumbai","Chennai","Delhi","Chennai","Mumbai"],
    "Joining_Date": ["2022-01-10","2021-05-15","2023-02-20","2020-08-12","2022-11-01","2022-11-01","2023-06-10","2019-03-15","2021-09-20","2022-04-05"]
}

df = pd.DataFrame(data)

df.to_csv("employee_data.csv", index=False)

print(df)