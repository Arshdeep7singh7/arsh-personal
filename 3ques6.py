import pandas as pd
data={'employeeId':[101,102,103,104,105],
      'name':['alice','bob','charlie','diana','edward'],
      'department':['HR','IT','IT','marketing','sales'],
      'age':[29,34,41,28,38],
      'salary':[50000,70000,65000,55000,6000,],
      'yearsOfExperience':[4,8,10,3,12],
      'joiningDate':['2020-03015','2017-07-19','2013-06-01','2021-02-10','2010-11-25'],
      'gender':['female','male','male','female','male'],
      'bonus':[5000,7000,6000,4500,5000],
      'rating':[4.5,4.0,3.8,4.7,3.5]
      }
df=pd.DataFrame(data)
# #part1
# print(f'no. of rows are {df.shape[0]}')
# print(f'no. of columns are {df.shape[1]}')
# #part2
# df.info()
# #part3
# print(df.describe())
#part4
# print(df.head())
# print(df.tail(3))
#part5
# average_salary = df['salary'].mean()
# total_bonus = df['bonus'].sum()
# youngest_age = df['age'].min()
# highest_rating = df['rating'].max()

# Display the results
# print(f"Average salary: {average_salary}")
# print(f"Total bonus paid: {total_bonus}")
# print(f"Youngest employee's age: {youngest_age}")
# print(f"Highest performance rating: {highest_rating}")
#part 6
# df_sorted = df.sort_values(by='salary', ascending=False)
# print(df_sorted)
#part 7
# def categorize_performance(rating):
#     if rating >= 4.5:
#         return 'Excellent'
#     elif rating >= 4.0:
#         return 'Good'
#     else:
#         return 'Average'
# df['Performance Category'] = df['rating'].apply(categorize_performance)
# print(df['Performance Category'])
#part 8
# missing_values=df.isnull()
# print(missing_values)
# missing_count=df.isnull().sum()
# print(missing_count)
#part 9
# df = df.rename(columns={'employeeId': 'ID'})
# print(df)
#part 10
# experienced_employees = df[df['yearsOfExperience'] > 5]
# it_employees = df[df['department'] == 'IT']
# print("Employees with more than 5 years of experience:")
# print(experienced_employees)
# print("\nEmployees in the IT department:")
# print(it_employees)
#part 11
# df['Tax'] = df['salary'] * 0.10
# print(df)
#part 12
df.to_csv('modified_employee_data.csv', index=False)
print("The modified DataFrame has been saved to 'modified_employee_data.csv'.")