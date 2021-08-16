import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('-'*80)
    print('-'*80)
    print('Hello! Let\'s explore some US bikeshare data!')
<<<<<<< HEAD
## My code starts here
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
||||||| 88b66f0
## My code starts here     
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
=======

    # : get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
>>>>>>> documentation
    city = input("Select one of these cities: 'chicago', 'new york city', 'washington', by entering its name:  ").lower()
    while city != 'chicago' and city != 'new york city' and city != 'washington':
        print('                  ---- input error----invalid option----please try again----')
        city = input("Select one of these cities: 'chicago', 'new york city', 'washington', by entering its name:  ").lower()
<<<<<<< HEAD

    # TO DO: get user input for month (all, january, february, ... , june)
||||||| 88b66f0
            
    # TO DO: get user input for month (all, january, february, ... , june)
=======

    # ACTION: get user input for month (all, january, february, ... , june)
>>>>>>> documentation
    month = input("Select either one month from 'january' to 'june' or enter 'all' for displaying the results for all months:  ").lower()
    while month != 'january' and month != 'february' and month != 'march' and month != 'april' and month != 'may' and month != 'june' and month != 'all':
        print('                  ---- input error----invalid option----please try again----')
        month = input("Select either one month from 'january' to 'june' or enter 'all' for displaying the results for all months:  ").lower()

    # ACTION: get user input for day of week (all, monday, tuesday, ... sunday)
    day = input("Enter either one day of week or enter 'all' for displaying the results for all days of week:  ").lower()
    while day != 'monday' and day != 'tuesday' and day != 'wednesday' and day != 'thursday' and day != 'friday' and day != 'saturday' and day != 'sunday' and day != 'all':
        print('                  ---- input error----invalid option----please try again----')
        day = input("Enter either one day of week or enter 'all' for displaying the results for all days of week:  ").lower()
    print('-'*80)
    print("DATA ANALYSIS for --- City: {} --- Month: {} --- Weekday: {} ---:".format(city.capitalize() ,month.capitalize() ,day.capitalize()))

<<<<<<< HEAD
## here ends my code
||||||| 88b66f0
## here ends my code    
=======
>>>>>>> documentation
    print('  '+'-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe

    df = pd.read_csv(CITY_DATA[city])
<<<<<<< HEAD
||||||| 88b66f0
    ## print(df.head())
    ## print(df.info()) 
=======
    ## print(df.head())
    ## print(df.info())
>>>>>>> documentation
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday_name
<<<<<<< HEAD
||||||| 88b66f0
    ### print(df.head())
    ### print(df.info()) 
=======
    ### print(df.head())
    ### print(df.info())
>>>>>>> documentation
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1

        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]
    # check data
    checkdata = input('\nWould you like to see the first 5 data rows? Enter yes or no: ')
    first_row = 0
    while checkdata.lower() == 'yes':
        print (df.iloc[first_row:(first_row+5)])
        first_row += 5
        checkdata = input('\nWould you like to see the next 5 data rows? Enter yes or no: ')
    print('  '+'-'*40)

    # adding additional columns 'start hour' and 'Trip' for later evaluation of most common start hour and station combination
    df['Start Hour'] = df['Start Time'].dt.hour
    df['Trip']='FROM ' + df['Start Station'] + ' TO ' + df['End Station']
<<<<<<< HEAD


## here ends my code
||||||| 88b66f0
   
    
## here ends my code
=======


>>>>>>> documentation
    return df


def time_stats(df, month, day):
    """Displays statistics on the most frequent times of travel."""

    print('\nI) Calculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # ACTION: display the most common month if all months selected
    if month == 'all':
        print('  most common month: %s ' % df['month'].mode()[0])
<<<<<<< HEAD

    # TO DO: display the most common day of week if all days selected
||||||| 88b66f0
    
    # TO DO: display the most common day of week if all days selected
=======

    # ACTION: display the most common day of week if all days selected
>>>>>>> documentation
    if day == 'all':
        print('  most common day of week: %s ' % df['day_of_week'].mode()[0])

    # ACTION: display the most common start hour
    print('  most common start hour: %s ' % df['Start Hour'].mode()[0])
<<<<<<< HEAD
## here ends my code
    # ACTION: display calculation time
||||||| 88b66f0
## here ends my code
=======

>>>>>>> documentation
    print("\n      <This took %s seconds>" % (time.time() - start_time))
    print('  '+'-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nII) Calculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # ACTION: display most commonly used start station
    print('  most commonly used start station: %s ' % df['Start Station'].mode()[0])
    # ACTION: display most commonly used end station
    print('  most commonly used end station: %s ' % df['End Station'].mode()[0])
    # ACTION: display most frequent combination of start station and end station trip
    print('  most frequent combination: %s ' % df['Trip'].mode()[0])
<<<<<<< HEAD
## here ends my code
    # ACTION: display calculation time
||||||| 88b66f0
## here ends my code   
=======

>>>>>>> documentation
    print("\n      <This took %s seconds>" % (time.time() - start_time))
    print('  '+'-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nIII) Calculating Trip Duration...\n')
    start_time = time.time()

    # ACTION: display total travel time
    print('  the total travel time is %s hrs' % (df['Trip Duration'].sum()/3600))
    # ACTION: display mean travel time
    print('  the mean travel time is %s min' % (df['Trip Duration'].mean()/60))
<<<<<<< HEAD
## here ends my code
    # ACTION: display calculation time
||||||| 88b66f0
## here ends my code
=======

>>>>>>> documentation
    print("\n      <This took %s seconds>" % (time.time() - start_time))
    print('  '+'-'*40)


def user_stats(df, city):
    """Displays statistics on bikeshare users."""

    print('\nIV) Calculating User Stats...\n')
    start_time = time.time()

    # ACTION: Display counts of user types
    print('\nUser Type      count')
    print(df['User Type'].value_counts())

<<<<<<< HEAD
    # TO DO: Display counts of gender
    if city != 'washington':
||||||| 88b66f0
    # TO DO: Display counts of gender
    if city != 'washington': 
=======
    # ACTION: Display counts of gender
    if city != 'washington':
>>>>>>> documentation
        print('\nGender      count')
        print(df['Gender'].value_counts())
        # ACTION: Display earliest, most recent, and most common year of birth
        print('\n  earliest year of birth: %s ' % int(df['Birth Year'].min()))
        print('  most recent year of birth: %s ' % int(df['Birth Year'].max()))
        print('  most common year of birth: %s ' % int(df['Birth Year'].mode()))
<<<<<<< HEAD
## here ends my code
    # ACTION: display calculation time
||||||| 88b66f0
## here ends my code    
=======

>>>>>>> documentation
    print("\n      <This took %s seconds>" % (time.time() - start_time))
    print('-'*80)


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
<<<<<<< HEAD

||||||| 88b66f0
       
        #checkdata = input('\nWould you like to restart? Enter yes or no.\n')
        
        
=======

        #checkdata = input('\nWould you like to restart? Enter yes or no.\n')


>>>>>>> documentation
        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
