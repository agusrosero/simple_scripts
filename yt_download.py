from pytube import YouTube

link = input("Ingresa el link del video: ")
yt = YouTube(link)

# Descargar el video
print("Descargando...")

download1 = yt.streams.get_highest_resolution()
download1.download()

print("Download complete!")

