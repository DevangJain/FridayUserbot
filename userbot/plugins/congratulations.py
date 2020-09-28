import random

from uniborg.util import admin_cmd, edit_or_reply, sudo_cmd

RUNSREACTS = [
    "`Thanks Bro 😘😘`",
    "`You are greatest Person in the Worl 😍`",
    "`Thank You 🤩`",
    "`You are Acting like God For Me.. Thanks 😘😘`",
    "`Congratulations on your well-deserved success.`",
    "`Heartfelt congratulations to you.`",
    "`Warmest congratulations on your achievement.`",
    "`Congratulations and best wishes for your next adventure!”`",
    "`So pleased to see you accomplishing great things.`",
    "`Feeling so much joy for you today. What an impressive achievement!`",
]


@borg.on(admin_cmd(pattern="thanks"))
@borg.on(sudo_cmd(pattern="thanks", allow_sudo=True))
async def _(event):
    if event.fwd_from:
        return
    bro = random.randint(0, len(RUNSREACTS) - 1)
    reply_text = RUNSREACTS[bro]
    await edit_or_reply(event, reply_text)
