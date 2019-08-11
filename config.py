# Hostname
hostname = "127.0.0.1:5000"
# Redirect time
cooldown_redirect = 10
# Site title
title = "telegram-redirect"

### MESSAGES ###
message_convert = "Convert"
message_redirect = "You will be redirected in "
message_sec = "sec."
message_redirecting = "Redirecting..."
message_open = "Open in Telegram"
footer_content = '<a href="https://github.com/kiriharu/telegram-redirect" class="text-white">Github</a>'
message_banned_title = "This content has been blocked by the administration of the resource...."
message_banned_info = "This chat / link / stickerpack / proxy has been banned by the administrator as suspicious " \
                      "or unwanted. Contact the resource administrator for more data."

### Banlist ###

banlist = {
    "joinchat": ["IEfu70tomR1g_8MQAAAAA", "IEfu70tomR1g_BBBBB"],
    "stickers": ["some_stickerpack1", "some_stickerpack2"],
    "ip": ["228.288.132.132", "312.213.321.123"],
    "username": ["someusername1", "somechannelname1"]
}

### Ads ###

# Enable adverstiments
adverstiment_active = False

# Check templates, don't modify this!
adv_templates = ["banned.html", "redirect.html", "index.html"]
# Ad height
adv_h = 200
# Ad weight
adv_w = 300
# Ad alt
adv_alt = "Adverstiment"

### Google Analytics ###

# Enable google analytics
g_active = False
# G-tag
g_tag = "AA-123456789-1"

# vars to inject, don't modify this

inject = dict(
      title=title,
      hostname=hostname,
      message_convert=message_convert,
      cooldown_redirect=cooldown_redirect,
      message_redirect=message_redirect,
      message_sec=message_sec,
      message_redirecting=message_redirecting,
      message_open=message_open,
      footer_content=footer_content,
      message_banned_title=message_banned_title,
      message_banned_info=message_banned_info,
      adverstiment_active=adverstiment_active,
      adv_h=adv_h,
      adv_w=adv_w,
      adv_alt=adv_alt,
      g_active=g_active,
      g_tag=g_tag
)