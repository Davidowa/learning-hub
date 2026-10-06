"""Extract the explanatory prose of slide decks into markdown, one file per deck,
one field per paragraph, and a sidecar .map.tsv giving the slide and field of every line, so the-writer's lint can be run on it
and each finding traced back to file, slide and field.

    python3 ppts/audit/herramientas/extraer_prosa.py OUTDIR deck.yaml [deck.yaml ...]
"""
import os, sys, yaml

PROSE = {'title', 'subtitle', 'unit', 'lead', 'lede', 'desc', 'text', 'brief', 'sub', 'head',
         'caption', 'note', 'notes', 'statement', 'question', 'verdict', 'before', 'after',
         'eyebrow', 'kicker', 'label', 'value', 'author', 'source_note', 'alt', 'body', 'why'}
SKIP = {'source', 'output', 'filename', 'lang', 'image', 'state', 'num', 'accent', 'dark',
        'theme', 'side', 'key'}

def walk(node, path, out):
    if isinstance(node, dict):
        for k, v in node.items():
            if k in SKIP:
                continue
            walk(v, path + [str(k)], out)
    elif isinstance(node, list):
        for i, v in enumerate(node):
            walk(v, path + [str(i)], out)
    elif isinstance(node, str):
        leaf = path[-1] if path else ''
        if leaf in PROSE or (leaf.isdigit() and len(path) > 1 and path[-2] in ('rows', 'headers', 'items', 'cells', 'options', 'phases', 'points', 'meta', 'rubric')):
            s = node.strip()
            if s and not s.replace('.', '').replace(' ', '').isdigit():
                out.append(('.'.join(path), s))

def main():
    outdir, files = sys.argv[1], sys.argv[2:]
    os.makedirs(outdir, exist_ok=True)
    for f in files:
        doc = yaml.safe_load(open(f, encoding='utf-8'))
        lines, where = [], []
        for i, entry in enumerate(doc.get('slides', []), 1):
            (layout, kw), = entry.items()
            out = []
            walk(kw or {}, [], out)
            for loc, s in out:
                for j, para in enumerate(s.split('\n\n')):
                    where.append((len(lines) + 1, f's{i} {layout} {loc}'))
                    lines.append(' '.join(para.split()))
                    lines.append('')
        name = os.path.basename(f).replace('.yaml', '.md')
        open(os.path.join(outdir, name), 'w', encoding='utf-8').write('\n'.join(lines))
        with open(os.path.join(outdir, name.replace('.md', '.map.tsv')), 'w', encoding='utf-8') as fh:
            fh.write(f'# deck: {f}\n# line\tslide layout field\n')
            for ln, loc in where:
                fh.write(f'{ln}\t{loc}\n')
        print(os.path.join(outdir, name))

if __name__ == '__main__':
    main()
