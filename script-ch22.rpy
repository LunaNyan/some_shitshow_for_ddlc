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

image yuri half = "images/yuri/1l.png"
image yuri_half2:
    "images/yuri/1r.png"
    block:
        xoffset -360
        linear 0.2 xoffset -280
        repeat

label ch22_main:
    $ finalConso = finalChecker(player)
    scene bg club_day2
    with dissolve_scene_half
    play music t6
    "또 하루가 지나고, 벌써 동아리 시간이 돌아왔다."
    "지난 이틀보단 이 곳이 좀 더 편해진 것 같다."
    "부실을 들어서니 익숙한 장면이 날 반겨준다."
    if renpy.random.randint(0,2) == 0:
        show yuri half zorder 2 at i11
        show yuri_half2 zorder 1 at i11
    else:
        show yuri 1s zorder 2 at t11
    y "어서와요, [player] 씨…."
    hide yuri_half2
    mc "아… 안녕 유리…."
    "나만 그런 건지는 모르겠지만…."
    "어제 말다툼의 아직도 공기 중에 떠도는 느낌이 든다."
    y 2v "으음…."
    "유리는 주변을 살짝 둘러보았다."
    "나츠키는 만화를 읽고 있다."
    "놀랍게도, 모니카는 아직 와있지 않았다."
    "그때, 유리가 내 팔을 붙잡고 날 교실 구석으로 데려갔다."
    show bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "어제 일은…."
    y "저…."
    y 2v "진심으로 사과드려요."
    y "이런 일이 있던 적은 없었는데…."
    y 2t "뭔가 제가 어떻게 됐었나 봐요…."
    y "이성적인 행동이 아니었어요."
    y 2w "원래 이렇지 않다는 것만 알아주세요!"
    y "저뿐만이 아니라, 나츠키 씨도…."
    show yuri 2t
    mc "유리…."
    mc "네가 이렇게 직접 와서 사과해준다니 기뻐."
    mc "너무 걱정하지 않아도 돼."
    mc "비록 내가 여기온지 며칠밖에 되지 않았지만, 어제는 뭔가 이상했어…."
    mc "아마 어제가 우리가 처음으로 시를 나눠본 거라 조금 예민했나봐 ."
    mc "그런데 그렇다고…."
    mc "그게 널 깎아내리지는 않아."
    mc "난 네가 나쁜 사람이 아니라는 걸 알아."
    mc "그럴 의도가 아니었을 테니까, 사과하지 않아도 돼."
    y 3t "아, 아…."
    y "[player] 씨…."
    y 3u "그런 걸 너무 솔직하게 말하지 마세요…."
    y "그러시면 저… 너무 행복해져요."
    y 1s "당신이 이렇게 이해심 깊은 사람이라는 게 너무 좋아요…."
    y "그리고 이 동아리에 들어와주셔서 너무 좋고."
    y "당신이랑 있으면 모든 게 밝아지는 거 같고, 그리고…."
    y 1t "아…."
    y 4c "죄송해요, 제가 또 이상한 소릴 했나요…?"
    y "전 그저…."
    show natsuki 2c zorder 3 at f33
    n "저기, 너희들 모니카 봤어?"
    show natsuki zorder 2 at t33
    show yuri 3n at h32
    y "아!"
    mc "아니, 못 봤는데…."
    mc "어디 있나 궁금하던 참이었는데."
    show natsuki zorder 3 at f33
    n 5g "하아…."
    n 5c "유리, 너도 모르는 거야?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 4a "…."
    "유리는 태평하게 자신에게 말을 거는 나츠키의 모습을 보고 기겁했다."
    y "아, 아, 아니요… 못 봤는데요."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1u "흐음, 걔 답지 않네."
    n "바보 같긴 하지만 조금 걱정되네…."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2t "…."
    show yuri zorder 2 at t32
    show natsuki 1h zorder 3 at f33
    n "왜?"
    n "뭘 그렇게 보는거야?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y "저, 저기…."
    y "나츠키 씨, 어제 일에 대해선…."
    y 3w "정말 사과드리고 싶어요!!"
    y "제가 말했던 것들 다 진심이 아니에요!"
    y 3t "앞으로는 자중하도록 노력할게요…."
    y "그리고…."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2c "유리, 갑자기 뭔 소리 하는 거야?"
    n "어제 무슨 일 있었어?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3f "…네?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    $ style.say_dialogue = style.normal
    n 2a "하아…."
    $ style.say_dialogue = style.edited
    n "네가 무슨 생각을 하고 있든 간에 그건 아무것도 아니었어."
    n "난 나쁜 일 같은 거 하나도 기억이 안 나."
    n "넌 너무 사소한 일에도 신경을 쓴다, 알고 있니?"
    $ style.say_dialogue = style.normal
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 2o "…."
    y "하, 하지만…."
    if renpy.random.randint(0, 3) == 0:
        $ style.say_dialogue = style.edited
        show yuri zorder 2 at t32
        show natsuki mouth as nm zorder 3 at i33
        show n_moving_mouth zorder 3:
            xoffset 400
        n 2a "mibulls sailcloth blindsight lifeline anan rectipetality faultlessly offered scleromalacia neighed catholicate"
        hide nm
        hide n_moving_mouth
        $ style.say_dialogue = style.normal
    show natsuki zorder 3 at f33
    n 2j "뭐 네 기분이 나아질 수 있다면, 그 사과 받아줄게."
    n "게다가, 네가 혹시 날 싫어하는 게 아닌가 하고 걱정했거든. 다행이네"
    n 2z "에헤헤."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3q "아, 아니에요…!"
    y "싫어하지 않아요…."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2l "아하하."
    n "음, 좀 이상하긴 하지만. 나도 널 싫어하진 않아."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3t "…."
    "나츠키는 날 바라보았다."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 2a "그래서, 넌 누구 편이야?"
    show natsuki zorder 2 at t33
    mc "…!!"
    "갑자기 문이 열렸다."
    show monika 1g at l41
    m "미안해! 진짜 미안해!"
    mc "아, 왔어?"
    show monika zorder 3 at f41
    m "늦으려고한 건 아니였는데…."
    m "걱정하게 만들었다면 정말 미안해!"
    show monika zorder 2 at t41
    mc "아냐…."
    mc "뭐, 나츠키는 걱정했지."
    show natsuki zorder 3 at f33
    n 1p "아, 안 했거든!!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1k "아하하."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 1s "… 어쨌든… 왜 이렇게 늦은 거야?"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1e "아…."
    m "오늘 마지막 교시가 자습이었거든."
    m "정신 차려보니 시간이 벌써 이렇게 된 거 있지…."
    m "아하하…."
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2c "말이 안 되는데."
    n "적어도 수업 종료 종소리는 들었을 거 아냐."
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m 1m "피아노 연습하느라 못 들었던 거 같아."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1e "피아노…?"
    y "모니카 씨, 악기도 다룰 줄 아셨었군요."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 1l "아, 그렇게 잘 하는 건 아냐."
    m 1m "연습하고 있는지는 꽤 됐는데… 아직 잘 못 치겠어."
    show monika zorder 2 at t41
    show yuri zorder 3 at f32
    y 1a "그래도…."
    y "엄청난 노력이 필요한 거잖아요."
    y "그래서 조금 감명받았어요."
    show yuri zorder 2 at t32
    show monika zorder 3 at f41
    m 5 "고마워, 유리~"
    show monika zorder 2 at t41
    show natsuki zorder 3 at f33
    n 2d "언젠가 꼭 우리한테 연주해줘야 해!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f41
    m "아하하, 그건…."
    "모니카는 날 바라봤다."
    m 1a "글쎄, 지금 작곡하고 있는 게 있긴 한데, 아직 다 되지가 않아서…."
    m "조금 더 잘 되면 들려줄게."
    show monika zorder 2 at t41
    mc "멋진데."
    mc "기대하고 있을게."
    show monika zorder 3 at f41
    m 1b "그래?"
    m "그렇다면…."
    m "실망시키지 않을게, [player]."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show monika 5 zorder 2 at t11
    "모니카는 달콤한 미소를 지었다."
    mc "아…."
    mc "너무 부담 갖지는 마!"
    m 1a "아하하, 걱정하지 마."
    m "꼭 들려주고 싶었거든."
    m "그래서 최근에 열심히 연습했던 거야."
    mc "그렇구나…."
    "우리한테 들려주고 싶다는 건지, 나한테 들려주고 싶다는 건지 모르겠다…."
    mc "그렇다면야, 행운을 빈다."
    m 1j "고마워~!"
    m 1a "혹시 내가 놓친거라도 있어?"
    mc "아, 아니. 딱히."
    show monika zorder 1 at thide
    hide monika
    "난 우리 셋이 한 얘기를 꺼내지 않기로 했다."
    "게다가, 이미 나츠키는 벽장 속으로 들어가 버렸다."
    show yuri 2q zorder 2 at t11
    y "[player] 씨…."
    y "으음…."
    y "당신의 칭찬이 절 기분 좋게 했으니…."
    y "오늘 저와 같이 시간을 보내고 싶으신지 궁금해서요."
    y 3o "제 말은… 동아리에서요!"
    if poemwinner[0] == "natsuki":
        $ y_appeal = 1
        mc "응, 그럴 거야."
        mc "네가 나한테 그 책을 줬으니, 거절은 못 할 거 같네."
        mc "그래도 나츠키가 날 기다리고 있지는 않은지 확인해야겠어."
        mc "우리가 어제 책을 다 읽고 나서, 나츠키가…."
        if n_appeal >= 2:
            y 3r "괜찮아요!"
            $ style.say_dialogue = style.normal
            y 3h "저기서 책을 읽고 있잖아요, 보이시죠?"
            $ style.say_dialogue = style.edited
            y 3f "나츠키 씨에 대해선 생각하지 마세요."
            y "줄곧 무시하곤 했으니까, 괜찮아요."
            y "자요, 저희는 저기로 가죠."
            $ style.say_dialogue = style.normal
            window hide(None)
            $ currentpos = get_pos()
            stop music
            scene black
            window auto
            pause 2.0
            play music "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
            jump ch22_main2
        else:
            y 3r "괘, 괜찮아요!"
            y 3h "저기서 책을 읽고 있잖아요, 보이시죠?"
            y 3y6 "그러니까 괜찮아요, 네?"
            mc "아…."
            mc "그렇다면, 괜찮은 거 같네…."
    else:
        $ y_appeal = 2
        mc "응, 당연하지."
        mc "나도 그러려고 했어."
    show yuri zorder 2 at h11
    y 3y5 "좋아요!"
    y "시작할까요?"
    y "앉을 자리를 찾아 보…."
    y 3n "아, 아아…."
    y "저 지금 너무 강압적인가요?"
    y 4c "죄송해요!"
    y "어째선지 제 심장이 계속 두근거리네요…."
    mc "걱정하지 마."
    mc "네가 활기차 보여서 좋은걸."
    y 3q "네!"
    y "그래도…."
    y 3j "진정하도록 노력해봐야겠어요."
    y "이래서는 책 읽는 데 집중할 수가 없을 것 같아요…."
    mc "서두르지 말고 천천히 해도 돼."
    "유리는 심호흡하고 나서, 가방에서 책을 꺼냈다."
label ch22_main2:
    if n_poemappeal[1] == 1:
        $ n_poemappeal[1] = 0
    $ poemwinner[1] = "yuri"


    scene bg club_day2
    show yuri 3a at i11
    with wipeleft
    $ nextscene = "yuri_exclusive2_" + str(eval("y_appeal")) + "_ch22"
    call expression nextscene from _call_expression_12

    return

label ch22_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("특별한 시가 해금되었습니다.\n읽어보시겠습니까?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[1]) from _call_expression_13
        scene black with Dissolve(1.0)
    else:
        pass
    if not faint_effect and renpy.random.randint(0,2) == 0:
        $ faint_effect = True
    else:
        $ faint_effect = None
    scene bg club_day2
    show monika 4b zorder 2 at t32
    if faint_effect:
        show layer master at dizzy(0.5, 1.0)
        show layer screens at dizzy(0.5, 1.0)
        show expression Solid("ff0000") as i1 onlayer front:
            additive 1.0
        show expression Solid("#440000") as i2 onlayer front:
            additive 0.4
        show veins onlayer front:
            additive 0.5
    with wipeleft_scene
    if faint_effect:
        play music t3g3
    else:
        play music t3
    if renpy.random.randint(0,2) == 0:
        $ config.mouse = {"default": [
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head2.png", 0, 0),
                                    ("gui/mouse/s_head.png", 0, 0),
                                    ]}



    m "좋아, 얘들아!"
    m "서로의 시는 다 나눠 보았겠지?"
    $ config.mouse = None
    m "오늘은 할 얘기가 있으니까, 교실 앞쪽으로 와서 앉아 줄래?"
    show natsuki 3c zorder 3 at f31
    n "혹시 축제에 관한 거야?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "뭐, 그런 거지~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "으, 축제때 진짜로 뭔가를 해야 돼? 그럴 필요 없잖아."
    n "겨우 며칠 만에 다 준비할 수 있 는것도 아니고."
    n "새 부원을 모으기는커녕 창피만 당할 것 같은데."
    if faint_effect:
        $ currentpos = get_pos() + 2.0
        stop music fadeout 2.0
        show black onlayer front:
            alpha 0.0
            linear 2.0 alpha 1.0
    show natsuki zorder 2 at t31
    show yuri 2g zorder 3 at f33
    y "제 생각도 그래요."
    if faint_effect:
        hide black onlayer front
        hide veins onlayer front
        hide i1 onlayer front
        hide i2 onlayer front
        show layer master
        show layer screens
        play music "<from " + str(currentpos) + " loop 4.618>bgm/3.ogg"
    y "마지막 순간까지 기다렸다 준비하는 건 별로 제 스타일이 아니기도 하고…."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "너무 걱정하지 마!"
    m "간단하게 할꺼니까, 알았지?"
    m 2a "있지…."
    m 2m "다들 [player]가 동아리에 들어오고 몇 동아리 활동을 하고 나서 조금 생기가 도는 건 알겠는데…."
    m 2d "그래도 지금은 우리가 현실에 안주하고 있을 때가 아니야."
    m "우린 아직 네 명밖에 없으니까…."
    m 2a "축제야말로 부원을 더 모을 수 있는 기회잖아, 그치?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5g "부원을 더 모은다고 좋은 게 있어?"
    n "이미 공식 동아리로 인정받았잖아."
    n "더 모으면 더 시끄럽고 관리도 어려워질 뿐인 거 같은데."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "나츠키…."
    m "난 네 관점이 옳다고 생각하지 않아."
    m "가능한 한 많은 사람한테 네 열정을 보여주고 싶지 않니?"
    m 3e "처음에 네가 문예부에 왔을 때의 그 감정과 같은 감정을 사람들에게 느끼게 해주고 싶지 않아?"
    m "문예부에서는 다른 곳에서는 하지 못하는 자기표현을 할 수 있는 곳이 되어야 해."
    m "너무 좋아서 떠나기 싫은 장소가 되어야 해."
    m 2e "네가 그렇게 느끼는 거 알아."
    m 2b "우리 모두가 그렇다는 걸 알아!"
    m "그래서 우리가 축제를 위해 뭔가 열심히 준비해야 하는거야…아무리 작은 거라도!"
    m "그렇지, [player]?"
    show monika 2a zorder 2 at t32
    mc "아…."
    show natsuki zorder 3 at f31
    n 42c "아, 좀!"
    n "[player]가 거절을 잘 안 하는 성격이라고 해서 너한테 동의하도록 이용하면 안 되는거야."
    stop music fadeout 1
    n 1c "있지, 모니카."
    n "여기 있는 우리 중 한 명이라도 사람을 만나고 싶어서 동아리에 들어온 사람 있어?"
    n "유리는 [player]가 오기 전엔 한마디도 안 했어."
    n 2b "난 그냥 집에 있는 것보다 여기가 더 좋아서 그렇고."
    n "그리고 [player]는 처음에 문학에 대해 잘 알지도 못했잖아."
    n "그게 전부야."
    n 4w "미안한데, 새 부원을 찾는 데 관심있는 건 너 밖에 없는 거 같다."
    n "나머지 우리는 지금 이대로가 좋아."
    n 4q "네가 부장이니 뭐니 해도, 우리의 의견을 한번쯤은 고려했어야지."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "…."
    "모니카는 나츠키의 말을 듣고 크게 놀란듯하다."
    play music t9
    m 1m "그건… 별로 그렇지 않아."
    m 2m "분명히 유리랑 [player]도 부원을 더 모으고 싶어 할 거야…."
    m 2p "…그렇지?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 4b "…."
    show yuri zorder 2 at t33
    mc "…."
    "유리는 어떻게 생각할지 모르겠지만, 난 그냥 그저 그랬다."
    "내가 만약 모니카가 원하는 만큼 열정스럽게 얘기한다면, 그건 거짓말일 것이다."
    "그래도 이 상황을 해결하는 게 내 손에 달려있다면…."
    mc "저…."
    show monika zorder 3 at f32
    m 1i "아니."
    m "나츠키의 말이 맞아, 그렇지?"
    m 1g "이 동아리는…."
    m "그냥 몇 사람이 친목을 도모하는 장소에 지나지 않아."
    m 1r "왜 여기 모두가 나랑 같은 생각을 하고 있을 거라고 생각했을까?"
    show monika zorder 2 at t32
    mc "하지만 그렇다고 해서 우리가 새 부원을 반대하거나 하는 건 아니야…."
    show monika zorder 3 at f32
    m 1i "[player], 너는 왜 이 동아리에 들어왔어?"
    m "뭐를 바라고 들어온 거야?"
    show monika zorder 2 at t32
    mc "글쎄…."
    "이건 내가 솔직하게 말할 수 있는 부분이 아니잖아, 그런거지…?"
    show monika zorder 3 at f32
    m 1p "사실…."
    m "내 기억이 맞다면, 너는 거절할 기회도 없었을 거야."
    show monika zorder 1 at thide
    hide monika
    "모니카는 자리에 앉아 책상을 멍하니 바라보았다."
    m "이게 다 무슨 소용이야?"
    m "이 동아리를 만든 거 자체가 실수가 아니었을까?"
    mc "…."
    show yuri zorder 3 at f33
    y 2g "한 건 하셨네요, 나츠키 씨…."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1p "뭐, 나?"
    n 1s "나는 그냥 내 생각을 말한 건데…."
    n "솔직한 게 죄야?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2l "그냥 솔직한 게 문제가 아니라."
    y "단어 선택이 잘못 됐어요."
    y 2h "게다가, 그런 식으로는 누구한테도 말하면 안 되죠…."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1e "넌 이해를 못 해!"
    n 5s "난 그냥…."
    n "난 그냥 편하고 친구 몇 명이랑 어울리기 좋은 곳을 원해."
    n 5u "나에게 동아리가 그런 장소가 되는 게 문제야?"
    n "별로… 별로 나한텐 편안한 곳이 없으니까…."
    n 5x "그런데 모니카가 그걸 빼앗으려고 하잖아!"
    show natsuki zorder 2 at t31
    mc "모니카는 빼앗지 않…."
    show natsuki zorder 3 at f31
    n 1g "아냐, [player]."
    n "그거랑 달라."
    n 1q "모니카가 원하는 방향으로 흘러가게 내버려두지 않을 거야."
    n "내가 만약 그걸 원했다면, 난 그냥 아무 멍청한 동아리나 들어갔겠지."
    n 12d "그런데 여긴…."
    n "내 말은…."
    n 12e "그래도 아주 잠깐이라도…."
    n "다 좋았어."
    "나츠키는 자신의 가방을 싸기 시작했다."
    n 12d "난 집에 갈래."
    n "여기에 더 오래 있으면 안 되는 기분이야."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3t "나츠키 씨…."
    show natsuki zorder 1 at thide
    hide natsuki
    "나츠키는 유리를 무시하고 교실 밖으로 나갔다."
    show yuri zorder 2 at t11
    y 3v "…."
    y "좋지 않네요…."
    y "뭘 해야 할지 모르겠어요…."
    mc "글쎄…."
    mc "축제에 대해 좋은 의견 있어?"
    y 4b "모르겠네요…."
    $ style.say_dialogue = style.normal
    y "저는 조금 무관심해서…."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 630 ypos -50 zoom 2.0
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "누가 저런 건방진 년을 신경 써요?"
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    y "제 말은, 전 지금 동아리가 딱 적당하다고 생각해요…."
    y "그리고 당신이 여기에 있어서 좋고…."
    y 2t "그렇다고 해도!"
    y "저는 부부장이니까…."
    y "그런 책임을 무시하는 건 맞지 않겠죠…."
    show black zorder 3
    show y_glitch_head zorder 3:
        xpos 430 ypos -450 zoom 4.5
    $ style.say_dialogue = style.edited
    $ currentpos = get_pos() / 2.07
    play music "<from " + str(currentpos) + " loop 1.532>bgm/9g.ogg"
    y "걔가 자살한다고 해도 아무도 울어주지 않아요."
    $ style.say_dialogue = style.normal
    $ currentpos = get_pos() * 2.07
    stop music
    pause 0.5
    play sound "sfx/stab.ogg"
    show blood_eye zorder 3:
        pos (710,380) zoom 2.5
    pause 0.75
    stop sound
    play music "<from " + str(currentpos) + " loop 3.172>bgm/9.ogg"
    hide black
    hide y_glitch_head
    hide blood_eye
    y 2l "모든 사람의 관점을 고려해보고 동아리에 맞는 결정을 내리기 위해서 최선을 다해야겠죠."
    y 1t "하지만 당신은 어때요, [player]?"
    y "이 동아리에서 뭘 얻고 싶으신 건가요?"
    "유리는 모니카와 같은 질문을 건넨다."
    "난 간접적인 대답을 하는 게 안 하는 것보다 낫다고 생각했다."
    mc "…내 생각엔 모두 사이좋게 지내는 게 가장 중요하다고 생각해…."
    mc "…그리고 동아리를 위해 다른 곳에서는 가질 수 없는 걸 제공하는 거지."
    mc "부원이 몇명이냐의 문제가 아니라 각 부원의 자질이 중요하다고 생각해."
    mc "그게 문예부를 특별한 곳으로 만드는 거겠지."
    y 1u "그렇군요…."
    y "완벽히 동의해요."
    show blood_eye2 zorder 3:
        pos (568, 165)
    y 1f "각각의 부원이 특별한 방법으로 자신의 능력을 동아리에 기여하죠."
    y "부원들의 변화와 함께 동아리 전체의 정체성도 바뀔 거에요."
    y 1h "저는 그게 꼭 나쁜 일이라고 생각하지는 않아요."
    y "한 번쯤은 안전 구역에서 나가는 것도 좋을 거에요…."
    y 1a "그러니 당신이 모니카 씨를 축제에 관해 도와주신다면, 저도 당신 편이에요."
    hide blood_eye2
    mc "알았어."
    mc "그럼, 내일 나츠키한테 말해야겠네…."
    "유리는 끄덕였다."
    show monika 1g zorder 3 at f21
    show yuri zorder 2 at t22
    m "저기, 유리…."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1t "에?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1p "어제 조금 안 좋은 일이 있던거…."
    m "네가 훌륭한 부부장의 자격이 있다는 것만 알아줬으면 좋겠어."
    m 1e "그리고 좋은 친구라는 걸."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 3s "모, 모니카 씨…."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 2e "난 이 동아리를 최고로 만들 수만 있다면 뭐든지 할거야."
    m "알겠지?"
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y "…저도요."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "그래…."
    m "오늘은 같이 집에 가자."
    m "축제에 대해서는 내일 얘기하자."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 1m "좋아요."
    y "기대하고 있을게요."
    y 1a "그럼 갈까요, [player]?"
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1d "음…."
    m 1p "괜한 오해는 하지 말아줘…."
    m "나가기 전에 잠깐 [player]랑 할 말이 있어서."
    m 1d "[player]가 여기서 보낸 날들이랑 그 외의 것들에 대해 어떻게 생각하는지 들어보려고…."
    m "부장으로서 중요한 얘기야."
    show monika zorder 2 at t21
    show yuri zorder 3 at f22
    y 2v "…."
    "유리는 조금 곤란해 보이지만, 반박하지는 않는다."
    y 2t "좋아요."
    y 2s "당신의 판단을 믿을게요, 모니카 씨."
    y "그럼, 두 분 다 내일 뵐게요."
    show yuri zorder 2 at t22
    show monika zorder 3 at f21
    m 1j "내일 보자~"
    show yuri zorder 1 at thide
    hide yuri
    "모니카는 교실을 나가는 유리를 향해 손을 흔든다."

    show monika 2a zorder 2 at t11
    m "휴우…."
    m 2e "요새 좀 정신 없이 바빴다, 그치?"
    show darkred:
        additive 0.2
        alpha 0
        linear 20 alpha 1.0
    show noise:
        alpha 0
        linear 20 alpha 0.1
    m "[player], 나는 그냥 네가 이 동아리에서 즐겁게 지내고 확인하고 싶었어."
    m "네가 불행한 걸 보는 게 난 정말 싫어."
    m 2m "왠지 부장으로서 책임이 드는 기분이야…."
    stop music
    m 4e "그리고 난 널 많이 신경 쓰고 있어, 알아?"
    m "다른 애들이 널 힘들게 하는 건 보고 싶지 않아."
    m 4r "얼마나 나츠키가 상스러운지…."
    m 4m "그리고 유리는… 너도 알지."
    m 5a "아하하…."
    m "가끔 너랑 나만 유일한 진짜 사람인것처럼 느껴진다니까."
    m "그게 무슨 뜻인지 알아?"
    m 1g "조금 이상하긴 한데, 네가 여기 있는 동안에, 우리가 함께 할 시간이 거의 없었어."
    m 1n "아, 내 말은…."
    m "아, 따지면 이틀밖에 안 된 거구나…."
    m 1l "미안, 이상한 소리를 하려던 건 아니었어!"
    m 1e "그냥 너와 이야기하고 싶었던 게 몇 가지 있어…."
    m "오직 너만 이해할 수 있는 이야기를."
    stop music fadeout 3.0
    show black onlayer front:
        alpha 0.0
        0.25
        linear 3.0 alpha 1.00
    m "그래서 내가…\"{space=5000}{w=0.75}{nw}"
    m 1g "잠깐, 아직 아냐!\"{space=5000}{w=0.5}{nw}"
    m "안돼!\"{space=5000}{w=0.5}{nw}"
    m "멈춰!\"{space=5000}{w=1.0}{nw}"
    window hide(None)
    window auto
    hide black onlayer front





    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
