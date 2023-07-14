from pytube import YouTube
from sys import argv

link = argv[1]
yt = YouTube(link)

print("Title: ", yt.title)
print("Author: ", yt.author)
print("Views: ", yt.views)
print("\n Downloading wait a moment!")


yd = yt.streams.get_highest_resolution()

yd.download('YT_Downloads')