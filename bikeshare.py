import time
import pandas as pd
import numpy as np

CITY_DATA = { 'Chicago': 'chicago.csv',
              'New York City': 'new_york_city.csv',
              'Washington': 'washington.csv' }


# I messed up a bit by using the abbreviations the names for a lot of the code, but wanting to display the proper name of the month/day of week
# So here's 4 dictionaries to convert between the two.

MONTH_NAME = { 'January': 'jan', 'February': 'feb', 'March': 'mar',
               'April': 'apr', 'May': 'may', 'June': 'jun'}
# Maybe do no data months after
               #'July': 'jul', 'August': 'aug', 'September': 'sep', 
               #'October': 'oct', 'November': 'nov', 'December': 'dec'}

MONTH_SHORT = {'jan': 'January', 'feb': 'February', 'mar': 'March',
               'apr': 'April', 'may': 'May', 'jun': 'June'}
# For no data months
               #'jul': 'July', 'aug': 'August', 'sep': 'September', 
               #'oct': 'October', 'nov': 'November', 'dec': 'December'}

DAY_NAME = { 'Monday': 'mon', 'Tuesday': 'tue', 'Wednesday': 'wed',
             'Thursday': 'thu', 'Friday':'fri', 'Saturday':'sat', 'Sunday': 'sun'}

DAY_SHORT = {'mon': 'Monday', 'tue': 'Tuesday', 'wed': 'Wednesday',
             'thu': 'Thursday', 'fri': 'Friday', 'sat': 'Saturday', 'sun': 'Sunday'}


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    while True:
        # Valid input should break from loop

        city = input("Please enter a city (Chicago, New York City, or Washington):")
        if (city in CITY_DATA):
            break

        # Handle capitalization variations
        elif (city.title() in CITY_DATA):
            city = city.title()
            print(city)
            break
        
        elif(city.lower().title() in CITY_DATA):
            city = city.lower().title()
            print(city)
            break
        
        # Shorthand for me for testing
        elif (city.lower() == 'nyc'):
            city = 'New York City'
            print(city)
            break

        elif (city.lower() == 'chi'):
            city = 'Chicago'
            print(city)
            break

        elif (city.lower() == 'was'):
            city = 'Washington'
            print(city)
            break

        else:
            print("{} is not a city in our dataset, please enter a valid city:".format(city).capitalize())
            print("(Example: New York City, new york city, NYC, and nyc are all acceptable formats for New York City.)")
            
            # I don't think there'll be an exception from input, it happens later in the code, so we'll have to hardcode it to only accept the right input
            
            
    # TO DO: get user input for month (all, january, february, ... , june)
    while True:

        month = input("Please enter a month (all, jan, feb, mar, apr, may, jun):")
        if month in MONTH_SHORT:
            print(MONTH_SHORT[month])
            break
        
        # handle capitalization differences
        elif month.lower() in MONTH_SHORT:
            month = month.lower()
            print(MONTH_SHORT[month])
            break
        
        # can type out whole name of month
        elif month in MONTH_NAME:
            month = MONTH_NAME[month]
            print(MONTH_SHORT[month])
            break
        
        # any wild capitalizations of the full month name
        elif month.lower().title() in MONTH_NAME:
            print(month.lower().title())
            month = MONTH_NAME[month.lower().title()]
            break
        
        # handle capital All
        elif month == 'All':
            month = month.lower()
            print('All months')
            break
            
        elif month == 'all':
            print('All months')
            break
            
        else:
            print("{} is not a valid month in our dataset (we only have data from January to June), please input a valid month.".format(month).capitalize())
            print("(Example: Jan, January, jan, january are all valid formats for January.)")
        
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    while True:
        day = input("Please enter a day of week (all, mon, tue, wed, thu, fri, sat, sun):")
        if day in DAY_SHORT:
            print(DAY_SHORT[day])
            break
        
        
        if day.lower() in DAY_SHORT:
            print(DAY_SHORT[day])
            break
        
        # set day to the shorthand if full name is typed
        if day in DAY_NAME:
            print(day)
            day = DAY_NAME[day]
            break
        
        # Wild capitalization of day acceptable
        elif day.lower().title() in DAY_NAME:
            print(day.lower().title())
            day = DAY_NAME[day.lower().title()]
            break
        
        
        # handle capital All
        elif day == 'All':
            day = day.lower()
            print('All days')
            break
            
        elif day == 'all':
            print('All days')
            break        
        
        else:
            print("{} is not a valid day in our dataset.  Please input a valid day.".format(day).capitalize())
            print("(Example: Monday, mon, Mon, monday are all valid formats for Monday.)")
    
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
    # load data based on the city input
    df = pd.read_csv(CITY_DATA[city])    
    
    # Filter by month and day (copied from my solution to Practice 3)
        # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday


    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['jan', 'feb', 'mar', 'apr', 'may', 'jun']
        month = months.index(month)+1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != 'all':
        # filter by day of week to create the new dataframe
        days = ['mon', 'tue', 'wed', 'thu', 'fri', 'sat', 'sun']
        day = days.index(day)
        df = df[df['day_of_week'] == day]
    

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    
    df['month'] = df['Start Time'].dt.month
    popular_month = df['month'].mode()[0]
    
    # Format popular month:
    
    print('Most Frequent Starting Month:', popular_month)    
    
    
    



    # TO DO: display the most common day of week
    df['weekday'] = df['Start Time'].dt.weekday
    
    popular_day = df['weekday'].mode()[0]
    
    # Convert this to the formatted version soon
    print('Most Frequent Starting Day of Week:', popular_day)
    
    

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    
    # Format popular hour:
    
    print('Most Frequent Starting Hour:', popular_hour)    


    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start = df['Start Station'].mode()[0]

    # TO DO: display most commonly used end station
    popular_end = df['End Station'].mode()[0]

    
    # How do you find the most common string?
    
    # TO DO: display most frequent combination of start station and end station trip
    print('The most popular start station is: ' + popular_start)
    print('The most popular destination station is: ' + popular_end)

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    # I assume this means total travel time summed over all users
    
    # This is in seconds for now
    totalsec = df["Trip Duration"].sum()
    print("Total travel time: {} hours, {} minutes, {} seconds.".format(totalsec//3600, totalsec%3600//60, totalsec%3600%60//1))

    # TO DO: display mean travel time
    meansec = df["Trip Duration"].mean()
    print("Mean travel time: {} hours, {} minutes, {} seconds.".format(int(meansec//3600), int(meansec%3600//60), int(meansec%3600%60//1)))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    print(df.groupby(['User Type'])['User Type'].count())
    print()

    # TO DO: Display counts of gender
    try:
        print(df.groupby(['Gender'])['Gender'].count())
        print()
    except KeyError:
        print('No gender data in dataset for this city, skipping this output.')

    
    
    # TO DO: Display earliest, most recent, and most common year of birth
    try:
        print("The oldest user was born in {}.".format(int(df['Birth Year'].min())))
        print("The youngest user was born in {}.".format(int(df['Birth Year'].max())))
        print("The most common birth year is {}.".format(int(df['Birth Year'].mode()[0])))
    except KeyError:
        print('No birth year data in dataset for this city, skipping this output.')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    
def display_data(df):
    index = 0
    endpoint = len(df)
    while True:
        display = input("Display 5 lines of data?")
        if display in ['y', 'yes', 'True', 'true']:
            # handle end of dataframe
            if index+5 >= endpoint:
                print(df.iloc[index:index+5])
                print()
                break
            # otherwise, print 5 lines and increment
            else:
                print(df.iloc[index:index+5])
                print()
                index += 5
        else:
            break
    return

def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)
        display_data(df)
        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            #print(df.head(10))
            break


if __name__ == "__main__":
	main()
