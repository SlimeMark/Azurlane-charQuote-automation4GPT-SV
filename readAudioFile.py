import os
import time
import glob
import tkinter as tk
from tkinter import filedialog


def read_audio_file():
    print('\033[93m' + '在弹出的窗口中选择音频文件夹')
    time.sleep(1)
    root = tk.Tk()
    root.withdraw()
    folder_path = filedialog.askdirectory()
    extension = '*.wav'
    file_list = []
    for file in glob.glob(os.path.join(folder_path, extension)):
        file_list.append(file)

    return file_list
