import os
import requests
from bs4 import BeautifulSoup

# Récupérer le chemin absolu du répertoire courant
repertoire_courant = os.path.abspath(os.getcwd())

# Liste des mots-clés à crawler
mots_cles = ['gapping', 'bing', 'chine', 'bretagne']

# Fonction pour crawler les pages pour un mot-clé donné et générer du HTML
def crawler_et_generer_html(mot_cle):
    # URL de la page à crawler pour un mot-clé donné sur Bing
    url = f'https://www.bing.com/search?q={mot_cle}'

    # Faire une requête pour récupérer le contenu de la page
    response = requests.get(url)

    # Vérifier si la requête s'est bien passée
    if response.status_code == 200:
        # Utiliser BeautifulSoup pour analyser le contenu HTML
        soup = BeautifulSoup(response.text, 'html.parser')

        # Trouver et collecter les résultats de recherche
        results = soup.find_all('li', class_='b_algo')  # Récupérer les balises contenant les résultats

        # Créer un nouveau fichier HTML et y insérer le contenu extrait dans le répertoire courant
        with open(os.path.join(repertoire_courant, f'{mot_cle}.php'), 'w', encoding='utf-8') as file:
            file.write('<?php\n')
            file.write('session_start();\n')
            file.write("if (!isset($_SESSION['user_id'])) {\n")
            file.write("    $_SESSION['redirect_url'] = $_SERVER['REQUEST_URI'];\n")
            file.write('}\n')
            file.write('$user_id = $_SESSION[\'user_id\'] ?? null;\n')
            file.write('$pdo = new PDO("mysql:host=localhost;dbname=VOTRE DB", "VOTRE USERNAME", "VOTRE MDP DE BDD");\n')
            file.write("if ($user_id) {\n")
            file.write('    $sql = "SELECT * FROM users WHERE id = ?";\n')
            file.write('    $stmt = $pdo->prepare($sql);\n')
            file.write('    $stmt->execute([$user_id]);\n')
            file.write('    $user = $stmt->fetch();\n')
            file.write('}\n')
            file.write('?>\n')
            file.write('<!DOCTYPE html>\n')
            file.write('<html lang="fr">\n')
            file.write('<head>\n')
            file.write('<script src="https://cdnjs.cloudflare.com/ajax/libs/fuse.js/6.4.6/fuse.min.js"></script>\n')
            file.write('<meta charset="UTF-8"/>\n')
            file.write('<meta name="viewport" content="width=device-width, initial-scale=1.0"/>\n')
            file.write('<meta http-equiv="X-UA-Compatible" content="ie=edge"/>\n')
            file.write('<link rel="icon" href="https://searcharea.ddns.net/searchicon.png"/>\n')
            file.write('<link rel="stylesheet" type="text/css" href="stylesheets/stylesheet.css"/>\n')
            file.write(f'<title>SearchArea - {mot_cle}</title>\n')  # Utilisation du mot-clé dans le titre
            file.write('<script>\n')
            file.write('function addFavorite() {\n')
            file.write('    var xhr = new XMLHttpRequest();\n')
            file.write('    xhr.open("POST", "add_favorite.php", true);\n')
            file.write('    xhr.setRequestHeader("Content-Type", "application/x-www-form-urlencoded");\n')
            file.write('    xhr.onload = function () {\n')
            file.write('        if (xhr.status === 200) {\n')
            file.write('            //REPLACEMEBYALERT\n')
            file.write('        }\n')
            file.write('    };\n')
            file.write('    var pageUrl = window.location.href;\n')
            file.write('    xhr.send("page_url=" + encodeURIComponent(pageUrl));\n')
            file.write('}\n')
            file.write('</script>\n')
            file.write('</head>\n')
            file.write('<body>\n')
            file.write('<div class="main-wrapper">\n')
            file.write('<div class="nav-bar">\n')
            file.write('<a href="https://searcharea.ddns.net/">\n')
            file.write('<?php if (isset($_SESSION[\'user_id\'])): ?>\n')
            file.write('<img src="<?php echo htmlspecialchars($user[\'profile_picture\']); ?>" alt="Profil" class="google-logo">\n')
            file.write('<?php else: ?>\n')
            file.write('<img src="https://searcharea.ddns.net/logosearchenginenew.png" alt="Logo Sudite" class="google-logo">\n')
            file.write('<?php endif; ?>\n')
            file.write('</a>\n')
            file.write('<div class="search-container">\n')
            file.write('<input type="text" id="search" placeholder="Effectuez une recherche..." onchange="openPage()" autocomplete="off">\n')
            file.write('<script type="text/javascript" src="script.js"></script>\n')
            file.write('</div>\n')
            file.write('</div>\n')
            file.write('<div class="second-navbar">\n')
            file.write('<div class="inner-second-div">\n')
            file.write(f'<a href="{mot_cle}.php">Recherche</a>\n')
            file.write(f'<a href="{mot_cle}images.html">Images</a>\n')
            file.write(f'<a href="areavidéos.html">Vidéos</a>\n')
            file.write(f'<a href="areamaps.html">Maps</a>\n')
            file.write(f'<a href="{mot_cle}bdd.html">Données de la recherche</a>\n')
            file.write('<a href="index.html">Revenir à SearchArea</a>\n')
            file.write('<?php if (!isset($_SESSION[\'user_id\'])): ?>\n')
            file.write('<a href="login.php" class="auth-button">Connectez-vous</a>\n')
            file.write('<?php else: ?>\n')
            file.write('<a href="profile.php" class="auth-button">Accéder à votre profil</a>\n')
            file.write('<a href="logout.php" class="auth-button">Se déconnecter</a>\n')
            file.write('<?php endif; ?>\n')
            file.write('<span class="right-second">\n')
            file.write('</span>\n')
            file.write('</div>\n')
            file.write('</div>\n')
            file.write('<div class="search-results">\n')
            file.write('<p>Rapide, non ?</p>\n')
            file.write('</div>\n')
            file.write('<div class="webpage">\n')
            file.write('<button onclick="addFavorite()">Ajouter cette page aux favoris</button>')   

            # Insérer les liens et descriptions des résultats de recherche dans le fichier HTML
            for result in results:
                title = result.find('h2').text  # Récupérer le titre
                link = result.find('a')['href']  # Récupérer le lien
                description = result.find('p').text  # Récupérer la description

                file.write(f'<h3><a href="{link}" target="_blank">{title}</a></h3>\n')  # Lien vers le site
                file.write(f'<p>{description}</p>\n')  # Description du site
                file.write("<br>\n")
            file.write('</div>\n')
            file.write('<div class="country-footer">\n')
            file.write('<ul>\n')
            file.write('<span class="kazakhstan">\n')
            file.write('<li>© 2024 SearchArea</li>\n')
            file.write('</span>\n')
            file.write('<span class="bold">\n')
            file.write('<li>Sarcelles, France</li>\n')
            file.write('</span>\n')
            file.write('<li>\n')
            file.write('<a href="https://searcharea.ddns.net/contact/index.php">Contact</a>\n')
            file.write('</li>\n')
            file.write('<li>\n')
            file.write('<a href="eula.html">Condition d utilisation</a>\n')
            file.write('</li>\n')
            file.write('<li>\n')
            file.write('<a href="https://twitter.com/PoloOhYeah_">Mon Twitter</a>\n')
            file.write('</li>\n')
            file.write('</ul>\n')
            file.write('</div>\n')
            file.write('</div>\n')
            file.write('</body>\n')
            file.write('</html>\n')

    else:
        print(f'La requête pour le mot-clé "{mot_cle}" sur Bing a échoué')

# Pour chaque mot-clé, crawler les résultats de recherche sur Bing et générer un fichier HTML
for mot_cle in mots_cles:
    crawler_et_generer_html(mot_cle)
