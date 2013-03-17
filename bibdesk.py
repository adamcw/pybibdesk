from appscript import app

class BibDesk:  
    def __init__(self):
        self.app = app('BibDesk')
        
    def import_reference(self, ref):
        a = self.app

        # Insert the reference
        doc = a.import_(a.document.get()[0], from_=ref)

        # Auto-generate a cite-key
        item = a.documents.get()[0].selection.get()[0]
        item.cite_key.set(item.generated_cite_key())
