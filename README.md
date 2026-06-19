# NCLEX-RN Exam Preparation Platform

A structured, documentation-first curriculum for nursing students preparing for the NCLEX-RN licensing exam.

## What this is

40 sessions split across 10 modules, progressing from infection control through specialty nursing domains to a capstone review. Every session has a pre-quiz, concept explanation, study session, commit checkpoint, and post-quiz. You must score 80% on quizzes to advance.

## Curriculum Modules

| Module | Topic | Sessions |
|--------|-------|----------|
| 1 | Infection Control & Safety | 01 – 04 |
| 2 | Emergency Response | 05 – 08 |
| 3 | Pharmacology | 09 – 12 |
| 4 | Patient Prioritization | 13 – 16 |
| 5 | Cardiovascular System | 17 – 20 |
| 6 | Respiratory System | 21 – 24 |
| 7 | Diabetes / Endocrine | 25 – 28 |
| 8 | Pediatrics | 29 – 32 |
| 9 | Pregnancy / Maternity | 33 – 36 |
| 10 | Mental Health / Psychiatric Nursing | 37 – 40 |

## Docs

All curriculum documentation lives in `/docs/` as static HTML. Serve it locally:

```bash
python -m http.server 6971 --directory docs
```

Then open `http://localhost:6971`.

## Tech Stack

- **Framework:** React via Vite (later modules)
- **Package manager:** npm
- **Language:** Plain JavaScript (no TypeScript)
- **Styling:** Plain CSS
- **Testing:** Vitest + React Testing Library (later modules)

## Architecture Source

This project is a domain migration of [react-learn-with-ai](../react-learn-with-ai). Same folder structure, session flow, quiz engine, and progression logic. Only the educational content changed.

## Rules

1. Never skip a session
2. One session = one commit
3. Assess before intervening — nursing process always
4. Score below 80% on a quiz = repeat the session
