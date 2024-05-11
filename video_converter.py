from file_dialog import FileDialog
from save_dialog import SaveDialog
from pathlib import Path
import subprocess

class VideoConverter:
    def convert_video_to_audio(self, video_file, save_file):
        video = Path(video_file)
        if video.exists() and video.suffix.lower() == '.mp4':
            audio_file = Path(save_file)
            subprocess.run(['ffmpeg', '-i', str(video), '-vn', str(audio_file)], capture_output=True, text=True)
            if audio_file.exists():
                print(f'Аудио файл {audio_file} успешно создан.')
            else:
                print('Что-то пошло не так при конвертации видео в аудио.')
        else:
            print('Указанный файл не существует или не является видео файлом формата MP4.')

    def choose_file_and_convert(self):
        file_dialog = FileDialog()
        file_path = file_dialog.choose_file()
        if file_path:
            save_dialog = SaveDialog()
            save_path = save_dialog.choose_save_location()
            if save_path:
                self.convert_video_to_audio(file_path, save_path)

if __name__ == "__main__":
    converter = VideoConverter()
    converter.choose_file_and_convert()
