from pytube import YouTube
from pytube.request import stream

# Path to your exported cookies file
cookies_path = "path/to/cookies.txt"

with open(cookies_path, "r") as file:
    cookies = file.read()

# Use the cookies while creating YouTube object
yt = YouTube(link, use_oauth=False, allow_oauth_cache=True)
stream.set_cookies(cookies)

SAVE_PATH = "/home/bluel/Downloads"  # Change to your desired location

link = "https://youtu.be/91C9IyFTdME?si=rs2KrdD7tWTCcMXo"  # URL must be in quotes

try:
    # Create a YouTube object
    yt = YouTube(link, use_oauth=False, allow_oauth_cache=True)
except Exception as e:
    print(f"Connection Error: {e}")
    exit()

try:
    # Filter for progressive streams and download the first available
    d_video = yt.streams.filter(progressive=True, file_extension="mp4").first()
    if d_video:
        d_video.download(output_path=SAVE_PATH)
        print("Video downloaded successfully!")
    else:
        print("No downloadable streams available.")
except Exception as e:
    print(f"Error downloading video: {e}")
