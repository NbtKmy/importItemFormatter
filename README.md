# importItemFormatter
Formatting items from div. sources for Zotero import 


## DNB
SRU with Marc-xml

description by the DNB
https://www.dnb.de/DE/Professionell/Metadatendienste/Datenbezug/SRU/sru_node.html#doc58294bodyText2
and 
https://www.dnb.de/DE/Service/Hilfe/Katalog/kataloghilfeExpertensuche_node.html#doc193268bodyText1


example
Query: ddc=340* and jhr=2022 and mat=books
https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=ddc=340*%20and%20jhr=2022%20and%20mat=books&recordSchema=MARC21-xml

https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=ddc=340*%20and%20jhr=2022&recordSchema=MARC21-xml&maximumRecords=100

https://services.dnb.de/sru/dnb?version=1.1&operation=searchRetrieve&query=ddc=340*%20and%20jhr=2022&recordSchema=MARC21-xml&maximumRecords=100&startRecord=250
