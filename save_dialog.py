from tkinter import Tk, filedialog

class SaveDialog:
    def choose_save_location(self):
        root = Tk()
        root.withdraw()  # скрыть главное окно
        save_path = filedialog.asksaveasfilename(title="Выберите место сохранения аудиофайла", defaultextension=".mp3", filetypes=[("Audio Files", "*.mp3")])
        root.destroy()  # закрыть окно после выбора места сохранения
        return save_path
