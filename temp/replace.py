import sys

file_path = "e:/JOBS/rentalmotorbanyuwangi/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

# Replace full names
content = content.replace("Rental Motor Banyuwangi", "Kilat Rental Motor Banyuwangi")

# Replace Navbar logo
content = content.replace("Rental<span class=\"text-white font-light\">BWI</span>", "Kilat<span class=\"text-white font-light\">Rental</span>")

# Replace Footer logo
content = content.replace("RMB<span class=\"text-brand-primary\">.</span>", "Kilat<span class=\"text-brand-primary\">.</span>")

# Replace whatsapp generic text
content = content.replace("Halo Rental Motor Banyuwangi", "Halo Kilat Rental Motor Banyuwangi")

# Also just in case "Kilat Kilat" appears, fix it (if ran twice)
content = content.replace("Kilat Kilat", "Kilat")

with open(file_path, "w", encoding="utf-8") as f:
    f.write(content)
print("done")
