import pandas as pd
import re

# Function to fix titles like "Emperor's New Groove, The (2000)" → "The Emperor's New Groove (2000)"
def fix_title(title):
    match = re.match(r"^(.*),\s(The|A|An)\s\((\d{4})\)$", title)
    if match:
        name, article, year = match.groups()
        return f"{article} {name} ({year})"
    else:
        return title

# Load your movie dataset
df = pd.read_csv("movies.csv")

# Apply the title fix
df["title"] = df["title"].apply(fix_title)

# Save it as a new file
df.to_csv("movies_fixed.csv", index=False)

print("✅ Titles fixed successfully! Saved as movies_fixed.csv")
