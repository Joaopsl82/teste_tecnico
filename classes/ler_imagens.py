import pytesseract, os, re
import pandas as pd
from PIL import Image
from datetime import datetime

class ImageToTexto:
    # Passo 3: Ler textos das imagens para montar o CSV
    def read_text(self, image_path):
        pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'
        img = Image.open(image_path)
        texto = pytesseract.image_to_string(img)
        return texto
    
    def extract_invoice_and_date(self, text):
        fatura = re.compile(r'Invoice #(\d+)')
        data = re.compile(r'\b\d{4}-\d{2}-\d{2}\b')
        faturas = fatura.findall(text)
        datas = data.findall(text)
        return faturas, datas
    
    def arquivos(self):
        caminho_arquivo = 'Faturas'
        data = []
        for nome_arquivo in os.listdir(caminho_arquivo):
            caminho_arquivo = os.path.join(caminho_arquivo, nome_arquivo)
            if os.path.isfile(caminho_arquivo):
                text = self.read_text(caminho_arquivo)
                if text:
                    faturas, datas = self.extract_invoice_and_date(text)
                    for fatura, data in zip(faturas, datas): 
                        data.append({
                            'Numero da fatura': fatura,
                            'Data da fatura': data,
                            'URL da fatura': f'https://rpachallengeocr.azurewebsites.net/invoices/{nome_arquivo}'
                        })
        data_atual = datetime.now().strftime('%d%m%Y')
        df = pd.DataFrame(data)
        arquivo_csv = f'dados_faturas{data_atual}.csv'
        df.to_csv(arquivo_csv, index=False, encoding='utf-8')