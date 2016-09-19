baseurl = "https://sammlungonline.mkg-hamburg.de/resource-cache/mkg/1/"

class Item:
    inventory_no = ""
    title = ""
    display_date = ""

    @property
    def uri(self):
        return baseurl + self.inventory_no + '.jpg'

    def __init__(self, inventory_no, title):
        self.inventory_no = inventory_no
        self.title        = title