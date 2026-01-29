# LeetCode Sync to GitHub

🤖 Automatically sync your accepted LeetCode solutions to GitHub and maintain your contribution graph!

## Overview

This repository automatically syncs all your accepted LeetCode submissions to GitHub using GitHub Actions. Your solutions are organized by difficulty level and committed daily, maintaining a green contribution graph without manual effort.

## Features

✅ **Automatic Daily Sync** - Syncs at midnight UTC every day  
✅ **Manual Trigger** - Can be manually triggered anytime from Actions tab  
✅ **Secure** - Uses GitHub Secrets to store LeetCode credentials  
✅ **Organized** - Solutions organized by difficulty (Easy, Medium, Hard)  
✅ **Zero Manual Work** - Just solve problems, automation does the rest  

## Setup Instructions

### Step 1: Extract LeetCode Session Cookies

1. Open [leetcode.com](https://leetcode.com) and login
2. Press `F12` to open Developer Tools
3. Go to **Application** tab → **Cookies** → `https://leetcode.com`
4. Copy the value of `LEETCODE_SESSION` cookie
5. Copy the value of `csrftoken` cookie

### Step 2: Update GitHub Secrets

1. Go to this repository's **Settings** → **Secrets and variables** → **Actions**
2. Edit `LEETCODE_SESSION` secret and paste your actual session cookie value
3. Edit `LEETCODE_CSRF_TOKEN` secret and paste your actual CSRF token value

### Step 3: Verify Setup

1. Go to **Actions** tab
2. Select **LeetCode Sync** workflow
3. Click **Run workflow** to test
4. Wait ~2 minutes for completion

## Workflow Details

**Schedule:** Daily at 00:00 UTC (Midnight)  
**Trigger:** Can be manually triggered from Actions tab  
**Output:** Solutions organized by difficulty in dedicated folders  

## File Structure

```
leetcode-sync/
├── Easy/
│   ├── two-sum.py
│   ├── palindrome-number.py
│   └── ...
├── Medium/
│   ├── add-two-numbers.py
│   └── ...
├── Hard/
│   └── ...
└── sync_leetcode.py
```

## How It Works

1. GitHub Action runs on schedule or manual trigger
2. Python script fetches your accepted submissions from LeetCode API
3. Solutions are organized by difficulty level
4. Files are committed with timestamps
5. Commits appear on your GitHub contribution graph

## Important Notes

⚠️ **Cookie Expiration** - LeetCode session cookies expire every 2-4 weeks. When syncing stops working, repeat Step 1-2 to refresh credentials.

⚠️ **Only Accepted Solutions** - Only fully accepted solutions are synced. Partial submissions are not included.

⚠️ **Privacy** - This repository can be public. Your solution files contain your problem-solving approach, not sensitive data.

## Maintenance

**Refresh Cookies:**
- If workflow fails, cookies have likely expired
- Repeat "Extract LeetCode Session Cookies" step
- Update secrets in GitHub
- Re-run workflow

**Check Workflow Status:**
- Visit `github.com/YOUR_USERNAME/leetcode-sync/actions`
- Click on latest LeetCode Sync run
- Review logs for any errors

## Contribution Graph Impact

- Each successful sync creates 1 commit
- Commits are dated based on sync time
- Appears as green squares on your GitHub profile
- Helps maintain contribution streak while learning

## Next Steps

Optional enhancements you can add:
- Add a progress badge showing total problems solved
- Generate statistics dashboard
- Add LeetCode difficulty/topic filtering
- Create tags for each problem category

## Security

- Your credentials are stored as GitHub Secrets (encrypted)
- Secrets are never logged or exposed
- Only accessible to GitHub Actions workflows in this repo
- Your actual cookie values are never visible after setting them

---

**Last Updated:** January 29, 2026  
**Maintained by:** shivambarkule  
**Status:** ✅ Active and Syncing
