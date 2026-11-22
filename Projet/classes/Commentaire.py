class Commentaire:
    def __init__(self, auteur, texte, datetime):
        self.auteur = auteur
        self.texte = texte
        self.datetime = datetime

class CommentaireHackerNews(Commentaire):
    def __init__(self, auteur, texte, datetime, id, parent_id, story_id, children, origine = "HackerNews"):
        super().__init__(auteur, texte, datetime)
        self.id = id
        self.parent_id = parent_id
        self.story_id = story_id
        self.children = children