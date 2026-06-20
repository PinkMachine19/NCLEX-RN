// Session 04 — Module 1 Gate — Infection Control Integration
// Complete infection control case study with commit checkpoint

const gateCaseStudy = {
    id: "PT-GATE-01",
    module: "Infection Control & Safety",
    session: 4,
    scenario: {
        setting: "Medical-surgical unit, 0700",
        events: [
            "Nurse enters Room 512 without reading isolation sign",
            "Patient has C. diff with active diarrhea",
            "Nurse adjusts IV without gown or gloves",
            "Same nurse goes directly to Room 508 post-op patient"
        ]
    },
    violations: [
        "Failed to verify transmission-based precautions",
        "No hand hygiene before patient contact",
        "No contact precautions PPE (C. diff requires gown + gloves)",
        "Cross-contamination risk to second patient"
    ],
    priorityInterventions: [
        {
            order: 1,
            action: "Stop — do not continue care chain",
            rationale: "Prevent further cross-contamination"
        },
        {
            order: 2,
            action: "Perform hand hygiene; don contact PPE for Room 512",
            rationale: "C. diff = contact precautions; soap and water preferred over gel"
        },
        {
            order: 3,
            action: "Before Room 508 — full hand hygiene; change PPE",
            rationale: "Break chain of infection between patients"
        },
        {
            order: 4,
            action: "Report near-miss to charge nurse; document",
            rationale: "Quality improvement and patient safety"
        }
    ],
    gateRequirements: {
        preQuizMin: 4,
        postQuizMin: 4,
        commitMessage: "session-04: module 1 gate — infection control integration complete",
        unlocks: "Module 2 — Emergency Response"
    }
};

console.log("Scenario:", gateCaseStudy.scenario.setting);
gateCaseStudy.priorityInterventions.forEach(i => {
    console.log(i.order + ". " + i.action);
    console.log("   Why: " + i.rationale);
});
console.log("Gate pass:", gateCaseStudy.gateRequirements.preQuizMin + "/5 on pre and post quiz");
console.log("Unlocks:", gateCaseStudy.gateRequirements.unlocks);
