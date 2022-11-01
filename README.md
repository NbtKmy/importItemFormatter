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

## SB Schweizer Buch


### Primo
https://nb-helveticat.primo.exlibrisgroup.com/discovery/search?query=lds02,exact,2022%2020&tab=Swissbook&search_scope=Swissbook&vid=41SNL_51_INST:swissbook&mfacet=lds23,include,340,1&lang=de&offset=0

### SRU
mit MARCXML vers. 1.2 (not working)
https://nb-helveticat.alma.exlibrisgroup.com/view/sru/41SNL_51_INST?version=1.2&operation=searchRetrieve&recordSchema=marcxml&maximumRecords=5&query=date_of_publication=2022%20and%20dewey_decimal_class_number=340%20and%20alma.mms_material_type=BK

mit MARCXML vers. 1.1 (works well)
https://nb-helveticat.alma.exlibrisgroup.com/view/sru/41SNL_51_INST?version=1.1&operation=searchRetrieve&recordSchema=marcxml&maximumRecords=5&query=date_of_publication=2022%20and%20dewey_decimal_class_number=340%20and%20alma.mms_material_type=BK

mit Mods vers. 1.2 (not working)
https://nb-helveticat.alma.exlibrisgroup.com/view/sru/41SNL_51_INST?version=1.2&operation=searchRetrieve&recordSchema=mods&maximumRecords=5&query=date_of_publication=2022%20and%20dewey_decimal_class_number=340%20and%20alma.mms_material_type=BK

