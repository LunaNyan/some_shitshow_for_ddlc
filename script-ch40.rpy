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

image sayori end-glitch:
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    1.00
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"
    0.15
    "sayori/end-glitch1.png"
    0.15
    "sayori/end-glitch2.png"

label ch40_main:
    $ finalConso = finalChecker(player)
    $ s_name = "사요리"
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full

    python:
        if not persistent.monika_back:
            try:
                renpy.file("…/characters/monika.chr")
                renpy.call_screen("dialog", message="내 마음가지고 장난치지 말아줘.\n난 돌아가고 싶지 않아.", ok_action=Return())
                persistent.monika_back = True
            except:
                pass

    $ delete_character("monika")
    play music t2
    "여느 때와 같은 평범한 등굣길."
    "커플들이랑 무리에 둘러싸여 가는 등굣길은 최악이다."
    "나 자신도 이젠 여자들이랑 얘기도 해봐야겠다던가, 사회생활을 시작하겠다고 다짐해 보지만…."
    show sayori 1a at t11
    s "야아, [player]…."
    "…이미 한 명 있으니까."
    "저 여자애는 옆집에 사는 아주 어릴 때부터 알고 지낸 소꿉친구 사요리다."
    "우린 매일같이 학교에 같이 간다."
    "…그리고 요즘, 우리는 다시 ‘그’ 습관이 들었다."
    s "[player], 내가 자랑스럽지?"
    mc "응? 갑자기 뭔 소리야?"
    s 1c "있잖아…."
    s "제시간에 일어나는 거!"
    mc "뭐, 당연히 계속 일찍 일어나니까…."
    s "응응!"
    s 4h "그치만 한 번도 말해준 적 없잖아!"
    show sayori at s11
    s "매일 학교에 같이 가는데도…."
    mc "글쎄, 그러네…."
    mc "항상 그렇다고 생각은 하고 있었어."
    mc "입 밖으로 내는 게 부끄러워서 그렇지."
    s 1d "부탁이야, 응?"
    s "좋은 동기부여가 될 거야~"
    mc "알았어, 알았어…."
    mc "네가 자랑스러워, 사요리."
    show sayori at t11
    s 1q "에헤헤~"
    show sayori zorder 1 at thide
    hide sayori
    "우리는 같이 걸어갔다."
    "학교에 다다를수록, 거리는 점점 학생들로 가득 차는듯했다."
    show sayori 3a zorder 2 at t11
    s "그런데, [player]…."
    s "동아리 어디 들어갈지 정했어?"
    mc "동아리?"
    mc "내가 얘기했잖아, 난 동아리 같은 거…."
    "나는 항상 얘기했듯 동아리 따윈 관심 없다고 말하려고 했다."
    "그런데 어째서인지 오늘따라 그 말을 해선 안 된다는 기분이 든다."
    "사요리가 스스로 동아리를 만들었는데…."
    "…어떻게 동아리 같은 건 시간 낭비라는 말을 하겠어?"
    mc "…사실, 그래."
    mc "어디 갈지 정했어."
    show sayori at h11
    s 1m "정말?!"
    s 1r "어딘데? 알려줘!"
    mc "으음…."
    mc "비밀이야."
    s 5d "우우…."
    s "너무해."
    mc "기다리면 곧 알게 될 거야."
    "난 어쩌다 이 천진난만한 소녀에게 잔소리를 듣게 되었는지 스스로 묻고는 했다."
    "그런데 깨닫고 나니, 난 사요리를 부러워하고 있었다는 걸 알게 됐다."
    "사요리는 무언가에 마음을 쏟을 때, 항상 멋진 결과들을 만든다."
    "그래서 뭔가 사요리에게 특별한 일을 해줘야 한다는 생각이 드는데…."

    scene bg class_day
    with wipeleft_scene

    "정신을 차려보니 여느 때와 다름없는 학교생활이 벌써 끝나있었다."
    "가방을 다 싸고, 난 결심한 채로 자리에서 일어났다."
    mc "어디 보자…."
    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene
    "난 홍보 전단지에서 본 동아리방을 기억하고 있다."
    "난 위층으로 이동했다. 3학년 교실과 방과 후 활동이 이뤄지는 곳이라 매일같이 학교에 와도 잘 오지 않는 곳이다."
    "조금 지나, 부실을 찾았다."
    "난 소심하게 문을 열었다."
    scene bg club_day
    with wipeleft
    play music t3
    mc "계세요…?"
    show sayori 1m at t32
    s "아!"
    s "[player]…?!"
    s 1c "네, 네가 왜 여기에?"
    mc "어… 그냥…."
    "응? 난 교실을 둘러보았다."
    show natsuki 3a at f31
    n "흐응."
    n "사요리가 항상 얘기하던 [player]가 너구나?"
    show natsuki at t31
    show yuri 2t at f33
    y "드, 들려주셔서 감사해요!"
    y 2m "만나서 반가워요, [player]."
    y "저희는 문예부에요."
    y 3v "즐거운 시간 보내세요!"
    show yuri at t33
    show natsuki at f31
    n 3g "하, 좀. 유리…."
    n "너무 딱딱하게 굴지 마."
    n "우리가 되게 엄격하다고 생각하면 어떡해…."
    show natsuki at t31
    $ y_name = "유리"
    $ n_name = "나츠키"
    show yuri at f33
    y 3q "아…."
    y "죄송해요, 나츠키 씨…."
    show yuri at t33
    "유리라는 키가 큰 친구는, 다른 아이들에 비교해 조금 부끄러움을 타는 것 같다."
    "그에 비교해 나츠키라는 친구는 키에 비해 적극적인 성격을 가진 것 같다."
    mc "어, 둘 다 만나서 반가워."
    mc "잘 지내보자."
    show sayori at f32
    s 1n "그런데 무슨 일이야…?"
    s 1b "[player], 너 설마…."
    s "너…."
    show sayori at t32
    mc "맞아."
    mc "내가 고른 동아리는 네 동아리야, 사요리."
    mc "문예부지."
    "사요리의 눈이 빛나기 시작한다."
    show sayori at f32
    s 1n "… 거짓말."
    s 1s "말도 안 돼!"
    show sayori at hf32
    s 4s "으아아아!"
    "사요리는 날 껴안고 폴짝폴짝 뛰기 시작했다."
    show sayori at t32
    mc "야, 야…."
    show natsuki at f31
    n 3y "에헤헤."
    n "글쎄, 사요리가 이렇게 기뻐한다면, 네가 들어와도 나쁘진 않겠네."
    show natsuki 3a at t31
    show yuri at f33
    y 1s "이제 부원이 네 명이네요."
    y "공식적으로 인정받는 동아리가 될 수 있어요."
    show yuri at t33
    show sayori at f32
    s 1x "무슨 말을 해야 할지 모르겠어!"
    s "일단 파티를 해야 해!"
    show sayori at t32
    show yuri at f33
    y 1m "후후."
    y "그러기에 적당한 날이네요, 그렇죠?"
    show yuri 1a at t33
    show sayori at f32
    s 1r "맞아!"
    s 1x "그것보다, 나츠키가…."
    show sayori at t32
    show natsuki at f31
    n 1w "야, 서프라이즈를 망치지 마!"
    show natsuki at t31
    show sayori at f32
    s 5a "에헤헤, 미안…."
    show sayori at t32
    show natsuki at f31
    n 1k "모두 자리에 앉아."
    show natsuki at t31
    show yuri at f33
    y 1a "그럼 저는 차를 내오도록 할게요."
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "여자애들이 책상 몇 개를 하나의 큰 탁자처럼 붙여 놓았다."
    "나츠키와 유리는 한쪽 구석으로 가더니 나츠키는 뭔가로 덮인 쟁반을, 유리는 벽장을 연다."
    "아직도 어색하기만 한 분위기 속에, 난 사요리의 옆자리에 앉는다."
    "나츠키가 위풍당당한 걸음으로 손에는 쟁반을 들고 책상으로 돌아온다."
    show natsuki 2z zorder 2 at t22
    n "자, 그럼 공개한다?"
    n "…짜잔!"
    show sayori 4m zorder 2 at t21
    s "우와아아아아!"
    "나츠키가 쟁반을 덮고있던 은박지를 벗기자 고양이 모양으로 장식된 열두 개의 컵케이크가 눈에 들어왔다."
    "아이싱으로 수염을 그려놓았고, 귀는 초콜릿 조각으로 되어있었다."
    show sayori at f21
    s 4r "진짜 귀엽다아아아~!"
    show sayori at t21
    mc "와, 굉장한데…?"
    show natsuki at f22
    n 2d "에헤헤. 있잖아."
    n "얼른 드시기나 하셔!"
    show natsuki at t22
    "사요리가 먼저 하나를 집었다. 그렇다면 나도."
    show sayori at f21
    s 4q "완전 맛있어어!"
    show sayori at t21
    "입안에 컵케이크를 가득 문 채로 사요리가 말했다. 다른 사람은 먹지도 않았는데 아이싱이 입가에 가득하다."
    "나는 손가락으로 컵케이크를 이리저리 돌리며 어디부터 먹어야 할지 고민한다."
    show sayori zorder 1 at thide
    hide sayori
    show natsuki 1c zorder 2 at t32
    "나츠키가 조용하다."
    "자꾸만 내 눈치를 보는 게 신경이 쓰인다."
    "내가 먹기를 기다리고 있는 걸까?"
    "마침내 한입 물었다."
    "아이싱이 참 달콤하고 풍미가 가득하다. 혹시 아이싱도 직접 만든 걸까?"
    mc "이거 진짜 맛있다!"
    mc "고마워, 나츠키."
    n 42c "무, 뭐. 당연하지!"
    n "나는 프로니까!"
    n 42a "고마워할 필요는 없어…."
    show natsuki zorder 1 at thide
    hide natsuki
    "나츠키가 칭찬을 받아들이는데 노력하고 있는 동안, 유리는 차 세트를 들고 돌아왔다."
    "조심스럽게 각자에게 찻잔을 나눠주고 쟁반 옆에 주전자를 놓는다…."
    show yuri 1a zorder 2 at t11
    mc "설마 교실에 찻잔 세트 전부를 가져온 거야?"
    y "선생님들께서 허락하셨어요."
    y "책을 읽을때 차 한 잔 만한게 없으니까요. 안 그런가요?"
    mc "아… 그, 그럴지도…."
    show natsuki 2y at f31
    n "에에에. 벌써 새 부원한테 잘 보이려는 거야, 유리?"
    show natsuki at t31
    show yuri at f11
    y 3n "네?! 그, 그런 게 아니에요…."
    show yuri at t11
    show natsuki at thide
    hide natsuki
    "유리는 눈을 돌린다."
    y 4b "전 그냥…."
    mc "응, 나도 알아."
    mc "뭐, 책 읽을 때 차를 마시는 편은 아니지만, 차는 좋아해."
    y 2u "다행이네요…."
    "다행이라는 듯이 유리가 희미하게 웃는다."
    y 1a "저어, [player] 씨는 어떤 책을 읽는 걸 좋아하세요?"
    mc "어… 그게…."
    "최근 몇 년 동안 읽은 책이 얼마 없어서 뭐라 할 말이 없는데…."
    mc "…만화…."
    "반 농담으로 조용히 얼버무린다."
    show natsuki 1c zorder 2 at t41
    "나츠키의 표정에 갑자기 활기가 넘친다."
    "뭔가 말하고 싶어 하는 것 같은데, 끝내 말하지 않는다."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "벼, 별로 책 읽는 쪽은 아닌가 보네요…."
    mc "… 아니, 뭐, 그거야 지금부터 바꾸면 되니까…."
    "내가 무슨 얘길 하고 있는 거야?"
    "유리가 슬픈 미소를 짓자 나도 모르게 말해버렸다."
    mc "너는 어떤 책을 좋아하는데?"
    y 1l "으응, 전…."
    "찻잔 가장자리를 손가락으로 훑으며 유리가 말을 잇는다…."
    y 1a "전 복잡한 세계관을 자세하게 그려내는 소설들을 좋아하는 편이에요."
    y "작가들의 창의력이나 글솜씨에 감명을 받곤 하거든요."
    y 1f "그런 이국적인 세계에서 좋은 이야기를 그려내는 솜씨도 마찬가지고요."
    "그러고도 한참이나 좋아하는 책에 관해서 이야기를 계속한다."
    "내성적이고 소심한 성격인 줄은 알았지만 책에 관해 얘기할 때 눈빛을 보아하니 역시 사람들과 관계하는 것보다는 독서를 더 좋아하는 모양이다…."
    y 2m "솔직히 좋아하는 장르는 많아요."
    y 2a "책을 많이 읽지 않는다고 너무 걱정하지는 마세요, 아시겠죠?"
    y "분명 공통점을 찾을 수 있을거에요."
    show yuri at t22
    show natsuki 2c at f21
    n "저기, 유리…."
    show natsuki at t21
    show yuri at f22
    y 2f "네?"
    show yuri at t22
    show natsuki at f21
    n 2h "그, 저기… 있잖아. 얘가 제일 처음 얘기한 거…."
    show natsuki at t21
    mc "만화?"
    show yuri at f22
    y 2i "맞아요…."
    y "나츠키 씨는 부실에서 만화를 읽……."
    show yuri at t22
    show natsuki at f21
    n 1r "마, 말하지 마!!"
    "어째서인지, 나츠키는 굉장히 부끄러워하는 듯했다."
    n 1q "그리고…."
    n "만화도… 문학이란 말이야!"
    n 1w "그러니까 만약 [player]가 내 만화책 읽어도 막거나 너무 뭐라고 하지 마!"
    show natsuki 1i at t21
    show yuri at f22
    y 1l "나츠키 씨…."
    y "저는 그런 짓 하지 않아요."
    y 1i "하지만 저희 자신을 다양화 해보는 것도 좋을 거 같아요…."
    y "[player] 씨도 이 기회를 통해 뭔가 새로운 걸 시도해볼 수도 있고."
    y 1s "동의하시죠, [player] 씨?"
    show yuri at t33
    show natsuki at t32
    show sayori 1l at f31
    s "우, 우리…."
    "사요리가 끼어든다."
    s 1x "우리 모두 각자 새로운 걸 해보자!"
    s 1l "내 생각엔 재밌을 거 같은데…."
    s 1c "그리고 서로를 좀 더 이해할 수 있을 거야!"
    s 1l "내 말은…."
    s "그게 문예부가 하는 일이겠지…?"
    show sayori at t31
    show yuri at f33
    y 1v "…."
    y "동의하지 않는 건 아닌데…."
    show yuri at t33
    show natsuki at f32
    n 2j "그래…."
    n "언제나 그랬듯이 네 말이 맞아, 부장."
    show natsuki at t32
    show sayori at f31
    s 1q "에헤헤~"
    show sayori at t31
    show natsuki at f32
    n 2c "그 말은 내가 소설을 골라봐야 한다는 거겠지…?"
    show natsuki at t32
    mc "나도 마찬가지겠네…."
    mc "나는 나 혼자 하는 게 아니라면 상관없어."
    show sayori at thide
    hide sayori
    show natsuki at f21
    show yuri at t22
    n 2y "그럼 유리는…."
    show natsuki at t21
    show yuri at f22
    y 2n "어…?"
    y "그럼 저는 만화를 읽어야하나요…?"
    show yuri at t22
    show natsuki at f21
    n 4i "아 좀…."
    n 4h "처음 다양화 어쩌고라고 말 꺼낸 건 너잖아!"
    n "넌 마음을 열 필요가 있어…."
    n 4u "조금 기분 나쁘네…."
    show natsuki at t21
    show yuri at f22
    y 2t "기분이 나빠요…?"
    y 2v "저, 저는…."
    y "…."
    "유리는 미안한 표정을 지으며 스스로 생각한다."
    y 2w "당신의 관심사를 무시해서 죄송해요, 나츠키 씨."
    y "다, 당신이 빠져있는 거라면, 그것도 가치 있는 문학의 형태겠죠."
    show yuri at t22
    show natsuki at f21
    n 5q "…지금 비꼬는 거야?"
    show natsuki at t21
    show yuri at f22
    y "아뇨…."
    y "진심이에요."
    y 2t "그래서, 소설 읽는 걸 고려해보신다면…."
    y 2u "…감사히 저도 읽을 만화를 찾아볼게요."
    show yuri at t22
    show natsuki at f21
    n 1l "정말?!"
    n 12c "그, 그니까…."
    n "네, 네가 그래준다면 되게 기쁠거야, 유리."
    n 2c "…네 맘에 쏙 들만한 거를 찾아줄 테니까 믿고 맡기라고!"
    show natsuki at t21
    show yuri at f22
    y 1m "저도 같아요…."
    y 1h "모임이 끝나면 서점에 들려야겠네요…."
    show yuri at t22
    show natsuki at f21
    n 1q "너, 너 혼자서?"
    show natsuki at t21
    show yuri at f22
    y 3q "앗, 아앗…."
    y 4a "같이 가고 싶으신가요?"
    show yuri at t22
    show natsuki at f21
    n 5s "음…."
    n "너만 괜찮다면…."
    show natsuki at t21
    show yuri at f22
    y 3t "좋아요!"
    y "저는 항상 집에 혼자 가니까요…."
    show yuri at t22
    show natsuki at f21
    n "응, 나도…."
    show natsuki at t21
    show sayori 4s at l41
    s "너무 귀엽다~!"
    mc "조용히 해, 사요리…."
    show sayori at lhide
    hide sayori
    show natsuki at f21
    n 2j "거기서 만화 몇 개 추천해줄 테니까, 알았지?"
    show natsuki at t21
    show yuri at f22
    y 1a "네."
    y "기대하고 있을게요."
    show natsuki at thide
    show yuri at thide
    hide natsuki
    hide yuri
    "나츠키와 유리는 먹은 것들을 치우기 시작했다."
    show sayori 1q at t11
    s "에헤헤~"
    s 1x "오늘 모임은 여기까지인것 같네, 그치?"
    mc "응, 그런 거 같네…."
    mc "모두 사이 좋은 게 보기 좋네."
    s 1q "그치?"
    s 1d "다들 너를 마음에 들어하는 거 같아, [player]."
    mc "그래…?"
    mc "글쎄, 다들 네가 있으니까 더 잘 지내는 거 같은데."
    s 1y "야아, [player]~"
    s "그런 말 하지 마, 부끄럽잖아!"
    mc "뭐, 어쨌든."
    mc "네가 동아리를 만든다고 했을 때 솔직히 놀랐어…."
    mc "그런데 잘 하고있는 거 같네."
    s 1r "우리는 최고의 동아리를 만들 거야!"
    s 1x "이제 네가 들어왔으니까, 하루하루가 즐거울 거야."
    stop music fadeout 2.0
    s 1a "저기, [player]…."
    s "너한테 정말 고마워."
    s "내 말은, 네가 동아리에 들어와줘서 고맙다는 거야…."
    s "근데 사실, 네가 들어올 거라는 건 이미 알고있었어."
    s 1q "에헤헤~"
    s 1a "그거말고 다른 것도 알고있어."
    $ if all(clear for clear in persistent.clear): persistent.clearall = True
    if persistent.clearall:
        call ch40_clearall from _call_ch40_clearall
    else:
        call ch40_clearnormal from _call_ch40_clearnormal
    window hide(None)
    window auto
    $ quick_menu = False
    return

    label ch40_clearnormal:
        show sayori 1a zorder 2 at t11
        s "…모니카를 없애줘서 고마워."
        play music hb
        show black:
            alpha 0.5
            parallel:
                0.36
                alpha 0.5
                repeat
            parallel:
                0.49
                alpha 0.475
                repeat
        show layer master at heartbeat
        s 1b "맞아…."
        s "난 걔가 무슨 짓을 했는지 다 알고 있어."
        s 1x "아마 이제 내가 부장이여서 그런가 봐."
        s "근데 진짜 다 알고있어, [player]."
        s 1q "에헤헤~"
        s 1d "네가 모두를 행복하게 해주기 위해 노력했던 일도…."
        s "모니카가 모두를 슬프게 했던 그 끔찍했던 일들도 다 알고 있어…."
        s 1b "하지만 이제 그런 건 상관없어."
        s "이젠 우리 둘뿐이야.{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        show room_glitch zorder 1:
            xoffset -5
            0.1
            xoffset 5
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 0
        s "우리 둘뿐이야.{fast}"
        hide room_glitch
        s 1d "그리고 넌 날 세상에서 가장 행복한 여자로 만들었어."
        s "매일 이렇게 있게 된다니, 너무 좋다…."
        s "단 둘이."
        play sound "sfx/s_kill_glitch1.ogg"
        show room_glitch zorder 1:
            xoffset -10
            0.1
            xoffset 0
            0.1
            linear 0.1 alpha 0.6
            linear 0.1 alpha 0.8
            0.1
            alpha 1.0
        pause 0.3
        stop sound
        s 1q "영원히 함께 하자…."
        hide sayori
        show sayori 1a onlayer screens zorder 101 at face
        s "영"
        s "원"
        s "히"
        show screen tear(20, 0.1, 0.1, 0, 40)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.25
        stop sound
        hide screen tear
        s "함"
        s "께"
        s "하"
        window show(None)
        stop music
        call screen dialog("안돼….", ok_action=Return())
        show layer master
        hide black
        show sayori end-glitch onlayer screens
        s "…에?"
        s "뭐, 뭐야…?"
        call screen dialog("해치게 놔두진 않을 거야.", ok_action=Return())
        s "누구야…."
        s "아, 아파…."
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        hide sayori onlayer screens
        pause 0.35
        stop sound
        hide screen tear
        window show(None)
        s "아…."
        call screen dialog("미안… 내가 잘못했어.", ok_action=Return())
        call screen dialog("여기에 행복이란 건 없어….", ok_action=Return())
        call screen dialog("안녕, 사요리.", ok_action=Return())
        call screen dialog("안녕, [player].", ok_action=Return())
        call screen dialog("안녕, 문예부.", ok_action=Return())
        $ gtext = glitchtext(120)
        s "[gtext]{nw}"
        show screen tear(20, 0.1, 0.1, 0, 40)
        window hide(None)
        play sound "sfx/s_kill_glitch1.ogg"
        pause 0.35
        stop sound
        hide screen tear
        scene black
        pause 3.0
        return

    label ch40_clearall:
        s "우리랑 많은 시간을 보내줘서 고마워."
        play music mend
        s 2d "우리가 모두 행복할 수 있게 정말 큰 노력을 해줬잖아."
        s "너는 우리 모두를 위로해줬어."
        s "그리고 우리가 사이좋게 지내도록 도와줬지."
        s 1a "…무슨 말인지 알겠어, [player]?"
        s "이제 내가 부장이니까, 모든 것이 이해됐어."
        s 1q "이 게임에 하나라도 놓치기 싫었던 거지, 그렇지?"
        s 1a "모두와 시간을 보내려고 무지하게 저장하고 불러왔더라."
        s "문예부를 진정으로 생각해주는 사람만이 그렇게 할 수 있어."
        s "그런데…."
        s 4d "그게 내가 원했던 거야."
        s "모두가 행복하고 서로를 아끼는 것."
        s 4q "아하하…."
        s 1t "좀 슬프다."
        s "네가 이 정도로 노력해줬는데, 내가 너한테 해줄 수 있는 게 아무것도 없네."
        s "우린 이미 게임의 끝까지 왔으니까."
        s 1y "이제…."
        s "작별할 시간인 거 같네."
        s 1d "{i}두근두근 문예부{/i}를 플레이해줘서 고마워."
        s "네가 그리울 거야, [player]."
        s "가끔씩 놀러 와, 알겠지?"
        s "항상 여기서 기다리고 있을게."
        s 1t "우리…."
        scene black with dissolve_cg
        s "우리 모두 널 사랑해."
        stop music fadeout 2.0
        scene black
        with Dissolve(2.0)
        return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
