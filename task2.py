import requests
from moviepy.editor import VideoFileClip
import os

def tiktok_to_gif(url: str, framrate: str):
    try:
        req = requests.get(url, allow_redirects=True)
    except:
        print("Url Error")
    finally:
        download_path = "result/mp4/tik_tok.mp4"

        # download video
        with open(download_path, 'wb') as file:
            file.write(req.content)

        # convert to gif
        # videoClip = VideoFileClip("tiktok.mp4")
        videoClip = VideoFileClip(download_path)

        gif_path = "result/gif/tik_tok.gif"

        videoClip.write_gif(gif_path, fps=framrate)

        result_path = os.path.abspath(gif_path)
        print(f"Converted tiktok at: {result_path}")

url = input("Enter video url: ")
# for faster download set framrate to 15 fps
fps = int(input("Enter fps for gif: "))
tiktok_to_gif(url, fps)