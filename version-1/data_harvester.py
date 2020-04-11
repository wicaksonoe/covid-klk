#!/usr/bin/env python
# coding: utf-8

# In[142]:


"""
Import library yang diperlukan
csv untuk membuat file csv nantinya
time untuk menggunakan fungsi time.sleep (suspend fungsi sebentar)
os.path untuk pengecekan file di akhir
datetime untuk menggunakan fungsi pengambilan tanggal dan waktu scrapping
selenium digunakan sebagai virtual browser, karena webpage tidak bisa hanya menggunakan library request,
    karena ada data yang lebih mudah diambil, tetapi berada di dalam javascript, jadi perlu eksekusi javascript
beautifulSoap adalah library web scrapping python yang di
"""

import csv 
import time
import os.path
import datetime as dt
from selenium import webdriver
from bs4 import BeautifulSoup


# In[143]:


browser = None
url = None
soup = None


# In[144]:


def init_browser():
    print("Getting website data")
    global browser, url, soup
    
    # pilih browser yang akan digunakan. disini saya menggunakan Firefox sebagai client browsernya
    browser = webdriver.Firefox()

    # masukan URL tujuan
    url = 'https://covid19.klungkungkab.go.id/'

    # buat request ke URL tujuan
    browser.get(url)

    # setelah browser selesai membukan URL, mulai parsing file htmlnya
    soup = BeautifulSoup(browser.page_source, "html.parser")


# In[145]:


"""
buat variabel nama file tujuan menyompan dataset
buat initial timestamp / waktu saat script dijalankan
"""

csv_file = "datasets_covid_klk.csv"
csv_row = {
    "timestamp": dt.datetime.utcnow().strftime("%Y-%m-%d %H:%M:%S %z")
}


# In[146]:


def get_banjarangkan_data(soup):
    print("Parsing Data Kecamatan Banjarangkan")
    
    # deklarasi kalau kita akan menggunakan variabel global
    global csv_row
    
    # buat dictionary kosong yang nantinya menampung data
    dict_banjarangkan_data = {}

    # mulai pencarian elemen yang mengandung data
    banjarangkan_table = soup.find_all(id="piechartKECAMATANBANJARANGKAN")
    banjarangkan_data = (banjarangkan_table[0]
     .contents[0]
     .contents[0]
     .contents[0]
     .contents[1]
     .contents[0]
     .contents[1]
     .contents)

    # memasukan hasil data yang diperoleh ke dictionary
    for data in banjarangkan_data:
        result = str(data.contents[0].contents[0]).split()
        dict_banjarangkan_data[result[0]] = result[1]

    # berdasarkan dictionary sebelumnya, kita masukan data-datanya ke dictionary CSV
    for x in dict_banjarangkan_data:
        if x == "ODP":
            csv_row["banjarangkan_odp"] = dict_banjarangkan_data[x]

        if x == "OTG":
            csv_row["banjarangkan_otg"] = dict_banjarangkan_data[x]

        if x == "PDP":
            csv_row["banjarangkan_pdp"] = dict_banjarangkan_data[x]

        if x == "Positif":
            csv_row["banjarangkan_positif"] = dict_banjarangkan_data[x]


# In[147]:


def get_dawan_data(soup):
    print("Parsing Data Kecamatan Dawan")
    
    # deklarasi kalau kita akan menggunakan variabel global
    global csv_row
    
    dict_dawan_data = {}

    dawan_table = soup.find_all(id="piechartKECAMATANDAWAN")
    dawan_data = (dawan_table[0]
     .contents[0]
     .contents[0]
     .contents[0]
     .contents[1]
     .contents[0]
     .contents[1]
     .contents)

    for data in dawan_data:
        result = str(data.contents[0].contents[0]).split()
        dict_dawan_data[result[0]] = result[1]

    for x in dict_dawan_data:
        if x == "ODP":
            csv_row["dawan_odp"] = dict_dawan_data[x]

        if x == "OTG":
            csv_row["dawan_otg"] = dict_dawan_data[x]

        if x == "PDP":
            csv_row["dawan_pdp"] = dict_dawan_data[x]

        if x == "Positif":
            csv_row["dawan_positif"] = dict_dawan_data[x]


# In[148]:


def get_klungkung_data(soup):
    print("Parsing Data Kecamatan Klungkung")
    
    # deklarasi kalau kita akan menggunakan variabel global
    global csv_row
    
    dict_klungkung_data = {}

    klungkung_table = soup.find_all(id="piechartKECAMATANKLUNGKUNG")
    klungkung_data = (klungkung_table[0]
     .contents[0]
     .contents[0]
     .contents[0]
     .contents[1]
     .contents[0]
     .contents[1]
     .contents)

    for data in klungkung_data:
        result = str(data.contents[0].contents[0]).split()
        dict_klungkung_data[result[0]] = result[1]

    for x in dict_klungkung_data:
        if x == "ODP":
            csv_row["klungkung_odp"] = dict_klungkung_data[x]

        if x == "OTG":
            csv_row["klungkung_otg"] = dict_klungkung_data[x]

        if x == "PDP":
            csv_row["klungkung_pdp"] = dict_klungkung_data[x]

        if x == "Positif":
            csv_row["klungkung_positif"] = dict_klungkung_data[x]


# In[149]:


def get_nusapenida_data(soup):
    print("Parsing Data Kecamatan Nusa Penida")
    
    # deklarasi kalau kita akan menggunakan variabel global
    global csv_row
    
    dict_nuspen_data = {}

    nuspen_table = soup.find_all(id="piechartKECAMATANNUSAPENIDA")
    nuspen_data = (nuspen_table[0]
     .contents[0]
     .contents[0]
     .contents[0]
     .contents[1]
     .contents[0]
     .contents[1]
     .contents)

    for data in nuspen_data:
        result = str(data.contents[0].contents[0]).split()
        dict_nuspen_data[result[0]] = result[1]

    for x in dict_nuspen_data:
        if x == "ODP":
            csv_row["nusapenida_odp"] = dict_nuspen_data[x]

        if x == "OTG":
            csv_row["nusapenida_otg"] = dict_nuspen_data[x]

        if x == "PDP":
            csv_row["nusapenida_pdp"] = dict_nuspen_data[x]

        if x == "Positif":
            csv_row["nusapenida_positif"] = dict_nuspen_data[x]


# In[150]:


def get_wna_data(soup):
    print("Parsing Data WNA")
    
    # deklarasi kalau kita akan menggunakan variabel global
    global csv_row
    
    dict_wna_data = {}

    wna_data = soup.find_all("h2")[5].next_sibling.next_sibling
    wna_table = wna_data.tr.next_sibling.next_sibling.contents

    # karena kebetulan hasil data ini belum 'bersih', jadi dilakukan pembersihan list data
    for i in wna_table:
        if i == '\n':
            wna_table.remove(i)

    dict_wna_data['ODP'] = wna_table[0].contents[0]
    dict_wna_data['OTG'] = wna_table[1].contents[0]
    dict_wna_data['PDP'] = wna_table[2].contents[0]
    dict_wna_data['Positif'] = wna_table[3].contents[0]

    for x in dict_wna_data:
        if x == "ODP":
            csv_row["wna_odp"] = dict_wna_data[x]

        if x == "OTG":
            csv_row["wna_otg"] = dict_wna_data[x]

        if x == "PDP":
            csv_row["wna_pdp"] = dict_wna_data[x]

        if x == "Positif":
            csv_row["wna_positif"] = dict_wna_data[x]


# In[151]:


def get_total_data(soup):
    print("Parsing Data Total Kabupaten Klungkung")
    
    # deklarasi kalau kita akan menggunakan variabel global
    global csv_row
    
    dict_overall_data = {}

    overall_data = soup.find_all('div', class_="total-div")

    for data in overall_data:
        if str(data
                .contents[1]
                .contents[0]
               ) == "POSITIF":

            dict_overall_data["Positif"] = str(data
                    .contents[0]
                    .contents[0]
                   )
        else:
            dict_overall_data[
                str(data
                    .contents[1]
                    .contents[0]
                   )
            ] = str(data
                    .contents[0]
                    .contents[0]
                   )

    for x in dict_overall_data:
        if x == "ODP":
            csv_row["total_odp"] = dict_overall_data[x]

        if x == "OTG":
            csv_row["total_otg"] = dict_overall_data[x]

        if x == "PDP":
            csv_row["total_pdp"] = dict_overall_data[x]

        if x == "Positif":
            csv_row["total_positif"] = dict_overall_data[x]


# In[152]:


# buat header CSV dengan format list
csv_head = ["timestamp", 
            "banjarangkan_odp", "banjarangkan_otg", "banjarangkan_pdp", "banjarangkan_positif", 
            "dawan_odp", "dawan_otg", "dawan_pdp", "dawan_positif", 
            "klungkung_odp", "klungkung_otg", "klungkung_pdp", "klungkung_positif", 
            "nusapenida_odp", "nusapenida_otg", "nusapenida_pdp", "nusapenida_positif", 
            "wna_odp", "wna_otg", "wna_pdp", "wna_positif", 
            "total_odp", "total_otg", "total_pdp", "total_positif"]


# In[153]:


# fungsi membuat file CSV baru dengan header pada baris paling atas
def create_csv(csv_file, csv_head, csv_row):
    print("Creating CSV files...")
    
    try:
        with open(csv_file, 'w') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_head)
            writer.writeheader()
            writer.writerow(csv_row)
    except IOError:
        print("I/O error")


# In[154]:


# fungsi menambahkan baris ke file CSV baru
def insert_csv(csv_file, csv_row):
    print("Writing to CSV files...")
    
    try:
        with open(csv_file, 'a+', newline='') as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=csv_head)
            writer.writerow(csv_row)
    except IOError:
        print("I/O error")


# In[155]:


failed = True
failed_count = 0

def run():
    global failed, failed_count
    
    try:
        init_browser()
        get_banjarangkan_data(soup)
        get_dawan_data(soup)
        get_klungkung_data(soup)
        get_nusapenida_data(soup)
        get_wna_data(soup)
        get_total_data(soup)
        failed = False
    except:
        print("Error index. Retrying in 10 seconds.....")
        failed_count += 1
        browser.close()
        
        if (failed_count > 5):
            print("5 Times Failed. Skipping this job. Next job in 8 Hours.")
            failed = False
        else:
            failed = True
        time.sleep(10)


# In[156]:


while failed:
    run()


# In[157]:


# pengecekan file CSV yang sudah ada. jadi kalau belum ada dia akan membuat yang baru.
if os.path.isfile(csv_file):
    insert_csv(csv_file, csv_row)
else:
    create_csv(csv_file, csv_head, csv_row)


# In[158]:


# setelah selesai parsing, tutup browser untuk memperkecil penggunaan memory (mungkin)
browser.close()

print("Job finished succesfully. Re-run job in 8 hours. Hopefully pandemic will be eradicated soon.")

