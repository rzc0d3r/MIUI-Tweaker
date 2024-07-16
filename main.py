VERSION = 'v2.0.0.1'

from modules.android_api import *
from modules.locales import *

remove_list = [ # these applications will be removed by any means possible
    # Google
    'com.google.android.calendar' # Calendar (Trash)
    'com.google.android.tts', # TextToSpeech Engine
    'com.google.android.googlequicksearchbox', # Google App
    'com.google.android.music', # Play Music (Trash)
    'com.google.android.videos', # Play Films (Trash)
    'com.google.android.marvin.talkback', # Talkback
    'com.google.android.cellbroadcastreceiver', # Cell Broadcast Receiver
    'com.google.android.projection.gearhead', # Android Auto (Trash)
    'com.google.android.ims', # Carrier Services (Trash)
    'com.google.android.apps.tachyon', # Parody of Zoom (Trash)
    'com.google.android.apps.subscriptions.red', # Google One (Trash)
    'com.google.android.apps.docs', # Google Disk
    'com.google.android.apps.maps', # Google Maps
    'com.google.android.apps.googleassistant', # Google Assistant (Trash)
    'com.google.android.apps.wellbeing', # Digital wellbeing (Trash)
    'com.google.android.apps.turbo' # Device Health Services (Trash)

    # Xiaomi
    'com.xiaomi.discover', # Component Update (Trash)
    'com.xiaomi.glgm', # Games and reviews (Trash)
    'com.xiaomi.mipicks', # Google Play parody (Trash)
    'com.xiaomi.joyose', # Advertising and tracking (Trash)
    'com.android.browser', # Browser (Trash)
    'com.android.email', # Email (Trash)
    'com.android.stk', # SIM Menu (Trash)
    'com.android.htmlviewer', # HTML viewer (Trash)
    'com.huaqin.diaglogger', # System Logging 
    'com.goodix.gftest', # Fingerprint test (Trash)
    'com.huaqin.sarcontroller', # idk (MIUI works without it)

    # MIUI
    'com.miui.misound', # Equalizer (Trash)
    'com.miui.phrase', # Keyboard User-Dictionary Module (Trash)
    'com.miui.fm', # Radio
    'com.miui.miservice', # Support (Trash)
    'com.miui.videoplayer', # Video player
    'com.miui.cleanmaster', # Cleanup (Trash)
    'com.miui.player', # Music (Trash)
    'com.miui.msa.global', # Advertising and tracking (Trash)
    'com.miui.hybrid.accessory', # (Trash)
    'com.miui.touchassistant', # (Trash)
    'com.miui.yellowpage', # (Trash)
    'com.miui.global.packageinstaller', # MIUI Apk installer parody (Trash) 
    'com.miui.analytics', # Advertising and tracking (Trash) 
    'com.miui.android.fashiongallery', # Live Wallpaper on Lockscreen (Trash) 
    'com.miui.android.personalassistant', # (Trash)
    'com.miui.bugreport', # MIUI Bug Reporting (Trash)
    'com.miui.weather2', # MIUI Weather (Trash)
    'com.miui.hybrid', # (Trash)
    'com.mi.globalTrendNews', # News Feed (Trash)
    'com.mipay.wallet.id', # Get Money (For Ukraine - Trash)
    'com.mipay.wallet.in', # Send money (For Ukraine - Trash)
    'com.miui.cit', # Test Phone (Trash)

    # Other
    'com.mediatek.location.lppe.main', # LPPe protocol (Uninstalled and the system worked + still eats a lot of memory)
    'com.facebook.system', # Part of Facebook App (Trash)
    'com.facebook.appmanager', # Part of Facebook App (Trash)
    'com.facebook.services', # Part of Facebook App (Trash)
    'com.netflix.partner.activation', # Netflix activation (Trash)
]

google_list = [ # these applications will be turned on and off in steps 3 and 2
    'com.google.android.gms',
    'com.android.vending',
    'com.google.android.gsf',
    'com.google.ar.core',
    'com.google.android.ims',
    'com.google.android.gm',
    'com.google.android.cellbroadcastreceiver',
    'com.android.providers.userdictionary',
    'com.google.android.googlequicksearchbox',
    'com.google.android.apps.subscriptions.red',
    'com.google.android.apps.tachyon',
    'com.google.android.apps.docs',
    'com.google.android.apps.maps',
    'com.google.android.apps.googleassistant',
    'com.google.android.onetimeinitializer',
    'com.google.android.configupdater',
    'com.google.android.apps.wellbeing',
    'com.google.android.projection.gearhead',
    'com.google.android.apps.turbo'
]

google_gms = [ # these applications will be turned on and off in step 5
    'com.android.vending',
    'com.google.ar.core',
    'com.google.android.ims',
    'com.google.android.onetimeinitializer',
    'com.google.android.apps.googleassistant',
    'com.google.android.googlequicksearchbox',
    'com.google.android.apps.subscriptions.red',
    'com.google.android.apps.tachyon',
    'com.google.android.apps.docs',
    'com.google.android.apps.maps',
    'com.google.android.gm',
    'com.google.android.apps.walletnfcrel',
    'com.google.android.calendar',
    'com.google.android.youtube',
    'com.google.android.projection.gearhead',
    'com.google.android.apps.wellbeing',
    'com.google.android.apps.turbo'
]

xiaomi_list = [ # these applications will be turned on and off in steps 7 and 6 
    'com.miui.cloudbackup',
    'com.miui.vsimcore',
    'com.duokan.phone.remotecontroller',
    'com.xiaomi.xmsfkeeper'
    'com.miui.cloudservice.sysbase',
    'com.miui.micloudsync',
    'com.xiaomi.xmsf',
    'com.xiaomi.joyose',
    'com.miui.hybrid',
    'com.mi.globalbrowser',
    'com.xiaomi.mirecycle',
    'com.miui.virtualsim',
    'com.miui.enbbs',
    'com.xiaomi.mipicks',
    'com.miui.userguide',
    'com.miui.msa.global',
    'com.xiaomi.midrop',
    'com.miui.bugreport',
    'com.miui.analytics',
    'com.xiaomi.payment',
    'com.xiaomi.glgm',
    'com.miui.cloudservice',
    'com.miui.micloudsync',
    'com.miui.backup',
    'com.xiaomi.simactivate.service',
    'com.miui.mishare.connectivity',
    'com.xiaomi.account',
    'com.milink.service',
    'com.huaqin.diaglogger',
    'com.huaqin.pocketbanreceiver',
    'com.xiaomi.mi_connect_service',
    'com.android.thememanager',
    'com.miui.screenrecorder',
    'com.miui.misound',
    'com.goodix.gftest',
    'com.miui.miservice',
    'com.miui.phrase'
]

def logo():
    name = f'MIUI Tweaker {VERSION} by rzc0d3r'
    print(name)
    print('--------------------------------')
    print()

LOCALE = EN_LOCALE()
if get_system_locale() in ['ru-RU', 'uk-UA']:
    LOCALE = RU_LOCALE

def menu():
    while True:
        print(LOCALE.menu_choose_action[0])
        print(f'    {LOCALE.menu_general[0]}')
        print(f'        0 - {LOCALE.menu_action_exit[0]}')
        print('    Google:')
        print(f'        2 - {LOCALE.menu_action_stop_google_apps[0]}')
        print(f'        3 - {LOCALE.menu_action_run_google_apps[0]}')
        print(f'        4 - {LOCALE.menu_action_kill_cellbroadcast[0]}')
        print(f'        5 - {LOCALE.menu_action_enable_only_gms_mode[0]}')
        print('    MIUI:')
        print(f'        1 - {LOCALE.menu_action_remove_miui_trash_apps[0]}')
        print(f'        6 - {LOCALE.menu_action_stop_xiaomi_trash_apps[0]}')
        print(f'        7 - {LOCALE.menu_action_run_xiaomi_trash_apps[0]}')
        print(f'        8 - {LOCALE.menu_action_run_systemui_boost[0]}')
        print(f'        9 - {LOCALE.menu_action_run_force_dexopt[0]}')
        print()
        code = input(': ').strip().upper()
        if code in '0123456789' and code != '':
            return code
        else:
            cls()
            logo()

cls()
logo()

su = init_SU()
if not su:
    print(LOCALE.need_root[0])
    exit(-1)

while True:
    cls()
    logo()
    code = menu() 
    print()
    
    if code == '0':
        print(LOCALE.goodbye[0])
        break

    elif code == '1': # uninstall trash apps
        for app in remove_list:
            print(LOCALE.uninstalling[0]+app)
            pm_uninstall_user(app, True)

    elif code == '2': # disable Google apps
        for app in google_list:
            kill_app(app)
            print(LOCALE.disabling[0]+app)
            pm_disable(app)
    
    elif code == '3': # enable Google apps
        for app in google_list:
            print(LOCALE.enabling[0]+app)
            pm_enable(app)

    elif code == '4': # disable cellbroadcast
        kill_app('com.google.android.cellbroadcastreceiver')
        print(f'{LOCALE.disabling[0]}com.google.android.cellbroadcastreceiver')
        pm_disable('com.google.android.cellbroadcastreceiver')

    elif code == '5': # enable only gms mode
        for app in google_gms:
            kill_app(app)
            print(LOCALE.disabling[0]+app)
            pm_disable(app)
        print('Врубаю com.google.android.gms')
        pm_enable('com.google.android.gms')

    elif code == '6': # disable Xiaomi apps
        for app in xiaomi_list:
            kill_app(app)
            print(LOCALE.disabling[0]+app)
            pm_disable(app)
    
    elif code == '7': # enable Xiaomi apps
        for app in xiaomi_list:
            print(LOCALE.enabling[0]+app)
            pm_enable(app)
    
    elif code == '8': # systemui boost
        print(LOCALE.systemui_boosting[0])
        kill_app('com.android.systemui')
    
    elif code == '9': # run force dexopt
        print(LOCALE.time_warning[0])
        apps = get_all_apps()
        print(f'{LOCALE.will_be_optimized[0]} {str(len(apps))} {LOCALE.apps[0]}')
        mode = input(LOCALE.begin[0]).strip().lower()
        if mode == 'да':
            mode2 = input(f'\n{LOCALE.enable_manual_process_control[0]}').strip().lower()
            print(f'\n{LOCALE.beginning[0]}\n')          
            for app in apps:
                print(LOCALE.optimiziting[0]+app)
                opt_app(app)
                print(LOCALE.optimization_complete[0])
                if mode2 == LOCALE.yes:
                    mode = input(LOCALE.optimization_continue[0]).strip().lower()
                    if mode == LOCALE.no:
                        break
                print()
    
    if code in '123456789':
        input(f'\n{LOCALE.done[0]}')