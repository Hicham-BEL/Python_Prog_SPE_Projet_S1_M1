from Document import Document

class ArxivDocument(Document):
    def __init__(self, titre, auteur, date, url, texte, commentaires_auteurs=None):
        super().__init__(titre, auteur, date, url, texte, type = "Arxiv")
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
        return self.type
        
        