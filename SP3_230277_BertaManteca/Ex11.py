import subprocess

def convertir_video(input_file, output_file, codec):
    comando = [
        'ffmpeg',
        '-i', input_file,
        '-c:v', codec,
        output_file
    ]
    subprocess.run(comando)

def ejecutar():
    # Videos de entrada
    videos = ['BBBVideo_160x120.mp4', 'BBBVideo_360x240.mp4', 'BBBVideo_480p.mp4', 'BBBVideo_720p.mp4']

    # Mostrar los videos disponibles al usuario
    print("Videos disponibles:")
    for i, video in enumerate(videos, 1):
        print(f"{i}. {video}")

    try:
        opcion = int(input("Seleccione el número del video que desea convertir (1-4): "))


        if opcion < 1 or opcion > 4:
            raise ValueError("Número de video no válido.")
    except ValueError as e:
        print(f"Error: {e}")
        exit()

    video_seleccionado = videos[opcion - 1]

    # Usuario escoge qué formato quiere y cuál no
    formato_vp8 = input("¿Desea convertir a VP8? (si/No): ").lower() == 'si'
    formato_vp9 = input("¿Desea convertir a VP9? (si/No): ").lower() == 'si'
    formato_h265 = input("¿Desea convertir a H.265 ? (si/No): ").lower() == 'si'

    # Conversión solo al formato seleccionado
    if formato_vp8:
        convertir_video(video_seleccionado, f'{video_seleccionado[:-4]}_vp8.webm', 'libvpx')
    if formato_vp9:
        convertir_video(video_seleccionado, f'{video_seleccionado[:-4]}_vp9.webm', 'libvpx-vp9')
    if formato_h265:
        convertir_video(video_seleccionado, f'{video_seleccionado[:-4]}_h265.mp4', 'libx265')

    print("Conversión completada para el video seleccionado.")

if __name__ == "__main__":
    ejecutar()
