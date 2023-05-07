import argparse

from colorama import Fore, Style

from config import output
from config.dirscan import dirxkscan


def get_parser():
    # create parser object
    parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)
    # parser = argparse.ArgumentParser(description='Scan directories at specified URL')

    # add arguments using add_argument() method
    parser.add_argument('-u', '--url', type=str, required=True, help='输入一个URL')
    parser.add_argument('-w', '--wordlists', type=str, required=False,default='tophigh', help="""{}小字典[shell,dir,asp,aspx,php,\npy,sql,pl,cgi,cfm,\nthinkphp,jsp,mdb,fck,springboot,\nbackup,tophigh,wordpress,phpmyadmin,phpcms,\ndiscuz,dedecms,ecshop,ewebeditor,empire]\n大字典[mdir,masp,maspx,mjsp,mmdb,mfck,mphp]{}""".format(Fore.LIGHTCYAN_EX, Style.RESET_ALL))
    parser.add_argument('-f', '--file', type=str, required=False, help='导入一个字典')
    parser.add_argument('-o', '--output', type=str, required=False, help='导出结果')
    parser.add_argument('-c', '--custom_status_code', type=int, required=False, default=200, help='自定义状态码')
    parser.add_argument('-x', '--x_forwarded_for', type=str, required=False, default='random',
                        help='指定 X-Forwarded-For 头部的值，默认为随机')

    parser.add_argument('-m', '--method', type=str, required=False, choices=['head', 'get', 'post'], default='get',
                        help='指定请求方法')
    parser.add_argument('-t', '--threads', type=int, required=False, default=10,
                        help='指定线程数')

    # parse arguments from command line
    args = parser.parse_args()
    return args

def main():
    output.logo()
    args=get_parser()
    dirxkscan(args)




if __name__ == '__main__':

    main()
