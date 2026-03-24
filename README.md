🏎️ F1 Analysis Tool by Yosef Kristian Bagaskara

👋 About This Project
I'm Yosef, 15 years old, and my dream is to work in Formula 1 engineering one day. 
This is one of my first real Python projects, a terminal-based F1 data analysis tool that lets you look up some session info.
I'm using Claude AI as my coding mentor throughout this project to help me learn because i have no experience at all.

🔍 What It Does
Enter a **year**, **Grand Prix**, **session type**, and **driver code** — and the tool will return:
- 👤 Driver full name, team & car number
- 🏁 Session name, track & date
- ⏱️ Fastest lap time with all 3 sector times
- 🏎️ Tyre compound & tyre age
- 💨 Speed trap result
- 🌤️ Average weather data (air temp, track temp, humidity, wind, rainfall)

⚙️ How To Use
**1. Clone the repo**
```bash
git clone https://github.com/yourusername/f1-analysis-tool.git
cd f1-analysis-tool
```

**2. Install dependencies**
```bash
pip install fastf1
```

**3. Run it**
```bash
python main.py
```

**4. Follow the prompts**
```
========================================
     F1 Analysis Tool - Yosef KB
========================================
Enter the year        : 2024
Enter the Grand Prix  : Monza
Enter the session (FP1/FP2/FP3/Q/R) : R
Enter the driver code : VER

```
🛠️ Built With

| Tool | Purpose |
|------|---------|
| [Python](https://python.org) | Core language |
| [FastF1](https://github.com/theOehrly/Fast-F1) | F1 data API |
| [Claude (Anthropic)](https://claude.ai) | AI mentor / learning assistant |

🗺️ Roadmap
This is just the beginning. Here's what I'm planning to add:
- [ ] Full UI (desktop or web app)
- [ ] Lap time comparison between two drivers
- [ ] Telemetry visualization (speed, throttle, brake)
- [ ] Tyre strategy breakdown across the whole race
- [ ] Qualifying gap analysis
- [ ] Season standings tracker

🙋 Why I Made This
I want to work in F1 one day as an engineer. So i made a small project like this to help me enter F1.

📎 Notes
- Data is sourced from the official **FastF1** library which pulls from the F1 timing API
- First load of a session may take a while — FastF1 caches data after the first fetch
- Some older sessions (pre-2018) may have incomplete data

📬 Contact
Instagram : yk18_b
Tiktok : diegoelwynnn
Gmail : kbagaskara.yosef@gmail.com

Yosef Kristian Bagaskara — 15 y/o, aspiring F1 engineer, Indonesia 🇮🇩
