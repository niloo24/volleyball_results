import requests
from bs4 import BeautifulSoup

url = 'https://www.fivb.com/en/results/men/worldchampionships'

response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.text, 'html.parser')
    
    results_table = soup.find('table', {'class': 'results-table'})
    
    if results_table:
        headers = [header.text.strip() for header in results_table.findAll('th')]
        
        rows = results_table.findAll('tr')[1:]  # Skip the header row.
        data = []
        for row in rows:
            data.append([cell.text.strip() for cell in row.findAll('td')])
        
        print(headers)
        for row in data:
            print(row)
    else:
        print("Results table not found.")
else:
    print(f"Request failed with status code {response.status_code}.")
