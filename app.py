from flask import Flask, request, abort
from linebot import LineBotApi, WebhookHandler
from linebot.models import MessageEvent, TextMessage, TextSendMessage

app = Flask(__name__)

line_bot_api = LineBotApi('0QCWE0u8rPIYkbxR4cMkv+9RHdFy186ZVYi/SXQ6tEiJ8TwRR9AShjzC310Yk2IyWWc5UloIOYjuyB5OsOv1E4nbfC04rBwlVcObvUvXMOC2FJ/ouwQJKSDfs4hsoDoCFR6KC507uNuF5iy315cPdQdB04t89/1O/w1cDnyilFU=')# ←実際のチャネルトークンを貼る
handler = WebhookHandler('c4659cb172cbba6664e08f9a21f136d9')         # ←実際のチャネルシークレットを貼る

@app.route("/callback", methods=['POST'])
def callback():
    signature = request.headers['X-Line-Signature']
    body = request.get_data(as_text=True)

    try:
        handler.handle(body, signature)
    except:
        abort(400)

    return 'OK'
@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text="メッセージありがとうございます！")
    )

if __name__ == "__main__":
    app.run()
