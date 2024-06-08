import readAudioFile as readAF
import getQuote
import platform


character = input('请输入角色名（使用完整英文）: ')
language = input('要获取的台词语言（jp/cn\ncn仅限中国船使用，其它阵营无中文语音）:')
file_list = readAF.read_audio_file()
quote_list = getQuote.get_quote(character, language)

with open(f'{character}.list', 'w', encoding='utf-8') as f:
    f.seek(0)
    if platform.system() == 'Windows':
        for i in range(len(file_list)):
            file_list[i] = file_list[i].replace('/', '\\')
            file_list[i] = file_list[i].replace('\\' + character + '-', '/' + character + '-')
            try:
                f.write(f'{file_list[i]}|{character}|{language}|{quote_list[i]}\n')
            except IndexError:
                print('\033[31m'+'\033[1m'+'音频文件与文本行数不匹配。\n请检查音频文件夹。')

    else:
        for i in range(len(file_list)):
            try:
                f.write(f'{file_list[i]}|{character}|{language}|{quote_list[i]}\n')
            except IndexError:
                print('\033[31m'+'\033[1m'+'音频文件与文本行数不匹配。\n请检查音频文件夹。')
  
        print('\033[36m'+'\033[1m'+'成功写入 ' + len(file_list) +' 行到 ' + character + '.list')
