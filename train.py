import pandas as pd, pickle
from sklearn.ensemble import RandomForestClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

# →  Make sure harrypotter.csv is in the same folder
df = pd.read_csv("harrypotter.csv")

# Friendly snake‑case column names for the six traits we’ll use
col_map = {
    "Bravery": "bravery",
    "Ambition": "ambition",
    "Intelligence": "intelligence",
    "Loyalty": "loyalty",
    "Creativity": "creativity",
    "Dark Arts Knowledge": "dark_arts_knowledge"
}
df = df.rename(columns=col_map)

FEATURES = list(col_map.values())          # six columns, snake‑case
X = df[FEATURES]

# Encode “Gryffindor / Hufflepuff / Ravenclaw / Slytherin” → 0‑3
le = LabelEncoder()
y  = le.fit_transform(df["House"])

Xtr, Xte, ytr, yte = train_test_split(
        X, y, test_size=0.2, random_state=42, stratify=y)

model = RandomForestClassifier(n_estimators=200, random_state=42)
model.fit(Xtr, ytr)
print("Validation accuracy:", model.score(Xte, yte))

# Save both the model *and* the class list so Flask can reverse‑map
with open("model.pkl", "wb") as f:
    pickle.dump({"model": model, "classes": le.classes_}, f)
print("Model and classes saved to model.pkl")