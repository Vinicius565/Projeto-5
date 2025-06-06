import pyautogui
import time
import pandas


#pyautogui.click -> clicar em algum lugar
#pyautogui.press -> apertar 1 tecla
#pyautogui.write -> escrever um texto
#pyautogui.hotkey -> apertar uma combinação de teclas

pyautogui.PAUSE = 0.7

# Passo 1: entra no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login

pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

#digitar e entrar no site
pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera por 3s
time.sleep(3)

# Passo 2: fazer login
pyautogui.click(x=2691, y=736)
pyautogui.write("avalug@gmailcom")
pyautogui.press("tab")
pyautogui.write("121313")
pyautogui.click(x=2541, y=896)

#espera de 3s
time.sleep(3)

# Passo 3: Importar a base de dados
tabela = pandas.read_csv("produtos.csv")
print(tabela)

# Passo 4: cadastrar 1 produto
for linha in tabela.index:

    pyautogui.click(x=2437, y=625)
    codigo = tabela.loc[linha, "codigo"]
    pyautogui.write(codigo)

    pyautogui.press("tab")

    marca = tabela.loc[linha, "marca"]
    pyautogui.write(marca)

    pyautogui.press("tab")

    tipo = tabela.loc[linha, "tipo"]
    pyautogui.write(tipo)

    pyautogui.press("tab")

    categoria = str(tabela.loc[linha, "categoria"])
    pyautogui.write(categoria)

    pyautogui.press("tab")

    preco_unitario = str(tabela.loc[linha, "preco_unitario"])
    pyautogui.write(preco_unitario)

    pyautogui.press("tab")

    custo = str(tabela.loc[linha, "custo"])
    pyautogui.write(custo)

    pyautogui.press("tab")

    obs = str(tabela.loc[linha, "obs"])
    pyautogui.write(obs)

    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(100000)
# Passo 5: repetir para todos os produtos


