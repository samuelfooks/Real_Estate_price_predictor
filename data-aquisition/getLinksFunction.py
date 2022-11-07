#bring in necessary modules

from bs4 import BeautifulSoup
import requests

#list to hold links that are extracted from each xml file from the sitemap
links_data_arr=[]
#list to hold the 'good' links that are for sale
goodlinks=[]



def getPropertyLinks(siteMapURL):
#additional function to get the urls of the xml files a website with url().xml)
    def get_urls_of_xml(xml_url):
        r = requests.get(xml_url)
        xml = r.text
        soup = BeautifulSoup(xml)

        links_arr = []
        for link in soup.findAll('loc'):
            linkstr = link.getText('', True)
            links_arr.append(linkstr)

        return links_arr
#get all the xml files from sitemap from immoweb
    allXMLImmoweb= get_urls_of_xml(siteMapURL)

#look through chosen XML files from the sitemap and extract the links
    for i in range(19,20):
        xmlFiles=allXMLImmoweb[i]
        links_data_arr=get_urls_of_xml(xmlFiles)
#check the links for "for-sale" and append goodlinks list until 5000
        for i in range(9000,19000):
            if len(goodlinks)<5005 and 'for-sale' in links_data_arr[i]:
                goodlinks.append(links_data_arr[i])

#check
    print(len(goodlinks))
    return(goodlinks)

print(len(getPropertyLinks('https://immoweb.be/sitemap.xml')))

