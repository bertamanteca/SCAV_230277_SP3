import subprocess
import os


class VideoSubtitlesProcessor:
    def __init__(self, input_video, output_video):
        self.input_video = input_video
        self.output_video = output_video

    def download_subtitles(self, output_subtitle_file):
        input_video_path = os.path.abspath(self.input_video)

        cmd_download_subtitles = [
            'youtube-dl',
            '--write-sub', '--sub-lang', 'en',
            '--skip-download',
            '--output', output_subtitle_file,
            input_video_path
        ]
        result = subprocess.run(cmd_download_subtitles, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print(f"Subtitle download failed. Error: {result.stderr.decode('utf-8')}")

    def integrate_subtitles(self, input_subtitle_file):
        cmd_integrate_subtitles = [
            'ffmpeg',
            '-i', self.input_video,
            '-vf', f'subtitles={input_subtitle_file}',
            '-c:a', 'copy',
            '-t', '50',
            self.output_video
        ]
        result = subprocess.run(cmd_integrate_subtitles, stdout=subprocess.PIPE, stderr=subprocess.PIPE)

        if result.returncode != 0:
            print(f"Subtitle integration failed. Error: {result.stderr.decode('utf-8')}")


class VideoCutter(VideoSubtitlesProcessor):
    def cut_video(self):
        subtitle_file = 'subtitles.srt'
        self.download_subtitles(subtitle_file)
        self.integrate_subtitles(subtitle_file)


def ejecutar():
    video_cutter = VideoCutter('LionelMessi.mp4', 'EX5_output_video_with_subtitles.mp4')


    video_cutter.cut_video()


if __name__ == "__main__":
    ejecutar()
