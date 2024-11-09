# NotifyToLine

## Overview

This is a REST API for sending LINE messages to a single user. It serves as a sample project for using the [LineLoginMicroService](https://github.com/jhjcpishva/LineLoginMicroService).

## Setup

### Preparation

First, set up a LINE Official Account and enable the Messaging API.

You'll need the `Channel access token (long-lived)` and `Channel secret` to use this service. To obtain a `LINE_USER_ID`, you can use the [LineLoginMicroService](https://github.com/jhjcpishva/LineLoginMicroService) or manually provide the credentials in a `.env` file as follows:

```env:.env
LINE_CHANNEL_ACCESS_TOKEN=Or3x....
LINE_CHANNEL_SECRET=f27d....
LINE_USER_ID=U1234....
```

### Docker

```sh
docker build -t notifytoline .

docker run \
  -it --rm \
  -p 8001:8001 \
  -v $PWD/config.json:/app/config.json \
  notifytoline
```

## Usage

We recommend using the `http` CLI command from [HTTPie](https://www.postman.com/cli) to test this service.

### Send Text Message `/text`

Send a text message in JSON format with a body like `{ "message": "Hello World" }`.

#### Request

```sh
# use httpie
http :8001/text message="Hello World"

# or curl
curl -X POST http://localhost:8001/text \
  -H "Content-Type: application/json" \
  -d '{"message": "hello world"}'

```

#### Response

```sh
HTTP/1.1 200 OK

{
    "message": "ok",
    "result": {
        "id": "....",
        "quote_token": "...."
    }
}
```

### Send Text Message (Raw) `/text/raw`

You can also send a text message using plain text input.

#### Request

```sh
# use httpie
echo "Hello World 2" | http POST :8001/text/raw

# or curl
curl -X POST http://localhost:8001/text \
  -d 'Hello World 2'
```

