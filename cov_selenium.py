from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time
import re
import pandas as pd

for i in range(0, 8):
    browser = webdriver.Chrome(ChromeDriverManager().install())
    browser.get(f"https://www.mai.gov.ro/informare-covid-19-grupul-de-comunicare-strategica-2{i}-ianuarie-ora-13-00/")
    browser.maximize_window()
    table = browser.find_element(By.TAG_NAME, 'tbody')
    table_text = table.text
    header = browser.find_element(By.TAG_NAME, 'tr').text
    header_list = re.findall('[A-Z][^A-Z]*', header)
    lista = table_text.split('\n')
    lista_aux = []
    for item, value in enumerate(lista):
        if item > 0:
            new_value = value.split(' ')
            if item == 32 or item == 42:
                new_value[1:3] = [' '.join(new_value[1:3])]     # Satu Mare si Mun. Bucuresti
            if item == 43:
                new_value[1:6] = [' '.join(new_value[1:6])]     # Cazurile totale
            for item2 in new_value:
                lista_aux.append(item2)
    lista_noua = header_list + lista_aux
    if header_list[0].startswith("Nr"):
        dictionar = {
            j: [] for j in header_list
        }
        for k in range(0, len(header_list)):
            if k == 0:
                dictionar[header_list[int(k)]].append(f"2{i} ianuarie 2021")
            else:
                dictionar[header_list[int(k)]].append('')
            for j in range(len(header_list) + int(k), len(lista_noua[0:220]), len(header_list)):
                dictionar[header_list[int(k)]].append(lista_noua[j])
            dictionar[header_list[int(k)]].append('')
        time.sleep(5)
        df = pd.DataFrame(dictionar)
        df.to_csv("date_covid.csv", mode='a', encoding='utf-8-sig', index=False)
    else:
        print("\nNu exista date in ziua respectiva")
