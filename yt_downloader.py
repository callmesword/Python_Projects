import pytube

print("Paste the video's URL: ")
url = input("URL: ")

pytube.YouTube(url).streams.get_highest_resolution().download('../Video')