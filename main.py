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

line_bot_api = LineBotApi('c9t3LHOS0GMhiyuMqF+FPryRbsNYJhAqEHwl7eYka95IaVAzelDIg7TtRbADF5BUeLNNxdNQjTy5rWDsAvoWHio710f7lHcN4++Qy9L860gd7tkS1y4Y5Mr6GDQHEjWMJ2GN6qOuWSWFAiRflgZDNgdB04t89/1O/w1cDnyilFU=')
handler = WebhookHandler('085c7e0e933d933724481fcf77fe32f9')


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