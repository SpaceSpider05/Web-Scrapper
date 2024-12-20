# Match Scraper

## Overview

This Python script scrapes match details from the website [eskooora.live](https://eskooora.live) for a given date (yesterday, today, or tomorrow). It extracts details about live and upcoming matches for various championships and saves the data to a CSV file.

## Features

- Fetch match details for a specified date.
- Parse live and upcoming matches.
- Save match information (team names, results, timings) into a structured CSV file.
- Automatically create an output directory if it doesn't exist.

## Prerequisites

Ensure you have the following installed on your system:
- Python 3.6+
- Required Python libraries:
  - `requests`
  - `beautifulsoup4`
  - `lxml`

### Installation

1. Clone or download this repository.
2. Install dependencies using pip:
   ```bash
   pip install requests beautifulsoup4 lxml
   ```

## Usage

1. Run the script:
   ```bash
   python web.py
   ```
2. Enter the desired date when prompted:
   - `yesterday`
   - `today`
   - `tomorrow`
   
3. The script will scrape match data and save it to a CSV file at the location:
   ```
   C:/Users/asus/Downloads/foot/matchesdetails.csv
   ```

## Output

The CSV file will contain the following columns:
- Championship
- Team A
- Team B
- Match Result
- Match Timing

## Notes

- Ensure the target website is accessible and the page structure hasn’t changed to avoid parsing errors.
- If no matches are found for the selected date, a message will be displayed.

## Example Output

```csv
championship,team_A,team_B,match_result,match_timing
Championship Name,Team A,Team B,1-2,15:00
Championship Name,Team C,Team D,0-0,16:30
```

## License

This project is licensed under the MIT License. See the LICENSE file for details.
© 2024 Spider. All rights reserved.