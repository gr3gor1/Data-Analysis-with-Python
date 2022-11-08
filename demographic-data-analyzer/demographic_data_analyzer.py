import pandas as pd
import numpy as np

def calculate_demographic_data(print_data=True):
    # Read data from file
    df = pd.read_csv('adult.data.csv')

    # How many of each race are represented in this dataset? This should be a Pandas series with race names as the index labels.
    #races = df['race'].unique()
    races = df['race'].value_counts()
    race_count = races.squeeze()

    # What is the average age of men?
    df2 = df.loc[df['sex']=='Male']
    average_age_men = df2['age'].mean()
    average_age_men = int(average_age_men*10)/10

    # What is the percentage of people who have a Bachelor's degree?
    count_row = df.shape[0]
    bachelor = df['education'].value_counts().Bachelors
    percentage_bachelors = (bachelor/count_row)*100
    percentage_bachelors = int(percentage_bachelors*10)/10

    # What percentage of people with advanced education (`Bachelors`, `Masters`, or `Doctorate`) make more than 50K?
    # What percentage of people without advanced education make more than 50K?

    # with and without `Bachelors`, `Masters`, or `Doctorate`
    higher_education = df.loc[(df['education']=='Bachelors')|(df['education']=='Masters') | (df['education']=='Doctorate')]
    lower_education = df.loc[(df['education']!='Bachelors') & (df['education']!='Masters') & (df['education']!='Doctorate')]

    # percentage with salary >50K
    df3 = higher_education.loc[higher_education['salary']=='>50K']
    df4 = lower_education.loc[lower_education['salary']=='>50K']
    higher_education_rich =(df3.shape[0]/higher_education.shape[0])*100
    higher_education_rich = int(higher_education_rich*10)/10
    lower_education_rich = (df4.shape[0]/lower_education.shape[0])*100
    lower_education_rich = round(lower_education_rich,1)

    # What is the minimum number of hours a person works per week (hours-per-week feature)?
    min_work_hours = df['hours-per-week'].min()

    # What percentage of the people who work the minimum number of hours per week have a salary of >50K?
    df6 = df.loc[df['hours-per-week']==1]
    df5 = df.loc[(df['hours-per-week']==1) & (df['salary']=='>50K')]
    num_min_workers = ((df5.shape[0])/df6.shape[0])*100

    rich_percentage = num_min_workers

    # What country has the highest percentage of people that earn >50K?
    
    df8 = df.groupby('native-country').count()
    df8 = pd.DataFrame(df8)

    df7 = df.loc[df['salary']=='>50K']
    df7 = df7.groupby('native-country')['salary'].count()
    df7 = pd.DataFrame(df7)
  
    df9 = pd.DataFrame(df7['salary']/df8['salary'])
    max = df9['salary'].max()
    
    index = np.where(df9['salary']==max)
    index = df9.index[index][0]
    
    highest_earning_country = index
    highest_earning_country_percentage = round(max*100,1)

    # Identify the most popular occupation for those who earn >50K in India.
    df10 = df.loc[(df['native-country']=="India") & (df['salary']=='>50K')]
    df10 = pd.DataFrame(df10.groupby('occupation')['occupation'].count())
    max1 = df10['occupation'].max()

    index1 = np.where(df10['occupation']==max1)
  
    top_IN_occupation = df10.index[index1][0]

    # DO NOT MODIFY BELOW THIS LINE

    if print_data:
        print("Number of each race:\n", race_count) 
        print("Average age of men:", average_age_men)
        print(f"Percentage with Bachelors degrees: {percentage_bachelors}%")
        print(f"Percentage with higher education that earn >50K: {higher_education_rich}%")
        print(f"Percentage without higher education that earn >50K: {lower_education_rich}%")
        print(f"Min work time: {min_work_hours} hours/week")
        print(f"Percentage of rich among those who work fewest hours: {rich_percentage}%")
        print("Country with highest percentage of rich:\n", highest_earning_country)
        print(f"Highest percentage of rich people in country: {highest_earning_country_percentage}%")
        print("Top occupations in India:", top_IN_occupation)

    return {
        'race_count': race_count,
        'average_age_men': average_age_men,
        'percentage_bachelors': percentage_bachelors,
        'higher_education_rich': higher_education_rich,
        'lower_education_rich': lower_education_rich,
        'min_work_hours': min_work_hours,
        'rich_percentage': rich_percentage,
        'highest_earning_country': highest_earning_country,
        'highest_earning_country_percentage':
        highest_earning_country_percentage,
        'top_IN_occupation': top_IN_occupation
    }
