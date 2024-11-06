import json
from dataclasses import dataclass

import requests
from flask import Flask, jsonify, request
from linebot.v3.messaging import (
    Configuration,
    ApiClient,
    MessagingApi,
    PushMessageRequest,
    TextMessage,
)

import config


@dataclass
class AppConfig:
    line_channel_access_token: str
    line_channel_secret: str
    user_id: str


app: Flask


def setup_app():
    """
    setup config.json
    """
    access_token: str
    secret: str

    if len(config.LINE_CHANNEL_ACCESS_TOKEN):
        access_token = config.LINE_CHANNEL_ACCESS_TOKEN
    else:
        access_token = input("input LINE channel access token: ")
        assert (len(access_token) != 0)

    if len(config.LINE_CHANNEL_SECRET):
        secret = config.LINE_CHANNEL_SECRET
    else:
        secret = input("input LINE channel access token: ")
        assert (len(secret) != 0)

    # open LineLoginMicroService
    login_url = f"{config.LLMS_HOST}/login"
    print(f"open '{login_url}' and input the code")
    import webbrowser
    webbrowser.open(login_url, autoraise=True)

    code = input("code: ")
    assert (len(code) != 0)

    auth_collect = requests.post(f"{config.LLMS_HOST}/api/v1/auth/collect", json={"code": code})
    session_id = auth_collect.json()["session"]
    profile = requests.get(f"{config.LLMS_HOST}/api/v1/sessions/{session_id}/")
    print(profile.json())

    with open(config.CONFIG_FILE, 'w') as fp:
        json.dump({
            "access_token": access_token,
            "secret": secret,
            "user_id": profile.json()["user_id"],
        }, fp=fp, indent=2)

    print(f"Configuration saved to '{config.CONFIG_FILE}'")


def serve_app(config: AppConfig):
    """
    Flask WebServer
    """
    app = Flask(__name__)
    app.config["DEBUG"] = True

    configuration = Configuration(access_token=config.line_channel_access_token)

    @app.route('/', methods=['GET'])
    def index():
        return jsonify({"message": "ok"})

    @app.route('/text', methods=['POST'])
    def text():
        data = request.get_json()
        with ApiClient(configuration) as api_client:
            line_bot_api = MessagingApi(api_client)
            result = line_bot_api.push_message(PushMessageRequest(
                to=config.user_id,
                messages=[TextMessage(
                    text=data["message"].strip()
                )]
            ))
        return jsonify({"message": "ok", "result": result.sent_messages[0].__dict__})

    app.run(host="0.0.0.0", port=8001)


def load_config() -> AppConfig:
    with open(config.CONFIG_FILE, "r") as fp:
        data = json.load(fp)
        return AppConfig(
            line_channel_access_token=data["access_token"],
            line_channel_secret=data["secret"],
            user_id=data["user_id"]
        )


if __name__ == "__main__":
    app_config: AppConfig | None = None

    try:
        app_config = load_config()
    except Exception as e:
        setup_app()
        app_config = load_config()

    serve_app(app_config)
