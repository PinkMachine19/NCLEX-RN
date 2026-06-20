#!/usr/bin/env python3
"""Generate NCLEX-RN project docs — mirrors react-learn-with-ai architecture."""

import os
import sys
from pathlib import Path

_SCRIPTS = Path(__file__).resolve().parent
if str(_SCRIPTS) not in sys.path:
    sys.path.insert(0, str(_SCRIPTS))
from hydrated_module1 import HYDRATED_CONCEPT, HYDRATED_STEPS, STUDY_FILE_CONTENT

ROOT = Path(r"D:\repos\source\NCLEX-RN")

BRAND = "🩺 NCLEX-RN Prep"
TITLE = "NCLEX-RN Exam Preparation Platform"

MODULES = [
    {
        "num": 1,
        "name": "Infection Control & Safety",
        "sessions": [
            (1, "Standard Precautions & Hand Hygiene", "Hand hygiene timing, standard precautions, chain of infection", "Document one patient case with infection risk factors"),
            (2, "Transmission-Based Precautions", "Contact, droplet, airborne isolation; room requirements", "Classify 3 patients by required isolation type"),
            (3, "PPE Selection & Donning/Doffing", "PPE sequence, exposure risk, doffing to prevent self-contamination", "Write PPE checklist for MRSA contact precautions"),
            (4, "Module 1 Gate — Infection Control Integration", "Integrate precautions across scenarios; safety checkpoints", "Complete infection control case study with commit checkpoint"),
        ],
    },
    {
        "num": 2,
        "name": "Emergency Response",
        "sessions": [
            (5, "ABCs & Primary Survey", "Airway, breathing, circulation; primary vs secondary survey", "Document primary survey findings for trauma patient"),
            (6, "Cardiac Arrest & BLS/ACLS Basics", "CPR ratios, defibrillation, code team roles", "Build cardiac arrest response checklist object"),
            (7, "Shock, Anaphylaxis & Rapid Response", "Shock types, epinephrine, rapid response criteria", "Map shock signs to nursing interventions"),
            (8, "Module 2 Gate — Emergency Response Scenarios", "Multi-emergency prioritization; team communication", "Complete emergency scenario case study"),
        ],
    },
    {
        "num": 3,
        "name": "Pharmacology",
        "sessions": [
            (9, "Medication Rights & Safe Administration", "6 rights, verification, documentation", "Create medication administration safety checklist"),
            (10, "High-Alert Medications", "Insulin, heparin, opioids, electrolytes; double-check rules", "Document high-alert med safety protocols"),
            (11, "Antidotes & Adverse Drug Reactions", "Common antidotes, anaphylaxis, toxicity signs", "Match drugs to antidotes and monitoring"),
            (12, "Module 3 Gate — Pharmacology Application", "Calculation review, safe dosing scenarios", "Complete pharmacology case study"),
        ],
    },
    {
        "num": 4,
        "name": "Patient Prioritization",
        "sessions": [
            (13, "NCLEX Prioritization Framework", "ABCs, Maslow, nursing process, acute vs stable", "Rank 5 patients using prioritization framework"),
            (14, "Delegation & Scope of Practice", "RN vs LPN vs UAP tasks; supervision requirements", "Assign tasks to appropriate care team members"),
            (15, "Triage & Multiple Patient Scenarios", "Disaster triage tags, simultaneous demands", "Triage 6 patients in ED waiting room"),
            (16, "Module 4 Gate — Prioritization Master Review", "Complex multi-system prioritization", "Complete prioritization capstone scenario"),
        ],
    },
    {
        "num": 5,
        "name": "Cardiovascular System",
        "sessions": [
            (17, "Heart Failure & Hypertension", "Left vs right HF, daily weights, fluid restriction", "Document HF patient assessment data object"),
            (18, "ACS, MI & Cardiac Monitoring", "STEMI vs NSTEMI, troponin, MONA-B", "Build MI patient monitoring checklist"),
            (19, "Dysrhythmias & ECG Basics", "A-fib, V-tach, heart blocks; intervention priorities", "Match dysrhythmias to immediate actions"),
            (20, "Module 5 Gate — Cardiovascular Integration", "Multi-cardiac scenario integration", "Complete cardiovascular case study"),
        ],
    },
    {
        "num": 6,
        "name": "Respiratory System",
        "sessions": [
            (21, "Asthma, COPD & Oxygen Therapy", "SpO2 targets, bronchodilators, O2 delivery devices", "Document respiratory patient with O2 orders"),
            (22, "Pneumonia & Ventilator Basics", "VAP prevention, suctioning, ABG interpretation intro", "Build ventilator patient care checklist"),
            (23, "Pulmonary Embolism & Respiratory Failure", "PE signs, anticoagulation, intubation indicators", "Map respiratory decline to nursing actions"),
            (24, "Module 6 Gate — Respiratory Integration", "Combined respiratory emergencies", "Complete respiratory case study"),
        ],
    },
    {
        "num": 7,
        "name": "Diabetes / Endocrine",
        "sessions": [
            (25, "Type 1 & Type 2 Diabetes Management", "Insulin types, oral agents, sick-day rules", "Document diabetic patient care plan object"),
            (26, "Hypoglycemia & Hyperglycemic Emergencies", "DKA, HHS, glucagon, insulin drip monitoring", "Build hypoglycemia response protocol"),
            (27, "Thyroid & Adrenal Disorders", "Hypo/hyperthyroid, Addison's, Cushing's signs", "Match endocrine disorders to nursing care"),
            (28, "Module 7 Gate — Endocrine Integration", "Multi-endocrine scenario review", "Complete endocrine case study"),
        ],
    },
    {
        "num": 8,
        "name": "Pediatrics",
        "sessions": [
            (29, "Growth & Development Milestones", "Erikson, Piaget, age-appropriate care", "Document pediatric milestone assessment"),
            (30, "Pediatric Immunizations & Common Illnesses", "Vaccine schedule, croup, RSV, dehydration", "Build pediatric illness triage guide"),
            (31, "Pediatric Medication Calculation & Safety", "Weight-based dosing, mg/kg, safe ranges", "Calculate and verify pediatric medication dose"),
            (32, "Module 8 Gate — Pediatrics Integration", "Pediatric prioritization scenarios", "Complete pediatric case study"),
        ],
    },
    {
        "num": 9,
        "name": "Pregnancy / Maternity",
        "sessions": [
            (33, "Prenatal Assessment & Complications", "Fundal height, preeclampsia, gestational diabetes", "Document prenatal patient assessment"),
            (34, "Labor, Delivery & Fetal Monitoring", "FHR patterns, stages of labor, decelerations", "Build labor monitoring checklist"),
            (35, "Postpartum & Newborn Care", "Lochia, breastfeeding, APGAR, thermoregulation", "Document postpartum/newborn care plan"),
            (36, "Module 9 Gate — Maternity Integration", "Obstetric emergency scenarios", "Complete maternity case study"),
        ],
    },
    {
        "num": 10,
        "name": "Mental Health / Psychiatric Nursing",
        "sessions": [
            (37, "Therapeutic Communication & Crisis Intervention", "Active listening, de-escalation, boundaries", "Document therapeutic communication scenarios"),
            (38, "Mood Disorders & Psychiatric Medications", "Depression, bipolar, SSRIs, lithium monitoring", "Build psychiatric med monitoring guide"),
            (39, "Substance Use & Behavioral Health", "Withdrawal, MAT, safety, nonjudgmental care", "Map withdrawal syndromes to nursing care"),
            (40, "Capstone — Full NCLEX-RN Readiness Review", "Cross-module integration; exam readiness", "Complete final capstone case study"),
        ],
    },
]

# Quiz bank per session — (question, options as list of (val, text), answer, explanation)
QUIZ_DATA = {
    1: [
        ("When should hand hygiene be performed according to standard precautions?",
         [("a", "Only after contact with body fluids"), ("b", "Before and after every patient contact"), ("c", "Only at the start of the shift"), ("d", "Only when gloves are not available")],
         "b", "Standard precautions require hand hygiene before and after every patient contact, even when gloves are worn."),
        ("A patient has confirmed MRSA wound infection. Which isolation precaution is required?",
         [("a", "Airborne"), ("b", "Droplet"), ("c", "Contact"), ("d", "Protective")],
         "c", "MRSA is spread by direct contact. Contact precautions include gown and gloves for all room entry."),
        ("Which action breaks the chain of infection at the portal of entry?",
         [("a", "Administering antibiotics"), ("b", "Proper wound dressing and aseptic technique"), ("c", "Isolating the reservoir"), ("d", "Vaccination")],
         "b", "Aseptic technique and wound care block pathogens from entering the body through broken skin or mucous membranes."),
        ("A nurse removes gloves after wound care but does not perform hand hygiene before leaving the room. What is the primary risk?",
         [("a", "Glove allergy"), ("b", "Cross-contamination to other patients and surfaces"), ("c", "Needlestick injury"), ("d", "Medication error")],
         "b", "Microorganisms on glove surfaces transfer to hands and then to the environment without hand hygiene."),
        ("Standard precautions apply to:",
         [("a", "Only patients with known infections"), ("b", "All patients regardless of diagnosis"), ("c", "Only immunocompromised patients"), ("d", "Only patients in isolation")],
         "b", "Standard precautions treat all blood, body fluids, and mucous membranes as potentially infectious."),
    ],
    2: [
        ("A patient with active tuberculosis requires which type of isolation?",
         [("a", "Contact"), ("b", "Droplet"), ("c", "Airborne"), ("d", "Standard only")],
         "c", "TB spreads via airborne droplet nuclei. Negative-pressure room and N95 respirator are required."),
        ("Contact precautions require which PPE for room entry?",
         [("a", "N95 respirator only"), ("b", "Gown and gloves"), ("c", "Surgical mask only"), ("d", "Face shield only")],
         "b", "Contact precautions require gown and gloves for all room entry to prevent spread by touch."),
        ("Droplet precautions are indicated for influenza. Which mask is appropriate?",
         [("a", "N95 respirator"), ("b", "Surgical mask within 3–6 feet"), ("c", "No mask needed"), ("d", "PAPR only")],
         "b", "Droplet precautions use a surgical mask within 3–6 feet of the patient; N95 is for airborne."),
        ("A patient on contact precautions may leave the room for a test. The nurse should:",
         [("a", "No special precautions needed"), ("b", "Ensure infected areas are covered and notify transport"), ("c", "Cancel the test"), ("d", "Remove isolation order")],
         "b", "Infected/draining sites must be covered; transport staff must follow precautions during transit."),
        ("Which patient requires the most restrictive isolation?",
         [("a", "Influenza"), ("b", "MRSA colonization"), ("c", "Active measles"), ("d", "C. difficile")],
         "c", "Measles is airborne; requires negative-pressure room and N95. Influenza is droplet; MRSA and C. diff are contact."),
    ],
    3: [
        ("What is the correct order for donning PPE?",
         [("a", "Gloves → Gown → Mask → Eye protection"), ("b", "Gown → Mask/Eye protection → Gloves"), ("c", "Mask → Gloves → Gown"), ("d", "Eye protection → Gloves → Gown")],
         "b", "Don gown first, then mask/eye protection, then gloves — gloves go on last."),
        ("When doffing PPE, which item should be removed FIRST?",
         [("a", "Gloves"), ("b", "Gown"), ("c", "Mask"), ("d", "Eye protection")],
         "a", "Gloves are removed first during doffing to minimize contamination of hands and clothing."),
        ("An N95 respirator is required for which scenario?",
         [("a", "C. difficile contact precautions"), ("b", "Influenza droplet precautions"), ("c", "Airborne isolation for varicella"), ("d", "Standard precautions only")],
         "c", "Varicella (chickenpox) requires airborne precautions with N95 or higher-level respirator."),
        ("After doffing all PPE, the nurse's next action is:",
         [("a", "Document in the chart"), ("b", "Perform hand hygiene"), ("c", "Re-don gloves immediately"), ("d", "Leave the room without washing")],
         "b", "Hand hygiene is always performed immediately after removing PPE, before any other action."),
        ("Which PPE error most increases self-contamination risk during doffing?",
         [("a", "Removing gloves before gown"), ("b", "Rolling gown away from body while removing"), ("c", "Touching the outside of the mask while removing"), ("d", "Performing hand hygiene after doffing")],
         "c", "Touching the contaminated outer surface of the mask during removal spreads organisms to hands."),
    ],
    4: [
        ("A nurse enters an isolation room without checking the precaution sign. What is the priority nursing action?",
         [("a", "Proceed — standard precautions cover everything"), ("b", "Exit, verify precaution type, don appropriate PPE, re-enter"), ("c", "Ask the patient what illness they have"), ("d", "Call the physician for orders")],
         "b", "Always verify isolation type on the door sign and don correct PPE before patient contact."),
        ("Which patient should the nurse see FIRST?",
         [("a", "Stable post-op patient requesting pain medication"), ("b", "Patient with new onset shortness of breath and SpO2 88%"), ("c", "Patient due for routine morning medications"), ("d", "Patient requesting discharge teaching")],
         "b", "Airway and breathing problems take priority — SpO2 88% with dyspnea is the most acute."),
        ("A used needle is found in the bed linens. The nurse should:",
         [("a", "Dispose in regular trash"), ("b", "Recap the needle and discard in sharps container"), ("c", "Use tongs/forceps to place in sharps container without recapping"), ("d", "Leave it for environmental services")],
         "c", "Never recap needles. Use mechanical device or forceps to place directly in sharps container."),
        ("Standard precautions include treating which substances as potentially infectious?",
         [("a", "Blood and body fluids only"), ("b", "All body fluids except sweat"), ("c", "Blood, all body fluids, mucous membranes, and non-intact skin"), ("d", "Only visible blood")],
         "c", "Standard precautions apply to blood, all body fluids, mucous membranes, and non-intact skin."),
        ("A student nurse asks why hand hygiene matters when wearing gloves. The best response is:",
         [("a", "Gloves make hand hygiene unnecessary"), ("b", "Gloves can have micro-tears; hand hygiene protects before and after glove use"), ("c", "Hand hygiene is only for the nurse's comfort"), ("d", "Hand hygiene replaces PPE entirely")],
         "b", "Gloves are not perfect barriers. Hand hygiene before donning and after removing gloves prevents cross-contamination."),
    ],
}

# Default quiz generator for sessions without custom data
def default_quiz(session_num, title, module_name):
    templates = [
        (f"Regarding {title.lower()}, which nursing action demonstrates clinical reasoning rather than memorization?",
         [("a", "Selecting an intervention based solely on the diagnosis label"), ("b", "Assessing the patient first, then matching intervention to findings"), ("c", "Delegating all care without assessment"), ("d", "Waiting for the physician before any action")],
         "b", f"NCLEX tests application. Assessment before intervention is the nursing process foundation for {title}."),
        (f"A stable patient on the unit develops new findings related to {module_name.lower()}. What is the nurse's first priority?",
         [("a", "Document and continue routine care"), ("b", "Assess airway, breathing, and circulation"), ("c", "Call family"), ("d", "Prepare discharge paperwork")],
         "b", "ABCs always come first in prioritization, regardless of clinical specialty."),
        (f"When studying {title}, which approach best prepares for NCLEX-style questions?",
         [("a", "Memorizing lists without understanding rationale"), ("b", "Understanding why each intervention is chosen"), ("c", "Skipping practice questions"), ("d", "Focusing only on one answer format")],
         "b", "NCLEX rewards understanding of rationale, not rote memorization."),
        (f"In a scenario combining {module_name.lower()} knowledge, the nurse must delegate a task. Which task is appropriate for unlicensed assistive personnel (UAP)?",
         [("a", "Assessing a new symptom"), ("b", "Ambulating a stable patient per care plan"), ("c", "Teaching a new medication"), ("d", "Interpreting lab results")],
         "b", "UAP may perform routine, non-assessment tasks on stable patients per care plan. Assessment and teaching remain RN scope."),
        (f"After completing this session on {title.lower()}, a post-quiz score below 80% means:",
         [("a", "Proceed to the next session anyway"), ("b", "Repeat the session until mastery is demonstrated"), ("c", "Skip the lab portion"), ("d", "Only review the wrong answers briefly")],
         "b", "The curriculum requires ≥80% (4/5) on quizzes before advancing — same rule as the source platform."),
    ]
    return templates


def nav_links(prefix="../", active=None):
    links = [
        ("index.html", "brand", BRAND),
        ("syllabus/index.html", "Syllabus", "Syllabus"),
        ("sessions/index.html", "Sessions", "Sessions"),
        ("quizzes/index.html", "Quizzes", "Quizzes"),
        ("labs/index.html", "Labs", "Labs"),
        ("architecture/index.html", "Architecture", "Architecture"),
        ("session-notes/index.html", "Notes", "Notes"),
        ("commit-reviews/index.html", "Commits", "Commits"),
        ("prompts/index.html", "Prompts", "Prompts"),
    ]
    parts = ['<nav>\n  <div class="container">']
    for href, key, label in links:
        cls = ""
        if key == "brand":
            cls = ' class="brand"'
        elif active == key:
            cls = ' class="active"'
        parts.append(f'    <a href="{prefix}{href}"{cls}>{label}</a>')
    parts.append("  </div>\n</nav>")
    return "\n".join(parts)


SESSION_STYLES = """
    .quiz-option {
      display: block;
      background: var(--surface-2);
      border: 1px solid var(--border);
      border-radius: var(--radius);
      padding: 10px 14px;
      margin-bottom: 8px;
      cursor: pointer;
      font-size: 14px;
      transition: border-color 0.15s, background 0.15s;
      user-select: none;
    }
    .quiz-option:hover { border-color: var(--accent); background: var(--surface); }
    .quiz-option.selected { border-color: var(--accent); background: rgba(88,166,255,0.1); }
    .quiz-option.correct  { border-color: var(--green);  background: rgba(63,185,80,0.1); }
    .quiz-option.wrong    { border-color: var(--red);    background: rgba(248,81,73,0.1); }
    .quiz-question { margin-bottom: 28px; }
    .quiz-question p { font-weight: 600; margin-bottom: 10px; font-size: 15px; }
    .quiz-question .question-num { color: var(--text-muted); font-size: 12px; font-weight: 400; margin-bottom: 4px; }
    .quiz-result {
      display: none;
      padding: 16px 20px;
      border-radius: var(--radius);
      margin-top: 16px;
      font-size: 15px;
      font-weight: 600;
    }
    .quiz-result.pass { background: rgba(63,185,80,0.12); border: 1px solid var(--green); color: var(--green); }
    .quiz-result.fail { background: rgba(248,81,73,0.12); border: 1px solid var(--red);   color: var(--red); }
    .explanation {
      display: none;
      font-size: 13px;
      color: var(--text-muted);
      margin-top: 6px;
      padding: 8px 12px;
      background: var(--surface-2);
      border-radius: var(--radius);
      border-left: 2px solid var(--border);
    }
    .submit-btn {
      background: var(--accent);
      color: #0d1117;
      border: none;
      border-radius: var(--radius);
      padding: 10px 22px;
      font-size: 14px;
      font-weight: 700;
      cursor: pointer;
      margin-top: 8px;
      transition: opacity 0.15s;
    }
    .submit-btn:hover { opacity: 0.85; }
    .submit-btn:disabled { opacity: 0.4; cursor: not-allowed; }
    .step { display: flex; gap: 16px; margin-bottom: 20px; }
    .step-num {
      flex-shrink: 0; width: 28px; height: 28px; border-radius: 50%;
      background: var(--accent); color: #0d1117; font-weight: 700; font-size: 13px;
      display: flex; align-items: center; justify-content: center; margin-top: 2px;
    }
    .step-body { flex: 1; }
    .step-body p { margin-bottom: 6px; }
    .section-divider { border: none; border-top: 2px solid var(--border); margin: 40px 0; }
    .checklist-item { display: flex; align-items: flex-start; gap: 10px; margin-bottom: 10px; font-size: 14px; }
    .checklist-item input[type="checkbox"] { margin-top: 3px; width: 16px; height: 16px; accent-color: var(--accent); flex-shrink: 0; }
"""

QUIZ_SCRIPT = """
<script>
  function setupQuiz(prefix) {
    const container = document.getElementById(prefix + '-quiz');
    if (!container) return;
    const questions = container.querySelectorAll('.quiz-question');
    const btn = container.querySelector('.submit-btn');
    let answeredCount = 0;
    let correct = 0;
    questions.forEach(q => {
      q.querySelectorAll('.quiz-option').forEach(opt => {
        opt.addEventListener('click', () => {
          if (q.dataset.answered) return;
          q.dataset.answered = 'true';
          answeredCount++;
          const answer = q.dataset.answer;
          q.querySelectorAll('.quiz-option').forEach(o => {
            o.style.pointerEvents = 'none';
            if (o.dataset.val === answer) o.classList.add('correct');
          });
          if (opt.dataset.val === answer) { correct++; } else { opt.classList.add('wrong'); }
          const explanation = q.querySelector('.explanation');
          if (explanation) explanation.style.display = 'block';
          if (answeredCount === questions.length) btn.disabled = false;
        });
      });
    });
    btn.addEventListener('click', () => {
      const result = document.getElementById(prefix + '-result');
      const pct = Math.round((correct / questions.length) * 100);
      result.style.display = 'block';
      btn.disabled = true;
      if (correct >= 4) {
        result.className = 'quiz-result pass';
        result.innerHTML = correct + '/5 correct (' + pct + '%) — Passed. ' +
          (prefix === 'pre' ? 'You may proceed to the study session.' : 'Session complete. Make your commit.');
      } else {
        result.className = 'quiz-result fail';
        result.innerHTML = correct + '/5 correct (' + pct + '%) — Below 80%. ' +
          (prefix === 'pre' ? 'Read the concept section carefully, then retake.' :
           'Re-read the concept section and redo the study session before committing.');
      }
    });
  }
  setupQuiz('pre');
  setupQuiz('post');
</script>
"""


def render_quiz_block(prefix, session_num, title, module_name):
    questions = QUIZ_DATA.get(session_num) or default_quiz(session_num, title, module_name)
    parts = [f'<div id="{prefix}-quiz">']
    for i, (qtext, options, answer, explanation) in enumerate(questions):
        parts.append(f'      <div class="quiz-question" data-question="{i}" data-answer="{answer}">')
        parts.append(f'        <div class="question-num">Question {i+1} of 5</div>')
        parts.append(f'        <p>{qtext}</p>')
        for val, text in options:
            parts.append(f'        <label class="quiz-option" data-val="{val}">{text}</label>')
        parts.append(f'        <div class="explanation">{explanation}</div>')
        parts.append('      </div>')
    parts.append(f'      <button class="submit-btn" disabled>Submit {"Pre-Quiz" if prefix == "pre" else "Post-Quiz"}</button>')
    parts.append(f'      <div class="quiz-result" id="{prefix}-result"></div>')
    parts.append('    </div>')
    return "\n".join(parts)


def get_session_info(session_num):
    for mod in MODULES:
        for s in mod["sessions"]:
            if s[0] == session_num:
                return mod, s
    return None, None


def session_status(session_num):
    if session_num == 1:
        return "badge-current", "Available"
    if session_num <= 4:
        return "badge-current", "Available"
    return "badge-locked", "Locked"


def generate_session(session_num):
    mod, sess = get_session_info(session_num)
    num, title, concept, milestone = sess
    mod_num, mod_name = mod["num"], mod["name"]
    is_gate = num == mod["sessions"][-1][0]
    status_badge, status_text = session_status(session_num)
    gate_badge = "badge-gate" if is_gate else status_badge
    gate_label = "Gate" if is_gate else status_text

    lab_file = "src/patient-case.js" if session_num == 1 else f"src/study/module-{mod_num:02d}-session-{num:02d}.js"

    objectives = [
        f"Explain the core clinical concepts of {title}",
        f"Apply {mod_name.lower()} knowledge to NCLEX-style scenarios",
        f"Identify priority nursing interventions using clinical reasoning",
        f"Demonstrate understanding through practice questions and study exercises",
        f"Connect this session's content to the broader {mod_name} module",
    ]

    concept_paragraphs = HYDRATED_CONCEPT.get(session_num)
    if not concept_paragraphs:
        concept_paragraphs = f"""
    <h3>Clinical Foundation — {title}</h3>
    <p>
      This session covers <strong>{concept}</strong>. NCLEX-RN questions in the {mod_name} domain
      test whether you can apply nursing knowledge to patient scenarios — not whether you can recite definitions.
    </p>
    <p>
      Registered nurses must integrate assessment findings, evidence-based interventions, and safety protocols.
      Every question on the NCLEX expects you to think like a nurse at the bedside: assess first, prioritize by
      acuity, intervene safely, and evaluate outcomes.
    </p>

    <h3>Key Concepts for This Session</h3>
    <ul>
      <li><strong>Core focus:</strong> {concept}</li>
      <li><strong>Module context:</strong> {mod_name} — Module {mod_num} of 10</li>
      <li><strong>NCLEX category:</strong> Safe and Effective Care Environment / Physiological Integrity</li>
      <li><strong>Study milestone:</strong> {milestone}</li>
    </ul>

    <div class="alert alert-warning">
      <strong>NCLEX testing tip:</strong> When two answers seem correct, choose the one that addresses
      the most acute patient need first. Use ABCs (Airway, Breathing, Circulation) and Maslow's hierarchy
      as your prioritization framework.
    </div>

    <h3>Clinical Application</h3>
    <p>
      In practice, {title.lower()} requires the nurse to gather data, recognize patterns, and select
      interventions that prevent harm. On the NCLEX, distractors often include actions that are correct
      in isolation but wrong for the specific scenario — always read the question stem carefully for
      keywords like "first," "priority," "best," and "initial."
    </p>

    <pre><code>// Patient case data structure used throughout this platform
const patientCase = {{
  id: "PT-{num:04d}",
  module: "{mod_name}",
  session: {num},
  chiefComplaint: "...",
  vitalSigns: {{ hr: 0, bp: "0/0", rr: 0, temp: 0, spo2: 0 }},
  assessment: {{ /* findings */ }},
  priorityInterventions: [ /* ordered list */ ]
}};</code></pre>

    <h3>Connection to NCLEX-RN Exam</h3>
    <p>
      Questions related to {mod_name.lower()} appear frequently on the NCLEX-RN. Mastery of {title.lower()}
      builds the clinical reasoning foundation needed for both standalone questions and case studies with
      6–10 follow-up questions in the new Next Generation NCLEX (NGN) format.
    </p>
"""

    step_list = HYDRATED_STEPS.get(session_num) or [
        ("Create the study file", f"Create <code>{lab_file}</code> in your editor."),
        ("Define the patient case", f"Write a patient scenario related to {title}. Include at least 5 clinical data points."),
        ("Document vital signs", "Add a vitalSigns object with hr, bp, rr, temp, and spo2 values appropriate to the scenario."),
        ("List assessment findings", "Document subjective and objective findings that support your clinical reasoning."),
        ("Identify priority interventions", "List 3 nursing interventions in priority order with rationale for each."),
        ("Log your reasoning", "Add console.log statements that output your priority intervention and why it comes first."),
        ("Self-check", "Review your case against the concept section. Can you defend every data point clinically?"),
    ]

    steps = step_list

    steps_html = ""
    for i, (heading, body) in enumerate(steps, 1):
        steps_html += f"""
    <div class="step">
      <div class="step-num">{i}</div>
      <div class="step-body">
        <p><strong>{heading}</strong></p>
        <p>{body}</p>
      </div>
    </div>"""

    next_session = session_num + 1 if session_num < 40 else None
    next_link = f'../../sessions/session-{next_session:02d}/index.html' if next_session else '../../sessions/index.html'
    next_title = get_session_info(next_session)[1][1] if next_session else "Curriculum Complete"
    next_num_str = f"{next_session:02d}" if next_session else "40"

    html = f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Session {num:02d} — {title}</title>
  <link rel="stylesheet" href="../../styles.css" />
  <style>{SESSION_STYLES}</style>
</head>
<body>

{nav_links("../../", "Sessions")}

<main>
  <div class="container">

    <div style="display:flex; align-items:center; gap:12px; margin-bottom:6px;">
      <span class="badge badge-layer">Module {mod_num}</span>
      <span class="badge {gate_badge}">Session {num:02d}</span>
      <span style="color:var(--text-muted); font-size:13px;">{mod_name}</span>
    </div>
    <h1>{title}</h1>
    <p class="subtitle">
      {concept}. This session is part of Module {mod_num}: {mod_name}.
      Complete the pre-quiz, study the concepts, complete the study session, commit, and pass the post-quiz.
    </p>

    <div class="alert alert-info">
      Estimated time: 35–40 minutes &nbsp;·&nbsp;
      Pre-quiz → Concept → Study Session → Commit → Post-quiz
    </div>

    <h2>1. Learning Objective</h2>
    <div class="card">
      <p>By the end of this session you will be able to:</p>
      <ul>
        {"".join(f"<li>{o}</li>" for o in objectives)}
      </ul>
    </div>

    <h2>2. Pre-Study Quiz</h2>
    <p>
      Answer these <strong>before</strong> reading the concept explanation or starting the study session.
      Score honestly. You need 4/5 (80%) to proceed.
    </p>
    {render_quiz_block("pre", session_num, title, mod_name)}

    <hr class="section-divider" />

    <h2>3. The Concept — {title}</h2>
    {concept_paragraphs}

    <hr class="section-divider" />

    <h2>4. Study Session</h2>
    <div class="alert alert-success">
      <strong>Study session objective:</strong> {milestone}
    </div>
    <h3>Step-by-step instructions</h3>
    {steps_html}

    <hr class="section-divider" />

    <h2>5. Expected Files Changed</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>File</th><th>Action</th><th>Why</th></tr></thead>
        <tbody>
          <tr>
            <td><code>{lab_file}</code></td>
            <td>Created or Updated</td>
            <td>Patient case / study exercise for this session.</td>
          </tr>
          <tr>
            <td><code>docs/sessions/session-{num:02d}/index.html</code></td>
            <td>Reference</td>
            <td>This session document.</td>
          </tr>
        </tbody>
      </table>
    </div>

    <hr class="section-divider" />

    <h2>6. Commit Checkpoint</h2>
    <p>Once the study session is complete and you can explain every clinical decision, make this commit:</p>
    <pre><code>git add {lab_file} docs/sessions/session-{num:02d}/index.html
git commit -m "session-{num:02d}: {title.lower()} — study session complete"</code></pre>

    <hr class="section-divider" />

    <h2>7. Code Review Checklist</h2>
    <div class="card">
      <div class="checklist-item"><input type="checkbox" id="c1" /><label for="c1">Patient case includes realistic vital signs for the scenario</label></div>
      <div class="checklist-item"><input type="checkbox" id="c2" /><label for="c2">Assessment findings support the priority interventions chosen</label></div>
      <div class="checklist-item"><input type="checkbox" id="c3" /><label for="c3">Interventions are listed in priority order (most acute first)</label></div>
      <div class="checklist-item"><input type="checkbox" id="c4" /><label for="c4">I can explain the clinical rationale for each intervention</label></div>
      <div class="checklist-item"><input type="checkbox" id="c5" /><label for="c5">Study file runs without errors in Node or browser console</label></div>
    </div>

    <hr class="section-divider" />

    <h2>8. Post-Study Quiz</h2>
    <p>Same 5 questions. Take again after completing the study session. Need 4/5 to mark complete.</p>
    {render_quiz_block("post", session_num, title, mod_name)}

    <hr class="section-divider" />

    <h2>9. Reflection Questions</h2>
    <div class="card">
      <ol>
        <li>Which concept in this session was most challenging? Why?</li>
        <li>How would you apply {title.lower()} knowledge if you had two patients with competing needs?</li>
        <li>What NCLEX-style distractors might trick you on this topic?</li>
        <li>What would you do differently in clinical practice based on today's study?</li>
      </ol>
    </div>

    <hr class="section-divider" />

    <h2>10. What Breaks If This Knowledge Is Missing?</h2>
    <div class="card">
      <ul>
        <li><strong>Patient safety:</strong> Gaps in {mod_name.lower()} knowledge directly impact patient outcomes on the NCLEX and at the bedside.</li>
        <li><strong>Prioritization errors:</strong> Without {title.lower()} mastery, you may select interventions that are correct but not the priority action.</li>
        <li><strong>Module progression:</strong> Later sessions in {mod_name} build on this content. Skipping mastery here compounds errors downstream.</li>
      </ul>
    </div>

    <hr class="section-divider" />

    <h2>11. What We Learned</h2>
    <div class="card" style="border-color: var(--green);">
      <p><strong>Clinical concept mastered:</strong> {title} — {concept}</p>
      <p><strong>Module progress:</strong> Session {num} of 4 in Module {mod_num}: {mod_name}</p>
      <p><strong>Next session:</strong> <a href="{next_link}">Session {next_num_str} — {next_title}</a></p>
    </div>

  </div>
</main>

{QUIZ_SCRIPT}
</body>
</html>
"""
    return html


def generate_index():
    rows = ""
    for mod in MODULES:
        gate_session = mod["sessions"][-1][0]
        prev_gate = mod["sessions"][0][0] - 1
        unlock = "None — starting point" if mod["num"] == 1 else f"Session {prev_gate:02d} quiz ≥ 80%"
        status = "Active" if mod["num"] == 1 else "Locked"
        badge = "badge-current" if mod["num"] == 1 else "badge-locked"
        s_start = mod["sessions"][0][0]
        s_end = mod["sessions"][-1][0]
        rows += f"""
          <tr>
            <td><span class="badge badge-layer">{mod['num']}</span></td>
            <td>{mod['name']}</td>
            <td>{s_start:02d} – {s_end:02d}</td>
            <td><span class="badge {badge}">{status}</span></td>
            <td>{unlock}</td>
          </tr>"""

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{TITLE}</title>
  <link rel="stylesheet" href="styles.css" />
</head>
<body>

{nav_links("", "brand")}

<main>
  <div class="container">

    <h1>{TITLE}</h1>
    <p class="subtitle">
      A structured, documentation-first NCLEX-RN exam preparation curriculum for nursing students
      who want to understand clinical reasoning deeply — not just memorize answer banks.
    </p>

    <div class="card">
      <div class="card-title">Overall Progress</div>
      <div class="progress-wrap">
        <div class="progress-label">
          <span>Sessions completed</span>
          <span id="progress-text">0 / 40</span>
        </div>
        <div class="progress-bar-bg">
          <div class="progress-bar" style="width: 0%"></div>
        </div>
      </div>
      <div style="display:flex; gap:12px; flex-wrap:wrap; margin-top:10px;">
        <span class="badge badge-complete">Complete: 0</span>
        <span class="badge badge-current">Active: Session 01</span>
        <span class="badge badge-locked">Locked: 39</span>
      </div>
    </div>

    <div class="alert alert-info" style="margin-bottom: 32px;">
      <strong>Active session:</strong>
      <a href="sessions/session-01/index.html">Session 01 — Standard Precautions &amp; Hand Hygiene</a>
      &nbsp;·&nbsp; Module 1: Infection Control &amp; Safety
    </div>

    <h2>Documentation Sections</h2>
    <div class="nav-grid">
      <a class="nav-card" href="syllabus/index.html"><div class="nav-card-title">Syllabus</div><div class="nav-card-desc">All 40 sessions, module breakdown, unlock gates, and dependency ordering.</div></a>
      <a class="nav-card" href="sessions/index.html"><div class="nav-card-title">Sessions</div><div class="nav-card-desc">Individual lesson docs — objectives, quizzes, study sessions, and commit checkpoints.</div></a>
      <a class="nav-card" href="quizzes/index.html"><div class="nav-card-title">Quizzes</div><div class="nav-card-desc">Quiz bank and score tracker. Must score 80% to advance each module.</div></a>
      <a class="nav-card" href="labs/index.html"><div class="nav-card-title">Study Sessions</div><div class="nav-card-desc">Study session reference index. Step-by-step exercises per session.</div></a>
      <a class="nav-card" href="architecture/index.html"><div class="nav-card-title">Architecture</div><div class="nav-card-desc">Architecture decision log. Every structural choice documented here.</div></a>
      <a class="nav-card" href="session-notes/index.html"><div class="nav-card-title">Session Notes</div><div class="nav-card-desc">Running notes from each session. Questions raised and answered.</div></a>
      <a class="nav-card" href="commit-reviews/index.html"><div class="nav-card-title">Commit Reviews</div><div class="nav-card-desc">Every commit reviewed here before moving forward.</div></a>
      <a class="nav-card" href="prompts/index.html"><div class="nav-card-title">Prompt Log</div><div class="nav-card-desc">Every prompt sent to the AI in this project, logged in order.</div></a>
    </div>

    <h2>Curriculum Modules</h2>
    <div class="table-wrap">
      <table>
        <thead>
          <tr><th>Module</th><th>Topic</th><th>Sessions</th><th>Status</th><th>Unlock Condition</th></tr>
        </thead>
        <tbody>{rows}
        </tbody>
      </table>
    </div>

    <h2>Rules We Follow</h2>
    <div class="card">
      <ol>
        <li>Never jump ahead — clinical concepts taught in strict dependency order.</li>
        <li>One session = one focused topic = one commit.</li>
        <li>Always assess before intervening — nursing process first.</li>
        <li>Score below 80% on a quiz = repeat the session.</li>
        <li>Every study session ends with documentation updates.</li>
        <li>Understand every commit before proceeding.</li>
        <li>Practice questions test clinical reasoning, not memorization.</li>
        <li>Every lesson completable in 35–40 minutes.</li>
      </ol>
    </div>

    <p class="subtitle" style="margin-top: 32px;">
      Package manager: <code>npm</code> &nbsp;·&nbsp;
      Framework: <code>React + Vite</code> &nbsp;·&nbsp;
      Testing: <code>Vitest + React Testing Library</code> &nbsp;·&nbsp;
      Language: <code>JavaScript (no TypeScript)</code>
    </p>

  </div>
</main>
</body>
</html>
"""


def generate_syllabus():
    sections = ""
    for mod in MODULES:
        gate_session = mod["sessions"][-1][0]
        prev_gate = mod["sessions"][0][0] - 1
        status_badge = "badge-current" if mod["num"] == 1 else "badge-locked"
        status_label = "Active" if mod["num"] == 1 else "Locked"
        rows = ""
        for num, title, concept, milestone in mod["sessions"]:
            s_badge = "badge-current" if mod["num"] == 1 else "badge-locked"
            s_label = "Current" if num == 1 else ("Available" if mod["num"] == 1 else "Locked")
            if num == gate_session:
                s_badge = "badge-gate"
                s_label = "Gate"
            link = f'<a href="../sessions/session-{num:02d}/index.html">{num:02d}</a>' if mod["num"] == 1 else f"{num:02d}"
            rows += f"""
          <tr>
            <td>{link}</td>
            <td>{title}</td>
            <td>{concept}</td>
            <td>{milestone}</td>
            <td><span class="badge {s_badge}">{s_label}</span></td>
          </tr>"""
        gate_msg = "None — starting point" if mod["num"] == 1 else f"Session {prev_gate:02d} quiz ≥ 80%"
        sections += f"""
    <div class="layer-header">
      <span class="badge {status_badge}">{status_label}</span>
      <span class="layer-title">Module {mod['num']} — {mod['name']}</span>
    </div>
    <p class="layer-desc">
      Sessions {mod['sessions'][0][0]:02d}–{gate_session:02d}. Gate quiz at Session {gate_session:02d} required before Module {mod['num']+1 if mod['num'] < 10 else 'Capstone'} unlocks.
    </p>
    <div class="table-wrap">
      <table>
        <thead><tr><th>#</th><th>Title</th><th>Core Concept</th><th>Study Milestone</th><th>Status</th></tr></thead>
        <tbody>{rows}
        </tbody>
      </table>
    </div>
    <div class="alert alert-warning">
      <strong>Module {mod['num']} Gate:</strong> Must score ≥ 80% on Session {gate_session:02d} post-quiz before Session {gate_session+1:02d} unlocks. Unlock condition: {gate_msg}
    </div>
"""
    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Syllabus — NCLEX-RN Prep</title>
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
{nav_links("../", "Syllabus")}
<main><div class="container">
    <h1>40-Session NCLEX-RN Curriculum</h1>
    <p class="subtitle">10 modules × 4 sessions. Each module unlocks after the gate session scores ≥ 80%.</p>
    <div class="alert alert-info"><strong>Active session:</strong> Session 01 — Standard Precautions &amp; Hand Hygiene</div>
    {sections}
    <h2>Dependency Ordering</h2>
    <p>Each module builds on prior modules. Infection control and safety foundations precede all clinical specialties.</p>
    <pre><code>Infection Control → Emergency Response → Pharmacology → Prioritization
  → Cardiovascular → Respiratory → Endocrine → Pediatrics
    → Maternity → Mental Health → Capstone Review</code></pre>
</div></main>
</body>
</html>
"""


def generate_sessions_index():
    mod1_rows = ""
    for num, title, _, _ in MODULES[0]["sessions"]:
        is_gate = num == 4
        badge = "badge-gate" if is_gate else "badge-current"
        label = "Gate" if is_gate else "Available"
        mod1_rows += f"""
          <tr>
            <td><a href="session-{num:02d}/index.html">{num:02d}</a></td>
            <td>{title}</td>
            <td><span class="badge {badge}">{label}</span></td>
            <td>—</td><td>—</td><td>—</td>
          </tr>"""

    locked_modules = ""
    for mod in MODULES[1:]:
        locked_modules += f"""
    <h2>Module {mod['num']} — {mod['name']}</h2>
    <div class="alert alert-warning">Locked until Module {mod['num']-1} gate quiz ≥ 80%</div>
    <div class="table-wrap"><table><thead><tr><th>#</th><th>Title</th><th>Status</th></tr></thead><tbody>"""
        for num, title, _, _ in mod["sessions"]:
            locked_modules += f'<tr><td>{num:02d}</td><td>{title}</td><td><span class="badge badge-locked">Locked</span></td></tr>'
        locked_modules += "</tbody></table></div>"

    return f"""<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Sessions — NCLEX-RN Prep</title>
  <link rel="stylesheet" href="../styles.css" />
</head>
<body>
{nav_links("../", "Sessions")}
<main><div class="container">
    <h1>Sessions</h1>
    <p class="subtitle">One session doc per lesson. Pre-quiz, study session, commit checkpoint, post-quiz.</p>
    <div class="alert alert-info"><strong>Sessions 01–04 are available.</strong> Complete Session 04 gate to unlock Module 2.</div>
    <h2>Module 1 — Infection Control &amp; Safety</h2>
    <div class="table-wrap">
      <table>
        <thead><tr><th>#</th><th>Title</th><th>Status</th><th>Pre-Quiz</th><th>Post-Quiz</th><th>Committed</th></tr></thead>
        <tbody>{mod1_rows}
        </tbody>
      </table>
    </div>
    {locked_modules}
    <p style="color:var(--text-muted);font-size:14px;">Full session list in <a href="../syllabus/index.html">Syllabus</a>.</p>
</div></main>
</body>
</html>
"""


def generate_quizzes_index():
    rows = ""
    for mod in MODULES:
        for num, title, _, _ in mod["sessions"]:
            link = f'<a href="../sessions/session-{num:02d}/index.html">{num:02d}</a>' if mod["num"] == 1 else f"{num:02d}"
            rows += f'<tr><td>{link}</td><td>{title}</td><td>—</td><td>—</td><td>—</td><td>—</td></tr>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Quizzes — NCLEX-RN Prep</title><link rel="stylesheet" href="../styles.css" /></head>
<body>
{nav_links("../", "Quizzes")}
<main><div class="container">
    <h1>Quiz Bank &amp; Score Tracker</h1>
    <p class="subtitle">Each session has 5 questions — pre and post study. Must score ≥ 80% (4/5) to advance.</p>
    <div class="alert alert-warning"><strong>Quiz rule:</strong> Questions test clinical reasoning, not memorization.</div>
    <h2>Score History</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>Session</th><th>Title</th><th>Pre-Quiz</th><th>Post-Quiz</th><th>Passed?</th><th>Date</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
</div></main></body></html>
"""


def generate_labs_index():
    rows = ""
    for mod in MODULES:
        for num, title, _, milestone in mod["sessions"]:
            lab_file = "src/patient-case.js" if num == 1 else f"src/study/module-{mod['num']:02d}-session-{num:02d}.js"
            status = "badge-current" if num == 1 else "badge-locked"
            label = "Current" if num == 1 else "Locked"
            link = f'<a href="../sessions/session-{num:02d}/index.html">{num:02d}</a>' if mod["num"] == 1 else f"{num:02d}"
            rows += f'<tr><td>{link}</td><td>{milestone}</td><td><code>{lab_file}</code></td><td><span class="badge {status}">{label}</span></td></tr>'
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Study Sessions — NCLEX-RN Prep</title><link rel="stylesheet" href="../styles.css" /></head>
<body>
{nav_links("../", "Labs")}
<main><div class="container">
    <h1>Study Session Reference Index</h1>
    <p class="subtitle">Study sessions are embedded in session docs — this page is a quick lookup index.</p>
    <h2>Study Objectives by Session</h2>
    <div class="table-wrap"><table>
      <thead><tr><th>#</th><th>Study Objective</th><th>Files Touched</th><th>Status</th></tr></thead>
      <tbody>{rows}</tbody>
    </table></div>
</div></main></body></html>
"""


def generate_architecture():
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Architecture — NCLEX-RN Prep</title><link rel="stylesheet" href="../styles.css" /></head>
<body>
{nav_links("../", "Architecture")}
<main><div class="container">
    <h1>Architecture Decisions</h1>
    <p class="subtitle">Structural decisions documented with reasoning — cloned from react-learn-with-ai philosophy.</p>
    <div class="card">
      <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
        <span class="card-title">ADR-001 — Plain JavaScript (no TypeScript)</span>
        <span class="badge badge-layer">Pre-curriculum</span>
      </div>
      <p><strong>Decision:</strong> Plain JavaScript throughout. No TypeScript.</p>
      <p><strong>Why:</strong> Same rationale as source project — one mental model at a time. Type errors distract from clinical content.</p>
    </div>
    <div class="card">
      <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
        <span class="card-title">ADR-002 — Static HTML docs (no build step)</span>
        <span class="badge badge-layer">Pre-curriculum</span>
      </div>
      <p><strong>Decision:</strong> Documentation is static HTML with shared styles.css.</p>
      <p><strong>Why:</strong> Zero dependencies. Openable anywhere. AI sessions read source directly.</p>
    </div>
    <div class="card">
      <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
        <span class="card-title">ADR-003 — Domain migration from react-learn-with-ai</span>
        <span class="badge badge-layer">Pre-curriculum</span>
      </div>
      <p><strong>Decision:</strong> Replicate exact folder structure, session flow, quiz engine, and progression gates from react-learn-with-ai. Only educational domain changes.</p>
      <p><strong>Why:</strong> Proven learning platform architecture. NCLEX-RN content swaps into existing patterns without redesign.</p>
    </div>
    <div class="card">
      <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
        <span class="card-title">ADR-004 — Mock patient data before live integrations</span>
        <span class="badge badge-layer">Pre-curriculum</span>
      </div>
      <p><strong>Decision:</strong> Patient cases live in /src/mock/ and /src/study/. No EHR integration until later modules.</p>
      <p><strong>Why:</strong> Same mock-first philosophy as source project. Study independently of external systems.</p>
    </div>
    <div class="card">
      <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
        <span class="card-title">ADR-005 — 10 modules × 4 sessions = 40 session curriculum</span>
        <span class="badge badge-layer">Pre-curriculum</span>
      </div>
      <p><strong>Decision:</strong> Mirror 40-session structure. 10 NCLEX domains with 4 sessions each. Gate quiz at session 4, 8, 12, etc.</p>
      <p><strong>Why:</strong> Preserves progression checkpoint rhythm from source project.</p>
    </div>
</div></main></body></html>
"""


def generate_session_notes():
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Session Notes — NCLEX-RN Prep</title><link rel="stylesheet" href="../styles.css" /></head>
<body>
{nav_links("../", "Notes")}
<main><div class="container">
    <h1>Session Notes</h1>
    <p class="subtitle">Running notes from each session. Questions, confusion points, breakthroughs.</p>
    <div class="card">
      <div style="display:flex;justify-content:space-between;margin-bottom:10px;">
        <span class="card-title">Pre-curriculum — NCLEX-RN Project Setup</span>
        <span style="color:var(--text-muted);font-size:13px;">2026-06-19</span>
      </div>
      <p><strong>Covered:</strong> Full 40-session NCLEX-RN curriculum created by domain migration from react-learn-with-ai.
      All documentation infrastructure generated. Module 1 sessions 01–04 available.</p>
      <p><strong>Decisions:</strong> Same architecture as source — static HTML docs, plain JS study files, 80% quiz gate, module progression.</p>
      <p><strong>Next:</strong> Session 01 — Standard Precautions &amp; Hand Hygiene.</p>
    </div>
</div></main></body></html>
"""


def generate_commit_reviews():
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Commit Reviews — NCLEX-RN Prep</title><link rel="stylesheet" href="../styles.css" /></head>
<body>
{nav_links("../", "Commits")}
<main><div class="container">
    <h1>Commit Reviews</h1>
    <p class="subtitle">Every commit reviewed before the session ends.</p>
    <div class="commit-entry">
      <div style="display:flex;justify-content:space-between;margin-bottom:12px;">
        <span class="card-title">Setup: NCLEX-RN repository from react-learn-with-ai domain migration</span>
        <span class="badge badge-complete">Committed</span>
      </div>
      <p><span class="commit-hash">Pre-curriculum</span> &nbsp;·&nbsp; 2026-06-19</p>
      <p style="margin-top:10px;"><strong>Files created:</strong></p>
      <ul>
        <li><code>docs/</code> — full documentation tree (index, syllabus, sessions, quizzes, labs, architecture, notes, commits, prompts)</li>
        <li><code>docs/sessions/session-01</code> through <code>session-40</code> — all session lesson docs</li>
        <li><code>src/patient-case.js</code> — Session 01 study file starter</li>
        <li><code>src/components|pages|hooks|services|mock|tests/</code> — placeholder folders matching source architecture</li>
        <li><code>README.md</code>, <code>.gitignore</code></li>
      </ul>
    </div>
</div></main></body></html>
"""


def generate_prompts():
    return f"""<!DOCTYPE html>
<html lang="en">
<head><meta charset="UTF-8" /><meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Prompt Log — NCLEX-RN Prep</title><link rel="stylesheet" href="../styles.css" /></head>
<body>
{nav_links("../", "Prompts")}
<main><div class="container">
    <h1>Prompt Log</h1>
    <p class="subtitle">Every prompt sent to the AI in this project, logged in order.</p>
    <div class="prompt-entry">
      <div class="prompt-meta"><span>#1</span><span>2026-06-19</span><span>Session: Pre-curriculum (Domain Migration)</span></div>
      <div class="prompt-text">Create NCLEX-RN sibling project beside react-learn-with-ai. Replicate exact architecture. Replace only educational domain with 10-module NCLEX-RN curriculum.</div>
    </div>
</div></main></body></html>
"""


def generate_readme():
    return """# NCLEX-RN Exam Preparation Platform

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
"""


def generate_patient_case_js():
    return """// Session 01 — Standard Precautions & Hand Hygiene
// Define a patient case as a JavaScript object to study infection control concepts

const patientCase = {
    id: "PT-0001",
    module: "Infection Control & Safety",
    session: 1,
    name: "Patient A",
    age: 67,
    diagnosis: "Post-operative wound infection — MRSA positive",
    isolation: "Contact Precautions",
    vitalSigns: {
        hr: 88,
        bp: "128/76",
        rr: 18,
        temp: 38.2,
        spo2: 96
    },
    assessment: {
        woundDrainage: "Purulent, moderate amount",
        handHygieneCompliance: "Required before and after all contact",
        ppeRequired: ["Gown", "Gloves"],
        roomRequirements: "Private room preferred; dedicated equipment"
    },
    priorityInterventions: [
        "Perform hand hygiene before entering room",
        "Don gown and gloves before patient contact",
        "Assess wound and document drainage characteristics",
        "Educate patient on contact precaution rationale"
    ]
};

// Read properties using dot notation
console.log("Patient ID:", patientCase.id);
console.log("Isolation type:", patientCase.isolation);
console.log("Temperature:", patientCase.vitalSigns.temp);

// Read property using bracket notation with a variable
const propertyToRead = "diagnosis";
console.log("Diagnosis (bracket):", patientCase[propertyToRead]);

// Reference behavior demonstration
const original = { compliance: "pending", score: 0 };
const copy = original;
copy.score = 100;
console.log("original.score:", original.score); // 100 — same reference

// Add property after creation
console.log("Before:", patientCase.cultureSent);
patientCase.cultureSent = true;
console.log("After:", patientCase.cultureSent);

// Nested object
patientCase.infectionChain = {
    infectiousAgent: "MRSA",
    reservoir: "Wound",
    portalOfExit: "Drainage",
    modeOfTransmission: "Direct contact",
    portalOfEntry: "Broken skin / mucous membrane",
    susceptibleHost: "Immunocompromised post-op patient"
};

console.log("Infectious agent:", patientCase.infectionChain.infectiousAgent);
console.log("First priority intervention:", patientCase.priorityInterventions[0]);
"""


def main():
    docs = ROOT / "docs"
    docs.mkdir(parents=True, exist_ok=True)

    (docs / "index.html").write_text(generate_index(), encoding="utf-8")
    (docs / "syllabus" / "index.html").write_text(generate_syllabus(), encoding="utf-8")
    (docs / "sessions" / "index.html").write_text(generate_sessions_index(), encoding="utf-8")
    (docs / "quizzes" / "index.html").write_text(generate_quizzes_index(), encoding="utf-8")
    (docs / "labs" / "index.html").write_text(generate_labs_index(), encoding="utf-8")
    (docs / "architecture" / "index.html").write_text(generate_architecture(), encoding="utf-8")
    (docs / "session-notes" / "index.html").write_text(generate_session_notes(), encoding="utf-8")
    (docs / "commit-reviews" / "index.html").write_text(generate_commit_reviews(), encoding="utf-8")
    (docs / "prompts" / "index.html").write_text(generate_prompts(), encoding="utf-8")

    for i in range(1, 41):
        session_dir = docs / "sessions" / f"session-{i:02d}"
        session_dir.mkdir(parents=True, exist_ok=True)
        (session_dir / "index.html").write_text(generate_session(i), encoding="utf-8")

    (ROOT / "README.md").write_text(generate_readme(), encoding="utf-8")
    (ROOT / "src" / "patient-case.js").write_text(generate_patient_case_js(), encoding="utf-8")

    for folder in ["components", "pages", "hooks", "services", "mock", "tests"]:
        p = ROOT / "src" / folder
        p.mkdir(parents=True, exist_ok=True)
        gitkeep = p / ".gitkeep"
        if not gitkeep.exists():
            gitkeep.write_text("", encoding="utf-8")

    (ROOT / "src" / "study").mkdir(parents=True, exist_ok=True)
    for rel_path, content in STUDY_FILE_CONTENT.items():
        out = ROOT / rel_path.replace("/", os.sep)
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text(content, encoding="utf-8")

    print(f"Generated NCLEX-RN project at {ROOT}")
    print(f"Sessions: 40 | Modules: 10 | Hydrated: sessions 02–04")


if __name__ == "__main__":
    main()
