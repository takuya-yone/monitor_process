# slack-cpu-monitor
プロセスのCPU利用率をSlackに投下

# requirement
- python 3.5.2
  - psutil==5.2.2
  - slackbot==0.4.1

# how to use
下記を変更
- slackbot_settings.py
  - API_TOKEN:SlackBotトークン
  - PROCNAME:監視対象プロセス名
  - CHANNEL:投稿チャンネル名
```
python run_bot.py
```
