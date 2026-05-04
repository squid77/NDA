import base64
from pathlib import Path

# 1. Configuration & Image Processing
desktop = Path.home() / "Desktop"
files = {
    "HERO": desktop / "villa_image.png",
    "V1": desktop / "villa_1.png",
    "V2": desktop / "villa_2.png",
    "V3": desktop / "villa_3.png"
}

data = {}
for key, path in files.items():
    if path.exists():
        data[key] = f"data:image/png;base64,{base64.b64encode(path.read_bytes()).decode()}"
    else:
        # High-quality technical fallback images if locals are missing
        fallbacks = {
            "HERO": "https://images.unsplash.com/photo-1512917774080-9991f1c4c750?q=80&w=2000",
            "V1": "https://images.unsplash.com/photo-1582266255765-fa5cf1a1d501?q=80&w=2000",
            "V2": "https://images.unsplash.com/photo-1518709268805-4e9042af9f23?q=80&w=2000",
            "V3": "https://images.unsplash.com/photo-1590479773265-7464e5d48118?q=80&w=2000"
        }
        data[key] = fallbacks[key]

# 2. The Pulse Node Logo (SVG String)
logo_svg = """
<svg width="40" height="40" viewBox="0 0 400 400" fill="none" xmlns="http://www.w3.org/2000/svg">
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
</svg>
"""

# 3. HTML Blueprint Structure
html_content = f"""
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Nicoya Systems | Infrastructure Command</title>
    <link href="https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&family=Urbanist:wght@400;700;900&display=swap" rel="stylesheet">
    <script src="https://cdn.tailwindcss.com"></script>
    <style>
        :root {{ --accent: #deff9a; --bg: #0a0f1a; }}
        body {{ font-family: 'Urbanist', sans-serif; background-color: var(--bg); color: #f5f5f5; margin: 0; overflow-x: hidden; scroll-behavior: smooth; }}
        .mono {{ font-family: 'Space Mono', monospace; }}
        .grid-layer {{ position: fixed; inset: 0; background-image: radial-gradient(circle at 1px 1px, rgba(222, 255, 154, 0.08) 1px, transparent 0); background-size: 30px 30px; z-index: -1; }}
        .node-panel {{ border: 1px solid rgba(222, 255, 154, 0.1); background: rgba(10, 15, 26, 0.85); backdrop-filter: blur(20px); position: relative; }}
        .node-panel::before {{ content: ''; position: absolute; top: -1px; left: -1px; width: 15px; height: 15px; border-top: 2px solid var(--accent); border-left: 2px solid var(--accent); }}
        .node-panel::after {{ content: ''; position: absolute; bottom: -1px; right: -1px; width: 15px; height: 15px; border-bottom: 2px solid var(--accent); border-right: 2px solid var(--accent); }}
        @keyframes sweep {{ from {{ transform: rotate(0deg); }} to {{ transform: rotate(360deg); }} }}
        .active-signal {{ position: absolute; width: 300%; height: 300%; background: conic-gradient(from 0deg, transparent 0%, rgba(222, 255, 154, 0.08) 5%, transparent 15%); top: -100%; left: -100%; animation: sweep 12s linear infinite; pointer-events: none; }}
        .asset-container {{ position: relative; background: #000; overflow: hidden; border: 1px solid rgba(255,255,255,0.05); }}
        .asset-container img {{ width: 100%; height: 100%; object-fit: cover; opacity: 0.6; filter: grayscale(0.5) contrast(1.2); transition: 0.8s cubic-bezier(0.16, 1, 0.3, 1); }}
        .asset-container:hover img {{ opacity: 1; filter: grayscale(0) contrast(1.1); transform: scale(1.04); }}
        @keyframes scanning {{ 0% {{ top: 0%; }} 100% {{ top: 100%; }} }}
        .scan-beam {{ position: absolute; width: 100%; height: 2px; background: var(--accent); box-shadow: 0 0 15px var(--accent); animation: scanning 5s linear infinite; z-index: 10; opacity: 0.3; }}
        .hud-label {{ font-size: 9px; letter-spacing: 0.2em; text-transform: uppercase; color: rgba(255,255,255,0.4); font-family: 'Space Mono', monospace; }}
        .hud-data {{ font-size: 11px; font-weight: bold; color: var(--accent); font-family: 'Space Mono', monospace; }}
    </style>
</head>
<body>
    <div class="grid-layer"></div>

    <div class="fixed top-0 left-0 w-full z-[100] bg-black/95 border-b border-white/10 px-8 py-3 flex justify-between items-center mono text-[9px] tracking-[0.4em]">
        <div class="flex items-center gap-6">
            <div class="flex items-center gap-2 text-[#deff9a]">
                <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" class="animate-pulse"><path d="M22 12h-4l-3 9L9 3l-3 9H2"/></svg>
                <span class="font-bold uppercase italic">Telemetry_Integrity: Locked</span>
            </div>
            <span class="opacity-10">||</span>
            <span class="opacity-30">NODE_COUNT: 04</span>
        </div>
        <div class="flex items-center gap-8 text-white/40">
            <span id="utc-time">00:00:00 UTC</span>
            <span class="border border-[#deff9a]/30 px-2 text-[#deff9a]">ACTIVE_GOVERNANCE</span>
        </div>
    </div>

    <nav class="w-full bg-black/40 border-b border-white/5 relative z-50 mt-12">
        <div class="max-w-7xl mx-auto px-10 h-24 flex items-center justify-between">
            <div class="flex items-center gap-4">
                <div class="bg-[#deff9a] p-1 rounded-sm text-black shadow-[0_0_15px_rgba(222,255,154,0.4)]">
                    {logo_svg}
                </div>
                <span class="text-2xl font-black tracking-tighter uppercase italic">Nicoya <span class="text-white/20 font-medium">Systems</span></span>
            </div>
            <button class="bg-[#deff9a]/10 border border-[#deff9a] text-[#deff9a] px-8 py-4 text-[10px] font-bold uppercase tracking-[0.2em] hover:bg-[#deff9a] hover:text-black transition-all">
                Audit Registry
            </button>
        </div>
    </nav>

    <section class="max-w-7xl mx-auto px-6 py-20 lg:py-32">
        <div class="node-panel p-12 lg:p-20 grid grid-cols-1 lg:grid-cols-2 gap-20 items-center overflow-hidden">
            <div class="active-signal"></div>
            <div class="relative z-10">
                <div class="hud-label mb-10">Infrastructure // Strategy_Briefing</div>
                <h1 class="text-7xl lg:text-[7.5rem] font-black italic uppercase leading-[0.8] tracking-tighter mb-12">
                    Hardened <br><span class="text-[#deff9a]">Nodes.</span>
                </h1>
                <p class="text-white/40 text-[11px] leading-relaxed max-w-sm mb-12 uppercase tracking-[0.05em]">
                    Applying high-fidelity telemetry to negate environmental volatility. Our OS transitions luxury assets into stable infrastructure nodes through automated governance.
                </p>
                <div class="flex gap-4">
                    <button class="bg-[#deff9a] text-black px-12 py-6 text-[11px] font-black uppercase tracking-[0.2em] shadow-2xl shadow-green-900/40 hover:bg-white transition-all">
                        Initialize Asset Scan
                    </button>
                </div>
            </div>
            <div class="asset-container h-[500px] border border-white/10">
                <div class="scan-beam"></div>
                <img src="{data['HERO']}" alt="Core Node">
                <div class="absolute bottom-8 left-8 bg-black/95 p-4 border border-white/10 mono text-[9px] tracking-[0.2em] text-white/40">
                    LAT: 9.6415° N <br> LONG: 85.1667° W <br> STATUS: ACTIVE_SYNC
                </div>
            </div>
        </div>
    </section>

    <section class="max-w-7xl mx-auto px-6 pb-40 space-y-40">
        <div class="flex justify-between items-end border-b border-white/10 pb-12">
            <div>
                <h2 class="text-6xl font-black italic uppercase tracking-tighter">Distributed <span class="text-[#deff9a]">Registry</span></h2>
                <p class="hud-label mt-5">Asset_Feed // Real_Time_Hardening</p>
            </div>
            <div class="text-right mono">
                <span class="text-5xl font-black text-[#deff9a]">03</span><span class="text-white/20 text-xl"> / 20</span>
            </div>
        </div>

        <div class="grid grid-cols-1 lg:grid-cols-12 gap-16 items-center">
            <div class="lg:col-span-7 h-[450px] asset-container">
                <div class="scan-beam"></div>
                <img src="{data['V1']}" alt="Node 01">
            </div>
            <div class="lg:col-span-5 space-y-10">
                <div>
                    <span class="hud-label tracking-[0.5em]">Node_ID: ST-01</span>
                    <h3 class="text-4xl font-black italic uppercase mt-3 tracking-tighter italic">Structural Monolith</h3>
                </div>
                <div class="grid grid-cols-2 gap-4">
                    <div class="bg-white/5 p-6 border-l-2 border-[#deff9a]">
                        <div class="hud-label mb-2">Salt Index</div>
                        <div class="hud-data text-red-500 italic">CRITICAL</div>
                    </div>
                    <div class="bg-white/5 p-6 border-l-2 border-[#deff9a]">
                        <div class="hud-label mb-2">Status</div>
                        <div class="hud-data italic">NOMINAL</div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <footer class="py-20 text-center border-t border-white/5">
        <div class="mono text-[9px] text-white/20 tracking-[1.2em] uppercase">End of Transmission // Infrastructure Intelligence Hub</div>
    </footer>

    <script>
        function updateTime() {{
            const now = new Date();
            document.getElementById('utc-time').innerText = now.toISOString().split('T')[1].split('.')[0] + ' UTC';
        }}
        setInterval(updateTime, 1000);
        updateTime();
    </script>
</body>
</html>
"""

# 4. Save Final File
(desktop / "Nicoya_Systems_V10_Intelligence.html").write_text(html_content)
print("V10 Pure Governance Interface Compiled on Desktop.")