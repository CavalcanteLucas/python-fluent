import unicodedata

from ex_4_16__sanitize import shave_marks_latin

single_map = str.maketrans("""‚ƒ„†ˆ‹‘’“”•–—˜›""", """'f"*^<''""---~>""")

multi_map = str.maketrans(
    {
        '€': '<euro>',
        '…': '...',
        'Œ': 'OE',
        '™': '(TM)',
        'œ': 'oe',
        '‰': '<per mille>',
        '‡': '**',
    }
)

multi_map.update(single_map)


def dewinize(txt):
    """Replace Win1252 symbols with ASCII chars or sequence"""
    return txt.translate(multi_map)


def asciize(txt):
    no_marks = shave_marks_latin(dewinize(txt))
    no_marks = no_marks.replace('ß', 'ss')
    return unicodedata.normalize('NFKC', no_marks)
