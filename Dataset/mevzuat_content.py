from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from urllib.parse import urlparse, parse_qs
import pandas as pd
import csv

chrome_options = Options()
chrome_options.add_argument("--headless")

driver = webdriver.Chrome(options=chrome_options)

input_csv_file = "data/mevzuat_links.csv"
output_csv_file = "data/mevzuat_content.csv"
output_data = []  


with open(input_csv_file, "r", encoding="utf-8") as file:
    reader = csv.DictReader(file)
    for row in reader:
        university = row['Üniversite']
        link = row['Link']
        parsed_url = urlparse(link)
        mevzuat_no = parse_qs(parsed_url.query).get('MevzuatNo', [None])[0]

        driver.get(link)

        try:
            iframe = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.ID, "mevzuatDetayIframe"))
            )
            driver.switch_to.frame(iframe)

            content = driver.find_element(By.TAG_NAME, "body").text

            driver.switch_to.default_content()
            
            resmi_gazete_bilgisi = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, "font-italic.small.ml-3.mr-3"))
            ).text

            tarih = resmi_gazete_bilgisi.split("Resmî Gazete Tarihi: ")[1].split(" Resmî Gazete Sayısı: ")[0]
            sayi = resmi_gazete_bilgisi.split("Resmî Gazete Sayısı: ")[1]

            output_data.append({
                'Üniversite': university,
                'Link': link,
                'İçerik': content,
                'Resmi Gazete Tarihi': tarih,
                'Resmi Gazete Sayısı': sayi,
                'Mevzuat No': mevzuat_no
            })

        except Exception as e:
            print(f"Link Hatalı {link}: {e}")


df = pd.DataFrame(output_data)
df.to_csv(output_csv_file, index=False)

driver.quit()
