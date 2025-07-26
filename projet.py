import requests

endpoint = "https://jsearch.p.rapidapi.com/search"

api_key = "57cc8d1375msh68815a3c5ed88fbp192a56jsn1ac0d6b85f85"
api_host = "jsearch.p.rapidapi.com"
hearders{
    "x-rapidapi-key" = api_key,
    "x-rapidapi-host" = "jsearch.p.rapidapi.com"
} 
parametre = {
    "query" : recherche_d_emploi,
    "page" = 1,
    "contry" = contry
}
response = requests.get(url,hearders=hearders,params=parametre)
#dictionnaire des pays
countries = {
    "1" : "us",
    "2" : "ca",
    "3" ; "ae"
}
#choix du pays
 def choisir_pays():
    print("choisir un pays :")
    for code ,nom in countries.items():
        print(f"{code} {nom}")
    choix = input("entrer le nom du pays").lower()
    return choix