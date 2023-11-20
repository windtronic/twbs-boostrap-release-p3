import requests
import csv

# GitHub API endpoint to fetch releases for the Bootstrap repository
api_url = 'https://api.github.com/repos/twbs/bootstrap/releases'

# Function to fetch releases from GitHub API
def fetch_releases():
    response = requests.get(api_url)
    return response.json()

# Function to write releases to a CSV file
def write_releases_to_csv(releases):
    with open('bootstrap_releases.csv', 'w', newline='') as csvfile:
        fieldnames = ['Created Date', 'Tag name', 'URL for the distribution zip file']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for release in releases:
            writer.writerow({
                'Created Date': release['created_at'],
                'Tag name': release['tag_name'],
                'URL for the distribution zip file': release['zipball_url']
            })

if __name__ == '__main__':
    releases_data = fetch_releases()
    write_releases_to_csv(releases_data)

