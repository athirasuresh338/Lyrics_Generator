# Lyrics Generator Application

## Overview

This application allows users to fetch and display the lyrics of a song by providing the song title and artist name. It uses the Genius API to retrieve song lyrics and displays them in a text area. The application is built using Python's Tkinter library for the GUI and the `lyricsgenius` package for interacting with the Genius API.

## Requirements

Before running the application, ensure that the following dependencies are installed:

- Python 3.x
- Tkinter (usually comes pre-installed with Python)
- `lyricsgenius` library

You can install the `lyricsgenius` library via pip:

```bash
pip install lyricsgenius
```
## Setup
### Genius API Access Token
To interact with the Genius API, you need to have an access token. Follow these steps to get your API token:

1. Go to the [LyricsGenius API](https://lyricsgenius.readthedocs.io/en/master/index.html) page.
2. Sign in or create an account.
3. Create an API client and get your access token.
4. Replace the `YOUR_ACCESS_TOKEN` placeholder in the code with your actual API token.
```bash
genius = lyricsgenius.Genius("YOUR_ACCESS_TOKEN")
```
## Running the Application
1. Download the script file.
2. Ensure you have Python 3.x and the necessary libraries installed.
3. Run the script:
```bash
python lyrics_generator.py
```
The application will open a graphical user interface (GUI) where you can enter the song title and artist name to fetch the lyrics.

# Features

- **Song Title and Artist Name Input**: Users can input the song title and artist name.
- **Get Lyrics Button**: When clicked, the button fetches the lyrics using the Genius API.
- **Lyrics Display Area**: The fetched lyrics are displayed in a text area.
- **Error Handling**: The application will notify the user if:
  - Both fields are not filled.
  - The song cannot be found on Genius.
  - An error occurs during the API call.

# GUI Layout

- **Song Name Input**: Text field for entering the song title.
- **Artist Name Input**: Text field for entering the artist name.
- **Get Lyrics Button**: Button to trigger the lyric-fetching process.
- **Lyrics Text Area**: Display the fetched lyrics in a scrollable text area.

# Code Structure

- **Imports**:
  - `tkinter` and `ttk` for the GUI.
  - `lyricsgenius` for interacting with the Genius API.

- **Functions**:
  - `get_lyrics()`: Fetches the lyrics from Genius using the song title and artist name.

- **Main Window Setup**:
  - Tkinter window (`root`) configuration.
  - Widgets for user input (labels, entry fields, button).
  - Text area to display lyrics.

# Error Handling

- **Empty Input Fields**: If the song title or artist name is empty, a warning message is shown.
- **Song Not Found**: If no song is found based on the entered details, an informational message is displayed.
- **API Errors**: In case of any errors while calling the Genius API, an error message is shown.

# Example Usage

1. Open the application window.
2. Enter the song title and artist name (e.g., "Let It Be" and "The Beatles").
3. Click the "Get Lyrics" button.
4. The lyrics will appear in the text area below.
