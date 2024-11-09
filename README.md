# NotifyToLine

## Overview

REST API to send LINE Message to single user.

It's aimed as sample project to use [LineLoginMicroService](https://github.com/jhjcpishva/LineLoginMicroService)


## Setup

### Preparation

You will need to setup your LINE Official Account and Enabled Messaging API for it.

You will need `Channel access token (long-lived)` and `Channel secret` to use this service.

To collect `LINE_USER_ID` you can use [LineLoginMicroService](https://github.com/jhjcpishva/LineLoginMicroService)

or provide `.env` file with following credentials

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

Recommend to use `http` cli command from [HTTPie](https://www.postman.com/cli) to test this service.


### Send Text Message `/text`

Send Text Message by JSON format `{ "message": "Hello World" }`
 body

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

You can send text message with plain text input.

#### Request

```sh
# use httpie
echo "Hello World 2" | http POST :8001/text/raw

# or curl
curl -X POST http://localhost:8001/text \
  -d 'Hello World 2'
```

