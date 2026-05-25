# https://ge.globo.com - > https://ge.globo.com/futebol/brasileirao-serie-a/
# menu -> tabelas -> nacionais -> brasileirão série a -> 14a rodada = Botafogo 1 - 2 Remo
# $ pip install selenium webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

servico = Service(ChromeDriverManager().install())
navegador = webdriver.Chrome(service=servico)

try:
    # 2. Abre o site
    navegador.get("https://ge.globo.com/futebol/brasileirao-serie-a/")

    botaomenu = driver.find_element(By.CLASS_NAME, "placar-box_valor placar-box_valor-mandante")
    botaomenu.click()

    # 3. Encontra a barra de pesquisa (inspecionando o HTML, o nome é 'q')
    #caixa_busca = navegador.find_element(By.NAME, "MENU")

    # 4. Digita e dá Enter
    #caixa_busca.send_keys("Python Selenium" + Keys.RETURN)

    # 5. Espera um pouco para o conteúdo carregar
    time.sleep(10)

    # 6. Captura os títulos dos resultados
    #resultados = navegador.find_elements(By.TAG_NAME, "")

finally:
    # 7. Fecha o navegador
    navegador.quit()