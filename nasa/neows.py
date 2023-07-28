#!/usr/bin/python3
import requests

## Define NEOW URL
NEOURL = "https://api.nasa.gov/neo/rest/v1/feed?"

# this function grabs our credentials
# it is easily recycled from our previous script
def returncreds():
    ## first I want to grab my credentials
    with open("/home/student/nasa.creds", "r") as mycreds:
        nasacreds = mycreds.read()
    ## remove any newline characters from the api_key
    nasacreds = "api_key=" + nasacreds.strip("\n")
    return nasacreds

# this is our main function
def main():
    nasacreds = returncreds()
    your_input = input("Enter a date in YYYY-MM-DD format: ") 
    your_endput = input("Enter a date in YYYY-MM-DD format: ")
    startdate ="start_date=" + your_input  # add a + between "start_date" and your_input
    endput = "end_date=" + your_endput

    neowrequest = requests.get(NEOURL + startdate + "&" + endput + "&" + nasacreds) 
    # then add + "&" + startdate to the end of this line and you're good

    neodata = neowrequest.json()

    print(neodata)

if __name__ == "__main__":
    main()

