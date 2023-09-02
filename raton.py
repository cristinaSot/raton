
import pyautogui
import time

while True:
    # Obtener la posición actual del ratón
    x, y = pyautogui.position()

    # Mover el ratón a una nueva posición
    pyautogui.moveTo(x + 10, y + 10, duration=1)

    # Esperar 10 segundos
    time.sleep(10)