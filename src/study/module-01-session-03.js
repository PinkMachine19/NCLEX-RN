// Session 03 — PPE Selection & Donning/Doffing
// PPE checklist for MRSA contact precautions

const ppeProtocol = {
    patient: "PT-0301",
    isolation: "Contact — MRSA wound",
    location: "Room 418",

    donning: [
        "Perform hand hygiene",
        "Apply gown — tie neck and waist, sleeves fully covered",
        "Apply mask if splash/spray anticipated",
        "Apply gloves last — cuff over gown sleeves"
    ],

    doffing: [
        "Remove gloves first — avoid touching outer surfaces",
        "Remove gown — roll away from body, touch inside only",
        "Remove eye protection by headband if worn",
        "Remove mask — do not touch front",
        "Perform hand hygiene immediately"
    ],

    errorsToAvoid: [
        "Donning gloves before gown",
        "Touching outer mask surface during removal",
        "Leaving room without hand hygiene after doffing",
        "Reusing disposable gown between patients"
    ],

    n95Required: false,
    note: "N95 is for airborne (TB, measles, varicella) — MRSA contact = gown + gloves"
};

console.log("=== DONNING ===");
ppeProtocol.donning.forEach((step, i) => console.log((i + 1) + ". " + step));

console.log("\n=== DOFFING ===");
ppeProtocol.doffing.forEach((step, i) => console.log((i + 1) + ". " + step));

console.log("\nFirst doff step (NCLEX):", ppeProtocol.doffing[0]);
console.log("N95 required?", ppeProtocol.n95Required);
