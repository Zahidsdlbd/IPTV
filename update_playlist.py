import requests

# List of raw GitHub file URLs
raw_urls = [
    "https://raw.githubusercontent.com/SonyIPTV/Sony-IPTV-Live/refs/heads/main/Sony%20IPTV%20Live.m3u",
    "https://raw.githubusercontent.com/FunctionError/PiratesTvPlus/main/PiratesPlus.m3u"
]

# File where the playlist will be stored
playlist_file = "playlist.m3u"

# Function to download content from URL and append to playlist
def download_and_add_to_playlist(url):
    try:
        print(f"Downloading content from: {url}")  # Debugging: Show URL being fetched
        response = requests.get(url)
        response.raise_for_status()  # Check for successful response
        
        # Debugging: Show the first 100 characters of the response
        print(f"Received content: {response.text[:100]}...")  # Show first 100 characters

        # Append content to the playlist file using UTF-8 encoding
        with open(playlist_file, 'a', encoding='utf-8') as f:  # Use UTF-8 encoding here
            f.write(response.text)
            f.write("\n")  # Add a newline after each file's content
        print(f"Added content from: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

# Create a new playlist or update the existing one
with open(playlist_file, 'w', encoding='utf-8') as f:  # Use UTF-8 encoding when creating the file
    f.write("# Playlist generated automatically\n")

# Download raw files and add to the playlist
for url in raw_urls:
    download_and_add_to_playlist(url)

print(f"Playlist {playlist_file} updated successfully.")
