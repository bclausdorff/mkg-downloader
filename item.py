from mkg_lido import EventDate

#baseurl = "https://sammlungonline.mkg-hamburg.de/resource-cache/mkg/1/"
baseurl = "https://sammlungonline.mkg-hamburg.de/de/object/{}/image_download/0"

class Item:
    record_id = ""
    inventory_no = ""
    title = ""
    description = ""
    date = None

    @property
    def uri(self):
        return baseurl.format(self.record_id)

    def __init__(self, record_id, inventory_no, title, description, date: EventDate):
        self.record_id    = record_id
        self.inventory_no = inventory_no
        self.title        = title
        self.description  = description
        self.date         = date

    def toJSON(self):
        return dict(record_id=self.record_id, inventory_no=self.inventory_no, title=self.title, description=self.description, date=self.date)