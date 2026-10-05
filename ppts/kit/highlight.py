"""Syntax highlighting for slide code cards.

Returns, for each source line, a list of ``(text, role)`` spans. Roles are keys
into ``tokens.DARK_CODE`` / ``tokens.LIGHT_CODE``, so the same tokenisation
renders on either card. Python goes through the stdlib tokenizer; the other
languages use a scanner, which is plenty for the ten-line excerpts a slide holds.
"""
import io
import keyword
import re
import tokenize

Span = tuple  # (text, role)

PY_BUILTINS = {
    'abs', 'all', 'any', 'bool', 'dict', 'dir', 'enumerate', 'filter', 'float',
    'format', 'frozenset', 'getattr', 'hasattr', 'id', 'input', 'int',
    'isinstance', 'issubclass', 'iter', 'len', 'list', 'map', 'max', 'min',
    'next', 'object', 'open', 'print', 'range', 'repr', 'reversed', 'round',
    'set', 'setattr', 'sorted', 'str', 'sum', 'super', 'tuple', 'type', 'zip',
}

_KEYWORD_SRC = {
    'csharp': """abstract as base bool break byte case catch char checked class const continue
        decimal default delegate do double else enum event explicit extern false finally fixed
        float for foreach get goto if implicit in int interface internal is lock long namespace
        new null object operator out override params private protected public readonly ref return
        sbyte sealed set short sizeof stackalloc static string struct switch this throw true try
        typeof uint ulong unchecked unsafe ushort using var virtual void volatile while""",
    'cpp': """alignas alignof auto bool break case catch char class const constexpr continue
        decltype default delete do double else enum explicit export extern false float for friend
        goto if inline int long mutable namespace new noexcept nullptr operator private protected
        public register return short signed sizeof static struct switch template this throw true
        try typedef typename union unsigned using virtual void volatile while""",
    'vba': """And As Boolean ByRef ByVal Call Case Const Dim Do Double Each Else ElseIf End Enum
        Erase Error Exit False For Function Get Goto If In Integer Is Let Long Loop Me Mod New
        Next Not Nothing Object On Option Optional Or Preserve Private Property Public ReDim Rem
        Resume Return Select Set Single Static Step Stop String Sub Then To True Type Until
        Variant Wend While With Xor""",
    'sql': """ALTER AND AS ASC BY CREATE DELETE DESC DISTINCT DROP FROM GROUP HAVING IN INSERT
        INTO JOIN KEY LEFT LIMIT NOT NULL ON OR ORDER PRIMARY SELECT SET TABLE UPDATE VALUES
        WHERE""",
}
_KEYWORD_SRC.update({
    'javascript': """as async await break case catch class const continue debugger default delete do
        else enum export extends false finally for from function if implements import in
        instanceof interface keyof let new null of readonly return satisfies static super switch
        this throw true try type typeof undefined var void while yield""",
    'swift': """actor any as associatedtype async await break case catch class continue default
        defer deinit didSet do else enum extension fallthrough false fileprivate final for func
        get guard if import in init inout internal is lazy let mutating nil nonisolated open
        operator override private protocol public repeat rethrows return self Self set some
        static struct subscript super switch throw throws true try var weak where while willSet""",
    'kotlin': """as break class companion continue data do else enum false for fun if import in
        interface internal is lateinit null object override package private protected public
        return sealed super suspend this throw true try typealias val var when while""",
    'java': """abstract boolean break byte case catch char class continue default do double else
        enum extends false final finally float for if implements import instanceof int interface
        long new null package private protected public return short static super switch this
        throw throws true try void while""",
    'json': "true false null",
    'bash': """case do done elif else esac export fi for function if in then while""",
    'xml': "",
})
KEYWORDS: dict[str, set[str]] = {k: set(v.split())
                                 for k, v in _KEYWORD_SRC.items()}

LINE_COMMENT = {'csharp': '//', 'cpp': '//', 'java': '//', 'vba': "'", 'sql': '--',
                'javascript': '//', 'swift': '//', 'kotlin': '//', 'json': '\0',
                'bash': '#', 'xml': '<!--'}

# Languages whose keywords are case sensitive and whose capitalised names are types
# (React components, SwiftUI views, Kotlin classes). In these, ``Text`` is a type and
# ``text`` is a name, so the case-folding the VBA and SQL scanners need would be wrong.
CASE_SENSITIVE = {'javascript', 'swift', 'kotlin', 'java', 'json', 'bash', 'xml'}
CAPITALS_ARE_TYPES = {'javascript', 'swift', 'kotlin', 'java'}
TYPE_WORDS = {'csharp': {'Console', 'List', 'Math', 'String', 'WriteLine'},
              'cpp': {'std', 'cout', 'cin', 'endl', 'vector', 'string'},
              'vba': {'Cells', 'Range', 'Worksheets', 'MsgBox', 'ActiveSheet'}}


def _python(src: str) -> list[list[Span]]:
    lines = src.split('\n')
    out: list[list[Span]] = [[] for _ in lines]
    marks: list[list] = [[] for _ in lines]  # (col0, col1, role) per line
    prev_name = ''
    try:
        toks = list(tokenize.generate_tokens(io.StringIO(src).readline))
    except (tokenize.TokenError, IndentationError, SyntaxError):
        return _generic(src, None)

    for i, tok in enumerate(toks):
        (r0, c0), (r1, c1) = tok.start, tok.end
        role = None
        if tok.type == tokenize.COMMENT:
            role = 'com'
        elif tok.type in (tokenize.STRING, getattr(tokenize, 'FSTRING_START', -1),
                          getattr(tokenize, 'FSTRING_MIDDLE', -2),
                          getattr(tokenize, 'FSTRING_END', -3)):
            role = 'str'
        elif tok.type == tokenize.NUMBER:
            role = 'num'
        elif tok.type == tokenize.NAME:
            nxt = next((t.string for t in toks[i + 1:] if t.type != tokenize.NL), '')
            if keyword.iskeyword(tok.string) or tok.string in ('match', 'case'):
                role = 'kw'
            elif tok.string in ('self', 'cls'):
                role = 'self'
            elif prev_name == 'class':
                role = 'cls'
            elif nxt == '(' or tok.string in PY_BUILTINS:
                role = 'fn'
            prev_name = tok.string
        elif tok.type == tokenize.OP:
            role = 'op'
            prev_name = ''
        if role and r0 == r1 and r0 - 1 < len(marks):
            marks[r0 - 1].append((c0, c1, role))

    for n, line in enumerate(lines):
        spans, cur = [], 0
        for c0, c1, role in sorted(marks[n]):
            if c0 < cur:
                continue
            if c0 > cur:
                spans.append((line[cur:c0], 'text'))
            spans.append((line[c0:c1], role))
            cur = c1
        if cur < len(line):
            spans.append((line[cur:], 'text'))
        out[n] = [s for s in spans if s[0]]
    return out


# JavaScript, TypeScript and Swift: template literals are strings, a JSX tag name
# (<View, </Text) is a type, and a Swift attribute or property wrapper (@State,
# @Observable) is a keyword. Everything else matches the shared scanner.
_TOKEN_RE_C = re.compile(r"""
    (?P<str>"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|`(?:[^`\\]|\\.)*`)
  | (?P<tag>(?<=<)/?[A-Za-z][A-Za-z0-9_.]*|(?<=</)[A-Za-z][A-Za-z0-9_.]*)
  | (?P<attr>@[A-Za-z_][A-Za-z_0-9]*)
  | (?P<num>\b\d+\.?\d*\b)
  | (?P<word>[A-Za-z_#$][A-Za-z_0-9$]*)
  | (?P<space>\s+)
  | (?P<op>[^\sA-Za-z_0-9])
""", re.X)

_TOKEN_RE = re.compile(r"""
    (?P<str>"(?:[^"\\]|\\.)*"|'(?:[^'\\]|\\.)*'|<[A-Za-z_./]+>)
  | (?P<num>\b\d+\.?\d*\b)
  | (?P<word>[A-Za-z_#][A-Za-z_0-9]*)
  | (?P<space>\s+)
  | (?P<op>[^\sA-Za-z_0-9])
""", re.X)


def _generic(src: str, lang: str | None) -> list[list[Span]]:
    kws = KEYWORDS.get(lang or '', set())
    case = lang in CASE_SENSITIVE
    kws_lower = kws if case else {k.lower() for k in kws}
    caps = lang in CAPITALS_ARE_TYPES
    token_re = _TOKEN_RE_C if lang in ('javascript', 'swift', 'kotlin', 'java') else _TOKEN_RE
    types = TYPE_WORDS.get(lang or '', set())
    com = LINE_COMMENT.get(lang or '', '#')
    out = []
    for line in src.split('\n'):
        spans: list[Span] = []
        idx = line.find(com)
        # a comment marker inside a string literal is not a comment
        quotes = '"\'`' if lang in CASE_SENSITIVE else '"'
        if lang in CASE_SENSITIVE:      # skip markers inside strings, e.g. 'https://'
            while idx >= 0 and not all(line[:idx].count(q) % 2 == 0 for q in quotes):
                idx = line.find(com, idx + 1)
        if idx >= 0 and all(line[:idx].count(q) % 2 == 0 for q in quotes):
            body, tail = line[:idx], line[idx:]
        else:
            body, tail = line, ''
        for m in token_re.finditer(body):
            kind, text = m.lastgroup or 'text', m.group()
            if kind == 'tag':
                role = 'cls'
            elif kind == 'attr':
                role = 'kw'
            elif kind == 'word':
                if (text if case else text.lower()) in kws_lower:
                    role = 'kw'
                elif text in types or (caps and text[:1].isupper()):
                    role = 'cls'
                elif body[m.end():m.end() + 1] == '(':
                    role = 'fn'
                elif text.startswith('#'):
                    role = 'kw'
                else:
                    role = 'text'
            elif kind == 'space':
                role = 'text'
            else:
                role = kind
            spans.append((text, role))
        if tail:
            spans.append((tail, 'com'))
        out.append(_merge(spans))
    return out


_XL_RE = re.compile(r"""
    (?P<str>"(?:[^"]|"")*")
  | (?P<ref>(?:'[^']+'|[A-Za-zÁÉÍÓÚÑ_][\wÁÉÍÓÚÑáéíóúñ ]*)!\$?[A-Z]{1,3}\$?\d+(?::\$?[A-Z]{1,3}\$?\d+)?
        | \$?[A-Z]{1,3}\$?\d+(?::\$?[A-Z]{1,3}\$?\d+)?\b
        | \$?[A-Z]{1,3}:\$?[A-Z]{1,3}\b)
  | (?P<err>\#[A-ZÁÉÍÓÚÑ¡/!.?]+[!]?)
  | (?P<fn>[A-Za-zÁÉÍÓÚÑ_][A-Za-z0-9ÁÉÍÓÚÑáéíóúñ_.]*(?=\s*\())
  | (?P<num>\b\d+(?:[.,]\d+)?%?)
  | (?P<word>[A-Za-zÁÉÍÓÚÑ_][\wÁÉÍÓÚÑáéíóúñ]*)
  | (?P<space>\s+)
  | (?P<op>[^\sA-Za-z_0-9])
""", re.X)

# roles the excel scanner emits, mapped onto the code-card palette
_XL_ROLE = {'str': 'str', 'ref': 'cls', 'err': 'com', 'fn': 'fn', 'num': 'num',
            'word': 'kw', 'space': 'text', 'op': 'op'}


def _excel(src: str) -> list[list[Span]]:
    """Scan a spreadsheet formula.

    Excel has no comment syntax, and `#` opens an error value rather than a
    comment, so this cannot go through ``_generic``: `#N/A` would swallow the
    rest of the line. Function names carry dots in Spanish (SUMAR.SI.CONJUNTO),
    which the generic word pattern splits into three.
    """
    out = []
    for line in src.split('\n'):
        spans = [(m.group(), _XL_ROLE.get(m.lastgroup or '', 'text'))
                 for m in _XL_RE.finditer(line)]
        out.append(_merge(spans))
    return out


def _merge(spans: list[Span]) -> list[Span]:
    """Collapse neighbouring spans of the same role — fewer runs, smaller XML."""
    merged: list[list] = []
    for text, role in spans:
        if merged and merged[-1][1] == role:
            merged[-1][0] += text
        else:
            merged.append([text, role])
    return [(t, r) for t, r in merged if t]


def highlight(src: str, lang: str = 'python') -> list[list[Span]]:
    """Tokenise ``src`` into per-line coloured spans."""
    src = src.replace('\t', '    ').rstrip('\n')
    lang = (lang or '').lower()
    if lang in ('py', 'python'):
        return _python(src)
    if lang in ('excel', 'xl', 'formula'):
        return _excel(src)
    if lang in ('text', 'output', 'console', 'plain', ''):
        return [[(l, 'text')] for l in src.split('\n')]
    return _generic(src, {'cs': 'csharp', 'c++': 'cpp', 'c': 'cpp',
                          'js': 'javascript', 'jsx': 'javascript', 'ts': 'javascript',
                          'tsx': 'javascript', 'typescript': 'javascript',
                          'swiftui': 'swift', 'kt': 'kotlin', 'sh': 'bash', 'shell': 'bash',
                          'zsh': 'bash', 'terminal': 'bash', 'html': 'xml',
                          'plist': 'xml'}.get(lang, lang))
