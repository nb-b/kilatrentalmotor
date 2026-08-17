import re

file_path = "e:/JOBS/rentalmotorbanyuwangi/index.html"
with open(file_path, "r", encoding="utf-8") as f:
    content = f.read()

def replacer(match):
    original_price = match.group(1)
    # create a random discounted price, e.g., subtract 20.000 or so. 
    # Let's say if original is 100.000, new is 80.000
    # Wait, let's just make it Rp 20.000 cheaper for all!
    # parse original price
    num_str = original_price.replace("Rp ", "").replace(".", "")
    val = int(num_str)
    # The current price shown becomes the original, and we subtract 15.000 for the discount
    new_val = val - 15000
    
    # format back
    new_price_str = f"Rp {new_val:,}".replace(",", ".")
    
    return f"""<div class=\"flex flex-col mb-1\">
                                <span class=\"text-sm font-medium text-gray-400 line-through decoration-brand-primary/50 decoration-2\">{original_price}</span>
                                <div class=\"flex items-baseline gap-1\">
                                    <span class=\"text-h3 font-bold text-brand-primary\">{new_price_str}</span>"""

# The target HTML chunk is:
# <div class="flex items-baseline gap-1">\n                                <span class="text-h3 font-bold text-brand-primary">Rp 100.000</span>
pattern = r'<div class="flex items-baseline gap-1">\s*<span class="text-h3 font-bold text-brand-primary">(Rp \d+\.\d{3})</span>'
new_content = re.sub(pattern, replacer, content)

with open(file_path, "w", encoding="utf-8") as f:
    f.write(new_content)
print("Discount applied!")
