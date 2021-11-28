from tkinter import *

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
get_videos = Button(root, text="Get Videos")
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
download_start = Button(root, text="Download Start", state=DISABLED)
download_start.pack(pady=10)

root.mainloop()