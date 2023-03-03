#Importando dependências
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time

#Define a localização do Chromedrive.
driver = webdriver.Chrome('coloque aqui o seu diretório') 

#Abre o site em questão
driver.get('https://esaj.tjsp.jus.br/cpopg/open.do') 

#Espera um tempo para poder proceder
time.sleep(5)

#Define a opção 'Documento da parte'
cpf_webelement = driver.find_element(By.ID,'cbPesquisa') #Pesquisa a seleção de opções.
seleção = Select(cpf_webelement)
docparte = seleção.select_by_visible_text("Documento da Parte")
opção_escolhida = seleção.first_selected_option

#Pesquisar barra para digitar CPF.
barra_cpf = driver.find_element(By.ID, 'campo_DOCPARTE')

#Digitar o CPF na barra.
barra_cpf.send_keys('SEUCPF')

#Clica no botão "Consultar"
botão_consultar = driver.find_element(By.ID,'botaoConsultarProcessos')
botão_consultar.click()

#Consultar o resultado dentro do código fonte da página
código_fonte = driver.page_source
if 'Não existem informações disponíveis para os parâmetros informados.' in código_fonte:
    print("O CPF consultado não apresenta protestos.")
    
else:
    if 'Busca e Apreensão' in código_fonte:
        print("O CPF consultado apresenta processo de busca e apreensão")
    
    else: 
        print("O CPF consultado não apresenta processo de busca e apreensão")

driver.quit()



