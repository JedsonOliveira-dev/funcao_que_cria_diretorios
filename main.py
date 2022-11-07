from tkinter import filedialog
from os import path, mkdir

caminho_diretorio = ''


def cria_diretorio():
    global caminho_diretorio
    caminho = filedialog.askdirectory()
    caminho += r'/Diretorio criado/'
    caminho_diretorio = caminho
    if not path.exists(str(caminho)):
        return mkdir(caminho)
    else:
        pass


cria_diretorio()
print(str(caminho_diretorio))
