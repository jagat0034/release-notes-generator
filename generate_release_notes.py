import json

with open('release_note.json', 'r') as file:
    data = json.load(file)

print(data["product"])
print(data["version"])
print(data["date"])

section_titles = {
    "new": "New Features",
    "improved": "Improved Features",
    "removed": "Removed Features"
}

lines=[]
lines.append("# " + data["product"] + " " + data["version"] + " release note")
lines.append("")
lines.append("Release date: " + data["date"])
lines.append("")

for audience in data["audiences"]:
    lines.append("## " + audience["audience_title"])
    lines.append("")

    for type in section_titles:
        lines.append("### " + section_titles[type])
        lines.append("")

        for change in audience["changes"]:
            if change["type"] == type:
                lines.append("- " + change["description"])
                lines.append("")


with open("release_notes_output.md", "w") as file:
    file.write("\n".join(lines))


print("Saved to release_notes_output.md")