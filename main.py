import pytube
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog

def download_and_convert_to_mp4():
    url = url_entry.get()
    output_directory = output_directory_entry.get()
    
    try:
        yt = pytube.YouTube(url)

        video_stream = yt.streams.filter(progressive=True, file_extension='mp4').get_highest_resolution()

        video_stream.download(output_path=output_directory)
        
        result_label.config(text="Download concluído.")
    except Exception as e:
        result_label.config(text=f"Ocorreu um erro: {e}")

def select_output_directory():
    directory = filedialog.askdirectory()
    output_directory_entry.delete(0, tk.END)
    output_directory_entry.insert(0, directory)

root = tk.Tk()
root.title("Download de Vídeo do YouTube")

url_label = ttk.Label(root, text="URL do vídeo do YouTube:")
url_label.pack(pady=10)
url_entry = ttk.Entry(root, width=40)
url_entry.pack()

output_directory_label = ttk.Label(root, text="Diretório de saída:")
output_directory_label.pack(pady=10)
output_directory_entry = ttk.Entry(root, width=40)
output_directory_entry.pack()
output_directory_button = ttk.Button(root, text="Selecionar Diretório", command=select_output_directory)
output_directory_button.pack()

download_button = ttk.Button(root, text="Baixar e Converter", command=download_and_convert_to_mp4)
download_button.pack(pady=20)

result_label = ttk.Label(root, text="")
result_label.pack()

root.mainloop()
