# Created by : Tochukwu Iroakazi
# Created on : Nov 2017
# Created for : ICS3UR
# Daily Assignment - Unit5-01
# This program accepts any array and finds the largest value 

def get_largest_value(array = []):
    
    array_number = max(array)
    return array_number
    
arrays = [2,5,4,3,7,8]
large_number = get_largest_value(arrays)
print('The largest number is: ' + str(large_number))
