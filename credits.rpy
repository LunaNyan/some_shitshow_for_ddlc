init python:
    import datetime

image credits_cg1:
    "images/cg/credits/1.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2:
    "images/cg/credits/2.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3:
    "images/cg/credits/3.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4:
    "images/cg/credits/4.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5:
    "images/cg/credits/5.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6:
    "images/cg/credits/6.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7:
    "images/cg/credits/7.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8:
    "images/cg/credits/8.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9:
    "images/cg/credits/9.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10:
    "images/cg/credits/10.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_locked:
    "images/cg/credits/1b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg2_locked:
    "images/cg/credits/2b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg3_locked:
    "images/cg/credits/3b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg4_locked:
    "images/cg/credits/4b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg5_locked:
    "images/cg/credits/5b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg6_locked:
    "images/cg/credits/6b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg7_locked:
    "images/cg/credits/7b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg8_locked:
    "images/cg/credits/8b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg9_locked:
    "images/cg/credits/9b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg10_locked:
    "images/cg/credits/10b.png"
    size (640, 360)
    8.6
    "images/menu/notfound.png"

image credits_cg1_clearall:
    "images/cg/credits/1.png"
    size (640, 360)

image credits_cg2_clearall:
    "images/cg/credits/2.png"
    size (640, 360)

image credits_cg3_clearall:
    "images/cg/credits/3.png"
    size (640, 360)

image credits_cg4_clearall:
    "images/cg/credits/4.png"
    size (640, 360)

image credits_cg5_clearall:
    "images/cg/credits/5.png"
    size (640, 360)

image credits_cg6_clearall:
    "images/cg/credits/6.png"
    size (640, 360)

image credits_cg7_clearall:
    "images/cg/credits/7.png"
    size (640, 360)

image credits_cg8_clearall:
    "images/cg/credits/8.png"
    size (640, 360)

image credits_cg9_clearall:
    "images/cg/credits/9.png"
    size (640, 360)

image credits_cg10_clearall:
    "images/cg/credits/10.png"
    size (640, 360)

image credits_logo:
    "gui/logo.png"
    truecenter
    zoom 0.6 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

image credits_ts:
    "images/bg/splash-white.png"
    xalign 0.5 yalign 0.6
    zoom 0.65 alpha 0 subpixel True
    linear 2.0 alpha 1
    4.5
    linear 2.0 alpha 0

style credits_header:
    font "gui/font/RifficFree-Bold.ttf"
    color "#ffaae6"
    size 36
    text_align 0.5
    outlines []

style credits_text:
    font "gui/font/Halogen.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines []

style monika_credits_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 24
    text_align 0.5
    outlines []
style monika_korsub_text:
    font "gui/font/m1.ttf"
    color "#fff"
    size 36
    text_align 0.5
    outlines [(2, "#000", 0, 0)]

image credits_header = ParameterizedText(style="credits_header", ypos=-40)
image credits_header2 = ParameterizedText(style="credits_header", ypos=-55)
image credits_text = ParameterizedText(style="credits_text", ypos=40)
image monika_credits_text = ParameterizedText(style="monika_credits_text", xalign=0.5)


transform credits_scroll:
    subpixel True
    yoffset 740
    linear 15 yoffset -380

transform credits_text_scroll:
    anchor (0.5, 0.5) subpixel True
    yoffset 920
    linear 15 yoffset -200

transform credits_sticker_scroll:
    subpixel True
    yoffset 940
    7.8
    linear 15 yoffset -180

transform credits_scroll_right:
    xalign 0.9
    credits_scroll

transform credits_scroll_left:
    xalign 0.1
    credits_scroll

transform credits_text_scroll_right:
    xpos 960
    credits_text_scroll

transform credits_text_scroll_left:
    xpos 320
    credits_text_scroll

transform credits_sticker_1:
    yanchor 1.00
    xalign 0.32
    credits_sticker_scroll
transform credits_sticker_2:
    yanchor 1.00
    xalign 0.44
    credits_sticker_scroll
transform credits_sticker_3:
    yanchor 1.00
    xalign 0.56
    credits_sticker_scroll
transform credits_sticker_4:
    yanchor 1.00
    xalign 0.68
    credits_sticker_scroll

define credits_ypos = 250

image mcredits_1a:
    ypos credits_ypos
    xoffset -147
    "black"
    10.33
    Text("난 매일", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_1b:
    ypos credits_ypos
    xoffset -20
    "black"
    11.75
    Text("너와 함께 할 그 날을", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 12.0, ramplen=4, alpha=False)
image mcredits_1c:
    ypos credits_ypos
    xoffset 130
    "black"
    13.76
    Text("상상하곤 해", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)
image mcredits_2a:
    ypos credits_ypos + 50
    xoffset -147
    "black"
    19.45
    Text("내 손엔", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 13.0, ramplen=4, alpha=False)
image mcredits_2b:
    ypos credits_ypos + 50
    xoffset -20
    "black"
    20.9
    Text("우리에 대한 시를 쓸", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)
image mcredits_2c:
    ypos credits_ypos + 50
    xoffset 130
    "black"
    22.27
    Text("펜을 들고서", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4, alpha=False)

image mcredits_3:
    ypos credits_ypos + 100
    "black"
    28.35
    Text("잉크가 까만 웅덩이를 만들면", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_4:
    ypos credits_ypos + 150
    "black"
    32.9
    Text("손짓으로 사랑을 써 보지만,", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 9.0, ramplen=4, alpha=False)

image mcredits_5:
    ypos credits_ypos + 200
    "black"
    37.5
    Text("무한한 선택지의 세계 속에선", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 16.0, ramplen=4, alpha=False)

image mcredits_6a:
    ypos credits_ypos + 250
    xoffset -60
    "black"
    42.0
    Text("그 날이 올 길이", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)
image mcredits_6b:
    ypos credits_ypos + 250
    xoffset 65
    "black"
    43.47
    Text(" 정말 있을까?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 10.0, ramplen=4, alpha=False)

image mcredits_7:
    "black"
    alpha 0.0
    48.62
    linear 1.5 alpha 1.0

image mcredits_1_test:
    ypos credits_ypos + 300
    Text("그 날이 올 길이 정말 있을까?", style="monika_credits_text") with ImageDissolve("images/menu/wipeleft.png", 15.0, ramplen=4)

image end_glitch1:
    "bg/end-glitch1.jpg"
    alpha 0.0
    time 1.0
    alpha 1.0
    block:
        yoffset 1280 ytile 2
        linear 1 yoffset 0
        repeat
    time 9.45
    "end_glitch2"
    time 22.1
    "end_glitch3"
    time 28.65
    "end_glitch4"

image end_glitch2:
    "bg/end-glitch2.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch3:
    "bg/end-glitch3.jpg"
    block:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image end_glitch4:
    parallel:
        "bg/end-glitch4.jpg"
        1.25
        "bg/end-glitch3.jpg"
        0.1
        repeat
    parallel:
        yoffset 1280 ytile 2
        linear 4 yoffset 0
        repeat

image korsub_0:
    xpos 556
    ypos 650
    Text("...내 말 들려?", style="monika_korsub_text")
image korsub_1:
    xpos 539
    ypos 650
    Text("어... 내 말 들려?", style="monika_korsub_text")
image korsub_2:
    xpos 565
    ypos 650
    Text("안녕! 나야...", style="monika_korsub_text")
image korsub_3:
    xpos 450
    ypos 650
    Text("어... 나 요즘 연습하던거 알지?", style="monika_korsub_text")
image korsub_4:
    xpos 538
    ypos 650
    Text("...피아노 말이야.", style="monika_korsub_text")
image korsub_5:
    xpos 502
    ypos 650
    Text("아직 별로 못 쳐, 아예.", style="monika_korsub_text")
image korsub_6:
    xpos 420
    ypos 650
    Text("그런데 너한테 쓴 곡이 하나 있어서", style="monika_korsub_text")
image korsub_7:
    xpos 476
    ypos 650
    Text("정말로 보여주고 싶었거든", style="monika_korsub_text")
image korsub_8:
    xpos 453
    ypos 650
    Text("정말 정말 신경 많이 썼으니까", style="monika_korsub_text")
image korsub_9:
    xpos 570
    ypos 650
    Text("그래서, 응!", style="monika_korsub_text")
image music_korsub_1:
    xpos 383
    ypos 650
    Text("오늘은 무슨 활동을 해야 재미가 있을까?", style="monika_korsub_text")
image music_korsub_2:
    xpos 392
    ypos 650
    Text("어차피 너와 함께라면 뭐든 재밌으니까", style="monika_korsub_text")
image music_korsub_3:
    xpos 484
    ypos 650
    Text("내가 내 마음도 모르는데", style="monika_korsub_text")
image music_korsub_4:
    xpos 461
    ypos 650
    Text("미소만큼 좋은 말이 있을까?", style="monika_korsub_text")
image music_korsub_5:
    xpos 469
    ypos 650
    Text("이뤄질 수 없는 운명이라면", style="monika_korsub_text")
image music_korsub_6:
    xpos 453
    ypos 650
    Text("내가 그 운명을 쓸 순 없을까?", style="monika_korsub_text")
image music_korsub_7:
    xpos 354
    ypos 650
    Text("내 펜은 정말 쓴소리 밖에 쓸 줄 모르는 걸까?", style="monika_korsub_text")
image music_korsub_8:
    xpos 395
    ypos 650
    Text("난 너를 놓아줘야 진정한 사랑인 걸까?", style="monika_korsub_text")
image music_korsub_9:
    xpos 455
    ypos 650
    Text("잉크가 까만 웅덩이를 만들면", style="monika_korsub_text")
image music_korsub_10:
    xpos 455
    ypos 650
    Text("사랑을 현실로 쓸 수 있을까?", style="monika_korsub_text")
image music_korsub_11:
    xpos 451
    ypos 650
    Text("네 심장 소리를 듣지 못한다면", style="monika_korsub_text")
image music_korsub_12:
    xpos 476
    ypos 650
    Text("사랑이라 말할 수 있을까?", style="monika_korsub_text")
image music_korsub_13:
    xpos 403
    ypos 650
    Text("네 세상에서 너를 사랑할 줄 모른다면", style="monika_korsub_text")
image music_korsub_14:
    xpos 580
    ypos 650
    Text("널 떠날게", style="monika_korsub_text")

label credits:

    $ persistent.autoload = "credit"
    $ config.keymap['game_menu'] = []
    $ config.keymap['hide_windows'] = []
    $ renpy.display.behavior.clear_keymap_cache()
    $ quick_menu = False
    $ config.skipping = False
    $ config.allow_skipping = False
    scene black
    play music "bgm/end-voice.ogg" noloop

    show noise zorder 9:
        alpha 0.0
        linear 1.5 alpha 1.0
        time 2.0
        parallel:
            0.05
            choice:
                alpha 0.5
            choice:
                alpha 0.75
            choice:
                alpha 1.0
            repeat
        parallel:
            linear 0.375 alpha 0.7
            linear 0.375 alpha 1.0
        time 2.75
        alpha 0.95
        time 6.45
        alpha 0.3
        time 6.95
        alpha 0.9
        time 8.65
        linear 0.8 alpha 0
        alpha 0.5
        time 22.1
        alpha 0.85
        time 22.35
        alpha 0.5
        time 28.20
        alpha 0.3
        linear 0.45 alpha 0.9
        alpha 0.4
    show vignette zorder 10:
        alpha 0.75
        parallel:
            0.36
            alpha 0.75
            repeat
        parallel:
            0.49
            alpha 0.7
            repeat
    show end_glitch1 zorder 2
    show black as bar zorder 9:
        alpha 0.3
        size (1280,500)
        block:
            ypos 720
            linear 15 ypos -500
            repeat
    show korsub_0 zorder 21:
        alpha 0.0
        time 2.75
        alpha 0.3
        time 4.67
        alpha 0.6
        time 5.41
        alpha 0.0
        time 7.53
        alpha 0.6
        time 8.55
        alpha 0.0
    show korsub_1 zorder 22:
        alpha 0.0
        time 6.25
        alpha 0.3
        time 6.45
        alpha 0.0
        time 9.5
        alpha 1.0
        time 10.86
        alpha 0.0
    show korsub_2 zorder 23:
        alpha 0.0
        time 13.22
        alpha 1.0
        time 14.61
        alpha 0.0
    show korsub_3 zorder 24:
        alpha 0.0
        time 15.5
        alpha 1.0
        time 18.49
        alpha 0.0
    show korsub_4 zorder 25:
        alpha 0.0
        time 18.80
        alpha 1.0
        time 21.27
        alpha 0.0
    show korsub_5 zorder 26:
        alpha 0.0
        time 21.87
        alpha 1.0
        time 26.10
        alpha 0.0
    show korsub_6 zorder 27:
        alpha 0.0
        time 26.75
        alpha 1.0
        time 28.5
        alpha 0.0
    show korsub_7 zorder 28:
        alpha 0.0
        time 28.9
        alpha 1.0
        time 32.0
        alpha 0.0
    show korsub_8 zorder 29:
        alpha 0.0
        time 32.5
        alpha 1.0
        time 35.53
        alpha 0.0
    show korsub_9 zorder 30:
        alpha 0.0
        time 36.14
        alpha 1.0
        time 37.49
        alpha 0.0

    pause 41
    scene black
    pause 0.5
    $ consolehistory = []
    call updateconsole ("renpy.music.play(\"ddlc.ogg\")", "다음 음원을 재생합니다 \"ddlc.ogg\"...") from _call_updateconsole_5
    pause 1.0
    call hideconsole from _call_hideconsole_1
    play music "<to 50.0>bgm/credits.ogg" noloop
    show mcredits_1a zorder 50
    show mcredits_1b zorder 49
    show mcredits_1c zorder 48
    show mcredits_2a zorder 47
    show mcredits_2b zorder 46
    show mcredits_2c zorder 45
    show mcredits_3 zorder 44
    show mcredits_4 zorder 43
    show mcredits_5 zorder 42
    show mcredits_6a zorder 41
    show mcredits_6b zorder 40
    show mcredits_7 zorder 51

    pause 50
    jump credits2

label credits2:
    python:
        sayoriTime = renpy.random.random() * 4 + 4
        natsukiTime = renpy.random.random() * 4 + 4
        yuriTime = renpy.random.random() * 4 + 4
        monikaTime = renpy.random.random() * 4 + 4
        sayoriPos = 0
        natsukiPos = 0
        yuriPos = 0
        monikaPos = 0
        sayoriOffset = 0
        natsukiOffset = 0
        yuriOffset = 0
        monikaOffset = 0
        sayoriZoom = 1
        natsukiZoom = 1
        yuriZoom = 1
        monikaZoom = 1
        imagenum = 0
    scene black
    show music_korsub_1 zorder 51:
        alpha 0.0
        time 10.5
        alpha 1.0
        time 15.7
        alpha 0.0
    show music_korsub_2 zorder 52:
        alpha 0.0
        time 19.5
        alpha 1.0
        time 24.70
        alpha 0.0
    show music_korsub_3 zorder 53:
        alpha 0.0
        time 28.3
        alpha 1.0
        time 32.8
        alpha 0.0
    show music_korsub_4 zorder 54:
        alpha 0.0
        time 32.8
        alpha 1.0
        time 37.0
        alpha 0.0
    show music_korsub_5 zorder 55:
        alpha 0.0
        time 37.5
        alpha 1.0
        time 42.0
        alpha 0.0
    show music_korsub_6 zorder 56:
        alpha 0.0
        time 42.0
        alpha 1.0
        time 46.0
        alpha 0.0
    show music_korsub_7 zorder 57:
        alpha 0.0
        time 65.9
        alpha 1.0
        time 71.0
        alpha 0.0
    show music_korsub_8 zorder 58:
        alpha 0.0
        time 75.0
        alpha 1.0
        time 80.2
        alpha 0.0
    show music_korsub_9 zorder 59:
        alpha 0.0
        time 88.3
        alpha 1.0
        time 92.8
        alpha 0.0
    show music_korsub_10 zorder 60:
        alpha 0.0
        time 92.8
        alpha 1.0
        time 96.8
        alpha 0.0
    show music_korsub_11 zorder 61:
        alpha 0.0
        time 97.6
        alpha 1.0
        time 101.8
        alpha 0.0
    show music_korsub_12 zorder 62:
        alpha 0.0
        time 101.8
        alpha 1.0
        time 105.9
        alpha 0.0
    show music_korsub_13 zorder 63:
        alpha 0.0
        time 105.9
        alpha 1.0
        time 111.2
        alpha 0.0
    show music_korsub_14 zorder 64:
        alpha 0.0
        time 114.7
        alpha 1.0
        time 116.2
        alpha 0.0
    $ consolehistory = []
    play music "<from 50.0>bgm/credits.ogg" noloop
    $ starttime = datetime.datetime.now()
    pause 0.88
    show credits_logo
    pause 9.12
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    show expression ("credits_cg1" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "콘셉트 & 게임 디자인" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(16.95 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_6
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg1.png\")", "n_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall
    show expression ("credits_cg2" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "캐릭터 아트" as credits_header_2 at credits_text_scroll_right
    show credits_text "Satchely" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(26.05 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_7
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg2.png\")", "n_cg2.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_1
    show expression ("credits_cg3" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "배경 아트" as credits_header_1 at credits_text_scroll_left
    show credits_text "Velinquent" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(35.15 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_8
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg1.png\")", "y_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_2
    show expression ("credits_cg4" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "글" as credits_header_2 at credits_text_scroll_right
    show credits_text "Dan Salvato" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(44.25 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_9
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg2.png\")", "y_cg2.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_3
    show expression ("credits_cg5" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header "음악" as credits_header_1 at credits_text_scroll_left
    show credits_text "Dan Salvato" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(53.35 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_10
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/n_cg3.png\")", "n_cg3.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_4
    show expression ("credits_cg6" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "보컬" as credits_header_2 at credits_text_scroll_right
    show credits_text "Jillian Ashcraft" as credits_text_2 at credits_text_scroll_right
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(62.45 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_11
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/y_cg3.png\")", "y_cg3.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_5
    show expression ("credits_cg7" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header2 "감사한 분들" as credits_header_1 at credits_text_scroll_left
    show credits_text "Masha Gutin\nKagefumi\nDavid Evelyn" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    $ pause(71.55 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_12
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg1.png\")", "s_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_6
    show expression ("credits_cg8" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header2 "감사한 분들" as credits_header_2 at credits_text_scroll_right
    show credits_text "Corey Shin\nAlecia Bardachino\nMatt Naples" as credits_text_2 at credits_text_scroll_right
    show s_sticker at credits_sticker_1
    show n_sticker at credits_sticker_2
    show y_sticker at credits_sticker_3
    show m_sticker at credits_sticker_4
    $ pause(80.60 - (datetime.datetime.now() - starttime).total_seconds())
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ imagenum += 1
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_13
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg2.png\")", "s_cg2.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_7
    $ pause(88.00 - (datetime.datetime.now() - starttime).total_seconds())
    show expression ("credits_cg9" + lockedtext) as credits_image_1 at credits_scroll_right
    show credits_header2 "한국어화 패치 by" as credits_header_1 at credits_text_scroll_left
    show credits_text "번역, 검수 RealBucheon\n번역, 프로그래밍 YC\n아이콘 제작 Erel_P & Pom_0117\n" as credits_text_1 at credits_text_scroll_left
    $ lockedtext = "" if persistent.clear[imagenum] else "_locked"
    $ if persistent.clearall: lockedtext = "_clearall"
    $ pause(95.00 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_14
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/s_cg3.png\")", "s_cg3.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_8
    show expression ("credits_cg10" + lockedtext) as credits_image_2 at credits_scroll_left
    show credits_header "특별히 감사한 분들" as credits_header_2 at credits_text_scroll_right
    show credits_text "모니카\n[player]" as credits_text_2 at credits_text_scroll_right
    $ pause(104.10 - (datetime.datetime.now() - starttime).total_seconds())
    if not persistent.clearall:
        call updateconsole ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_15
    else:
        call updateconsole_clearall ("os.remove(\"images/cg/m_cg1.png\")", "m_cg1.png 가 성공적으로 제거되었습니다.") from _call_updateconsole_clearall_9

    call updateconsole ("os.remove(\"game/screens.rpy\")", "screens.rpy 가 성공적으로 제거되었습니다.") from _call_updateconsole_16
    call updateconsole ("os.remove(\"game/gui.rpy\")", "gui.rpy 가 성공적으로 제거되었습니다.") from _call_updateconsole_17
    call updateconsole ("os.remove(\"game/menu.rpy\")", "menu.rpy 가 성공적으로 제거되었습니다.") from _call_updateconsole_18
    call updateconsole ("os.remove(\"game/script.rpy\")", "script.rpy 가 성공적으로 제거되었습니다.") from _call_updateconsole_19
    $ pause(115.72 - (datetime.datetime.now() - starttime).total_seconds())
    call hideconsole from _call_hideconsole_2
    show credits_ts
    show credits_text "사랑을 담아서":
        zoom 0.75 xalign 0.5 yalign 0.25 alpha 0 subpixel True
        linear 2.0 alpha 1
        4.5
        linear 2.0 alpha 0
    pause 9.3
    play sound page_turn
    show poem_end with Dissolve(1)
    label postcredits_loop:
        $ persistent.autoload = "postcredits_loop"
        $ config.keymap['game_menu'] = []
        $ config.keymap['hide_windows'] = []
        $ renpy.display.behavior.clear_keymap_cache()
        $ quick_menu = False
        $ config.skipping = False
        $ config.allow_skipping = False
        scene black
        show poem_end
        $ pause()
        call screen dialog(message="오류: 스크립트 파일이 존재하지 않습니다.\n게임을 재설치 해주세요.", ok_action=Quit(confirm=False))
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
