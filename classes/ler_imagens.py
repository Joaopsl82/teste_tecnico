import pytesseract, os, re
import pandas as pd
from PIL import Image
from datetime import datetime

class ImageToTexto:
    def ler_texto(self, image_path):
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        img = Image.open(image_path)
        texto = pytesseract.image_to_string(img)
        return texto
    
    def extrair_faturas_datas(self, texto):
        fatura = re.compile(r'Invoice #(\d+)')
        data = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
        faturas = fatura.findall(texto)
        datas = data.findall(texto)
        return faturas, datas
    
    def arquivos(self):
        caminho_pasta = 'Faturas'
        data = []
        for caminho_nome in os.listdir(caminho_pasta):
            caminho_arquivo = os.path.join(caminho_pasta, caminho_nome)
            if os.path.isfile(caminho_arquivo):
                text = self.ler_texto(caminho_arquivo)
                if text:
                    invoices, dates = self.extrair_faturas_datas(text)
                    for invoice, date in zip(invoices, dates): 
                        data.append({
                            'Numero da fatura': invoice,
                            'Data da fatura': date,
                            'URL da fatura': f'https://rpachallengeocr.azurewebsites.net/invoices/{caminho_nome}'
                        })
        data_atual = datetime.now().strftime('%d%m%Y')
        df = pd.DataFrame(data)
        csv_file = f'dados_faturas{data_atual}.csv'
        df.to_csv(csv_file, index=False, encoding='utf-8')
