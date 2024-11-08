import json
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
import time


with open('data/university_id.json', 'r', encoding='utf-8') as f:
    university_data = json.load(f)

driver = webdriver.Chrome()
driver.get("https://www.mevzuat.gov.tr/#kurumKurulusVeUniversiteYonetmelikleri")

search_area_selects = driver.find_elements(By.ID, "AranacakYer")
search_area_select_obj = Select(search_area_selects[11])
search_area_select_obj.select_by_visible_text("Tümü")
time.sleep(2)

mevzuat_select = driver.find_element(By.ID, "kurumKurulusVeUniversiteYonetmelikleri_yonetmelikMevzuatTur")
mevzuat_select_obj = Select(mevzuat_select)
mevzuat_select_obj.select_by_visible_text("Üniversite Yönetmelikleri")
time.sleep(2)

data = []

for university_id, university_name in university_data.items():

    universite_select = driver.find_element(By.ID, "kurumKurulusVeUniversiteYonetmelikleri_universiteId")
    universite_select_obj = Select(universite_select)
    universite_select_obj.select_by_value(university_id)
    time.sleep(2)

    baslangic_selects = driver.find_elements(By.ID, "BaslangicTarihi")
    baslangic_select_obj = Select(baslangic_selects[9])
    baslangic_select_obj.select_by_value("2000")
    time.sleep(2)

    bitis_selects = driver.find_elements(By.ID, "BitisTarihi")
    bitis_select_obj = Select(bitis_selects[9])
    bitis_select_obj.select_by_value("2024")
    time.sleep(2)

    search_buttons = driver.find_elements(By.ID, "btnSearch")
    search_buttons[9].click()
    time.sleep(2)

    records_per_page = driver.find_element(By.CSS_SELECTOR, "select.custom-select.custom-select-sm.form-control")
    select = Select(records_per_page)
    select.select_by_value("100")
    time.sleep(10)

    links = driver.find_elements(By.CSS_SELECTOR, "a.ml-1")
    for link in links:
        data.append({"Üniversite": university_name, "Link": link.get_attribute("href")})

df = pd.DataFrame(data)
df.to_csv('data/mevzuat_links.csv', index=False)