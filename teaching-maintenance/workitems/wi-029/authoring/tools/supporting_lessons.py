"""Read the two maintained Markdown lessons and verified illustration manifest."""
from pathlib import Path
import hashlib
import json
import re
from PIL import Image

FIELDS = ('情境', '原理', '重點', '取捨', '自測', '解析')

def parse_lesson(text: str) -> dict:
    heading = re.match(r'# (.+)\n', text)
    if not heading:
        raise ValueError('Missing lesson title')
    parts = re.split(r'^## ([a-z-]+) \| (.+)$', text, flags=re.M)
    result = {'title': heading[1], 'intro': parts[0][heading.end():].strip(), 'chapters': []}
    for index in range(1, len(parts), 3):
        slug, title, body = parts[index:index+3]
        sections = re.split(r'^### (.+)$', body, flags=re.M)
        keys = sections[1::2]
        if set(keys) != set(FIELDS) or len(keys) != len(FIELDS):
            raise ValueError(f'{slug}: missing or duplicate sections')
        fields = dict(zip(keys, [s.strip() for s in sections[2::2]]))
        if any(not value for value in fields.values()):
            raise ValueError(f'{slug}: empty section')
        points = fields['重點'].splitlines()
        if len(points) != 3 or any(not p.startswith('- ') for p in points):
            raise ValueError(f'{slug}: expected three readable points')
        result['chapters'].append({'id': slug, 'title': title, 'case': fields['情境'], 'principle': fields['原理'], 'points': [p[2:] for p in points], 'tradeoff': fields['取捨'], 'question': fields['自測'], 'answer': fields['解析']})
    ids = [c['id'] for c in result['chapters']]
    if len(ids) != 3 or len(set(ids)) != len(ids) or not result['intro']:
        raise ValueError('Expected three distinct chapters and an introduction')
    return result

def load_lessons(root: Path) -> dict:
    directory = root / '_course_content/supporting-lessons'
    manifest = json.loads((directory / 'assets.json').read_text(encoding='utf-8'))
    output = {}
    for view in ('foundations', 'production'):
        lesson = parse_lesson((directory / f'{view}.md').read_text(encoding='utf-8'))
        for chapter in lesson['chapters']:
            record = manifest[chapter['id']]
            for mode in ('desktop', 'mobile'):
                asset = record[mode]
                path = (root / asset['path']).resolve()
                if not path.is_relative_to(root.resolve()) or asset['review'] != 'self-reviewed':
                    raise ValueError('Unreviewed or invalid lesson asset')
                if hashlib.sha256(path.read_bytes()).hexdigest() != asset['sha256']:
                    raise ValueError(f'Changed asset: {path}')
                with Image.open(path) as image:
                    if list(image.size) != asset['size']:
                        raise ValueError(f'Unexpected dimensions: {path}')
                chapter[mode] = asset
            chapter['image_title'] = record['title']
        lesson['sources'] = json.loads((directory / 'sources.json').read_text(encoding='utf-8'))[view]
        lesson['source'] = f'_course_content/supporting-lessons/{view}.md'
        output[view] = lesson
    return output
