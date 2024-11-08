import pandas as pd

def csv_to_txt():
  data = pd.read_csv('Data/mevzuat_content.csv')
  icerik = data['İçerik']

  icerik_text = ""
  for item in icerik:
      icerik_text += item

  with open('Data/icerik.txt', 'w', encoding='utf-8') as file:
      file.write(icerik_text)
      
csv_to_txt()