import os
import mactypes
from appscript import app

class BibDesk:  
    def __init__(self):
        self.app = app('BibDesk')
        
    def import_reference(self, ref):
        a = self.app

        # Get the selected bibdesk database
        db = a.documents.get()[0]

        # Insert the reference
        doc = a.import_(db, from_=ref)

        # Auto-generate cite-key
        doc[0].cite_key.set(doc[0].generated_cite_key())

        return doc[0]

    def find_authors(self):
        a = self.app

        # Get the selected bibdesk database
        if not a.documents.get():
            return []

        db = a.documents.get()[0]
        pubs = db.publications()

        l = set()
        for pub in pubs:
            auths = pub.authors()
            for auth in auths:
                l.add(auth.abbreviated_normalized_name())

        return l

    def find_arxiv_ref(self, arxiv_id):
        a = self.app

        # Get the selected bibdesk database
        db = a.documents.get()[0]
        pubs = db.publications()

        if arxiv_id[-2] == "v":
            arxiv_id = arxiv_id[:-2]

        find_url = "http://arxiv.org/abs/{}".format(arxiv_id)
        for pub in pubs:
            url = pub.URL()
            if not url:
                continue

            if url[-2] == "v":
                url = url[:-2]

            if url == find_url:
                return pub

        return False

    def link_pdf(self, ref, filename):
        filename = os.getcwd() + "/" + filename
        ref.linked_files.add(mactypes.File(filename), to=ref)
        ref.auto_file()
