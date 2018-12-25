from wxpy import *

bot = Bot()

# bot = Bot(console_qr=True) 

# 发送表情 文件必须是gif

from tempfile import NamedTemporaryFile
url='https://timgsa.baidu.com/timg?image&quality=80&size=b9999_10000&sec=1545717885410&di=e25af024214e835f11e5419b99649460&imgtype=0&src=http%3A%2F%2Fp0.so.qhmsg.com%2Ft019cd39f56a71a18a5.gif'
tmp = NamedTemporaryFile()
import requests
res = requests.get(url, allow_redirects=False)
res = requests.get(url, allow_redirects=False)
tmp.write(res.content)
tmp.flush()
media_id = bot.upload_file(tmp.name)
tmp.close()

@bot.register()
def print_others(msg):
    msg.reply(content='@img@.gif',media_id=media_id)



tuling = Tuling(api_key='f940116868864965aaa3977d80c60447')


def auto_reply_groupMsg(msg):
    if msg.is_at:
        tuling.do_reply(msg)

# 来自组的文本消息
@bot.register(Group,msg_types=TEXT)
def auto_ReplyForwardSend_groupMsg(msg):
    auto_reply_groupMsg(msg)
