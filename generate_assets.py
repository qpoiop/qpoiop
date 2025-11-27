import os
import random

# Directory for assets
ASSETS_DIR = os.path.join(os.path.dirname(__file__), "assets")
os.makedirs(ASSETS_DIR, exist_ok=True)

def generate_banner():
    width = 800
    height = 300
    
    # Pastel Pop Theme - Truly Bold & Round
    # Using Outfit font (clean, bold, round) instead of Fredoka (script-like)
    
    # 1. Define Gradients & Filters
    defs = """
    <defs>
        <!-- Pastel Pink/Orange Background Gradient -->
        <linearGradient id="bg-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FF6B9D;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#FFA07A;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FFB6C1;stop-opacity:1" />
        </linearGradient>
        
        <!-- Text Gradient (Vibrant) -->
        <linearGradient id="text-grad" x1="0%" y1="0%" x2="100%" y2="0%">
            <stop offset="0%" style="stop-color:#FF1493;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#FF6347;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#FFD700;stop-opacity:1" />
        </linearGradient>
        
        <!-- Border Gradient -->
        <linearGradient id="border-grad" x1="0%" y1="0%" x2="100%" y2="100%">
            <stop offset="0%" style="stop-color:#FF1493;stop-opacity:1" />
            <stop offset="50%" style="stop-color:#FFD700;stop-opacity:1" />
            <stop offset="100%" style="stop-color:#00CED1;stop-opacity:1" />
        </linearGradient>
        
        <filter id="shadow" x="-50%" y="-50%" width="200%" height="200%">
            <feDropShadow dx="4" dy="4" stdDeviation="2" flood-color="#000000" flood-opacity="0.3"/>
        </filter>
    </defs>
    """

    # 2. Decorative Background Elements (Abstract Shapes)
    decorations = ""
    # Large circles
    decorations += '<circle cx="100" cy="80" r="60" fill="#FFB6C1" opacity="0.3" />'
    decorations += '<circle cx="700" cy="220" r="80" fill="#FFA07A" opacity="0.25" />'
    # Dots pattern
    for i in range(15):
        x = random.randint(50, 750)
        y = random.randint(50, 250)
        r = random.randint(2, 5)
        decorations += f'<circle cx="{x}" cy="{y}" r="{r}" fill="#FFFFFF" opacity="0.4" />'
    
    # Curved shapes
    decorations += '<path d="M 600,50 Q 650,100 700,50" stroke="#FFFFFF" stroke-width="3" fill="none" opacity="0.3" />'
    decorations += '<path d="M 50,200 Q 100,250 150,200" stroke="#FFFFFF" stroke-width="3" fill="none" opacity="0.3" />'

    # 3. Typing Animation
    text_content = "undefined is not a function"
    char_count = len(text_content)
    
    css_content = f"""
        @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@900&family=Poppins:wght@800&display=swap');
        
        /* Main Title - EXTRA Bold & Thick */
        .title {{
            font-family: 'Outfit', sans-serif;
            font-weight: 900;
            font-size: 44px;
            fill: url(#text-grad);
            stroke: #FFFFFF;
            stroke-width: 1.5px;
            paint-order: stroke fill;
            filter: url(#shadow);
        }}
        
        /* Subtitle */
        .subtitle {{
            font-family: 'Poppins', sans-serif;
            font-size: 20px;
            fill: #FF1493;
            font-weight: 800;
        }}

        /* Cursor */
        .cursor {{
            fill: #FFD700;
            animation: blink 0.8s infinite;
        }}

        /* Typing Animation */
        .typing-mask {{
            animation: type 4s steps({char_count}) infinite;
        }}
        
        @keyframes type {{
            0%, 10% {{ width: 0; }}
            90%, 100% {{ width: 700px; }}
        }}
        
        @keyframes blink {{
            0%, 49% {{ opacity: 1; }}
            50%, 100% {{ opacity: 0; }}
        }}
        
        /* Floating Animation */
        @keyframes float {{
            0%, 100% {{ transform: translateY(0) rotate(0deg); }}
            50% {{ transform: translateY(-15px) rotate(5deg); }}
        }}
        .floater {{ animation: float 4s ease-in-out infinite; }}
    """
    
    svg_content = f"""<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
    {defs}
    <style>
    /* <![CDATA[ */
    {css_content}
    /* ]]> */
    </style>
    
    <!-- Gradient Border -->
    <rect x="0" y="0" width="{width}" height="{height}" fill="url(#bg-grad)" />
    <rect x="5" y="5" width="{width-10}" height="{height-10}" fill="url(#bg-grad)" stroke="url(#border-grad)" stroke-width="8" rx="15" />
    
    <!-- Background Decorations -->
    <g opacity="0.6">{decorations}</g>
    
    <!-- Floating Shapes -->
    <circle cx="650" cy="100" r="25" fill="#FFD700" opacity="0.4" class="floater" style="animation-delay: 0s;" />
    <rect x="120" y="220" width="35" height="35" rx="8" fill="#FF1493" opacity="0.3" class="floater" style="animation-delay: 1.5s;" />
    <polygon points="750,200 770,230 730,230" fill="#00CED1" opacity="0.35" class="floater" style="animation-delay: 0.8s;" />

    <!-- Main Content -->
    <g transform="translate(50, 150)">
        
        <!-- Subtitle -->
        <text x="5" y="-50" class="subtitle">웹 개발자</text>
        
        <!-- Typing Mask -->
        <mask id="type-mask">
            <rect x="0" y="-40" width="0" height="80" fill="white" class="typing-mask" />
        </mask>
        
        <!-- Main Text -->
        <text x="0" y="10" class="title" mask="url(#type-mask)">{text_content}</text>
        
        <!-- Blinking Cursor -->
        <rect x="0" y="-30" width="5" height="50" class="cursor" rx="2">
            <animate attributeName="x" 
                     dur="4s" 
                     calcMode="discrete" 
                     values="0;25;50;75;100;125;150;175;200;225;250;275;300;325;350;375;400;425;450;475;500;525;550;575;600;625;650;675;700" 
                     repeatCount="indefinite" />
        </rect>
        
    </g>
    
    </svg>
    """
    
    with open(os.path.join(ASSETS_DIR, "banner.svg"), "w") as f:
        f.write(svg_content)
    print("Generated banner.svg")

if __name__ == "__main__":
    generate_banner()
