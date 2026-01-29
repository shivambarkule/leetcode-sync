#!/usr/bin/env python3
import os
import requests
import json
from datetime import datetime
from pathlib import Path

def get_leetcode_submissions():
    """Fetch LeetCode accepted submissions"""
    session_cookie = os.environ.get('LEETCODE_SESSION')
    csrf_token = os.environ.get('LEETCODE_CSRF_TOKEN')
    username = os.environ.get('LEETCODE_USERNAME')
    
    if not all([session_cookie, csrf_token, username]):
        print("Missing required environment variables")
        return []
    
    headers = {
        'User-Agent': 'Mozilla/5.0',
        'Referer': 'https://leetcode.com/',
        'Cookie': f'LEETCODE_SESSION={session_cookie}',
        'X-CSRFToken': csrf_token,
    }
    
    try:
        # Fetch submissions from LeetCode GraphQL API
        url = 'https://leetcode.com/api/submissions/'
        response = requests.get(url, headers=headers, timeout=10)
        
        if response.status_code != 200:
            print(f"Failed to fetch submissions: {response.status_code}")
            return []
        
        submissions = response.json().get('submissions_dump', [])
        # Filter only accepted submissions
        accepted = [s for s in submissions if s.get('status') == 'Accepted']
        return accepted
    
    except Exception as e:
        print(f"Error fetching submissions: {e}")
        return []

def save_submission(submission):
    """Save submission to local file"""
    try:
        title = submission.get('title', 'Unknown')
        slug = submission.get('title_slug', 'unknown')
        code = submission.get('code', '')
        difficulty = submission.get('difficulty', 'Unknown')
        
        # Create directory structure by difficulty
        base_dir = Path(difficulty)
        base_dir.mkdir(exist_ok=True)
        
        # Save solution file
        filename = f"{slug}.py"
        filepath = base_dir / filename
        
        with open(filepath, 'w', encoding='utf-8') as f:
            f.write(f"# {title}\n")
            f.write(f"# Difficulty: {difficulty}\n")
            f.write(f"# Submitted: {datetime.now().isoformat()}\n\n")
            f.write(code)
        
        print(f"Saved: {filepath}")
        return True
    
    except Exception as e:
        print(f"Error saving submission: {e}")
        return False

def main():
    print("Starting LeetCode sync...")
    submissions = get_leetcode_submissions()
    
    if not submissions:
        print("No submissions found or failed to fetch")
        return
    
    saved_count = 0
    for submission in submissions:
        if save_submission(submission):
            saved_count += 1
    
    print(f"Successfully synced {saved_count} submissions")

if __name__ == '__main__':
    main()
