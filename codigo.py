# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
import pyautogui
import time

pyautogui.PAUSE = 0.5

# abrir o navegador
# apertar a tecla win
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link: https://dlp.hashtagtreinamentos.com/python/intensivao/login



# Passo 2: fazer login
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# dar uma pausa de 3 segundos
time.sleep(3)
pyautogui.click(x=620, y=423)
pyautogui.write("testepythonteste@gmail.com")

# passar para o proximo campo
pyautogui.press("tab")
pyautogui.write("minhasenha")

# apertar botão de login
pyautogui.press("tab")
pyautogui.press("enter")
time.sleep(2)



# Passo 3: Importar a base de dados
import pandas as pd

tabela = pd.read_csv("produtos.csv")
print(tabela)


# Passo 4: Cadastrar produtos
for linha in tabela.index:

    # selecionar o primeiro produto
    pyautogui.click(x=578, y=312)

    # codigo
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(str(codigo))
    pyautogui.press("tab")

    # marca
    marca = tabela.loc[linha, "marca"]
    pyautogui.write(str(marca))
    pyautogui.press("tab")

    # tipo
    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(str(tipo))
    pyautogui.press("tab")

    # categoria
    categoria = tabela.loc[linha, "categoria"]
    pyautogui.write(str(categoria))
    pyautogui.press("tab")

    # preco unitario
    preco = tabela.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco))
    pyautogui.press("tab")

    # custo
    custo = tabela.loc[linha, "custo"]
    pyautogui.write(str(custo))
    pyautogui.press("tab")

    # obs
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))
    pyautogui.press("tab")

    # clickar em enviar
    pyautogui.press("enter")
    pyautogui.scroll(5000)

# Passo 5: Repetir o processo de cadastro ate acabar os produtos