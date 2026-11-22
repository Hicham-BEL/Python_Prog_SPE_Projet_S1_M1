class Author:
    def __init__(self, name, ndoc, production):
        self.name = name
        self.ndoc = ndoc if ndoc is not None else 0
        self.production = production if production is not None else []

    def add(self, dict_docs):
        for cle, valeur in dict_docs.items():
            if valeur.auteur == self.name and cle not in self.production:
                self.production.append(cle)
                self.ndoc = self.ndoc + 1

    def __str__(self):
        return self.name