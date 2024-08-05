<h1>Para o funcionamento do Código</h1>

Para esse projeto funcionar precisamos fazer alguns passos:

<b>1º Passo: Instalar as bibliotecas</b><br><br>
Para podermos instalar as bibliotecas Python necessárias usamos o comando pip install + nome da biblioteca<br>
As bibliotecas que foram utilizadas para esse projeto são:<br>
<b>requests, selenium, webdriver-manager, BeautifulSoup, pandas e pilow</b>

<b>2º Passo: Possível problema na biblioteca webdriver-manager</b><br><br>
Caso rode o código e apareça a seguinte mensagem <b>"oserror: [winerror 193] %1 não é um aplicativo win32 válido"</b> pode ocorrer por conta
do webdriver-manager estar gerando arquivos além do "chromedriver.exe". Para resolver o problema precisamos remover esses dois arquivos.<br>
Normalmente esse arquivo se localiza no caminho: <b>C:\Users\User\.wdm\drivers\chromedriver\win64\127.0.6533.72\chromedriver-win32</b> onde "User" é
o nome do usuário da seu computador. <br>Os arquivos que precisam ser excluídos são:
<br>LICENSE.chromedriver e THIRD_PARTY_NOTICES.chromedriver</b><br>
Se mesmo ao remover ainda estiver aparecendo a mensagem no código no lugar da linha <b>service = Service(ChromeDriverManager().install())</b> vamos alterar
para <b>C:\\Users\\User\\.wdm\\drivers\\chromedriver\\win64\\127.0.6533.72\\chromedriver-win32\\chromedriver.exe</b> sempre se atentando a alterar o nome do 
"USER" para o nome do seu usuário.

<b>3º Passo: Instalação do Pytesseract</b><br><br>
Caso o script vá ser rodado em um ambiente Windows precisamos baixar um arquivo do tesseract antes de instalá-lo via python. Para isso vamos acessar a URL:
<a>https://github.com/UB-Mannheim/tesseract/releases/download/v5.4.0.20240606/tesseract-ocr-w64-setup-5.4.0.20240606.exe</a> assim que acessar a URL o download
irá começar, apenas devemos nos atentar em baixar no caminho "C:\Program Files\Tesseract-OCR\tesseract.exe".<br>
Depois de instalado, iremos rodar o comando pip install pytesseract e assim o script estará funcionando.

<br><br>Esses são os passos para o funcionamento 100% do código, muito obrigado pela atenção :) <br><br>

<h2>Para a execução do código utilizar o arquivo main.py</h2>
