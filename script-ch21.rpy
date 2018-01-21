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

label ch21_main:
    $ finalConso = finalChecker(player)
    scene bg club_day2
    with dissolve_scene_half
    play music t2g3
    show monika 5 zorder 2 at t11
    show layer master:
        subpixel True
        truecenter
        linear 240 rotate 8 zoom 1.30
    m "안녕, [player]!"
    m "도망가지 않았다니 다행이네. 하하하!"
    mc "에이, 그런 걱정은 하지도 마."
    mc "난 한다면 하는 사람이라, 적어도 약속은 지켜."
    show monika zorder 1 at thide
    hide monika
    "결국, 난 문예부에 돌아왔다"
    "내가 마지막에 들어온 사람이라, 모두들 벌써 얘기를 나누고 있었다."
    show yuri glitch2 zorder 2 at t32
    y "약속을 지켜주셔서 고마워요, [player]."
    y 1a "글에 익숙치 않으실 텐데 이렇게 와 주시고."
    y 1u "저희가 괜히 너무 어려운 결정을 내리게 만든 건 아닌지…."
    show natsuki glitch1 zorder 2 at i33
    n "저기! 얘가 어떤 앤 줄은 알고 그러는 거야?"
    n 4e "넌 이미 모니카한테 끌려나갔어야 했어."
    n "네가 그냥 놀러 온 건지는 잘 모르겠지만…."
    n "진지하게 임하지 않으면, 오래 못 갈 줄 알아…."
    show monika 2b onlayer front at l41
    m "나츠키, 문예부실에 만화 컬렉션을 넣고 다니는 사람이 할 말은 아닌 것 같은데…."
    n 4o "몬…만……!"
    show monika onlayer front at lhide
    hide monika onlayer front
    "나츠키는 \"모니카\" 와 \"만화\"를 동시에 말하려다 혀가 꼬여버렸다."
    show natsuki at h33
    n 1v "만화도 문학이야!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "혼자 찌뿌둥해져서 꼬리를 말듯 자리에 앉는 나츠키."
    show yuri 2s zorder 2 at t11
    y "죄송해요, [player] 씨…."
    y "먼저 편안하신 게 가장 중요하겠죠?"
    show yuri 2g
    "유리는 나츠키를 실망한 눈빛으로 본다."
    y 1a "음, 아무튼…."
    y "일단 저희 부에 들어오셨으니…."
    y "…혹시 읽을 책 고르는 데 관심이 있으신가요?"
    mc "글쎄…."
    mc "관심이 있다고도, 없다고도 못 하겠네."
    mc "네가 말했듯이 일단 동아리에 왔으니까."
    mc "네가 관심을 가지라면 가져야겠지."
    y 4b "자, 잠시만요…."
    y "그런 뜻이 아니에요."
    y "우으…."
    y "원하지 않으신다면, 제가 말한 건 잊어버리셔도 좋아요…."
    mc "으아, 아냐. 그게 아냐, 유리…."
    mc "난 정말 이 부의 일원이 되고싶어."
    mc "비록 내가 책을 자주 읽지는 않지만, 네가 원한다면 기쁜 마음으로 책을 고를 거야."
    y 3t "저, 정말인가요…?"
    y "그렇다면…."
    y 3u "…전 일단 부부장이기도 하니까…."
    y "…좋아하실 수 있도록 도와드릴게요."
    "유리는 가방에서 책을 하나 꺼내어 건네주었다"
    y 1s "소외감을 느끼시지 않게…."
    y "그래서 좋아하실 만한 책을 골라봤어요."
    y "내용이 길지 않아서, 책을 자주 읽지 않더라도 집중할 수 있으실 거에요…."
    y "그리고, 그…."
    show yuri at sink
    y 4b "얘기할 거리도… 생기니까…."
    "이…이건…."
    "어떻게 여자들은 생각지도 못한 곳에서 귀여워질 수 있을까?"
    "심지어 직접 고민해서 내가 좋아할 만한 책을 골라줬어, 내가 책을 많이 읽지 않는다는 걸 아는데도 말야…."
    mc "유리, 고마워! 이 책, 무조건 읽을게!"
    "나는 매우 기뻐하며 책을 가져갔다."
    show yuri 2m zorder 2 at t11
    y "휴우…."
    y 2a "천천히 읽으셔도 좋아요."
    y "나중에 꼭 어땠는지 말씀해주셔야 해요."
    show yuri zorder 1 at thide
    hide yuri
    show layer master

    "이제 모두 왔으니 모니카가 준비해온 부 활동을 시작하겠지."
    "…라고 생각했건만 그게 아닌 것 같다."
    "유리는 책에 코를 박고 있다."
    "이때만을 기다렸다는 듯 긴장된 표정으로 책을 읽는 모습이 안 볼래야 안 볼 수가 없다…."
    "한편, 나츠키는 벽장 안을 뒤지고 있었다."


    $ nextscene = poemwinner[0] + "_exclusive2_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_24

    return

label ch21_end:
    stop music fadeout 1.0
    scene bg club_day2
    with wipeleft_scene
    play music t3g
    queue music t3g2
    mc "휴우…."
    "모두와 시를 나눠 보았다."
    "그리곤 잠시 교실을 둘러보았다."
    "생각했던 것보다 더 힘든 일이었다."
    "지극히 평범한 내 글쓰기 실력을 평가받는 꼴이라니…."
    "잘해주려고는 한다지만, 내가 봐도 내 시는 다른 애들 시에 비하면 그냥 낙서 수준이다."
    "하긴. 여기는 문예부니까."
    "나는 한숨을 쉬었다."
    "결국은 내가 자초한 일이니까."
    "방 맞은편에는 모니카가 공책에 뭔가를 쓰고 있었다."
    "내 눈은 유리와 나츠키에게 멈췄다."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "둘은 조심스레 서로의 시를 교환했다."
    show yuri 2i zorder 2 at t21
    "조용히 시를 읽어내려가는데, 표정이 바뀌는 게 눈에 보일 정도다."
    "나츠키는 답답해하며 눈썹을 찌푸리고."
    "유리는 슬프게 미소를 짓는다."
    show natsuki zorder 3 at f22
    n 1q "{i}(단어 선택이 왜이래…?){/i}"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2f "에?"
    y "어… 방금 무슨 말 하셨나요?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2c "아, 아무것도 아니야."
    "나츠키가 질렸다는 듯, 한 손으로 시를 책상에 내려놓는다."
    n "멋지네."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2i "아… 감사합니다…."
    y "나츠키 씨 건… 귀엽네요…."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2h "귀여워?"
    n 1h "혹시 상징적 표현을 아예 이해를 못한 거야?"
    n "이건 포기하는 감정에 대한 시야."
    n "그게 어떻게 귀여울 수가 있는 거야?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3f "저, 저도 그건 알아요!"
    y "제 말은…."
    y 3h "그 표현 방식, 말이에요…."
    y "전 그냥 좋은 말을 하려고 한건데…."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n "에?"
    n 4w "좋은 말을 하려고 노력했어야 할 만큼 못 썼다는 거야?"
    n "고마워, 하지만 별로 좋은 말인지는 모르겠어!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1i "음…."
    y "두 가지 의견이 있습니다만…."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 5x "흥."
    n "내가 의견을 듣고싶은 거였다면, 이걸 좋아하는 사람한테 물어봤겠지."
    n "물론 좋아하는 사람이 {i}있었고{/i}."
    n 5e "모니카가 좋아했어."
    n "그리고 [player]이도!"
    n "그러니까, 내가 친히 너에게 내 의견을 말해주지."
    n "우선……."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "죄송해요…."
    y "말씀은 감사하지만, 전 제 문체를 정하는데 엄청난 시간을 썼어요."
    y 2h "특별한 영감이 떠오르지 않는다면 바꾸지는 않을 것 같아요…."
    y "바꿀 생각도 없지만요."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "으으윽…!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1k "그리고 [player]씨는 제 시도 좋아한다고 했어요."
    y "그리고 인상 깊은 시였다고도 말해줬어요."
    stop music fadeout 1.0
    "나츠키가 갑자기 일어났다."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4y "호오?"
    n "네가 새 멤버한테 관심받는 데에 그렇게나 열중인 줄은 몰랐네, 유리."
    play music t7a
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "에…에?!"
    y "전 그런 게…!"
    y 1o "우으…."
    y "나… 나츠키 씨야말로…."
    "유리도 일어섰다."
    y 2r "[player]씨가 나츠키 씨 조언보다 제 조언을 더 좋아하셨다고 질투하시는 거 아니에요?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "참나! {i}내{/i} 조언을 더 좋아했는지 네 조언을 더 좋아했는지 네가 그걸 어떻게 알아?"
    n "네가 그렇게 잘났어?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "저는…!"
    y "아뇨…."
    y "제가 그렇게 잘났으면…."
    y 1r "…제가 하는 짓마다 과하게 귀엽게 하고 다녔겠죠!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "으으으으으으…!"
    n "있지, 그거 알아?!"
    n "난 누구처럼 [player]가 나타나고 나서 마법같이 가슴이 커지거나 하진 않거든!"
    show yuri 3p at h21
    show natsuki zorder 2 at t22
    y "나, 나츠키 씨"
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show monika 3l behind yuri, natsuki at l41
    m "저기, 나츠키, 그건…."
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "너랑은 관련 없잖아!\n모니카 씨는 상관없잖아요…!"
    show monika at lhide
    hide monika
    show yuri 2h zorder 2 at f21
    show natsuki zorder 2 at t22
    queue music t7g
    $ timeleft = 12.453 - get_pos()
    show noise zorder 3 at noisefade(25 + timeleft)
    show vignette as flicker zorder 4 at vignetteflicker(timeleft)
    show vignette zorder 4 at vignettefade(timeleft)
    show layer master at layerflicker(timeleft)
    y "자신의 불안감을 다른 사람한테 해소하는 건…."
    y "나츠키 씨의 외견만큼이나 어린 애처럼 행동하는 짓이에요."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4o "{i}내가?{/i} 누가 누구보고? 이 정서불안 걸린 년아!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "정서불안…?"
    y 2r "죄송하지만 제 인생은 당신처럼 정신연령이 낮은 사람이 이해할 수 있는 게 아니에요!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4f "그치?"
    n "그게 증명해주네."
    n 4e "대부분 중학교를 졸업하고 나면 스스로 극복하는 법을 배운다고들 하지."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y "증명하고 싶다면, 그딴 태도로 다른 사람들을 괴롭히는 건 그만두세요!"
    y "그냥 귀엽게 입고 다니고 행동하면 당신의 그 더러운 성격이 묻힐 거라고 생각했나요?"
    y 1k "진짜 귀여운 건 당신이 노력하는 거예요."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 2y "우와, 조심하지 않으면 불안해서 자해할 정돈데, 유리?"
    n "아, 미안. 이미 그러고 있지?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "지, 지금 제가 자해한다고 떠벌린 건가요?"
    y 3r "씨발, 도대체 머리에 뭐가 들은 거예요?!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "그래, 계속 해!"
    n "네 진짜 생각이 뭔지 [player]가 다 듣게 해!"
    n "끝나고 나면 너한테 완전 푹 빠져있을걸?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3n "아, 아…!"
    show yuri zorder 2 at t21
    "내가 옆에 있다는 걸 드디어 알아차린 유리는 갑자기 날 바라보며 섰다."
    show yuri zorder 3 at f21
    y 2n "[player] 씨…!"
    y "나… 나츠키 씨는 그냥 절 나쁜 사람으로 만드려고…!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "아니야!"
    n "유리가 먼저 시작했어!"
    show yuri 1t zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    $ style.say_dialogue = style.normal
    mc "…."
    $ style.say_dialogue = style.edited
    "{cps=*2}어쩌다 이게 이 지경까지 온거지?!{/cps}{nw}"
    "{cps=*2}내가 글쓰기에 그렇게 대단한 것도 아니고…{/cps}{nw}"
    "{cps=*2}가만, 이거 점수 딸 기회가 온게 아닐까?{/cps}{nw}"
    "{cps=*2}그렇다면야 나는…!{/cps}{nw}"
    $ style.say_dialogue = style.normal
    $ menu_clicked = 0
    window hide(None)
    label ch21_end_menu:
        menu:
            "나츠키.":
                jump menu_click
            "유리.":
                jump menu_click

    label menu_click:
        $ srf = screenshot_srf()
        show layer screens:
            truecenter
            zoom 1.00
        show screen tear(20, 0.1, 0.1, 0, 40, srf)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        hide screen tear
        stop sound
        $ menu_clicked += 1
        if menu_clicked < 9:
            show layer master:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            show layer screens:
                truecenter
                zoom 1.00 + menu_clicked * menu_clicked * 0.06
                yalign 0.25
            jump ch21_end_menu


    window show(None)
    stop music
    $ menu_clicked = 8
    $ quick_menu = False
    show layer master:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show layer screens:
        truecenter
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    show monika 1 onlayer front at i11:
        zoom 1.00 + menu_clicked * menu_clicked * 0.06
        yalign 0.25
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "…."
    show layer master
    show layer screens
    show monika 1 onlayer front at i11
    window auto
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "…."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "…."
    show monika 1m onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "어…."
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "저기, [player]야…."
    show monika 1e onlayer front at i11
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "우리 잠깐\n바깥 공기좀\n쐬고 올까?"
    $ renpy.display_menu(items=[('Natsuki.', True), ('Yuri.', True)], interact=False, screen='choice')
    m "괜찮지?"
    scene bg corridor
    hide monika onlayer front
    show monika 1n onlayer master at t11
    with wipeleft_scene
    $ quick_menu = True
    m "미안해…."
    m "쟤네가 너까지 끌어들일 줄이야…."
    m 1e "우리가 이렇게 나와 있는 게 훨씬 나을거야…."
    m "그만 싸울 때쯤 다시 들어가자."
    m 5 "아하하…."
    m "이런 부장이라니, 참 이상하지?"
    m 1m "부원들한테 직접 관여하지도 못하고…."
    m "내가 좀 더 당당해질 수 있다면 좋을 텐데…."
    m "이런 일이 일어나면 내가 먼저 중재해야 하는데, 용기가 안 나…."
    m 1e "넌 이해해줄 수 있지, 그치?"
    m "어쨌든…."
    m 1a "이게 널 다른 사람이랑 있기 싫게 만든다면, 그럼 됐어."
    m 1j "난 너랑 이런 식으로 같이 있으니까 좋으…."
    show monika zorder 1 at thide
    hide monika
    "갑자기, 나츠키가 교실에서 뛰쳐나왔다."
    show natsuki 12h zorder 2 at t11
    n "…."
    show natsuki 12f at lhide
    $ pause(0.75)
    hide natsuki
    "나츠키는 급히 어디론가 뛰어갔다."
    show monika 1l zorder 2 at t11
    m "이런…."
    m "…어, 어느정도 정리된 거 같네…."
    scene bg club_day2
    with wipeleft_scene
    y "그런 뜻이 아니었는데…."
    y "그런 뜻이 아니었는데…."
    y "그런 뜻이 아니었는데…."
    "유리는 이마에 손을 짚은 상태로 몸을 이리저리 떨고 있었다."
    mc "유리…?"
    show yuri 4d zorder 2 at t11
    y "그런 뜻이 아니었어요!!"
    mc "으, 응. 난 널 믿어…."
    "난 유리가 나츠키에게 무슨 말을 한 건지 아직까지 잘 모르겠다."
    "아닐수도."
    y "[player] 씨."
    y "절 싫어하지 마세요."
    y "제발요!"
    y "전 이런 사람이 아니에요!"
    y "오늘 뭔가 분명히 잘못된…."
    show monika 1d zorder 3 at f31
    m "괜찮아, 유리."
    m "네가 그러려고 한 게 아닌 걸."
    m 1j "나츠키는 내일이면 다 잊어버릴 거야."
    m 1a "완전히."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "…."
    show yuri zorder 3 at t32
    show monika zorder 2 at f31
    m "어쨌든, 오늘 모임은 여기서 끝이야, 집에 가고 싶으면 가도 돼."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 4a "…."
    show yuri zorder 2 at t32
    "유리는 나에게 할 말이 있다는 듯이 계속 날 쳐다보았다."
    "그러면서도 계속 모니카의 눈치를 보고 있다."
    show yuri zorder 3 at f32
    y 2v "머, 먼저 가셔도 돼요, 모니카 씨…."
    y "전 좀 더 있고 싶어서…."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2k "난 부장이니까, 내가 마지막까지 있어야지."
    m "마음 정리 다 될 때까지 기다려줄게."
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f32
    y 4b "…."
    y "…."
    y "저기, 저도 부부장이니까…."
    y "오늘 있었던 일은 제가 책임지고 싶어요."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 2i "그냥 내가 여기 없었으면 하는 것처럼 말하는데, 유리?"
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 3p "그런 게 아니에요!!"
    y 3o "그게 아니라…."
    y 3n "전 그저…."
    y 3q "[player] 씨와 읽었던 책에 대해 말할 기회가 잘 없었으니까…."
    y "모니카 씨가 듣는다면…조금 부끄러워서…."
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1r "{i}하아{/i}"
    m 1d "어쩔 수 없는 거 같네."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1t "문제를 일으켜서 죄송해요…."
    $ gtext = glitchtext(20)
    y 1s "그래도 이해해주신다니 정말 감{nw}"
    play music g1
    show monika 1 onlayer front at i31
    y glitch "그래도 이해해주신다니 정말 감{fast}[gtext] [gtext][gtext]{nw}"
    $ _history_list.pop()
    hide monika onlayer front
    window hide(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
