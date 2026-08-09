"""Design tokens lifted from Programming_course_slide_template.pptx.

Every number here was measured off the template, so a deck built with the kit
lines up with a slide the template already ships.

Colour is split into per-language palettes. The template's own blue and duck
orange stay as ``generic``; a Python deck reads in Python blue and Python
yellow, per the "use colours related to the language" rule in guidelines.md.
Every text colour listed here clears WCAG AA (4.5:1) against the surface it
sits on.
"""

# ─────────────────────────────────────────────── type
# The template designs in Instrument Serif / Inter Tight / JetBrains Mono and
# ships Georgia / Arial / Courier New so the file renders anywhere. Same here.
SERIF = 'Georgia'
SANS  = 'Arial'
MONO  = 'Courier New'


# Every size the template uses, named. Nothing below 18 pt (~24 px projected).
class T:
    cover_title    = 81.0
    cover_sub      = 28.5
    divider_title  = 75.0
    divider_lede   = 27.0
    stat           = 132.0
    quote          = 46.5
    closing_title  = 88.0
    statement      = 36.0
    title          = 43.5
    card_num       = 33.0
    arrow          = 33.0
    h2             = 30.0
    lead           = 27.0
    head           = 25.5
    card_title     = 24.0
    block_title    = 23.25
    serif_inline   = 30.0
    value          = 22.5
    body           = 22.5
    note           = 21.75
    step           = 21.0
    sub            = 20.25
    code           = 20.25
    card_body      = 19.5
    eyebrow        = 18.0
    label          = 18.75
    caption        = 18.0


# line-spacing multipliers, straight from the template
class LS:
    cover_title   = 0.90433
    divider_title = 0.92105
    title         = 0.95224
    card_title    = 1.01053
    head          = 1.06250
    body          = 1.17419
    lead          = 1.17209
    sub           = 1.21935
    desc          = 1.20690
    note          = 1.23030
    step          = 1.22500
    loose         = 1.26290
    code          = 1.45778


# ─────────────────────────────────────────────── geometry (inches)
SLIDE_W, SLIDE_H = 20.0, 11.25
M          = 1.04          # left margin — everything hangs off this
CONTENT_W  = 17.92         # margin to margin
EYEBROW_Y  = 0.92
TITLE_Y    = 1.41
TITLE_W    = 14.21
BODY_Y     = 2.57          # first content row on a titled slide
FOOTER_RULE_Y = 9.76
FOOTER_Y      = 10.14
FOOTER_LOGO   = (1.04, 10.10, 0.35, 0.35)
PAGENUM_X     = 18.66

# four-up card grid
CARD_Y, CARD_W, CARD_H, CARD_STEP = 2.61, 4.26, 3.25, 4.5533
PAD = 0.35                 # card inner padding

# code card
CODE_X, CODE_Y, CODE_W = 1.04, 2.49, 10.40
CODE_HEADER_H = 0.70
CODE_LINE_1   = 3.55
CODE_LINE_STEP = 0.4555
CODE_STEP = 0.75           # code shrinks in fixed steps, so a deck reads even
CODE_MAX_LINES = 18        # the card shrinks the type to fit; past this, split the slide
ANNOT_X, ANNOT_W = 12.03, 6.93     # 12.03 + 6.93 lands exactly on the right margin


# ─────────────────────────────────────────────── palettes
class Palette:
    """Colour slots a layout can ask for. Values are hex, no leading hash."""

    def __init__(self, **kw):
        self.__dict__.update(kw)


# Surfaces and neutrals are shared. Only the accent pair and the code theme
# change from one language to the next.
#
# On comment grey. The dark themes used to set `com` to 6B7F9E, which is 4.18:1
# on the navy card. Code sets at 20.25 pt, so WCAG counts it as large text and
# 4.18 clears that bar, but this file promises 4.5 for every colour in it and a
# comment is the run most likely to be read from the back of a room. 7789A6 is
# 4.80:1 and still recedes behind the code, which is what a comment should do.
# The two Office palettes never had the problem; their comment greys were chosen
# against the green canvas and already sat above 6:1.
_NEUTRAL = dict(
    NAVY='0B1B3A',      # dark canvas, code cards, the "process" block
    PAPER='F7F8FA',     # light canvas
    WHITE='FFFFFF',     # cards on paper
    PANEL='EEF2F8',     # card headers, table zebra
    BORDER='DBE3EF',    # 0.75 pt hairline, rules, inactive bars
    INK='0F172A',       # primary text on light
    MUTED='5B6B84',     # secondary text on light, 5.1:1 on paper
    ON_NAVY='F7F8FA',
    ON_NAVY_SOFT='B8C8E4',
    ON_NAVY_DIM='7F97BF',
)

GENERIC = Palette(
    **_NEUTRAL,
    BLUE='2563EB',       # structure text, 4.9:1 on paper
    BLUE_FILL='2563EB',  # chips and bars that carry white text
    BLUE_DEEP='1D4ED8',
    ACCENT='E8871E',     # accent on navy, 6.4:1
    ACCENT_LO='B4530A',  # accent on paper, 4.7:1
    ON_NAVY_LINK='93B4FF',
    DARK_CODE=dict(bg='0B1B3A', text='E6EDF7', kw='7AA2FF', fn='9ECBFF', num='F0A868',
                   str='F5B461', com='7789A6', cls='A5C8FF', op='B8C8E4', self='E8871E',
                   dot='E8871E', chrome='7F97BF', rule='F7F8FA', header=None),
    LIGHT_CODE=dict(bg='FFFFFF', text='0F172A', kw='1D4ED8', fn='1D4ED8', num='B4530A',
                    str='B4530A', com='5B6B84', cls='1D4ED8', op='5B6B84', self='B4530A',
                    dot='2563EB', chrome='5B6B84', rule='DBE3EF', header='EEF2F8'),
)

# Python's own two colours: the brand blue and the logo yellow FFD43B. The yellow
# is darkened on paper and runs bright on navy. Blue marks the language itself,
# yellow marks the names you wrote.
#
# The blue is 306998, the one the Python brand guidelines publish. The kit used to
# carry 3776AB, the older python.org blue, darkened to 2B5F8F for text because
# 3776AB only reaches 4.55:1 on paper and 4.84:1 under white. 306998 needs neither
# trick: 5.5:1 on paper and 5.8:1 with white on it, so one brand-exact colour fills
# both slots, the way the C++ blue already does.
PYTHON = Palette(
    **_NEUTRAL,
    BLUE='306998',       # brand blue, 5.5:1 on paper
    BLUE_FILL='306998',  # white text on it is 5.8:1
    BLUE_DEEP='244E72',  # the same blue at 75 %, 8.2:1 on paper
    ACCENT='FFD43B',     # logo yellow on navy, 12.0:1
    ACCENT_LO='8A6A00',  # logo yellow darkened, 4.8:1 on paper
    ON_NAVY_LINK='8AB8E0',
    DARK_CODE=dict(bg='0B1B3A', text='E6EDF7', kw='8AB8E0', fn='FFD43B', num='FFE873',
                   str='E3B778', com='7789A6', cls='B5D3EC', op='B8C8E4', self='FFD43B',
                   dot='FFD43B', chrome='7F97BF', rule='F7F8FA', header=None),
    LIGHT_CODE=dict(bg='FFFFFF', text='0F172A', kw='306998', fn='244E72', num='8A6A00',
                    str='8A6A00', com='5B6B84', cls='306998', op='5B6B84', self='8A6A00',
                    dot='306998', chrome='5B6B84', rule='DBE3EF', header='EEF2F8'),
)

# The ISO C++ blues. 00599C is the logo blue and clears AA on paper as it is, so
# unlike Python's yellow it needs no darkening. C++ has no second brand colour, so
# the accent pair stays the academy's duck orange: that keeps "the accent means
# this is the risk" readable instead of collapsing it into another blue.
CPP = Palette(
    **_NEUTRAL,
    BLUE='00599C',       # logo blue, 6.8:1 on paper
    BLUE_FILL='00599C',  # white text on it is 7.2:1
    BLUE_DEEP='004482',
    ACCENT='E8871E',     # duck orange on navy, 6.4:1
    ACCENT_LO='B4530A',  # duck orange on paper, 4.7:1
    ON_NAVY_LINK='9CC3E8',
    DARK_CODE=dict(bg='0B1B3A', text='E6EDF7', kw='8AB4DE', fn='9CC3E8', num='F0A868',
                   str='E3B778', com='7789A6', cls='B5D3EC', op='B8C8E4', self='F0A868',
                   dot='E8871E', chrome='7F97BF', rule='F7F8FA', header=None),
    LIGHT_CODE=dict(bg='FFFFFF', text='0F172A', kw='00599C', fn='004482', num='B4530A',
                    str='B4530A', com='5B6B84', cls='00599C', op='5B6B84', self='B4530A',
                    dot='00599C', chrome='5B6B84', rule='DBE3EF', header='EEF2F8'),
)

# The dark canvas for the two Office palettes. The template's own dark surface is
# NAVY, and it is the right neutral for a language whose logo is blue; for Excel
# it left every cover, divider and code card reading in a colour the program does
# not use. 0B2A1B is the same hue family as the brand green, taken down to a
# canvas. It sits a little lighter than NAVY (0.018 against 0.012 relative
# luminance), so the secondary text and the comment colour are re-tuned below
# rather than inherited: the blue-greys would read as a different palette showing
# through, and the shared comment grey, which already misses AA on NAVY at
# 4.18:1, would drop to 3.79:1 here.
#
# This overrides the slot for these two palettes only. GENERIC, PYTHON and CPP
# keep _NEUTRAL untouched.
_OFFICE_DARK = dict(
    NAVY='0B2A1B',           # deep Excel green, white text at 14.5:1
    ON_NAVY='F7F8FA',        # 14.5:1
    ON_NAVY_SOFT='BEDACB',   # 10.3:1
    ON_NAVY_DIM='8FB3A0',    # 6.7:1
)

# Office green. Excel publishes four greens and this palette uses all four, each
# on the surface where it clears AA, which is the same split the Python yellow
# gets. 107C41 is 5.0:1 on paper and takes white at 5.3:1, so it carries the
# structure; 185C37 is the darkest at 7.5:1; 33C481 is 2.1:1 on paper and useless
# there, but 6.9:1 on the green canvas, so it carries the keywords in the dark
# code card. 21A366 is the one that fits nowhere comfortably, 3.0:1 on paper and
# 4.8:1 on the canvas, and it is left out.
#
# The kit used to carry 217346 here, which is not a published Excel green at all.
# It read slightly better than 107C41, 5.5:1 against 5.0:1, and both clear the
# bar, so the brand-exact colour wins.
#
# VBA has no second brand colour either, so the accent pair stays the academy's
# duck orange, which keeps "the accent means this is the risk" from collapsing
# into a second green.
#
# In the syntax theme green marks the language (Sub, Dim, End, For) and its
# objects (Range, Cells, Worksheets), and the warm pair marks literals: what the
# recorder wrote down from what you typed.
VBA = Palette(
    **{**_NEUTRAL, **_OFFICE_DARK},
    BLUE='107C41',       # Excel forest green, 5.0:1 on paper
    BLUE_FILL='107C41',  # white text on it is 5.3:1
    BLUE_DEEP='185C37',
    ACCENT='E8871E',     # duck orange on the green canvas, 5.8:1
    ACCENT_LO='B4530A',  # duck orange on paper, 4.7:1
    ON_NAVY_LINK='33C481',
    DARK_CODE=dict(bg='0B2A1B', text='E6EDF7', kw='33C481', fn='8FD3AB', num='F0A868',
                   str='E3B778', com='93AE9E', cls='B7E4CB', op='BEDACB', self='F0A868',
                   dot='E8871E', chrome='8FB3A0', rule='F7F8FA', header=None),
    LIGHT_CODE=dict(bg='FFFFFF', text='0F172A', kw='107C41', fn='185C37', num='B4530A',
                    str='B4530A', com='5B6B84', cls='107C41', op='5B6B84', self='B4530A',
                    dot='107C41', chrome='5B6B84', rule='DBE3EF', header='EEF2F8'),
)

# The same Office green, for a deck whose code cards hold spreadsheet formulas
# rather than VBA. It is a separate palette rather than an alias because the
# formula scanner in highlight.py emits a different set of roles: `com` never
# carries a comment, since Excel has no comment syntax, it carries an error
# value such as #N/A or #¡DIV/0!. So `com` here is the accent, which keeps the
# "the accent means this is the risk" rule intact instead of burying an error in
# comment grey. Literals drop to the neutral, because in a formula the reference
# and the error matter more than the number you typed inside it.
EXCEL = Palette(
    **{**_NEUTRAL, **_OFFICE_DARK},
    BLUE='107C41',       # Excel forest green, 5.0:1 on paper
    BLUE_FILL='107C41',  # white text on it is 5.3:1
    BLUE_DEEP='185C37',
    ACCENT='E8871E',     # duck orange on the green canvas, 5.8:1
    ACCENT_LO='B4530A',  # duck orange on paper, 4.7:1
    ON_NAVY_LINK='33C481',
    DARK_CODE=dict(bg='0B2A1B', text='E6EDF7', kw='8FD3AB', fn='33C481', num='BEDACB',
                   str='BEDACB', com='E8871E', cls='B7E4CB', op='BEDACB', self='F0A868',
                   dot='E8871E', chrome='8FB3A0', rule='F7F8FA', header=None),
    LIGHT_CODE=dict(bg='FFFFFF', text='0F172A', kw='185C37', fn='185C37', num='5B6B84',
                    str='5B6B84', com='B4530A', cls='107C41', op='5B6B84', self='B4530A',
                    dot='107C41', chrome='5B6B84', rule='DBE3EF', header='EEF2F8'),
)

# C# publishes one colour, the purple 9179E4, and it cannot carry text as it is:
# 3.3:1 on paper and 3.5:1 under white. It gets the same treatment the Python
# yellow gets, which is the pattern this file already has for a brand colour that
# will not sit on a light surface. The purple at 70 % is 6.0:1 on paper and takes
# white at 6.3:1, so it fills the structure slots; the purple lightened is 6.1:1
# on navy and carries the keywords in the dark code card. Like C++ and VBA, C# has
# no second brand colour, so the accent pair stays the academy's duck orange.
#
# No COM101 deck exists yet. The palette is here so that the first one does not
# start by inventing colours.
CSHARP = Palette(
    **_NEUTRAL,
    BLUE='65549F',       # brand purple at 70 %, 6.0:1 on paper
    BLUE_FILL='65549F',  # white text on it is 6.3:1
    BLUE_DEEP='574888',  # at 60 %, 7.4:1 on paper
    ACCENT='E8871E',     # duck orange on navy, 6.4:1
    ACCENT_LO='B4530A',  # duck orange on paper, 4.7:1
    ON_NAVY_LINK='A18DE8',
    DARK_CODE=dict(bg='0B1B3A', text='E6EDF7', kw='A18DE8', fn='B7A7ED', num='F0A868',
                   str='E3B778', com='7789A6', cls='C9BDF2', op='B8C8E4', self='F0A868',
                   dot='E8871E', chrome='7F97BF', rule='F7F8FA', header=None),
    LIGHT_CODE=dict(bg='FFFFFF', text='0F172A', kw='65549F', fn='574888', num='B4530A',
                    str='B4530A', com='5B6B84', cls='65549F', op='5B6B84', self='B4530A',
                    dot='65549F', chrome='5B6B84', rule='DBE3EF', header='EEF2F8'),
)

# The dark canvas for the MySQL palette. The template navy would work on contrast
# alone, but MySQL teal 00758F and the C++ blue 00599C are close enough that a
# navy deck in teal reads as a C++ deck at a glance, and the two courses run in
# the same term. Shifting the dark surface into the same teal family separates
# them on sight. Every value clears AA against 0A1F2B.
_DB_DARK = dict(
    NAVY='0A1F2B',           # deep MySQL teal, white text at 15.9:1
    ON_NAVY='F7F8FA',        # 15.9:1
    ON_NAVY_SOFT='BBD3DC',   # 10.8:1
    ON_NAVY_DIM='8FAAB5',    # 6.9:1
)

# MySQL publishes two colours and, unlike C++, VBA and C#, both of them are
# usable, so this is the only palette besides Python whose accent is the language's
# own rather than the academy's duck. They split by surface the way the Python
# pair does: the teal is 5.0:1 on paper and only 3.2:1 on a dark canvas, so it
# carries the structure on light; the orange is 2.2:1 on paper and 7.1:1 on the
# teal canvas, so it carries the accent on dark and is darkened to 91570A, 5.9:1,
# when it has to sit on white.
#
# In the syntax theme teal marks the language (SELECT, FROM, WHERE, JOIN) and the
# orange pair marks what you wrote into the query: the aggregate functions, the
# numbers and the strings.
MYSQL = Palette(
    **{**_NEUTRAL, **_DB_DARK},
    BLUE='00758F',       # brand teal, 5.0:1 on paper
    BLUE_FILL='00758F',  # white text on it is 5.3:1
    BLUE_DEEP='00576B',  # the same teal at 75 %, 8.2:1 on white
    ACCENT='F29111',     # brand orange on the teal canvas, 7.1:1
    ACCENT_LO='91570A',  # brand orange darkened, 5.9:1 on white
    ON_NAVY_LINK='72B3C1',
    DARK_CODE=dict(bg='0A1F2B', text='E6EDF7', kw='72B3C1', fn='F29111', num='F0A868',
                   str='E3B778', com='7789A6', cls='8CC0CC', op='B8C8E4', self='F29111',
                   dot='F29111', chrome='8FAAB5', rule='F7F8FA', header=None),
    LIGHT_CODE=dict(bg='FFFFFF', text='0F172A', kw='00758F', fn='91570A', num='91570A',
                    str='91570A', com='5B6B84', cls='00576B', op='5B6B84', self='91570A',
                    dot='00758F', chrome='5B6B84', rule='DBE3EF', header='EEF2F8'),
)

PALETTES = {'generic': GENERIC, 'python': PYTHON, 'cpp': CPP, 'csharp': CSHARP,
            'vba': VBA, 'excel': EXCEL, 'mysql': MYSQL}


def palette(name: str) -> Palette:
    """Look up a language palette, falling back to the template's own colours."""
    return PALETTES.get((name or 'generic').lower(), GENERIC)
