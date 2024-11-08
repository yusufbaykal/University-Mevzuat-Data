from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup
import json
import time

driver = webdriver.Chrome()
url = "https://mevzuat.gov.tr/#kurumKurulusVeUniversiteYonetmelikleri"
driver.get(url)

time.sleep(3)

select_element = driver.find_element(By.ID, "kurumKurulusVeUniversiteYonetmelikleri_universiteler")
html_content = select_element.get_attribute('outerHTML')

soup = BeautifulSoup(html_content, 'html.parser')
universities = soup.find_all('option')

university_dict = {}
for option in universities:
    university_id = option.get('value')
    university_name = option.text.strip()
    if university_id != "0":
        university_dict[university_id] = university_name

with open("university_id.json", "w", encoding="utf-8") as f:
    json.dump(university_dict, f, ensure_ascii=False, indent=4)

driver.quit()