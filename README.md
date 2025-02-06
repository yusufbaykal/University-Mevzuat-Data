# Turkey University Regulation Data Collection

This repository automates the collection of regulatory documents from Turkish universities as listed on mevzuat.gov.tr. The project employs web scraping technologies such as Selenium and BeautifulSoup to retrieve data, which is then exported in JSON and CSV formats.

## Overview

- **Data Sources:** mevzuat.gov.tr website  
- **Technologies Used:** Selenium, BeautifulSoup, Python  
- **Data Formats:** JSON, CSV

## Project Workflow

1. **University Data Extraction**  
   - Scrapes University IDs and Names.
   - Data is saved in `university_id.json`.

2. **Regulatory Link Collection**  
   - Filters and collects regulatory document links (years 2000–2024) for each university.
   - Links and corresponding university names are stored in `mevzuat_links.csv`.

3. **Content Extraction**  
   - Opens each regulatory link to extract full document content and Official Gazette details.
   - The extracted information is saved in `mevzuat_content.csv`.

## Mevzuat Content CSV Data Structure

This dataset provides a comprehensive collection of regulatory documents of Turkish universities obtained from mevzuat.gov.tr. 
It includes full texts of regulations with detailed publication information and unique identifiers.

| Column                 | Description                                                 |
|------------------------|-------------------------------------------------------------|
| **Üniversite**         | Name of the university.                                     |
| **Link**               | URL to the regulatory document.                             |
| **İçerik**            |  Full text of the regulation.                                |
| **Resmi Gazete Tarihi** | Date when the regulation was published.                  |
| **Resmi Gazete Sayısı** | Publication number of the regulation.                  |
| **Mevzuat No**         | Unique regulation identifier.                               |

### Example Record

- **Üniversite:** Abdullah Gül Üniversitesi  
- **Link:** [Regulation Document](https://www.mevzuat.gov.tr/mevzuat?MevzuatNo=39034&MevzuatTur=8&MevzuatTertip=5)  
- **İçerik:** Regulation details including purpose, scope, legal basis, and definitions.  
- **Resmi Gazete Tarihi:** 07.11.2021  
- **Resmi Gazete Sayısı:** 31652  
- **Mevzuat No:** 39034

### Citation Information

```
@dataset{turkish-university-mevzuat,
  author = {Yusuf Baykaloğlu},
  title = {Turkey University Regulation Data},
  year = {2024},
  url = {https://huggingface.co/datasets/yusufbaykaloglu/turkish-university-mevzuat}
}
```
## Contributions and Support

For any questions or feedback, please contact:

- **Author**: Yusuf Baykaloğlu  
- [Email](mailto:yusuff.baykaloglu@gmail.com)
