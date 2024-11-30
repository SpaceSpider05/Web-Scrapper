import os
import requests
from bs4 import BeautifulSoup
import csv

date_url = input("Enter the date (yesterday, today, tomorrow): ")
pageUrl = requests.get(f"https://eskooora.live-koora.live/matches-{date_url}/")
pageUrl.encoding = 'utf-8'



def main(pageUrl):
    source = pageUrl.content
    soup = BeautifulSoup(source, "lxml")  # parsing to html
    matches_details = []
    div_name = 'tab-pane section'
    championship = soup.find_all("div", {'class': div_name})

    def get_info_match(championship):
        championship_title = championship.find("h2").text.strip()
        CommingMatches = championship.contents[3].find_all("div", {'class': 'match-container soon'})
        liveMatches = championship.contents[3].find_all("div", {'class': 'match-container live'})

        print(f"the matche link {pageUrl}")
        print(f"\nChampionship: {championship_title}")
        print(f"Number of Coming Matches: {len(CommingMatches)}")
        print(f"Number of Live Matches: {len(liveMatches)}")

        for match in liveMatches:
            team_A = match.find("div", {'class': 'right-team'}).text.strip()
            team_B = match.find("div", {'class': 'left-team'}).text.strip()
            match_result = match.find("div", {'class': 'result'}).text.strip()
            match_timing = match.find("div", {'id': 'match-time'}).text.strip()

            match_info = {
                "championship": championship_title,
                "team_A": team_A,
                "team_B": team_B,
                "match_result": match_result,
                "match_timing": match_timing
            }
            matches_details.append(match_info)

            # Print structured details
            print(f"  Match: {team_A} vs {team_B}")
            print(f"    Result: {match_result}")
            print(f"    Timing: {match_timing}\n")

    for champ in championship:
        get_info_match(champ)

    if matches_details:
        # Ensure the directory exists
        output_dir = 'C:/Users/asus/Downloads/foot'
        os.makedirs(output_dir, exist_ok=True)

        output_file = os.path.join(output_dir, 'matchesdetails.csv')
        keys = matches_details[0].keys()
        with open(output_file, 'w', newline='', encoding='utf-8-sig') as file:
            dict_writer = csv.DictWriter(file, keys)
            dict_writer.writeheader()
            dict_writer.writerows(matches_details)

        print(f"\nThe file has been created successfully at: {output_file}")
    else:
        print("No matches found for the selected date.")


main(pageUrl)
