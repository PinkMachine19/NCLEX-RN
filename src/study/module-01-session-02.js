// Session 02 — Transmission-Based Precautions
// Classify 3 patients by required isolation type

const patients = [
    {
        id: "PT-0201",
        name: "Mr. Chen",
        age: 54,
        diagnosis: "Active pulmonary tuberculosis",
        symptoms: ["Persistent cough", "Night sweats", "Positive sputum AFB"],
        precaution: "Airborne",
        ppe: ["N95 respirator (fit-tested)", "Gown if splash risk", "Gloves if touch risk"],
        room: "AIIR — negative pressure, door closed"
    },
    {
        id: "PT-0202",
        name: "Ms. Rivera",
        age: 32,
        diagnosis: "Influenza A",
        symptoms: ["Fever", "Myalgia", "Productive cough"],
        precaution: "Droplet",
        ppe: ["Surgical mask within 3–6 feet", "Gloves for contact", "Gown if soiling expected"],
        room: "May cohort with same organism; door may stay open"
    },
    {
        id: "PT-0203",
        name: "Mr. Walsh",
        age: 71,
        diagnosis: "MRSA colonization — wound drainage",
        symptoms: ["Purulent wound drainage", "Erythema at site"],
        precaution: "Contact",
        ppe: ["Gown", "Gloves for all room entry"],
        room: "Private room preferred; dedicated equipment"
    }
];

patients.forEach(p => {
    console.log(p.name + " | " + p.diagnosis);
    console.log("  → Precaution:", p.precaution);
    console.log("  → PPE:", p.ppe.join(", "));
    console.log("  → Room:", p.room);
    console.log("---");
});

// Bracket notation — read property dynamically
const field = "precaution";
console.log("Mr. Chen isolation type:", patients[0][field]);

// Most restrictive comparison (NCLEX pattern)
const restrictiveness = { Contact: 1, Droplet: 2, Airborne: 3 };
const mostRestrictive = patients.reduce((max, p) =>
    restrictiveness[p.precaution] > restrictiveness[max.precaution] ? p : max
);
console.log("Most restrictive patient:", mostRestrictive.name, "—", mostRestrictive.precaution);
