// Session 01 — Standard Precautions & Hand Hygiene
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
