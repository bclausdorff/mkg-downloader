#baseurl = "https://sammlungonline.mkg-hamburg.de/resource-cache/mkg/1/"
baseurl = "https://sammlungonline.mkg-hamburg.de/de/object/{}/image_download/0"

class Item:
    record_id = ""
    inventory_no = ""
    title = ""
    display_date = ""

    @property
    def uri(self):
        return baseurl.format(self.record_id)

    def __init__(self, record_id, inventory_no, title):
        self.record_id    = record_id
        self.inventory_no = inventory_no
        self.title        = title