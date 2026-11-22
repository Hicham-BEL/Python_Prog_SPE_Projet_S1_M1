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
        return f"Titre : {self.titre} - Date de publication : {self.date}"



class HackerNewsDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, id, children, origine = "HackerNews"):
        super().__init__(titre, auteur, date, url, texte)
        self.id = id
        self.children = children # Id des commentaires du post
        self.nb_commentaires = len(children) if children is not None else 0

    def get_nb_commentaires(self):
        return self.nb_commentaires
    
    def set_nb_commentaires(self, nb_commentaires):
        if nb_commentaires >= 0:
            self.nb_commentaires = nb_commentaires
        else:
            raise ValueError("nb_commentaire ne peut pas être négatif")
    
    def __str__(self):
        return f"{super().__str__()} - Commentaires : {self.nb_commentaires}"
    
    def getType(self):
        return self.origine


class ArxivDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, commentaires_auteurs=None):
        super().__init__(titre, auteur, date, url, texte, origine = "Arxiv")
        if commentaires_auteurs is None:    
            self.commentaires_auteurs = []
        else:
            self.commentaires_auteurs = commentaires_auteurs
        
    def get_commentaires_auteurs(self):
        return self.commentaires_auteurs
    
    def set_commentaires_auteurs(self, commentaires_auteurs):
        self.commentaires_auteurs = commentaires_auteurs
    
    def __str__(self):
        if len(self.commentaires_auteurs) == 0:
            comm_auteurs = "Aucun commentaire"
        else:
            comm_auteurs = self.commentaires_auteurs
        return f"{super().__str__()} - Commentaires Auteurs : {comm_auteurs}"
    
    def getType(self):
        return self.origine