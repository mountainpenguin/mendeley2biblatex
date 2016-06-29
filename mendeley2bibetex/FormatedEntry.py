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
}}''',
        'ConferenceProceedings': '''
@proceedings{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    publisher = "{entry[publisher]}",
    pages     = "{entry[pages]}",
    year      = "{entry[year]}",
    doi       = "{entry[doi]}",
}}''',
        'WebPage': '''
@online{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    year      = "{entry[year]}",
    url       = "{entry[url]}",
    urldate   = "{entry[urldate]}"
}}''',
        'Book': '''
@book{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    publisher = "{entry[publisher]}",
    year      = "{entry[year]}",
    pages     = "{entry[pages]}",
    volume    = "{entry[volume]}",
    doi       = "{entry[doi]}",
}}''',
        'BookSection': '''
@inbook{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    booktitle = "{entry[publication]}"
    publisher = "{entry[publisher]}",
    year      = "{entry[year]}",
    volume    = "{entry[volume]}",
    pages     = "{entry[pages]}",
    doi       = "{entry[doi]}",
    url       = "{entry[url]}",
    urldate   = "{entry[urldate]}"
}}''',
        'Report': '''
@inbook{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    type = "{entry[publication]}"
    institution = "{entry[institution]}",
    year      = "{entry[year]}",
    type      = "{entry[sourceType]}",
    doi       = "{entry[doi]}",
    pages     = "{entry[pages]}",
    url       = "{entry[url]}",
    urldate   = "{entry[urldate]}"
}}''',
        'Thesis': '''
@thesis{{{entry[citationKey]},
    author    = "{entry[authors]}",
    title     = "{entry[title]}",
    institution = "{entry[institution]}",
    year      = "{entry[year]}",
    type      = "{entry[sourceType]}",
    doi       = "{entry[doi]}",
    pages     = "{entry[pages]}",
    url       = "{entry[url]}",
    urldate   = "{entry[urldate]}"
}}'''
    }
