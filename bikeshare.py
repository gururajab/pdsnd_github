import time
import pandas as pd
import numpy as np

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def get_filters():
    
    print('Hello! Let\'s explore US bikeshare data!\n')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    
    city= input('Which city you want to explore chicago, new york city, or washington?\n')
    city=city.strip().lower()
    while city!= 'new york city' and city != 'chicago' and city != 'washington':
        print('Oops! this is unavilable city\n')
        city=input('Please try again\n')
        city=city.strip().lower()

    # TO DO: get user input for month (all, january, february, ... , june)
    month= input('Do you want to explore specific month from jan to june or all? enter january, february\n')
    month= month.strip().lower()

    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    day= input('Do you want to explore about specific day of the week or all if yes enter the weekday as monday, sunday,...\n')
    day=day.strip().lower()


    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    
    
    filename=CITY_DATA[city]
    df = pd.read_csv(filename)
    
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['Hour'] = pd.to_datetime(df['Start Time']).dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]

    if day != 'all':
        df = df[df['day_of_week'] == day.title()]


    return df


def time_stats(df):

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    print('The most common month: ', df['month'].mode()[0])
    
    # TO DO: display the most common day of week
    print('The most common day of the week: ', df['day_of_week'].mode()[0])

    # TO DO: display the most common start hour
    print('The most common start hour: ', df['Hour'].mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    print('The most common start station: ', df['Start Station'].mode()[0])


    # TO DO: display most commonly used end station
    print('The most common end station: ', df['End Station'].mode()[0])


    # TO DO: display most frequent combination of start station and end station trip
    print('The most common trip if form-to distinations: ', (df['Start Station']+df['End Station']).mode()[0])


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    print('Total travel time = ', df['Trip Duration'].sum())

    # TO DO: display mean travel time
    print('Average travel time = ', df['Trip Duration'].mean())


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df, city):

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df['User Type'].value_counts())


    # TO DO: Display counts of gender
    if city != 'washington':
        print(df['Gender'].value_counts())


    # TO DO: Display earliest, most recent, and most common year of birth
    if city != 'washington':
        print('The earliest year of birth ', df['Birth Year'].min())
        print('The most recent year of birth ', df['Birth Year'].max())
        print('The most common year of birth ', df['Birth Year'].mode()[0])

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_data(city):
    view_display= input("To view 5 rows of individual trip data? Enter yes or no?")
    view_display = view_display.lower().strip()
    
    filename=CITY_DATA[city]
    df = pd.read_csv(filename)
    
    start_loc=5
    while(view_display == "yes"):
         print(df.iloc[:start_loc])
         start_loc += 5
         view_display = input("Do you wish to continue?: ").lower().strip()

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df, city)
        display_data(city)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()