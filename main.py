from classes.fatura import RPA
from classes.ler_imagens import ImageToTexto

def processar():
    rpa = RPA()
    img = ImageToTexto()
    
    if rpa.obter_dados_proxima_pagina() is True:
        img.arquivos()

processar()