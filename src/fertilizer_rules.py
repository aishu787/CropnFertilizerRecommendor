ideal_npk = {
    'rice': {'N': 90, 'P': 40, 'K': 40},
    'maize': {'N': 120, 'P': 60, 'K': 40},
    'wheat': {'N': 100, 'P': 50, 'K': 50},
    'banana': {'N': 200, 'P': 60, 'K': 250}
}

def recommend_fertilizer(crop, N, P, K):
    crop = crop.lower()
    if crop not in ideal_npk:
        return ["No fertilizer recommendation available for this crop."]

    ideal = ideal_npk[crop]
    advice = []

    if N < ideal['N']:
        advice.append("Add Nitrogen-rich fertilizer (e.g., Urea)")
    elif N > ideal['N']:
        advice.append("Reduce Nitrogen input")

    if P < ideal['P']:
        advice.append("Add Phosphorus-rich fertilizer (e.g., SSP, DAP)")
    elif P > ideal['P']:
        advice.append("Reduce Phosphorus input")

    if K < ideal['K']:
        advice.append("Add Potassium-rich fertilizer (e.g., MOP)")
    elif K > ideal['K']:
        advice.append("Reduce Potassium input")

    return advice or ["NPK levels are balanced."]
