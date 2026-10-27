import os
import subprocess

DIAGRAMS_DIR = r"e:\ecotrackcall\ECOTRACK\Document\diagrams"
CHROME_PATH = r"C:\Program Files\Google\Chrome\Application\chrome.exe"
if not os.path.exists(CHROME_PATH):
    CHROME_PATH = r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe"

svg_files = [f for f in os.listdir(DIAGRAMS_DIR) if f.endswith(".svg")]
print(f"Found {len(svg_files)} SVGs to convert to PNG...")

for svg_file in svg_files:
    base_name = os.path.splitext(svg_file)[0]
    svg_path = os.path.join(DIAGRAMS_DIR, svg_file)
    png_path = os.path.join(DIAGRAMS_DIR, f"{base_name}.png")
    
    # Create a small HTML wrapper to render the SVG cleanly
    html_content = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  html, body {{
    margin: 0;
    padding: 0;
    background: transparent;
    overflow: hidden;
  }}
  img {{
    width: 100vw;
    height: 100vh;
    display: block;
  }}
</style>
</head>
<body>
  <img src="{svg_file}" />
</body>
</html>"""
    html_path = os.path.join(DIAGRAMS_DIR, f"_temp_{base_name}.html")
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html_content)

    # Determine resolution based on diagram aspect
    if "figure_5_7" in base_name:
        dim = "1250,820"
    elif "figure_data_flow" in base_name:
        dim = "1200,480"
    elif "figure_9_1" in base_name:
        dim = "1150,720"
    elif "figure_3_1" in base_name:
        dim = "1100,650"
    else:
        dim = "1000,620"

    cmd = [
        CHROME_PATH,
        "--headless",
        "--disable-gpu",
        "--no-sandbox",
        f"--window-size={dim}",
        f"--screenshot={png_path}",
        html_path
    ]
    
    res = subprocess.run(cmd, capture_output=True, text=True)
    if os.path.exists(png_path) and os.path.getsize(png_path) > 1000:
        print(f"[OK] Converted {svg_file} -> {base_name}.png ({os.path.getsize(png_path)} bytes)")
    else:
        print(f"[FAIL] Failed {svg_file}: {res.stderr}")

    if os.path.exists(html_path):
        os.remove(html_path)

print("Finished rasterizing all diagrams.")
