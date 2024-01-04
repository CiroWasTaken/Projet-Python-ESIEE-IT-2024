def remove_html_tags(html_text):
    soup = BeautifulSoup(html_text, "html.parser")
    return soup.get_text()
