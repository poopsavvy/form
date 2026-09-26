#!/usr/bin/env python3
"""Build the city pages and the clean-yard guide from shared pieces.

Run from the repo root:  python3 scripts/build_pages.py
Edit the text here, then re-run; it rewrites dog-poop-removal-*/index.html
and did-you-know/index.html. Styles live in assets/brand.css, behavior in
assets/brand.js, so these pages match the homepage.
"""
from html import escape
from pathlib import Path
import json

ROOT = Path(__file__).resolve().parent.parent
SITE = "https://dogpoopremovalnearyou.com"
PHONE, TEL = "214.702.6169", "tel:+12147026169"
EMAIL = "contact@dogpoopremovalnearyou.com"
UPDATED = "2026-09-26"

# slug, name, zips, opening line, map position (x, y) and label offset (dx, anchor)
CITIES = [
    ("desoto", "DeSoto", ["75115", "75123"],
     "Our service began in DeSoto. Weekly pickup keeps the backyard ready without putting another dirty chore on your calendar.",
     (220, 135)),
    ("lancaster", "Lancaster", ["75134", "75146"],
     "Lancaster dog owners can keep the yard cleaner without giving up an evening or weekend to hunt for every pile.",
     (310, 110)),
    ("duncanville", "Duncanville", ["75116", "75137", "75138"],
     "Duncanville yards are for playtime, cookouts and relaxing, not watching every step.",
     (175, 70)),
    ("cedar-hill", "Cedar Hill", ["75104", "75106"],
     "Cedar Hill dog owners have better things to do than spend their free time scooping the backyard.",
     (105, 125)),
    ("glenn-heights", "Glenn Heights", ["75154"],
     "Glenn Heights families can keep the backyard ready for dogs, kids and company while we handle the dirty work.",
     (230, 200)),
    ("red-oak", "Red Oak", ["75154"],
     "A cleaner Red Oak backyard is easier to enjoy, and weekly service keeps the mess from piling up.",
     (275, 250)),
    ("ovilla", "Ovilla", ["75154"],
     "Ovilla dog owners can hand off one repetitive outdoor chore and spend more time enjoying the yard.",
     (160, 235)),
    ("midlothian", "Midlothian", ["76065"],
     "Midlothian yards are made for family time, dogs and fresh air, not piles underfoot.",
     (95, 295)),
]

PAW = ('<svg width="24" height="24" viewBox="0 0 24 24" fill="#fff"><ellipse cx="6" cy="9" rx="2.2" ry="2.8"/>'
       '<ellipse cx="10.5" cy="5.5" rx="2.2" ry="2.8"/><ellipse cx="15.5" cy="5.5" rx="2.2" ry="2.8"/>'
       '<ellipse cx="19.5" cy="9.5" rx="2" ry="2.6"/><path d="M12.8 11c-3 0-6.3 4.4-6.3 7 0 1.8 1.4 2.6 3 2.6 '
       '1.3 0 2.2-.6 3.3-.6s2 .6 3.3.6c1.6 0 3-.8 3-2.6 0-2.6-3.3-7-6.3-7z"/></svg>')

FAVICON = ("data:image/svg+xml,%3Csvg xmlns='http://www.w3.org/2000/svg' viewBox='0 0 24 24'%3E%3Crect width='24' "
           "height='24' rx='6' fill='%232f9e44'/%3E%3Cpath d='M12.8 11c-3 0-6.3 4.4-6.3 7 0 1.8 1.4 2.6 3 2.6 1.3 0 "
           "2.2-.6 3.3-.6s2 .6 3.3.6c1.6 0 3-.8 3-2.6 0-2.6-3.3-7-6.3-7z' fill='%23fff'/%3E%3C/svg%3E")


def city_url(slug):
    return f"dog-poop-removal-{slug}-tx/"


def head(title, description, path, ld):
    ld_tags = "\n".join(f'  <script type="application/ld+json">{json.dumps(x, ensure_ascii=False)}</script>' for x in ld)
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{escape(title)}</title>
  <meta name="description" content="{escape(description)}">
  <link rel="canonical" href="{SITE}/{path}">
  <meta property="og:title" content="{escape(title)}">
  <meta property="og:description" content="{escape(description)}">
  <meta property="og:url" content="{SITE}/{path}">
  <meta name="theme-color" content="#2f9e44">
  <link rel="icon" type="image/svg+xml" href="{FAVICON}">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Fredoka:wght@500;600;700&family=Inter:wght@400;500;600;700&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="../assets/brand.css">
{ld_tags}
</head>
<body>
  <div class="progress" id="progress"></div>
"""


def nav(current=None):
    guide = ' aria-current="page"' if current == "guide" else ""
    return f"""  <header class="nav" id="nav">
    <div class="wrap">
      <a href="../" class="logo" aria-label="Dog Poop Removal Near You home">
        <span class="logo-mark" aria-hidden="true">{PAW}</span>
        <span class="logo-text">Dog Poop Removal<small>Near You</small></span>
      </a>
      <button class="menu-btn" id="menuBtn" aria-label="Open menu" aria-expanded="false"><span></span><span></span><span></span></button>
      <ul class="nav-links" id="navLinks">
        <li><a href="../#how">How it works</a></li>
        <li><a href="../#plans">Plans</a></li>
        <li><a href="../#areas">Service area</a></li>
        <li><a href="../did-you-know/"{guide}>Did you know?</a></li>
        <li><a href="{TEL}" class="nav-phone">📞 {PHONE}</a></li>
        <li><a href="../#estimate" class="btn btn-primary">Free quote</a></li>
      </ul>
    </div>
  </header>
"""


def footer():
    cities = " ".join(f'<a href="../{city_url(s)}">{n}</a>' for s, n, *_ in CITIES)
    return f"""  <footer>
    <div class="wrap">
      <a href="../" class="logo"><span class="logo-text">Dog Poop Removal<small>Near You</small></span></a>
      <p>Family-owned in DeSoto · Serving Southern DFW<br>Call or text <a href="{TEL}">{PHONE}</a> · <a href="mailto:{EMAIL}">{EMAIL}</a></p>
      <p>© <span id="year">2026</span> Dog Poop Removal Near You.<br>Operated by Reed &amp; Reed Ventures LLC.</p>
      <p class="footer-links"><b>Service areas:</b> {cities} <a href="../did-you-know/">Clean-yard guide</a></p>
      <p class="family">Dog Poop Removal Near You is part of the <a href="https://poop-savvy.com" rel="noopener">Poop Savvy</a> family, run by the same local owners.</p>
    </div>
  </footer>

  <div class="sticky-cta" id="stickyCta">
    <a href="../#estimate" class="btn btn-primary">Free quote</a>
    <a href="{TEL}" class="btn btn-ghost">📞 Call / text</a>
  </div>

  <script src="../assets/brand.js"></script>
</body>
</html>
"""


def city_map(active):
    pins = []
    for i, (slug, name, _, _, (x, y)) in enumerate(CITIES):
        here = slug == active
        col = "#6b4423" if here else "#2f9e44"
        ring = f'<circle class="ring" cx="{x}" cy="{y}" r="12" fill="{col}"/>' if here else ""
        r = 10 if here else 6
        left = x > 250
        tx, anchor = (x - 16, "end") if left else (x + 16, "start")
        weight = "800" if here else "600"
        size = "15" if here else "11"
        fill = "#1d2a21" if here else "#5b6b60"
        pins.append(
            f'<g class="pin{" here" if here else ""}" style="--d:{(i + 1) / 10:.1f}s">{ring}'
            f'<circle cx="{x}" cy="{y}" r="{r}" fill="{col}"/>'
            f'<text x="{tx}" y="{y + 4}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}">{name}</text></g>')
    return f"""<svg viewBox="0 0 400 360" role="img" aria-label="Map of the Southern DFW cities we serve">
            <defs><pattern id="grid" width="24" height="24" patternUnits="userSpaceOnUse"><path d="M24 0H0V24" fill="none" stroke="#dcebdf" stroke-width="1"/></pattern></defs>
            <rect x="10" y="10" width="380" height="340" rx="32" fill="#fff"/>
            <rect x="10" y="10" width="380" height="340" rx="32" fill="url(#grid)"/>
            <path d="M30 200 C 110 170, 160 230, 250 190 S 360 150, 380 170" stroke="#bfe3c7" stroke-width="10" fill="none" stroke-linecap="round"/>
            <path d="M200 20 C 190 120, 230 200, 200 340" stroke="#f1e2cf" stroke-width="8" fill="none" stroke-linecap="round"/>
            <g font-family="Inter, sans-serif">
              {"".join(pins)}
            </g>
          </svg>"""


def faq(items):
    out = []
    for i, (q, a) in enumerate(items):
        d = f' style="--d:{i * .05:.2f}s"' if i else ""
        out.append(f'<details class="reveal"{d}><summary>{q}<i></i></summary><div class="faq-body"><p>{a}</p></div></details>')
    return "\n          ".join(out)


def build_city(slug, name, zips, lead, pos):
    path = city_url(slug)
    zip_text = " and ".join(zips) if len(zips) < 3 else ", ".join(zips[:-1]) + " and " + zips[-1]
    faqs = [
        ("How much does weekly service cost?",
         "It depends on how often we come and how many dogs you have. Get a free quote online and you'll see your price in about a minute."),
        ("Do I have to sign a contract?",
         "No. Service is prepaid monthly, and you can cancel before your next renewal."),
        (f"Is every {name} address covered?",
         f"We serve {name}, but route boundaries can vary. We check your full address before confirming service."),
        ("When does service begin?",
         "After your free quote, tap Start service and fill out a short form. We check your address and email your payment link with your service day and start date."),
        ("What do you do with the waste?",
         "We double-bag everything and place it in your outdoor trash bin, so it goes out with your regular pickup."),
    ]
    ld = [
        {"@context": "https://schema.org", "@type": "Service", "name": f"Dog poop removal in {name}, Texas",
         "serviceType": "Dog waste removal",
         "description": f"Weekly and every-other-week dog poop removal in {name}, TX. Free quote online, prepaid monthly, no contract.",
         "provider": {"@type": "LocalBusiness", "name": "Dog Poop Removal Near You", "url": SITE + "/", "telephone": "+1-214-702-6169",
                      "address": {"@type": "PostalAddress", "addressLocality": "DeSoto", "addressRegion": "TX", "addressCountry": "US"}},
         "areaServed": {"@type": "City", "name": f"{name}, Texas"}, "url": f"{SITE}/{path}"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in faqs]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": f"Dog poop removal in {name}", "item": f"{SITE}/{path}"}]},
    ]
    current = ' aria-current="page"'
    others = " ".join(
        f'<a href="../{city_url(s)}"{current if s == slug else ""}>{n}</a>' for s, n, *_ in CITIES)
    zips_html = "".join(f"<span>{z}</span>" for z in zips)
    html = head(f"Dog Poop Removal in {name}, TX | Free Quote",
                f"Dog poop removal in {name}, TX from a local, family-owned team. Weekly or every-other-week yard cleanup, prepaid monthly, no contract. Get a free quote in about a minute.",
                path, ld)
    html += nav()
    html += f"""
  <main id="top">
    <section class="page-hero">
      <div class="wrap">
        <div>
          <nav class="crumbs reveal" aria-label="Breadcrumb"><a href="../">Home</a><span aria-hidden="true">›</span><a href="../#areas">Service area</a><span aria-hidden="true">›</span><span>{name}</span></nav>
          <h1 class="reveal" style="--d:.1s">Dog poop removal in <mark>{name}.</mark></h1>
          <p class="lead reveal" style="--d:.2s">{lead}</p>
          <div class="hero-cta reveal" style="--d:.3s">
            <a href="../#estimate" class="btn btn-primary">Get my free quote <span class="arrow">→</span></a>
            <a href="{TEL}" class="btn btn-ghost">📞 Call or text {PHONE}</a>
          </div>
          <p class="fine reveal" style="--d:.4s">Free quote in about a minute · prepaid monthly · no contract</p>
        </div>
        <div class="mini-map reveal zoom" style="--d:.2s">
          {city_map(slug)}
          <span class="map-tag">📍 Now scooping {name}</span>
        </div>
      </div>
    </section>

    <section class="block" style="padding-bottom:60px">
      <div class="wrap">
        <div class="head reveal">
          <span class="eyebrow">The chore you can cross off</span>
          <h2>We scoop. You enjoy the yard.</h2>
          <p>Weekly pickup keeps the job manageable and gives your household a routine you don't have to remember.</p>
        </div>
        <div class="cards">
          <article class="info-card reveal"><h3>Free quote</h3><span class="big"><span class="count" data-to="60">60</span>s</span><p>See your price online before you decide anything.</p></article>
          <article class="info-card reveal" style="--d:.1s"><h3>No long-term contract</h3><span class="big"><span class="count" data-to="0">0</span></span><p>Prepaid monthly. Cancel before your next renewal.</p></article>
          <article class="info-card reveal" style="--d:.2s"><h3>Every visit</h3><span class="big">📸</span><p>An on-the-way text, a done text and a photo of your closed gate.</p></article>
        </div>
      </div>
    </section>

    <section class="block plans-bg" id="how">
      <div class="wrap">
        <div class="head reveal">
          <span class="eyebrow">How to get started</span>
          <h2>A cleaner {name} yard in 3 easy steps</h2>
        </div>
        <div class="steps" id="steps">
          <div class="steps-line"><i id="stepsLine"></i></div>
          <div class="step reveal"><div class="step-num">📋<b>1</b></div><h3>Get your free quote</h3><p>Tell us your zip, schedule and number of dogs. Your price shows up right away.</p></div>
          <div class="step reveal" style="--d:.15s"><div class="step-num">📝<b>2</b></div><h3>Start service</h3><p>Like it? A short form grabs your address, gate access and yard details.</p></div>
          <div class="step reveal" style="--d:.3s"><div class="step-num">🐶<b>3</b></div><h3>We handle the rest</h3><p>We email your payment link with your service day and start date. Then we scoop.</p></div>
        </div>
      </div>
    </section>

    <section class="block">
      <div class="wrap split">
        <div class="reveal from-left">
          <span class="eyebrow">One important detail</span>
          <h2>We check every full address.</h2>
          <p>{name} is one of the eight Southern DFW cities we serve, but route boundaries can vary. We review your complete address before confirming service, so the route stays tight and dependable.</p>
        </div>
        <div class="check-card reveal from-right">
          <h3>{name} zip codes we serve</h3>
          <p>Serving {name} in {zip_text}.</p>
          <div class="zips">{zips_html}</div>
          <a href="../#estimate" class="btn btn-primary">Check my address <span class="arrow">→</span></a>
        </div>
      </div>
    </section>

    <section class="block faq-bg" id="faq">
      <div class="wrap">
        <div class="head reveal">
          <span class="eyebrow">Questions from {name} dog owners</span>
          <h2>Before we scoop…</h2>
        </div>
        <div class="faqs">
          {faq(faqs)}
        </div>
      </div>
    </section>

    <section class="block" style="padding-bottom:40px">
      <div class="wrap">
        <div class="cta reveal zoom" id="cta">
          <h2>Let's get your {name} yard on the route.</h2>
          <p>Get your free quote in under a minute.</p>
          <a href="../#estimate" class="btn btn-primary">Get my free quote <span class="arrow">→</span></a>
        </div>
      </div>
    </section>

    <section class="block" style="padding-top:40px">
      <div class="wrap reveal">
        <span class="eyebrow">Southern DFW service areas</span>
        <h2 style="font-size:clamp(1.6rem,3.4vw,2.2rem);margin:8px 0 4px">Dog poop removal near {name}</h2>
        <div class="area-tags">{others}</div>
      </div>
    </section>
  </main>

"""
    html += footer()
    out = ROOT / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


REASONS = [
    ("Parasites", "The invisible problem", "Parasites can turn soil into a waiting room.", [
        "Some infected dogs pass parasite eggs or larvae in their feces. Roundworms and hookworms are two well-known examples. Once waste is left on the ground, the concern is no longer limited to the pile itself: the surrounding soil can become contaminated, and some parasite stages can remain in the environment after the visible waste is gone.",
        "That's why the practical advice is so unglamorous and so effective: remove feces promptly. It reduces the time waste spends in the yard and the chance for contamination to spread. Routine pickup matters most in yards shared by several dogs or visited by neighborhood pets.",
    ], 'Health guidance: <a href="https://www.avma.org/resources-tools/pet-owners/petcare/intestinal-parasites-cats-and-dogs" rel="noopener" target="_blank">American Veterinary Medical Association</a>.'),
    ("Dog exposure", "Dogs will be dogs", "Your dog investigates the yard with its nose, and sometimes its mouth.", [
        "A pile that seems easy for a person to avoid may be fascinating to a dog. Dogs sniff, lick, paw at and sometimes eat feces. That creates another chance for contact with parasites or infectious organisms, especially when several dogs use the same space.",
        "Removing waste quickly doesn't replace veterinary care, parasite prevention or vaccines. It does remove an obvious source of exposure from the place your dog visits every day. Think of scooping as basic backyard hygiene: one simple layer in a bigger plan to keep pets healthy.",
    ], 'The <a href="https://www.avma.org/resources-tools/pet-owners/petcare/disease-risks-dogs-social-settings" rel="noopener" target="_blank">AVMA advises keeping dogs from sniffing, licking or swallowing other animals’ feces</a>.'),
    ("Water pollution", "Rain doesn't clean it up", "Stormwater can carry the problem beyond your fence.", [
        "Rain may make a pile less visible, but that doesn't make it harmless. Runoff can move bacteria and nutrients from pet waste across driveways, into storm drains and toward creeks and lakes. In many neighborhoods, storm drains lead to local water without the treatment household sewage gets.",
        "Picking up before the next North Texas downpour is a small household habit with a community benefit. Bag the waste, dispose of it according to local rules and keep it out of the next wave of runoff.",
    ], 'The <a href="https://www.epa.gov/nps/basic-information-about-nonpoint-source-nps-pollution" rel="noopener" target="_blank">U.S. Environmental Protection Agency</a> lists pet waste as a source of bacteria and nutrients in runoff.'),
    ("Lawn stress", "Not free fertilizer", "Dog poop isn't the lawn food people hope it is.", [
        "It's tempting to compare dog waste with manure used on farms, but raw dog feces sitting in a residential yard isn't finished compost or a balanced lawn treatment. Piles can smother grass, leave residue and make routine mowing and watering less sanitary.",
        "If you want to feed the turf, use a lawn product or properly finished compost made for that purpose. Let the dog poop leave in a bag.",
    ], None),
    ("Odor", "Your nose already knows", "Odor makes the whole yard feel dirty.", [
        "Heat and moisture make an old pile everybody's business. In a Southern DFW summer, odors build quickly, especially in shaded corners, dog runs and smaller yards where waste is concentrated. The smell drifts toward the patio, the fence line, open windows and outdoor furniture.",
        "A weekly removal rhythm keeps a scattered mess from becoming the yard's defining feature. You should smell cut grass or dinner on the grill, not spend a cookout wondering where that smell is coming from.",
    ], None),
    ("Pests", "Unwanted guests", "Waste and odor can attract nuisance pests.", [
        "Flies are drawn to decaying organic material, and a yard with piles gives them more places to feed and breed. No single cleanup makes every outdoor bug disappear, but removing what attracts them is a sensible place to start.",
        "This is another reason frequency beats a heroic once-a-season cleanup. The less time waste sits, the less time it's part of the backyard pest cycle.",
    ], None),
    ("People", "Small hands. Bare feet.", "Children and guests don't know where every pile is hiding.", [
        "You may know the dog's favorite corner. A child chasing a ball, a neighbor crossing the grass or a guest walking to the patio doesn't. Kids also play close to the ground and are more likely to touch soil and then their faces.",
        "Prompt pickup isn't about panic. It's about controlling the obvious thing you can control. A clean play area lets everyone use the space without inspecting every step.",
    ], None),
    ("Tracking & mowing", "The mower isn't a magic wand", "Shoes, paws and mower wheels spread the mess.", [
        "Stepping in dog poop is the classic backyard disaster because the problem immediately travels: across the patio, into the car, onto rugs and through the house. Dogs track residue on their paws too. And mowing over a pile doesn't get rid of it. It breaks it apart and spreads it over the mower and nearby grass.",
        "The best order is simple: scoop first, then enjoy or mow. When the yard is consistently clean, you stop scanning the ground every time you walk outside.",
    ], None),
    ("Bigger cleanup", "The chore compounds", "Waiting turns five minutes into a weekend project.", [
        "Dog waste is a recurring task. Skipping one round doesn't cancel the next; it stacks them together. Old piles get harder to spot, wet weather softens them, tall grass hides them and each new one adds another reason to put the job off.",
        "A weekly schedule keeps the workload predictable. That's the real value of routine service: never letting the yard reach dramatic-cleanup status in the first place.",
    ], None),
    ("Lost yard time", "The biggest cost", "A dirty yard steals the reason you have a yard.", [
        "The backyard is supposed to be usable space: morning coffee, fetch, grilling, gardening, birthday parties and a place for the kids to run. When the ground is dotted with dog waste, people avoid it, and the yard becomes a view through the window instead of part of the home.",
        "This is the reason that matters most day to day. Removing the poop gives the space back. You don't have to love scooping, or even remember it, to have a yard that's ready when you are.",
    ], None),
]


def build_guide():
    path = "did-you-know/"
    toc = "\n            ".join(
        f'<li><a href="#reason-{i}"><span>{i:02d}</span>{short}</a></li>' for i, (short, *_) in enumerate(REASONS, 1))

    def reason(i):
        short, eyebrow, title, paras, note = REASONS[i - 1]
        body = "".join(f"<p>{p}</p>" for p in paras)
        if note:
            body += f'<p class="source-note">{note}</p>'
        return (f'<section class="reason reveal" id="reason-{i}"><div class="reason-num">{i:02d}</div>'
                f'<div><span class="eyebrow">{eyebrow}</span><h2>{title}</h2>{body}</div></section>')

    city_grid = "".join(
        f'<a href="../{city_url(s)}"><b>{n}</b><span>{" · ".join(z)}</span></a>' for s, n, z, *_ in CITIES)
    guide_faq = [
        ("Is the service prepaid?", "Yes. Service is prepaid monthly with no contract. Your exact price comes with your free quote."),
        ("Is there an initial cleanup charge?", "Regular pricing assumes the yard has been cleaned in the last 30 days. If there's heavy buildup, we quote any one-time cleanup before doing extra work."),
        ("Do I need to be home?", "No. We just need safe access to the yard and all dogs kept away from it during the visit."),
        ("What happens if it rains?", "Light rain doesn't stop us. If conditions make cleanup unsafe or ineffective, we'll let you know and move the visit to the next workable time."),
        ("Where does the waste go?", "We double-bag it and place it in your outdoor trash bin."),
        ("Can I cancel?", "Yes. There's no long-term contract. Cancel before your next monthly renewal to stop future charges."),
    ]
    ld = [
        {"@context": "https://schema.org", "@type": "BlogPosting", "headline": "10 reasons you shouldn't let dog poop sit in your yard",
         "description": "Ten practical reasons to remove dog waste promptly, from parasites and water pollution to lawn hygiene and lost backyard time.",
         "datePublished": "2026-09-13", "dateModified": UPDATED, "author": {"@type": "Person", "name": "Josh Reed"},
         "publisher": {"@type": "Organization", "name": "Dog Poop Removal Near You"}, "mainEntityOfPage": f"{SITE}/{path}"},
        {"@context": "https://schema.org", "@type": "FAQPage", "mainEntity": [
            {"@type": "Question", "name": q, "acceptedAnswer": {"@type": "Answer", "text": a}} for q, a in guide_faq]},
        {"@context": "https://schema.org", "@type": "BreadcrumbList", "itemListElement": [
            {"@type": "ListItem", "position": 1, "name": "Home", "item": SITE + "/"},
            {"@type": "ListItem", "position": 2, "name": "Did you know?", "item": f"{SITE}/{path}"}]},
    ]
    ticker = "".join(f"<span>{t}</span>" for t in ["Don't step in it", "Don't mow over it", "Don't wait for the rain", "Scoop the yard"] * 4)
    faq_html = faq(guide_faq)
    html = head("10 Reasons Not to Leave Dog Poop in Your Yard | Southern DFW",
                "Why is leaving dog poop in the yard a bad idea? 10 health, lawn, water, pest and quality-of-life reasons, plus an easy weekly cleanup option in Southern DFW.",
                path, ld)
    html += nav("guide")
    html += f"""
  <main id="top">
    <section class="page-hero">
      <div class="wrap">
        <div>
          <nav class="crumbs reveal" aria-label="Breadcrumb"><a href="../">Home</a><span aria-hidden="true">›</span><span>Did you know?</span></nav>
          <span class="pill reveal" style="margin-top:14px"><span class="pulse"></span> The clean-yard files · Issue #01</span>
          <h1 class="reveal" style="--d:.1s">10 reasons you shouldn't let dog poop sit in your yard.</h1>
          <p class="lead reveal" style="--d:.2s">It doesn't disappear. It gets rained on, stepped in, mowed over, sniffed by the dog and promoted from quick chore to whole situation. Here's what's really happening while those piles wait.</p>
          <div class="hero-cta reveal" style="--d:.3s">
            <a href="#reason-1" class="btn btn-primary">Get the dirty details <span class="arrow">↓</span></a>
            <span class="fine">About 8 minutes · worth every scoop</span>
          </div>
        </div>
        <div class="ten-badge reveal zoom" style="--d:.2s" aria-hidden="true"><div><b>10</b><span>good reasons</span></div></div>
      </div>
    </section>

    <div class="marquee ticker" aria-hidden="true"><div class="marquee-track">{ticker}</div></div>

    <section class="block">
      <div class="wrap guide">
        <aside class="toc reveal from-left" aria-label="Article contents">
          <span class="eyebrow">The short version</span>
          <h2>Why scoop now?</h2>
          <ol>
            {toc}
          </ol>
          <a href="../#estimate" class="btn btn-primary">Skip the chore <span class="arrow">→</span></a>
        </aside>

        <article class="article" id="article">
          <div class="intro-card reveal"><b>First, the honest version</b>One forgotten pile isn't a backyard emergency. The problem is repetition. Dogs keep going, piles accumulate, weather spreads what was concentrated and the task gets easier to avoid. Prompt, routine removal breaks that cycle before it becomes gross, inconvenient or risky.</div>
          {reason(1)}
          {reason(2)}
          <p class="pull-quote reveal"><span>"Later"</span> is how four piles become forty.</p>
          {reason(3)}
          {reason(4)}
          {reason(5)}
          {reason(6)}
          {reason(7)}
          <section class="calc reveal">
            <span class="eyebrow">Southern DFW, this one's for you</span>
            <h2>Local routes. Familiar neighborhoods. Cleaner Saturdays.</h2>
            <p>We grow neighborhood by neighborhood so routes stay dependable and communication stays personal.</p>
            <div class="city-grid">{city_grid}</div>
          </section>
          <aside class="mid-cta reveal"><div><p>Your yard has better things to do</p><h2>See your price in about a minute.</h2></div><a class="btn btn-primary" href="../#estimate">Get my free quote <span class="arrow">→</span></a></aside>
          {reason(8)}
          {reason(9)}
          {reason(10)}

          <section class="calc reveal" aria-labelledby="calc-title">
            <span class="eyebrow">The dirty-math calculator</span>
            <h2 id="calc-title">What is the chore costing you?</h2>
            <p>Use your real routine. We'll turn the piles and cleanup time into a monthly picture.</p>
            <form class="calc-grid" id="calc" onsubmit="return false">
              <div class="field"><label for="calcDogs">Dogs</label><select id="calcDogs"><option value="1">1 dog</option><option value="2" selected>2 dogs</option><option value="3">3 dogs</option><option value="4">4 dogs</option></select></div>
              <div class="field"><label for="calcPiles">Piles per dog, per day</label><select id="calcPiles"><option value="1">1 pile</option><option value="2" selected>2 piles</option><option value="3">3 piles</option></select></div>
              <div class="field"><label for="calcFreq">How often do you clean?</label><select id="calcFreq"><option value="28">Daily</option><option value="12">3 times a week</option><option value="8">Twice a week</option><option value="4" selected>Weekly</option></select></div>
              <div class="field"><label for="calcMin">Minutes each time: <output id="calcMinOut">20</output></label><input id="calcMin" type="range" min="5" max="60" step="5" value="20"></div>
              <div class="calc-out" id="calcOut" aria-live="polite">
                <span>Your yard produces about</span><strong id="calcPilesOut">112 piles</strong>
                <span>a month. Weekly service gives you back roughly</span><strong id="calcTimeOut">1 hour 20 minutes</strong>
                <span>of dirty-yard duty every month.</span>
              </div>
            </form>
          </section>

          <section class="calc reveal">
            <span class="eyebrow">No fine-print surprises</span>
            <h2>Questions people ask before starting.</h2>
            <div class="faqs" style="margin-top:14px">
              {faq_html}
            </div>
          </section>

          <div class="cta reveal zoom" id="cta">
            <h2>Enough reading about poop. Let's get it out of your yard.</h2>
            <p>We pick up dog waste across Southern DFW, sanitize our equipment, close the gate and text you a photo when the job is done.</p>
            <a href="../#estimate" class="btn btn-primary">Get my free quote <span class="arrow">→</span></a>
          </div>

          <section class="sources reveal">
            <h2>Sources &amp; a sensible note</h2>
            <p>This article is general educational information, not veterinary or medical advice. If a person or pet may have been exposed or is ill, contact an appropriate health professional.</p>
            <ul>
              <li><a href="https://www.avma.org/resources-tools/pet-owners/petcare/intestinal-parasites-cats-and-dogs" target="_blank" rel="noopener">AVMA: Intestinal parasites in cats and dogs</a></li>
              <li><a href="https://www.avma.org/resources-tools/pet-owners/petcare/disease-risks-dogs-social-settings" target="_blank" rel="noopener">AVMA: Disease risks for dogs in social settings</a></li>
              <li><a href="https://www.epa.gov/nps/basic-information-about-nonpoint-source-nps-pollution" target="_blank" rel="noopener">EPA: Basic information about nonpoint source pollution</a></li>
            </ul>
          </section>
        </article>
      </div>
    </section>
  </main>

  <script>
    // Dirty-math calculator: piles per month and time spent scooping, no pricing.
    (function () {{
      const $ = id => document.getElementById(id);
      const out = $('calcOut');
      function update() {{
        const dogs = +$('calcDogs').value, piles = +$('calcPiles').value, freq = +$('calcFreq').value, mins = +$('calcMin').value;
        const total = mins * freq, h = Math.floor(total / 60), m = total % 60;
        $('calcMinOut').textContent = mins;
        $('calcPilesOut').textContent = (dogs * piles * 28) + ' piles';
        $('calcTimeOut').textContent = [h ? h + ' hour' + (h === 1 ? '' : 's') : '', m ? m + ' minutes' : ''].filter(Boolean).join(' ');
        out.classList.remove('bump'); void out.offsetWidth; out.classList.add('bump');
      }}
      $('calc').addEventListener('input', update);
      update();
    }})();
  </script>
"""
    html += footer()
    out = ROOT / path / "index.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(html)


def build_sitemap():
    urls = [("", "1.0"), ("did-you-know/", "0.8")] + [(city_url(s), "0.9") for s, *_ in CITIES]
    rows = "\n".join(f"  <url><loc>{SITE}/{u}</loc><lastmod>{UPDATED}</lastmod><priority>{p}</priority></url>" for u, p in urls)
    (ROOT / "sitemap.xml").write_text(
        f'<?xml version="1.0" encoding="UTF-8"?>\n<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">\n{rows}\n</urlset>\n')
    (ROOT / "robots.txt").write_text(f"User-agent: *\nAllow: /\nDisallow: /intake.html\nSitemap: {SITE}/sitemap.xml\n")


if __name__ == "__main__":
    for c in CITIES:
        build_city(*c)
    build_guide()
    build_sitemap()
    print("Built", len(CITIES), "city pages, the guide, sitemap.xml and robots.txt")
