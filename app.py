#print("Hello World")

#02.2 IMPORTING
import pandas as pd
#data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data_frame)

#4 SERIES

#ages = pd.Series([23,45,7,34,6,63,36,78,54,34])
#print(ages)

#4.1 DATE RANGE

#dates = pd.date_range(start='2021-05-01', end='2021-05-12')
#print(dates)

#4.2 SERIES APPLY

#my_series = pd.Series([2, 4, 6, 8, 10])
#def divide_by_2(x):
#    return x / 2
#result_series = my_series.apply(divide_by_2)
#print(result_series)

#5 DATAFRAMES
#data = [["Toyota", "Corolla", "Blue"], ["Ford", "K", "Yellow"], ["Porche", "Cayenne", "White"]]
#df = pd.DataFrame(data,columns=['Brand','Model','Color'])
#print(df)

#5.1 DATAFRAME DICT
#car_data = [
 #   { 
     #   "brand": "Toyota", 
     #   "make": "Corolla",
     #   "color": "Blue"
    #},
    #{
     #   "brand": "Ford", 
     #   "make": "K",
     #   "color": "Yellow"
    #},
    #{
     #   "brand": "Porche", 
     #   "make": "Cayenne",
     #   "color": "White"
    #},
    #{
    #    "brand": "Tesla",
   #     "make": "Model S",
  #      "color": "Red"
 #   }
#]
#car_data = pd.DataFrame(car_data,columns=['brand','make','color'])
#print(car_data)

#5.2 DATAFRAME iLOC

#data_frame = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(data_frame.iloc[133, 6])

#5.3 FILE HEAD
#FileHead_Data = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(FileHead_Data.head(3))

#5.4 DATAFRAME TAIL
#FileTail_Data = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(FileTail_Data.tail(3))

#5.5 PRINT COLUMNS
#Column_Data = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(Column_Data[['Name', 'Type 1']][0:10])

#5.6 LOC FUNCTION
#Filtered_Data = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(Filtered_Data.loc[Filtered_Data['Attack'] > 80])

#5.7 FILTER & COUNT
#Filtered_Data = pd.read_csv('.learn/assets/pokemon_data.csv')
#print(len(Filtered_Data.loc[Filtered_Data["Legendary"]==True]))

#6 CLEAN DATASETS
#US_baby_names = pd.read_csv('.learn/assets/us_baby_names_right.csv')
#print(US_baby_names.head(5))

#6.1 REMOVE COLUMN
US_baby_names = pd.read_csv('.learn/assets/us_baby_names_right.csv')
Top_US_baby_names = US_baby_names.head(5)
Top_US_baby_names.drop('Id', axis=1, inplace=True)
print(Top_US_baby_names)
