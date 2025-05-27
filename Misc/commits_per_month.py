import requests
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import os
from tqdm import tqdm
import time

def fetch_commits(owner, repo, page=1, per_page=100):
    """Fetch commits from a GitHub repository with pagination."""
    url = f"https://api.github.com/repos/{owner}/{repo}/commits"
    params = {
        'page': page,
        'per_page': per_page,
        'sha': 'master'  # Default branch, change if needed
    }
    
    response = requests.get(url, params=params)
    
    # Check if we hit the rate limit
    if response.status_code == 403 and 'rate limit' in response.text.lower():
        reset_time = int(response.headers.get('X-RateLimit-Reset', 0))
        current_time = time.time()
        sleep_time = max(reset_time - current_time, 0) + 1
        
        print(f"Rate limit hit. Sleeping for {sleep_time:.2f} seconds...")
        time.sleep(sleep_time)
        return fetch_commits(owner, repo, page, per_page)
    
    # If other error, just print the status and return empty list
    if response.status_code != 200:
        print(f"Error: Status code {response.status_code}")
        print(f"Response: {response.text}")
        return []
    
    return response.json()

def get_all_commits(owner, repo):
    """Get all commits from a repository using pagination."""
    all_commits = []
    page = 1
    
    print(f"Fetching commits from {owner}/{repo}...")
    
    while True:
        commits = fetch_commits(owner, repo, page)
        if not commits:
            break
        
        all_commits.extend(commits)
        print(f"Fetched page {page} ({len(commits)} commits)")
        
        # Check if we got fewer commits than requested, meaning it's the last page
        if len(commits) < 100:
            break
        
        page += 1
        
        # Be nice to the GitHub API
        time.sleep(1)
    
    return all_commits

def extract_date_from_commit(commit):
    """Extract the date from a commit."""
    try:
        date_str = commit['commit']['author']['date']
        return datetime.strptime(date_str, '%Y-%m-%dT%H:%M:%SZ')
    except (KeyError, ValueError) as e:
        print(f"Error extracting date: {e}")
        return None

def plot_commits_per_month(dates):
    """Plot commits per month."""
    # Convert dates to pandas datetime
    df = pd.DataFrame({'date': dates})
    
    # Extract year and month to group by month
    df['year_month'] = df['date'].dt.to_period('M')
    
    # Count commits per month
    monthly_counts = df.groupby('year_month').size()
    
    # Convert period index to datetime for plotting
    monthly_index = monthly_counts.index.to_timestamp()
    
    # Create the plot
    plt.figure(figsize=(12, 6))
    plt.bar(monthly_index, monthly_counts, width=25)
    
    # Format the x-axis to show months
    plt.gca().xaxis.set_major_locator(mdates.MonthLocator(interval=6))
    plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m'))
    
    # Rotate date labels for better readability
    plt.gcf().autofmt_xdate()
    
    plt.title('Commits per Month in scikit-bio/scikit-bio')
    plt.xlabel('Month')
    plt.ylabel('Number of Commits')
    plt.tight_layout()
    
    # Save the plot
    plt.savefig('commits_per_month.png')
    print(f"Plot saved as 'commits_per_month.png'")
    
    # Display the plot
    plt.show()

def main():
    owner = "scikit-bio"
    repo = "scikit-bio"
    
    # Fetch all commits
    commits = get_all_commits(owner, repo)
    print(f"Total commits fetched: {len(commits)}")
    
    # Extract dates
    dates = [extract_date_from_commit(commit) for commit in commits]
    dates = [date for date in dates if date is not None]
    
    # Plot commits per month
    plot_commits_per_month(dates)

if __name__ == "__main__":
    main() 