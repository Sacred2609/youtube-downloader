import yt_dlp
def print_banner():
    print('='*40)
    print('Welcome to the YouTube Video Downloader!')
    print('You can download videos in MP4 format.')
    print('='*40)
def progress_hook(d):
    if d['status'] == 'downloading':
        print(f"Downloading: {d['_percent_str']} at {d['_speed_str']} ", end="\r")
    if d['status'] == 'finished':
        print("\nDownload complete! Processing file...")
print_banner()           
save_path = input("Enter the path where you want to save the video (leave blank for current directory): ")
if save_path == "":
    save_path = "."
ydl_opts = {"format": "mp4", "outtmpl": f"{save_path}/%(title)s.%(ext)s", "progress_hooks": [progress_hook]}
while True:
    url = input("Enter the URL of the video you want to download: ")
    if url == "quit":
        print("Exiting the program.")
        break
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([url])
    except yt_dlp.utils.DownloadError as e:
        print(f"Download error: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")