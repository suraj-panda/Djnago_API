from django.shortcuts import render
import requests
from bs4 import BeautifulSoup
import json

def retrieve(request):
    if request.method=="POST":
        country = request.POST.get('country')
        URL = 'https://en.wikipedia.org/wiki/' + country
        r = requests.get(URL)
        soup = BeautifulSoup(r.content, 'html.parser')

        script1 = soup.find_all('a')[7]
        sample1 = str(script1)
        c_list1 = sample1.split("\"")
        flag_link = "https:" + str(c_list1[21].split(",")[0])
        print(flag_link)

        capital = []
        script2 = soup.find_all('a')[25].text
        sample2 = str(script2)
        capital.append(sample2)
        if len(capital)>1:
            print(capital)
        else:
            print(sample2)

        largest_city = []
        script3 = soup.find_all('a')[27].text
        largest_city.append(script3)
        script4 = soup.find_all('a')[28].text
        largest_city.append(script4)
        if len(largest_city)>1:
            print(largest_city)
        else:
            print(script3)


        official_languages = []
        script5 = soup.find_all('a')[29].text
        official_languages.append(script5)
        script6 = soup.find_all('a')[30].text
        official_languages.append(script6)
        if len(official_languages)>1:
            print(official_languages)
        else:
            print(script5)

        area_total = 0
        script7 = soup.find_all('td')[28].text
        sample3 = script7.split(" ")
        #print(sample3)
        sample4 = str(sample3[0])
        c_list2 = []
        for i in sample4:
            if i!='[':
                c_list2.append(i)
            elif i==',':
                continue
            else:
                break
        sample3 = ""
        for i in c_list2:
            if i==',':
                continue
            sample3 = sample3 + i
        area_total = int(sample3)
        print(area_total)

        Population = ""
        script8 = soup.find_all('td')[30].text
        sample3 = str(script8)
        c_list3 = []
        for i in sample3:
            if i!='[':
                c_list3.append(i)
            else:
                break
        sample3 = ""
        for i in c_list3:
            sample3 = sample3 + i
        Population = str(sample3)
        print(Population)

        GDP_nominal = ""
        script9 = soup.find_all('td')[37].text
        sample3 = str(script9)
        c_list4 = []
        for i in sample3:
            if i!='[':
                c_list4.append(i)
            else:
                break
        sample3 = ""
        for i in c_list4:
            sample3 = sample3 + i
        GDP_nominal = sample3
        print(GDP_nominal)
            
        context = {}
        context = {'flag_link': flag_link, 'capital':sample2, 'largest_city': largest_city, 'official_languages': official_languages, 'area_total': area_total, 'Population': Population, 'GDP_nominal': GDP_nominal}
        #print(context)
        json_object = json.dumps(context, indent = 4)
        
        print("JSON SCRAPING")
        print(json_object)

        return render(request, 'index.html', context)
    else:
        return render(request, 'index.html')
