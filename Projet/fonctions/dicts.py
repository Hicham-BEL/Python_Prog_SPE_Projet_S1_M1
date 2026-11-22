from classes import Author

# Crée un dictionnaire servant à indexer des documents issus d'une liste ainsi que les auteurs dans les dicts id2doc et id2aut
def docs_to_dict(docs):
    for doc in docs:
        cle = str(doc.origine) + str(doc.id) # La clé se compose de l'origine et de l'id du doc donné par l'api
        if cle not in id2doc.keys():
            id2doc[cle]= doc

        if doc.auteur not in id2aut.keys():
            id2aut[doc.auteur] = Author(doc.auteur, ndoc = 1, production = doc)
        else:
            id2aut[doc.auteur].add(doc)