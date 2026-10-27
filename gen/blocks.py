# -*- coding: utf-8 -*-
"""Pomoćni blokovi za sastavljanje sadržaja stranica."""

from render import SITE, SVG_PHONE, SVG_TICK, depth_prefix, quote_form


def hero(page, pill, h1, lead, ticks, pre_note=None, with_form=True):
    pre = depth_prefix(page["slug"])
    t = "\n      ".join(f"<li>{SVG_TICK}{x}</li>" for x in ticks)
    note = f'<p class="lead" style="font-size:16px">{pre_note}</p>' if pre_note else ""
    form = quote_form(page) if with_form else ""
    return f"""<section class="hero">
  <div class="hero-in">
    <div class="hero-main">
      <p class="pill"><i></i>{pill}</p>
      <h1>{h1}</h1>
      <p class="lead">{lead}</p>
      {note}
      <div class="cta-row">
        <a class="btn btn-primary" href="tel:{SITE['phone_href']}">{SVG_PHONE}Pozovite {SITE['phone_display']}</a>
        <a class="btn btn-ghost" href="{pre}kontakt/#upit">Pitajte za cenu</a>
      </div>
      <ul class="ticks">
      {t}
      </ul>
    </div>
    {form}
  </div>
</section>
"""


def sec(inner, cls="sec", sid=None):
    i = f' id="{sid}"' if sid else ""
    return f'<section class="{cls}"{i}>\n  <div class="wrap">\n{inner}\n  </div>\n</section>\n'


def prose(h2, paragraphs, h2_id=None):
    hid = f' id="{h2_id}"' if h2_id else ""
    body = "\n".join(f"    <p>{p}</p>" for p in paragraphs)
    return f'    <h2{hid}>{h2}</h2>\n    <div class="prose">\n{body}\n    </div>'


def cards(h2, items, intro=None, cls="g3", page=None):
    pre = depth_prefix(page["slug"]) if page else ""
    out = [f"    <h2>{h2}</h2>"]
    if intro:
        out.append(f'    <p class="intro">{intro}</p>')
    cs = []
    for it in items:
        price = f'<div class="price">{it[3]}</div>' if len(it) > 3 and it[3] else ""
        if it[0]:
            cs.append(
                f'      <a class="card" href="{pre}{it[0]}/"><h3>{it[1]}</h3>'
                f"<p>{it[2]}</p>{price}</a>"
            )
        else:
            cs.append(f'      <div class="card"><h3>{it[1]}</h3><p>{it[2]}</p>{price}</div>')
    out.append(f'    <div class="grid {cls}">\n' + "\n".join(cs) + "\n    </div>")
    return "\n".join(out)


def steps(h2, items, intro=None):
    out = [f"    <h2>{h2}</h2>"]
    if intro:
        out.append(f'    <p class="intro">{intro}</p>')
    ss = "\n".join(
        f'      <div class="step"><div class="n">{i:02d}</div><h3>{t}</h3><p>{d}</p></div>'
        for i, (t, d) in enumerate(items, start=1)
    )
    out.append(f'    <div class="steps">\n{ss}\n    </div>')
    return "\n".join(out)


def price_table(h2, rows, intro=None, note_up=None, note_in=None, caption="Okvirne cene"):
    out = [f"    <h2>{h2}</h2>"]
    if intro:
        out.append(f'    <p class="intro">{intro}</p>')
    body = "\n".join(
        f'          <tr><td>{a}</td><td class="num">{b}</td></tr>' for a, b in rows
    )
    out.append(f"""    <div class="table-wrap">
      <table>
        <caption class="sr-only">{caption}</caption>
        <thead><tr><th scope="col">Intervencija</th><th scope="col" class="num">Cena, RSD</th></tr></thead>
        <tbody>
{body}
        </tbody>
      </table>
    </div>""")
    if note_up or note_in:
        n = []
        if note_up:
            n.append(f'      <div class="note note-warn"><h3>Šta može da podigne cenu</h3><p>{note_up}</p></div>')
        if note_in:
            n.append(f'      <div class="note note-calm"><h3>Šta je uključeno u cenu</h3><p>{note_in}</p></div>')
        out.append('    <div class="note-row">\n' + "\n".join(n) + "\n    </div>")
    return "\n".join(out)


def faq_block(items, h2="Česta pitanja"):
    qs = "\n".join(
        f"      <div><h3>{q}</h3><p>{a}</p></div>" for q, a in items
    )
    return f'    <h2>{h2}</h2>\n    <div class="faq">\n{qs}\n    </div>'


def works(h2, items, intro=None):
    out = [f"    <h2>{h2}</h2>"]
    if intro:
        out.append(f'    <p class="intro">{intro}</p>')
    ws = "\n".join(
        f"""      <article class="work">
        <div class="ph">[FOTO: {alt}]</div>
        <div class="work-body">
          <div class="meta">{meta}</div>
          <h3>{t}</h3>
          <p>{d}</p>
        </div>
      </article>"""
        for alt, meta, t, d in items
    )
    out.append(f'    <div class="grid g3">\n{ws}\n    </div>')
    return "\n".join(out)


def chips(h2, items, page, intro=None, last=None):
    pre = depth_prefix(page["slug"])
    out = [f"    <h2>{h2}</h2>"]
    if intro:
        out.append(f'    <p class="intro">{intro}</p>')
    cs = [f'      <a class="chip" href="{pre}{s}/">{l}</a>' for s, l in items]
    if last:
        cs.append(f'      <a class="chip" href="{pre}{last[0]}/" style="font-weight:700">{last[1]}</a>')
    out.append('    <div class="chips">\n' + "\n".join(cs) + "\n    </div>")
    return "\n".join(out)


def related(page, items, h2="Povezane usluge"):
    pre = depth_prefix(page["slug"])
    cs = "\n".join(
        f'      <a class="card" href="{pre}{s}/"><h3 style="margin:0;font-size:16px">{l}</h3></a>'
        for s, l in items
    )
    return f'    <h2 style="font-size:24px">{h2}</h2>\n    <div class="grid g4">\n{cs}\n    </div>'


def brief(items, h2="Ukratko"):
    """Сжатый фактический ответ под заголовком: то, что читает и человек, и машина."""
    rows = "\n".join(
        f'      <div class="b-row"><dt>{k}</dt><dd>{v}</dd></div>' for k, v in items
    )
    return (f'    <h2 class="sr-only">{h2}</h2>\n'
            f'    <dl class="brief">\n{rows}\n    </dl>')
