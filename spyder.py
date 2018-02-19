from bs4 import BeautifulSoup
import requests

url = "https://www.rxlist.com/drugs/alpha_a.htm"
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html.parser')
lst = soup.find('div', attrs={'class': 'contentstyle'})
drug_list = lst.find_all('li')
for drug in drug_list:
    link = (drug.find('a'))
    name = drug.get_text()
    try:
        new_name = name.split("(")
        gen_name = new_name[0]
        new_name_again = new_name[1].split(")")
        class_name = new_name_again[0]
        prof_or_cns = new_name_again[1]
    except IndexError:
        print("Not Found")
    clean_link = link.get('href')
    main_link = "https://www.rxlist.com" + clean_link
    print("Generic Name - " + gen_name)
    print("Class Name - " + class_name)
    print("Professional or Consumer " + prof_or_cns)
    print("Information - " + main_link)

