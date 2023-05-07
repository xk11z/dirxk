# dirxk
一款集成了多种老牌工具字典的轻量级目录扫描器，包括御剑后台扫描字典，test404网站备份，web破壳扫描器，御剑1.5扫描字典，御剑专业版字典，wwwscan字典，dirscan字典，dirsafe字典，swebscan等字典已合并去重
# 项目介绍
支持多线程扫描，可指定线程数。 随机user-agent头。  

-x指定X-forward-for头，默认随机。 

-f支持导入字典检测。  

-o导出html报告  

-m指定扫描方法（head，get，post） 

-c指定状态码 

-m指定内置字典

# 安装
git clone https://github.com/xk11z/dirxk.git 

cd dirxk 

pip install -r requirements.txt
# 项目截图
## 界面
![l界面](https://user-images.githubusercontent.com/126586204/236677457-800bb799-7620-47f0-b110-9abb7fd7a521.PNG)
## 内置字典列表
### 小字典 
![x](https://user-images.githubusercontent.com/126586204/236677778-32b1cd30-24e4-46ac-8699-3df55f165714.PNG)
### 大字典
![d](https://user-images.githubusercontent.com/126586204/236677784-9e3991b8-8890-403c-809d-b889e4202320.PNG)

## 结果
![l结果](https://user-images.githubusercontent.com/126586204/236677470-00d89840-a41d-4fec-a9a8-02bcd520f9aa.PNG)
## 导出html报告
![l导出](https://user-images.githubusercontent.com/126586204/236677479-03907e28-fa98-4534-8e2e-10b1e7ecf885.PNG)
![l页面](https://user-images.githubusercontent.com/126586204/236677493-21bd9401-d9b6-4383-8f4e-b1c75f98eacc.PNG)

# 免责声明
本工具仅面向合法授权的企业安全建设行为，如您需要测试本工具的可用性，请自行搭建靶机环境。 在使用本工具进行检测时，您应确保该行为符合当地的法律法规，并且已经取得了足够的授权。请勿对非授权目标进行扫描。 如您在使用本工具的过程中存在任何非法行为，您需自行承担相应后果，我们将不承担任何法律及连带责任。
