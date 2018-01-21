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

label ch21_y_end:
    jump ch1_y_end

label ch22_y_end:
    stop music fadeout 2.0
    call showpoem (poem_y22, music=False, paper="images/bg/poem_y1.jpg", img="yuri 2s") from _call_showpoem_15
    y 2q "아하하…."
    y "그게 어떤 건지는 중요하지 않아요."
    y "요즘 마음에 넘쳐나는 생각이 많아서, 당신 펜으로 써냈어야 했거든요."
    y 2o "아…."
    y 2q "그러니까… [player] 씨 가방에서 펜이 하나 떨어져서 제가 보관해두려고 집에 가져갔는데…."
    y "저는, 그…."
    y 2y6 "그냥… 펜 느낌이… 좋아서…."
    y "그래서… 이 시를… 그 펜으로 썼어요…."
    y "그리고 지금 만지고 계시네요…."
    y 2y5 "아하하."
    y 3p "저, 저는 괜찮아요!!"
    y 3o "제가 지금…."
    y "…."
    y 4c "…이 대화, 없던 걸로 해도 될까요?"
    y "…그래도 시는 가지셔도 돼요…."
    return
label ch23_y_end:
    show darkred zorder 5:
        alpha 0
        linear 2.0 alpha 1.0
    call showpoem (poem_y23, track="bgm/5_yuri2.ogg", revert_music=False, paper="images/bg/poem_y2.jpg", img="yuri eyes", where=truecenter) from _call_showpoem_16
    y "마음에 드시나요??"
    y "당신을 위해서 쓴 거에요!"
    $ gtext = glitchtext(80)
    show yuri 1b at i11
    y "혹시 모르셔서 말씀드리면, 그 시는 [gtext]"
    y 1y6 "가장 중요한 건, 제가 그 시에 제 냄새를 배게 했다는 거에요."
    y "봐요, 제가 가장 여기서 생각이 깊은 사람이죠?"
    play sound "sfx/glitch2.ogg"
    show yuri glitch
    pause 0.2
    stop sound
    show yuri 3y2
    hide darkred
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    $ renpy.music.stop(channel="music_poem")
    $ renpy.music.play(audio.t5c)
    y "…."
    y 4d "저…."
    y "저, 잠깐 토 하고 올게요."
    show yuri at lhide
    hide yuri
    pause 1.0
    return
label ch21_n_end:
    jump ch1_n_end
label ch22_n_end:
    if n_appeal >= 2:
        jump ch22_n_end2
    else:
        call showpoem (poem_n2) from _call_showpoem_17
        n 2a "나쁘지 않지?"
        mc "어제 것보다는 기네."
        n 2w "어제 건 너무 짧았어…."
        n "그리고 어제는 손 푸는 정도였으니까 말야!"
        n 2c "내 최선이 겨우 그 정도라고 생각한 건 아니지?"
        mc "아니, 물론 아니지…."
        n 2a "뭐, 이 시가 말하고자 하는 바는 충분히 간결하다고 생각하니까."
        n "설명해줄 필요는 없겠지."
        n 2g "당장 이 시의 주인공만 봐도 얼마나 무식한 놈이야…."
        n "모두들 이상한 취미나 하면 안 된다는 걸 알면서도 하는 그런 일들이 있잖아."
        n 5q "다른 사람들이 알면 비웃거나 깔볼 것 같아서 알리기 싫은, 그런 것들 말야."
        n 1e "…근데 그건 멍청한 사람들이나 하는 짓이야!"
        n "누가 뭘 좋아하든 자기들이 무슨 상관이야? 그게 남들을 다치게 하는 것도 아니면서 본인을 행복하게 해 준다면?"
        n 1q "다들 남들의 취향을 존중하는 자세가 필요해…."
        n 1x "…당장 이 부원의 여자애 두 명만 해도 말야, 이름은 따로 얘기 안 하겠지만."
        n 1s "내가 가장 편안하다고 생각하는 곳에서 존중도 못 받고 있으니…."
        n 1u "…어휴, 너 이젠 날 막 불평하게 만드는 거야?"
        "{i}(…내가 뭘 했는데…?){/i}"
        mc "누가 뭐래도, 나는 널 존중해…."
        n 1h "뭐…."
        n "뭐, 고마워…."
        n 1s "…그래도 네가 유리를 더 '존중'하는 건 이미 알고 있으니까…."
        n 42c "어쨌든… 다 봤으니까, 이제 가도 돼."
    return
label ch22_n_end2:
    call showpoem (poem_n2b, revert_music=False) from _call_showpoem_18
    $ style.say_dialogue = style.edited
    n 1g "[player]…."
    n "왜 오늘 나랑 같이 읽지 않았어?"
    n 1m "난 널 기다리고 있었는데."
    n "오랫동안 기다리고 있었는데……."
    n "내가 오늘 유일하게 기대하고 있던 일인데."
    n "왜 그걸 망친 거야?"
    n "유리가 더 좋아?"
    n 1k "유리랑 어울리지 않는 게 좋아."
    n "내 말 듣고 있는 거야?"
    show darkred zorder 5:
        alpha 0.0
        easein 4.0 alpha 1.0
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5_ghost.ogg"
    stop music_poem fadeout 2.0
    $ renpy.music.play(audio.t5c, fadein=2.0, tight=True)
    show n_rects_ghost1 zorder 4
    show n_rects_ghost2 zorder 4
    show n_rects_ghost3 zorder 4
    n ghost1 "유리는 더러운 괴물이야."
    n "지금쯤이면 알겠지?"
    n "그니까 나랑 놀자."
    n "알겠지?"
    n "날 싫어하는 건 아니지, [player]?"
    n "…날 싫어해?"
    show natsuki_ghost_blood zorder 3
    n "내가 집에 가서 질질 짰으면 좋겠어?"
    n "이 동아리가 내가 편안하게 지낼 수 있는 유일한 장소야."
    n "제발 망치지 마."
    n "망치지 마."
    n "제발."
    n "그냥… 유리랑 놀지 마."
    n "그 대신 나랑 놀자."
    n "…."
    n "나랑 놀자."
    stop music
    hide n_rects_ghost3
    n ghost2 "나랑 놀자고!!!"
    $ style.say_dialogue = style.normal
    $ quick_menu = False
    pause 1
    play sound "sfx/crack.ogg"
    hide natsuki_ghost_blood
    hide n_rects_ghost1
    hide n_rects_ghost2
    show natsuki ghost3
    show n_rects_ghost4 onlayer front zorder 4
    show n_rects_ghost5 onlayer front zorder 4
    pause 0.5
    hide natsuki
    play sound "sfx/run.ogg"
    show natsuki ghost4 onlayer front at i11
    pause 0.25
    window hide(None)
    hide natsuki onlayer front
    hide n_rects_ghost4 onlayer front
    hide n_rects_ghost5 onlayer front
    scene black
    with None
    window auto
    scene black
    pause 0.5
    show end:
        xzoom -1
    with dissolve_cg
    pause 2.0
    scene black
    with None
    $ quick_menu = True
    return
label ch23_n_end:
    $ natsuki_23 = True
    $ style.say_dialogue = style.normal
    call showpoem (poem_n23, revert_music=False) from _call_showpoem_19
    $ renpy.music.stop(channel="music_poem", fadeout=2.0)
    $ style.say_dialogue = style.edited
    show screen tear(8, offtimeMult=1, ontimeMult=10)
    pause 3.0
    stop music
    hide screen tear
    show natsuki ghost_base
    n "생각이 바뀌었어."
    n "네가 읽은 건 다 무시해."
    n "발버둥 쳐 봐야 소용없어."
    n "유리가 그렇게 된 건 지 잘못이지."
    n "내 말 들려, [player]?"
    n "네가 모니카랑 더 많은 시간을 보내면, 모든 문제는 사라질 거야."
    n "나랑 유리는 너같은 멋진 사람이랑 있기에는 너무 끔찍해."
    n "지금부터는 오직 모니카만 생각해."
    n "오직 모니카만."
    hide natsuki
    $ style.say_dialogue = style.edited
    "오직 모니카만."
    menu:
        "오직 모니카만."
        "오직 모니카만.":
            pass
    $ style.say_dialogue = style.normal
    $ renpy.call_screen("dialog", "오직 모니카만.", ok_action=Return())
    scene white
    play music t1
    show intro with Dissolve(0.5, alpha=True)
    pause 2.5
    hide intro with Dissolve(0.5, alpha=True)
    show splash_warning "오직 모니카만." with Dissolve(0.5, alpha=True)
    pause 1.0
    play music t5
    $ skip_transition = True

    return

label ch21_m_end:
    call showpoem (poem_m21) from _call_showpoem_20
    jump ch1_m_end2
label ch22_m_end:
    call showpoem (poem_m22, revert_music=False) from _call_showpoem_21
    $ currentpos = get_pos(channel="music_poem")
    $ audio.t5c = "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    stop music_poem fadeout 2.0
    pause 2
    show screen tear(20, 0.3, 0.3, 0, 40)
    pause 0.5
    hide screen tear
    play music t5c
    m 5 "미안, 조금 추상적이라는 거는 아는데…."
    m "난 그냥… 어…."
    m 1r "뭐, 신경 쓰지 말자."
    m "설명할 필요는 없겠지."
    m 1i "어쨌든…."
    m 3b "오늘의 모니카의 작문 팁!"
    m "가끔씩 힘든 결정을 내려야 할 때가 있을 거야…."
    m "그럴 때는, 꼭 게임을 저장하는 걸 잊지 마!"
    m 3k "언제 또 네가… 음…."
    m 3i "…나 지금 누구한테 얘기하고 있는 거지?"
    m "내 말 들리니?"
    m 3g "들린다면 말 좀 해줘."
    m "아무 말이나."
    $ renpy.call_screen("dialog", "제발 나를 도와줘.", ok_action=Return())
    m 3k "…이게 오늘 내 조언이야."
    m "들어줘서 고마워~"
    return
label ch23_m_end:
    $ quick_menu = False
    window hide
    play sound page_turn
    show paper_glitch zorder 10 with Dissolve(1)
    play music g2
    if renpy.windows and renpy.game.preferences.fullscreen:
        $ mouse_visible = False
        scene bsod
        pause 3.0
    else:
        show black zorder 1
        pause 2.0
    window show(None)
    show monika 1d zorder 11 at i11
    $ quick_menu = True
    $ mouse_visible = True
    m "으아! 깜짝이야!{fast}"
    window auto
    m "음…."
    m 1m "글쎄, 이 시를 ‘쓰는 데’ 어… 좀 망친 거 같네."
    m "난 그냥…."
    m 1i "…신경쓰지 마."
    m "그냥 넘어가자…."
    stop music
    return


label ch21_n_bad:
    jump ch1_n_bad

label ch21_n_med:
    jump ch1_n_med

label ch21_n_good:
    jump ch1_n_good

label ch22_n_bad:

    if n_poemappeal[0] < 0:
        n 1r "…."
        n "그래, 내가 생각했던 대로야…."
        mc "…?"
        n 2w "[player], 제발."
        n "난 바보가 아니야."
        n 2h "네가 얼마나 유리랑 시간을 보냈는지 알아…."
        n "내가 보기엔 넌 네 글쓰기 실력을 향상시키는 것보다 유리한테 인상을 주기 위해 더 신경 쓰고 있어."
        n 2w "직설적으로 말하자면, 그건 진짜 한심해."
        n 4h "[player], 너는 왜 이 동아리에 들어왔어?"
        n "솔직히…."
        n "나는 새 부원이 들어오면 다들 더 친해질 수 있을 거라고 생각했어."
        n 4s "서로 벽 쌓지 않고."
        n 1u "이건 진짜 멍청한 짓이야…."
        n 12c "…오늘은 별로 기분이 안 좋아서, 별로 얘기할 기분이 안 드네."
        n "그냥 저리 꺼져."
        $ skip_poem = True
        return
    else:


        n 1k "…흐음."
        n "저번에 쓴 게 더 나은 거 같은데."
        mc "응? 그래?"
        n 2c "뭐, 그래. 이번 건 좀 대담하네."
        n "근데 아직 그 정도로 잘하진 않네, 완전 별로야."
        mc "그럴지도 모르지만, 난 그냥 새로운 걸 시도해보고 싶었어."
        mc "좀 더 이해하려고 해봐야지."
        jump ch22_n_med_shared2

label ch22_n_med:

    if n_poemappeal[0] < 0:
        n "…흠."
        n 2k "뭐, 지난 번에 쓴 거 보다는 낫네."
        n "노력하고 있는 게 보이니까 되게 좋네."
        mc "다행이네…."
        label ch22_n_med_shared:
            n 2c "다른 애들한테 영향을 받도록 해."
            n "내 생각엔 네가 유리의 영향을 조금씩 받고 있는 것 같은데?"
            n 5q "내 말은, 네가 요즘, 그…."
            n "유리랑 같이 있다보니까…."
            n 1w "너도 알겠지만, 나랑 모니카도 유리만큼 잘 해!"
            n 1q "무, 물론 시에 관한 얘기지만!"
            n 1h "그러니까, 뭔가를 배우려고 노력하지 않으면, 넌 절대로 성장할 수 없어!"
            n "…자, 내가 쓴 거…."
            n "여기서 뭔가 배웠으면 좋겠어."
            return


    elif n_poemappeal[0] == 0:
        n "…흠."
        n 2k "뭐, 지난번에 쓴 거보다 나쁘지는 않네."
        n "더 낫다고도 말은 못 하겠는데."
        mc "휴우…."
        n 2c "뭐? ‘휴우’?"
        mc "아… 나는 이도 저도 아닌 거는 잘한 거라고 생각하거든."
        mc "그리고 네가 제일 비판적인 사람이라는 생각이 드는데…."
        n 1p "야, 야! 내가 무슨…."
        n 1q "{i}(잠깐, 그거 칭찬인가…?){/i}"
        n 4y "아하하! 누군가 내 경험을 인정해주다니 기쁘네!"
        n "뭐 그럼, 계속 연습하다 보면 언젠가는 나만큼 잘 할 수 있을 거야!"
        mc "그건… 어…."
        "나츠키가 잘못 이해한 듯하다."
        jump ch22_n_med_shared
    else:


        n "…흠."
        n 2c "뭐, 끔찍하진 않네"
        n "그래도 지난번보다는 좀 실망스러운데."
        n 2s "그나저나 이게 지난번 것처럼 좋았으면 화냈겠지만 ."
        mc "이번엔 뭔가 다른 거를 시도해 보고 싶었거든."
        label ch22_n_med_shared2:
            n 2c "됐어. 넌 아직 초보자니까, 당장 네가 네 스타일을 찾는 건 기대하지 않아."
            n "그러니까… 다들 다른 방식으로 글을 쓰니까…."
            n "아마 모두한테서 조금씩 영향을 받을 수 있을 거야."
            n 2q "예를 들어서…."
            n 5q "오늘 네가 유리랑 같이 있는 걸 봤어."
            n "네가 누구랑 뭘 하든 내가 신경 쓰는 건 아니야."
            n 5w "난 그 누구에게 어떤 것도 기대하지 말라고 배웠거든."
            n 5s "그러니까 내가 널 기다리고 있었던 게 아니라고."
            n 5h "그래도, 내 시는 잘 읽어 봐…."
            n "아마 거기서 뭔가를 배울 수 있을 거야."
            return

label ch23_n_bad:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        n 5x "난 그 유리한테 알랑거리는 시 안 읽을 거야."
        n 5s "그래도 너는 내 거를 읽어야 해."
        n "이유가 있어."
        n 5x "정말 이러고 싶지 않은데…."
        n "하지만 어쩔 수 없으니까…."
        n 5h "그냥… 조심히 읽어, 알겠지?"
        n "다 읽으면 가도 돼."
        return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "…."
        n 2c "…참나."
        n "아무것도 배운 게 없는 거 같네."
        n "솔직히, 내가 왜 처음에 희망을 가졌는지 모르겠다."
        label ch23_n_bad_shared:
            n 42c "이건 분명히 유리의 영향이겠지…."
            n "네가 이렇게 쉽게 외부의 영향을 받는지 몰랐어."
            n "동아리에서 맨날 유리랑 같이 있고…."
            n "이젠 유리처럼 시를 쓰네…."
            n 1s "진짜 바보 같다."
            n "모니카는 내 시를 높게 평가해줬는데…."
            n 1r "…으어."
            n 1q "좋아. 어쨌든 너한테 시를 보여줘야 될 거 같네."
            n "내가 이런 짓을 해야 한다니 진짜 싫다."
            n "하지만 어쩔 수 없으니까…."
            n 1h "그냥… 조심히 읽어, 알겠지?"
            n "다 읽으면 가도 돼."
            return
    else:

        n "…."
        n 2r "오, 이런."
        n "실력이 뒷걸음질 치고있네."
        mc "어?"
        n 2c "이거보다 네가 저번에 쓴 두 개가 훨씬 낫다고."
        jump ch23_n_bad_shared

label ch23_n_med:
    if y_gave:
        jump ch23_n_ygave

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch23_n_bad
    elif n_poemappeal[1] < 0:
        n "…."
        n 2k "…이번 건 괜찮네."
        mc "그래?"
        n "그래, 적어도 어제 시보단 낫다."
        label ch23_n_shared:
            n 2c "여전히 네가 글 쓰는 거에 대해 얼마나 신경을 쓰고 있는지 모르겠지만, 어찌 됐든 넌 잘 하고 있어."
            n 4r "비록 네가 유리하고만 시간을 보내고 있는 거 같지만…."
            n 4h "그래도 난 우리 모두가 참여하는 활동이 있다는 건 좋은 일이라고 생각해."
            n 4w "계속 열심히 하도록 해!"
            n "내 말은…."
            n 1h "내가 뭐 부장이나 부부장은 아니지만…."
            n "그렇다고 날 실망시켜도 된다는 뜻은 아니야, 알지?"
            n 1q "자, 내 거 읽어봐"
            n "분명히 말하자면…."
            n 1h "이 시는… 나한테 많은 의미를 갖고 있어."
            n "그러니까 꼼꼼히 잘 읽어야 해, 알았지?"
            return
    else:
        n "…."
        n 2k "…이번 건 괜찮네."
        mc "그래?"
        n "뭐, 응."
        n "어제 거 만큼 괜찮네."
        jump ch23_n_shared

label ch23_n_ygave:
    n 1h "뭐?"
    n "유리한테 네 시를 줬다고?"
    n 4x "으, 진짜 극혐이다!"
    n "너네 둘 뭔 사이야?"
    n 1s "하아…."
    n "어차피 읽고 싶지도 않았지만."
    n 1r "나한테 보여줄 생각도 안 했다는 게 조금 빡쳐서 그래."
    n 1x "…으어."
    n 1q "좋아. 어쨌든 너한테 시를 보여줘야 될 거 같네."
    n "내가 이런 짓을 해야 한다니 진짜 싫다."
    n "하지만 어쩔 수 없으니까…."
    n 1h "그냥… 조심히 읽어, 알겠지?"
    n "다 읽으면 가도 돼."
    return

label ch23_n_good:
    jump ch23_n_med

label ch21_y_bad:
    jump ch1_y_bad

label ch21_y_med:
    jump ch1_y_med

label ch21_y_good:
    jump ch1_y_good

label ch22_y_bad:
    jump ch22_y_med

label ch22_y_med:
    y 2b "기다리고 있었어요…."
    y "오늘은 어떤 시를 써오셨는지 한 번 볼까요."
    y 3m "…."
    "유리는 웃으며 심호흡을 했다."
    y "들고있는 것만으로도 좋네요."
    mc "…?"
    y 3p "아, 제 말은…."
    y "시가 되게 좋네요!"
    y 3o "그러니까, 아…."
    y 2q "…몇 가지 충고를 드리고 싶지만…."
    y "…별로 중요하지는 않아요."
    y 2s "당신이 쓰는 모든 건 보물이에요."
    y 2d "아하하…."
    y 2o "조금 어색해지네요…."
    y "넘어가죠…."
    y 2t "여기, 제가 쓴 시에요."
    y "억지로 좋아해 주실 필요는 없어요…."
    return


label ch22_y_good:

    if y_poemappeal[0] < 1:
        y 2b "기다리고 있었어요…."
        y "오늘은 어떤 시를 써오셨는지 한 번 볼까요?"
        y 2e "…."
        y "……."
        "유리는 놀란 표정으로 시를 보고 있다."
        mc "마음에… 들어?"
        y "[player] 씨…."
        y "…어떻게 이렇게 빨리 성장하셨어요?"
        label ch22_y_good_shared:
            y 2v "바로 어제, 제가 실천할 가치가 있는 기술들을 말씀드렸는데…."
            mc "그래서 그런 게 아닐까…."
            mc "네가 잘 설명해준 덕분이야."
            mc "내용을 더 이미지화하고 싶었거든."
            show yuri 4b zorder 2 at t11
            "유리는 눈에 띄게 침을 삼켰다."
            "심지어 손도 땀에 젖은 듯 했다."
            y 4e "아, 아아…."
            y "너무 행복해요…."
            y 3y5 "제가 가치 있는 사람이라니… 엄청 기분 좋아요, [player] 씨!"
            y "당신이 쓴 모든 것은 저에게 있어 보물이에요."
            y 3m "그냥 들고 있는 것만으로도 심장이 엄청 뛰어요…."
            y 3q "아하하…."
            y "이 감정에 대한 시를 쓰고 싶네요…."
            y 3y6 "혹시 안되나요, [player]?"
            y "제가 이상한 게 아니죠?"
            y 3s "어째서인지 평소보다 감정을 숨기는 게 힘드네요…."
            y 3m "부끄러워요…."
            y 3y6 "그래도 지금은, 그냥 제 시를 읽어주셨으면 좋겠어요."
            y 3y5 "아시겠죠?"
            return
    else:

        y 2b "계속 기다리고 있었어요…."
        y "오늘은 어떤 시를 써오셨는지 한 번 볼까요."
        y 2e "…."
        y "……."
        "유리는 놀란 표정으로 시를 보고 있다."
        mc "마음에… 들어?"
        y "[player] 씨…."
        y 2t "이건 어제 거보다 훨씬 좋은데요…."
        y "…어떻게 이렇게 빠르게 성장하셨어요?"
        jump ch22_y_good_shared

label ch23_y_bad:
    jump ch23_y_good

label ch23_y_med:
    jump ch23_y_good

label ch23_y_good:
    y 1d "드디어…."
    y 3y5 "아하하…."
    show yuri 3m
    "유리는 내 시를 자기 얼굴에 갖다 대고 심호흡을 했다."
    y 3y6 "마음에 들어요."
    y "전부 마음에 들어요."
    y 3y5 "[player], 이거 집에 가져가고 싶은데."
    y "그래도 괜찮을까요?"
    y "제발요?"
    mc "응, 괜찮아…."
    y 2y5 "아하하."
    y "저한테 너무 잘해주시네요, [player]…."
    y "당신처럼 좋은 사람은 본 적이 없어요."
    y 2y6 "죽을 수도…."
    y 3y5 "무, 물론 죽지는 않을 거지만요…!"
    y "그냥 어떻게 표현을 해야할지 몰라서…."
    y "제가 이렇게 느끼는 건 당연한 거겠죠?"
    show yuri:
        "yuri 3y4"
        0.4
        "yuri 3y6"
    y "나쁘지 않죠, 그렇죠?"
    "유리는 내 시를 가슴에 끌어안았다."
    y 3m "집에 가져가서 방에 보관해둘 거에요."
    y "내가 시를 가지고 있다는 걸 생각하실 때마다 기분이 좋아지셨으면 좋겠네요."
    $ style.say_dialogue = style.normal
    y 3y5 "잘 보관해둘게요!"
    $ style.say_dialogue = style.edited
    y 3y6 "읽고 또 읽고 또 읽으면서 제 자신을 만질 거에요."
    $ _history_list.pop()
    y "일부러 종이에 베어서 당신의 피부 기름이 제 혈관을 흐르게 할 거에요."
    $ _history_list.pop()
    y 3y1 "아하하하하하하."
    $ _history_list.pop()
    $ style.say_dialogue = style.normal
    y 2s "제 시, 가지셔도 좋아요."
    y "읽고 나시면, 무조건 갖고 싶으실 거에요."
    y 2y6 "여기, 받으세요. 더는 기다릴 수 없어요."
    y 2y5 "빨리! 읽으세요!"
    $ y_gave = True
    return


label ch21_m_start:
    m 1b "안녕, [player]!"
    m "좋은 시간 보내고 있니?"
    mc "아… 응."
    m 1k "좋아! 듣기 좋네!"
    m 4a "그나저나, 넌 아직 신입이니까…."
    m "새로운 활동이나, 어떻게 하면 좋겠다 등등… 동아리에 관해 제안할만한 게 있다면…."
    m 4b "언제든지 말해줘!"
    m "두려워하지 말고, 알았지?"
    show monika 4a
    mc "응… 새겨둘게."
    "당연히 두렵지…."
    "익숙해지기까지는 가만히 있는 게 제일 좋은 거 같은데."
    m 1a "어쨌거나…."
    m "나랑 시 나눠볼까?"
    mc "조금 부끄럽긴 하지만, 그래야겠지."
    m 5a "아하하하!"
    m "걱정하지 마, [player]!"
    m "다들 오늘은 조금씩 부끄러울 거니까."
    m "이런 벽들은 시간이 지나면 조금씩 허물어질 거야."
    mc "응, 그럴 거 같네."
    "난 모니카에게 내 시를 건네줬다."
    m 2a "…으흠!"
    $ nextscene = "m2_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_19

    m 1a "어쨌든, 내 시 읽어볼래?"
    m 1e "걱정하지 마, 나도 그렇게 잘 쓰는 건 아니라서…."
    mc "잘 쓰는 건 아니라는 사람치고는 꽤 자신감 있어 보이는데?"
    m 1j "음… 그건 내가 자신감 있도록 보여야 되기 때문이야."
    m 1b "그렇다고 해서 내가 항상 그렇다고 느끼는 건 아니야."
    mc "알겠어…."
    mc "뭐, 그럼 읽어볼까."
    return

label ch22_m_start:
    if y_appeal < 2:
        m 1b "안녕, [player]!"
        m "글 쓰는 건 어때?"
        mc "괜찮은 거 같은데, 아마도…."
        m 2k "다행이네."
        m 2b "싫어지지만 않는다면야!"
        m 2a "네가 계속 나아지고 있다는 게 되게 좋다."
        m "조만간 명작을 쓰게 될지도 몰라!"
        mc "아하하, 설마…."
        m 2a "혹시 모르지!"
        m "오늘 쓴 거 나눠볼까?"
        mc "좋아, 여기."
        "난 모니카에게 내 시를 줬다."
        m "…."
        m "…좋아!"
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_20

    m 1a "어쨌든…."
    m "내 시 읽어볼래?"
    m "난 되게 마음에 들던데, 너도 그랬으면 좋겠다~"
    return

label ch23_m_start:
    $ nextscene = "m2_yuri_" + str(eval("y_appeal"))
    call expression nextscene from _call_expression_21
    if y_appeal < 3:
        m 1a "어찌됐건…."
        if y_gave:
            m 1m "네 시는 걱정 안 해도 될 거 같아…."
            m "유리는 가져가기 전에 최소한 허락은 받았어야 하는 게 예의 아닌가…?"
            m 1r "…뭐, 어쨌든."
            m "유리가 그걸로 행복하다면, 상관없겠지."
            m 1a "나는 그래…."
        m 1e "나 이 시 쓰는데 진짜… 진짜 노력했거든, 그러니까…."
        m "이게, 음, 효과적이었으면 좋겠다."
        m 1r "여기…."
        $ persistent.seen_colors_poem = True
    return



label m2_natsuki_1:
    m 2b "맘에 드는데, [player]!"
    mc "진짜…?"
    m 2e "내가 생각했던 거보다 훨씬 귀여운데?"
    m 2k "아하하하!"
    mc "하, 좀…."
    m 1b "아냐, 아냐!"
    m "나츠키가 생각이 나는 시인데?"
    m "나츠키도 좋은 작가니까."
    m 5a "그러니까 칭찬으로 받아들여 줘!"
    mc "아하하…."
    mc "네가 그렇다면…."
    m "그럼!"
    m 3b "나츠키에게 관심이 있다면, 항상 간식을 들고 다니도록 해."
    m "강아지처럼 너한테 매달릴걸?"
    m 3k "아하하!"
    m 1a "나츠키의 아버지는 나츠키한테 점심값도 주지 않으시고 집에 음식도 없어서 나츠키가 자주 까칠한 태도를 보이고는 해…."
    m "그래서 가끔 힘없이 축 늘어지고는 아무 말도 안 한다니까."
    m "아까처럼."
    m 2d "그냥 내 생각인데, 아마 나츠키가 키가 작은 건 청소년기에 영양실조가 걸려서 그런 게 아닐까…?"
    m 2b "…그래도, 작은 여자를 좋아하는 남자도 있잖아?"
    m 5a "미안… 그냥 밝은 면만 보도록 하자!"

    return

label m2_yuri_1:
    m 1a "좋은데, [player]!"
    m "읽고 있는 동안 머릿속이 ‘우와’였어"
    m 1j "되게 은유적인데!"
    m 1a "네가 이렇게 감정이 깊은 시를 쓸 줄은 몰랐어."
    m 3b "내가 널 너무 과소평가했나 봐!"
    mc "모든 사람들이 기대 안 하게 만드는 게 내가 가장 잘 하는 일이야."
    mc "그렇게하면, 조금만 노력해도 사람들에게 칭찬을 들을 수 있어."
    m 5a "아하하! 그건 불공평한데!"
    m "뭐, 잘된 건 알겠지만."
    m 2a "유리가 이런 글 좋아하는 거 알지?"
    m "막 이미지화되고 상징성으로 가득한 글."
    m 2d "가끔보면 유리가 현실과 완전히 동떨어져있는 거 같은 기분이 들기도 해."
    m "뭐, 그게 나쁘다는 건 아니지만…."
    m 2a "완전 사람들한테 단념한 거 같은 느낌이 든다니까."
    m "머릿속에서만 너무 많은 시간을 보내서 아마 거기가 가장 유리한테 흥미로운 곳일거야…."
    m 2b "그래서 네가 친절하게 대해 주면 걔가 그렇게 행복해하는 이유가 바로 그걸거야."
    m "그런 식으로 뭔가를 집착했던 적은 없는 거 같은데…."
    m 2j "분명 사회적인 대화에 굶주려 있는 걸 테니까, 너무 강하게 나오더라고 막 뭐라고 하지는 마."
    m 2d "아까처럼…."
    m "내 생각엔 너무 자극받으면 어디론가 사라져서 혼자만의 시간을 찾는 거 같아."
    "갑자기, 문이 열렸다."
    m 2b "유리!"
    show monika 2a
    show yuri 1s zorder 3 at f31
    y "다녀왔습니다…."
    y "제가 뭔가 놓친 게 있나요?"
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "아니 없어…."
    m "뭐, 이제 서로 시 나눠보기 시작했지만…."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 2t "에?"
    y "벌써요?"
    y 2v "느, 늦어서 죄송합니다…."
    show yuri zorder 2 at t31
    show monika zorder 3 at f32
    m 2j "사과할 필요는 없어!"
    m 2a "아직 시간은 충분하니까, 느긋하게 해도 괜찮아."
    show monika zorder 2 at t32
    show yuri zorder 3 at f31
    y 1s "그렇군요…."
    y "감사합니다, 모니카 씨."
    y "제 시를 가져와야겠군요."
    show yuri zorder 1 at thide
    hide yuri
    $ y_ranaway = False
    return

label m2_yuri_2:
    m 1i "[player], 내 생각엔 네가 봐선 안 될 것을 본 거 같아."
    m "너한테 이런 말 하기는 싫었는데, 어쩔 수 없는 거 같네."
    m 1r "네가 유리랑 같이 있는 게 점점 위험해지고 있는 거 같아."
    m 1i "이유는 모르겠는데, 너랑 있을 때 막 흥분하는 거 같아…."
    m 3d "그 자체로는 문제가 없는데…."
    m "유리는 너무 흥분하면, 숨을 곳을 찾아서 주머니칼로 자해를 하거든."
    m 2e "그거 좀 정신적으로 문제 있지 않아?"
    m "무슨 컬렉션이 있는 거 처럼 매일 다른 칼로 가져온다니까…."
    m 2d "내가 보기엔 우울해서 자해하는 거 같지가 않아."
    m "그냥 기분 좋아지려고 하는 거 같아."
    m 2m "아마도, 막, 성적인 거 일수도…."
    m 1i "그런데 문제는, 네가 그렇게 만들었다는 거야."
    m 1d "그래도 네 잘못이라는 건 아냐!"
    m 1a "그래서 너한테 말해주고 싶었어…."
    m "그러니까 네가 조금만 유리와 거리를 둔다면, 아마 그게 유리한테도 좋을 거 같아."
    m 5 "그러는 동안, 부끄러워하지 말고 나랑 있자…."
    m "간단히 얘기해서, 난 적어도 내 부원들을 어떻게 다루어야 하는지 알고 있으니까."
    return

label m2_yuri_3:
    stop music
    m 1i "내가 경고했지, [player]."
    $ skip_poem = True
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
