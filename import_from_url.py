from bs4 import BeautifulSoup
import requests
import xml.etree.ElementTree as ET

def get_items_from_html(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    return soup.title.text

def get_items_from_xml(file):
    xml_obj =ET.parse(file).getroot()
    # wenn man die items von RSS holen will
    dnb_id = xml_obj.findtext('.//feed//entry//id')

    return dnb_id
    