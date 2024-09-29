from pytube import YouTube
yt = YouTube('https://youtu.be/3kyWhpoHEHY')
yt.streams.filter(progressive=True, file_extension='mp4').order_by('resolution').desc().first().download()