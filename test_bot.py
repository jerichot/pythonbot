from flask import Flask
app = Flask(__name__)

#@app.route("/")
#def hello():
#    return "Hello World!"\


from flask import Flask, request, abort

from linebot import (
    LineBotApi, WebhookHandler
)
from linebot.exceptions import (
    InvalidSignatureError
)
from linebot.models import (
    MessageEvent, TextMessage, TextSendMessage,
)

app = Flask(__name__)

line_bot_api = LineBotApi('/1PZqfZc31glqg1otEueg7XPNcdZBy7GubXKF/4CLNzcSQVdFcocD5kNZhCfn3yR3saiLOBBo02rbhDsZCOs/BffOqDYRmLWkpP4o8dsl5/lvGux0sefve7at6vYLOMRE2RtaUEgnhgGhZ9zcJt8oQdB04t89/1O/w1cDnyilFU=
')
handler = WebhookHandler('b2beae22ed6d5e669b663b867bf98094
')


@app.route("/callback", methods=['POST'])
def callback():
    # get X-Line-Signature header value
    signature = request.headers['X-Line-Signature']

    # get request body as text
    body = request.get_data(as_text=True)
    app.logger.info("Request body: " + body)

    # handle webhook body
    try:
        handler.handle(body, signature)
    except InvalidSignatureError:
        abort(400)

    return 'OK'


@handler.add(MessageEvent, message=TextMessage)
def handle_message(event):
    line_bot_api.reply_message(
        event.reply_token,
        TextSendMessage(text=event.message.text))


if __name__ == "__main__":
    app.run()