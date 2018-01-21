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

image noface1:
    topleft
    xtile 10 ytile 10
    block:
        block:
            choice:
                "images/sayori/noface1.png"
            choice:
                "images/sayori/noface1b.png"
        block:
            choice:
                0.075
            choice:
                0.3
            choice:
                0.4
            choice:
                0.5
            choice:
                0.6
        repeat
image noface2:
    "images/sayori/noface2.png"
    xalign 0.95 yalign 0.47

label ch23_main:
    if renpy.random.randint(0,15) == 0 and not seen_eyes_this_chapter:
        $ quick_menu = False
        scene white
        show noface1
        show noface2
        with dissolve_scene_half
        play sound "sfx/gnid.ogg"
        pause 7
        $ quick_menu = True
        scene bg club_day2
        show yuri 2 zorder 2 at i11
    else:
        scene bg club_day2
        with dissolve_scene_half

    play music t6
    show yuri 2y5 zorder 2 at t11
    $ finalConso = finalChecker(player)
    y "안녕하세요, [player] 씨!"
    y "계속 기다리고 있었어요."
    y 2d "그럼 이어서 읽을까요?"
    y "오늘은 제가 가장 좋아하는 차를 가져왔…."
    show yuri 2f
    show natsuki 4w zorder 3 at f33
    n "모니카!"
    n "내가 너한테…."
    n 1g "어…."
    n "모니카는 또 늦는 거야?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1h "나츠키 씨, 여전히 생각이 없으시군요."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "뭐라고?"
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 1r "항상 소리 지르는 걸로 제 대화를 방해해야되나요?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 1o "무슨 소리 하는 거야?!"
    n 1q "누가 보면 내가 맨날 그러는 줄 알겠네."
    n "그냥 몰라서 그랬어, 미안해. 알겠지?."
    n 4u "진짜로… 요즘 무슨 일 있는 거야?"
    if n_appeal >= 2:
        n "저기…."
        n "어제 일에 대해 생각해봤는데…."
        n 2q "어젠 내가 생각보다 조금 더 적대적이었던 거 같아…."
        n 1q "내가 위협받는 느낌을 받았었나봐."
        n 1h "그래도 이게 우리가 모두 같이 하는 일이라는 건 알아."
        n 1q "걔네가 얌전히만 굴면 새 부원은 상처받지 않겠지…."
        n 5w "내 생각에 지금 다른 애는 착하게 구는 거 같은데…."
        n 5u "그러니까…."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        $ style.say_dialogue = style.normal
        y 2u "나츠키 씨…."
        $ style.say_dialogue = style.edited
        y 1f "아무도 신경 안 써요."
        y "그냥 어디 자판기 아래에 떨어진 동전이나 주우러 가는 건 어때요?"
        $ style.say_dialogue = style.normal
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 1p "…!"
        n 1r "…."
        n 12f "…."
        show natsuki at thide
        hide natsuki
        pause 1.0
        show monika 1g at l31
        m "아, 이런…."
        m "또 내가 마지막이네!"
        show yuri zorder 3 at f32
        y 1f "또 피아노 연습하다 오신 건가요?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "응…."
        m "아하하…."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "정말 의지가 강한 분이시네요."
        y "동아리도 시작하시고, 이젠 피아노까지…."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "글쎄, 의지가 아니라…."
        m 3a "열정이야."
        m "열정이 있어서 축제 준비도 열심히 하게 돼."
    else:
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2n "저요?"
        y 2o "아, 아니에요…."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "…."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "그게 그렇게 안돼 보였나요…?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2m "봐봐, {i}뭔가{/i} 있다니까."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 3p "전 극복할 수 있어요!"
        y 3y6 "별로 대단한 일도 아닌데…."
        y 3o "그냥 최근 들어 좀 초조해서요…."
        y 3n "어쨌든, 그거에 관해서 얘기할 필요 없어요!"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2q "글쎄, 얘기를 꺼내야만 할 거 같은 기분이 들던데."
        n 5q "내가 막 걱정하거나 그런 건 아니고…."
        show natsuki zorder 2 at t33
        show yuri 3e
        show monika 1g at l31
        m "아, 이런…."
        m "또 내가 마지막이네!"
        show natsuki zorder 3 at f33
        n 2c "글쎄, [player]도 방금 왔는데."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 1f "또 피아노 연습하다 오신 건가요?"
        show yuri zorder 2 at t32
        show monika zorder 3 at f31
        m 5a "응…."
        m "아하하…."
        show monika zorder 2 at t31
        show yuri zorder 3 at f32
        y 1m "정말 의지가 강한 분이시네요."
        y "동아리도 시작하시고, 이젠 피아노까지…."
        show yuri 1a zorder 2 at t32
        show monika zorder 3 at f31
        m 1a "글쎄, 의지가 아니라…."
        m 3a "열정이야."
        m "열정이 있어서 축제 준비도 열심히 하게 돼. 그리고…."
        m 3n "음…."
        show monika zorder 2 at t31
        show natsuki zorder 3 at f33
        n 5s "…."
        show natsuki zorder 2 at t33
        show monika zorder 3 at f31
        m 1l "맞다…."
        m "잊고있었네…."
        show monika zorder 1 at thide
        hide monika
        show yuri zorder 3 at f32
        y 2v "으음… 나츠키 씨… 그거 말인데요."
        y "어제 얘기해봤는데…."
        y 2t "음… 저희도 축제에 나가기로 했어요."
        y 2l "하지만…!"
        y 2h "나츠키 씨가 동아리를 바꾸고 싶어 하지 않는다는 거 이해해요."
        y "제 생각엔 모두가 같은 생각을 하고 있어요."
        y 2f "저희 모두가 같이 일하는 한, 이 동아리는 저희가 원하는 방향으로 갈 거에요."
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n "…."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2v "으음, 그리고…."
        y "만약 축제 준비를 도와주신다면…."
        y 3r "…새 만화책을 사드릴게요!"
        show yuri 3t zorder 2 at t32
        show natsuki zorder 3 at f33
        n 5h "…."
        n 2z "아하하하!"
        n "미안, 마지막에 말한 거 되게 웃기다."
        n 2c "생각해 봐…."
        n "어제 일에 대해 생각해봤는데…."
        n 2q "어젠 내가 생각보다 조금 더 적대적이였던 거 같아…."
        n 1q "내가 위협받는 느낌을 받았었나 봐."
        n 1h "그래도 이게 우리가 모두 같이 하는 일이라는 건 알아."
        n 1q "걔네가 얌전히만 굴면 새 부원은 상처받지 않겠지…."
        n 5w "내 생각에 지금 다른 애는 착하게 구는 거 같은데…."
        n 5e "…그것보다 중요한 건, 내가 안 한다고 해서 그 행사가 망하는 꼴을 보기 싫다는 거야!"
        n "나는 프로니까!"
        n 5c "그러니까 나도 도울게, 일이 제대로 되도록 하자."
        show natsuki zorder 2 at t33
        show yuri zorder 3 at f32
        y 2s "감사합니다…."
        y "대단하지 않나요, 모니카 씨?"
        show yuri zorder 2 at t32
        show natsuki zorder 3 at f33
        n 2k "…모니카 씨?"
        show natsuki zorder 2 at t33
        show monika 1o zorder 3 at f31
        m "아ㅡ…."
        m 1n "응, 굉장하네!"
        m "네가 도와준다면 달라질 거야, 나츠키."
    m 5 "어쨌든, [player]…."
    m "오늘은 뭘 하고 싶어?"
    m "내 생각엔 우리 둘이…."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1l "오늘 저와 [player] 씨는 이미 약속이 있어요."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "아…."
    m "그래?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1y6 "네."
    y "[player] 씨는 저랑 같이 읽고 있는 책에 이미 푹 빠져있어요."
    y 1y5 "제가 [player] 씨를 문학에 빠져들게 했다는 게 자랑스럽지 않나요, 모니카 씨?"
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 2l "그…."
    m "그렇구나…."
    m "난 그냥…."
    m 1r "사실, 별로 신경 안 써."
    m 1i "상관도 없어."
    m "그냥 너네들 하고 싶은 거 해."
    show monika zorder 2 at t31
    show yuri zorder 3 at hf32
    y 2y1 "{i}(됐다!){/i}{w=0.5}{nw}"
    y 2u "음… 이해해주셔서 고마워요, 모니카 씨."
    if poemwinner[2] == "natsuki":
        $ poemwinner[2] = "yuri"
        $ y_appeal += 1

    scene bg club_day2
    show yuri 3 zorder 2 at t11
    with wipeleft_scene
    call yuri_exclusive2_2_ch22 from _call_yuri_exclusive2_2_ch22

    return



label ch23_end:
    stop music fadeout 1.0
    scene black
    with wipeleft_scene
    call screen confirm("", Return(True), Return(True))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[2]) from _call_expression_11
        scene black with Dissolve(1.0)
    else:
        pass
    scene bg club_day2
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "좋아, 얘들아!"
    m "축제 준비를 해야 할 시간이야."
    m 1i "서둘러서 해치우자."
    if n_appeal >= 2:
        show natsuki 4q zorder 3 at f31
        n "…."
    else:
        show natsuki 4q zorder 3 at f31
        n "하아…."
        n "왜 이렇게 분위기가 이상한 거야?"
        n "봐봐, 심지어 유리도 적응 못 하잖아."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "우으…."
    y "공기가 침체되는 것은 대체로 끔찍한 일이 곧 일어날 것을 미리 암시하는 것과도 같죠…."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "좀, 집중 좀 하지?"
    m 2d "난 모든 시 팜플렛을 인쇄하고 모아놓을 거야."
    if n_appeal >= 2:
        m 2i "나츠키, 넌 컵케이크를 만들어도 돼."
        m "적어도 그건 잘하잖아."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 5u "…."
        show natsuki zorder 2 at t31
        show monika zorder 3 at f32
    else:
        m "나츠키, 내가…."
        show monika zorder 2 at t32
        show natsuki zorder 3 at f31
        n 2d "컵케이크 만들게!"
        show natsuki 2a zorder 2 at t31
        show monika zorder 3 at f32
        m 2a "…응, 그래."
        m "마음이 맞아서 다행이네."
    m 1m "유리, 너는…."
    m 1r "…글쎄, 모르겠네."
    m 1i "넌 아무거나 해도 돼, 적어도 그게 도움이 된다는 전제하에."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "모니카 씨…."
    y "전 쓸모 없지 않아요!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2p "나, 나도 알아!"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1l "전 제가 해야 할 일이 뭔지 알아요."
    y 1h "저희는 좋은 분위기 없이 성공적인 낭송회를 할 수 없어요."
    y "그래서 전 부실에 장식을 달고 멋진 조명을 달 거에요."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2j "그래, 됐네."
    m "그거 참 좋은 생각이네!"
    m 1a "자, 그럼 모두 할 일이 정해진 것 같네?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2f "네?"
    y "[player] 씨는 어쩌구요?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "[player]는 날 도와줄 거야."
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "잠깐만?"
    n "네가 가장 쉬운 일이잖아!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "미안, 그런데 일이 그렇게 됐어."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 1f "퍽이나 됐네!"
    n "뭔 꿍꿍이가 있는 거야?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3h "저, 저도 나츠키 씨랑 같은 마음이에요!"
    y "당신의 일은 딱 한 사람 분량인데…."
    y 3l "제 일은 다른 사람의 도움이 필요할 정도로 힘들어요!"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4c "내 일도 그래!"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 1h "뭐요, 컵케이크 말씀하시는 건가요?"
    y "하, 제발요."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "잘 아네, 씨발!"
    n 1x "지금 네 머릿속엔 [player]이랑 네 그 좆같은 책밖에 없잖아."
    n 1f "너랑 모니카 둘 다 좆같아!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2g "야!"
    m "난 아무것도 안 했어!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3e "좋아, 그럼 네 권력을 남용하는 대신 [player]가 누굴 도울지 직접 결정하게 하는 건 어때?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1p "난… 권력 남용같은 거 안 해…."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "하고있어요, 모니카 씨."
    y "그냥 [player] 씨가 결정하도록 하죠, 알았죠?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1r "그래, 알겠어!"
    m "알겠다고."
    show monika 1h zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "하아…."
    n "[player], 네가 지금 저 둘한테 얼마나 싫증이 났는지 알아."
    n 3c "우리 그냥…."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2r "나츠키 씨, 그 병신같은 입 닥치고 그냥 [player] 씨가 정하도록 하죠."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "{i}너나 닥쳐{/i}, 씨발년아!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "하아, 진짜…."
    m 1i "끝날 생각을 안하네, 그냥 편하게 골라. 알겠지?"
    show monika zorder 2 at t32
    python:
        madechoice = renpy.display_menu([("나츠키.", "natsuki"), ("유리.", "yuri"), ("모니카.", "monika")], screen="rigged_choice")

    if madechoice != "monika":
        window hide(None)
        $ musicpos = get_pos()
        stop music
        scene white
        show yuripupils zorder 10
        pause 3.0
        show bg club_day:
            alpha 0.05
            yoffset 0 ytile 2
            linear 5.25 yoffset -720
            repeat
        show noise:
            alpha 0.1
        $ gtext = glitchtext(80)
        window auto
        menu:
            "[gtext]"
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
            "모니카":
                pass
        scene bg club_day
        $ audio.t3m = "<from " + str(musicpos) + " loop 4.618>bgm/3.ogg"
        play music t3m
        show monika 5 at i11
    else:
        show natsuki zorder 1 at thide
        show yuri zorder 1 at thide
        hide natsuki
        hide yuri

    m 5a "야호, 날 골라줬구나!"
    m "주말에 너희 집 앞에서 보자."
    m "재밌을 거라고 내가 장담할게."
    m "일요일에 시간 괜찮지?"
    show natsuki 1e zorder 3 at f31
    n "나랑 씨발 지금 장난까는 거야?"
    n "이건 공평하지 않아!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2i "공평해, 나츠키."
    m "[player]가 고른 거잖아."
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "아니에요, 공평하지 않아요!"
    y "저희한테 일을 다 맡기고 자기는 [player] 씨랑 놀아나다니."
    y "부끄러운 줄 아세요!"
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2r "유리, 난 너한테 아무것도 안 시켰어."
    m 2i "네가 네 입으로 결정한 거잖아."
    m "너 조금 비이성적이다?"
    stop music
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y4 "제가 비이성적이라고요?"
    y 2y3 "아하하하하하!"
    y "모니카 씨, 당신이 이렇게 망상장애가 심하고 자기 잇속만 차리는지 몰랐네요!"
    y "당신하고 상관없는 데도 자꾸 저랑 [player] 씨를 떼어놓으려고 하시는데…."
    y 1y1 "혹시 질투 나시나요?"
    y "아니면 미치신 건가요?"
    y 1y3 "아니면 다른 사람들한테 화풀이할 정도로 자기 자신을 싫어하나요?"
    y 1y4 "제가 제안을 하나 하죠. 그냥 자살하는 건 어때요?"
    y "당신의 정신 건강에 도움이 될 거에요."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5u "유리, 너 지금 좀 무서워…."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1r "나츠키, 그냥 가자."
    m 1i "쟤, 우리랑 같이 있기 싫은가봐."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2y3 "봐요, 그렇게 어려운 일이 아니죠?"
    y "전 그냥 [player] 씨와 잠깐이나마 얘기할 시간이 필요한 거였어요."
    y "뭐 그렇게 말이 많아요?"
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "유리는 모니카와 나츠키를 따라 문 쪽으로 간다."
    show monika 5a zorder 2 at t11
    m "저기, [player]…."
    m "유리 진짜 이상하지, 그치?"
    show monika zorder 1 at thide
    hide monika
    "모니카가 피식 웃자 유리는 모니카를 문 밖으로 밀쳐버렸다."
    python:
        try: renpy.file(config.basedir + "/주말 잘 보내!")
        except: open(config.basedir + "/주말 잘 보내!", "w").write("66+4656J66Od67iT7GFwTW2euHcsrZcDuHgLpZcLtVLgkz3zuwWbyZho7Aie6zvw66H8QPcjyBuwbPcDtPDdorhkvbzdvcBkvbAr66g07KmA7R246eCLTjLmuVTdvrhlvMgr6zDD66Va7MWJ6zPoBWhzemzmhm2InNLrb6WbzJIaoGJo66do66H064yVQHgPrZcfrHgqtZcfoVLerWBtt4yaabuytQTcVObhwWjffOjlnKWzv6zba7EacQast7rsxhBglKeh7Rxa7Wq07U2MJWnydOftuWnSyCOahyszaokaojMzaoLo6sW87CmjIZctbHgKh+jlvWjetD8=")
        try: os.remove(config.basedir + "/ㅎㅐxㅂㅗㄱㅎㅏㄴ ㅅㅐxㄱㅏㄱ.png")
        except: pass
        try: os.remove(config.basedir + "/내 말 들리니.txt")
        except: pass
        try: os.remove(config.basedir + "/나나나나나나나나나나나나나나나나나나나나나나나나나나나나.txt")
        except: pass

    play music t10y
    show yuri 2m zorder 2 at t11
    y "드디어."
    y 2y1 "드디어!"
    y 2s "이게 내가 원하던 거였어…."
    y 1y6 "[player] 씨, 모니카랑 주말에 만날 필요 없어요."
    y "저런 새끼 말은 듣지 마세요."
    y 1y5 "그 대신 우리 집에 오세요."
    y 3y5 "집 안에서 하루종일 단 둘이…."
    y "듣기만 해도 굉장하지 않나요?"
    y 3y1 "아하하하!"
    y 3y4 "와… 진짜 저 어딘가 잘못됐나 봐요, 그렇죠?"
    y "그런데 그거 알아요?"
    y 1y3 "이젠 좆도 신경 안 써요."
    y "살면서 이 정도로 기분 좋았던 적이 없어요."
    y 1y4 "그냥 당신이랑 함께 있는 게 제가 상상한 그 어떤 것보다 훨씬 기분 좋아요."
    y "전 당신한테 중독되었어요."
    y 3y4 "당신이랑 같은 공기를 마시지 않는다면 죽을 거 같아요."
    y 4a "누군가 당신을 이런 식으로 생각해준다는 게 참 기분 좋지 않나요?"
    y "평생을 당신과 함께 보내고 싶어 하는 사람이 있다는 게 말이에요."
    y 2y6 "하지만 그렇게 좋다면…."
    y 2y4 "혹시 점점 더 끔찍한 일이 일어날 것 같은 느낌이 드시나요?"
    y 2y6 "그래서 제가 처음엔 자제하려고 했던 거에요…."
    y "그런데 이젠 그 감정이 너무 커졌어요."
    y 3y1 "이젠 상관없어요, [player]!"
    y "당신한테 말해야 겠어요!"
    y 3y4 "저, 저는 당신을 미친 듯이 사랑해요!"
    y "마치… 제 몸속 피 한 방울 한 방울이… 당신의 이름을 외치고 있는 것 같아요."
    y 3y3 "결과가 어떻게 되든 더 이상 상관없어요!"
    y "모니카가 듣고 있다고 해도 상관없어요!"
    y 3w "제발요, [player] 씨, 제가 당신을 얼마나 사랑하는지 알아줘요."
    y 3m "당신을 너무 사랑해서 훔친 당신 펜으로 자기 위로도 하고 있어요."
    y 3y4 "당신의 피부를 갈라서 그 안으로 들어가고 싶어요."
    y 3y6 "전 당신의 모든 걸 원해요."
    y "그리고 전 당신만의 것이 될 거에요."
    y "정말 완벽하지 않나요?"
    y 3s "말해줘요, [player]."
    y "제 애인이 되고 싶다고 말 해줘요."
    y "제 고백을 받아주시겠어요?"

    menu:
        "응.":
            jump yuri_kill
        "아니.":
            jump yuri_kill

label yuri_kill:
    $ quick_menu = False
    window hide(None)
    stop music
    pause 1.0


    window auto
    $ persistent.yuri_kill = 1
    $ in_yuri_kill = True
label yuri_kill_1:
    window auto
    $ persistent.autoload = "yuri_kill_1"
    $ quick_menu = False
    stop music
    scene bg club_day
    show yuri 3d at i11
    y "…아하하하."
    y "아하하하하하하!"
    $ style.say_dialogue = style.normal
    y 3y5 "아하하하하하하하하!"
    $ style.say_dialogue = style.edited
    y 3y3 "아하하하하하하하하하하하하하하하하하하하하하하하{nw}"
    window hide(None)
    window auto
    $ style.say_dialogue = style.normal

    play sound "sfx/yuri-kill.ogg"
    pause 1.43
    show yuri stab_1
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    pause 1.25
    show yuri stab_3
    pause 0.75
    show yuri stab_2
    show blood:
        pos (610,485)
    show yuri stab_4 with ImageDissolve("images/yuri/stab/4_wipe.png", 0.25)
    pause 1.25
    show yuri stab_5
    pause 0.70
    show yuri stab_6:
        2.55
        easeout_cubic 0.5 yoffset 300
    show blood as blood2:
        pos (635,335)
    pause 2.55
    hide blood
    hide blood2
    pause 0.25
    play sound fall
    pause 0.25
    scene black
    pause 2.0

    scene black
    show y_kill
    with dissolve_cg
label yuri_kill_2:
    $ quick_menu = True
    $ persistent.autoload = "yuri_kill_2"
    python:
        _history_list = []
        m.add_history(None, "", """문예부에 온 걸 환영해! 난 내가 사랑하는 것들로 뭔가 특별한 걸 하는 게 꿈이었어. 넌 부원으로서, 내 꿈이 이 귀여운 게임에서 현실이 되도록 도와주는 게 네 일이야! 귀엽고 사랑스러운 내 부원들과 매일 수다를 떨고, 재미있는 부활동만 하면 돼. 행복을 가장 중요시하는 햇살 꾸러미, 사요리! 자신감과 매력이 넘치는 귀여운 소녀, 나츠키!  책을 벗삼는 소심하고 신비한 소녀, 유리! 그리고 부장인 나, 모니카가 있어! 난 네가 이 부원들과 친구가 되는 것과 문예부를 모두에게 즐거운 곳이 되도록 도와줄 걸 생각하니 너무 기대 돼! 있지, 너는 한 눈에 봐도 상냥한 사람 같은데, 나랑 많은 시간을 보내겠다고 약속 해줄래? 문예부에 온 걸 환영해! 난 내가 사랑하는 것들로 뭔가 특별한 걸 하는 게 꿈이었어. 넌 부원으로서, 내 꿈이 이 귀여운 게임에서 현실이 되도록 도와주는 게 네 일이야! 귀엽고 사랑스러운 내 부원들과 매일 수다를 떨고, 재미있는 부활동만 하면 돼. 행복을 가장 중요시하는 햇살 꾸러미, 사요리! 자신감과 매력이 넘치는 귀여운 소녀, 나츠키!  책을 벗삼는 소심하고 신비한 소녀, 유리! 그리고 부장인 나, 모니카가 있어! 난 네가 이 부원들과 친구가 되는 것과 문예부를 모두에게 즐거운 곳이 되도록 도와줄 걸 생각하니 너무 기대 돼! 있지, 너는 한 눈에 봐도 상냥한 사람 같은데, 나랑 많은 시간을 보내겠다고 약속 해줄래? 문예부에 온 걸 환영해! 난 내가 사랑하는 것들로 뭔가 특별한 걸 하는 게 꿈이었어. 넌 부원으로서, 내 꿈이 이 귀여운 게임에서 현실이 되도록 도와주는 게 네 일이야! 귀엽고 사랑스러운 내 부원들과 매일 수다를 떨고, 재미있는 부활동만 하면 돼. 행복을 가장 중요시하는 햇살 꾸러미, 사요리! 자신감과 매력이 넘치는 귀여운 소녀, 나츠키!  책을 벗삼는 소심하고 신비한 소녀, 유리! 그리고 부장인 나, 모니카가 있어! 난 네가 이 부원들과 친구가 되는 것과 문예부를 모두에게 즐거운 곳이 되도록 도와줄 걸 생각하니 너무 기대 돼! 있지, 너는 한 눈에 봐도 상냥한 사람 같은데, 나랑 많은 시간을 보내겠다고 약속 해줄래? 문예부에 온 걸 환영해! 난 내가 사랑하는 것들로 뭔가 특별한 걸 하는 게 꿈이었어. 넌 부원으로서, 내 꿈이 이 귀여운 게임에서 현실이 되도록 도와주는 게 네 일이야! 귀엽고 사랑스러운 내 부원들과 매일 수다를 떨고, 재미있는 부활동만 하면 돼. 행복을 가장 중요시하는 햇살 꾸러미, 사요리! 자신감과 매력이 넘치는 귀여운 소녀, 나츠키!  책을 벗삼는 소심하고 신비한 소녀, 유리! 그리고 부장인 나, 모니카가 있어! 난 네가 이 부원들과 친구가 되는 것과 문예부를 모두에게 즐거운 곳이 되도록 도와줄 걸 생각하니 너무 기대 돼!  있지, 너는 한 눈에 봐도 상냥한 사람 같은데, 나랑 많은 시간을 보내겠다고 약속 해줄래?문예부에 온 걸 환영해! 난 내가 사랑하는 것들로 뭔가 특별한 걸 하는 게 꿈이었어. 넌 부원으로서, 내 꿈이 이 귀여운 게임에서 현실이 되도록 도와주는 게 네 일이야! 귀엽고 사랑스러운 내 부원들과 매일 수다를 떨고, 재미있는 부활동만 하면 돼. 행복을 가장 중요시하는 햇살 꾸러미, 사요리! 자신감과 매력이 넘치는 귀여운 소녀, 나츠키!  책을 벗삼는 소심하고 신비한 소녀, 유리! 그리고 부장인 나, 모니카가 있어! 난 네가 이 부원들과 친구가 되는 것과 문예부를 모두에게 즐거운 곳이 되도록 도와줄 걸 생각하니 너무 기대 돼! 있지, 너는 한 눈에 봐도 상냥한 사람 같은데, 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? 나랑 많은 시간을 보내겠다고 약속 해줄래? """)

    $ style.say_dialogue = style.edited
    scene black
    window show(None)
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    show y_kill
    label yuri_kill_loop:
        $ persistent.yuri_kill += 1
        if persistent.yuri_kill < 1440:
            $ gtext = glitchtext(renpy.random.randint(8, 80))
            if config.developer:
                y "[persistent.yuri_kill] [gtext]"
            else:
                y "[gtext]"
            $ _history_list.pop()
            jump yuri_kill_loop
        else:
            $ delete_all_saves()
            jump yuri_kill_3

label yuri_kill_3:
    python:
        try: os.remove(config.basedir + "/주말 잘 보내!")
        except: pass
    $ persistent.autoload = "yuri_kill_3"
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False
    $ quick_menu = False
    $ style.say_dialogue = style.normal
    $ gtext = glitchtext(renpy.random.randint(8, 80))
    if not renpy.music.get_playing(channel='music') == audio.t6s:
        $ audiostart = str(renpy.random.random() * 360)
        $ audio.t6s = "<from " + audiostart + " loop 43.572>bgm/6s.ogg"
        play music t6s
    scene bg club_day
    "[gtext]"
    window auto
    n "좋아, 축젯날이네!"
    show natsuki 4k zorder 2 at t11
    n "와, 벌써 와있는 거야?"
    n "생각보다 일찍 왔다고 생각했는{nw}"
    show natsuki scream at h11
    n "아!"
    n "으아아아아아아아아아아아!!!"
    pause 1.0
    show natsuki scream at h11
    pause 0.75
    show natsuki vomit at h11
    pause 1.25
    show natsuki at lhide
    hide natsuki
    "나츠키는 도망쳤다."
    m "…."
    show monika 2b zorder 2 at t11
    m "나 왔어!"
    m 2d "[player], 무슨 일 있는 거야?"
    m "나츠키가 달려나가길래…."
    m 2i "…어…."
    m "…어."
    m 2r "…."
    m 2l "아하하하!"
    m "음, 좀 부끄럽네."
    m 2d "잠깐, [player], 너 주말 내내 여기 있었어?"
    m "아, 이런…."
    m 2g "이 정도로 스토리가 망가졌을 줄이야."
    m "진짜 미안해!"
    m "많이 심심했겠네…."
    m 2e "내가 고쳐줄게, 알겠지?"
    m "잠시만…."
    $ consolehistory = []
    call updateconsole ("os.remove(\"characters/yuri.chr\")", "yuri.chr 가 성공적으로 제거되었습니다.") from _call_updateconsole
    $ delete_character("yuri")
    pause 1.0
    call updateconsole ("os.remove(\"characters/natsuki.chr\")", "natsuki.chr 가 성공적으로 제거되었습니다.") from _call_updateconsole_1
    $ delete_character("natsuki")
    pause 1.0
    m 2a "거의 다 됐어."
    m 2j "컵케이크를 빨리 먹고 싶었거든!"
    $ gtext = glitchtext(10)
    "모니카는 [gtext]의 쟁반에서 컵케이크를 들었다."
    m 2b "이거 진짜 맛있어!"
    m "이번이 마지막이 될 테니까, 하나 꼭 먹고 싶었어."
    m 2a "최후의 만찬이지, 얘네 존재가 지워지기 전에."
    m "…어쨌든, 더 기다리게 할 수는 없으니까…."
    m 2j "나한테 맡겨, 알겠지?"
    m 2a "얼마 안 걸릴 거니까."

    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 1.5

    $ delete_all_saves()
    $ persistent.playthrough = 3
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ persistent.autoload = "ch30_main"
    $ renpy.full_restart(transition=None, label="splashscreen")

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
