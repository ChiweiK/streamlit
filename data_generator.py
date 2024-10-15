import pandas as pd
import random
from datetime import datetime, timedelta

def generate_records(nr_records):
    records = []
    id_time = {} 

    while len(records) < nr_records:
        id1 = random.randint(1, 9999)
        id2 = random.randint(1, 9999)

        # Generate start date with random day in the year (leap years are excluded)
        # datetime.now() so every entry is somewhat close to each other. Can remove it if not needed
        start_time = datetime.now() + timedelta(days=random.randint(-600, 600))
        
        # Generate random time
        start_time += timedelta(hours=random.randint(0, 23), minutes=random.randint(0, 59))

        # Ensure end time is at least 1 minute later than start time
        end_time = start_time + timedelta(minutes=random.randint(1, 100)) 

        # Format times as YYMMDDHHMM
        start_time_str = start_time.strftime('%y%m%d%H%M')
        end_time_str = end_time.strftime('%y%m%d%H%M')

        # Check if the ID is in another call at this time
        if id1 not in id_time:
            id_time[id1] = []
        overlap = any(start <= end_time and end >= start_time for start, end in id_time[id1])
        
        if not overlap:
            records.append([id1, id2, start_time_str, end_time_str])
            id_time[id1].append((start_time, end_time))
         
        if len(records) == 1000000:
            print('1 miljoen')
        
        if len(records) == 2000000:
            print('2 miljoen')

        if len(records) == 3000000:
            print('3 miljoen')

        if len(records) == 4000000:
            print('4 miljoen')
        
        if len(records) == 5000000:
            print('5 miljoen')
        
        if len(records) == 6000000:
            print('6 miljoen')

        if len(records) == 7000000:
            print('7 miljoen')

        if len(records) == 8000000:
            print('8 miljoen')

        if len(records) == 9000000:
            print('9 miljoen')

        if len(records) == 9500000:
            print('9.5 miljoen')



    return records
    
# Generate amount of records
amount_records = 10000000
records = generate_records(amount_records)

# Save to csv
df = pd.DataFrame(records, columns=['ID1', 'ID2', 'Start Time', 'End Time'])
df.to_csv('records.csv', index=False)

# Run for amount of rows (never the amount specified with 'records'), and amount of unique ID's
df = pd.read_csv('records.csv')
print(len(df))
print(df['ID1'].nunique())