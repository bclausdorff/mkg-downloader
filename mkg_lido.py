from enum import Enum
from filter import unwrap_element
from const import *

class EventType(Enum):
    Ereignis         = "Ereignis"
    Entwurf          = "Entwurf"
    Vertrieb         = "Vertrieb"
    Ausführung       = "Ausführung"
    Ausstellung      = "Ausstellung"
    Fund             = "Fund"
    Bearbeitung      = "Bearbeitung"
    Auftrag          = "Auftrag"
    Herstellung      = "Herstellung"
    Geistige         = "Geistige"
    Schöpfung        = "Schöpfung"
    Vollendung       = "Vollendung"
    Veröffentlichung = "Veröffentlichung"

class EventDate:
    display_date  = ""
    earliest_date = ""
    latest_date   = ""
    eventType     = ""

    def __init__(self, display_date: str, earliest_date: str, latest_date: str, eventType: EventType):
        self.display_date  = display_date
        self.earliest_date = earliest_date
        self.latest_date   = latest_date
        self.eventType     = eventType

    @classmethod
    def fromEventWrap(self, elem, eventType):
        events = elem.findall('.//lido:eventWrap//lido:eventSet', namespaces)
        for e in events:
            term = e.find('.//lido:eventType//lido:term', namespaces)
            if term.text == eventType.value:
                display_date  = unwrap_element(e.find('.//lido:eventDate//lido:displayDate', namespaces))
                earliest_date = unwrap_element(e.find('.//lido:eventDate//lido:earliestDate', namespaces))
                latest_date   = unwrap_element(e.find('.//lido:eventDate//lido:latestDate', namespaces))
                return EventDate(display_date, earliest_date, latest_date, eventType)

    def __str__(self):
        return "EventDate for %s: display is %s, earliest is %s, latest is %s" % (self.eventType.value, self.display_date, self.earliest_date, self.latest_date)