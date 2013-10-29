from bs4 import BeautifulSoup
import urllib2
 
wiki = "http://www.ncbtmb.org/tools/find-a-certified-massage-therapist/results?city=&email=&name=&phone=&state=All&zipcode=&country=USA&moderate=&page=1&modality="
header = {'User-Agent': 'Mozilla/5.0'} 
req = urllib2.Request(wiki,headers=header)
page = urllib2.urlopen(req)
soup = BeautifulSoup(page)
 
name = ""
city = ""
state = ""
zipcode = ""
phone = ""
email = "" 
modality = ""
table = soup.find("table", { "class" : "views-table cols-7" })
 
f = open('output.csv', 'w')
 
for row in table.findAll("tr"):
    cells = row.findAll("td")
    
    if len(cells) == 7:
        name = cells[0].find(text=True)
        city = cells[1].find(text=True)
        state = cells[2].find(text=True)
        zipcode = cells[3].find(text=True)
        phone = cells[4].find(text=True)
        email = cells[5].find(text=True)
        modality = cells[6].find(text=True) 
    write_to_file = name + "," + city + "," + state + "," + zipcode +  "," +phone +  ","  + email + "," +modality+ "\n"
   
    print write_to_file
    f.write(write_to_file)
 
f.close()



___output___

            Aaron C. Dembroski          
            Chicago          
            IL          
60613
            312-730-3473          



            Aaron C. Harnik          
            Las Vegas          
            NV          
89122
            702-328-2013          



            Aaron C. Wigsmoen          
            Hammond          
            IN          
46824
            219-931-3089          



            Aaron Cason          
            Denton          
            TX          
76205
            940-442-6900          



            Aaron D. Cripe          
            Vandalia          
            IL          
62471
            618-367-6471          



            Aaron D. Rosen          
            Panama City Beach          
            FL          
32407
            850-866-5558          



            Aaron D. Schneider          
            Boulder          
            CO          
80304
            720-327-4772          



            Aaron E. McLaughlin          
            Richland          
            WA          
99354
            509-619-2809          



            Aaron Easton          
            Sioux City          
            IA          
51103
            712-389-4830          



            Aaron G Brockman          
            Independence          
            MO          
64050
            816-316-0947          



            Aaron Gaylord          
            St. Paul          
            MN          
55109
            978-457-5875          



            Aaron J. Huerta          
            San Antonio          
            TX          
78255
            210-275-6714          



            Aaron J. Nadeau          
            Piscataway          
            NJ          
8854
            848-702-3931          



            Aaron J. Witz          
            Vernon Hills          
            IL          
60061
8479228028



            Aaron James Richter          
            Homosassa          
            FL          
34446
            352-621-3332          



            Aaron L. Farquhar          
            Huddleston          
            VA          
24104
            540-529-8998          



            Aaron Land          
            Baltimore          
            MD          
21210
4436689025



            Aaron M. Fetty          
            Reno          
            NV          
89509
            775-771-2532          



            Aaron M. Shaw          
            Albuquerque          
            NM          
87109
            505-944-5850          



            Aaron Meile          
            Central Square          
            NY          
13036
            315-436-9822          
