import json # used for parsing the JSON response
import requests # used for sending a request to the api server
import sys # used for exiting the script
import time # used for parsing unix time response from the server
import pandas as pd # used for displaying the data in a tabular format

# the flag which runs the loop as long as it is True
keepFetching = True

while keepFetching:
    # asking the user to enter the country of their choice
    country = input("Enter the country for which you want the latest COVID-19 stats. Type q to quit: ")
    if country == 'q':
        keepFetching = False
        sys.exit()
    else:
    # concatenating the country to the full api address
        API_address = f"https://disease.sh/v3/covid-19/countries/{country}?strict=true"

    # we will use a 'get' request to the api server and capture the response object
    response = requests.get(API_address)
    if response.status_code != 200:
        print("Either the server is experiencing problems or your internet connection is down. Please check your internet connection and try again")
    else:
        print(f"updated {(time.time() - response.json()['updated']) // 60 % 60} minutes ago")
        data_dict = {"total cases reported " : response.json()['cases'],
                     "total number of patients recovered" : response.json()['recovered'],
                      "total number of deaths" : response.json()['deaths'], "total number of active cases remaining" : response.json()['active'], "cases reported today" : response.json()['todayCases'], "patients recovered today"  : response.json()['todayRecovered'], "deaths reported today" : response.json()['todayDeaths']}
        print(pd.DataFrame.from_dict(data_dict, orient = 'index'))



