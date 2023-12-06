import subprocess

def apply_psychedelic_filter(input_path, output_path):
    subprocess.run(['ffmpeg', '-i', input_path, '-vf', 'frei0r=filter=vertigo', output_path])

if __name__ == "__main__":
    input_file = "BBBVideo.mp4"
    output_file = "output_psychedelic_video.mp4"
    apply_psychedelic_filter(input_file, output_file)
