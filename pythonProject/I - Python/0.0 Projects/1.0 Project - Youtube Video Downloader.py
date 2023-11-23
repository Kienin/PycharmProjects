from pytube import YouTube

def download_video(url, output_path='.'):
    try:
        # Create a Youtube object
        yt = YouTube(url)

        # Get the highest resolution stream
        video_stream = yt.streams.get_highest_resolution()

        # Download the video to the specified output path
        video_stream.download(output_path)

        print(f"Video downloaded successfully to: {output_path}")

    except Exception as e:
        print(f"An error occurred: {str(e)}")

# Video input will be saved to Downloads folder.

video = input("Please Enter the URL of the video you want to download: ")
downloads = r"C:\Users\kevin\Videos\Youtube Downloads I - Python"

download_video(video, downloads)