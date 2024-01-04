from urllib.parse import urlparse

# Etape 8: Extraction du nom de domaine d'une URL
def extract_domain_name(url):
    parsed_url = urlparse(url)
    return parsed_url.netloc

# Etape 9: Séparation d'URLs basée sur l'appartenance à un domaine
def separate_urls_by_domain(urls, domain):
    domain_urls = []
    external_urls = []
    for url in urls:
        if extract_domain_name(url) == domain:
            domain_urls.append(url)
        else:
            external_urls.append(url)
    return domain_urls, external_urls

# Etape 10: Ouverture d'une page HTML et récupération du contenu
def get_html_content(url):
    try:
        response = requests.get(url)
        response.raise_for_status()  # s'assure que la requête a réussi
        return response.text
    except requests.RequestException as e:
        return str(e)

# Test des fonctions avec des exemples
example_url = "http://example.com"
example_domain = extract_domain_name(example_url)
print("Nom de domaine :", example_domain)

example_urls = ["http://example.com/page1", "https://otherdomain.com/page2"]
domain_urls, external_urls = separate_urls_by_domain(example_urls, example_domain)
print("URLs du domaine :", domain_urls)
print("URLs externes :", external_urls)

# Tester la récupération du contenu HTML
html_content = get_html_content(example_url)
print("Contenu HTML (premiers 100 caractères) :", html_content[:100])
