from import_donnees import get_hackernews

docs = [] # Stockage des documents
coms = [] # Commentaires d'hackernews

get_hackernews.requete_hacker_news("volcano", docs, coms)

print(len(docs))
print(len(coms))