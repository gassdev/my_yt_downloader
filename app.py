from tkinter import *
from pyyoutube import Api
from threading import Thread
from pytube import YouTube
from tkinter import messagebox
from decouple import config

def get_list_videos():
    global playlist_item_by_id
    # Clear list box
    list_box.delete(0, 'end')

    # create API Object
    api = Api(api_key=config('YT_API_KEY'))

    if "youtube" in playlistId.get():
        playlist_id = playlistId.get()[len("https://www.youtube.com/playlist?list="):]
    else:
        playlist_id = playlistId.get()

    # Get list of video links
    playlist_item_by_id = api.get_playlist_items(
        playlist_id=playlist_id,
        count=None,
        return_json=True
        )
    
    # Iterate through all video links and insert into listbox
    for index, videoid in enumerate(playlist_item_by_id['items']):
        list_box.insert(
            END,
            f"{str(index+1)}. {videoid['contentDetails']['videoId']}"
        )

    download_start.config(state=NORMAL)

def threading():
    # Call download_videos_function
    t1 = Thread(target=download_videos)
    t1.start()

def download_videos():
    download_start.config(state="disabled")
    get_videos.config(state="disabled")

    # Iterate through all selected videos
    for i in list_box.curselection():
        videoid = playlist_item_by_id['items'][i]['contentDetails']['videoId']

        link = f"https://www.youtube.com/watch?v={videoid}"

        yt_obj = YouTube(link)

        filters = yt_obj.streams.filter(
            progressive=True,
            file_extension='mp4'
        )

        # dowload the highest quality video
        filters.get_highest_resolution().download()

    messagebox.showinfo("Success", "Video successfully downloaded")
    download_start.config(state="normal")
    get_videos.config(state="normal")


# root element
root = Tk()


screen_width, screen_height = root.winfo_screenwidth(), root.winfo_screenheight()
# print(screen_width, screen_height)

window_width, window_height = 400, 400
# print(window_width, window_height)

position_top = (screen_height//2) - (window_height//2)
position_right = (screen_width//2) - (window_width//2)
# print(position_top, position_right)

root.geometry(f"{window_width}x{window_height}+{position_right}+{position_top}")

# Labels
Label(root, text="Youtube Playlist Downloader",
        font="italic 15 bold").pack(pady=10)

Label(root, text="Enter Playlist URL:-", font="italic 10").pack()

# Entry box
playlistId = Entry(root, width=60)
playlistId.pack(pady=5)

# Button
get_videos = Button(root, text="Get Videos", command=get_list_videos)
get_videos.pack(pady=10)

# scrollbar
scrollbar = Scrollbar(root)
scrollbar.pack(side=RIGHT, fill=BOTH)

# list box
list_box = Listbox(root, selectmode="multiple")
list_box.pack(expand=YES, fill="both")
list_box.config(yscrollcommand=scrollbar.set)
scrollbar.config(command=list_box.yview)

# Button
download_start = Button(
    root, 
    text="Download Start",
    command=threading, 
    state=DISABLED
    )
download_start.pack(pady=10)

root.mainloop()
