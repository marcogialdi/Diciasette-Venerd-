# Venerdì e Diciassette

Sito della Dott.ssa Rossana Binetti, psicologa. Sito statico pubblicato con GitHub Pages:
https://marcogialdi.github.io/Diciasette-Venerd-/

## Struttura

| File | Pagina |
|---|---|
| `index.html` | Home |
| `chi-sono.html` | Chi sono |
| `adolescenti.html` | Adolescenti |
| `perche-parlarne.html` | Perché dovrei parlare con uno sconosciuto? (domande frequenti) |
| `contatti.html` | Contatti |
| `prenota.html` | Prenota un colloquio (tariffe e calendario Google) |
| `privacy.html` | Informativa privacy (da completare) |
| `assets/style.css` | Stile di tutto il sito |
| `assets/logo*.svg` | Logo in versione verticale, orizzontale e solo disegno |

## Come modificare i testi

Intestazione, menu e piede sono uguali su tutte le pagine, quindi i testi si modificano in un solo posto:

1. apri `strumenti/genera_sito.py` e cambia i testi;
2. dal terminale, nella cartella del sito, lancia `python3 strumenti/genera_sito.py .`;
3. fai commit e push: GitHub Pages pubblica da solo in un paio di minuti.

Se modifichi a mano un file `.html`, ricordati che verrà sovrascritto al prossimo lancio dello script.

## Da completare

Tutto ciò che manca è evidenziato in giallo nel sito (classe `da-completare`). Per trovarlo: `grep -n "da-completare" strumenti/genera_sito.py`.

- foto di Rossana (home) e dello studio: salvarle in `assets/` e sostituire i riquadri `.foto`;
- Albo, partita IVA, email, telefono, città e indirizzo dello studio;
- tariffe e politica di disdetta;
- informativa privacy (meglio farla verificare da un professionista: si trattano dati sanitari).

## Prenotazioni con Google Calendar

In Google Calendar: pagina di prenotazione → Opzioni → Opzioni di condivisione → Incorpora nel sito web → "Pagina di prenotazione in linea". Copiare l'iframe e incollarlo in `strumenti/genera_sito.py`, nel blocco "Scegli un orario", al posto del `calendario-segnaposto`.

Consiglio: usare un account Google dedicato all'attività, perché la pagina di prenotazione mostra nome e foto dell'account.
