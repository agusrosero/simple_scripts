from pytube import YouTube

link = input("Ingresa el link del video: ")
yt = YouTube(link)

# Descarga el video
print("Descargando...")
descarga = yt.streams.get_highest_resolution()
descarga.download()

print("Download complete!")
