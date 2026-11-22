class Corpus:
    def __init__(self, nom, dict_auteurs, dict_docs):
        self.nom = nom
        self.authors = dict_auteurs
        self.id2doc = dict_docs
        self.ndoc = int(len(id2doc))
        self.naut = int(len(dict_auteurs))

    def afficher_par_date(self, nb_doc):
        docs_tries = sorted(self.id2doc.values(), key = lambda doc: doc.date)
        
        for doc in docs_tries[:nb_doc]:
            print(doc)
            
    def afficher_par_titre(self, nb_doc):
        docs_tries = sorted(self.id2doc.values(), key = lambda doc: doc.titre)
        
        for doc in docs_tries[:nb_doc]:
            print(doc)
            
    def __repr__(self):
        return f"Corpus {self.nom} : {self.ndoc} documents et {self.naut} auteurs"
    
    # Sauvegarde du corpus sur le pc
    def save(self, nom_fichier):
        with open(nom_fichier, "wb") as sav:
            pickle.dump(self, sav)
        print(f"Sauvegarde du corpus dans {nom_fichier}")
    
    # Chargement du corpus depuis le pc
    def load(self, chemin_fichier):
        with open(chemin_fichier, "rb") as sav:
            corpus_load = pickle.load(sav)
        
        self.nom = corpus_load.nom
        self.authors = corpus_load.authors
        self.id2doc = corpus_load.id2doc
        self.ndoc = corpus_load.ndoc
        self.naut = corpus_load.naut