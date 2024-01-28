import requests
from datetime import date
from bs4 import BeautifulSoup
import csv
import pandas as pd


def scrape_website(url) -> None:
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    table = soup.find('table', {'id': 'AutoNumber3'})

    csv_filename = f'files/{date.today()}.csv'
    with open(csv_filename, 'w', newline='') as csv_file:
        csv_writer = csv.writer(csv_file)

        header_row = [header.text.strip() for header in table.find_all('th')]
        csv_writer.writerow(header_row)

        for row in table.find_all('tr')[2:]:
            data_row = [data.text.strip() for data in row.find_all('td')]
            csv_writer.writerow(data_row)

    print(f"Table has been scraped and exported to '{csv_filename}'.")


def search_power_outage(csv_filename, target_feeder_name):
    df = pd.read_csv(csv_filename)
    res = df[df['Name of Feeder'] == target_feeder_name]
    
    result_message = ''
    
    if not res.empty:
       for _, row in res.iterrows():
        result_message += f"Power Outage at'{target_feeder_name}':\n"
        result_message += f"Date Of Outage: {row['Date Of Outage']}\n"
        result_message += f"Time: {row['From (HH:MM)']} to {row['To (HH:MM)']}\n"
        result_message += f"Area Affected: {row['Area Affected']}\n"
        result_message += f"Reason: {row['Maintenance Type']}\n"
    else:
        result_message += f"No power outage information found for feeder '{target_feeder_name}'."

    return result_message



def get_power_outage():
    url = 'https://webportal.tssouthernpower.com/TSSPDCL/Information/ScheduledOutageInformation.jsp'
    scrape_website(url)
    
    csv_file = f'files/{date.today()}.csv'
    target_feeder_name = '11 KV BANDARI LAYOUT FEEDER'

    result_message = search_power_outage(csv_file, target_feeder_name)
    return result_message
