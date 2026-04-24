import fitz  # PyMuPDF

def extract_links_from_pdf(file_path):
    """Finds all clickable URLs inside the PDF."""
    doc = fitz.open(file_path)
    links = []
    for page in doc:
        for annot in page.annots():
            if annot.type[0] == 2:  # URI link type
                uri = annot.info.get("uri")
                if uri:
                    links.append(uri)
    doc.close()
    return list(set(links))