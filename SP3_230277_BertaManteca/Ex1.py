
#este codi el que fa és la conversio a les 4 resolucions proposades
import subprocess

def convertir_video(input_path, output_path, resolution):
    
    command = [
        'ffmpeg',
        '-i', input_path,
        '-vf', f'scale={resolution}',
        '-c:a', 'aac',
        '-strict', 'experimental',
        '-b:a', '128k',
        output_path
    ]

    subprocess.run(command)

def ejecutar():

    input_video_path = "BBBVideo.mp4"
    output_video_path_720p = "BBBVideo_720p.mp4"
    output_video_path_480p = "BBBVideo_480p.mp4"
    output_video_path_360x240 = "BBBVideo_360x240.mp4"
    output_video_path_160x120 = "BBBVideo_160x120.mp4"


    convertir_video(input_video_path, output_video_path_720p, '1280:720')
    convertir_video(input_video_path, output_video_path_480p, '854:480')
    convertir_video(input_video_path, output_video_path_360x240, '360:240')
    convertir_video(input_video_path, output_video_path_160x120, '160:120')

if __name__ == "__main__":
    ejecutar()

