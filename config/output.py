import time
from jinja2 import Template
import colorama as colorama
from pyfiglet import Figlet
def logo():
    print('version:1.0 | made by xkllz | date:2023/05/07')

    # 初始化 colorama 库，以便在控制台上输出 ANSI 转义序列
    colorama.init()
    # 创建 Figlet 实例并指定字体
    f = Figlet(font='banner')
    # 使用 colorama 库设置字体颜色
    print(colorama.Fore.GREEN + f.renderText('dirxk') + colorama.Style.RESET_ALL)


def get_time():
    return time.strftime("  %Y-%m-%d /%H:%M:%S/", time.localtime())


# create a template for the HTML report
template = Template("""
<!DOCTYPE html>
<html>
<head>
    <title>{{ title }}</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            font-size: 14px;
            line-height: 1.5;
        }
        h1 {
            font-size: 32px;
            margin-top: 60px;
        }
        h2 {
            font-size: 24px;
            margin-top: 40px;
        }
        .result {
          display: flex;
          flex-wrap: wrap;
        }
        .result-item {
          margin-right: 30px;
          margin-bottom: 10px;
        }
        .result-label {
          font-weight: bold;
          margin-right: 5px;
        }
    </style>
</head>
<body>
    <h1>{{ title }}</h1>
    {% for result in results %}
        
         <div class="result-item">
           <li><a href="{{ result.url }}">{{ result.url }}</a></li>
          </div>
        <div class="result">
          <div class="result-item">
            <span class="result-label">Status Code:</span> {{ result.status }}
          </div>
          <div class="result-item">
            <span class="result-label">Content Length:</span> {{ result.length }}
          </div>

          {% if 'X-Powered-By' in result.headers %}
            <div class="result-item">
              <span class="result-label">X-Powered-By:</span> {{ result.headers.get('X-Powered-By') }}
            </div>
          {% endif %}

          {% if 'server' in result.headers %}
            <div class="result-item">
              <span class="result-label">Server:</span> {{ result.headers.get('server') }}
            </div>
          {% endif %}

          {% if 'Server' in result.headers %}
            <div class="result-item">
              <span class="result-label">Server:</span> {{ result.headers.get('Server') }}
            </div>
          {% endif %}
        </div>
    {% endfor %}

    <p>[+]文件写入结束...{{ get_time() }}</p>
</body>
</html>
""")
