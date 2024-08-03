from pytube.cli import on_progress
from pytube import YouTube
from pytube import exceptions
import os

# where to save
SAVE_PATH = os.path.join(os.getenv("USERPROFILE"), "Downloads")

print("Bienvenido al descargador de videos de YouTube :)")
print("by: Jaime de la Fuente")
# link of the video to be downloaded
link = str(input("Introduzca el link: "))


def mp3_converter(out_file):
    base, ext = os.path.splitext(out_file)
    new_file = base + '.mp3'
    os.rename(out_file, new_file)

try:
    yt = YouTube(link, on_progress_callback=on_progress)
    opcion = input("En que formato lo quiere descargar (mp3/mp4): ")
    opcion = opcion.lower()

    if opcion == 'mp3':
        t = yt.streams.filter(only_audio=True).first()

    elif opcion == 'mp4':        
        t = yt.streams.get_highest_resolution()    

    else:
        print('Formato no válido')

    d_file = t.download(output_path=SAVE_PATH)

    if opcion == 'mp3':
        mp3_converter(d_file)

    print(yt.title + " ha sido descargado con exito en " + SAVE_PATH)

except Exception as ex:
    print("Error, no se pudo descargar: "+ str(ex))

input("Presiona cualquier botón para salir")
