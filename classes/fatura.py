import requests, os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
from time import sleep
from datetime import datetime

class RPA:

    service = Service(ChromeDriverManager().install())
    opts = webdriver.ChromeOptions()
    driver = webdriver.Chrome(service=service, options=opts)
    driver.maximize_window()
    driver.get('https://rpachallengeocr.azurewebsites.net/')

    def __init__(self):
            if not os.path.exists('Faturas'):
                os.makedirs('Faturas')

    def acessando_dados(self):
        data_atual = datetime.now()
        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        table = soup.find('table', id='tableSandbox')
        tbody = table.find('tbody')
        linhas = tbody.find_all('tr')
        validar_hrefs = []
        for linha in linhas:
            colunas = linha.find_all('td')
            date_str = colunas[2].get_text(strip=True)
            href = colunas[3].find('a').get('href')
            try:
                linha_data = datetime.strptime(date_str, '%d-%m-%Y')            
                if linha_data <= data_atual:
                    validar_hrefs.append(href)
            except ValueError:
                continue

        for href in validar_hrefs:
            url_imagem = f'https://rpachallengeocr.azurewebsites.net{href}'
            self.download_image(url_imagem)
        return True
        

    def download_image(self, url_image):
        try:
            response = requests.get(url_image, stream=True)
            response.raise_for_status()
            
            nome_arquivo = os.path.basename(url_image)
            caminho_arquivo = os.path.join('Faturas', nome_arquivo)
            
            with open(caminho_arquivo, 'wb') as file:
                for chunk in response.iter_content(chunk_size=8192):
                    file.write(chunk)
        
        except requests.exceptions.RequestException as e:
            print('Erro ao baixar a imagem')
            
    def obter_dados_proxima_pagina(self):
        while True:
            if self.acessando_dados() is True:
                botao_proximo = self.driver.find_element(By.ID, 'tableSandbox_next')
                if "disabled" in botao_proximo.get_attribute('class'):
                    break
                botao_proximo.click()
                sleep(2)
        return True