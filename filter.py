from const import *

def unwrap_element(elem):
    if elem is not None:
        return elem.text
    else:
        return ""

def has_term(elem, term):
    term_elements = elem.findall('.//lido:classificationWrap//lido:term', namespaces)
    term_texts    = map(lambda x: x.text, term_elements)

    if term is None:
        return True

    if term in term_texts:
        return True

    return False

def has_license(elem, license):
    if license is None:
        return True

    subitem_license = elem.find('.//lido:rightsResource//lido:term', namespaces)

    # subitem of item has no license (so probably no image either)
    if subitem_license is None:
        return False

    subitem_license_text = subitem_license.text

    if license == subitem_license_text:
        return True

    return False