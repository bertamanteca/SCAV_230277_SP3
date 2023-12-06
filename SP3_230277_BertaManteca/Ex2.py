import subprocess

def create_split_screen(input_file_vp8, input_file_vp9, output_file):
    comando = [
        'ffmpeg',
        '-i', input_file_vp8,
        '-i', input_file_vp9,
        '-filter_complex', '[0:v]scale=iw/2:ih[vp8];[1:v]scale=iw/2:ih[vp9];[vp8][vp9]hstack',
        '-c:v', 'libx264',
        output_file
    ]
    subprocess.run(comando)

def ejecutar():
    # Input videos (asegúrate de que ya estén en formatos VP8 y VP9)
    input_video_vp8 = 'BBBVideo_160x120_vp8.webm'
    input_video_vp9 = 'BBBVideo_160x120_vp9.webm'

    # Output video
    output_comparison = 'split_screen_comparison.mp4'

    create_split_screen(input_video_vp8, input_video_vp9, output_comparison)

    print("Comparación de pantalla dividida creada.")


if __name__ == "__main__":
    ejecutar()
