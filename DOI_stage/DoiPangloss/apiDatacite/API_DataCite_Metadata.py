import requests
from DOI_stage.DoiPangloss.constantes import USERNAME, PASSWORD, ENDPOINTMETADATA

def enregistrer_metadonneesRessource(filename, doi):
    metadata = open(filename, 'r').read()
    response = requests.post(ENDPOINTMETADATA, auth=(USERNAME, PASSWORD), data=metadata.encode('UTF-8'), headers={'Content-Type':'application/xml;charset=UTF-8'})
    file = open('DoiPangloss/Data/apiMetadonnees', 'a')
    if response.status_code != requests.codes.ok:
        file.write(str(response.status_code) + " " + doi + response.text + "\n")
        print(str(response.status_code) + " " + response.text)

def enregistrer_metadonneesPhrase(filename, id):
    metadata = open(filename, 'r').read()
    response = requests.post(ENDPOINTMETADATA, auth=(USERNAME, PASSWORD), data=metadata.encode('UTF-8'), headers={'Content-Type':'application/xml;charset=UTF-8'})
    file = open('DoiPangloss/Data/apiMetadonnees', 'a')
    if response.status_code != requests.codes.ok:
        file.write(str(response.status_code) + " " + id + response.text + "\n")
        print(str(response.status_code) + " " + response.text)

