"""Genera le pagine HTML del sito con intestazione e piede comuni.

Uso:  python3 strumenti/genera_sito.py .
Modifica i testi in questo file e rilancia il comando: le pagine .html vengono riscritte.
"""
import os, sys

OUT = sys.argv[1]

MENU = [
    ("index.html", "Home"),
    ("chi-sono.html", "Chi sono"),
    ("adolescenti.html", "Adolescenti"),
    ("perche-parlarne.html", "Perché parlarne"),
    ("contatti.html", "Contatti"),
]

ETICHETTE = {
    "chi-sono.html": "Chi sono",
    "adolescenti.html": "Adolescenti",
    "perche-parlarne.html": "Domande frequenti",
    "contatti.html": "Contatti",
    "prenota.html": "Prenotazioni",
    "privacy.html": "Privacy",
}

DC = lambda t: f'<span class="da-completare">[{t}]</span>'
EMAIL = '<a href="mailto:indirizzo@esempio.it">indirizzo@esempio.it</a>'
FRECCIA = '<svg viewBox="0 0 16 16" fill="none" stroke="currentColor" stroke-width="1.4" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="M2 8h12M9.5 3.5 14 8l-4.5 4.5"/></svg>'

ICONE = {
    "persona": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="11" r="5.5"/><path d="M6.5 27c0-5.5 4.3-9 9.5-9s9.5 3.5 9.5 9"/></svg>',
    "persone": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="12" cy="11" r="4.5"/><path d="M4 26c0-4.6 3.6-7.5 8-7.5s8 2.9 8 7.5"/><circle cx="22" cy="12.5" r="3.6"/><path d="M20.5 19.2c4.2-.6 7.5 2 7.5 6.3"/></svg>',
    "giovane": '<svg viewBox="0 0 32 32" aria-hidden="true"><circle cx="16" cy="10" r="4.8"/><path d="M8 27c0-5 3.6-8.4 8-8.4s8 3.4 8 8.4"/><path d="M11.5 8.5c1.5-3 7.5-3.5 9 0"/></svg>',
    "foglia": '<svg viewBox="0 0 32 32" aria-hidden="true"><path d="M7 25C7 13 14 6 26 6c0 12-7 19-19 19Z"/><path d="M7 25 19 13"/></svg>',
    "posta": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="m3.5 7 8.5 6 8.5-6"/></svg>',
    "telefono": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M5 4h3.5l1.5 4-2.2 1.4a11 11 0 0 0 6.8 6.8L16 14l4 1.5V19a2 2 0 0 1-2 2C10.3 21 3 13.7 3 6a2 2 0 0 1 2-2Z"/></svg>',
    "luogo": '<svg viewBox="0 0 24 24" aria-hidden="true"><path d="M12 21s-7-6.2-7-11.5a7 7 0 0 1 14 0C19 14.8 12 21 12 21Z"/><circle cx="12" cy="9.5" r="2.5"/></svg>',
    "schermo": '<svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="4.5" width="18" height="12" rx="1.5"/><path d="M9 20h6M12 16.5V20"/></svg>',
}

FOGLIA_GRANDE = '<svg class="foglia" viewBox="0 0 120 300" fill="none" stroke="currentColor" stroke-width="2" aria-hidden="true"><path d="M60 300V20"/><path d="M60 60c-30-6-44-26-46-44 22 2 40 18 46 44Z" fill="currentColor"/><path d="M60 110c30-6 44-26 46-44-22 2-40 18-46 44Z" fill="currentColor"/><path d="M60 160c-30-6-44-26-46-44 22 2 40 18 46 44Z" fill="currentColor"/><path d="M60 210c30-6 44-26 46-44-22 2-40 18-46 44Z" fill="currentColor"/><path d="M60 260c-30-6-44-26-46-44 22 2 40 18 46 44Z" fill="currentColor"/></svg>'


def pagina(file, titolo, descrizione, apertura, corpo, interna=True):
    voci = []
    for href, nome in MENU:
        cur = ' aria-current="page"' if href == file else ''
        voci.append(f'        <li><a href="{href}"{cur}>{nome}</a></li>')
    cur = ' aria-current="page"' if file == "prenota.html" else ''
    voci.append(f'        <li><a class="azione" href="prenota.html"{cur}>Prenota {FRECCIA}</a></li>')
    menu = "\n".join(voci)
    titolo_pag = titolo if file == "index.html" else f"{titolo} – Rossana Binetti, Psicologa"
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
  <meta name="theme-color" content="#f8f5f0">
  <link rel="icon" href="assets/logo-mark.svg" type="image/svg+xml">
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,500;0,600;1,500&family=Jost:wght@400;500&family=Nothing+You+Could+Do&display=swap" rel="stylesheet">
  <link rel="stylesheet" href="assets/style.css">
</head>
<body>

<a class="salta" href="#contenuto">Vai al contenuto</a>

<header class="top">
  <div class="contenitore">
    <a class="firma" href="index.html">
      <img src="assets/logo-mark.svg" alt="" width="64" height="48">
      <span class="firma-nome">Rossana Binetti<small>Psicologa</small></span>
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
        <p class="motto">Ascolto · Corpo · Relazione</p>
      </div>
      <ul>
        <li>{ICONE["posta"]} {EMAIL}</li>
        <li>{ICONE["telefono"]} {DC("telefono")}</li>
        <li>{ICONE["luogo"]} In presenza a {DC("città")}</li>
        <li>{ICONE["schermo"]} Online</li>
      </ul>
      <div class="logo-piede">
        <img src="assets/logo.svg" alt="Venerdì e Diciassette" width="460" height="400">
      </div>
    </div>
  </section>
  <div class="barra">
    <div class="contenitore">
      <span class="albo">© 2026 Dott.ssa Rossana Binetti, Psicologa. Albo Psicologi {DC("regione")} n. {DC("numero")}. P. IVA {DC("…")}</span>
      <ul>
        <li><a href="privacy.html">Privacy</a></li>
        <li><a href="perche-parlarne.html">Domande frequenti</a></li>
        <li><a href="contatti.html">Contatti</a></li>
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
    """Fascia verde a tutta larghezza (interrompe e riapre il contenitore)."""
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
    """Fascia rosata di chiusura con invito all'azione."""
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


def servizio(icona, titolo, testo, href):
    return f'''        <li>
          <span class="icona">{ICONE[icona]}</span>
          <h3>{titolo}</h3>
          <p>{testo}</p>
          <a class="collegamento" href="{href}">Scopri {FRECCIA}</a>
        </li>'''


# ------------------------------------------------------------------ HOME
HOME_APERTURA = f'''  <section class="eroe">
    <div class="eroe-testo">
      <p class="etichetta">Psicologia per adolescenti e famiglie</p>
      <h1>Dall'ascolto di sé all'ascolto dell'altro.</h1>
      <p class="per-chi">Adolescenti · Genitori · Giovani adulti</p>
      <p class="modalita">Colloqui in presenza e online</p>
      <div class="azioni">
        <a class="azione" href="prenota.html">Prenota un primo colloquio {FRECCIA}</a>
        <a class="azione leggera" href="chi-sono.html">Scopri di più</a>
      </div>
      <p class="a-mano">Uno spazio sicuro per dare voce a ciò che senti.</p>
    </div>
    <div class="foto">
      <span>{DC("foto di Rossana")}</span>
      <span class="didascalia a-mano">Ogni persona ha una storia che merita ascolto.</span>
    </div>
  </section>'''

HOME_CORPO = f'''
  <section class="sezione">
    <div class="contenitore">
      <p class="etichetta">Con chi lavoro</p>
      <div class="sezione-testa">
        <h2>Uno spazio di ascolto, in ogni fase della crescita.</h2>
        <a class="nota-destra" href="perche-parlarne.html">Perché parlare con uno sconosciuto?</a>
      </div>
      <ul class="servizi">
{servizio("giovane", "Adolescenti", "Emozioni, identità, corpo che cambia, amicizie e scuola.", "adolescenti.html")}
{servizio("persone", "Genitori", "Capire le trasformazioni dei figli e come stargli accanto.", "adolescenti.html#genitori")}
{servizio("persona", "Giovani adulti", "Orientarsi, scegliere, dare un nome a ciò che si prova.", "chi-sono.html")}
{servizio("foglia", "Corpo e respiro", "Percorsi di gruppo con pratiche di consapevolezza corporea.", "adolescenti.html#gruppi")}
      </ul>
    </div>
  </section>

  <section class="fascia-salvia">
    {FOGLIA_GRANDE}
    <div class="contenitore">
      <div>
        <p class="etichetta">Il mio percorso</p>
        <h2>Dalla teoria alla pratica, accanto ai ragazzi.</h2>
        <p class="titoli">Psicologa · Tirocinio presso Àntes ODV · {DC("prima laurea / esperienze dal CV")}</p>
        <p>Ho lavorato in centri di ascolto, doposcuola e percorsi psicoeducativi nelle scuole, con preadolescenti, adolescenti e famiglie. Lì ho progettato e condotto laboratori paralleli per i ragazzi e per i loro genitori.</p>
        <a class="collegamento" href="chi-sono.html">Chi sono {FRECCIA}</a>
      </div>
      <blockquote>Ascoltare il corpo è già un primo passo verso l'altro.</blockquote>
    </div>
  </section>

  <section class="sezione">
    <div class="contenitore">
      <p class="etichetta">Il mio modo di lavorare</p>
      <div class="affiancati">
        <div class="foto">{DC("foto dello studio")}</div>
        <div>
          <h2>Ascoltare. Sentire. Crescere insieme.</h2>
          <p>Al centro c'è la relazione: un incontro autentico, senza giudizio, in cui la persona si sente accolta per quello che è. Accanto alla parola do spazio al corpo e al respiro, perché spesso le emozioni si fanno sentire lì prima ancora delle parole.</p>
          <ul class="pilastri">
            <li>{ICONE["persona"]}<strong>La persona</strong><span>Un ascolto autentico, nel rispetto dei suoi tempi.</span></li>
            <li>{ICONE["foglia"]}<strong>Il corpo</strong><span>Respiro e consapevolezza per riconoscere le emozioni.</span></li>
            <li>{ICONE["persone"]}<strong>Le relazioni</strong><span>Gruppo e famiglia come risorse di crescita.</span></li>
          </ul>
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
      <p>Il primo colloquio è un momento per conoscerci: mi racconti cosa ti porta, chiariamo le tue domande e capiamo insieme se questo percorso fa per te. Senza nessun impegno.</p>
      <a class="azione" href="prenota.html">Prenota un primo colloquio {FRECCIA}</a>
    </div>
  </section>
'''

pagina("index.html", "Venerdì e Diciassette – Dott.ssa Rossana Binetti, Psicologa",
  "Rossana Binetti, psicologa. Uno spazio di ascolto per adolescenti, genitori e giovani adulti, che tiene insieme parola, corpo e respiro.",
  HOME_APERTURA, HOME_CORPO, interna=False)

# ------------------------------------------------------------------ CHI SONO
pagina("chi-sono.html", "Chi sono",
  "Chi sono, il mio percorso e il mio modo di intendere la relazione psicologica.",
  '''    <h1>Chi sono</h1>
    <p class="sotto">Credo che ognuno porti con sé un patrimonio unico di risorse, fragilità e possibilità. Il mio lavoro è offrire uno spazio sicuro in cui tutto questo possa essere riconosciuto ed espresso.</p>''',
  blocco("Il mio percorso", f'''      <p>Mi sono laureata in Psicologia all'Università degli Studi Guglielmo Marconi, con una tesi dal titolo <em>Dall'ascolto di sé all'ascolto dell'altro: il ruolo dello Yoga nella relazione psicologica con gli adolescenti</em>.</p>
      <p>Ho svolto il tirocinio pratico valutativo presso il centro diurno Àntes ODV, in servizi dedicati a preadolescenti, adolescenti e famiglie: centri di ascolto, doposcuola assistito e percorsi psicoeducativi nelle scuole. Lì ho progettato e condotto due laboratori paralleli, uno per i ragazzi e le ragazze del centro e uno per i loro genitori.</p>
      <p>{DC("prima laurea, altre esperienze, formazione in corso: dal CV")}</p>''')
  + blocco("Come intendo la relazione", '''      <p>Il mio riferimento principale è l'approccio centrato sulla persona di Carl Rogers. Empatia, autenticità e accettazione incondizionata non sono tecniche da applicare: sono il modo in cui scelgo di stare accanto a chi incontro.</p>
      <p>Ascoltare, per me, significa essere davvero presente: sintonizzarmi su ciò che l'altro vive, rispettarne i tempi e il punto di vista, senza fretta di giudicare o di correggere.</p>''')
  + blocco("Mente e corpo insieme", '''      <p>Le emozioni non abitano solo i pensieri. Il respiro che si accorcia, le spalle che si irrigidiscono, la postura che cambia: il corpo è spesso il primo posto in cui un'emozione si fa sentire.</p>
      <p>Per questo, accanto al colloquio, posso proporre semplici pratiche di consapevolezza corporea e di respirazione, ispirate allo yoga. Le uso come strumenti per imparare ad ascoltarsi e a regolarsi, mai come un fine in sé né come un'alternativa al lavoro psicologico.</p>''')
  + fascia_salvia("Perché lo faccio", "Dall'ascolto di sé all'ascolto dell'altro.", f'''        <p>{DC("qualche riga personale sulla motivazione, con parole sue")}</p>''', "La consapevolezza di sé, quando trova uno spazio per crescere, diventa apertura all'incontro con l'altro.")
  + blocco("Il nome", f'''      <p><em>Venerdì e Diciassette</em>: due bambini, uno in piedi e uno a testa in giù. {DC("la storia del nome e del disegno, raccontata da lei")}</p>
      <p>Mi piace come immagine di questo lavoro: a volte, per capire davvero qualcuno, bisogna provare a guardare il mondo dal suo punto di vista, anche se è capovolto.</p>''')
  + fascia_rosa("Parliamone", "Un primo passo, insieme.", "Se senti che potrebbe esserti utile, il primo passo è un colloquio conoscitivo, senza impegno.", PRENOTA_BTN + ' <a class="azione leggera" href="contatti.html">Scrivimi</a>'))

# ------------------------------------------------------------------ ADOLESCENTI
pagina("adolescenti.html", "Adolescenti",
  "Uno spazio di ascolto per adolescenti e preadolescenti, con percorsi individuali, di gruppo e di sostegno ai genitori.",
  '''    <h1>Crescere è un lavoro difficile.</h1>
    <p class="sotto">L'adolescenza è un periodo in cui cambia tutto insieme: il corpo, le emozioni, le amicizie, il rapporto con i genitori, l'idea di chi si è. Non serve avere “un problema” per meritare uno spazio in cui essere ascoltati.</p>''',
  blocco("Cosa succede in questi anni", '''      <p>Il corpo si trasforma in fretta, a volte più in fretta di quanto si riesca ad accettarlo. Le emozioni diventano più intense e più difficili da gestire. Gli amici contano sempre di più, gli adulti di riferimento vengono messi in discussione.</p>
      <p>Dentro tutto questo, ragazzi e ragazze stanno costruendo la propria identità. Comportamenti che da fuori sembrano solo chiusura, rabbia o provocazione hanno quasi sempre un senso, se letti come parte di questo grande cambiamento.</p>''')
  + blocco("Cosa offro", '''      <h3>Colloqui individuali</h3>
      <p>Uno spazio riservato in cui un ragazzo o una ragazza può parlare liberamente, senza sentirsi giudicato. L'obiettivo è dare un nome a ciò che prova, riconoscere le proprie risorse e trovare modi nuovi di stare con sé e con gli altri.</p>
      <h3 id="gruppi">Percorsi di gruppo con corpo e respiro</h3>
      <p>Piccoli gruppi in cui si alternano attività corporee semplici, respirazione consapevole e momenti di confronto. Per molti ragazzi riconoscere un'emozione parte dal corpo: dal respiro, da una tensione, da una postura. Solo dopo arrivano le parole per raccontarla.</p>
      <p>Il gruppo, quando è un luogo di ascolto reciproco e di rispetto dei tempi di ciascuno, diventa a sua volta uno strumento di crescita.</p>
      <h3 id="genitori">Sostegno ai genitori</h3>
      <p>Incontri individuali o di gruppo per capire meglio le trasformazioni di questa età e trovare chiavi di lettura comuni. Quello che i ragazzi vivono negli incontri ha più valore quando trova continuità anche a casa.</p>''')
  + fascia_salvia("Il mio approccio", "Corpo, gruppo, famiglia.", '''        <p>Nel lavoro con gli adolescenti ho visto tre livelli intrecciarsi continuamente: il corpo, come via d'accesso alle emozioni; il gruppo dei pari, come spazio sicuro in cui riconoscersi negli altri; la famiglia, perché ciò che cambia possa continuare nella vita di ogni giorno.</p>
        <p>Tenerli insieme rende il percorso più solido.</p>''', "Non serve avere un problema per meritare di essere ascoltati.")
  + blocco("Prevenire, non solo curare", f'''      <p>L'adolescenza è una finestra preziosa per sviluppare competenze che accompagneranno la persona per tutta la vita: riconoscere e regolare le emozioni, comunicare, gestire lo stress, chiedere aiuto.</p>
      <p>Per questo propongo percorsi anche a scuole, associazioni e centri educativi. {DC("confermare se vuole offrire questo servizio")}</p>''')
  + blocco("Quando chiedere un colloquio", '''      <p>Non c'è bisogno di aspettare che le cose vadano male. Può essere utile, per esempio, quando un figlio o una figlia:</p>
      <ul class="lista">
        <li>sembra spesso in ansia, triste o irritabile, più del solito e più a lungo;</li>
        <li>si chiude, evita gli amici o la scuola;</li>
        <li>vive con fatica il proprio corpo o i cambiamenti che sta attraversando;</li>
        <li>attraversa un momento di passaggio: un trasloco, una separazione, un lutto, un cambio di scuola.</li>
      </ul>
      <p>Oppure, semplicemente, quando il dialogo in famiglia si è fatto difficile e serve un punto di vista esterno.</p>''')
  + blocco("Per i minorenni", '''      <p class="avviso">Per avviare un percorso con un ragazzo o una ragazza minorenne è necessario il consenso di entrambi i genitori, o di chi esercita la responsabilità genitoriale. Il primo incontro può essere fatto con i genitori, da soli o insieme al figlio.</p>''')
  + fascia_rosa("Il primo colloquio", "Un primo passo, insieme.", "Il primo incontro può essere con il ragazzo, con i genitori o con tutti insieme. Lo decidiamo in base a cosa vi fa sentire più a vostro agio.", PRENOTA_BTN + ' <a class="azione leggera" href="perche-parlarne.html">Domande frequenti</a>'))

# ------------------------------------------------------------------ PERCHÉ PARLARNE
def q(domanda, risposta, aperta=False):
    o = " open" if aperta else ""
    return f'''        <details class="domanda"{o}>
          <summary>{domanda}</summary>
          <div class="risposta">
{risposta}
          </div>
        </details>'''

domande_tu = "\n".join([
  q("Perché dovrei parlare con uno sconosciuto?", '''            <p>Proprio perché non mi conosci. Con le persone a cui vogliamo bene tendiamo a proteggerle, a non farle preoccupare, a temere il loro giudizio. Con una psicologa non c'è niente da proteggere: puoi dire le cose come stanno, anche quelle che non hai mai detto a nessuno.</p>
            <p>Non sono lì per giudicarti né per dirti cosa fare, ma per ascoltarti e aiutarti a capire meglio quello che vivi. E tutto resta tra noi.</p>''', aperta=True),
  q("Non sono “matto”. Ho davvero bisogno di uno psicologo?", '''            <p>Non serve stare male per parlare con uno psicologo, così come non serve essere malati per andare da un medico per un controllo. Si può venire per un momento di confusione, una scelta difficile, un periodo di stanchezza, o semplicemente per conoscersi meglio.</p>'''),
  q("Quello che dico resta riservato?", '''            <p>Sì. La psicologa è tenuta al segreto professionale: quello che racconti non esce dalla stanza, se non nei rarissimi casi previsti dalla legge, quando c'è un pericolo serio per la vita o la salute di qualcuno. Se dovesse succedere, te ne parlerei prima.</p>
            <p>Con i ragazzi minorenni, all'inizio del percorso chiarisco con loro e con i genitori cosa resta riservato e cosa invece è giusto condividere.</p>'''),
  q("Cosa succede al primo colloquio?", '''            <p>Ci conosciamo. Mi racconti cosa ti porta da me, con i tuoi tempi e con le parole che vuoi. Io ti faccio qualche domanda e ti spiego come lavoro. Alla fine valutiamo insieme se e come proseguire: non c'è nessun obbligo.</p>'''),
  q("Quanto dura un percorso?", '''            <p>Dipende da cosa ti porta e da cosa desideri. A volte bastano pochi incontri per fare chiarezza, altre volte serve più tempo. Ne parliamo apertamente fin dall'inizio e facciamo il punto insieme lungo la strada.</p>'''),
  q("Che c'entrano il corpo e il respiro? Devo fare yoga?", '''            <p>No, non devi saper fare niente. Quando può essere utile, propongo semplici esercizi di respirazione o di attenzione al corpo, ispirati allo yoga: servono a notare come ci si sente, a calmarsi, a ritrovare un contatto con sé. Sono sempre una proposta, mai un obbligo.</p>'''),
])

domande_genitori = "\n".join([
  q("Mio figlio non vuole venire. Cosa posso fare?", '''            <p>È più comune di quanto si pensi, e non è un fallimento. Si può partire da un incontro con voi genitori, per capire insieme cosa sta succedendo e come avvicinarsi a lui senza forzarlo. A volte, quando un ragazzo vede che lo spazio è davvero suo, la diffidenza si scioglie.</p>'''),
  q("Posso venire io, genitore, senza mio figlio?", '''            <p>Certo. Il sostegno ai genitori è una parte importante del mio lavoro: capire le trasformazioni di questa età aiuta a stare accanto ai figli con più serenità.</p>'''),
  q("Serve il consenso di tutti e due i genitori?", '''            <p>Sì, per un percorso con un minorenne serve il consenso di entrambi i genitori o di chi esercita la responsabilità genitoriale. Se la situazione familiare è complessa, ne parliamo prima e troviamo insieme la strada corretta.</p>'''),
])

domande_pratiche = "\n".join([
  q("Psicologa, psicoterapeuta, psichiatra: che differenza c'è?", f'''            <p>La <strong>psicologa</strong> si occupa di ascolto, sostegno, consulenza e prevenzione, aiutando la persona a comprendere e affrontare le proprie difficoltà. Lo <strong>psicoterapeuta</strong> ha una specializzazione ulteriore di quattro anni per la cura dei disturbi psicologici. Lo <strong>psichiatra</strong> è un medico e può prescrivere farmaci.</p>
            <p>Io sono psicologa {DC("aggiornare se inizierà una scuola di specializzazione")}. Se durante il nostro lavoro emergesse il bisogno di un altro professionista, te lo direi con chiarezza e ti aiuterei a trovarlo.</p>'''),
  q("Si può fare online?", '''            <p>Sì, i colloqui si possono fare anche in videochiamata. Per molte persone è più comodo, e per alcuni ragazzi è persino più facile aprirsi da casa propria. Serve solo un luogo tranquillo e una connessione stabile.</p>'''),
  q("Quanto costa? È detraibile?", '''            <p>Le tariffe sono indicate nella pagina <a href="prenota.html">Prenota un colloquio</a>. Le prestazioni psicologiche sono spese sanitarie detraibili: ricevi sempre regolare fattura.</p>'''),
])

pagina("perche-parlarne.html", "Perché dovrei parlare con uno sconosciuto?",
  "Le domande più comuni prima di rivolgersi a una psicologa: riservatezza, primo colloquio, durata, adolescenti e genitori, costi.",
  '''    <h1>Perché dovrei parlare con uno sconosciuto?</h1>
    <p class="sotto">È la domanda che quasi tutti si fanno, anche se pochi la dicono ad alta voce. Qui trovi questa e altre risposte, scritte con parole semplici.</p>''',
  blocco("Se stai pensando di venire", f'''      <div class="domande">
{domande_tu}
      </div>''')
  + blocco("Se sei un genitore", f'''      <div class="domande">
{domande_genitori}
      </div>''')
  + blocco("Domande pratiche", f'''      <div class="domande">
{domande_pratiche}
      </div>''')
  + fascia_rosa("Hai un'altra domanda?", "Scrivimi, ti rispondo volentieri.", "Anche se non sei ancora sicuro di voler iniziare: chiedere informazioni non impegna a nulla.", f'<a class="azione" href="contatti.html">Scrivimi {FRECCIA}</a> <a class="azione leggera" href="prenota.html">Prenota un colloquio</a>'))

# ------------------------------------------------------------------ CONTATTI
pagina("contatti.html", "Contatti",
  "Come contattare la Dott.ssa Rossana Binetti: email, telefono, studio e colloqui online.",
  '''    <h1>Contatti</h1>
    <p class="sotto">Puoi scrivermi per una domanda, per capire se posso esserti utile o per fissare un primo colloquio. Rispondo personalmente a ogni messaggio.</p>''',
  blocco("Scrivimi o chiamami", f'''      <dl class="recapiti">
        <dt>Email</dt>
        <dd>{EMAIL}</dd>
        <dt>Telefono</dt>
        <dd>{DC("numero di telefono")}</dd>
        <dt>Rispondo</dt>
        <dd>{DC("giorni e fasce orarie")}. Se non posso rispondere subito, ti richiamo appena possibile.</dd>
      </dl>
      <div class="azioni">
        <a class="azione" href="mailto:indirizzo@esempio.it">Scrivi una email</a>
        <a class="azione leggera" href="prenota.html">Prenota un colloquio</a>
      </div>''')
  + blocco("Dove ci incontriamo", f'''      <dl class="recapiti">
        <dt>In studio</dt>
        <dd>{DC("indirizzo dello studio")}</dd>
        <dt>Online</dt>
        <dd>In videochiamata, da dove ti trovi.</dd>
      </dl>
      <div class="mappa">{DC("qui la mappa dello studio, quando ci sarà l'indirizzo")}</div>''')
  + blocco("Dati professionali", f'''      <ul class="lista">
        <li>Dott.ssa Rossana Binetti, Psicologa</li>
        <li>Iscritta all'Albo degli Psicologi della Regione {DC("regione")}, n. {DC("numero")}</li>
        <li>P. IVA {DC("partita IVA")}</li>
      </ul>
      <p class="avviso">Se stai vivendo un'emergenza o temi per la tua sicurezza o per quella di qualcun altro, non aspettare una risposta via email: chiama il 112.</p>'''))

# ------------------------------------------------------------------ PRENOTA
pagina("prenota.html", "Prenota un colloquio",
  "Prenota un colloquio in studio o online. Tariffe e modalità degli incontri.",
  '''    <h1>Prenota un colloquio</h1>
    <p class="sotto">Scegli giorno e orario tra quelli disponibili. Riceverai una mail di conferma con tutti i dettagli dell'appuntamento.</p>''',
  blocco("Tariffe", f'''      <table class="tariffe">
        <tbody>
          <tr><th scope="row">Primo colloquio conoscitivo<span class="nota">50 minuti, in studio o online</span></th><td class="prezzo">{DC("€")}</td></tr>
          <tr><th scope="row">Colloquio individuale<span class="nota">50 minuti</span></th><td class="prezzo">{DC("€")}</td></tr>
          <tr><th scope="row">Colloquio con i genitori<span class="nota">60 minuti</span></th><td class="prezzo">{DC("€")}</td></tr>
          <tr><th scope="row">Percorsi di gruppo per ragazzi<span class="nota">ciclo di incontri</span></th><td class="prezzo">su richiesta</td></tr>
        </tbody>
      </table>
      <p style="margin-top:1.2em;font-size:1rem">Le prestazioni psicologiche sono detraibili come spese sanitarie. Ricevi sempre regolare fattura.</p>''')
  + blocco("Scegli un orario", '''      <div class="calendario">
        <!--
          INCOLLARE QUI il codice "Pagina di prenotazione in linea" di Google Calendar
          (Calendar > pagina di prenotazione > Opzioni > Opzioni di condivisione > Incorpora nel sito web)
          al posto del blocco segnaposto qui sotto.
        -->
        <div class="calendario-segnaposto">Qui comparirà il calendario per le prenotazioni, collegato a Google Calendar.</div>
      </div>
      <p style="margin-top:1.2em;font-size:1rem">Preferisci prima un contatto? <a href="contatti.html">Scrivimi</a>.</p>''', ' id="calendario"')
  + blocco("Da sapere", f'''      <ul class="lista">
        <li><strong>Dove:</strong> {DC("indirizzo dello studio")}, oppure online in videochiamata.</li>
        <li><strong>Disdette:</strong> ti chiedo di avvisarmi almeno 24 ore prima. {DC("confermare")}</li>
        <li><strong>Minorenni:</strong> serve il consenso di entrambi i genitori. Per il primo incontro, prenota a nome di un genitore.</li>
        <li><strong>Privacy:</strong> i dati servono solo a gestire l'appuntamento e sono trattati nel rispetto del segreto professionale e del GDPR. <a href="privacy.html">Informativa</a></li>
      </ul>'''))

# ------------------------------------------------------------------ PRIVACY (segnaposto)
pagina("privacy.html", "Informativa privacy",
  "Informativa sul trattamento dei dati personali.",
  '''    <h1>Informativa privacy</h1>
    <p class="sotto">Come vengono trattati i dati personali raccolti attraverso questo sito.</p>''',
  blocco("Da completare", f'''      <p>{DC("testo dell'informativa privacy ai sensi del GDPR: titolare, finalità, base giuridica, conservazione, diritti, servizi terzi usati (Google Calendar, Google Fonts, GitHub Pages)")}</p>
      <p>È consigliabile farla redigere o verificare da un professionista, perché nel lavoro della psicologa si trattano dati relativi alla salute.</p>'''))

print("ok")
