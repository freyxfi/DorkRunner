import argparse
import webbrowser
import sys
import os
import json


class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'

BANNER = f"""
{Colors.OKGREEN}
                _,.---._                ,--.-.,-.                           .-._        .-._           ,----.               
  _,..---._   ,-.' , -  `.   .-.,.---. /==/- |\  \  .-.,.---.  .--.-. .-.-./==/ \  .-._/==/ \  .-._ ,-.--` , \  .-.,.---.   
/==/,   -  \ /==/_,  ,  - \ /==/  `   \|==|_ `/_ / /==/  `   \/==/ -|/=/  ||==|, \/ /, /==|, \/ /, /==|-  _.-` /==/  `   \  
|==|   _   _\==|   .=.     |==|-, .=., |==| ,   / |==|-, .=., |==| ,||=| -||==|-  \|  ||==|-  \|  ||==|   `.-.|==|-, .=., | 
|==|  .=.   |==|_ : ;=:  - |==|   '='  /==|-  .|  |==|   '='  /==|- | =/  ||==| ,  | -||==| ,  | -/==/_ ,    /|==|   '='  / 
|==|,|   | -|==| , '='     |==|- ,   .'|==| _ , \ |==|- ,   .'|==|,  \/ - ||==| -   _ ||==| -   _ |==|    .-' |==|- ,   .'  
|==|  '='   /\==\ -    ,_ /|==|_  . ,'./==/  '\  ||==|_  . ,'.|==|-   ,   /|==|  /\ , ||==|  /\ , |==|_  ,`-._|==|_  . ,'.  
|==|-,   _`/  '.='. -   .' /==/  /\ ,  )==\ /\=\.'/==/  /\ ,  )==/ , _  .' /==/, | |- |/==/, | |- /==/ ,     //==/  /\ ,  ) 
`-.`.____.'     `--`--''   `--`-`--`--' `--`      `--`-`--`--'`--`..---'   `--`./  `--``--`./  `--`--`-----`` `--`-`--`--'                                                                                            
{Colors.ENDC}
"""

# hey if you are reading this you can add your cool dorks from the custom add option :) 
PREDEFINED_DORKS = {
    'google': {
        'subdomains_basic': 'site:*.{} -site:www.{}',
        'subdomains_advanced': 'site:*.*.{} -site:www.{}',
        'sensitive_files': 'site:{} (ext:pdf | ext:xls | ext:doc | ext:txt) intext:"confidential" | intext:"password"',
        'open_directories': 'site:{} intitle:"index of"',
        'admin_pages': 'site:{} inurl:admin | inurl:login | inurl:dashboard',
        'error_messages': 'site:{} intext:"error" | intext:"warning" | intext:"sql syntax"',
        'exposed_databases': 'site:{} ext:sql | ext:bak | ext:mdb',
        'vulnerable_params': 'site:{} inurl:?id= | inurl:&id= | inurl:php?id=',
        'exposed_configs': 'site:{} ext:xml | ext:conf | ext:cnf | ext:reg | ext:inf | ext:rdp | ext:cfg | ext:txt | ext:ora | ext:ini',
        'exposed_logs': 'site:{} ext:log',
        'backup_files': 'site:{} ext:bkf | ext:bkp | ext:bak | ext:old | ext:backup',
        'sql_errors': 'site:{} intext:"sql syntax" | intext:"mysql dump" | intext:"Error Executing Database Query"',
        'php_errors': 'site:{} intext:"PHP Parse error" | intext:"PHP Warning" | intext:"PHP Error"',
        'exposed_git': 'site:{} inurl:.git',
        'exposed_svn': 'site:{} inurl:.svn/entries',
        'open_redirects': 'site:{} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http',
        'api_keys': 'site:{} intext:"api_key" | intext:"apikey" | intext:"api key"',
        'password_exposure': 'site:{} intext:"password" filetype:txt',
        'email_exposure': 'site:{} intext:"@{}"',
        'cache_pages': 'cache:{}',
        'related_sites': 'related:{}',
        'juicy_files': 'site:{} ext:swf | ext:csv | ext:xml | ext:json | ext:sql',
        'graphql_endpoints': 'site:{} inurl:graphql | inurl:graphiql',
        's3_buckets': 'site:s3.amazonaws.com intext:{}',
        'cloud_storage': 'site:{} inurl:blob.core.windows.net | inurl:storage.googleapis.com',
    },
    'ddg': {
        'subdomains_basic': 'site:*.{} -site:www.{}',
        'subdomains_advanced': 'site:*.*.{} -site:www.{}',
        'sensitive_files': 'site:{} (filetype:pdf | filetype:xls | filetype:doc | filetype:txt) "confidential" | "password"',
        'open_directories': 'site:{} intitle:"index of"',
        'admin_pages': 'site:{} inurl:admin | inurl:login | inurl:dashboard',
        'error_messages': 'site:{} "error" | "warning" | "sql syntax"',
        'exposed_databases': 'site:{} filetype:sql | filetype:bak | filetype:mdb',
        'vulnerable_params': 'site:{} inurl:?id= | inurl:&id= | inurl:php?id=',
        'exposed_configs': 'site:{} filetype:xml | filetype:conf | filetype:cnf | filetype:reg | filetype:inf | filetype:rdp | filetype:cfg | filetype:txt | filetype:ora | filetype:ini',
        'exposed_logs': 'site:{} filetype:log',
        'backup_files': 'site:{} filetype:bkf | filetype:bkp | filetype:bak | filetype:old | filetype:backup',
        'sql_errors': 'site:{} "sql syntax" | "mysql dump" | "Error Executing Database Query"',
        'php_errors': 'site:{} "PHP Parse error" | "PHP Warning" | "PHP Error"',
        'exposed_git': 'site:{} inurl:.git',
        'exposed_svn': 'site:{} inurl:.svn/entries',
        'open_redirects': 'site:{} inurl:redir | inurl:url | inurl:redirect | inurl:return | inurl:src=http | inurl:r=http',
        'api_keys': 'site:{} "api_key" | "apikey" | "api key"',
        'password_exposure': 'site:{} "password" filetype:txt',
        'email_exposure': 'site:{} "@{}"',
        'cache_pages': 'cache:{}',
        'related_sites': 'related:{}',
        'juicy_files': 'site:{} filetype:swf | filetype:csv | filetype:xml | filetype:json | filetype:sql',
        'graphql_endpoints': 'site:{} inurl:graphql | inurl:graphiql',
        's3_buckets': 'site:s3.amazonaws.com "{}"',
        'cloud_storage': 'site:{} inurl:blob.core.windows.net | inurl:storage.googleapis.com',
    }
}

CUSTOM_DORKS_FILE = 'custom_dorks.json'

# File to save generated dorks log
GENERATED_DORKS_LOG = 'generated_dorks.log'

def load_custom_dorks():
    if os.path.exists(CUSTOM_DORKS_FILE):
        with open(CUSTOM_DORKS_FILE, 'r') as f:
            return json.load(f)
    return {'google': {}, 'ddg': {}}

def save_custom_dorks(custom_dorks):
    with open(CUSTOM_DORKS_FILE, 'w') as f:
        json.dump(custom_dorks, f, indent=4)

def log_generated_dork(engine, dork, search_url):
    with open(GENERATED_DORKS_LOG, 'a') as f:
        f.write(f"[{engine.upper()}] Dork: {dork}\nURL: {search_url}\n\n")
    print(f"{Colors.OKBLUE}Generated dork saved to {GENERATED_DORKS_LOG}!{Colors.ENDC}")

def print_menu(options, title):
    print(f"{Colors.HEADER}{Colors.BOLD}{title}{Colors.ENDC}")
    for idx, option in enumerate(options, 1):
        print(f"{Colors.OKBLUE}{idx}. {option}{Colors.ENDC}")
    print(f"{Colors.OKBLUE}0. Back/Exit{Colors.ENDC}")

def get_user_choice(max_choice):
    while True:
        try:
            choice = int(input(f"{Colors.OKGREEN}Enter your choice: {Colors.ENDC}"))
            if 0 <= choice <= max_choice:
                return choice
            else:
                print(f"{Colors.FAIL}Invalid choice. Please try again.{Colors.ENDC}")
        except ValueError:
            print(f"{Colors.FAIL}Please enter a number.{Colors.ENDC}")

def generate_dork(engine, category, target):
    dork_template = PREDEFINED_DORKS[engine].get(category)
    if dork_template:
        if '{}' in dork_template and '{}' in dork_template[1:]:
            return dork_template.format(target, target)
        else:
            return dork_template.format(target)
    return None

def add_custom_dork(custom_dorks, engine):
    name = input(f"{Colors.OKGREEN}Enter a name for your custom dork: {Colors.ENDC}")
    dork = input(f"{Colors.OKGREEN}Enter the dork template (use {{}} for target): {Colors.ENDC}")
    custom_dorks[engine][name] = dork
    save_custom_dorks(custom_dorks)
    print(f"{Colors.OKBLUE}Custom dork added successfully!{Colors.ENDC}")

def apply_filters(dork):
    print(f"{Colors.HEADER}Apply additional filters (optional):{Colors.ENDC}")
    print("Examples: filetype:pdf, inurl:admin, -site:blog, etc.")
    filter_str = input(f"{Colors.OKGREEN}Enter filters (space-separated, or leave blank): {Colors.ENDC}")
    if filter_str:
        dork += ' ' + filter_str
    return dork

def main():
    parser = argparse.ArgumentParser(description="Dorkrunner - CLI for Google and DuckDuckGo Dorking")
    parser.add_argument('--target', help="Target domain (e.g., example.com)")
    args = parser.parse_args()

    print(BANNER)

    target = args.target
    if not target:
        target = input(f"{Colors.OKGREEN}Enter the target domain (e.g., example.com): {Colors.ENDC}")

    custom_dorks = load_custom_dorks()

    while True:
        print("\n" + "=" * 50)
        print(f"{Colors.HEADER}{Colors.BOLD}Dorkrunner - Target: {target}{Colors.ENDC}")
        print("=" * 50 + "\n")

        main_options = ["Select Search Engine", "Add Custom Dork", "Exit"]
        print_menu(main_options, "Main Menu:")

        choice = get_user_choice(len(main_options))

        if choice == 0 or choice == 3:
            print(f"{Colors.OKBLUE}Exiting... Happy hunting!{Colors.ENDC}")
            sys.exit(0)
        elif choice == 1:
            engine_options = ["Google", "DuckDuckGo"]
            print_menu(engine_options, "Select Search Engine:")
            engine_choice = get_user_choice(len(engine_options))
            if engine_choice == 0:
                continue
            engine = 'google' if engine_choice == 1 else 'ddg'
            base_url = 'https://www.google.com/search?q=' if engine == 'google' else 'https://duckduckgo.com/?q='

            while True:
                categories = list(PREDEFINED_DORKS[engine].keys()) + list(custom_dorks[engine].keys())
                print_menu(categories, f"{engine.capitalize()} Dorks:")
                cat_choice = get_user_choice(len(categories))
                if cat_choice == 0:
                    break

                category = categories[cat_choice - 1]
                if category in PREDEFINED_DORKS[engine]:
                    dork = generate_dork(engine, category, target)
                else:
                    dork = custom_dorks[engine][category].format(target)

                dork = apply_filters(dork)
                full_query = dork.replace(' ', '+')  
                search_url = base_url + full_query

                print(f"{Colors.OKBLUE}Generated Dork: {dork}{Colors.ENDC}")
                print(f"{Colors.OKBLUE}Search URL: {search_url}{Colors.ENDC}")

                save_log = input(f"{Colors.OKGREEN}Save this dork to log? (y/n): {Colors.ENDC}").lower() == 'y'
                if save_log:
                    log_generated_dork(engine, dork, search_url)

                open_browser = input(f"{Colors.OKGREEN}Open in browser? (y/n): {Colors.ENDC}").lower() == 'y'
                if open_browser:
                    webbrowser.open(search_url)
        elif choice == 2:
            engine_options = ["Google", "DuckDuckGo"]
            print_menu(engine_options, "Select Engine for Custom Dork:")
            engine_choice = get_user_choice(len(engine_options))
            if engine_choice == 0:
                continue
            engine = 'google' if engine_choice == 1 else 'ddg'
            add_custom_dork(custom_dorks, engine)

if __name__ == "__main__":
    main()
