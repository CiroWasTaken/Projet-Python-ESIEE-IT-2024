def extract_attribute_values(html_text, tag_name, attribute_name):
    soup = BeautifulSoup(html_text, "html.parser")
    return [tag[attribute_name] for tag in soup.find_all(tag_name) if tag.get(attribute_name)]
