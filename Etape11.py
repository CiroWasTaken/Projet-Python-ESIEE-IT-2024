# Etape 11: Programme d'audit de la première page
def seo_audit(url):
    # Récupération du contenu HTML
    html_content = get_html_content(url)
    if not html_content:
        return "Impossible de récupérer le contenu HTML."

    # Suppression des balises HTML pour analyse de texte
    text = remove_html_tags(html_content)
    word_count = extract_words_and_count(text)
    
    # Supposons une liste de mots parasites
    stopwords = ['et', 'ou', 'le', 'la', 'les', 'un', 'une', 'de', 'des', 'pour', 'l']
    filtered_words = filter_stopwords(word_count, stopwords)
    
    # Récupération des 3 mots les plus fréquents
    top_words = dict(sorted(filtered_words.items(), key=lambda item: item[1], reverse=True)[:3])

    # Analyse des liens
    alt_values = extract_attribute_values(html_content, 'img', 'alt')
    href_values = extract_attribute_values(html_content, 'a', 'href')

    domain = extract_domain_name(url)
    internal_links, external_links = separate_urls_by_domain(href_values, domain)

    # Résultats de l'audit
    audit_results = {
        "Top mots-clés": top_words,
        "Nombre de liens internes": len(internal_links),
        "Nombre de liens externes": len(external_links),
        "Présence de balises alt dans les images": len(alt_values) > 0
    }

    return audit_results

# Exemple d'audit avec une URL fictive (en réalité, vous demanderiez à l'utilisateur de fournir l'URL)
example_audit_url = "http://example.com"
audit_results = seo_audit(example_audit_url)
print("Résultats de l'audit SEO :", audit_results)
