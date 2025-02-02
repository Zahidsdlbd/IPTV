import requests

# List of raw GitHub file URLs
raw_urls = [
    "https://raw.githubusercontent.com/SonyIPTV/Sony-IPTV-Live/refs/heads/main/Sony%20IPTV%20Live.m3u",
    "https://raw.githubusercontent.com/FunctionError/PiratesTvPlus/main/PiratesPlus.m3u"
]

# Output file (playlist)
playlist_file = "playlist.m3u"

# Function to download and save content
def download_and_save(url):
    try:
        print(f"Downloading: {url}")
        response = requests.get(url)
        response.raise_for_status()  # Check if the request was successful

        # Append to the file
        with open(playlist_file, 'a', encoding='utf-8') as f:
            f.write(response.text + "\n")

        print(f"Added content from: {url}")
    except requests.exceptions.RequestException as e:
        print(f"Error downloading {url}: {e}")

# Create or reset the playlist file
with open(playlist_file, 'w', encoding='utf-8') as f:
    f.write("# Auto-updated playlist\n")

# Download all playlists
for url in raw_urls:
    download_and_save(url)

print("✅ Playlist update complete!")
