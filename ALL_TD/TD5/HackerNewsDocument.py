from Document import Document

class HackerNewsDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, nb_commentaires):
        super().__init__(titre, auteur, date, url, texte, type = "Hacker News")
        self.nb_commentaires = nb_commentaires
        
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
        return self.type