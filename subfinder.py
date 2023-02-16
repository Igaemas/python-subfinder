import requests
import sys

print('''\
========================================================================
    ''')
print('''\
  ██████  █    ██  ▄▄▄▄     █████▒██▓ ███▄    █ ▓█████▄ ▓█████  ██▀███
▒██    ▒  ██  ▓██▒▓█████▄ ▓██   ▒▓██▒ ██ ▀█   █ ▒██▀ ██▌▓█   ▀ ▓██ ▒ ██▒
░ ▓██▄   ▓██  ▒██░▒██▒ ▄██▒████ ░▒██▒▓██  ▀█ ██▒░██   █▌▒███   ▓██ ░▄█ ▒
  ▒   ██▒▓▓█  ░██░▒██░█▀  ░▓█▒  ░░██░▓██▒  ▐▌██▒░▓█▄   ▌▒▓█  ▄ ▒██▀▀█▄
▒██████▒▒▒▒█████▓ ░▓█  ▀█▓░▒█░   ░██░▒██░   ▓██░░▒████▓ ░▒████▒░██▓ ▒██▒
▒ ▒▓▒ ▒ ░░▒▓▒ ▒ ▒ ░▒▓███▀▒ ▒ ░   ░▓  ░ ▒░   ▒ ▒  ▒▒▓  ▒ ░░ ▒░ ░░ ▒▓ ░▒▓░
░ ░▒  ░ ░░░▒░ ░ ░ ▒░▒   ░  ░      ▒ ░░ ░░   ░ ▒░ ░ ▒  ▒  ░ ░  ░  ░▒ ░ ▒░
░  ░  ░   ░░░ ░ ░  ░    ░  ░ ░    ▒ ░   ░   ░ ░  ░ ░  ░    ░     ░░   ░
      ░     ░      ░              ░           ░    ░       ░  ░   ░
                        ░                        ░
        ''')

print('''\
========================================================================
        ''')

class colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    RESET = '\033[0m'

wordlist = sys.argv[2]
main_domain = sys.argv[1]

def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    # caracter = ALT + 219
    bar = '█' * int(percent) + ' ' * (100 - int(percent))
    print(f"\r|{bar}| {percent:2f}%", end="\r")

sub_list = open(wordlist).read()
subdoms = sub_list.splitlines()
progress_int = 0
sub_number = len(subdoms) 
valid_domain_list = []

for sub in subdoms:
    progress_int += 1
    sub_domain = f"http://{sub}.{main_domain}"

    if len(sys.argv) > 3:
        pass
    else:
        progress_bar(progress_int, sub_number)

    try:
        requests.get(sub_domain)

    except requests.ConnectionError:
        if len(sys.argv) > 3 :
            if sys.argv[3] == '-v':
                print(colors.RED + f'({progress_int}/{sub_number}) : {sub_domain} isnt Valid' + colors.RESET)
            pass
        else:
            pass
    else:
        if len(sys.argv) > 3 :
            if sys.argv[3] == '-v':
                print(colors.GREEN + f'({progress_int}/{sub_number}) : {sub_domain} is Valid' + colors.RESET)
        valid_domain_list.append(sub_domain)

if len(valid_domain_list) == 0:
    print("no valid domain found")
else:
    print(f'There are {len(valid_domain_list)} valid sub domain: ')
    for valid_domain in valid_domain_list:
        print('   ' + valid_domain)
