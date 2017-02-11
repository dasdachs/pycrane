
# Python2 ARTICLE_TOKEN = re.compile(r"\d\.\s\w+(?=\n)", re.UNICODE)
ARTICLE_TOKEN = re.compile(r"\d\.\s\w+(?=\n)")
PARAGRAPH_TOKEN = re.compile(r"")


def parse_text(text=None, file=None):
    """
    Parses a string, an StringIO object or opens a file.
    """
    if not text:
        text = open(file).readlines()
    parsed_text = re.split(ARTICLE_TOKEN, text)
    return parsed_text
tmp = t[:]
    ...: for x in re.findall(, t):
            ...:     found = tmp[:tmp.find(x)]
                ...:     print(found)
                    ...:     tmp = tmp.split(found)[1]
                        ...:     print(10*"=")
                            ...: print(tmp)
