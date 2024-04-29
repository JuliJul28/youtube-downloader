import webbrowser
from pytube import YouTube
import os
 # made by juilijul
orange_ascii_art = r"""


$$$$$$$$\ $$\   $$\ $$$$$$$$\ $$$$$$$$\ $$$$$$$\        $$\   $$\ $$$$$$$\  $$\                 
$$  _____|$$$\  $$ |\__$$  __|$$  _____|$$  __$$\       $$ |  $$ |$$  __$$\ $$ |                
$$ |      $$$$\ $$ |   $$ |   $$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |            $$\ 
$$$$$\    $$ $$\$$ |   $$ |   $$$$$\    $$$$$$$  |      $$ |  $$ |$$$$$$$  |$$ |            \__|
$$  __|   $$ \$$$$ |   $$ |   $$  __|   $$  __$$<       $$ |  $$ |$$  __$$< $$ |                
$$ |      $$ |\$$$ |   $$ |   $$ |      $$ |  $$ |      $$ |  $$ |$$ |  $$ |$$ |            $$\ 
$$$$$$$$\ $$ | \$$ |   $$ |   $$$$$$$$\ $$ |  $$ |      \$$$$$$  |$$ |  $$ |$$$$$$$$\       \__|
\________|\__|  \__|   \__|   \________|\__|  \__|       \______/ \__|  \__|\________|          
                                                                                                                                                                                                                                                     
"""

orange_ascii_art = "\033[38;5;208m" + orange_ascii_art + "\033[0m"

print(orange_ascii_art)

choices = ["music", "video"]

choice = input("music , video:\n >> ")

if choice in choices:
    if choice == "music":
        url = input("Youtube Link:\n >>")
        yt = YouTube(url)
        video = yt.streams.filter(only_audio = True).first()
        destination = r'C:\Users\shon\Desktop\LoveCoding'
        out_file = video.download(output_path = destination)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
    else:
        url = input("Youtube Link:\n >>")
        url = url[:12] + "ss" + url[12:]
        webbrowser.open(url)
