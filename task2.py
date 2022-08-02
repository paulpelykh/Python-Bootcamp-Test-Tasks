import requests
from moviepy.editor import VideoFileClip
import os

def tiktok_to_gif(url: str):
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
        videoClip = VideoFileClip("tiktok.mp4")
        # videoClip = VideoFileClip(download_path)

        gif_path = "result/gif/tik_tok.gif"

        # for faster download set framrate to 15 fps
        videoClip.write_gif(gif_path, fps=1)

        result_path = os.path.abspath(gif_path)
        print(f"Converted tiktok at: {result_path}")

url = 'https://v16m-webapp.tiktokcdn-us.com/ed129ecb01ab00e202682e99f68a9288/62e7cb0d/video/tos/useast5/tos-useast5-pve-0068-tx/d69985b1677b4a73a584b56d604011ca/?a=1988&ch=0&cr=0&dr=0&lr=tiktok_m&cd=0%7C0%7C1%7C0&cv=1&br=4020&bt=2010&cs=0&ds=3&ft=ebtHKH-qMyq8ZjFl1we2N9befl7Gb&mime_type=video_mp4&qs=0&rc=OTU4MzU0NzVnaDpnOGg8OEBpajM5Z2c6ZmYzZTMzZzczNEAuMC9jLWBgNmExMzJfY18tYSMxX28vcjRnMGRgLS1kMS9zcw%3D%3D&l=20220801064449EF653E99EF32BC2EAB55'
tiktok_to_gif(url)