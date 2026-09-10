from pathlib import Path
C=Path(__file__).resolve().parents[2];p=C/'tools/build_interactive_learning_html.py'
s=p.read_text(encoding='utf-8')
anchor='    function lessonStepHTML(topic, slide, first) {'
helper='''    function engineeringMediaHTML(slide, first = false) {
      const img = `<img data-asset src="${escapeHTML(slide.image)}" width="1672" height="941" ${first ? 'loading="eager" fetchpriority="high"' : 'loading="lazy"'} decoding="async" alt="${escapeHTML(slide.alt)}">`;
      if (!slide.mobileImage) return img;
      return `<picture class="engineering-media"><source media="(max-width: 760px)" srcset="${escapeHTML(slide.mobileImage)}" width="${slide.mobileWidth}" height="${slide.mobileHeight}">${img}</picture>`;
    }
'''
assert anchor in s
if 'function engineeringMediaHTML' not in s:s=s.replace(anchor,helper+anchor)
old='<img data-asset src="${escapeHTML(slide.image)}" width="1672" height="941" ${first ? \'loading="eager" fetchpriority="high"\' : \'loading="lazy"\'} decoding="async" alt="${escapeHTML(slide.alt)}">'
# Replace the figure instance, not the helper's img string.
start=s.index(anchor);head=s[:start];tail=s[start:];assert old in tail
tail=tail.replace(old,'${engineeringMediaHTML(slide, first)}',1)
oldzoom='<div class="lightbox-image-wrap"><img src="${escapeHTML(slide.image)}" width="1672" height="941" alt="${escapeHTML(slide.alt)}"></div>'
newzoom='<div class="lightbox-image-wrap${slide.mobileImage ? \' engineering-zoom\' : \'\'}">${engineeringMediaHTML(slide, true)}</div>'
assert oldzoom in tail;tail=tail.replace(oldzoom,newzoom,1)
s=head+tail
css='''
    .engineering-media { display: block; width: 100%; }
    .image-button .engineering-media img { aspect-ratio: auto; height: auto; }
    .lightbox-image-wrap.engineering-zoom { display: block; touch-action: pan-x pan-y pinch-zoom; }
    .engineering-zoom .engineering-media { width: 1672px; max-width: none; }
    .engineering-zoom .engineering-media img { display: block; width: 100%; height: auto; max-width: none; max-height: none; }
    @media (max-width: 760px) { .engineering-zoom .engineering-media { width: 768px; } }
'''
if '.image-button .engineering-media img' not in s:s=s.replace('    .teaching-figure {',css+'    .teaching-figure {',1)
p.write_text(s,encoding='utf-8');print('Optional engineering mobile renderer updated; legacy paths retained')
