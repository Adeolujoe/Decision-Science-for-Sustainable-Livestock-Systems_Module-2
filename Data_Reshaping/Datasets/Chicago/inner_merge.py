import pandas as pd

taxi_veh = pd.read_pickle('taxi_vehicles.p')
taxi_owners = pd.read_pickle('taxi_owners.p')
print(taxi_owners.shape)
print(taxi_veh.shape)

print(taxi_veh['fuel_type'].value_counts())

taxi_own_veh = taxi_owners.merge(taxi_veh, on= 'vid', suffixes= ('_own', '_veh'))
print(taxi_own_veh)

