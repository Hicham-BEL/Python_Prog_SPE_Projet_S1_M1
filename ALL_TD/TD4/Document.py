class Document:
    def __init__(self, titre, auteur, date, url, texte):
        self.titre = titre
        self.auteur = auteur
        self.date = date
        self.url = url
        self.texte = texte

    def infos(self):
        print("Titre : ", self.titre)
        print("Auteur : ", self.auteur)
        print("date : ", self.date)
        print("url : ", self.url)
        print("texte : ", self.texte)

    def __str__(self):
        return self.titre