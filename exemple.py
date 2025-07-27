import requests

endpoint = "https://jsearch.p.rapidapi.com/search"

api_key = "57cc8d1375msh68815a3c5ed88fbp192a56jsn1ac0d6b85f85"
api_host = "jsearch.p.rapidapi.com"

headers = {
    "x-rapidapi-key": api_key,
    "x-rapidapi-host": api_host
}

countries = {
    "1": "us",
    "2": "ca",
    "3": "ae"
}

def choisir_pays():
    print("Choisir un pays :")
    for code, nom in countries.items():
        print(f"{code}: {nom}")
    choix = input("Entrer le code du pays: ").strip()
    return countries.get(choix, "us")

def main():
    pays = choisir_pays()
    recherche_d_emploi = input("Entrez le poste recherché: ").strip()
    params = {
        "query": recherche_d_emploi,
        "page": 1,
        "country": pays
    }
    response = requests.get(endpoint, headers=headers, params=params)
    if response.status_code == 200:
        data = response.json()
        print("Résultats de la recherche:")
        for job in data.get("data", []):
            print(f"- {job.get('job_title')} chez {job.get('employer_name')}")
    else:
        print("Erreur lors de la requête:", response.status_code)
def resultats(offre):
    if not offre:
        print("aucun resultat trouver.")
        return
    for i , offre in enumerate(offre[:5],1):
        print(f"\n offre{i}")
        print("poste:", offre.get("Titre du poste","N/A"))
        print("Entreprise:",offre.get("nom de l'entreprise","N/A"))
        print("Localisation:",offre.get("Lieu du travail","N/A"))
        print("Type de contrat:",offre.get("typr de contrat","N/A"))
        print("Description:",offre.get("bref_resume","N/A")[:100]+"...")
    

if __name__ == "__main__":
    main()

choisir_pays()
main()