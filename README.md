<div align="center">

```
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
 ░                                                                     ░
 ░    ███████╗██╗  ██╗██████╗ ██╗   ██╗████████╗██╗                   ░
 ░    ██╔════╝██║  ██║██╔══██╗██║   ██║╚══██╔══╝██║                   ░
 ░    ███████╗███████║██████╔╝██║   ██║   ██║   ██║                   ░
 ░    ╚════██║██╔══██║██╔══██╗██║   ██║   ██║   ██║                   ░
 ░    ███████║██║  ██║██║  ██║╚██████╔╝   ██║   ██║                   ░
 ░    ╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝ ╚═════╝    ╚═╝   ╚═╝                   ░
 ░                                                                     ░
 ░          ██████╗ ██╗   ██╗██╗██╗     ██████╗ ███████╗██████╗       ░
 ░          ██╔══██╗██║   ██║██║██║     ██╔══██╗██╔════╝██╔══██╗      ░
 ░          ██████╔╝██║   ██║██║██║     ██║  ██║█████╗  ██████╔╝      ░
 ░          ██╔══██╗██║   ██║██║██║     ██║  ██║██╔══╝  ██╔══██╗      ░
 ░          ██████╔╝╚██████╔╝██║███████╗██████╔╝███████╗██║  ██║      ░
 ░          ╚═════╝  ╚═════╝ ╚═╝╚══════╝╚═════╝ ╚══════╝╚═╝  ╚═╝      ░
 ░                                                                     ░
 ░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░░
```

### *12 Agents. One Command. Zero Slides Left Behind.*

<br>

[![Python](https://img.shields.io/badge/Python-3.10%2B-FFD43B?style=for-the-badge&logo=python&logoColor=black)](https://python.org)
[![Gemini](https://img.shields.io/badge/Gemini-2.5--Pro-4285F4?style=for-the-badge&logo=google&logoColor=white)](https://deepmind.google/technologies/gemini/)
[![LangGraph](https://img.shields.io/badge/LangGraph-Orchestration-FF6B6B?style=for-the-badge&logo=langchain&logoColor=white)](https://langchain.com)
[![License](https://img.shields.io/badge/License-MIT-00C9A7?style=for-the-badge)](./LICENSE)
[![Status](https://img.shields.io/badge/Status-Actively%20Maintained-brightgreen?style=for-the-badge)](.)

</div>

---

<br>

## ⚡ What Is This, Actually?

> You drop a PDF. You type a topic. You walk away.  
> Twelve agents later — you have a **boardroom-ready pitch deck**.

ShrutiBuilder is not a "template filler." It does not take your bullet points and slap them onto a slide theme. It **reads**, **reasons**, **researches**, **architects**, **diagrams**, and **designs** — all autonomously, all chained together by a multi-agent graph that knows what it's doing.

This is the kind of tool you build once and wonder how you ever lived without.

<br>

---

<br>

## 🧠 The Agent Pipeline — All 12, Explained

```
  INPUT: topic + optional PDF + slide limit + special instructions
    │
    ▼
┌─────────────────────────────────────────────────────────────────────┐
│                                                                     │
│  [01] PDF READER          → Extracts & structures raw content       │
│          │                                                          │
│  [02] TOPIC ANALYZER      → Understands core domain & problem       │
│          │                                                          │
│  [03] MARKET RESEARCHER   → Pulls real-world competitive context    │
│          │                                                          │
│  [04] PROBLEM FRAMER      → Crystallizes pain points & opportunity  │
│          │                                                          │
│  [05] SOLUTION INVENTOR   → Ideates the product/approach            │
│          │                                                          │
│  [06] SYSTEM ARCHITECT    → Designs the technical solution stack    │
│          │                                                          │
│  [07] DIAGRAM GENERATOR   → Builds Mermaid architecture diagrams    │
│          │                                                          │
│  [08] CONTENT WRITER      → Writes every slide's narrative copy     │
│          │                                                          │
│  [09] DECK DESIGNER       → Applies visual hierarchy & layout rules │
│          │                                                          │
│  [10] PPTX BUILDER        → Natively assembles the .pptx file       │
│          │                                                          │
│  [11] PDF CONVERTER       → Converts deck → polished .pdf           │
│          │                                                          │
│  [12] QA VALIDATOR        → Reviews and logs final output quality   │
│                                                                     │
└─────────────────────────────────────────────────────────────────────┘
    │
    ▼
  OUTPUT: /output/deck.pptx  +  /output/deck.pdf  +  /logs/run.log
```

<br>

---

<br>

## 🔥 Features That Actually Matter

<table>
<tr>
<td width="50%">

**🤖 True Multi-Agent Orchestration**  
Built on `LangChain` + `LangGraph`. Not fake sequential calls — actual stateful agent graph with memory, retries, and conditional routing between nodes.

</td>
<td width="50%">

**🧬 Gemini 2.5-Pro Intelligence**  
Every agent runs on Google's most capable model. The research agent uses it for grounding, the architect uses it for system design, the writer uses it for consulting-level narrative.

</td>
</tr>
<tr>
<td>

**📐 Native PPTX Generation**  
Zero web rendering, zero Puppeteer, zero screenshots. Slides are built atom-by-atom using `python-pptx` — that means perfect formatting, real fonts, real layouts.

</td>
<td>

**📊 AI-Generated Architecture Diagrams**  
Mermaid code is auto-generated by the Diagram Agent and injected directly into your slides. Every deck ships with a real system architecture visual.

</td>
</tr>
<tr>
<td>

**📄 One-Click PDF Export**  
After PPTX generation, the converter agent seamlessly exports to `.pdf`. No manual steps. Works via Microsoft Office COM automation on Windows.

</td>
<td>

**📋 Full Run Logs**  
Every agent's reasoning, every decision, every diagram — all logged to `/logs/`. You can trace exactly why every slide looks the way it does.

</td>
</tr>
</table>

<br>

---

<br>

## 🛠 Installation

**Step 1 — Clone the repo**
```bash
git clone https://github.com/yourusername/ShrutiBuilder.git
cd ShrutiBuilder
```

**Step 2 — Create & activate a virtual environment**
```bash
python -m venv venv

# Windows
.\venv\Scripts\activate

# macOS / Linux
source venv/bin/activate
```

**Step 3 — Install dependencies**
```bash
pip install -r requirements.txt
```

**Step 4 — Set up your environment**
```bash
# Rename the example env file
cp .env.example .env

# Open .env and add your Gemini API key
GOOGLE_GEMINI_API_KEY=your_actual_key_here
```

> **Get a Gemini API key** → [aistudio.google.com](https://aistudio.google.com/)

<br>

---

<br>

## 🚀 Usage

```bash
python main.py
```

You'll be guided through 4 prompts:

```
┌────────────────────────────────────────────────────────────┐
│                                                            │
│  [?] ShrutiBuilder Topic / Subject                         │
│      > e.g. "AI-powered supply chain optimization"         │
│                                                            │
│  [?] Path to Requirements PDF (optional, press Enter skip) │
│      > e.g. "./docs/requirements.pdf"                      │
│                                                            │
│  [?] Slide limit                                           │
│      > e.g. 15                                             │
│                                                            │
│  [?] Special instructions for judges                       │
│      > e.g. "Focus on ROI metrics and enterprise scale"    │
│                                                            │
└────────────────────────────────────────────────────────────┘
```

Then just... **wait**. All 12 agents run automatically.

<br>

---

<br>

## 📁 Project Structure

```
ShrutiBuilder/
│
├── main.py                    ← Entry point. Run this.
│
├── agents/
│   ├── pdf_reader.py          ← Agent 01: PDF extraction
│   ├── topic_analyzer.py      ← Agent 02: Domain analysis
│   ├── market_researcher.py   ← Agent 03: Market research
│   ├── problem_framer.py      ← Agent 04: Problem framing
│   ├── solution_inventor.py   ← Agent 05: Solution ideation
│   ├── system_architect.py    ← Agent 06: Technical architecture
│   ├── diagram_generator.py   ← Agent 07: Mermaid diagram gen
│   ├── content_writer.py      ← Agent 08: Slide copy writing
│   ├── deck_designer.py       ← Agent 09: Visual layout rules
│   ├── pptx_builder.py        ← Agent 10: Native PPTX creation
│   ├── pdf_converter.py       ← Agent 11: PPTX → PDF
│   └── qa_validator.py        ← Agent 12: Quality assurance
│
├── graph/
│   └── pipeline.py            ← LangGraph orchestration graph
│
├── utils/
│   ├── logger.py              ← Logging utilities
│   └── helpers.py             ← Shared helper functions
│
├── output/                    ← Generated decks land here
├── logs/                      ← Agent reasoning logs
│
├── .env.example               ← Copy → .env, add your key
├── requirements.txt
└── README.md
```

<br>

---

<br>

## 📦 Requirements

```txt
langchain
langgraph
langchain-google-genai
python-pptx
mermaid-py
pypdf2
python-dotenv
google-generativeai
Pillow
comtypes          # Windows only, for PDF conversion via MS Office
```

Install all at once:
```bash
pip install -r requirements.txt
```

> **Windows users:** PDF conversion requires Microsoft PowerPoint installed. On Linux/Mac, PDF export uses LibreOffice or is skipped gracefully.

<br>

---

<br>

## 🔑 Environment Variables

| Variable | Required | Description |
|---|---|---|
| `GOOGLE_GEMINI_API_KEY` | ✅ Yes | Your Google AI Studio API key |
| `LOG_LEVEL` | Optional | `DEBUG` / `INFO` / `WARNING` (default: `INFO`) |
| `OUTPUT_DIR` | Optional | Custom output path (default: `./output`) |
| `MAX_RETRIES` | Optional | Agent retry limit on failure (default: `3`) |

<br>

---

<br>

## 🗺 How The Agent Graph Works

```
                    ┌─────────────────┐
                    │   User Inputs   │
                    └────────┬────────┘
                             │
              ┌──────────────▼──────────────┐
              │        PDF READER           │  ← if PDF provided
              │   (skips if no PDF given)   │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │      TOPIC ANALYZER         │  ← always runs
              └──────┬──────────────┬───────┘
                     │              │
           ┌─────────▼──┐    ┌──────▼──────────┐
           │  MARKET     │    │  PROBLEM        │
           │  RESEARCHER │    │  FRAMER         │
           └─────────┬───┘    └──────┬──────────┘
                     │               │
                     └──────┬────────┘
                            │
           ┌────────────────▼───────────────┐
           │        SOLUTION INVENTOR        │
           └────────────────┬───────────────┘
                            │
           ┌────────────────▼───────────────┐
           │       SYSTEM ARCHITECT          │
           └──────────┬─────────────┬───────┘
                      │             │
              ┌───────▼──┐   ┌──────▼────────┐
              │ DIAGRAM   │   │ CONTENT       │
              │ GENERATOR │   │ WRITER        │
              └───────┬───┘   └──────┬────────┘
                      │              │
                      └──────┬───────┘
                             │
              ┌──────────────▼──────────────┐
              │        DECK DESIGNER         │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │        PPTX BUILDER          │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │        PDF CONVERTER         │
              └──────────────┬──────────────┘
                             │
              ┌──────────────▼──────────────┐
              │        QA VALIDATOR          │
              └──────────────┬──────────────┘
                             │
                    ┌────────▼────────┐
                    │  /output/ ready │
                    └─────────────────┘
```

<br>

---

<br>

## 🧪 Example Output

After running with topic: *"AI-Powered Crowd Safety Platform"*

```
✅ [Agent 01] PDF Reader         — Processed 14 pages, 3,847 tokens extracted
✅ [Agent 02] Topic Analyzer     — Domain: Public Safety / Smart Infrastructure
✅ [Agent 03] Market Researcher  — Found 6 competitors, TAM: $4.2B by 2028
✅ [Agent 04] Problem Framer     — 3 core pain points identified
✅ [Agent 05] Solution Inventor  — Proposed YOLOv8 + IoT + NTES integration
✅ [Agent 06] System Architect   — 5-layer microservices architecture designed
✅ [Agent 07] Diagram Generator  — Mermaid diagram: 12 nodes, 16 edges
✅ [Agent 08] Content Writer     — 15 slides, 2,100 words of narrative copy
✅ [Agent 09] Deck Designer      — Layout rules applied, slide templates chosen
✅ [Agent 10] PPTX Builder       — deck.pptx generated (4.2 MB, 15 slides)
✅ [Agent 11] PDF Converter      — deck.pdf generated (2.8 MB)
✅ [Agent 12] QA Validator       — Score: 94/100. 0 critical issues.

📁 Output saved to: ./output/
   ├── deck.pptx
   └── deck.pdf

⏱  Total time: 2m 34s
```

<br>

---

<br>

## ⚠️ Known Limitations

- PDF conversion to `.pdf` requires **Microsoft PowerPoint** on Windows. On other OS, only `.pptx` is generated.
- Gemini API rate limits may cause delays for very large PDFs (>50 pages). The retry logic handles this, but expect longer run times.
- Mermaid diagram rendering quality depends on complexity — very large graphs (20+ nodes) may be truncated.
- Internet connection required for market research agent (uses Gemini's grounding feature).

<br>

---

<br>

## 🤝 Contributing

PRs are welcome. For major changes, open an issue first to discuss what you'd like to change.

```bash
# Fork it → clone your fork → create a branch
git checkout -b feature/your-feature-name

# Make your changes, then
git commit -m "feat: describe what you did"
git push origin feature/your-feature-name

# Open a PR on GitHub
```

Please make sure any new agent follows the existing `BaseAgent` interface pattern in `agents/`.

<br>

---

<br>

## 📜 License

MIT — do whatever you want, just don't claim you built it from scratch if you didn't.

<br>

---

<br>

<div align="center">

```
  built late at night, fueled by chai and a deadline that was yesterday
  — the kind of tool you write because nothing else does what you need
```

**⭐ If this saved your pitch — star it. Someone else needs to find it too.**

</div>
