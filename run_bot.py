from slacker import Slacker
import slackbot_settings
import psutil

if __name__ == '__main__':
    for proc in psutil.process_iter():
        if proc.name() == slackbot_settings.PROCNAME:
            pid = proc.pid
    process_cpu = psutil.Process(pid).cpu_percent(interval=3)
    message = slackbot_settings.PROCNAME + ' CPU使用率：' + str(process_cpu) +'%'
    slack = Slacker(slackbot_settings.API_TOKEN)
    slack.chat.post_message(slackbot_settings.CHANNEL,message)
