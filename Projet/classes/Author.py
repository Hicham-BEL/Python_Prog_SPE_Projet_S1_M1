class Author:
    def __init__(self, name):
        self.name = name
        self.ndoc = ndoc if ndoc is not None else 0
        self.production = dict()

    def add(self, doc):
        self.production.append(doc)
        self.ndoc = len(self.production)

    def __str__(self):
        
        if self.ndoc == 0:
            return f"Auteur : {self.name} - Aucun document"
        else:
            for document in self.production.values():
                all_titre.append(document.titre)
                
            return f"Auteur : {self.name} - Nombre de documents : {self.ndoc} - Titres des documents : {all_titre}"


    def taille_moyenne_doc(self):
        if self.ndoc == 0:
            return 0
        total_carac = 0
        for document in self.production.values():
            total_carac += len(document.texte)
        return total_carac / self.ndoc