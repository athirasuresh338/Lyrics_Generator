import tkinter as tk
from tkinter import messagebox, ttk
import lyricsgenius

# Initialize Genius API
genius = lyricsgenius.Genius("YOUR_ACCESS_TOKEN")

def get_lyrics():
    song_title = title_entry.get()
    artist_name = artist_entry.get()
    
    if not song_title or not artist_name:
        messagebox.showwarning("Input Error", "Please enter both song title and artist name.")
        return
    
    try:
        song = genius.search_song(song_title, artist_name)
        if song:
            lyrics_text.delete(1.0, tk.END)  # Clear previous lyrics
            lyrics_text.insert(tk.END, song.lyrics)  # Insert new lyrics
        else:
            messagebox.showinfo("Not Found", "Song not found.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Set up the main window
root = tk.Tk()
root.title("Lyrics Generator")
root.geometry("600x500")
root.configure(bg="#f0f8ff")

# Create a style for the widgets
style = ttk.Style()
style.configure("TLabel", background="#f0f8ff", font=("Arial", 12))
style.configure("TButton", background="#4caf50", foreground="Black", font=("Arial", 12), padding=10)
style.map("TButton", background=[('active', '#45a049')])
style.configure("TText", font=("Arial", 10))

# Create input fields
ttk.Label(root, text="Song Name").pack(pady=10)
title_entry = ttk.Entry(root, width=50)
title_entry.pack(pady=5)

ttk.Label(root, text="Artist Name").pack(pady=10)
artist_entry = ttk.Entry(root, width=50)
artist_entry.pack(pady=5)

# Create a button to fetch lyrics
fetch_button = ttk.Button(root, text="Get Lyrics", command=get_lyrics)
fetch_button.pack(pady=20)

# Create a text area to display lyrics
lyrics_text = tk.Text(root, wrap=tk.WORD, width=60, height=20, bg="#e0f7fa", fg="#000000", borderwidth=2, relief="groove")
lyrics_text.pack(pady=10)

# Start the main loop
root.mainloop()