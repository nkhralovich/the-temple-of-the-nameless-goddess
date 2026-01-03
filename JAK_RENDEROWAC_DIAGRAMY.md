# Jak renderować diagramy Mermaid do sprawozdania

Diagramy w plikach `class_diagram.md` i `sequence_diagram.md` są napisane w notacji Mermaid. Oto kilka sposobów na ich renderowanie:

## Metoda 1: GitHub (najłatwiejsza)
1. Wrzuć pliki na GitHub
2. Otwórz pliki `.md` w przeglądarce GitHub
3. GitHub automatycznie wyrenderuje diagramy Mermaid
4. Zrób screenshot (Win: `Win+Shift+S`, Mac: `Cmd+Shift+4`, Linux: `Shift+PrtScr`)

## Metoda 2: VSCode (jeśli używasz)
1. Zainstaluj rozszerzenie: **Markdown Preview Mermaid Support**
2. Otwórz plik `.md`
3. Kliknij prawym przyciskiem → "Markdown: Open Preview to the Side"
4. Diagramy będą widoczne w podglądzie
5. Zrób screenshot

## Metoda 3: Mermaid Live Editor (online)
1. Otwórz: https://mermaid.live/
2. Skopiuj kod z sekcji ```mermaid ... ``` (bez znaczników)
3. Wklej do edytora
4. Kliknij "PNG" lub "SVG" aby pobrać obraz

## Metoda 4: Obsidian (jeśli używasz do notatek)
1. Otwórz pliki `.md` w Obsidian
2. Diagramy Mermaid renderują się automatycznie
3. Zrób screenshot

## Metoda 5: Mermaid CLI (dla zaawansowanych)
```bash
# Instalacja
npm install -g @mermaid-js/mermaid-cli

# Renderowanie
mmdc -i class_diagram.md -o class_diagram.png
mmdc -i sequence_diagram.md -o sequence_diagram.png
```

## Metoda 6: Draw.io / Diagrams.net
1. Otwórz https://app.diagrams.net/
2. File → Import from → Text (Mermaid)
3. Wklej kod Mermaid
4. Wyeksportuj jako PNG/PDF

## Wskazówki do sprawozdania

### Format obrazów
- **Preferowane formaty**: PNG (dla screenshots), SVG (dla wektorów)
- **Rozdzielczość**: minimum 1200px szerokości
- **Nazwy plików**:
  - `diagram_klas.png`
  - `diagram_sekwencji_factory.png`
  - `diagram_sekwencji_strategy.png`

### Gdzie umieścić w sprawozdaniu
1. **Diagram klas** - Sekcja 3.1
2. **Diagram sekwencji (Factory)** - Sekcja 2.1 (Factory Pattern)
3. **Diagram sekwencji (Strategy)** - Sekcja 2.2 (Strategy Pattern)

### Alternatywa: Link do GitHub
Jeśli renderujesz przez GitHub, możesz podać link zamiast embedować obrazy:
```markdown
Diagram klas dostępny online:
https://github.com/[twoj-username]/the-temple-of-the-nameless-goddess/blob/main/class_diagram.md
```

---

## Quick Start dla nagrania video

Podczas nagrywania video, możesz:
1. Otworzyć `class_diagram.md` w GitHub/VSCode z podglądem
2. Pokazać kod obok diagramu
3. Wytłumaczyć relacje między klasami wskazując na diagram

**Przykładowy scenariusz:**
- "Tutaj widzicie diagram klas... (pokaż diagram)"
- "Zacznę od Factory Pattern - widzicie klasę EnemyFactory..." (pokaż w kodzie enemy.py)
- "Ta klasa tworzy różne typy wrogów..." (pokaż na diagramie strzałki creates)
- "Dzięki temu w main.py wystarczy wywołać..." (pokaż w main.py)
