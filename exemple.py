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

if __name__ == "__main__":
    main()

choisir_pays()
main()