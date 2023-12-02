# Billboard Spotify Playlist Creator

## Introduction
This script, `playlist.py`, automates the process of creating a Spotify playlist based on the Billboard Hot 100 chart for a specific date. It scrapes song names from the Billboard website and adds these tracks to a new Spotify playlist.

## Requirements
To run this script, you'll need Python installed along with a few additional libraries. Install the required libraries using pip:
`pip install beautifulsoup4 requests spotipy python-dotenv`


## Setting Up Spotify API Credentials
### Step 1: Spotify Developer Account
- Create a Spotify Developer account at [Spotify for Developers](https://developer.spotify.com/).
- Once logged in, create an app to obtain your Client ID and Client Secret.

### Step 2: Setting Environment Variables
- Rename the `.env.example` file to `.env`.
- Fill in the `SPOTIPY_CLIENT_ID`, `SPOTIPY_CLIENT_SECRET`, and `SPOTIPY_USERNAME` with your Spotify details.

## Usage
Run the script with:
`python playlist.py`


Follow the prompt to enter the date in the format `YYYY-MM-DD`. The script will create a Spotify playlist with songs from the Billboard Hot 100 chart of that date.

## Environment Setup (Optional)
For a more isolated environment, use a virtual environment:
`python -m venv venv`
`source venv/bin/activate` 
# On Windows, use 
`venv\Scripts\activate`
`pip install -r requirements.txt`



