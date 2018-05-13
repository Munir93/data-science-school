#### Munir welch 13/05/2018 ############

from bs4 import BeautifulSoup as soup
import pandas as pd
import numpy as np
from urllib.request import urlopen as uReq
import re

# beautiful soup us a libabry for pulling data out of HTML files
# we know what pandas and numpy are used for
# urllib is a pckage containing lots of modules for working with URL's we are
#going to be using .request which is used for opening and reading urls

#--------------------Extracting Arsenals stats--------------------------------------------

##### I like to think of a html file as a giant array which contains lots of informaion that we dont need
##### so the bulk of the tast is reading the html script and trying to figure out where our data is
##### then we just need to extract that data and store it

#opening and reading the url
url = 'http://www.uefa.com/uefaeuropaleague/season=2018/clubs/club=52280/statistics/index.html'
uClient = uReq(url)
page_html = uClient.read()
uClient.close()

#Pulling data out of the html file using beautiful soup
# good idea to print the whole file and note the parts of the html script that has the data we are interested in
#namely the stats, labels and the actual data
page_soup = soup(page_html,"html.parser")
#here we are finding only the data we are interested in when I checked the full html file I notcied all the
#data was split into grids so we I just went though each grid starting with class="stats--aggregated grid_4"
#print(page_soup)
#output grid 4 as an array
A_stats = page_soup.findAll("div",{"class":"stats--aggregated grid_4"})
#check to see if we have the right stats
#print(A_stats)
#checking the Asats list for labels and stats by indexing and using findall
labels2 = A_stats[0].findAll("span", {"class":"statistics--list--label"})
label2_stats = A_stats[0].findAll("div", {"class":"statistics--list--data"})
labels = A_stats[1].findAll("span", {"class":"statistics--list--label"})
label_stats = A_stats[1].findAll("div", {"class":"statistics--list--data"})
#check to see if we have the right labels and stat data
#print(labels2)
#print(label2_stats)
#print(label_stats)

# iterate through list of labels and use .text method to append label text to a list
# same with the stats

performance_label = []
performance_stats = []
j = 0

for label in labels2:
    performance = label.text
    performance_label.append(performance)
    stats = label2_stats[j].text
    performance_stats.append(stats)
    j+=1

i = 0
for label in labels:
    performance = label.text
    performance_label.append(performance)
    stats = label_stats[i].text
    if('\n' not in stats):
        performance_stats.append(stats)
    else:
        stats = stats.replace('\n',"")
        performance_stats.append(stats)
    i+=1

#print(performance_label)
#print(performance_stats)

#---------------------------------------defending stats and possession stats -----------------------------------------------------------#

D_stats = page_soup.findAll("div",{"class":"stats--aggregated grid_2"})
#print(D_stats)

labels2 = D_stats[0].findAll("span", {"class":"statistics--list--label"})
label2_stats = D_stats[0].findAll("div", {"class":"statistics--list--data"})
labels = D_stats[1].findAll("span", {"class":"statistics--list--label"})
label_stats = D_stats[1].findAll("div", {"class":"statistics--list--data"})
#print(labels)
#print(label_stats)

defence_labels = []
defence_stats = []

j = 0

for label in labels2:
    d = label.text
    defence_labels.append(d)
    s = label2_stats[j].text
    if ('\n' not in s):
        defence_stats.append(s)
    else:
        s=s.replace('\n',"")
        defence_stats.append(s)
    j+=1
i = 0
for label in labels:
    d = label.text
    defence_labels.append(d)
    s = label_stats[i].text
    if ('\n' not in s):
        defence_stats.append(s)
    else:
        s = s.replace('\n', "")
        defence_stats.append(s)
    i += 1


#---------------------------------------cleaning the data and converting to floats------------------------------------------------
### this stage is very important and will depend on that your lists of data look like I only needed to remove the %
### from a few values in each stats list and found a replace function to do it
###I also noticed that the label 'accuracy' was a bit ambigous so i changed that
### then I converted everything to floats for visulisation later

k = 0
for stats in performance_stats:
    if("%" in stats):
        stats = stats.replace("%","")
        performance_stats[k] = stats
    else:
        performance_stats[k] = stats
    k+=1

t = 0
for stats in defence_stats:
    if("%" in stats):
        stats = stats.replace("%","")
        defence_stats[t] = stats
    else:
        defence_stats[t] = stats
    t+=1

defence_labels[0] = 'Passing accuracy'


performance_stats = list(map(float,performance_stats))
defence_stats = list(map(float,defence_stats))


print(performance_label)
print(performance_stats)
print(defence_labels)
print(defence_stats)


#### now that we have all the data that we need from arsneal in a nice format we just need to do the same for athletico madrid

#-------------------------------------------------------Athletico Madrid section ------------------------------------------

ATL_url = 'http://www.uefa.com/uefaeuropaleague/season=2018/clubs/club=50124/statistics/index.html'
ATL_uClient = uReq(ATL_url)
ATL_page_html = ATL_uClient.read()
ATL_uClient.close()

ATL_page_soup = soup(ATL_page_html,"html.parser")

ATL_stats = ATL_page_soup.findAll("div",{"class":"stats--aggregated grid_4"})

#print(ATL_stats)
#checking the Asats list for labels and stats by indexing and using findall
ATL_labels2 = ATL_stats[0].findAll("span", {"class":"statistics--list--label"})
ATL_label2_stats = ATL_stats[0].findAll("div", {"class":"statistics--list--data"})
ATL_labels = ATL_stats[1].findAll("span", {"class":"statistics--list--label"})
ATL_label_stats = ATL_stats[1].findAll("div", {"class":"statistics--list--data"})
#check to see if we have the right labels and stat data
#print(ATL_labels2)
#print(ATL_label2_stats)
#print(ATL_labels)
#print(ATL_label_stats)

ATL_performance_label = []
ATL_performance_stats = []

q = 0

for label in ATL_labels2:
    x = label.text
    ATL_performance_label.append(x)
    y = ATL_label2_stats[q].text
    ATL_performance_stats.append(y)
    q+=1
w = 0
for label in ATL_labels:
    x = label.text
    ATL_performance_label.append(x)
    y = ATL_label_stats[w].text
    if ('\n' not in y):
        ATL_performance_stats.append(y)
    else:
        y = y.replace('\n','')
        ATL_performance_stats.append(y)
    w+=1

#print(ATL_performance_label)
#print(ATL_performance_stats)

#---------------------------------------defending stats and possession stats -----------------------------------------------------------#

ATL_D_stats = ATL_page_soup.findAll("div",{"class":"stats--aggregated grid_2"})
#print(ATL_D_stats)

ATL_labels2 = ATL_D_stats[0].findAll("span", {"class":"statistics--list--label"})
ATL_label2_stats = ATL_D_stats[0].findAll("div", {"class":"statistics--list--data"})
ATL_labels = ATL_D_stats[1].findAll("span", {"class":"statistics--list--label"})
ATL_label_stats = ATL_D_stats[1].findAll("div", {"class":"statistics--list--data"})


ATL_defence_labels = []
ATL_defence_stats = []

r = 0

for label in ATL_labels2:
    d = label.text
    ATL_defence_labels.append(d)
    s = ATL_label2_stats[r].text
    if ('\n' not in s):
        ATL_defence_stats.append(s)
    else:
        s=s.replace('\n',"")
        ATL_defence_stats.append(s)
    r+=1
g = 0
for label in ATL_labels:
    d = label.text
    ATL_defence_labels.append(d)
    s = ATL_label_stats[g].text
    if ('\n' not in s):
        ATL_defence_stats.append(s)
    else:
        s = s.replace('\n', "")
        ATL_defence_stats.append(s)
    g += 1


#---------------------------------------cleaning the data and converting to floats-------------------------------------

l = 0
for stats in ATL_performance_stats:
    if("%" in stats):
        stats = stats.replace("%","")
        ATL_performance_stats[l] = stats
    else:
        ATL_performance_stats[l] = stats
    l+=1

v = 0
for stats in ATL_defence_stats:
    if("%" in stats):
        stats = stats.replace("%","")
        ATL_defence_stats[v] = stats
    else:
        ATL_defence_stats[v] = stats
    v+=1

ATL_defence_labels[0] = 'Passing accuracy'


ATL_performance_stats = list(map(float,ATL_performance_stats))
ATL_defence_stats = list(map(float,ATL_defence_stats))

print(ATL_performance_label)
print(ATL_performance_stats)
print(ATL_defence_labels)
print(ATL_defence_stats)


#------------------------------------Finally we convert to a pd dataframe and save as an Exel file------------------------------------


df = pd.DataFrame({"Label":performance_label, "Arsenal Stats":performance_stats, "Athletico Mardrid Stats":ATL_performance_stats})
df2 = pd.DataFrame({"Label":defence_labels, "Arsenal Stats":defence_stats, "Athletico Madrid Stats": ATL_defence_stats})
print(df)


writer =pd.ExcelWriter('ARS-Vs-ATL-Pdata.xlsx')
df.to_excel(writer,index=False)
writer.save()

writer2 = pd.ExcelWriter('ARS-Vs-ATL-Ddata.xlsx')
df2.to_excel(writer2,index=False)
writer2.save()
