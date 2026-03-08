import pyautogui
import time
import pandas as pd

pyautogui.PAUSE = 0.3
#Apertar tecla "Win";
pyautogui.press("win")

#Escrever Google;
pyautogui.write("Microsoft Edge")
#Apertar Enter;
pyautogui.press("enter")
time.sleep(3)

#Acessar o site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
#Cadastrar usuário
time.sleep(3)
pyautogui.press("tab")
pyautogui.write("teste@gmail.com.br")

pyautogui.press("tab")
pyautogui.write("123456789")
pyautogui.press("enter")
time.sleep(3)
pyautogui.press("tab")

#Cadastro de produto
#codigo,marca,tipo,categoria,preco_unitario,custo,obs 
tabela = pd.read_csv("produtos.csv")

for linha in tabela.index:
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    #marca = tabela.loc[linha, "marca"]
    #pyautogui.write(str(marca))
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")
    pyautogui.press("enter")
    pyautogui.press("pageup")
    pyautogui.click(x=639, y=359)