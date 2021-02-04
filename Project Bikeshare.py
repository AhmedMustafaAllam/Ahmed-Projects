"""
@author: Ahmed Mustafa, e-mail: ahmed.mustafa.hassan@gmail.com
"""
import pandas as pd
import time
########################################################################################
# List of cities, months and days availble in List format and dictionary format
CITY= {'Chicago':'chicago.csv','New York':'new_york_city.csv','Washington':'washington.csv'}
MONTHS = ['All','January','February','March','April','May','June']
DAYS = ['All','Sunday','Monday','Tuesday','Wednesday','Thursday','Friday','Saturday']
########################################################################################
#Checking functions to match the input to the above list elements 
def check_city(city):
    for i in CITY:
        if city.title() == i:
            chk = True
            break
        else:
            chk = False
    return chk
def check_month(month):
    for i in MONTHS:
        if month.title() == i:
            chk =  True
            break
        else:
            chk = False
    return chk
def check_day(day):
    for i in DAYS:
        if day.title() == i:
            chk =  True
            break
        else:
            chk = False
    return chk
########################################################################################
########################################################################################
# asking for the needed city 
city=input('Hello! Welcome to Bikeshare USA Project \n Please Enter the City you want (Chicago - New York - Washington)\n')

# to check if the city entered is right or wrong
chk_city = check_city(city)  
if chk_city == False:
    print('Sorry you entered a wrong city , please check the city name and mind spaces and restart the program')
else:
    # ask about the month
    month_user = input('Please select the needed month (All - January - February - March - April - May - June):\n ')
    # check if the month entered is right or wrong
    chk_month= check_month(month_user)
    
    if chk_month == False:
        print('Sorry you entered a wrong month , please enter month from Jan to June and mind spaces and restart the program')
    else:
        # as about the day
        day_user = input(' Please select the day needed (All - Sunday - Monday - Tuesday - Wednesday - Thursday - Friday - Saturday):\n')
        # checking if the day entered is right or wrong
        chk_day = check_day(day_user)
        
        if chk_day == False:
            print('Sorry you entered a wrong day , please mind spaces and restart the program')
        else:
        
            print('\n \n Please Hold while Statistics are being prepared ... \n \n')
            
            t1 = time.time() # to start the time calculation for each operation
            
            #ready the CSV according to the file naming in the dictionary
            df = pd.read_csv(CITY[city.title()])
        
            #############################################################################
            # Adjusting the column and it's addition inside the functions
            #############################################################################
            
            df['Start Time'] = pd.to_datetime(df['Start Time']) # Start Time is converted into time Format
            
            df['End Time'] = pd.to_datetime(df['End Time']) # End Time is converted into Time Format
            
            df['Start Month'] = df['Start Time'].dt.month_name() # creating column with Month names
            
            df['Start Day'] = df['Start Time'].dt.day_name() #creating column with Day names
            
            df['Start Hour'] = df['Start Time'].dt.hour # creating column in start Hours
            
            df['End Month'] = df['End Time'].dt.month_name() # creating column with Month names
            
            df['End Day'] = df['End Time'].dt.day_name() #creating column with Day names
            
            df['End Hour'] = df['End Time'].dt.hour # creating column in end Hours
            
            df['Trip'] ='( \'' + df['Start Station']+' , \''+df['End Station'] + '\' )'
            ################################################################
            # Getting the Hour 
            def getting_pop_hour(month,day):
                
                if month.title() == 'All':
                   
                    if day.title() == 'All': ## Tested ##
                        popular_hour = df['Start Hour'].mode()[0]
                        count_pop_hour = df['Start Hour'].count()
                        t2 = time.time()
                        filt = 'No Filter'
                   
                    elif day.title() != 'All': ## Tested ##
                        df_filtered = df[df['Start Day'] == day.title()]
                        popular_hour = df_filtered['Start Hour'].mode()[0] # get the peak hour 
                        df_filtered_2 = df_filtered[df_filtered['Start Hour'] == popular_hour] #filter on Peak hour
                        count_pop_hour = df_filtered_2['Start Hour'].count() # get the count of the peak hour
                        t2 = time.time()
                        filt ='Filter Day on all months'
                
                elif month.title() != 'All': 
                    
                    if day.title() == 'All':
                        df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                        popular_hour = df_filtered['Start Hour'].mode()[0] # get the peak hour 
                        df_filtered_2 = df_filtered[df_filtered['Start Hour'] == popular_hour] #filter on Peak hour
                        count_pop_hour = df_filtered_2['Start Hour'].count() # get the count of the peak hour
                        t2 = time.time()
                        filt = 'Filter Month and all Days'
                    
                    elif day.title() != 'All':
                        df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                        df_filtered_2 = df_filtered[df_filtered['Start Day'] == day.title()] # filtering on the day
                        popular_hour = df_filtered_2['Start Hour'].mode()[0] # get the peak hour 
                        df_filtered_3 = df_filtered_2[df_filtered_2['Start Hour'] == popular_hour] #filter on Peak hour
                        count_pop_hour = df_filtered_3['Start Hour'].count() # get the count of the peak hour
                        t2 = time.time()
                        filt = 'Both'
                
                return popular_hour , count_pop_hour , t2 , filt
            
            #################################################################
            # Getting durations
            
            def getting_durations (month,day):
                
                if month.title() == 'All' and day.title() == 'All':
                    tdelta = df['End Time'] - df['Start Time'] # creating the difference / duration
                    tdelta_sec_sum = tdelta.dt.seconds.sum()
                    tdelta_sec_count = tdelta.count()
                    tdelta_sec_avg = tdelta.dt.seconds.mean()
                    filt = 'No Filter'
                    t2 = time.time()
                elif month.title() =='All' and day.title() !='All':
                    df_filtered = df[df['Start Day'] == day.title()]
                    tdelta = df_filtered['End Time'] - df_filtered['Start Time'] # creating the difference / duration
                    tdelta_sec_sum = tdelta.dt.seconds.sum()
                    tdelta_sec_count = tdelta.count()
                    tdelta_sec_avg = tdelta.dt.seconds.mean()
                    filt = 'Filter Day on all months'
                    t2 = time.time()
                elif month.title() !='All' and day.title() =='All':
                    df_filtered = df[df['Start Month'] == month.title()]
                    tdelta = df_filtered['End Time'] - df_filtered['Start Time'] # creating the difference / duration
                    tdelta_sec_sum = tdelta.dt.seconds.sum()
                    tdelta_sec_count = tdelta.count()
                    tdelta_sec_avg = tdelta.dt.seconds.mean()
                    filt = 'Filter Month and all Days'
                    t2 = time.time()
                elif month.title() !='All' and day.title() !='All':
                    df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                    df_filtered_2 = df_filtered[df_filtered['Start Day'] == day.title()] # filtering on the day
                    tdelta = df_filtered_2['End Time'] - df_filtered_2['Start Time'] # creating the difference / duration
                    tdelta_sec_sum = tdelta.dt.seconds.sum()
                    tdelta_sec_count = tdelta.count()
                    tdelta_sec_avg = tdelta.dt.seconds.mean()
                    filt = 'Both'
                    t2 = time.time()
                return tdelta_sec_sum , tdelta_sec_count , tdelta_sec_avg , filt , t2
            
            ##################################################################
            # get popular station
            def getting_pop_station (month,day):
                if month.title() == 'All' and day.title() == 'All':
                    
                    df_values_start=df['Start Station'].value_counts() # getting the list of count/Station
                    count_start = df_values_start.max() #getting the station max count
                    station_name_start =df_values_start.index[0] #getting the station name
                    
                    df_values_end=df['End Station'].value_counts() # getting the list of count/Station
                    count_end = df_values_end.max() #getting the station max count
                    station_name_end =df_values_end.index[0] #getting the station name
                    
                    filt = 'No Filter'
                    t2 = time.time()
                
                elif month.title() =='All' and day.title() !='All':
                    df_filtered = df[df['Start Day'] == day.title()]
                    
                    df_values_start=df_filtered['Start Station'].value_counts() # getting the list of count/Station
                    count_start = df_values_start.max() #getting the station max count
                    station_name_start =df_values_start.index[0] #getting the station name
                    
                    df_values_end=df_filtered['End Station'].value_counts() # getting the list of count/Station
                    count_end = df_values_end.max() #getting the station max count
                    station_name_end =df_values_end.index[0] #getting the station name
                    
                    filt = 'Filter Day on all months'
                    t2 = time.time()
                    
                elif month.title() !='All' and day.title() =='All':
                    df_filtered = df[df['Start Month'] == month.title()]
                    
                    df_values_start=df_filtered['Start Station'].value_counts() # getting the list of count/Station
                    count_start = df_values_start.max() #getting the station max count
                    station_name_start =df_values_start.index[0] #getting the station name
                    
                    df_values_end=df_filtered['End Station'].value_counts() # getting the list of count/Station
                    count_end = df_values_end.max() #getting the station max count
                    station_name_end =df_values_end.index[0] #getting the station name
                    
                    filt = 'Filter Month and all Days'
                    t2 = time.time()
                    
                elif month.title() !='All' and day.title() !='All':
                    df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                    df_filtered_2 = df_filtered[df_filtered['Start Day'] == day.title()] # filtering on the day
                    
                    df_values_start=df_filtered_2['Start Station'].value_counts() # getting the list of count/Station
                    count_start = df_values_start.max() #getting the station max count
                    station_name_start =df_values_start.index[0] #getting the station name
                    
                    df_values_end=df_filtered_2['End Station'].value_counts() # getting the list of count/Station
                    count_end = df_values_end.max() #getting the station max count
                    station_name_end =df_values_end.index[0] #getting the station name
                    
                    filt = 'Both'
                    t2 = time.time()
            
                return station_name_start,count_start,station_name_end,count_end,filt,t2
            #################################################################
            # get Popular Trip 
            def getting_pop_trip(month,day):
                if month.title() == 'All' and day.title() == 'All':
                    
                    df_values_trip=df['Trip'].value_counts() # getting the list of count/trip
                    count_trip = df_values_trip.max() #getting the trip max count
                    station_name_trip =df_values_trip.index[0] #getting the trip name
                    
                    filt = 'No Filter'
                    t2 = time.time()
                
                elif month.title() =='All' and day.title() !='All':
                    df_filtered = df[df['Start Day'] == day.title()]
                    
                    df_values_trip=df_filtered['Trip'].value_counts() # getting the list of count/trip
                    count_trip = df_values_trip.max() #getting the trip max count
                    station_name_trip =df_values_trip.index[0] #getting the trip name
                    
                    filt = 'Filter Day on all months'
                    t2 = time.time()
                    
                elif month.title() !='All' and day.title() =='All':
                    df_filtered = df[df['Start Month'] == month.title()]
                    
                    df_values_trip=df_filtered['Trip'].value_counts() # getting the list of count/trip
                    count_trip = df_values_trip.max() #getting the trip max count
                    station_name_trip =df_values_trip.index[0] #getting the trip name
                    
                    filt = 'Filter Month and all Days'
                    t2 = time.time()
                    
                elif month.title() !='All' and day.title() !='All':
                    df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                    df_filtered_2 = df_filtered[df_filtered['Start Day'] == day.title()] # filtering on the day
                    
                    df_values_trip=df_filtered_2['Trip'].value_counts() # getting the list of count/trip
                    count_trip = df_values_trip.max() #getting the trip max count
                    station_name_trip =df_values_trip.index[0] #getting the trip name
                    
                    filt = 'Both'
                    t2 = time.time()
            
                return station_name_trip,count_trip,filt,t2
            ##################################################################
            # get the user types
            def getting_user_type(month,day):
                if month.title() == 'All' and day.title() == 'All':
                    
                    df_user_type=df['User Type'].value_counts() # getting the list of count per user type
                    index_length = len(df_user_type.index) #getting the length of the index es 
                    
                    for i in range(0,index_length):
                        user_type = df_user_type.index[i]
                        User_count = df_user_type[i]
                        print('{} = {}'.format(user_type,User_count))
                    
                    filt = 'No Filter'
                    t2 = time.time()
                
                elif month.title() =='All' and day.title() !='All':
                    df_filtered = df[df['Start Day'] == day.title()]
                    
                    df_user_type=df_filtered['User Type'].value_counts() # getting the list of count per user type
                    index_length = len(df_user_type.index) #getting the length of the index es 
                    
                    for i in range(0,index_length):
                        user_type = df_user_type.index[i]
                        User_count = df_user_type[i]
                        print('{} = {}'.format(user_type,User_count))
                    
                    filt = 'Filter Day on all months'
                    t2 = time.time()
                    
                elif month.title() !='All' and day.title() =='All':
                    df_filtered = df[df['Start Month'] == month.title()]
                    
                    df_user_type=df_filtered['User Type'].value_counts() # getting the list of count per user type
                    index_length = len(df_user_type.index) #getting the length of the index es 
                    
                    for i in range(0,index_length):
                        user_type = df_user_type.index[i]
                        User_count = df_user_type[i]
                        print('{} = {}'.format(user_type,User_count))
                    
                    filt = 'Filter Month and all Days'
                    t2 = time.time()
                    
                elif month.title() !='All' and day.title() !='All':
                    df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                    df_filtered_2 = df_filtered[df_filtered['Start Day'] == day.title()] # filtering on the day
                    
                    df_user_type=df_filtered_2['User Type'].value_counts() # getting the list of count per user type
                    index_length = len(df_user_type.index) #getting the length of the index es 
                    
                    for i in range(0,index_length):
                        user_type = df_user_type.index[i]
                        User_count = df_user_type[i]
                        print('{} = {}'.format(user_type,User_count))
                    
                    filt = 'Both'
                    t2 = time.time()
            
                return filt,t2
            ##################################################################
            #get the gender of the users
            def getting_gender(month,day,city):
                if city.title() == 'Washington':
                    print('Sorry, there is no gender data for {}'.format(city))
                    filt = '--'
                    t2 = time.time()
                else:
                    if month.title() == 'All' and day.title() == 'All':
                    
                        df_user_type=df['Gender'].value_counts() # getting the list of count per user type
                        index_length = len(df_user_type.index) #getting the length of the index es 
                    
                        for i in range(0,index_length):
                            user_type = df_user_type.index[i]
                            User_count = df_user_type[i]
                            print('{} = {}'.format(user_type,User_count))
                    
                        filt = 'No Filter'
                        t2 = time.time()
                
                    elif month.title() =='All' and day.title() !='All':
                        df_filtered = df[df['Start Day'] == day.title()]
                        
                        df_user_type=df_filtered['Gender'].value_counts() # getting the list of count per user type
                        index_length = len(df_user_type.index) #getting the length of the index es 
                        
                        for i in range(0,index_length):
                            user_type = df_user_type.index[i]
                            User_count = df_user_type[i]
                            print('{} = {}'.format(user_type,User_count))
                        
                        filt = 'Filter Day on all months'
                        t2 = time.time()
                        
                    elif month.title() !='All' and day.title() =='All':
                        df_filtered = df[df['Start Month'] == month.title()]
                        
                        df_user_type=df_filtered['Gender'].value_counts() # getting the list of count per user type
                        index_length = len(df_user_type.index) #getting the length of the index es 
                        
                        for i in range(0,index_length):
                            user_type = df_user_type.index[i]
                            User_count = df_user_type[i]
                            print('{} = {}'.format(user_type,User_count))
                        
                        filt = 'Filter Month and all Days'
                        t2 = time.time()
                        
                    elif month.title() !='All' and day.title() !='All':
                        df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                        df_filtered_2 = df_filtered[df_filtered['Start Day'] == day.title()] # filtering on the day
                        
                        df_user_type=df_filtered_2['Gender'].value_counts() # getting the list of count per user type
                        index_length = len(df_user_type.index) #getting the length of the index es 
                        
                        for i in range(0,index_length):
                            user_type = df_user_type.index[i]
                            User_count = df_user_type[i]
                            print('{} = {}'.format(user_type,User_count))
                        
                        filt = 'Both'
                        t2 = time.time()
                return filt,t2 
            ##################################################################
            #get the birth details of the users
            def getting_birth(month,day,city):
                if city.title() == 'Washington':
                    print('Sorry, there is no birth data for {}'.format(city))
                    early_birth = 0
                    recent_birth = 0
                    common_birth = 0
                    filt = '--'
                    t2 = time.time()
                else:
                    if month.title() == 'All' and day.title() == 'All':
                    
                        early_birth = df['Birth Year'].min()
                        recent_birth = df['Birth Year'].max()
                        common_birth = df['Birth Year'].mode()
                
                        filt = 'No Filter'
                        t2 = time.time()
                
                    elif month.title() =='All' and day.title() !='All':
                        df_filtered = df[df['Start Day'] == day.title()]
                        
                        early_birth = df_filtered['Birth Year'].min()
                        recent_birth = df_filtered['Birth Year'].max()
                        common_birth = df_filtered['Birth Year'].mode()
                        
                        filt = 'Filter Day on all months'
                        t2 = time.time()
                        
                    elif month.title() !='All' and day.title() =='All':
                        df_filtered = df[df['Start Month'] == month.title()]
                        
                        early_birth = df_filtered['Birth Year'].min()
                        recent_birth = df_filtered['Birth Year'].max()
                        common_birth = df_filtered['Birth Year'].mode()
                        
                        filt = 'Filter Month and all Days'
                        t2 = time.time()
                        
                    elif month.title() !='All' and day.title() !='All':
                        df_filtered = df[df['Start Month'] == month.title()] #Filtering on the month
                        df_filtered_2 = df_filtered[df_filtered['Start Day'] == day.title()] # filtering on the day
                        
                        early_birth = df_filtered_2['Birth Year'].min()
                        recent_birth = df_filtered_2['Birth Year'].max()
                        common_birth = df_filtered_2['Birth Year'].mode()
                        
                        filt = 'Both'
                        t2 = time.time()
                
                return early_birth,recent_birth,common_birth,filt,t2
            ####################################################################
            
            #########################
            #General City Statistics
            #########################
            common_month_start = df['Start Month'].value_counts().index[0]
            common_day_start = df['Start Day'].value_counts().index[0]
            print('##########################################')
            print('Starting with General Statistics for the {} City\n##########################################\nCommon Month is {}\nCommon Day is {} \nPreparing Hour details ....\n'.format(city.title(),common_month_start,common_day_start))
            ######################################################
            # Displaying the Function output in the desired form
            
            pop_h,pop_count,pop_t,pop_filt = getting_pop_hour(month_user,day_user)
            print('Most Popular hour = {}\nCount = {}\nFilter: {} \nThat took = {} sec \n\n\n Calculating the next statistic .... Trip Duration \n'.format(pop_h,pop_count,pop_filt,pop_t-t1))
            
            dur_sum,dur_count,sur_avg,dur_filt,dur_time = getting_durations(month_user,day_user)
            
            print('Total Duration: {} seconds\nCount: {}\nAvg Duration: {}\nFilter: {} \n That tool {} seconds \n\n Calculating the next statistic ... popular_Station\n\n'.format(dur_sum,dur_count,sur_avg,dur_filt,dur_time-t1))
            
            st_start_name,st_start_count,st_end_name,st_end_count,st_filt,st_time = getting_pop_station(month_user,day_user)
            
            print('Start Station : {}\nCount: {} \nEnd Station: {}\nCount: {} \nFilter: {} \nThat Took {} Seconds \n\n Calculating the next statistic ... popular_Trip \n\n'.format(st_start_name,st_start_count,st_end_name,st_end_count,st_filt,st_time-t1))
            
            trip_name,trip_count,trip_filt,trip_time = getting_pop_trip(month_user,day_user)
            
            print('Trip: {}\nCount: {}\nFilter: {} \nThat took {} seconds \n\n Calculating the next statistic .... user type \n'.format(trip_name,trip_count,trip_filt,trip_time-t1))
            
            user_filt,user_time = getting_user_type(month_user,day_user)
            
            print('Filter : {} \nThat took {} seconds \ncalculating the next statistics ... Gender\n'.format(user_filt,user_time-t1))
            
            gender_filt,gender_time = getting_gender(month_user,day_user,city)
            
            print('Filter : {} \nThat took {} seconds \ncalculating the next statistics ... Birth Years\n'.format(gender_filt,gender_time-t1))
            
            birth_early,birth_recent,birth_common,birth_filt,birth_time = getting_birth(month_user,day_user,city)
            
            print('Earliest Birth Year : {}\nRecent Birth Year : {}\nCommon Birth Year : {}\nFilter {} \nThat took {} seconds\nThanks a lot for using Bikeshare'.format(int(birth_early),int(birth_recent),int(birth_common),birth_filt,birth_time-t1))
