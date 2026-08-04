import requests
import pandas as pd
import time
import json
import os

def fetch_repos():
    repos = []
    # GitHub unauthenticated search API allows 10 requests per minute.
    # We will fetch 5 pages (500 repositories) to be safe and fast.
    for page in range(1, 6):
        url = f"https://api.github.com/search/repositories?q=stars:>5000&sort=stars&order=desc&per_page=100&page={page}"
        print(f"Fetching page {page}...")
        response = requests.get(url)
        
        if response.status_code == 200:
            data = response.json()
            for item in data.get("items", []):
                repos.append({
                    "repository_name": item.get("full_name"),
                    "owner": item.get("owner", {}).get("login"),
                    "description": item.get("description", ""),
                    "language": item.get("language", ""),
                    "topics": json.dumps(item.get("topics", [])),
                    "stars": item.get("stargazers_count", 0),
                    "forks": item.get("forks_count", 0),
                    "license": item.get("license", {}).get("name") if item.get("license") else None,
                    "created_at": item.get("created_at"),
                    "updated_at": item.get("updated_at")
                })
        else:
            print(f"Error {response.status_code} on page {page}")
        
        # Sleep to respect rate limits
        time.sleep(2)

    return pd.DataFrame(repos)

if __name__ == "__main__":
    print("Starting fetch...")
    df = fetch_repos()
    
    # Ensure data directory exists
    os.makedirs("data", exist_ok=True)
    
    # Save to CSV
    output_path = "data/github_repositories.csv"
    df.to_csv(output_path, index=False)
    
    print(f"Saved {len(df)} repositories to {output_path}")
    print("\nDataset structure:")
    print(df.info())
    print("\nSample rows:")
    print(df.head(3))
