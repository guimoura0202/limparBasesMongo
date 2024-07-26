import pyautogui
import time
import re
import pyperclip
import os
from dotenv import load_dotenv
load_dotenv()

# Função para deletar todas as base de dados
def delete_database():
    mongodb_uri = os.getenv('MONGODB_URI')
    database_name = os.getenv('DATABASE_NAME')
    caminho_mongo = os.getenv('CAMINHO_MONGO')
    #Abrir o MongoDBCompass
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('MongoDBCompass')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(5)
    # # Posição do botão "Connect"
    x = 1210
    y = 510
    pyautogui.click(x, y)
    time.sleep(1)
    # Posição do campo de pesquisa
    x = 300
    y = 335
    pyautogui.click(x, y)
    time.sleep(1)
    pyautogui.write(database_name)
    time.sleep(1)
    pyautogui.press('enter')
    # Posição do icone da lixeira
    x = 472
    y = 372
    #Antes de clicar passa o mouse por cima pra lixeira aparecer
    pyautogui.moveTo(x, y)
    time.sleep(1)
    pyautogui.click(x, y)
    time.sleep(1)

    # Informar o nome da base de dados para confirmar exclusão
    x = 768
    y = 557
    pyautogui.click(x, y)
    time.sleep(1)
    pyperclip.copy(database_name)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    # Posição do botão "Drop Database"
    x = 1177
    y = 620 
    pyautogui.click(x, y)

    # Abrir Prompt de Comando
    pyautogui.hotkey('win', 's')
    time.sleep(1)
    pyautogui.write('cmd')
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write('cd ' + caminho_mongo)
    time.sleep(1)
    pyautogui.press('enter')
    time.sleep(1)
    pyautogui.write(mongodb_uri)
    time.sleep(1)
    pyautogui.press('enter')

if __name__ == '__main__':
    delete_database()