# GPT-SoVITS碧蓝航线角色语音标注半自动脚本

## 功能
- 提取 http://azurlane.koumakan.jp/ 上的日文和中文语音文本并自动按序写入标注文件
- 尽可能地解决了Windows特有的反斜杠问题，大概率不需要后期手动修改标注文件中的路径部分

## 使用
0. `pip install -r requirements.txt`  
1. 下载所有的角色语音文件，并确保语音文件顺序符合该网站上记录的语音顺序  
   - 您需要重命名这些语音文件。在此建议使用Motrix等下载器批量下载语音，并在下载前将文件名批量指定为`<英文角色名(与网站上一致)>-<三位从000或001开始的数字，与网站中对应语音顺序一致>`  
   - 由于该网站过于随机的页面更新情况，若您不是从该英文Wiki下载语音文件可能会出现下载到的语音文件与网站记录台词数目不一致的情况，请保持本地文件与网站记录匹配（移除多出来的语音文件）
   - 同样由于该网站中一些角色的部分台词（多为早期台词）存在双语情况，您最终仍需要检查生成的标注文件并手动修改错误
2. 运行`main.py`，按照提示操作