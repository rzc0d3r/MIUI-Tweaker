from os import system, remove
from shutil import rmtree
from subprocess import run, PIPE

def init_SU():
    try:
        f = open('/data/null', 'w')
        f.close()
        remove('/data/null')
        return True
    except:
        return False
        
def remove_dir(path):
    try:
        rmtree(path)
        return True
    except:
        return False

def remove_file(path):
    try:
        remove(path)
        return True
    except:
        return False

def pm_uninstall_user(package, all=False):
    if all:
        rcode = system(f'pm uninstall --user 0 {package} > /dev/null 2>&1')
    else:
        rcode = system(f'pm uninstall -k --user 0 {package} > /dev/null 2>&1')
    if rcode == 0:
        return True
    return False

def pm_uninstall_system(package):
    rcode = system(f'pm uninstall {package} > /dev/null 2>&1')
    if rcode == 0:
        return True
    return False

def pm_disable(package):
    rcode = system(f'pm disable {package} > /dev/null 2>&1')
    rcode2 = system(f'pm disable-user --user 0 {package} > /dev/null 2>&1')
    if rcode == 0 or rcode2 == 0:
        return True
    return False

def pm_enable(package):
    rcode = system(f'pm enable {package} > /dev/null 2>&1')
    if rcode == 0:
        return True
    return False

def kill_app(package):
    rcode = system(f'kill $(pidof {package}) > /dev/null 2>&1')
    if rcode == 0:
        return True
    return False

def cls():
    system('clear')

def opt_app(package):
    rcode = system(f'pm force-dex-opt {package} > /dev/null 2>&1')
    if rcode == 0:
        return True
    return False

def get_all_apps():
    proc = ['pm', 'list', 'package', '-e']
    out = run(proc, stdout=PIPE).stdout.decode('utf8')
    apps = []
    for app in out.split('package:'):
        app = app.strip()
        if app != '':
            apps.append(app)
    return apps

def get_system_locale():
    proc = ['getprop', 'persist.sys.locale']
    return run(proc, stdout=PIPE).stdout.decode('utf8').strip()