from elasticsearch_dsl import Document, Date, Keyword, Text
from constants import ESIndex

class PopplyPopup(Document):
    title = Text() 
    location = Text()
    period = Text()
    link = Keyword()
    created_at = Date()

    class Index:
        name = ESIndex.POPPLY_POPUPS