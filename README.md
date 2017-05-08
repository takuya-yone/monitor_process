# monitor_process
プロセスのCPU利用率をSlackに投下

# requirement
- python 3.5.2
  - psutil==5.2.2
# how to use
下記を変更
- slackbot_settings.py
  - API_TOKEN:SlackBotトークン
- run_bot.py
  - PROCNAME:監視対象プロセス名

```
python run_bot.py
```
