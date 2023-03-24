import pyautogui
import time

#Registrando Usuário Pedro
pyautogui.click(660,444,duration=3)
pyautogui.click(672,385,duration=1)
pyautogui.write("Pedro")

time.sleep(1)

pyautogui.click(672,410,duration=1)
pyautogui.write("123456")

time.sleep(1)

pyautogui.click(614,440,duration=2)


#Logando no Usuário Pedro
pyautogui.click(671,384,duration=1)
pyautogui.write("Pedro")

time.sleep(1)

pyautogui.click(670,411,duration=1)
pyautogui.write("123456")

time.sleep(1)
pyautogui.click(597,440,duration=1)


#Dividindo o arquivo produtos.txt 
with open('produtos.txt','r') as file:
    for l in file:
        nome_produto = l.split(',')[0]
        qtd_produto = l.split(',')[1]
        preco_produto = l.split(',')[2]

        #Registrando os valores
        pyautogui.click(387,372,duration=1)
        pyautogui.write(nome_produto)

        pyautogui.click(387,398,duration=1)
        pyautogui.write(qtd_produto)

        pyautogui.click(386,424,duration=1)
        pyautogui.write(preco_produto)

        pyautogui.click(312,582,duration=2)

        time.sleep(1)





