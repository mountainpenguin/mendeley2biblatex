class FormatedEntry:
    TEMPLATES = {
        'JournalArticle': '''
@article{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    journal   = "{entry[publication]}",
    number    = "{entry[issue]}",
    volume    = "{entry[volume]}",
    pages     = "{entry[pages]}",
    year      = "{entry[year]}",
    doi       = "{entry[doi]}",
    localfile = "{entry[localUrl]}"
}}''',
        'ConferenceProceedings': '''
@proceedings{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    publisher = "{entry[publisher]}",
    pages     = "{entry[pages]}",
    year      = "{entry[year]}",
    doi       = "{entry[doi]}",
    localfile = "{entry[localUrl]}"
}}''',
        'WebPage': '''
@online{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    year      = "{entry[year]}",
    url       = "{entry[url]}",
    urldate   = "{entry[dateAccessed]}"
}}''',
        'Book': '''
@book{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    publisher = "{entry[publisher]}",
    year      = "{entry[year]}",
    volume    = "{entry[volume]}",
    doi       = "{entry[doi]}",
    localfile = "{entry[localUrl]}"
}}'''
    }
