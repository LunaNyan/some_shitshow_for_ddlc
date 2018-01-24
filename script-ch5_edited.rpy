init python:

    finalConso =  None

    def finalChecker(name):
        import re
        name = name
        expr = re.compile(r'([a-zA-Z0-9\s~!@#$%^&*()_+|}{:"<>?`\-=\\\[\];\',./])')
        temp = expr.sub('', name)
        
        if temp == '':
            return False
        
        last_alphabet = repr(temp[-1])
        dec = int(str(last_alphabet[4:-1]), 16)
        
        while dec < 0x3164:
            temp = temp[:-1]
            if not temp:
                return False
            
            last_alphabet=repr(temp[-1])
            dec = int(str(last_alphabet[4:-1]), 16)
        
        dec= (dec-44032) % 588 % 28
        
        if dec == 0:
            return False
        
        else:
            return True


    def pppChanger(input):
        import re
        pppList = [('가', '이'), ('는', '은'),
                        ('를', '을'), ('와', '과'),
                        ]
        
        if finalConso:
            
            input = re.sub('\[player\]야', player + '아', input)
            
            for p, pc in pppList:
                input = re.sub('\[player\]'+ p, "[player]" + pc, input)
                input = re.sub('%\(player\)s' + p, "[player]" + pc, input)
        else:
            input = re.sub('\[player\]이', player, input)
        
        return input

    config.say_menu_text_filter = pppChanger

style fakeerror:
    font "gui/font/Aller_Rg.ttf"
    color "#000"
    size 36
    outlines []

image exception_bg = "#dadada"
image fake_exception = Text("응 구라 ㄴㄴ해", size=40, style="fakeerror")
image fake_exception2 = Text("\"game/script-ch5.rpy\" 파일, 라인 307\n자세한 내용은 traceback.txt을 참조하세요.", size=20, style="fakeerror")

image splash_glitch:
    subpixel True
    "images/bg/splash-glitch.png"
    alpha 0.0
    pause 0.5
    linear 0.5 alpha 1.0
    pause 2.5
    linear 0.5 alpha 0.0
    "gui/menu_bg.png"
    topleft
    alpha 0.0
    parallel:
        xoffset 0 yoffset 0
        linear 0.25 xoffset -100 yoffset -100
        repeat
    parallel:
        linear 0.5 alpha 1.0
    parallel:
        ypos 0
        pause 1.0
        easeout 1.0 ypos -500
image splash_glitch2:
    subpixel True
    "gui/menu_bg.png"
    topleft
    block:
        xoffset 0 yoffset 0
        linear 0.05 xoffset -100 yoffset -100
        repeat

image splash_glitch_m:
    subpixel True
    "gui/menu_art_m.png"
    zoom 0.5
    xpos 0.5 ypos 0.5
    pause 0.1
    parallel:
        xpos 0.3 ypos 1.2
        linear 0.08 ypos 0.1
        repeat
    parallel:
        pause 0.5
        alpha 0.0

image splash_glitch_n:
    subpixel True
    "gui/menu_art_n.png"
    zoom 0.5
    pause 0.2
    xpos 0.8 ypos 0.8
    pause 0.05
    xpos 0.2 ypos 0.7
    pause 0.05
    xpos 0.4 ypos 0.2
    pause 0.05
    xpos 0.7 ypos 1.2
    pause 0.05
    xpos 0.1 ypos 1.0
    pause 0.05
    xpos 0.2 ypos 0.6
    pause 0.05
    xpos 0.9 ypos 0.4
    pause 0.05
    alpha 0.0

image splash_glitch_y:
    subpixel True
    "gui/menu_art_y.png"
    zoom 0.5
    ypos 1.3
    block:
        xpos 0.85
        pause 0.02
        xpos 0.81
        pause 0.02
        repeat


label ch5_main:
    $ finalConso = finalChecker(player)
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    "오늘은 축제 날이다."
    "다른 날도 아니고 오늘만큼은 사요리와 함께 학교에 가겠다고 생각했는데."
    "사요리가 전화를 받지 않는다."
    "사요리를 깨우러 걔 집에 갈까 잠시 생각했지만, 그건 좀 과하지 않나 라는 생각이 들었다."
    "축제 준비도 거의 다 끝났겠지."
    if ch4_scene == "natsuki":
        "컵케익이 가득 담긴 두 쟁반을 조심스럽게 쌓아 들고 길을 나선다."
        "나츠키가 폭풍같이 문자를 보내고 있는데, 덕분에 난 손이 없어서 답장할 수가 없다."
        "축제에 대해서 말인데, 조금 웃기기는 하지만 나도 나츠키랑 같은 마음이다."
        "낭송회보다도, 사요리와 나츠키랑 같이 축제를 즐길 생각에 벌써 마음이 들뜬다."
    else:
        "유리랑 내가 칠한 현수막은 이미 말라 있었고, 난 조심스럽게 그걸 말았다."
        "혹시나 잊어버리지 말라는 문자를 유리가 보냈고, 걱정 말라는 답장을 보냈다."
        "축제에 대해서 말인데, 조금 웃기기는 하지만 나도 나츠키랑 같은 마음이다."
        "낭송회보다도, 사요리와 유리랑 같이 축제를 즐길 생각에 벌써 마음이 들뜬다."

    "물론 모니카가 잘 이끌어주면 우리 행사도 잘 끝나겠지."

    scene bg club_day with wipeleft_scene
    show monika 5 zorder 2 at t11
    m "[player]!"
    m "네가 제일 일찍 왔어."
    m "일찍 와줘서 고마워!"
    mc "그래? 적어도 유리라면 이미 와있을 거라고 생각했는데."
    "모니카는 작은 책자를 교실 안 책상 위에 하나씩 올려놓고 있었다."
    "부원들이 낭송할 시를 적어둔다는 그 책자겠지."
    "난 결국 인터넷에서 아무 시나 하나 찾아서 모니카에게 보냈다."
    "나중에 낭송하게 되겠지."
    m 1d "사요리랑 같이 안 왔다니… 좀 의외다."
    mc "응, 또 늦잠 잤거든…."
    mc "그 바보."
    mc "이런 날에는 좀 더 진지하게 임해줬으면 좋겠는데…."
    "말은 그렇게 하지마는, 어제 사요리가 말해준 말을 다시 떠올린다…."
    "그렇게 간단한 일이 아니라는 걸 아니까 죄책감이 든다."
    "그렇게 생각하는 게 편하니까 그렇게 말한 거지만."
    "하지만…."
    "역시 직접 가서 깨우는 게 나았으려나…."
    m 1k "아하하."
    m 4b "조금은 책임감을 가져, [player]!"
    m "특히, 어제 그런 얘기를 나눈 후라면 말야…."
    m "걔 지금 목이 빠져라 기다리고 있는거 아냐?"
    show monika 4a
    mc "그런 얘기…?"
    mc "모니카, 너 그거 알고있는 거야?"
    m 2a "당연히 알고있지."
    m "일단 난 부장이니까."
    mc "하… 하지만!"
    "부끄러워져서, 난 말을 더듬었다."
    "사요리가 그 일을 벌써 얘기했나?"
    if sayori_confess:
        "이제… 우리 사귀는 사이라고?"
        "아직은 얘기할 생각이 없었는데…."
    else:
        "내가 어떻게 고백을 거절했는지를?"
        "그럼 내가 제일 나쁜 놈으로 보일 텐데…."
        "그렇지만 그게 최선이었는걸, 그렇지?"
    mc "하아…."
    mc "넌 자세히 모르니까…."
    m 2j "아 그런 거라면야."
    m "아마 네 생각보단 자세히 알고 있을 걸?"
    mc "어…?"
    "평소와 다름없이 친절한 목소리였지만, 왠지 그 말을 들으니 소름이 끼친다."
    m 5 "있지, 팸플릿 보지 않을래?"
    m "진짜 괜찮게 됐거든!"
    mc "응, 그래."
    "난 책상 위에 진열되어있는 팸플릿 중 하나를 집었다."
    mc "오, 진짜 잘 만들었는데."
    mc "이정도라면 사람들도 제대로 된 동아리라고 생각하겠는걸."
    m "응, 나도 그렇게 생각해!"
    show monika zorder 1 at thide
    hide monika
    "나는 페이지들을 넘겼다."
    "각 부원들이 쓴 시가 전문적인 시집처럼 페이지마다 깔끔하게 인쇄되어있었다."
    "나츠키랑 유리의 시는 우리가 연습할때 발표했었던 시였다는 걸 알 수 있었다."
    mc "이게 뭐지…?"
    "난 사요리의 시로 페이지를 넘겼다."
    "걔가 연습했던 거랑은 조금 다른데…."
    "내가 읽어본 적 없는…."
    call showpoem (poem_s3, music=False)
    mc "어…."
    "이게 뭐지…?"
    "간담이 서늘해진다."
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "무슨 일이야?"
    mc "아냐, 아무것도…."
    "이 시는 지금까지 사요리가 썼던 시와는 완전히 다르다."
    "그런데 그것보다는…."
    mc "새… 생각이 바뀌었어!"
    mc "사요리를 데리러 갈 테니까."
    m "어…."
    m 1b "그래 그럼!"
    m "너무 오래 걸리면 안 돼, 알겠지?"
    scene bg corridor with wipeleft
    "난 급하게 부실을 나갔다."
    m "너무 부담 갖지는 마!"
    "난 그런 말을 하는 모니카를 뒤로하고…."
    "난 더 빠르게 달려나갔다."

    scene bg residential_day with wipeleft_scene
    "난 무슨 생각으로 그런거지?"
    "사요리를 위해 좀 더 노력해 줄 수 있었는데."
    "기다려주는 것, 일어나는 걸 도와주는 것… 따지고 보면 그렇게 어려운 일도 아니었는데."
    "학교에 같이 갈 때 했던 작은 행동들조차도 사요리는 굉장히 행복해 했잖아."
    "그리고…."
    "모든 것들이 지금까지와 같을 거라고 어제 사요리한테 얘기했는데."
    "그게 사요리가 원했던 거고, 내가 해주고 싶은 거였는데."

    scene bg house with wipeleft
    "사요리의 집 문을 두드렸다."
    "전화도 받지 않았으니, 반응이 없는 것쯤은 예상했다."
    "어제처럼 난 그냥 문을 열고 들어갔다."
    scene black with wipeleft
    mc "사요리?"
    "진짜 잠탱이네…."
    "난 침을 삼킨다."
    "내가 이런 짓을 하리라곤 상상도 못 했다."
    "직접 집에 가서 깨운다니…."
    if sayori_confess:
        "남자친구가 해줄 만한 일이긴 하지…?"
    else:
        "보통 이런건 남자친구가 해 주는 일이 아닌가…?"
    "어쨌든…."
    "맞는 선택인 것 같다."

    "사요리의 방 앞에서, 난 문을 두드렸다."
    mc "사요리?"
    mc "일어나, 바보야…."
    "반응이 없다."
    "정말 이런 식으로 방에 들어가고 싶지는 않았는데…."
    "사생활 침해는… 아니겠지?"
    "그런 거 생각할 때는 아니겠지…."
    "나는 천천히 문을 열었다."
    mc "{cps=30}…….사요{/cps}{nw}"
    $ persistent.playthrough = 1
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("sayori")
    $ in_sayori_kill = True
    window hide(None)
    window auto
    play music td
    show s_kill_bg2
    show s_kill2
    show s_kill_bg as s_kill_bg at s_kill_bg_start
    show s_kill as s_kill at s_kill_start
    pause 3.75
    show s_kill_bg2 as s_kill_bg
    show s_kill2 as s_kill
    pause 0.01
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    hide s_kill_bg
    hide s_kill
    show s_kill_bg_zoom zorder 1
    show s_kill_bg2_zoom zorder 1
    show s_kill_zoom zorder 3
    show s_kill2_zoom zorder 3
    show s_kill as s_kill_zoom_trans zorder 3:
        truecenter
        alpha 0.5
        zoom 2.0 xalign 0.5 yalign 0.05
        pause 0.5
        dizzy(1, 1.0)
    pause 2.0
    show noise zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.25
    show vignette zorder 3:
        alpha 0.0
        linear 3.0 alpha 0.75
    pause 1.5
    show white zorder 2
    show splash_glitch zorder 2
    pause 1.5
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    pause 4.0
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.2
    stop sound
    hide screen tear
    hide splash_glitch
    show splash_glitch2 zorder 2
    show splash_glitch_m zorder 2
    show splash_glitch_n zorder 2
    show splash_glitch_y zorder 2
    pause 0.75
    hide white
    hide splash_glitch2
    hide splash_glitch_m
    hide splash_glitch_n
    hide splash_glitch_y
    show exception_bg zorder 2
    show fake_exception zorder 2:
        xpos 0.1 ypos 0.05
    show fake_exception2 zorder 2:
        xpos 0.1 ypos 0.15
    python:
        try: sys.modules['renpy.error'].report_exception("어라… 내가 잘못한 건 아니지? 잠깐만, 고칠 수 있을 거야… 아마도…\n 음, 생각해보니까 그냥 사요리를 삭제해버리는 게 나을지도 모르겠는걸? 애초에 이걸 어렵게 만든 건 걔니까 말이야. 아하하! 한번 해 보지 뭐.", False)
        except: pass
    pause 6.0


    "…."
    hide fake_exception
    hide fake_exception2
    hide exception_bg
    "뭐야…?"
    "{i}이게 뭐야?{/i}"
    "악몽인가?"
    "악몽일 거야…."
    "이게 진짜일 리가…."
    "이게 진짜일 리가 없어."
    "사요리는 이런 짓을 할 애가 아니야…."
    "며칠전까진 모든 게 다 정상이였는데…."
    "그래서 더 더욱 내 눈을 믿을 수가 없어…!"
    scene black with dissolve_cg
    "난 구토가 쏠리는 걸 억지로 참았다."
    "당장 어제만해도…."
    "옆에 있어 주겠다고 했는데."
    "최선이 뭔 줄 안다고, 모든 게 괜찮을 거라고 말해줬는데."
    "그런데 왜…?"
    "왜 이런 짓을…?"
    "어떻게 이렇게 허무하게?"
    "내가 뭘 잘못한 거지?"
    if sayori_confess:
        "고백…."
        "고백 같은 건하지 말았어야 했다."
        "그게 사요리가 원하는 건 아니였을테니까."
        "다른 애들이 어떻게 자기를 생각할지 두렵다고까지 말했는데…."
        "그런데 왜 난 고백을 하고 사요리의 기분을 더 망친 거지?"
    else:
        "고백을 거절한 것…."
        "그게 사요리를 벼랑 끝에서 밀어버린 거겠지."
        "사요리의 비명이 여전히 귀에서 울리는 거 같다."
        "사요리가 가장 필요한 사람은 나였을 텐데, 왜 그런 거지?"
    "난 왜 이렇게 이기적이지?"
    "이건 내 잘못이야…!"
    "이렇게 했었다면 이런 일은 막을 수 있었을텐데, 라는 생각이 머릿속을 가득 채운다."
    "내가 조금 더 사요리랑 같이 시간을 보냈더라면."
    "학교에 같이 걸어가고…."
    if sayori_confess:
        "항상 그랬듯이 친구로 남아있었다면…."
    else:
        "사요리가 원했던 그런 관계로 발전했었더라면…."
    "…그럼 이런 일 따위… 일어나지 않았겠지."
    "그럼 이런 일 따윈 일어나지 않았을텐데!"
    "문예부 같은 거…. 필요 없어."
    "축제 따위 좆 까라 그래."
    "난 지금… 내 가장 친한 친구를 잃었어."
    "내 소꿉친구…."
    "영영 사라졌어."
    "다시 사요리를 돌려낼 방법이 없어."
    "이건 초기화 같은 걸 해서 되돌릴 수 있는 게임 같은 게 아니야…."
    "딱 한 번만 더 기회가 주어진다면, 그렇게 성급한 선택은 하지 않을 텐데…."
    "이제 죽을 때까지 이 죄를 안고 가야겠지."
    "사요리가 살아온 인생에 비교하면 보잘것없는 인생이었는데…."
    "그런데도 사요리가 원하는 것 하나를 못 해주다니."
    "이젠…."
    "절대로 되돌릴 수 없어."
    "절대로."
    "절대로."
    "절대."
    "절대."
    "절대…."
    $ in_sayori_kill = False


    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
