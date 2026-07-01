import subprocess

chrome = r"C:\Program Files\Google\Chrome\Application\chrome.exe"

def help_menu():
    print("""
==================== HELP ====================

Search & AI
-----------
gg         Google
yt         YouTube
chat       ChatGPT
gemini     Google Gemini
claude     Claude AI
perplex    Perplexity

Social Media
------------
yt         YouTube
ig         Instagram
fb         Facebook
x          X (Twitter)
reddit     Reddit
threads    Threads
discord    Discord
snap       Snapchat
pin        Pinterest

Communication
-------------
what       WhatsApp Web
mail       Gmail
outlook    Outlook
meet       Google Meet
zoom       Zoom

Entertainment
-------------
netflix    Netflix
prime      Prime Video
hotstar    Disney+ Hotstar
spotify    Spotify
music      YouTube Music

Coding
------
gh         GitHub
gl         GitLab
so         Stack Overflow
pypi       PyPI
docs       Python Documentation

Productivity
------------
drive      Google Drive
docsg      Google Docs
sheet      Google Sheets
slides     Google Slides
cal        Google Calendar
keep       Google Keep

Shopping
--------
amazon     Amazon India
flip       Flipkart

Learning
--------
wiki       Wikipedia
coursera   Coursera
udemy      Udemy
khan       Khan Academy

Misc
----
maps       Google Maps
news       Google News
translate  Google Translate
weather    Weather

Other
-----
help       Show this help menu
stop       Exit the program

==============================================
""")

commands = {
    # Search & AI
    "gg": "https://google.com",
    "yt": "https://youtube.com",
    "chat": "https://chatgpt.com",
    "gemini": "https://gemini.google.com",
    "claude": "https://claude.ai",
    "perplex": "https://perplexity.ai",

    # Social Media
    "ig": "https://instagram.com",
    "fb": "https://facebook.com",
    "x": "https://x.com",
    "reddit": "https://reddit.com",
    "threads": "https://threads.net",
    "discord": "https://discord.com/app",
    "snap": "https://snapchat.com",
    "pin": "https://pinterest.com",

    # Communication
    "what": "https://web.whatsapp.com",
    "mail": "https://mail.google.com",
    "outlook": "https://outlook.live.com",
    "meet": "https://meet.google.com",
    "zoom": "https://zoom.us",

    # Entertainment
    "netflix": "https://netflix.com",
    "prime": "https://primevideo.com",
    "hotstar": "https://hotstar.com",
    "spotify": "https://spotify.com",
    "music": "https://music.youtube.com",

    # Coding
    "gh": "https://github.com",
    "gl": "https://gitlab.com",
    "so": "https://stackoverflow.com",
    "pypi": "https://pypi.org",
    "docs": "https://docs.python.org/3/",

    # Productivity
    "drive": "https://drive.google.com",
    "docsg": "https://docs.google.com",
    "sheet": "https://sheets.google.com",
    "slides": "https://slides.google.com",
    "cal": "https://calendar.google.com",
    "keep": "https://keep.google.com",

    # Shopping
    "amazon": "https://amazon.in",
    "flip": "https://flipkart.com",

    # Learning
    "wiki": "https://wikipedia.org",
    "coursera": "https://coursera.org",
    "udemy": "https://udemy.com",
    "khan": "https://khanacademy.org",

    # Misc
    "maps": "https://maps.google.com",
    "news": "https://news.google.com",
    "translate": "https://translate.google.com",
    "weather": "https://weather.com",
}

print("-"*70)
print("BROWSER-SHELL: A SCRIPT THAT AUTOMATE YOUR WEB SEARCHES.")
print("-"*70)

while True:

    in_command = input("Enter the command: ")

    if in_command == "stop":
        break

    elif in_command == "help":
        help_menu()

    else:
        subprocess.Popen([chrome, commands[in_command]])
