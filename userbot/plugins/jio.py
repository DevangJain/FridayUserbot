"""Emoji
Available Commands:
.emoji shrug
.emoji apple
.emoji :/
.emoji -_-"""


import asyncio

from uniborg.util import admin_cmd


@borg.on(admin_cmd(pattern=r"airtel"))
async def _(event):

    if event.fwd_from:

        return

    animation_interval = 1

    animation_ttl = range(0, 19)

    # input_str = event.pattern_match.group(1)

    # if input_str == "jio":

    await event.edit("airtel")

    animation_chars = [
        "`Connecting To Airtel Network 📡 ....`",
        "`█ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▇ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▆ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▅ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▄ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▂ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▁`",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "*Optimising Network....*",
        "`▒ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▒ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▒ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▒ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▒ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▒ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ ▒`",
        "`▁ ▂ ▄ ▅ ▆ ▇ █`",
        "**Airtel Network Connected and Boosted....**",
    ]

    for i in animation_ttl:

        await asyncio.sleep(animation_interval)

        await event.edit(animation_chars[i % 19])
