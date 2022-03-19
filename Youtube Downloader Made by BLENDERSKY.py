import os
from pytube import YouTube

def start() :  
    print("hello")
    link()
def link() :
    link = input("Paste link here\n>>")
    global yt
    yt = YouTube(link)
    destination()
def destination() : 
    print("Enter the destination(example: C:\ytdownloads) (leave blank for default directory)")
    global output 
    output = str(input(">> ")) or "C:\ytdownloads"
    audioorvid()
def audioorvid() :
    typp = input("Audio or Video?\ntype 'a' for audio | 'v' for video\n>>")
    if typp == "a":
        out_file = yt.streams.filter(only_audio=True,).first().download(output_path=output, skip_existing=True)
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        end()
    elif typp == "v":
        resolution()
def resolution() :
    res = input("Choose Resolution\n('360', '480', '720', '1080')\n>>")
    if res == "360":
        yt.streams.filter(res="360p").first().download(output_path=output, skip_existing=True)
        end()
    elif res == "480":
        yt.streams.filter(res="480p").first().download(output_path=output, skip_existing=True)
        end()
    elif res == "720":
        yt.streams.filter(res="720p").first().download(output_path=output, skip_existing=True)
        end()
    elif res == "1080":
        yt.streams.filter(res="1080p").first().download(output_path=output, skip_existing=True)
        end()
    else:
        print("WRONG RESOLUTION!")
        resolution()
    

def end() :
    print(yt.title + " has been successfully downloaded.\n at " +output)
    print("Thanks for using")
    endvar = input("press enter to end")

start()


