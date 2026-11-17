"""Genera le pagine HTML del sito con intestazione e piede comuni.

Uso:  python3 strumenti/genera_sito.py .
Modifica i testi in questo file e rilancia il comando: le pagine .html vengono riscritte.

Convenzioni sui testi
- I testi scritti da Rossana sono riportati così come li ha scritti (cerca "TESTO DI ROSSANA").
- Dove il testo manca c'è Lorem ipsum: funzione lorem().
- Dati da completare (telefono, Albo, città...): funzione DC(), evidenziati in giallo nel sito.
"""
import hashlib
import os
import sys

OUT = sys.argv[1]

with open(os.path.join(OUT, "assets", "style.css"), "rb") as _f:
    VERSIONE_CSS = hashlib.sha1(_f.read()).hexdigest()[:8]

# --------------------------------------------------------------------------- dati di base

STUDIO = "Prosopon"  # nome di lavoro, in valutazione
DC = lambda t: f'<span class="da-completare">[{t}]</span>'
EMAIL = '<a href="mailto:info@prosopon.it">info@prosopon.it</a>'
TELEFONO = DC("telefono")
WHATSAPP = "https://wa.me/390000000000?text=" + "Buongiorno%20dottoressa%2C%20vorrei%20qualche%20informazione%20per%20fissare%20un%20primo%20colloquio."
ORARI = f"Su appuntamento, {DC('giorni e orari')}"

LOREM = [
    "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua.",
    "Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo consequat.",
    "Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur.",
    "Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt mollit anim id est laborum.",
    "Curabitur pretium tincidunt lacus, nulla gravida orci a odio, nullam varius turpis et commodo pharetra.",
    "Integer in mauris eu nibh euismod gravida, duis ac tellus et risus vulputate vehicula.",
]


def lorem(frasi=2, inizio=0):
    return " ".join(LOREM[(inizio + i) % len(LOREM)] for i in range(frasi))


def p_lorem(paragrafi=1, frasi=2):
    return "\n".join(f"        <p>{lorem(frasi, i * 2)}</p>" for i in range(paragrafi))


FRECCIA = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 8h12M9.5 3.5 14 8l-4.5 4.5"/></svg>'

ICONE = {
    "persona": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="11" r="5.5"/><path d="M6.5 27c0-5.5 4.3-9 9.5-9s9.5 3.5 9.5 9"/></svg>',
    "persone": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="12" cy="11" r="4.5"/><path d="M4 26c0-4.6 3.6-7.5 8-7.5s8 2.9 8 7.5"/><circle cx="22" cy="12.5" r="3.6"/><path d="M20.5 19.2c4.2-.6 7.5 2 7.5 6.3"/></svg>',
    "giovane": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="10" r="4.8"/><path d="M8 27c0-5 3.6-8.4 8-8.4s8 3.4 8 8.4"/><path d="M11.5 8.5c1.5-3 7.5-3.5 9 0"/></svg>',
    "foglia": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M7 25C7 13 14 6 26 6c0 12-7 19-19 19Z"/><path d="M7 25 19 13"/></svg>',
    "edificio": '<svg viewBox="0 0 32 32" aria-hidden="true"><rect x="7" y="5" width="18" height="22" rx="1.5"/><path d="M12 10h2M18 10h2M12 15h2M18 15h2M12 20h2M18 20h2M14 27v-3h4v3"/></svg>',
    "posta": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/></svg>',
    "telefono": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h3.5l1.5 4-2.2 1.4a11 11 0 0 0 6.8 6.8L16 14l4 1.5V19a2 2 0 0 1-2 2C10.3 21 3 13.7 3 6a2 2 0 0 1 2-2Z"/></svg>',
    "luogo": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "schermo": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4.5" width="18" height="12" rx="1.5"/><path d="M9 20h6M12 16.5V20"/></svg>',
    "chat": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 19.5 5.3 15A8 8 0 1 1 9 18.7Z"/></svg>',
    "orologio": '<svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="8.5"/><path d="M12 7.5V12l3 2"/></svg>',
}

FOGLIA_GRANDE = '<svg class="foglia" viewBox="0 0 120 300" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M60 300V20"/><path d="M60 60c-30-6-44-26-46-44 22 2 40 18 46 44Z" fill="currentColor"/><path d="M60 110c30-6 44-26 46-44-22 2-40 18-46 44Z" fill="currentColor"/><path d="M60 160c-30-6-44-26-46-44 22 2 40 18 46 44Z" fill="currentColor"/><path d="M60 210c30-6 44-26 46-44-22 2-40 18-46 44Z" fill="currentColor"/><path d="M60 260c-30-6-44-26-46-44 22 2 40 18 46 44Z" fill="currentColor"/></svg>'

# --------------------------------------------------------------------------- navigazione

PERCORSI = [
    ("percorsi.html#sostegno", "Sostegno psicologico"),
    ("percorsi.html#crescita", "Crescita e benessere"),
    ("adolescenti.html", "Adolescenti e famiglie"),
    ("aziende.html", "Aziende"),
]
PAGINE_PERCORSI = {"percorsi.html", "adolescenti.html", "aziende.html"}

MENU = [
    ("chi-sono.html", "Chi sono"),
    ("percorsi.html", "Percorsi"),
    ("come-lavoro.html", "Come lavoro"),
    ("studio.html", "Lo studio"),
    ("perche-parlarne.html", "Domande frequenti"),
    ("contatti.html", "Contatti"),
]

ETICHETTE = {
    "chi-sono.html": "Chi sono",
    "percorsi.html": "Percorsi psicologici",
    "adolescenti.html": "Percorsi",
    "aziende.html": "Percorsi",
    "come-lavoro.html": "Come lavoro",
    "studio.html": "Lo studio",
    "perche-parlarne.html": "Domande frequenti",
    "contatti.html": "Contatti",
    "prenota.html": "Prenotazioni",
    "privacy.html": "Privacy",
}


def voce_menu(file, href, nome):
    if href == "percorsi.html":
        attivo = ' aria-current="page"' if file in PAGINE_PERCORSI else ""
        sotto = "\n".join(
            f'            <li><a href="{h}">{n}</a></li>' for h, n in PERCORSI
        )
        return f'''        <li class="con-sottomenu">
          <a href="percorsi.html"{attivo}>Percorsi</a>
          <ul class="sottomenu">
{sotto}
          </ul>
        </li>'''
    attivo = ' aria-current="page"' if href == file else ""
    return f'        <li><a href="{href}"{attivo}>{nome}</a></li>'


# --------------------------------------------------------------------------- pagina

def pagina(file, titolo, descrizione, apertura, corpo, interna=True):
    menu = "\n".join(voce_menu(file, h, n) for h, n in MENU)
    cur = ' aria-current="page"' if file == "prenota.html" else ""
    menu += f'\n        <li><a class="azione" href="prenota.html"{cur}>Prenota {FRECCIA}</a></li>'
    titolo_pag = titolo if file == "index.html" else f"{titolo} – {STUDIO}, Dott.ssa Rossana Binetti"
    if interna:
        apertura = f'''  <section class="apertura-interna">
    <div class="contenitore">
      <p class="etichetta">{ETICHETTE.get(file, "")}</p>
{apertura}
    </div>
  </section>'''
        corpo = f'''  <div class="contenitore">
{corpo}
  </div>'''
    html = f'''<!doctype html>
<html lang="it">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1">
  <title>{titolo_pag}</title>
  <meta name="description" content="{descrizione}">
  <meta name="theme-color" content="#faf6f2">
  <link rel="icon" href="assets/prosopon-marchio.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500&family=Nothing+You+Could+Do&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css?v={VERSIONE_CSS}">
</head>
<body>

<a class="salta" href="#contenuto">Vai al contenuto</a>

<div class="barra-alta">
  <div class="contenitore">
    <ul>
      <li>{ICONE["telefono"]} {TELEFONO}</li>
      <li>{ICONE["chat"]} <a href="{WHATSAPP}">Scrivimi su WhatsApp</a></li>
      <li class="solo-largo">{ICONE["orologio"]} {ORARI}</li>
    </ul>
    <span class="solo-largo">{ICONE["posta"]} {EMAIL}</span>
  </div>
</div>

<header class="top">
  <div class="contenitore">
    <a class="firma" href="index.html">
      <img src="assets/prosopon-orizzontale.svg" alt="{STUDIO} – Studio di Psicologia, Dott.ssa Rossana Binetti" width="483" height="134">
    </a>
    <button class="apri-menu" type="button" aria-expanded="false" aria-controls="menu-principale">
      <span></span><span></span><span></span><span class="sr">Menu</span>
    </button>
    <nav aria-label="Menu principale" id="menu-principale">
      <ul class="menu">
{menu}
      </ul>
    </nav>
  </div>
</header>

<main id="contenuto">
{apertura}
{corpo}
</main>

<footer>
  <section class="piede-contatti" aria-label="Contatti">
    <div class="contenitore">
      <div>
        <p class="etichetta">Contatti</p>
        <p class="nome">Dott.ssa Rossana Binetti</p>
        <p class="ruolo">Psicologa</p>
        <p class="motto">{DC("motto di tre parole")}</p>
      </div>
      <ul>
        <li>{ICONE["telefono"]} {TELEFONO}</li>
        <li>{ICONE["chat"]} <a href="{WHATSAPP}">WhatsApp</a></li>
        <li>{ICONE["posta"]} {EMAIL}</li>
        <li>{ICONE["luogo"]} {DC("indirizzo dello studio")}</li>
        <li>{ICONE["schermo"]} Anche online</li>
      </ul>
      <div class="logo-piede">
        <img src="assets/prosopon-logo.svg" alt="{STUDIO} – Studio di Psicologia, Dott.ssa Rossana Binetti" width="520" height="392">
      </div>
    </div>
  </section>
  <div class="barra">
    <div class="contenitore">
      <span class="albo">© 2026 Dott.ssa Rossana Binetti, Psicologa. Albo Psicologi {DC("regione")} n. {DC("numero")}. P. IVA {DC("…")}</span>
      <ul>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="perche-parlarne.html">Domande frequenti</a></li>
        <li><a href="#contenuto">Torna su</a></li>
      </ul>
    </div>
  </div>
</footer>

<script>
  (function () {{
    var b = document.querySelector('.apri-menu');
    if (!b) return;
    b.addEventListener('click', function () {{
      var aperto = b.getAttribute('aria-expanded') === 'true';
      b.setAttribute('aria-expanded', String(!aperto));
      document.querySelector('.top').classList.toggle('menu-aperto', !aperto);
    }});
  }})();
</script>
</body>
</html>
'''
    with open(os.path.join(OUT, file), "w") as f:
        f.write(html)


# --------------------------------------------------------------------------- mattoncini

def blocco(titolo, testo, attr=""):
    return f'''
    <section class="blocco"{attr}>
      <h2>{titolo}</h2>
      <div class="testo">
{testo}
      </div>
    </section>
'''


def fascia_salvia(etichetta, titolo, testo, citazione):
    return f'''
  </div>
  <section class="fascia-salvia">
    {FOGLIA_GRANDE}
    <div class="contenitore">
      <div>
        <p class="etichetta">{etichetta}</p>
        <h2>{titolo}</h2>
{testo}
      </div>
      <blockquote>{citazione}</blockquote>
    </div>
  </section>
  <div class="contenitore">
'''


def fascia_rosa(etichetta, titolo, testo, azioni):
    return f'''
  </div>
  <section class="fascia-sabbia">
    <div class="contenitore">
      <div>
        <p class="etichetta">{etichetta}</p>
        <h2>{titolo}</h2>
      </div>
      <p>{testo}</p>
      <div class="azioni">{azioni}</div>
    </div>
  </section>
  <div class="contenitore">
'''


PRENOTA_BTN = f'<a class="azione" href="prenota.html">Prenota un primo colloquio {FRECCIA}</a>'
SCRIVIMI_BTN = '<a class="azione leggera" href="contatti.html">Scrivimi</a>'


def servizio(icona, titolo, testo, href):
    return f'''        <li>
          <span class="icona">{ICONE[icona]}</span>
          <h3>{titolo}</h3>
          <p>{testo}</p>
          <a class="collegamento" href="{href}">Scopri di più {FRECCIA}</a>
        </li>'''


def elenco(voci):
    """voci = [(titolo, descrizione), ...] -> elenco con titolo in evidenza."""
    righe = "\n".join(f"          <li><strong>{t}</strong>{d}</li>" for t, d in voci)
    return f'''        <ul class="ambiti">
{righe}
        </ul>'''


def apri_chiudi(contenuto):
    """Il pulsante 'Scopri di più / Chiudi' preso da Dedalo."""
    return f'''        <details class="apri-chiudi">
          <summary><span class="apri">Scopri di più</span><span class="chiudi">Chiudi</span></summary>
          <div class="dettaglio">
{contenuto}
          </div>
        </details>'''


def foto(testo, classe=""):
    return f'<div class="foto {classe}"><span>{DC(testo)}</span></div>'


# =========================================================================== TESTI DI ROSSANA
# Riportati così come li ha scritti (17 novembre 2026).

SOSTEGNO_SOTTOTITOLO = "Uno spazio di ascolto per comprendere ciò che vivi e ritrovare nuove possibilità."
SOSTEGNO_TESTO = [
    "La vita ci pone di fronte a cambiamenti, scelte e situazioni che possono mettere alla prova il nostro equilibrio emotivo e relazionale.",
    "In questi momenti, trovare uno spazio in cui sentirsi ascoltati, accolti e compresi può aiutare a guardare le proprie esperienze da una prospettiva diversa.",
    "Il sostegno psicologico è un percorso di ascolto e riflessione che permette di dare significato a ciò che si sta vivendo, riconoscere le proprie risorse e individuare nuove modalità per affrontare le difficoltà.",
    "Ogni persona porta con sé una storia unica, intrecciata alle relazioni e ai contesti in cui vive. Per questo, il percorso si costruisce insieme, nel rispetto dei bisogni, dei tempi e dell'unicità di ciascuna e ciascuno.",
]
SOSTEGNO_AMBITI = [
    ("Difficoltà emotive e relazionali", "Ansia, stress, insicurezza e momenti di disagio personale."),
    ("Adolescenza e giovani adulti e adulte", "Identità, autostima, relazioni, difficoltà scolastiche e cambiamenti evolutivi."),
    ("Genitorialità e relazioni familiari", "Difficoltà educative, comunicazione e cambiamenti negli equilibri familiari."),
    ("Cambiamenti e transizioni di vita", "Scelte personali, passaggi professionali e ridefinizione dei propri ruoli."),
    ("Separazioni, perdite e momenti critici", "Sostegno nell'affrontare esperienze di cambiamento, vulnerabilità e lutto."),
]
SOSTEGNO_CHIUSA = "L'obiettivo non è offrire risposte già definite, ma accompagnare ogni persona nella ricerca delle proprie."

CRESCITA_SOTTOTITOLO = "Coltivare la consapevolezza, valorizzare le proprie risorse, costruire relazioni più positive."
CRESCITA_TESTO = [
    "Prendersi cura di sé significa anche imparare a conoscersi, ascoltare le proprie emozioni e riconoscere le risorse che ci aiutano ad affrontare le esperienze quotidiane.",
    "Il benessere psicologico si costruisce nel tempo, attraverso una maggiore consapevolezza di sé, la qualità delle relazioni e lo sviluppo di nuove competenze emotive e comunicative.",
    "I percorsi di crescita personale, individuali e di gruppo, offrono occasioni di riflessione e apprendimento per rafforzare le proprie capacità e favorire un maggiore equilibrio nella vita personale, familiare e professionale.",
]
CRESCITA_AMBITI = [
    ("Consapevolezza e gestione delle emozioni", "Riconoscere le proprie emozioni, comprenderne il significato e sviluppare strategie di regolazione emotiva."),
    ("Gestione dello stress e benessere personale", "Individuare le fonti di stress e acquisire strumenti per affrontare con maggiore equilibrio le sfide quotidiane."),
    ("Comunicazione e assertività", "Imparare a esprimere bisogni e opinioni, favorendo relazioni più autentiche e rispettose."),
    ("Sostegno alle competenze genitoriali", "Favorire il dialogo con i figlie e figli comprendere i bisogni emotivi e relazionali nelle diverse fasi della crescita."),
    ("Benessere digitale", "Promuovere un rapporto equilibrato e consapevole con le tecnologie, soprattutto durante l'infanzia e l'adolescenza."),
    ("Prevenzione e benessere nelle scuole", "Percorsi psicoeducativi dedicati alle emozioni, all'identità, alla gestione dei conflitti e alle relazioni tra pari."),
    ("Formazione per insegnanti ed educatori", "Incontri e attività per migliorare la comunicazione, comprendere le dinamiche dei gruppi e promuovere contesti educativi accoglienti."),
]
CRESCITA_CHIUSA = "La crescita personale non è il tentativo di diventare qualcun altro, ma la possibilità di conoscere meglio sé stessi e valorizzare ciò che si è."

# =========================================================================== HOME

aree_home = [
    ("percorsi.html#sostegno", "Ansia e stress"),
    ("percorsi.html#sostegno", "Difficoltà emotive e relazionali"),
    ("adolescenti.html", "Adolescenza"),
    ("percorsi.html#sostegno", "Genitorialità e famiglia"),
    ("percorsi.html#sostegno", "Cambiamenti e transizioni di vita"),
    ("percorsi.html#sostegno", "Separazioni e lutto"),
    ("percorsi.html#crescita", "Gestione delle emozioni"),
    ("percorsi.html#crescita", "Benessere digitale"),
    ("aziende.html", "Benessere al lavoro"),
]
aree_html = "\n".join(f'        <li><a href="{h}">{n}</a></li>' for h, n in aree_home)

HOME_APERTURA = f'''  <section class="eroe">
    <div class="eroe-testo">
      <p class="etichetta">Studio di psicologia a {DC("città")}</p>
      <h1>Dall'ascolto di sé all'ascolto dell'altro.</h1>
      <p class="per-chi">Privati · Adolescenti e famiglie · Aziende</p>
      <p class="modalita">Colloqui in studio e online</p>
      <div class="azioni">
        {PRENOTA_BTN}
        <a class="azione leggera" href="percorsi.html">I percorsi</a>
      </div>
      <p class="a-mano">{lorem(1)[:60]}…</p>
    </div>
    {foto("foto di Rossana")}
  </section>

  <section class="aree">
    <div class="contenitore">
      <h2>Posso aiutarti in queste aree</h2>
      <ul>
{aree_html}
      </ul>
    </div>
  </section>'''

HOME_CORPO = f'''
  <section class="sezione">
    <div class="contenitore">
      <p class="etichetta">Percorsi</p>
      <div class="sezione-testa">
        <h2>Percorsi per persone, famiglie e organizzazioni.</h2>
        <a class="nota-destra" href="percorsi.html">Tutti i percorsi</a>
      </div>
      <ul class="servizi">
{servizio("persona", "Sostegno psicologico", SOSTEGNO_SOTTOTITOLO, "percorsi.html#sostegno")}
{servizio("foglia", "Crescita e benessere", CRESCITA_SOTTOTITOLO, "percorsi.html#crescita")}
{servizio("giovane", "Adolescenti e famiglie", lorem(1), "adolescenti.html")}
{servizio("edificio", "Aziende", lorem(1, 1), "aziende.html")}
      </ul>
    </div>
  </section>

  <section class="fascia-salvia">
    {FOGLIA_GRANDE}
    <div class="contenitore">
      <div>
        <p class="etichetta">Domande frequenti</p>
        <h2>Perché dovrei parlare con uno sconosciuto?</h2>
        <p>{lorem(2)}</p>
        <a class="azione" href="perche-parlarne.html">Leggi le domande e le risposte {FRECCIA}</a>
      </div>
      <blockquote>{SOSTEGNO_CHIUSA}</blockquote>
    </div>
  </section>

  <section class="sezione">
    <div class="contenitore">
      <p class="etichetta">Chi sono</p>
      <div class="professionista">
        {foto("ritratto di Rossana", "ritratto")}
        <div>
          <h2>Dott.ssa Rossana Binetti</h2>
          <p class="qualifica">Psicologa · {DC("n. iscrizione Albo")}</p>
          <p>{lorem(3)}</p>
          <a class="collegamento" href="chi-sono.html">Il mio percorso {FRECCIA}</a>
        </div>
      </div>
    </div>
  </section>

  <section class="fascia-sabbia">
    <div class="contenitore">
      <div>
        <p class="etichetta">Il primo colloquio</p>
        <h2>Un primo passo, insieme.</h2>
      </div>
      <p>{lorem(2, 2)}</p>
      <div class="azioni">{PRENOTA_BTN}</div>
    </div>
  </section>
'''

pagina("index.html", f"{STUDIO} – Studio di Psicologia, Dott.ssa Rossana Binetti",
       "Studio di psicologia della Dott.ssa Rossana Binetti: sostegno psicologico, crescita e benessere, adolescenti e famiglie, aziende.",
       HOME_APERTURA, HOME_CORPO, interna=False)

# =========================================================================== CHI SONO

pagina("chi-sono.html", "Chi sono", "Il percorso e l'approccio della Dott.ssa Rossana Binetti, psicologa.",
       f'''      <h1>Chi sono</h1>
      <p class="sotto">{lorem(1)}</p>''',
       f'''
    <div class="professionista grande">
      {foto("ritratto di Rossana", "ritratto")}
      <div>
        <h2>Dott.ssa Rossana Binetti</h2>
        <p class="qualifica">Psicologa · Albo {DC("regione")} n. {DC("numero")}</p>
{p_lorem(2, 2)}
      </div>
    </div>
''' + blocco("Il mio percorso", p_lorem(2, 2))
       + blocco("Formazione", elenco([(lorem(1)[:40], lorem(1, 1)) for _ in range(3)]))
       + fascia_salvia("Il mio approccio", "Le persone nei loro contesti.", f"        <p>{lorem(3, 1)}</p>\n        <a class=\"collegamento\" href=\"come-lavoro.html\">Come lavoro {FRECCIA}</a>", lorem(1, 3))
       + blocco("Perché faccio questo lavoro", p_lorem(1, 3))
       + fascia_rosa("Parliamone", "Un primo passo, insieme.", lorem(2, 4), PRENOTA_BTN + " " + SCRIVIMI_BTN))

# =========================================================================== PERCORSI (struttura Dedalo)

def percorso(ancora, titolo, sottotitolo, testo, ambiti_titolo, ambiti, chiusa):
    paragrafi = "\n".join(f"        <p>{t}</p>" for t in testo)
    return f'''
    <section class="percorso" id="{ancora}">
      <h2>{titolo}</h2>
      <p class="sottotitolo">{sottotitolo}</p>
      <div class="testo">
{paragrafi}
{apri_chiudi(f"""            <h3>{ambiti_titolo}</h3>
{elenco(ambiti)}
            <p class="chiusa">{chiusa}</p>""")}
      </div>
    </section>
'''


def percorso_rimando(ancora, titolo, href, testo):
    return f'''
    <section class="percorso" id="{ancora}">
      <h2>{titolo}</h2>
      <p class="sottotitolo">{lorem(1)[:70]}…</p>
      <div class="testo">
        <p>{testo}</p>
        <a class="collegamento" href="{href}">Vai alla pagina {FRECCIA}</a>
      </div>
    </section>
'''


pagina("percorsi.html", "Percorsi psicologici",
       "Sostegno psicologico, crescita e benessere, adolescenti e famiglie, aziende.",
       f'''      <h1>Percorsi psicologici</h1>
      <p class="sotto">{lorem(1)}</p>''',
       percorso("sostegno", "Sostegno psicologico", SOSTEGNO_SOTTOTITOLO, SOSTEGNO_TESTO,
                "Ambiti di sostegno", SOSTEGNO_AMBITI, SOSTEGNO_CHIUSA)
       + percorso("crescita", "Crescita e benessere psicologico", CRESCITA_SOTTOTITOLO, CRESCITA_TESTO,
                  "Percorsi e attività", CRESCITA_AMBITI, CRESCITA_CHIUSA)
       + percorso_rimando("adolescenti", "Adolescenti e famiglie", "adolescenti.html", lorem(2))
       + percorso_rimando("aziende", "Aziende", "aziende.html", lorem(2, 2))
       + fascia_rosa("Quale percorso?", "Scegliamolo insieme.", lorem(2, 1), PRENOTA_BTN + " " + SCRIVIMI_BTN))

# =========================================================================== ADOLESCENTI

pagina("adolescenti.html", "Adolescenti e famiglie",
       "Percorsi per adolescenti, genitori e scuole.",
       f'''      <h1>Adolescenti e famiglie</h1>
      <p class="sotto">{lorem(1)}</p>''',
       blocco("Lorem ipsum dolor", p_lorem(2, 2))
       + blocco("Per i ragazzi e le ragazze", p_lorem(1, 3))
       + blocco("Per i genitori", p_lorem(1, 3), ' id="genitori"')
       + fascia_salvia("Scuole", "Per le scuole e gli educatori.", f"        <p>{lorem(3, 2)}</p>", lorem(1, 4))
       + blocco("Per i minorenni", f'        <p class="avviso">Per avviare un percorso con una persona minorenne serve il consenso di entrambi i genitori o di chi esercita la responsabilità genitoriale. {DC("testo da rivedere con Rossana")}</p>')
       + fascia_rosa("Il primo colloquio", "Un primo passo, insieme.", lorem(2, 3), PRENOTA_BTN + ' <a class="azione leggera" href="perche-parlarne.html">Domande frequenti</a>'))

# =========================================================================== AZIENDE

passi_lorem = "\n".join(f"          <li>{lorem(1, i)}</li>" for i in range(3))
pagina("aziende.html", "Aziende",
       "Sportello di ascolto per i dipendenti e servizi per il benessere organizzativo, in collaborazione con la funzione HR.",
       f'''      <h1>Aziende</h1>
      <p class="sotto">{lorem(1, 1)}</p>''',
       blocco("Lo sportello di ascolto", p_lorem(2, 2))
       + blocco("Come funziona", f'''        <ol class="passi">
{passi_lorem}
        </ol>''')
       + fascia_salvia("Riservatezza", "Lorem ipsum dolor sit amet.", f"        <p>{lorem(3, 3)}</p>", lorem(1, 5))
       + blocco("Altri servizi per le organizzazioni", elenco([(lorem(1)[:35], lorem(1, i)) for i in range(4)]))
       + fascia_rosa("Per le aziende", "Parliamone.", lorem(2, 2), f'<a class="azione" href="contatti.html">Contattami {FRECCIA}</a>'))

# =========================================================================== COME LAVORO

pagina("come-lavoro.html", "Come lavoro",
       "L'approccio sistemico-relazionale e come si svolge un percorso.",
       f'''      <h1>Come lavoro</h1>
      <blockquote class="in-evidenza">{lorem(1)[:80]}… <strong>{lorem(1, 2)[:40]}</strong></blockquote>''',
       f'''
    <div class="foto larga"><span>{DC("foto dello studio, a tutta larghezza")}</span></div>
''' + blocco("Un approccio sistemico-relazionale", p_lorem(3, 2))
       + blocco("Il primo colloquio", f'''        <ol class="passi">
{passi_lorem}
        </ol>''')
       + blocco("Durata e frequenza", p_lorem(1, 3))
       + blocco("In studio e online", p_lorem(1, 2))
       + fascia_rosa("Iniziare", "Un primo passo, insieme.", lorem(2), PRENOTA_BTN + " " + SCRIVIMI_BTN))

# =========================================================================== LO STUDIO

galleria = "\n".join(f'      <div class="foto"><span>{DC(f"foto {i}")}</span></div>' for i in range(1, 7))
pagina("studio.html", "Lo studio", "Le foto dello studio e come raggiungerlo.",
       f'''      <h1>Lo studio</h1>
      <p class="sotto">{lorem(1, 1)}</p>''',
       f'''
    <div class="galleria">
{galleria}
    </div>
''' + blocco("Come arrivare", f'''        <dl class="recapiti">
          <dt>Indirizzo</dt>
          <dd>{DC("indirizzo dello studio")}</dd>
          <dt>Mezzi</dt>
          <dd>{lorem(1)}</dd>
          <dt>Parcheggio</dt>
          <dd>{lorem(1, 1)}</dd>
        </dl>
        <div class="mappa">{DC("mappa")}</div>'''))

# =========================================================================== DOMANDE FREQUENTI

DOMANDE = [
    "Perché dovrei parlare con uno sconosciuto?",
    "Non sto male: ha senso rivolgermi a una psicologa?",
    "Quello che dico resta riservato?",
    "Cosa succede al primo colloquio?",
    "Quanto dura un percorso?",
    "Mio figlio non vuole venire. Cosa posso fare?",
    "Psicologa, psicoterapeuta, psichiatra: che differenza c'è?",
    "Si può fare online?",
    "Quanto costa? È detraibile?",
]
voci_faq = "\n".join(f'''        <details class="domanda"{" open" if i == 0 else ""}>
          <summary>{d}</summary>
          <div class="risposta">
            <p>{lorem(2, i)}</p>
          </div>
        </details>''' for i, d in enumerate(DOMANDE))
pagina("perche-parlarne.html", "Domande frequenti",
       "Le domande più comuni prima di rivolgersi a una psicologa.",
       f'''      <h1>Perché dovrei parlare con uno sconosciuto?</h1>
      <p class="sotto">{lorem(1)}</p>''',
       blocco("Domande e risposte", f'''        <div class="domande">
{voci_faq}
        </div>''')
       + fascia_rosa("Un'altra domanda?", "Scrivimi.", lorem(1, 2), f'<a class="azione" href="contatti.html">Scrivimi {FRECCIA}</a> <a class="azione leggera" href="{WHATSAPP}">WhatsApp</a>'))

# =========================================================================== CONTATTI

pagina("contatti.html", "Contatti", "Come contattare la Dott.ssa Rossana Binetti.",
       f'''      <h1>Contatti</h1>
      <p class="sotto">{lorem(1, 1)}</p>''',
       blocco("Scrivimi o chiamami", f'''        <dl class="recapiti">
          <dt>Telefono</dt>
          <dd>{TELEFONO}</dd>
          <dt>WhatsApp</dt>
          <dd><a href="{WHATSAPP}">Scrivimi su WhatsApp</a></dd>
          <dt>Email</dt>
          <dd>{EMAIL}</dd>
          <dt>Orari</dt>
          <dd>{ORARI}</dd>
        </dl>
        <div class="azioni">{PRENOTA_BTN}</div>''')
       + blocco("Dove ci incontriamo", f'''        <dl class="recapiti">
          <dt>In studio</dt>
          <dd>{DC("indirizzo dello studio")}</dd>
          <dt>Online</dt>
          <dd>{lorem(1)}</dd>
        </dl>
        <div class="mappa">{DC("mappa")}</div>''')
       + blocco("Dati professionali", f'''        <ul class="lista">
          <li>Dott.ssa Rossana Binetti, Psicologa</li>
          <li>Iscritta all'Albo degli Psicologi della Regione {DC("regione")}, n. {DC("numero")}</li>
          <li>P. IVA {DC("partita IVA")}</li>
        </ul>
        <p class="avviso">In caso di emergenza non aspettare una risposta via email: chiama il 112.</p>'''))

# =========================================================================== PRENOTA

pagina("prenota.html", "Prenota un colloquio", "Prenota un colloquio in studio o online. Tariffe e modalità.",
       f'''      <h1>Prenota un colloquio</h1>
      <p class="sotto">{lorem(1)}</p>''',
       blocco("Scegli un orario", f'''        <div class="calendario">
          <!-- Qui va incorporata la pagina di prenotazione di Google Calendar -->
          <div class="calendario-segnaposto">Qui comparirà il calendario per le prenotazioni, collegato a Google Calendar.</div>
        </div>
        <p style="margin-top:1.2em">Il pagamento avviene dopo la seduta. {lorem(1, 1)}</p>''', ' id="calendario"')
       + blocco("Tariffe", f'''        <table class="tariffe">
          <tbody>
            <tr><th scope="row">Primo colloquio<span class="nota">{DC("durata")}</span></th><td class="prezzo">{DC("€")}</td></tr>
            <tr><th scope="row">Colloquio individuale<span class="nota">{DC("durata")}</span></th><td class="prezzo">{DC("€")}</td></tr>
            <tr><th scope="row">Colloquio con i genitori<span class="nota">{DC("durata")}</span></th><td class="prezzo">{DC("€")}</td></tr>
            <tr><th scope="row">Percorsi di gruppo<span class="nota">ciclo di incontri</span></th><td class="prezzo">su richiesta</td></tr>
          </tbody>
        </table>''')
       + blocco("Da sapere", f'''        <ul class="lista">
          <li><strong>Disdette:</strong> {lorem(1)}</li>
          <li><strong>Pagamento:</strong> {lorem(1, 1)}</li>
          <li><strong>Minorenni:</strong> {lorem(1, 2)}</li>
          <li><strong>Privacy:</strong> {lorem(1, 3)} <a href="privacy.html">Informativa</a></li>
        </ul>'''))

# =========================================================================== PRIVACY

pagina("privacy.html", "Informativa privacy", "Informativa sul trattamento dei dati personali.",
       '''      <h1>Informativa privacy</h1>''',
       blocco("Da completare", f"        <p>{DC('testo dell’informativa privacy, da far verificare a un professionista')}</p>\n{p_lorem(2, 2)}"))

print("ok")
