import pyautogui
import time
import pandas

pyautogui.PAUSE = 1
pyautogui.press("win")
pyautogui.write("google chrome")
pyautogui.press("enter")


pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

time.sleep(2)

pyautogui.click(x=717, y=408)
pyautogui.hotkey("ctrl", "a")
pyautogui.write("email@gmail.com")
pyautogui.press("tab")
pyautogui.write("testando123@")
pyautogui.click(x=959, y=572)

time.sleep(2)

tabelaExcel = pandas.read_csv("produtos (1).csv")

print(tabelaExcel)


for linha in tabelaExcel.index:

    pyautogui.click(x=698, y=290)
    codigo = tabelaExcel.loc[linha, "codigo"]
    pyautogui.write(str(codigo))

    pyautogui.press("tab")
    marca = tabelaExcel.loc[linha, "marca"]
    pyautogui.write(str(marca))

    pyautogui.press("tab")
    tipo = tabelaExcel.loc[linha, "tipo"]
    pyautogui.write(str(tipo))

    pyautogui.press("tab")
    categoria = tabelaExcel.loc[linha, "categoria"]
    pyautogui.write(str(categoria))

    pyautogui.press("tab")
    preco_unitario = tabelaExcel.loc[linha, "preco_unitario"]
    pyautogui.write(str(preco_unitario))

    pyautogui.press("tab")
    custo = tabelaExcel.loc[linha, "custo"]
    pyautogui.write(str(custo))

    
    pyautogui.press("tab")
    obs = str(tabelaExcel.loc[linha, "obs"])
    if obs != "nan":
        pyautogui.write(obs)

    pyautogui.click(x=843, y=940)


    pyautogui.scroll(5000)