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
