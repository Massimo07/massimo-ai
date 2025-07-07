"""
Modulo: badge_generator.py
Crea badge grafici PNG/JPG con nome, livello, logo, colore, premi. Pronto per onboarding, reward, NFT, social!
"""

from PIL import Image, ImageDraw, ImageFont

def generate_badge(name, level, filename="badge.png", color="#FFD700", logo_path=None):
    img = Image.new('RGB', (400, 400), color)
    draw = ImageDraw.Draw(img)
    font_big = ImageFont.truetype("arial.ttf", 42)
    font_small = ImageFont.truetype("arial.ttf", 24)
    draw.text((50, 50), name, fill="black", font=font_big)
    draw.text((50, 120), level, fill="black", font=font_small)
    if logo_path:
        logo = Image.open(logo_path).resize((100,100))
        img.paste(logo, (250, 250))
    img.save(filename)
    return filename

# --- ESEMPIO USO ---
if __name__ == "__main__":
    print(generate_badge("Black Diamond", "Top Leader", color="#00D1FF"))
