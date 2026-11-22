# from datetime import datetime, timezone

class Document :
    def __init__(self, titre, auteur, date, url, texte, type = ""):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte
        self.type = type
    
    def __str__(self):
        return f"Titre : {self.titre} - Date de publication : {self.date}"
    
    
    
