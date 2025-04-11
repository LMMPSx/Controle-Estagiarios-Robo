import pyautogui
import time
import pyperclip

# abre o google e seleciona a aba certa
pyautogui.click(1205, 1059, duration=0.5)
pyautogui.click(629,17, duration=0.5)

# seleciona a primeira célula e copia
pyautogui.click(276,387, duration=0.5)
pyautogui.hotkey('ctrl', 'c')
nome_escola = pyperclip.paste()

while nome_escola != '-':

    # vai para o drive e pesquisa a célula copiada e apaga a pesquisa anterior
    pyautogui.click(395,17, duration=0.5)
    pyautogui.click(316,150, duration=0.5)
    pyautogui.hotkey('ctrl', 'a')
    pyautogui.hotkey('backspace')
    pyautogui.write(f'title:"{nome_escola}"')
    time.sleep(1)
    pyautogui.hotkey('enter')

    # abre o primeiro resultado da pesquisa
    pyautogui.click(555,373, duration=3, clicks=2)
    pyautogui.click(866,19, duration=0.5)
    time.sleep(1)
 
    # ve quantos estagiários tem na escola e salva numa variavel
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)
    pyautogui.moveTo(1651,255, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.move(22,0,  duration=1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.mouseUp()
    x = pyperclip.paste()
    estagQTD = int(''.join([char for char in x if char.isdigit()]))
    pyautogui.click(1808, 255, duration=0.5)

    # +seleciona e copia todos os estagiarios da escola
    pyautogui.keyDown('shiftleft')
    pyautogui.keyDown('shiftright')
    pyautogui.hotkey('space')
    for i in range(estagQTD - 1):
        pyautogui.hotkey('down')
    pyautogui.keyUp('shiftleft')
    pyautogui.keyUp('shiftright')
    pyautogui.hotkey('ctrl', 'c')

    # cola as informações da Controle dos estagiarios e cola na pasta da escola
    pyautogui.click(633,18, duration=0.5)
    pyautogui.click(276,405, duration=0.5)
    pyautogui.hotkey('ctrl', 'v')
    time.sleep(1)

    # ve quantos estagiários tem na PASTA da escola e salva numa variavel
    pyautogui.hotkey('ctrl', 'f')
    pyautogui.write(nome_escola)
    time.sleep(1)
    pyautogui.moveTo(1652,255, duration=0.5)
    pyautogui.mouseDown()
    pyautogui.move(22,0,  duration=1)
    pyautogui.hotkey('ctrl', 'c')
    time.sleep(1)
    pyautogui.mouseUp()
    y = pyperclip.paste()
    escolaQTD = int(''.join([char for char in y if char.isdigit()]))
    pyautogui.click(1808, 255, duration=0.5)


    # apaga a diferença de estagiários
    diff = escolaQTD - estagQTD

    if diff <= 0:
        pyautogui.click(728,19, duration=0.5)
    else:
        for i in range(escolaQTD - diff):
            pyautogui.hotkey('down')

        pyautogui.keyDown('shiftleft')
        pyautogui.keyDown('shiftright')
        pyautogui.hotkey('space')
        for i in range(diff):
            pyautogui.hotkey('backspace')
            pyautogui.hotkey('down')
        pyautogui.keyUp('shiftleft')
        pyautogui.keyUp('shiftright')
        pyautogui.click(728,19, duration=0.5)
        
            
    # passa para o próximo
    pyautogui.click(866,19, duration=0.5)
    for i in range(estagQTD):
        pyautogui.hotkey('down')

    # seleciona a primeira célula e copia
    pyautogui.hotkey('ctrl', 'c')
    nome_escola = pyperclip.paste()