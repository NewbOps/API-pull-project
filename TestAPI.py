 #requests module for API pull; json for creation of json file
import requests
import json

# parent function

def main():
    # pull count used to stop the loop and apend to file name

    pullcount = 0

  # user input for the amount of pulls
    global how_many
    how_many = int(input('how many pulls'))

    # web pull function

    def web_pull():
        nonlocal pullcount
        pullcount += 1

        # get request to the API
        response = requests.get(
            "http://worldtimeapi.org/api/timezone/America/New_York")
        data = response.json()

        # create json file and dump api pull in
        with open(f"test_api_pull {pullcount}.json", 'w') as file:
            json.dump(data, file, sort_keys=True, indent=4)
        print(f'pull count: {pullcount}')

    # pull count counter
    while pullcount < how_many:
        web_pull()


main()

print(f"{how_many} of files created successfully!")
