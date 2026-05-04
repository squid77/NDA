import os

# 1. Define the destination path (Desktop)
desktop_path = os.path.expanduser("~/Desktop/Nicoya_Systems_Logo.svg")

# 2. The high-fidelity Pulse Node logo code
# This SVG is designed for "Infrastructure Intelligence" branding
logo_svg = """<svg width="1000" height="1000" viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">
  <rect width="400" height="400" fill="#020617"/>

  <path d="M100 120V100H120" stroke="#deff9a" stroke-width="4"/>
  <path d="M280 100H300V120" stroke="#deff9a" stroke-width="4"/>
  <path d="M100 280V300H120" stroke="#deff9a" stroke-width="4"/>
  <path d="M280 300H300V280" stroke="#deff9a" stroke-width="4"/>

  <path d="M150 250V150L250 250V150" stroke="#deff9a" stroke-width="12" stroke-linecap="square"/>

  <circle cx="200" cy="200" r="10" fill="#deff9a">
    <animate attributeName="opacity" values="1;0.4;1" dur="2s" repeatCount="indefinite" />
  </circle>

  <circle cx="150" cy="150" r="4" fill="#deff9a"/>
  <circle cx="250" cy="250" r="4" fill="#deff9a"/>
</svg>"""

# 3. Write the file to the desktop
try:
    with open(desktop_path, "w") as f:
        f.write(logo_svg)
    print(f"Successfully rendered: {desktop_path}")
except Exception as e:
    print(f"Error rendering logo: {e}")