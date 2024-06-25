# Description

This is GitHub Action to send messages or files to Telegram using official
[Telegram Bot API](https://core.telegram.org/bots/api). <br>

# Prerequisites

**TL;DR - Bot token and chat ID required.**

1. First of all, you need to create (or take already existed if you have)
   Telegram
   Bot. You need to go to `@BotFather` bot in Telegram to create one. Just
   follow
   bot instructions. <br>
   After creating a bot, you need to write down **bot token**. You can find
   token of all your bot with `@BotFather` bot.
2. Next, you need to create Telegram channel (can be private) and add your bot
   to it.
   You need to grant at least `Post messages` permission.
3. After creating channel, you need to get **channel ID**. You can do it
   with `@username_to_id_bot` (Not official Telegram bot).
4. Now you have both **bot token** and **channel ID**. Add these variables to
   Github Secrets. <br>
   **It's strictly not recommended to use raw values in your pipeline, please
   consider using Secrets!**
5. Now, you're ready to go! Go to Examples section for some inspiration!

# Examples

1. **Send simple message**
   ```yaml
   on: [ push ]
   
   jobs:
     tg_post_job:
       runs-on: ubuntu-latest
       name: A job to post data in tg
       steps:
         - name: Send data
           uses: BorisTestov/tg_sender_action@latest
           env:
             TG_SENDER_TG_CHAT_ID: ${{ secrets.TG_SENDER_TG_CHAT_ID }}
             TG_SENDER_TG_BOT_TOKEN: ${{ secrets.TG_SENDER_TG_BOT_TOKEN }}
             TG_SENDER_PAYLOAD_MESSAGE: "Hello World!"
             TG_SENDER_PAYLOAD_PARSE_MODE: "HTML"
   ```
2. **Send file**
   ```yaml
   on: [ push ]
   
   jobs:
     tg_post_job:
       runs-on: ubuntu-latest
       name: A job to post data in tg
       steps:
         - name: Send data
           uses: BorisTestov/tg_sender_action@latest
           env:
             TG_SENDER_TG_CHAT_ID: ${{ secrets.TG_SENDER_TG_CHAT_ID }}
             TG_SENDER_TG_BOT_TOKEN: ${{ secrets.TG_SENDER_TG_BOT_TOKEN }}
             TG_SENDER_PAYLOAD_FILE_PATH: /path/to/file
   ```
3. **Send file with caption**
   ```yaml
   on: [ push ]
   
   jobs:
     tg_post_job:
       runs-on: ubuntu-latest
       name: A job to post data in tg
       steps:
         - name: Send data
           uses: BorisTestov/tg_sender_action@latest
           env:
             TG_SENDER_TG_CHAT_ID: ${{ secrets.TG_SENDER_TG_CHAT_ID }}
             TG_SENDER_TG_BOT_TOKEN: ${{ secrets.TG_SENDER_TG_BOT_TOKEN }}
             TG_SENDER_PAYLOAD_MESSAGE: "Hello World!"
             TG_SENDER_PAYLOAD_FILE_PATH: /path/to/file
   ```
4. **Send nothing** (Doesn't trigger error but do nothing)
   ```yaml
   on: [ push ]
   
   jobs:
     tg_post_job:
       runs-on: ubuntu-latest
       name: A job to post data in tg
       steps:
         - name: Send data
           uses: BorisTestov/tg_sender_action@latest
           env:
             TG_SENDER_TG_CHAT_ID: ${{ secrets.TG_SENDER_TG_CHAT_ID }}
             TG_SENDER_TG_BOT_TOKEN: ${{ secrets.TG_SENDER_TG_BOT_TOKEN }}
   ```

# Variables

- `TG_SENDER_TG_BOT_TOKEN` - Bot token. Required.
- `TG_SENDER_TG_CHAT_ID` - ID of the chat to send data to. Required.
  <br><br>
- `TG_SENDER_PAYLOAD_FILE_PATH` - Path to file to send. Optional.
- `TG_SENDER_PAYLOAD_MESSAGE` - Message to send. Optional.
- `TG_SENDER_PAYLOAD_PARSE_MODE` - Parse mode for message. Can be one of (`HTML`, `MARKDOWN`, `MARKDOWNV2`). If not set
  or set to incorrect value, no parse mode will be used (plain text will be sent)
  <br><br>
- `TG_SENDER_LOG_LEVEL` - Log level. Optional. Default is `INFO`.
- `TG_SENDER_LOG_FORMAT` - Message format. Optional. Default
  is `%(asctime)s,%(msecs)03d %(levelname)-8s %(name)s: %(message)s`.
- `TG_SENDER_LOG_DATEFMT` - Date format. Optional. Default
  is `%b-%d-%Y %H:%M:%S`

# Limitations

⚠️You can send only one message and one file at a time. If you need to send
several messages, create several Action instances.⚠️

⚠️Be careful with Telegram limitations for bots. You can't send large
files ([the limit is 50 Mb for now](https://telegram-bot-sdk.readme.io/reference/senddocument))
.⚠️

⚠️Also consider not sending messages too frequently as Telegram
has [frequency limitation](https://core.telegram.org/bots/faq#:~:text=If%20you're%20sending%20bulk,minute%20to%20the%20same%20group)
.⚠️

⚠️This action works only on Linux steps as it uses Docker.⚠️

# License

Licensed under the [MIT](https://opensource.org/license/mit/) license. See
LICENSE for more information.
