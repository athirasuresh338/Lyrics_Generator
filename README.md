# Lyrics Generator App 🎶

## Overview  
This project is a simple **Lyrics Generator** app built using **Tkinter** and the **Genius API**. It allows users to search for song lyrics by entering the **song title** and **artist name**. Once the user inputs the required information, the app fetches the lyrics and displays them in a clean and interactive interface.

## Features  
- 🎤 **Search for Song Lyrics**: Enter the song title and artist name to fetch lyrics.  
- 📜 **Text Display**: The lyrics are displayed in a scrollable text box.  
- ⚠️ **Error Handling**: Shows helpful messages if no song is found or there is an input error.  
- 🌈 **User-Friendly Interface**: Built using Tkinter with a visually appealing design.

## How to Use  
1. **Input Song Title and Artist Name**: Type the song title and artist's name into the respective fields.  
2. **Click "Get Lyrics"**: Hit the "Get Lyrics" button to retrieve the song's lyrics from the Genius database.  
3. **View Lyrics**: The lyrics will appear in the text area, where you can read them at your convenience.  

## Installation  
1. Install the required libraries using pip:
    ```bash
    pip install lyricsgenius
    pip install tk
    ```
2. Get your **Genius API Access Token** from [Genius API](https://genius.com/developers).
3. Replace `"YOUR_ACCESS_TOKEN"` in the code with your actual access token.

4. Run the Python script to launch the app.

## Code Breakdown  
- **Tkinter**: Used to create the graphical user interface (GUI).  
- **lyricsgenius**: Interacts with the Genius API to fetch song lyrics based on the song title and artist name.  
- **Error Handling**: Includes error messages using `messagebox` to notify users if something goes wrong.

## Example Usage  
1. Enter "Shape of You" for the song and "Ed Sheeran" for the artist.  
2. Click the **Get Lyrics** button to see the lyrics of "Shape of You".

---
