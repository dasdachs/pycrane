"""
Document.py contains the "model" for building a legal document.

A legal document(a Document object) usually consisit of a preamble, the body and a footer.

The pramble and the footer contain some initial text, the signing parties and
metadata and are optional. The main part of any legal document is the body.

The body of a legal document contains the articles. It can be dividen into
sections and subsections.

Articles are the atoms of a legal document. They can be divided into paragraphs
and/or lists.
"""
class Document(object):
    """
    Represents a legal document: preamble, body (divided into sections,
    subsections and articles) and a footer).

    The Document has a computed property "text" and a method "pretty_print" for
    displaying the legal document, but under the hood a Document is a DOM with
    sections, subsections and articles acting as nodes.
    """
    def __init__(self, title=None, preamble=None, body=None, footer=None):
        """
        :param title: a string representing the title
        :param preamble: an Element node that does not contain any articles
        :param body: a list conating Element nodes with articles
        :param footer: an Element node without an article at the end of the
         document
        """
        self.title = title
        self.preamble = preamble
        self.body = body
        self.footer = footer


class Article(object):
    """
    An Article is the main element of any bill or contract. It 
    """
    def __init__(self, article_number, paragraphs, title=None):
        """
        An article is divided into paragraphs. Paragraphs are
        represented by a Paragraph object.

        A usual article has the following structure:

        1. article number
        (a short title)

        First paragraph.

        Second paragraph:
        - a list item
        - a list item

        Third paragraph

        :param article_number: the article number (string)
        :param paragraphs: a tuple of Paragraphs (tuple)
        :param title: a special paragraph, usually the first (string)
         after the article num
        """
        self.article_number = article_number
        self.title = title
        self.paragraphs = paragraphs
   
    @property
    def text(self):
        paragraphs = [para.text for para in self.paragraphs]
        article_text = "".join(paragraphs)
        return article_text

    def __str__(self):
        return self.title if self.title else self.article_number

    def __repr__(self):
        return "Article <%s>" % self.article_number 


