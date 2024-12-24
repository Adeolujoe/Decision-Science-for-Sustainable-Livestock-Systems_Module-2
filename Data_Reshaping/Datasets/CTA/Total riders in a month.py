''' Your goal is to find the total number of rides provided to passengers passing through the Wilson station (station_name == 'Wilson')
when riding Chicago's public transportation system on weekdays (day_type == 'Weekday') in July (month == 7).'''

import pandas as pd

ridership = pd.read_pickle('cta_ridership.p')
cal = pd.read_pickle('cta_calendar.p')
stations = pd.read_pickle('stations.p')

ridership_cal_stations = (ridership.merge(cal, on= ['year', 'month', 'day'])
                          .merge(stations, on= 'station_id'))

required = ((ridership_cal_stations['month'] == 7)
            & (ridership_cal_stations['day_type'] == 'Weekday')
            & (ridership_cal_stations['station_name'] == 'Wilson'))

print(ridership_cal_stations.loc[required, 'rides'].sum())

# You merged three DataFrames together, including merging two tables on multiple columns. Once the tables were merged, you filtered and selected just like any other DataFrame. Finally, you found out that the Wilson station had 140,005 riders during weekdays in July.