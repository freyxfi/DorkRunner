

```
                _,.---._                ,--.-.,-.                           .-._        .-._           ,----.               
  _,..---._   ,-.' , -  `.   .-.,.---. /==/- |\  \  .-.,.---.  .--.-. .-.-./==/ \  .-._/==/ \  .-._ ,-.--` , \  .-.,.---.   
/==/,   -  \ /==/_,  ,  - \ /==/  `   \|==|_ `/_ / /==/  `   \/==/ -|/=/  ||==|, \/ /, /==|, \/ /, /==|-  _.-` /==/  `   \  
|==|   _   _\==|   .=.     |==|-, .=., |==| ,   / |==|-, .=., |==| ,||=| -||==|-  \|  ||==|-  \|  ||==|   `.-.|==|-, .=., | 
|==|  .=.   |==|_ : ;=:  - |==|   '='  /==|-  .|  |==|   '='  /==|- | =/  ||==| ,  | -||==| ,  | -/==/_ ,    /|==|   '='  / 
|==|,|   | -|==| , '='     |==|- ,   .'|==| _ , \ |==|- ,   .'|==|,  \/ - ||==| -   _ ||==| -   _ |==|    .-' |==|- ,   .'  
|==|  '='   /\==\ -    ,_ /|==|_  . ,'./==/  '\  ||==|_  . ,'.|==|-   ,   /|==|  /\ , ||==|  /\ , |==|_  ,`-._|==|_  . ,'.  
|==|-,   _`/  '.='. -   .' /==/  /\ ,  )==\ /\=\.'/==/  /\ ,  )==/ , _  .' /==/, | |- |/==/, | |- /==/ ,     //==/  /\ ,  ) 
`-.`.____.'     `--`--''   `--`-`--`--' `--`      `--`-`--`--'`--`..---'   `--`./  `--``--`./  `--`--`-----`` `--`-`--`--'  
```

**Dorkrunner** is an interactive **CLI-based Google & DuckDuckGo dorking automation tool** built for bug bounty hunters, red teamers, and OSINT researchers.

It helps you **generate, customize, filter, log, and launch powerful search engine dorks** against a target domain all from your terminal.

>  Think of it as a *dork engine runner* — fast, modular, and hacker-friendly.

---

## Features

*  **Predefined Advanced Dorks**

  * Subdomain discovery (basic & advanced)
  * Sensitive files & configs
  * Open directories
  * Admin & login panels
  * SQL / PHP error leaks
  * Backup files & logs
  * Git / SVN exposure
  * Open redirects
  * API keys & password exposure
  * GraphQL endpoints
  * Cloud storage leaks (S3, Azure, GCP)

* **Supports Multiple Search Engines**

  * Google
  * DuckDuckGo (DDG)

![main](images/Screenshot%202025-12-28%20192541.png)

*  **Custom Dorks**

  * Add your own dorks dynamically
  * Stored persistently in `custom_dorks.json`

*  **Target-First Workflow**

  * Prompts for target domain
  * Automatically injects it into dorks

*  **Live Filtering**

  * Append filters like:

    * `filetype:pdf`
    * `inurl:admin`
    * `-site:blog.target.com`

*  **One-Click Browser Launch**

  * Instantly open generated dorks in browser

* **Dork Logging**

  * Save generated dorks + URLs to `generated_dorks.log`

*  **Colorized Hacker-Style CLI UI**

  * Clean menus
  * Banner
  * Easy navigation

![result](images/Screenshot%202025-12-28%20192612.png)

---

## Installation

```bash
git clone https://github.com/freyxfi/dorkrunner.git
cd dorkrunner
python3 dorkrunner.py
```

> ✅ Python 3.x required
> ❌ No external dependencies needed

---

## Usage

### Basic Run

```bash
python3 dorkrunner.py
```

### Run With Target

```bash
python3 dorkrunner.py --target example.com
```

---

##  Workflow Overview

1. Enter target domain (e.g. `example.com`)
2. Select search engine (Google / DuckDuckGo)
3. Choose a predefined or custom dork
4. Optionally apply filters
5. View generated dork + search URL
6. Save to log or open directly in browser

---

## Example Dorks Generated

```text
site:*.example.com -site:www.example.com
site:example.com intitle:"index of"
site:example.com ext:env | ext:log | ext:bak
site:example.com inurl:graphql | inurl:graphiql
site:s3.amazonaws.com example.com
```

---

## Custom Dorks

Add your own dorks directly from the CLI.

Example custom dork template:

```text
site:{} intext:"internal use only"
```

Stored in:

```bash
custom_dorks.json
```

---

## Project Structure

```bash
dorkrunner/
├── dorkrunner.py
├── custom_dorks.json
├── generated_dorks.log
└── README.md
```

---

##  Disclaimer

> This tool is intended for **educational purposes and authorized security testing only**.
> Do **NOT** use against targets you don’t own or have explicit permission to test.

You are responsible for how you use this tool.

---

## Contributing

Pull requests are welcome.

Ideas:

* Bing / Brave support
* Export dorks as TXT/Markdown
* Headless mode
* Auto-rotate dorks
* Integration with recon pipelines

---

## Philosophy

> “Recon is not about tools.
> It’s about asking the right questions Dorkrunner helps you ask them faster.”
> also I have taken some ideas from websites :) 

---

## If You Like It

* Star ⭐ the repo
* Fork 🍴 it
* Add your own dorks
* Break things responsibly 😈

---


