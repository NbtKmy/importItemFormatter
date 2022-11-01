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


### SRU
mit MARCXML vers. 1.2 (not working)
https://nb-helveticat.alma.exlibrisgroup.com/view/sru/41SNL_51_INST?version=1.2&operation=searchRetrieve&recordSchema=marcxml&maximumRecords=5&query=date_of_publication=2022%20and%20dewey_decimal_class_number=340%20and%20alma.mms_material_type=BK

mit MARCXML vers. 1.1 (works well)
https://nb-helveticat.alma.exlibrisgroup.com/view/sru/41SNL_51_INST?version=1.1&operation=searchRetrieve&recordSchema=marcxml&maximumRecords=5&query=date_of_publication=2022%20and%20dewey_decimal_class_number=340%20and%20alma.mms_material_type=BK

mit Mods vers. 1.2 (not working)
https://nb-helveticat.alma.exlibrisgroup.com/view/sru/41SNL_51_INST?version=1.2&operation=searchRetrieve&recordSchema=mods&maximumRecords=5&query=date_of_publication=2022%20and%20dewey_decimal_class_number=340%20and%20alma.mms_material_type=BK

## BNF

### SRU

https://catalogue.bnf.fr/api/SRU?version=1.2&operation=searchRetrieve&query=bib.date%20=%20%222022%22%20and%20bib.dewey%20any%20%2234*%22&recordSchema=unimarcxchange&maximumRecords=5&startRecord=1

Das MARC-Format von BNF-SRU funktioniert so nicht. -> Daten wiederum ins passende MARC-Format umwandeln (siehe "./examples/test2.xml")

## Schulthess
Web-Seite
Alle
https://www.schulthess.com/buchshop/fachkatalog/juristische-verlage-schweiz/schulthess-verlag
Neuerscheinung
https://www.schulthess.com/buchshop/fachkatalog/juristische-verlage-schweiz/schulthess-verlag/neuerscheinungen-schulthess

Das entsprechende div-element hat 'class="sectionDesc" data-bpmisbn="[ISBN ohne Bindestrich]"'
Da kann man vielleicht über diese Attribute ISBN-Nummer holen?

## Oasis
Aus der Spalte N ("EAN/ISBN") der Tabelle die ISBN-Nummer holen



