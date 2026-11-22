from classes import Commentaire, Document
import urllib.parse
import urllib.request
import json
import math
from datetime import datetime, timezone
import html

def get_json(url):
    try:
        with urllib.request.urlopen(url) as reponse:
            d_hn = json.load(reponse)

    except Exception as e:
        print("Erreur récupération json : ", e)
        raise
    return d_hn


# Met dans des listes les stories et les commentaires
def hits_to_list(hits): 

    for hit in hits: # Dans un hit se trouve toutes les données qui nous intéresse

        tags = hit.get("_tags") # Déterminer si l'objet est un commentaire ou une story

        if "story" in tags :
                
            titre = hit.get("title")    
            auteur = hit.get("author")

            # Gestion du format de date
            date = hit.get("created_at")
            date = datetime.fromisoformat(date.replace("Z", "+00:00"))

            url = hit.get("url")
            story_id = hit.get("story_id")
            commentaires = hit.get("children")

            # Nettoyage des balises html dans le texte
            texte = hit.get("story_text")
            texte = html.unescape(texte).replace("<p>", " ").strip()

            doc = HackerNewsDocument(titre, auteur, date, url, texte, story_id, commentaires)    
            docs.append(doc)
            
        
        if "comment" in tags:
            
            auteur = hit.get("author")
            date = hit.get("created_at")
            texte = hit.get("comment_text", "")
            texte = html.unescape(texte).replace("<p>", " ").strip()
            identifiant = int(hit.get("objectID"))
            enfants = hit.get("children")
            story_id = hit.get("story_id")
            parent_id = hit.get("parent_id")

            commentaire = CommentaireHackerNews(auteur, texte, date, identifiant, parent_id, story_id, enfants)
            coms.append(commentaire)

    return



def requete_hacker_news(theme): # Requête l'api, max 10000 requêtes / minutes

    nb_hits_page = 1000

    url = "https://hn.algolia.com/api/v1/search_by_date?" + urllib.parse.urlencode(
        {"query": theme, "tags": "(story,comment)", "hitsPerPage": nb_hits_page}) # Ajout des commentaires dans les tags

    print("requete: ", url)

    d_hn = get_json(url)
    print(d_hn)

    nb_hits = d_hn["nbHits"]
    print("Nombre de hits trouvés (story + comms) : ", nb_hits)

    hits = d_hn["hits"]
    print("enregistrement des 1000 premiers hits")
    hits_to_list(hits)

    if nb_hits > 1000:

        nb_iterations = math.ceil(nb_hits / nb_hits_page) #Nombre d'itérations à effectuer pour requêter la totalité des données issues de la requête (max 1000 par requête)
  
        print("Nombre de requetes pour tout stocker : ", nb_iterations)

        # Réitère la requête à partir de la date du dernier objet récupéré
        for i in range(1,nb_iterations):

            if len(hits) == 0: # Si il n'y a plus de stories ou de commentaires à stocker
                break
            nv_debut = hits[-1]["created_at_i"]
            nv_date = "created_at_i<" + str(nv_debut)
            nv_url = url + "&numericFilters=" + urllib.parse.quote(nv_date, safe=",<>=")

            d_hn = get_json(nv_url)
            
            hits = d_hn["hits"]
            hits_to_list(hits)

            # Mettre les prints en commentaires pour gagner en perf
            #print("enregistrement jusqu'aux  ", i+1, "000ème hits")
            #print("total documents : ", len(docs))

    return