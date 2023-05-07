import random

import colorama
import requests
import threading
from config.output import get_time
from config.output import template
def dirxkscan(args):
    # define function to check if directory exists

    with open('config/user-agents.txt', 'r') as f:
        useragents = f.readlines()

    # 随机选择一个 user agent
    random_useragent = random.choice(useragents).strip()

    if args.x_forwarded_for == 'random':
        x_forwarded_for = '.'.join([str(random.randint(0, 255)) for _ in range(4)])
    else:
        x_forwarded_for = args.x_forwarded_for
    headers = {
        'user-agent': random_useragent,
        'X-Forwarded-For': x_forwarded_for
    }
    def check_directory(url, directory, results):

        try:

            if args.method == 'head':
                req = requests.head(url + directory,headers=headers)
            elif args.method == 'post':
                req = requests.post(url + directory,headers=headers)
            else:
                req = requests.get(url + directory,headers=headers)

            # print(colorama.Fore.YELLOW +'正在检测:'+req.url+get_time()+ colorama.Style.RESET_ALL)

            if req.status_code == args.custom_status_code:
                result = {
                    'url': req.url,
                    'status': req.status_code,
                    'length': len(req.content),
                    'headers': dict(req.headers),
                }
                # if req.headers.get('X-Powered-By'):
                #     result['X-Powered-By']=req.headers['X-Powered-By']
                # if req.headers.get('server'):
                #     result['server'] = req.headers['server']
                # if req.headers.get('Server'):
                #     result['Server'] = req.headers['Server']
                results.append(result)
            else:

                # results.append({
                #     'url': req.url,
                #     'status': req.status_code,
                #     'length': len(req.content),
                # })
                pass
        except:
            pass

    # get URL from args
    url = args.url

    # get wordlist from args or file
    if args.file:
        # read wordlist from file
        with open(args.file, 'r') as f:
            wordlist = [line.strip() for line in f.readlines()]
    else:
        # open wordlist file based on type
        wordlist_type = args.wordlists
        if wordlist_type == 'php':
            wordlist_file = open('dic/PHP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'jsp':
            wordlist_file = open('dic/JSP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'asp':
            wordlist_file = open('dic/ASP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'aspx':
            wordlist_file = open('dic/ASPX.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'dir':
            wordlist_file = open('dic/DIR.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'mdb':
            wordlist_file = open('dic/MDB.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'fck':
            wordlist_file = open('dic/FCK.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'springboot':
            wordlist_file = open('dic/SPRINGBOOT.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'shell':
            wordlist_file = open('dic/SHELL.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'cfm':
            wordlist_file = open('dic/CFM.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'cgi':
            wordlist_file = open('dic/CGI.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'backup':
            wordlist_file = open('dic/BACKUP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'thinkphp':
            wordlist_file = open('dic/THINKPHP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'pl':
            wordlist_file = open('dic/PL.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'py':
            wordlist_file = open('dic/PY.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'ecshop':
            wordlist_file = open('dic/ECSHOPV2.7.2.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'dedecms':
            wordlist_file = open('dic/DEDECMSV5.7.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'discuz':
            wordlist_file = open('dic/DISCUZ3.1.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'phpcms':
            wordlist_file = open('dic/PHPCMS9.5.7.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'phpmyadmin':
            wordlist_file = open('dic/PHPMYADMIN.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'wordpress':
            wordlist_file = open('dic/WORDPRESS3.5.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'ewebeditor':
            wordlist_file = open('dic/EWEBEDITOR.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'empire':
            wordlist_file = open('dic/EMPIRE.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'sql':
            wordlist_file = open('dic/SQL.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'thinkphp':
            wordlist_file = open('dic/THINKPHP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'masp':
            wordlist_file = open('dic/max/MASP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'maspx':
            wordlist_file = open('dic/max/MASPX.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'mdir':
            wordlist_file = open('dic/max/MDIR.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'mfck':
            wordlist_file = open('dic/max/MFCK.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'mjsp':
            wordlist_file = open('dic/max/MJSP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'mmdb':
            wordlist_file = open('dic/max/MMDB.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'mphp':
            wordlist_file = open('dic/max/MPHP.txt', 'r', encoding='gbk', errors='ignore')
        elif wordlist_type == 'tophigh':
            wordlist_file = open('dic/TOPHIGH.txt', 'r', encoding='gbk', errors='ignore')

        else:
            # if no type specified, use default DIR wordlist
            wordlist_file = open('dic/DIR.txt', 'r', encoding='gbk', errors='ignore')
        # read wordlist from file
        wordlist = [line.strip() for line in wordlist_file.readlines()]

    # create results list and threads
    results = []
    progress_lock = threading.Lock()  # add lock for shared variable
    progress = 0  # initialize shared variable for progress
    total = len(wordlist)  # length of wordlist
    threads = []
    if progress == 0:

        print('[+]开始探测目录...{}'.format(get_time()))


    def update_progress():  # helper function to update progress bar
        with progress_lock:
            progress_bar_length = 50
            filled_length = int(progress * progress_bar_length // total)
            bar = '#' * filled_length + '-' * (progress_bar_length - filled_length)
            print(f'\rProgress: [{bar}] {progress}/{total} ({(progress / total) * 100:.1f}%)', end='', flush=True)

    for directory in wordlist:
        # limit number of threads to specified amount
        while threading.active_count() > args.threads:
            pass
        thread = threading.Thread(target=check_directory, args=(url, directory, results))
        threads.append(thread)
        thread.start()
        with progress_lock:
            progress += 1  # increment progress
        update_progress()  # update progress bar

    # join all threads before returning results
    for thread in threads:
        thread.join()



    # render the template with the data and write it to file
    if args.output:
        with open(args.output, 'w') as f:
            html_report = template.render(title="符合条件的扫描结果", results=results, get_time=get_time)
            f.write(html_report)
        print('[+]HTML报告已经生成! {}'.format(get_time()))
    else:

        for result in results:
            print(colorama.Fore.YELLOW)
            print(result)
            print(colorama.Style.RESET_ALL)
        print('[+]目录探测结束...{}'.format(get_time()))

