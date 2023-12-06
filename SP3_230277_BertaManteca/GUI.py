import subprocess
from tkinter import Tk, Label, Button, filedialog, OptionMenu, StringVar, Tk
from PIL import Image, ImageTk


class SubtitleProcessor:
    def __init__(self, input_video, output_video, subtitle_file):
        self.input_video = input_video
        self.output_video = output_video
        self.subtitle_file = subtitle_file

    def add_subtitles(self):
        cmd_add_subtitles = [
            'ffmpeg',
            '-i', self.input_video,
            '-vf', f'subtitles={self.subtitle_file}',
            '-c:a', 'copy',
            self.output_video
        ]
        subprocess.run(cmd_add_subtitles)


class VideoProcessorGUI:
    def __init__(self, master):
        self.master = master
        master.title("Video Processing Tool")

        #
        background_image = Image.open('messi.png')
        background_image = background_image.resize((800, 600), Image.ANTIALIAS)
        self.background_photo = ImageTk.PhotoImage(background_image)
        background_label = Label(master, image=self.background_photo)
        background_label.place(relwidth=1, relheight=1)

        # Crear botones con colores
        self.create_button("Convertir Resolución", self.show_resolution_window, 100, 50, "blue")
        self.create_button("Convertir Formatos", self.show_format_window, 100, 120, "blue")
        self.create_button("Comparar Videos", self.show_comparison_window, 100, 190, "blue")
        self.create_button("Añadir Subtítulos", self.add_subtitles, 100, 260, "blue")

        # Etiqueta de notificación
        self.notification_label = Label(self.master, text="", bg="white", font=("arial", 12))
        self.notification_label.place(x=250, y=350, width=300, height=30)

        # Atributos para almacenar rutas de archivos
        self.selected_video = None
        self.vp8_file = None
        self.vp9_file = None

    def create_button(self, text, command, x, y, color):
        button = Button(self.master, text=text, command=command, bg=color)
        button.place(x=x, y=y, width=200, height=30)
        return button

    def show_resolution_window(self):
        # Primero, solicitar al usuario que seleccione un video
        file_types = [("MP4 files", "*.mp4"), ("All files", "*.*")]
        self.selected_video = filedialog.askopenfilename(title="Seleccionar Video", filetypes=file_types)

        if not self.selected_video:
            self.show_notification("Por favor, selecciona un video primero.")
            return

        resolution_window = Tk()
        resolution_window.title("Seleccionar Resolución")
        resolution_window.configure(bg="blue")

        Label(resolution_window, text="Selecciona la resolución:", bg="blue", fg="white").pack(pady=10)

        resolutions = ["720p", "480p", "360x240", "160x120"]
        resolution_var = StringVar(resolution_window)
        resolution_var.set(resolutions[0])

        resolution_menu = OptionMenu(resolution_window, resolution_var, *resolutions)
        resolution_menu.pack(pady=10)

        confirm_button = Button(resolution_window, text="Confirmar", command=lambda: self.process_resolution(resolution_var.get(), resolution_window),
                                bg="blue", fg="white")
        confirm_button.pack(pady=10)

        resolution_window.mainloop()

    def process_resolution(self, resolution, resolution_window):
        output_resolution = f"output_{resolution}.mp4"
        cmd_resolution = [
            'ffmpeg',
            '-i', self.selected_video,
            '-vf', f'scale={resolution}',
            '-c:a', 'copy',
            output_resolution
        ]
        subprocess.run(cmd_resolution)

        self.show_notification(f"Video convertido a {resolution}: {output_resolution}")
        resolution_window.destroy()

    def show_format_window(self):
        format_window = Tk()
        format_window.title("Seleccionar Formato")
        format_window.configure(bg="green")

        Label(format_window, text="Selecciona el formato:", bg="green", fg="white").pack(pady=10)

        formats = ["VP8", "VP9", "H.265"]
        format_var = StringVar(format_window)
        format_var.set(formats[0])

        format_menu = OptionMenu(format_window, format_var, *formats)
        format_menu.pack(pady=10)

        confirm_button = Button(format_window, text="Confirmar", command=lambda: self.process_format(format_var.get(), format_window),
                                bg="green", fg="white")
        confirm_button.pack(pady=10)

        format_window.mainloop()

    def process_format(self, video_format, format_window):
        if not self.selected_video:
            self.show_notification("Por favor, selecciona un video primero.")
            format_window.destroy()
            return

        output_format = f"output_{video_format.lower()}.mp4"
        cmd_format = [
            'ffmpeg',
            '-i', self.selected_video,
            '-c:v', f'lib{video_format.lower()}',
            '-c:a', 'aac',
            output_format
        ]
        subprocess.run(cmd_format)

        self.show_notification(f"Video convertido a {video_format}: {output_format}")
        format_window.destroy()

    def show_comparison_window(self):
        comparison_window = Tk()
        comparison_window.title("Comparar Videos")
        comparison_window.configure(bg="red")

        Label(comparison_window, text="Selecciona el video VP8:", bg="red", fg="white").pack(pady=10)
        vp8_button = Button(comparison_window, text="Seleccionar VP8 Video", command=lambda: self.select_video('vp8', comparison_window),
                            bg="red", fg="black")
        vp8_button.pack(pady=10)

        Label(comparison_window, text="Selecciona el video VP9:", bg="red", fg="white").pack(pady=10)
        vp9_button = Button(comparison_window, text="Seleccionar VP9 Video", command=lambda: self.select_video('vp9', comparison_window),
                            bg="red", fg="white")
        vp9_button.pack(pady=10)

        confirm_button = Button(comparison_window, text="Comparar", command=self.process_comparison,
                                bg="red", fg="white")
        confirm_button.pack(pady=10)

        comparison_window.mainloop()

    def select_video(self, codec, window):
        file_types = [("WebM files", "*.webm"), ("MP4 files", "*.mp4"), ("All files", "*.*")]
        file_path = filedialog.askopenfilename(title=f"Select {codec.upper()} Video", filetypes=file_types)

        if codec == 'vp8':
            self.vp8_file = file_path
            self.show_notification("VP8 video selected")
        elif codec == 'vp9':
            self.vp9_file = file_path
            self.show_notification("VP9 video selected")

        window.destroy()

    def process_comparison(self):
        try:
            self.vp8_file
            self.vp9_file
        except AttributeError:
            self.show_notification("Please select both VP8 and VP9 videos.")
            return

        output_comparison = 'split_screen_comparison.mp4'

        create_split_screen(self.vp8_file, self.vp9_file, output_comparison)

        self.show_notification("Comparison video created: split_screen_comparison.mp4")

    def add_subtitles(self):
        subtitle_window = Tk()
        subtitle_window.title("Añadir Subtítulos")
        subtitle_window.configure(bg="purple")

        Label(subtitle_window, text="Selecciona el video:", bg="purple", fg="white").pack(pady=10)
        video_button = Button(subtitle_window, text="Seleccionar Video", command=self.select_video_for_subtitles,
                              bg="purple", fg="white")
        video_button.pack(pady=10)

        Label(subtitle_window, text="Selecciona el archivo de subtítulos:", bg="purple", fg="white").pack(pady=10)
        subtitle_button = Button(subtitle_window, text="Seleccionar Subtítulos", command=self.select_subtitles_file,
                                 bg="purple", fg="white")
        subtitle_button.pack(pady=10)

        confirm_button = Button(subtitle_window, text="Añadir Subtítulos", command=self.process_subtitles,
                                bg="purple", fg="white")
        confirm_button.pack(pady=10)

        subtitle_window.mainloop()

    def select_video_for_subtitles(self):
        file_types = [("MP4 files", "*.mp4"), ("All files", "*.*")]
        self.selected_video = filedialog.askopenfilename(title="Seleccionar Video", filetypes=file_types)

    def select_subtitles_file(self):
        file_types = [("SubRip files", "*.srt"), ("All files", "*.*")]
        self.subtitle_file = filedialog.askopenfilename(title="Seleccionar Archivo de Subtítulos", filetypes=file_types)

    def process_subtitles(self):
        if not self.selected_video or not self.subtitle_file:
            self.show_notification("Please select both video and subtitles.")
            return

        output_file_path = filedialog.asksaveasfilename(defaultextension=".mp4", filetypes=[("MP4 files", "*.mp4")])

        if not output_file_path:
            self.show_notification("Please select a location to save the video with subtitles.")
            return

        subtitle_processor = SubtitleProcessor(self.selected_video, output_file_path, self.subtitle_file)
        subtitle_processor.add_subtitles()

        self.show_notification("Subtitles added to the video.")

    def show_notification(self, message):
        self.notification_label.config(text=message)
        self.master.after(2000, lambda: self.notification_label.config(text=""))  # Elimina el mensaje después de 2 segundos

    def execute(self):
        self.master.mainloop()


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
    root = Tk()
    gui = VideoProcessorGUI(root)
    gui.execute()


if __name__ == "__main__":
    ejecutar()






