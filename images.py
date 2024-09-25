import requests
from bs4 import BeautifulSoup

# Fonction pour récupérer les résultats de recherche de Bing
def bing_search(query, num_results=50):
    url = f"https://www.bing.com/images/search?q={query}&count={num_results}"
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for div in soup.find_all('div', class_='imgpt'):
        img_tag = div.find('img')
        if img_tag and img_tag.has_attr('src'):
            img_url = img_tag['src']
            results.append({'img_url': img_url})
    return results

# Exemple d'utilisation
query = "1664"
num_results = 20
results = bing_search(query, num_results)

html_content = '<!DOCTYPE html>'
html_content += '<html lang="fr">'
html_content += '<head>'
html_content += '<script src="https://cdnjs.cloudflare.com/ajax/libs/fuse.js/6.4.6/fuse.min.js"></script>'
html_content += '<meta charset="UTF-8"/>'
html_content += '<meta name="viewport" content="width=device-width, initial-scale=1.0"/>'
html_content += '<meta http-equiv="X-UA-Compatible" content="ie=edge"/>'
html_content += '<link rel="icon" href="https://searcharea.ddns.net/searchicon.png"/>'
html_content += '<link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css"/>'
html_content += f'<title>SearchArea - {query}</title>'
html_content += '</head>'
html_content += '<body>'
html_content += '<div class="main-wrapper">'
html_content += '<div class="nav-bar">'
html_content += '<a href="index.html">'
html_content += '<img src="logosearchenginenew.png" alt="area" id="google-logo"/>'
html_content += '</a>'
html_content += '<div class="search-container">'
html_content += '<input type="text" id="search" placeholder="Effectuez une recherche..." onchange="openPage()" autocomplete="off">'
html_content += '<script type="text/javascript" src="script.js"></script>'
html_content += '</div>'
html_content += '</div>'
html_content += '<div class="second-navbar">'
html_content += '<div class="inner-second-div">'
html_content += f'<a href="{query}.php">Recherche</a>'
html_content += f'<a href="{query}images.html">Images</a>'
html_content += f'<a href="areavidéos.html">Vidéos</a>'
html_content += f'<a href="areamaps.html">Maps</a>'
html_content += f'<a href="{query}bdd.html">Données de la recherche</a>'
html_content += '<a href="index.html">Revenir à SearchArea</a>'
html_content += '<span class="right-second">'
html_content += '</span>'
html_content += '</div>'
html_content += '</div>'
html_content += '<div class="search-results">'
html_content += '<p>Nous sommes désolés pour les images, FUCK le CSS !!!</p>'
html_content += '</div>'
html_content += '<div class="webpage">'
html_content += '</div>'
html_content += '<center>'

for i, r in enumerate(results):
    img_data = requests.get(r['img_url']).content
    img_filename = f"{query}_image_{i+1}.jpg"
    with open(img_filename, 'wb') as f:
        f.write(img_data)
    # Ajouter la balise d'image au contenu HTML
    html_content += f'<img src="{img_filename}" alt="Image {i+1}">'

html_content += '</center>'    
html_content += '<br>'
html_content += '<br>'
html_content += '<p>Donnez votre avis sur le nouveau style des pages en cliquant <a href="avissite.php">ICI.</a></p>'
html_content += '<br>'
html_content += '</div>'
html_content += '</body>'
html_content += '</html>'

# Écrire le contenu HTML dans un fichier portant le nom du mot-clé
with open(f"{query}images.html", 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)
