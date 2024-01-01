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
    print('Hello! Let\'s explore some US bikeshare data!')
    # get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    print("Enter name of one of the city chicago, new york city, washington")
    city = input().lower()
    while CITY_DATA.get(city) is None:
        print("Invalid city enterd.retry!!")
        city=input().lower()

    # get user input for month (all, january, february, ... , june)
    months = ["january", "february", "march", "april", "may", "june"]
    print("Enter name of one of the month jan..june or all")
    month = input().lower()
    while month not in months and month !="all":
        print("Invalid month enterd.retry!!")
        month=input().lower()

    # get user input for day of week (all, monday, tuesday, ... sunday) 
    days =["monday", "tuesday", "wednesday", "thrusday", "friday", "saturday", "sunday"]
    print("Enter the day of week monday .. sunday or all")
    day = input().lower()
    while day not in days and day!="all":
        print("Invalid day enterd.retry!!")
        day = input().lower()

    print('-'*40)
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
    df= pd.read_csv(CITY_DATA[city])
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.day_name()
    df['hour'] = df['Start Time'].dt.hour

    if month != 'all':
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        df = df[df['month'] == month]


    if day != 'all':
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df, month , day):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # display the most common month
    if month =="all":
        print(f"Most common month is {df['month'].mode()[0]}")

    # display the most common day of week
    if day=="all":
        print(f"Most common day of week is {df['day_of_week'].mode()[0]}")

    # display the most common start hour
    print(f"Most common hour is { df['hour'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # display most commonly used start station
    print(f"Most commonly used start station is {df['Start Station'].mode()[0]}")

    # display most commonly used end station
    print(f"Most commonly used end station is {df['End Station'].mode()[0]}")

    # display most frequent combination of start station and end station trip
    df['start end station'] = df['Start Station'] + df['End Station']
    print(f"Most frequently used start and end station combination is {df['start end station'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # display total travel time taken 
    print(f" Time taken by all trips is {df['Trip Duration'].sum()}")

    # display mean travel time taken
    print(f" Mean time taken by all trips is {df['Trip Duration'].mean()}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # Display counts of user types
    print(f" User types are {df['User Type'].value_counts()}")

    # Display counts of gender
    print(f" Counts of gender are {df['Gender'].value_counts()}")

    # Display earliest, most recent, and most common year of birth
    print(f"Earliest Birth year is {df['Birth Year'].min()}")
    print(f"Most recent Birth year is {df['Birth Year'].max()}")
    print(f"Most common birth year is {df['Birth Year'].mode()[0]}")

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

def display_raw_data(df):
    """Displays the raw data"""
    restart = input('\nWould you like to see raw data? Enter yes or no.\n')
    start=0
    end=5
    while restart.lower() == 'yes':
        print(df[start:end])
        end+=5
        start+=5
        restart = input('\nWould you like to see raw data? Enter yes or no.\n')
    

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        original =df

        time_stats(df, month, day)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(original)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()
