from tkinter import Tk, filedialog

class FileDialog:
    def choose_file(self):
        root = Tk()
        root.withdraw()  # скрыть главное окно
        file_path = filedialog.askopenfilename(title="Выберите видеофайл", filetypes=[("Video Files", "*.mp4")])
        root.destroy()  # закрыть окно после выбора файла
        return file_path
