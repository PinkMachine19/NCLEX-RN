#!/usr/bin/env python3
"""Generate TikTok-style NCLEX quizzes — same format as sql-quiz."""

import json
import re
import shutil
from pathlib import Path

ROOT = Path(r"D:\repos\source\NCLEX-RN")
OUT = ROOT / "tik-tok quizes"
UPLOADS = Path(r"D:\apps\uploads")
UPLOADS_QUIZZES = UPLOADS / "nclex-rn-tik-tok-quizes"
TEMPLATE = Path(r"D:\repos\source\sql-quiz\sql-fundamentals-quiz-4.html")
THEME_CSS = Path(__file__).parent / "nclex_tiktok_theme.css"

WATERMARK_SVG_TEMPLATE = """
<svg class="watermark" viewBox="0 0 500 500">

<defs>
<linearGradient id="{grad_id}">
<stop offset="0%" stop-color="#3a86ff"/>
<stop offset="100%" stop-color="#2ec4b6"/>
</linearGradient>
</defs>

<circle cx="250" cy="250" r="190" fill="url(#{grad_id})" opacity=".10"/>

<rect x="155" y="120" width="190" height="260"
rx="28"
fill="none"
stroke="url(#{grad_id})"
stroke-width="18"
opacity=".55"/>

<rect x="205" y="92"
width="90"
height="54"
rx="20"
fill="#07111f"
stroke="url(#{grad_id})"
stroke-width="14"/>

<path d="M185 325 L225 360 L315 270"
fill="none"
stroke="#2ec4b6"
stroke-width="22"
stroke-linecap="round"/>

<text x="250"
y="430"
text-anchor="middle"
font-size="42"
font-weight="800"
fill="#7db7ff"
opacity=".45">
NCLEX
</text>

</svg>
"""


def watermark_block(uid="intro"):
    grad_id = f"grad-{uid}"
    svg = WATERMARK_SVG_TEMPLATE.format(grad_id=grad_id)
    return f'<div class="watermark-wrap" aria-hidden="true">{svg}</div>'

QUIZZES = [
    {
        "quizNumber": 1,
        "sessionNumber": 1,
        "file": "nclex-infection-control-quiz-1.html",
        "title": "NCLEX Quiz #1 — Standard Precautions",
        "introTagline": "Think you know infection control?",
        "introHook": "Take a breath — answer before the timer ends.",
        "introBottom": "Scrub in smart",
        "resultsHeadline": "How ready are you for NCLEX?",
        "resultsSub": "Module 1: Infection Control & Safety",
        "scoreTiers": [
            ("0–1", "NCLEX Rookie"),
            ("2–3", "Student Nurse"),
            ("4–5", "Safety Pro"),
        ],
        "hashtags": "#NCLEX #NCLEXRN #Nursing #NurseLife #InfectionControl",
        "resultsBottom": "Protect every patient",
        "questions": [
            {
                "question": "When should hand hygiene be performed according to standard precautions?",
                "choices": [
                    "A) Only after contact with body fluids",
                    "B) Before and after every patient contact",
                    "C) Only at the start of the shift",
                    "D) Only when gloves are not available",
                ],
                "correct": "B",
                "answer": "Hand hygiene is required before and after every patient contact — even when gloves are worn.",
            },
            {
                "question": "A patient has confirmed MRSA wound infection. Which isolation precaution is required?",
                "choices": [
                    "A) Airborne",
                    "B) Droplet",
                    "C) Contact",
                    "D) Protective",
                ],
                "correct": "C",
                "answer": "MRSA spreads by direct contact. Gown and gloves are required for all room entry.",
            },
            {
                "question": "Which action breaks the chain of infection at the portal of entry?",
                "choices": [
                    "A) Administering antibiotics",
                    "B) Proper wound dressing and aseptic technique",
                    "C) Isolating the reservoir",
                    "D) Vaccination",
                ],
                "correct": "B",
                "answer": "Aseptic technique blocks pathogens from entering through broken skin or mucous membranes.",
            },
            {
                "question": "A nurse removes gloves after wound care but skips hand hygiene before leaving the room. What is the primary risk?",
                "choices": [
                    "A) Glove allergy",
                    "B) Cross-contamination to other patients and surfaces",
                    "C) Needlestick injury",
                    "D) Medication error",
                ],
                "correct": "B",
                "answer": "Organisms on glove surfaces transfer to hands and the environment without hand hygiene.",
            },
            {
                "question": "Standard precautions apply to:",
                "choices": [
                    "A) Only patients with known infections",
                    "B) All patients regardless of diagnosis",
                    "C) Only immunocompromised patients",
                    "D) Only patients in isolation",
                ],
                "correct": "B",
                "answer": "Standard precautions treat all blood, body fluids, and mucous membranes as potentially infectious.",
            },
        ],
    },
    {
        "quizNumber": 2,
        "sessionNumber": 2,
        "file": "nclex-infection-control-quiz-2.html",
        "title": "NCLEX Quiz #2 — Transmission-Based Precautions",
        "introTagline": "Know your isolation types?",
        "introHook": "Take a breath — answer before the timer ends.",
        "introBottom": "Isolate with confidence",
        "resultsHeadline": "Transmission precautions score",
        "resultsSub": "Contact · Droplet · Airborne",
        "scoreTiers": [
            ("0–1", "Isolation Confused"),
            ("2–3", "Precaution Aware"),
            ("4–5", "Isolation Expert"),
        ],
        "hashtags": "#NCLEX #NCLEXRN #Nursing #InfectionControl #StudyNursing",
        "resultsBottom": "Match precaution to pathogen",
        "questions": [
            {
                "question": "A patient with active tuberculosis requires which type of isolation?",
                "choices": [
                    "A) Contact",
                    "B) Droplet",
                    "C) Airborne",
                    "D) Standard only",
                ],
                "correct": "C",
                "answer": "TB spreads via airborne droplet nuclei. Negative-pressure room and N95 respirator required.",
            },
            {
                "question": "Contact precautions require which PPE for room entry?",
                "choices": [
                    "A) N95 respirator only",
                    "B) Gown and gloves",
                    "C) Surgical mask only",
                    "D) Face shield only",
                ],
                "correct": "B",
                "answer": "Contact precautions require gown and gloves for all room entry.",
            },
            {
                "question": "Droplet precautions are indicated for influenza. Which mask is appropriate?",
                "choices": [
                    "A) N95 respirator",
                    "B) Surgical mask within 3–6 feet",
                    "C) No mask needed",
                    "D) PAPR only",
                ],
                "correct": "B",
                "answer": "Droplet precautions use a surgical mask within 3–6 feet. N95 is for airborne pathogens.",
            },
            {
                "question": "A patient on contact precautions leaves the room for imaging. The nurse should:",
                "choices": [
                    "A) No special precautions needed",
                    "B) Cover infected sites and notify transport staff",
                    "C) Cancel the test",
                    "D) Remove the isolation order",
                ],
                "correct": "B",
                "answer": "Infected or draining sites must be covered; transport must follow precautions during transit.",
            },
            {
                "question": "Which patient requires the most restrictive isolation?",
                "choices": [
                    "A) Influenza",
                    "B) MRSA colonization",
                    "C) Active measles",
                    "D) C. difficile",
                ],
                "correct": "C",
                "answer": "Measles is airborne — negative-pressure room and N95. Influenza is droplet; MRSA and C. diff are contact.",
            },
        ],
    },
    {
        "quizNumber": 3,
        "sessionNumber": 3,
        "file": "nclex-infection-control-quiz-3.html",
        "title": "NCLEX Quiz #3 — PPE & Donning/Doffing",
        "introTagline": "PPE sequence matters.",
        "introHook": "Take a breath — answer before the timer ends.",
        "introBottom": "Don and doff safely",
        "resultsHeadline": "PPE mastery check",
        "resultsSub": "Protect yourself first",
        "scoreTiers": [
            ("0–1", "PPE Beginner"),
            ("2–3", "Gown & Glove Ready"),
            ("4–5", "PPE Pro"),
        ],
        "hashtags": "#NCLEX #NCLEXRN #Nursing #PPE #PatientSafety",
        "resultsBottom": "Sequence saves lives",
        "questions": [
            {
                "question": "What is the correct order for donning PPE?",
                "choices": [
                    "A) Gloves → Gown → Mask → Eye protection",
                    "B) Gown → Mask/Eye protection → Gloves",
                    "C) Mask → Gloves → Gown",
                    "D) Eye protection → Gloves → Gown",
                ],
                "correct": "B",
                "answer": "Don gown first, then mask/eye protection, then gloves — gloves go on last.",
            },
            {
                "question": "When doffing PPE, which item should be removed FIRST?",
                "choices": [
                    "A) Gloves",
                    "B) Gown",
                    "C) Mask",
                    "D) Eye protection",
                ],
                "correct": "A",
                "answer": "Gloves are removed first during doffing to minimize contamination of hands and clothing.",
            },
            {
                "question": "An N95 respirator is required for which scenario?",
                "choices": [
                    "A) C. difficile contact precautions",
                    "B) Influenza droplet precautions",
                    "C) Airborne isolation for varicella",
                    "D) Standard precautions only",
                ],
                "correct": "C",
                "answer": "Varicella (chickenpox) requires airborne precautions with N95 or higher-level respirator.",
            },
            {
                "question": "After doffing all PPE, the nurse's next action is:",
                "choices": [
                    "A) Document in the chart",
                    "B) Perform hand hygiene",
                    "C) Re-don gloves immediately",
                    "D) Leave the room without washing",
                ],
                "correct": "B",
                "answer": "Hand hygiene is always performed immediately after removing PPE, before any other action.",
            },
            {
                "question": "Which PPE error most increases self-contamination risk during doffing?",
                "choices": [
                    "A) Removing gloves before gown",
                    "B) Rolling gown away from body while removing",
                    "C) Touching the outside of the mask while removing",
                    "D) Performing hand hygiene after doffing",
                ],
                "correct": "C",
                "answer": "Touching the contaminated outer surface of the mask during removal spreads organisms to hands.",
            },
        ],
    },
    {
        "quizNumber": 4,
        "sessionNumber": 4,
        "file": "nclex-infection-control-quiz-4.html",
        "title": "NCLEX Quiz #4 — Module 1 Gate Review",
        "introTagline": "Module 1 gate — pass or repeat.",
        "introHook": "Take a breath — answer before the timer ends.",
        "introBottom": "Gate quiz time",
        "resultsHeadline": "Module 1 gate result",
        "resultsSub": "Need 4/5 to unlock Module 2",
        "scoreTiers": [
            ("0–1", "Repeat Module 1"),
            ("2–3", "Almost There"),
            ("4–5", "Module 2 Unlocked"),
        ],
        "hashtags": "#NCLEX #NCLEXRN #Nursing #StudyNursing #FutureRN",
        "resultsBottom": "Safety first, always",
        "questions": [
            {
                "question": "A nurse enters an isolation room without checking the precaution sign. What is the priority nursing action?",
                "choices": [
                    "A) Proceed — standard precautions cover everything",
                    "B) Exit, verify precaution type, don appropriate PPE, re-enter",
                    "C) Ask the patient what illness they have",
                    "D) Call the physician for orders",
                ],
                "correct": "B",
                "answer": "Always verify isolation type on the door sign and don correct PPE before patient contact.",
            },
            {
                "question": "Which patient should the nurse see FIRST?",
                "choices": [
                    "A) Stable post-op patient requesting pain medication",
                    "B) Patient with new onset shortness of breath and SpO2 88%",
                    "C) Patient due for routine morning medications",
                    "D) Patient requesting discharge teaching",
                ],
                "correct": "B",
                "answer": "Airway and breathing problems take priority — SpO2 88% with dyspnea is the most acute.",
            },
            {
                "question": "A used needle is found in the bed linens. The nurse should:",
                "choices": [
                    "A) Dispose in regular trash",
                    "B) Recap the needle and discard in sharps container",
                    "C) Use tongs/forceps to place in sharps container without recapping",
                    "D) Leave it for environmental services",
                ],
                "correct": "C",
                "answer": "Never recap needles. Use mechanical device or forceps to place directly in sharps container.",
            },
            {
                "question": "Standard precautions include treating which substances as potentially infectious?",
                "choices": [
                    "A) Blood and body fluids only",
                    "B) All body fluids except sweat",
                    "C) Blood, all body fluids, mucous membranes, and non-intact skin",
                    "D) Only visible blood",
                ],
                "correct": "C",
                "answer": "Standard precautions apply to blood, all body fluids, mucous membranes, and non-intact skin.",
            },
            {
                "question": "A student nurse asks why hand hygiene matters when wearing gloves. The best response is:",
                "choices": [
                    "A) Gloves make hand hygiene unnecessary",
                    "B) Gloves can have micro-tears; hand hygiene protects before and after glove use",
                    "C) Hand hygiene is only for the nurse's comfort",
                    "D) Hand hygiene replaces PPE entirely",
                ],
                "correct": "B",
                "answer": "Gloves are not perfect barriers. Hand hygiene before donning and after removing gloves prevents cross-contamination.",
            },
        ],
    },
    {
        "quizNumber": 5,
        "sessionNumber": 5,
        "moduleNum": 2,
        "moduleName": "Emergency Response",
        "file": "nclex-emergency-response-quiz-5.html",
        "title": "NCLEX Quiz #5 — ABCs & Primary Survey",
        "introTagline": "Airway before everything else.",
        "introHook": "Take a breath — answer before the timer ends.",
        "introBottom": "Assess first",
        "resultsHeadline": "Primary survey score",
        "resultsSub": "Module 2: Emergency Response · Session 05",
        "scoreTiers": [
            ("0–1", "Code Blue Confused"),
            ("2–3", "Rapid Response Ready"),
            ("4–5", "ABC Pro"),
        ],
        "hashtags": "#NCLEX #NCLEXRN #Nursing #EmergencyNursing #FutureRN",
        "resultsBottom": "ABCs save lives",
        "questions": [
            {
                "question": "During the primary survey, what is assessed FIRST?",
                "choices": [
                    "A) Circulation",
                    "B) Airway",
                    "C) Disability",
                    "D) Exposure",
                ],
                "correct": "B",
                "answer": "The primary survey follows ABCDE — Airway is always first because without a patent airway, breathing and circulation cannot be sustained.",
            },
            {
                "question": "An unresponsive patient is found. After checking responsiveness and calling for help, the nurse's NEXT priority is:",
                "choices": [
                    "A) Start IV fluids",
                    "B) Open the airway and assess breathing",
                    "C) Complete the secondary survey",
                    "D) Obtain consent from family",
                ],
                "correct": "B",
                "answer": "After activating the emergency response, open the airway and assess breathing — do not delay ABCs for IV access or detailed assessment.",
            },
            {
                "question": "A trauma patient has absent breath sounds on one side, tracheal deviation, and distended neck veins. Priority action?",
                "choices": [
                    "A) Order a chest X-ray and wait",
                    "B) Prepare for needle decompression of tension pneumothorax",
                    "C) Administer morphine for pain",
                    "D) Place the patient in Trendelenburg position",
                ],
                "correct": "B",
                "answer": "These are classic signs of tension pneumothorax — a life-threatening breathing problem requiring immediate decompression.",
            },
            {
                "question": "The primary survey differs from the secondary survey because the primary survey:",
                "choices": [
                    "A) Is completed hours after arrival",
                    "B) Identifies and treats life-threatening problems immediately",
                    "C) Replaces all diagnostic testing",
                    "D) Is performed only by physicians",
                ],
                "correct": "B",
                "answer": "Primary survey finds what kills first. Secondary survey is a head-to-toe evaluation after immediate threats are addressed.",
            },
            {
                "question": "Which finding requires IMMEDIATE airway intervention?",
                "choices": [
                    "A) SpO2 96% on room air",
                    "B) Gurgling respirations with an ineffective cough",
                    "C) Blood pressure 118/72 mmHg",
                    "D) Small laceration on the forearm",
                ],
                "correct": "B",
                "answer": "Gurgling with ineffective cough signals airway obstruction or inability to clear secretions — suction and airway support come first.",
            },
        ],
    },
]


PINCH_ZOOM_SCRIPT = """
<script>
(function(){
  var MIN = 0.65;
  var MAX = 1.85;
  var scale = 1;
  var startDist = 0;
  var startScale = 1;
  var pinching = false;

  function distance(a, b){
    return Math.hypot(a.clientX - b.clientX, a.clientY - b.clientY);
  }

  function applyScale(){
    document.querySelectorAll(".quiz-card").forEach(function(el){
      el.style.transform = "scale(" + scale + ")";
    });
  }

  function relocateTimers(){
    document.querySelectorAll(".quiz-slide").forEach(function(slide){
      var timer = slide.querySelector(".quiz-timer");
      var slot = slide.querySelector(".timer-slot");
      if(timer && slot && timer.parentElement !== slot){
        slot.appendChild(timer);
      }
    });
  }

  function onTouchStart(e){
    if(e.touches.length !== 2) return;
    pinching = true;
    startDist = distance(e.touches[0], e.touches[1]);
    startScale = scale;
  }

  function onTouchMove(e){
    if(!pinching || e.touches.length !== 2) return;
    var next = startScale * (distance(e.touches[0], e.touches[1]) / startDist);
    scale = Math.min(MAX, Math.max(MIN, next));
    applyScale();
    e.preventDefault();
  }

  function onTouchEnd(e){
    if(e.touches.length < 2) pinching = false;
  }

  document.querySelectorAll(".safe-content").forEach(function(zone){
    zone.addEventListener("touchstart", onTouchStart, {passive: true});
    zone.addEventListener("touchmove", onTouchMove, {passive: false});
    zone.addEventListener("touchend", onTouchEnd, {passive: true});
    zone.addEventListener("touchcancel", onTouchEnd, {passive: true});
  });

  relocateTimers();
  var observer = new MutationObserver(relocateTimers);
  document.querySelectorAll(".quiz-slide .safe-frame").forEach(function(frame){
    observer.observe(frame, {childList: true, subtree: true});
  });
})();
</script>
"""


def load_template_parts():
    theme = THEME_CSS.read_text(encoding="utf-8")
    style = f"<style>\n{theme}\n</style>"
    text = TEMPLATE.read_text(encoding="utf-8")
    script_match = re.search(r"(<script>.*?</script>)", text, re.DOTALL)
    if not script_match:
        raise RuntimeError("Could not parse quiz script from template")
    script = script_match.group(1)
    return style, script


def format_choice(text):
    """A) foo -> A. foo to match TikTok mockup labels."""
    if len(text) >= 2 and text[1] == ")":
        return f"{text[0]}. {text[3:].lstrip()}"
    return text


def render_question_slide(q, index, total):
    choices_html = "\n".join(
        f"          <li>{format_choice(c)}</li>" for c in q["choices"]
    )
    return f"""
<section class="slide quiz-slide">
  <div class="safe-frame">
    <div class="safe-content">
      <div class="quiz-card">
        {watermark_block(f"q{index}")}
        <div class="card-topbar">
          <div class="slide-num">Q {index}/{total}</div>
          <div class="timer-slot"></div>
        </div>
        <div class="slide-main">
          <div class="big">{q['question']}</div>
          <ul>
{choices_html}
          </ul>
          <div class="reveal-text">{q['answer']}</div>
        </div>
      </div>
    </div>
  </div>
</section>"""


def render_quiz(quiz, style, script):
    questions = quiz["questions"]
    total = len(questions)
    correct_prefixes = [f"{q['correct']}." for q in questions]

    question_slides = "\n".join(
        render_question_slide(q, i + 1, total) for i, q in enumerate(questions)
    )

    score_rows = "\n".join(
        f'          <div class="score-row"><span class="score-range">{r}</span><span class="score-name">{n}</span></div>'
        for r, n in quiz["scoreTiers"]
    )

    slides = f"""
<section class="slide intro-slide">
  <div class="safe-frame">
    <div class="safe-content">
      <div class="quiz-card">
        {watermark_block("intro")}
        <div class="slide-main">
          <h1>{quiz['title']}</h1>
          <div class="big">{quiz['introTagline']}</div>
          <p class="intro-hook">{quiz['introHook']}</p>
          <div class="intro-countdown" aria-live="polite">
            <span class="intro-countdown-text"></span>
          </div>
        </div>
      </div>
    </div>
    <div class="bottom">{quiz['introBottom']}</div>
  </div>
</section>
{question_slides}
<section class="slide results-slide">
  <div class="safe-frame">
    <div class="safe-content">
      <div class="quiz-card">
        {watermark_block("results")}
        <div class="slide-main">
        <h1>Your score</h1>
        <div class="big">{quiz['resultsHeadline']}</div>
        <div class="score-legend" aria-label="Score guide">
          <div class="score-legend-heading">Score guide</div>
{score_rows}
        </div>
        <p class="results-cta">{quiz['resultsSub']}</p>
        <p class="results-hashtags">{quiz['hashtags']}</p>
        </div>
      </div>
    </div>
    <div class="bottom">{quiz['resultsBottom']}</div>
  </div>
</section>
"""

    patched_script = re.sub(
        r"const correctPrefixes = \[[\s\S]*?\];",
        "const correctPrefixes = [\n    "
        + ",\n    ".join(f'"{p}"' for p in correct_prefixes)
        + "\n  ];",
        script,
        count=1,
    )

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
<title>{quiz['title']}</title>
{style}
</head>
<body>

<div id="start-overlay" role="button" aria-label="Tap to start quiz">
  <div class="overlay-content">
    <div class="overlay-title">Begin</div>
    <div class="overlay-subtitle">Tap to start</div>
  </div>
</div>

<div class="slide-container">
{slides}
</div>

{patched_script}

{PINCH_ZOOM_SCRIPT}

</body>
</html>
"""


def build_question_bank():
    global_num = 1
    bank_quizzes = []
    master_quizzes = []

    for quiz in QUIZZES:
        bank_questions = []
        master_questions = []
        for i, q in enumerate(quiz["questions"], 1):
            bank_questions.append({
                "globalQuestionNumber": global_num,
                "questionNumberInQuiz": i,
                "sessionNumber": quiz["sessionNumber"],
                "question": q["question"],
                "choices": q["choices"],
                "correctAnswer": q["correct"],
                "correctAnswerText": next(
                    (c for c in q["choices"] if c.startswith(q["correct"] + ")")),
                    q["choices"][0],
                ),
                "answer": q["answer"],
            })
            master_questions.append({
                "globalQuestionNumber": global_num,
                "question": q["question"],
                "answer": q["answer"],
            })
            global_num += 1

        bank_quizzes.append({
            "quizNumber": quiz["quizNumber"],
            "sessionNumber": quiz["sessionNumber"],
            "name": quiz["title"],
            "file": quiz["file"],
            "questionCount": len(quiz["questions"]),
            "questions": bank_questions,
        })
        master_quizzes.append({
            "quizNumber": quiz["quizNumber"],
            "title": quiz["title"],
            "questionCount": len(quiz["questions"]),
            "questions": master_questions,
        })

    bank = {
        "title": "NCLEX-RN TikTok Question Bank",
        "totalQuestions": global_num - 1,
        "totalQuizzes": len(QUIZZES),
        "modules": sorted({q.get("moduleName", "Infection Control & Safety") for q in QUIZZES}),
        "quizzes": bank_quizzes,
    }
    master = {
        "name": "NCLEX-RN TikTok Quiz Master Index",
        "totalQuestions": global_num - 1,
        "totalQuizzes": len(QUIZZES),
        "quizzes": master_quizzes,
    }
    return bank, master


def render_index():
    sections = {}
    for q in QUIZZES:
        mod = q.get("moduleName") or "Infection Control & Safety"
        sections.setdefault(mod, []).append(q)

    body = ""
    for mod_name, quizzes in sections.items():
        rows = ""
        for q in quizzes:
            rows += f"""
      <a class="quiz-card" href="{q['file']}">
        <div class="quiz-num">Quiz {q['quizNumber']}</div>
        <div class="quiz-title">{q['title']}</div>
        <div class="quiz-meta">Session {q['sessionNumber']:02d} · 5 questions · auto-play</div>
      </a>"""
        body += f"""
  <h2 class="module-title">{mod_name}</h2>
  <div class="grid">{rows}
  </div>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=5.0, user-scalable=yes">
<title>NCLEX TikTok Quizzes</title>
<style>
*{{box-sizing:border-box;margin:0;padding:0;}}
body{{
  font-family:-apple-system,BlinkMacSystemFont,'Segoe UI',sans-serif;
  background:#050b14;color:#e5edf7;padding:20px 16px 40px;
}}
.content{{max-width:640px;margin:0 auto;}}
h1{{font-size:24px;font-weight:800;margin-bottom:4px;color:#fff;}}
.subtitle{{color:#a8b5c8;font-size:15px;margin-bottom:20px;}}
.module-title{{font-size:16px;font-weight:800;color:#7db7ff;margin:24px 0 12px;}}
.grid{{display:flex;flex-direction:column;gap:10px;}}
.quiz-card{{
  display:block;text-decoration:none;color:inherit;
  background:#111d32;border:1px solid #243650;border-radius:18px;
  padding:18px;
}}
.quiz-num{{font-size:12px;font-weight:700;color:#3a86ff;margin-bottom:4px;}}
.quiz-title{{font-size:17px;font-weight:700;color:#fff;}}
.quiz-meta{{font-size:14px;color:#a8b5c8;margin-top:4px;}}
a.back{{display:inline-block;margin-bottom:16px;color:#3a86ff;font-weight:600;font-size:14px;text-decoration:none;}}
</style>
</head>
<body>
<div class="content">
  <a class="back" href="/nclex-rn/index.html">← Back to NCLEX-RN</a>
  <h1>NCLEX TikTok Quizzes</h1>
  <p class="subtitle">{len(QUIZZES)} auto-play carousel quizzes · swipe · timer · ding</p>{body}
</div>
</body>
</html>
"""


def main():
    OUT.mkdir(parents=True, exist_ok=True)
    style, script = load_template_parts()

    for quiz in QUIZZES:
        html = render_quiz(quiz, style, script)
        (OUT / quiz["file"]).write_text(html, encoding="utf-8")
        print(f"  wrote {quiz['file']}")

    bank, master = build_question_bank()
    (OUT / "nclex-question-bank.json").write_text(
        json.dumps(bank, indent=2), encoding="utf-8"
    )
    (OUT / "nclex-quiz-master-index.json").write_text(
        json.dumps(master, indent=2), encoding="utf-8"
    )
    (OUT / "index.html").write_text(render_index(), encoding="utf-8")
    print(f"Generated {len(QUIZZES)} TikTok quizzes in {OUT}")
    deploy_to_uploads()


def deploy_to_uploads():
    if not UPLOADS.is_dir():
        print(f"  skip deploy — uploads not found: {UPLOADS}")
        return
    if UPLOADS_QUIZZES.exists():
        shutil.rmtree(UPLOADS_QUIZZES)
    shutil.copytree(OUT, UPLOADS_QUIZZES)
    for q in QUIZZES:
        shutil.copy2(OUT / q["file"], UPLOADS / q["file"])
    print(f"  deployed quizzes -> {UPLOADS_QUIZZES}")
    print(f"  browse: http://localhost:6970/nclex-rn-tik-tok-quizes/")


if __name__ == "__main__":
    main()
