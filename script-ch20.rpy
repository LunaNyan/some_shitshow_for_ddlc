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

label ch20_from_ch10:
    scene bg residential_day
    with dissolve_scene_half
    play music t2
    jump ch20_main2

label ch20_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

label ch20_main2:
    $ finalConso = finalChecker(player)
    "여느 때와 같은 평범한 등굣길."
    "커플들이랑 무리에 둘러싸여 가는 등굣길은 최악이다."
    "말이 나온 김에 하는 얘기지만, 난 항상 학교에 혼자 걸어 다녔다."
    "내 스스로도 이젠 여자들이랑 얘기도 해봐야겠다던가, 사회생활을 시작하겠다고 다짐해 보지만…."
    "그냥 어떤 동아리에도 들어갈 필요성을 못 느끼겠다."
    "난 게임을 하거나 애니메이션을 보며 하루하루를 보내는 게 좋고, 그게 또 일상이라…."
    "뭐, 애니메이션 동아리가 있긴 하지만, 그런 곳에 여자애들이 있는 것도 아니고…."

    scene bg class_day
    with wipeleft_scene

    "정신을 차려보니 여느 때와 다름없는 학교생활이 벌써 끝나있었다."
    "가방을 다 싸고, 이제는 뭘 해야 할까 생각하며 멍때리고 있었다."
    mc "동아리라…."
    "별로 흥미를 끄는 동아리는 없었다."
    "게다가, 대부분 나한테 힘든 조건을 요구할 거고…."
    "역시 애니메이션 동아리부터 찾아보는 게…."

    $ m_name = "???"

    m "…[player]?"
    window hide(None)
    show monika g2 zorder 2 at t11
    pause 0.75
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    show monika 1 zorder 2 at t11
    mc "…모니카?"
    $ m_name = "모니카"
    m 1b "와, 여기서 널 볼 줄 상상도 못 했어!"
    m 5 "진짜 오랜만이다, 그치?"
    mc "아…."
    mc "응, 오랜만이네."
    "모니카가 기분 좋은 미소를 보낸다."
    "우리는 서로 아는 사이다. 뭐, 얘기는 얼마 나누지 않았지만 일단은 작년에 같은 반이었으니까."
    "똑똑하고, 예쁘고, 운동신경이 좋기까지 한 모니카는 반에서 가장 인기 있는 여학생이었다."
    "줄여서 나랑은 전혀 다른 세계에 사는 사람 정도일까."
    "그래서 그렇게 따뜻한 미소를 보내시면 나 같은 건 어떻게 해, 해야…."
    mc "무슨 일로 여기 온 거야?"
    m 1a "아, 동아리 활동에 쓸 재료를 찾느라."
    m 1d "혹시 여기 모눈종이 같은 거 있니?"
    m "아니면 마커펜이라던가?"
    mc "책장 한 번 봐봐."
    mc "…너 아직도 토론회 하지?"
    m 5 "아하하, 그거라면…."
    m "나 사실 토론회 그만뒀어."
    mc "진짜? 그만뒀다고?"
    m "응…."
    m 2e "솔직히 큰 동아리들 분위기가 감당이 안되더라구."
    m "예산을 얼마 받아야 한다느니, 선전은 어떻게 해야 한다느니, 축제는 어떻게 준비해야 하겠다느니 맨날 싸우는 일 말곤 하는 게 없는 것 같아서."
    m "그런 거 할 바에야 내가 좋아하는 일을 해서 뭔가 특별한 걸 해내는 게 낫겠더라구."
    mc "그럼, 어디 동아리 들어갈 건데?"
    m 1b "사실, 동아리를 하나 새로 만들었거든"
    m "문예부 말이야!{nw}"
    show screen tear(20, 0.1, 0.1, 0, 40)
    window hide(None)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    window show(None)
    m "문예부 말이야!{fast}"
    window auto
    mc "문예부…?"
    "별로 재미는 없을 것 같은데…."
    mc "부원은 몇 명이나 있어?"
    m 5 "음…."
    m "아하하…."
    m "조금 부끄러운데, 아직은 세 명밖에 없어."
    m "지루해 보인다고 다들 들어오려고 하지 않아서…."
    mc "뭔가 이해될 법도 한데…."
    m 3d "별로 지루하지 않아!"
    m "문학은 뭐든 될 수 있다고. 독서, 작문, 시…."
    m 3e "그리고, 부원중 한 명은 부실에 만화 컬렉션을 보관하고 있고…."
    mc "잠깐… 진짜?"
    m 2k "응, 진짜 웃기지?"
    m 2e "맨날 만화는 문학이라고 하는 여자애야."
    m "뭐, 물론 틀린 말은 아니겠지만…."
    m "그래도, 부원은 부원이니까?"
    "… 잠깐… 방금 얘 \"여자애\"라고 했지?"
    "흐음…."
    m 1a "저기, [player]야…."
    m "혹시… 동아리 어디 들어갈지 안 정했어?"
    mc "아."
    mc "뭐, 그렇다면… 그렇지."
    m "그러면…."
    m 5 "내 부탁 하나 들어주지 않을래?"
    m "들어오라는 말은 안 할테니까…."
    m "적어도 우리 동아리에 들려주기만 한다면, 난 진짜 기쁠 거야."
    m "제바알?"
    mc "으음…."
    "뭐, 거절할 이유는 없는 거 같다…."
    "그리고 모니카 같은 애의 부탁을 어떻게 거절하겠어?"
    mc "그래, 그럼 들려보기라도 할까."
    m 1k "아, 다행이다!"
    m 1b "[player], 너 그거 알아? 너 진짜 착한 애야!"
    mc "그, 글쎄… 벼, 별로…."
    m 1a "그럼, 갈까?"
    m "재료들은 다음에 찾으면 되니까. 지금은 네가 더 중요해."

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "그렇게, 오늘 난 모니카와 모니카의 거부할 수 없는 미소에 내 영혼을 팔았다 ."
    "모니카를 따라나서 계단을 따라 위층으로 올라간다. 3학년 교실과 방과후 활동이 이뤄지는 곳이라 매일같이 학교에 와도 잘 오지 않는 곳이다"
    "모니카는 활기차게 부실 문을 열었다."

    scene bg club_day2
    with wipeleft
    play music t3

    if renpy.random.randint(0, 2) == 0:
        show monika g1 at l31
    else:
        show monika 3b at l31
    m "돌아왔어~!"
    m "그리고 몰래 온 손님도 한분 데리고왔지!"
    show yuri 2t zorder 2 at t33
    if not config.skipping:
        show screen invert(0.15, 0.3)
    y "네…?"
    y "소… 손님이요?"
    show natsuki 4c zorder 2 at t32
    n "진심이야? 남자를 데려왔어?"
    n "분위기를 깨도 정도가 있지."
    show monika 3m zorder 3 at f31
    m "너무 그러지 마, 나츠키…."
    m 3b "뭐 어쨌든… [player], 문예부에 온 걸 환영해!"
    show monika 3a zorder 2 at t31
    mc "…."
    "할 말을 잃었다…."
    "이 동아리…."
    "{i}…엄청나게 귀여운 여자애만 모여있잖아!!{/i}"

    show natsuki zorder 3 at f32
    n 5c "자, 어디 보자…."
    n "그러니까 네가 모니카의 남자친구인 거지?"
    show natsuki zorder 2 at t32
    mc "무스…."
    mc "아냐, 아냐!"
    show yuri zorder 3 at f33
    y 2l "나츠키 씨…."
    $ n_name = '나츠키'
    "나츠키라고 불린 이 까칠한 여자애는 처음 보는 얼굴이다."
    "순간 1학년으로 착각했을 정도로 몸집이 작다"

    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 2l "어, 어쨌든! 이쪽은 나츠키, 항상 밝은 친구야."
    m 2b "그리고 여기는 부부장, 유리!"
    $ y_name = '유리'
    show monika 2a zorder 2 at t31
    show yuri zorder 3 at f33
    y 4 "마… 만나서 반가워요…."
    "성숙한 분위기를 풍기는 유리는 소심한 성격을 가진 것 같다. 나츠키 같은 활발한 애랑 어울리기엔 많이 피곤할 텐데."
    show yuri zorder 2 at t33
    mc "아… 어, 둘 다 만나서 반가워."
    show monika zorder 3 at f31
    m 1a "있지, 내가 [player]이 교실에 들어가서, 직접 동아리에 와보라고 데려왔어."
    m "굉장하지?"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f32
    n 4e "잠깐, 모니카!"
    n "내가 새 부원 데리고 올 땐 미리 말하라고 했지?"
    n 4q "내가… 알잖아."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1e "미안, 미안해!"
    m "그걸 잊은 건 아닌데, 정말 우연히 마주쳐서."
    show monika zorder 2 at t31
    show yuri zorder 3 at f33
    y 1a "그럼, 전 차라도 타 올까요?"
    show yuri zorder 2 at t33
    show monika zorder 3 at f31
    m 1b "그래, 그게 좋겠다!"
    m "[player] 여기와서 앉아."
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "여자애들이 책상 몇 개를 하나의 큰 탁자처럼 붙여 놓았다."
    "유리는 교실 구석으로 가, 벽장을 열었다."
    "모니카와 나츠키는 서로를 마주 보고 앉았다."
    "아직도 어색하기만 한 분위기 속에, 난 모니카의 옆자리에 앉는다."
    show monika 1a zorder 2 at t11
    m "뭐, 여기 올 예정은 아니었겠지만…."
    m "너희 집 안방처럼 편안히 있어, 알겠지?"
    m 1j "문예부의 부장으로서 부원들에게 재밌는 동아리를 만들어가야 하는 건 당연한 의무니까!"
    mc "그렇게 열심히 하는데 부원이 얼마 없다는 게 놀랍네."
    mc "역시 새 동아리를 만든다는 건 어려운 건가 봐?"
    m 3b "그렇다고 볼 수 있지."
    m "사람들은 아예 새로운 걸 시작하는 데에는 별로 관심이 없거든…."
    m "별로 인기가 없는 문학이라면 더더욱 그렇고…."
    m "문예부에서의 활동이 재미가 있고 가치가 있다는 걸 알리기 위해선 꽤 공을 많이 들여야 해."
    m "그래서 학교 축제 같은 중요한 행사들이 더더욱 중요해지는 거고."
    m 2k "그러다 보면 우리가 졸업하기 전에는 동아리도 꽤 키울 수 있을거야!"
    m "그치, 나츠키?"
    show monika zorder 2 at t22
    show natsuki 4q zorder 2 at t21
    n "뭐…."
    n "…아마도."
    "나츠키는 마지못해 동의한다."
    "성격이 이렇게나 다른데도 같은 목표를 향해 나아간다니…."
    "나츠키와 유리, 이 두 명을 찾는 데에는 모니카의 상당한 노력이 있었겠지."
    "유리가 티 세트를 들고 돌아온다."
    "조심스럽게 각자에게 찻잔을 나눠주고 쟁반 옆에 주전자를 놓는다…."
    show natsuki zorder 1 at thide
    show monika zorder 1 at thide
    hide natsuki
    hide monika
    show yuri 1a zorder 2 at t21
    mc "설마 교실에 찻잔 세트 전부를 가져온 거야?"
    y "선생님들께서 허락하셨어요…."
    y "책을 읽을 때 차 한 잔 만한 게 없으니까요. 안 그런가요?"
    mc "아… 그, 그럴지도…."
    show monika 4a zorder 3 at f22
    m "에헤헤, 그렇게 기죽지 마, 유리가 너한테 잘 보이려고 그러는거니까."
    show monika zorder 2 at t22
    show yuri at hf21
    y 3n "에에?! 전, 전 그저…."
    "유리가 시선을 돌렸다"
    y 4b "저, 전 그, 그저…."
    show yuri zorder 2 at t21
    mc "아하하."
    mc "뭐, 책 읽을 때 차를 마시는 편은 아니지만, 차는 좋아해."
    show yuri zorder 3 at f21
    y 2u "다행이네요…."
    show yuri zorder 2 at t21
    "다행이라는 듯이 유리가 희미하게 웃는다."
    show monika zorder 1 at thide
    hide monika
    show yuri 1a zorder 2 at t32
    y "저어, [player] 씨는 어떤 책을 읽는 걸 좋아하세요?"
    mc "어… 그게…."
    "최근 몇년 동안 읽은 책이 얼마 없어서 뭐라 할 말이 없는데…."
    mc "…만화…."
    "반 농담으로 조용히 얼버무린다"
    show natsuki 1c zorder 2 at t41
    "나츠키의 표정에 갑자기 활기가 넘친다."
    "뭔가 말하고 싶어 하는 것 같은데, 끝내 말하지 않는다."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "벼, 별로 책 읽는 쪽은 아닌가 보네요…."
    mc "…아니, 뭐, 그거야 지금부터 바꾸면 되니까…."
    "내가 무슨 얘길 하고 있는 거야?"
    "유리가 슬픈 미소를 짓자 나도 모르게 말해버렸다…."
    mc "너는 어떤 책을 좋아하는데?"
    y 1l "으응, 전…."
    "찻잔 가장자리를 손가락으로 훑으며 유리가 말을 잇는다."
    y 1a "전 복잡한 세계관을 자세하게 그려내는 소설들을 좋아하는 편이에요."
    y "작가들의 창의력이나 글솜씨에 감명을 받곤 하거든요."
    y 1f "그런 이국적인 세계에서 좋은 이야기를 그려내는 솜씨도 마찬가지구요."
    "그러고도 한참이나 좋아하는 책에 대해서 이야기를 계속한다."
    "내성적이고 소심한 성격인 줄은 알았지만 책에 대해 얘기할 때 눈빛을 보아하니 역시 사람들과 관계하는 것보다는 독서를 더 좋아하는 모양이다…."
    y 2m "솔직히 좋아하는 장르는 많아요."
    y "심리적인 요소가 담긴 이야기에 푹 빠지고는 해요."
    y 2a "독자의 상상력 부족을 고의로 이용해 심기를 툭툭 건드리는 작가의 실력이 놀랍지 않나요?"
    y "요즘은 공포물을 자주 읽는 편이긴 하지만…."
    mc "아, 나도 공포물을 읽어본 적 있어…."
    "겨우겨우 나랑 연관 지을만한 부분을 찾아냈다."
    "이대로 가다간 유리는 돌이랑 얘기하는 꼴 날 뻔 했어."
    show monika 1j zorder 3 at f33
    m "아하하. 그럴 거 같았어. 유리."
    m 1a "네 성격에 딱 맞는다."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "아, 그런가요?"
    y "깊은 생각을 가지게 한다던가, 완전히 다른 세계로 날 보내준다던가, 그런 책은 손에서 놓을 수가 없어요."
    y "특히 공포물 같은 경우에는 세상을 보는 관점을 완전히 바꿔주거든요. 설령 그게 아주 잠깐뿐이라도 말이에요."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "난 공포물같은 거 싫어…."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "응? 왜요?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "으응, 난 그냥…."
    "나츠키가 또 내 눈치를 본다."
    n 5q "아무것도 아냐…."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "뭐, 나츠키는 귀여운 거 쓰는 걸 좋아하니까. 안 그래, 나츠키?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "무, 뭐라고?"
    n "누가 그래?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "저번 모임 때 놔두고 간 종이 말이야."
    m "거기에 너가 쓰던 시가 있던데? 제목이…."
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "시끄러!!"
    n "그리고 그거 내놔!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "알았어, 알았어~"
    show monika 1a zorder 2 at t33
    mc "나츠키, 너 시도 써?"
    show natsuki zorder 3 at f31
    n 1c "에? 응, 가끔."
    n "네가 무슨 상관이야?"
    show natsuki zorder 2 at t31
    mc "아니 그냥 멋있어서."
    mc "보여준다던가, 그럴 생각 없어?"
    show natsuki zorder 3 at f31
    n 5q "시, 싫거든!"
    "나츠키가 눈을 피한다."
    n "별로… 맘에 안 들어할껄…."
    show natsuki zorder 2 at t31
    mc "아, 아직은 별로 자신 없는 거야?"
    show yuri zorder 3 at f32
    y 2f "나츠키의 마음을 알 것도 같아요."
    y "자기가 쓴 글을 남에게 보여준다는 건 자신감의 문제가 아니거든요."
    y 2k "진정한 글짓기는 누군가에게 글을 쓸 때 나타나요."
    y "독자에게 자기 자신의 취약점들을 드러내고 속마음 깊숙이 있는 것들을 꺼내 보여줄 수 있는 용기가 있어야 해요"
    show yuri zorder 2 at t32
    show monika 2a zorder 3 at f33
    m "유리, 너도 글 같은 거 써?"
    m "네 걸 먼저 보여주면 나츠키도 용기가 나지 않을까?."
    show yuri at s32
    y 3o "…."
    mc "유리도 자신 없긴 마찬가지인 것 같은데…."
    "잠깐동안, 침묵이 돈다."
    show monika zorder 3 at f33
    m 5a "좋은 생각이 났어!"
    m "이러는 건 어때?"
    show monika zorder 2 at t33
    show natsuki 2k zorder 3 at f31
    show yuri 3e zorder 3 at f32
    ny "…?"
    "나츠키와 유리가 궁금하다는 표정으로 모니카를 바라본다."
    show natsuki zorder 2 at t31
    show yuri zorder 2 at t32
    show monika zorder 3 at f33
    m 2b "각자 집에 가서 시를 하나씩 써 오는 거야!"
    m "다음 모임 때 각자 쓴 시를 서로에게 보여주는 거지."
    m "그럼 모두 공평한 거잖아!"
    show monika 2a zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5q "으… 으음…."
    show natsuki zorder 2 at t31
    show yuri 3v zorder 3 at f32
    y "…."
    show yuri zorder 2 at t32
    show monika 2m zorder 3 at f33
    m "아…."
    m "내 말은…, 그냥 좋은 생각이라고 생각해서…."
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 2l "으음…."
    y "…모니카 씨의 말이 맞아요."
    y 2f "모두가 같이 할 수 있는 활동을 찾아봐야 해요."
    y 2h "부부장으로서의 책임도 있고…."
    y "모두들 그러겠지만, 전 동아리를 키우는 데 최선을 다 할거에요."
    y 2a "게다가, 새 부원도 들어왔으니…."
    y "좋은 발판이 될 거 같네요."
    y "동의하시죠, [player]?"
    show yuri zorder 2 at t32
    mc "잠깐만…문제가 하나 있어."
    show monika zorder 3 at f33
    m 1d "에? 어떤 문제?"
    "새 부원 얘기로 돌아왔으니 이제 직설적으로 얘기할 필요가 있다."
    show monika zorder 2 at t33
    mc "나 아직 이 동아리 들어온다고 안 했는데!"
    mc "모니카가 와보라고 해서 오기는 했지만… 아직 들어온다는 결정은 안했으니까."
    mc "아직 다른 동아리들도 들려볼 거고, 그리고… 어…."
    show monika 1g
    show natsuki 4g
    show yuri 2e
    "머릿속이 새하얘진다"
    "그렇게 실망한 눈빛으로 쳐다보면 전 어떻게 해야 합니까."
    show monika at s33
    m 1p "그, 그치만…."
    show yuri at s32
    y 2v "죄, 죄송해요, 전 또…."
    show natsuki at s31
    n 5s "흥."
    mc "어…?"
    "다들 서로 눈치를 보고 있다가, 모니카가 입을 연다."
    show monika zorder 3 at f33
    m 1m "알았어, 사실을 말해줄게. [player]."
    m "그게…."
    m 1p "…아직 정규 동아리로 인정받을만한 인원이 안 됐어."
    m "네 명이 있어야 해…."
    m "그리고 새 부원을 찾는 데에 진짜진짜 오랜 시간이 걸렸어."
    m "축제일이 오기 전에 새 부원을 찾지 못한다면…."
    show monika zorder 2 at t33
    mc "…."
    "괜히 미안한 감정이 들었다."
    "이런 상황에서 어떻게 결정을 내리라는 거야?!"
    "그런 눈으로 쳐다보면 냉정하게 판단을 내릴 수가 없잖아…."
    "뭐, 동아리 자체도 꽤 편안해보이고…."
    "그, 그래. 시 몇 편 쓰는 것 만으로도 이 여자애들과 함께할 수 있다면…."
    mc "…그래."
    mc "좋아, 결정했어."
    mc "문예부에 들어갈게."
    show monika 1e zorder 2 at t33
    show yuri 3f zorder 2 at t32
    show natsuki 1k zorder 2 at t31
    "한 명, 한 명, 표정이 서서히 밝아진다."
    show monika zorder 3 at f33
    m "진짜?"
    m "진심이야, [player]?"
    show monika zorder 2 at t33
    mc "응…."
    mc "재밌을 거 같다, 그렇지?"
    show yuri zorder 3 at f32
    y 1m "정말! 놀랐잖아요…."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5q "그냥 이러고 가버렸으면 정말 화냈을꺼야."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m "[player], 나 너무 기뻐…."
    m 1k "이제 정식 동아리가 될 수 있어!"
    m 1e "진짜진짜 너무 고마워."
    m "네가 재밌게 보낼 수 있도록 최선을 다할게."
    show monika zorder 2 at t33
    mc "아, 응. 고마워."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    m 3b "자 그럼, 여러분!"
    m "이것으로 오늘의 모임은 공식적으로 마치겠습니다."
    m "모두 오늘 숙제 잊지마! 시 써오는 거 말야."
    m "다음에 만날 때 공유할 수 있도록!"
    "모니카가 다시 나를 바라본다."
    m 1a "[player], 난 네 시가 기대되는걸."
    show monika 5 at hop
    m "에헤헤~"
    mc "으… 응…."
    show monika zorder 1 at thide
    hide monika
    "과연 평범하기 짝이 없을 게 뻔한 내 글쓰기 실력으로 모니카의 기대를 만족시킬 수 있을지 모르겠다."
    "벌써 부담이 팍팍 든다."
    "유리가 찻잔 세트를 치우는 동안 다른 여자애들은 계속 수다를 떨고 있다."
    mc "그럼 난 슬슬 가 볼게."
    show monika 5a zorder 2 at t11
    m "그래!"
    m "그럼 내일 보자."
    m "기대된다!"

    scene bg residential_day
    with wipeleft_scene

    "그렇게 나는 교실을 나서 집으로 돌아온다."
    "돌아오는 길에도 내 마음은 세 명의 소녀들 생각으로 가득 차 있다."
    show natsuki 4a zorder 2 at t31
    "나츠키,"
    show yuri 1a zorder 2 at t32
    "유리,"
    show monika 1a zorder 2 at t33
    "그리고 모니카까지."
    "과연 내가 매일 방과 후 시간을 문예부에서 보내는 걸 좋아할 수 있을까?"
    "어쩌면 여자애들 중 하나와 더 가까워질 수 있는 계기가 될 수도…."
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "좋아!"
    "어차피 하기로 한 거, 최선을 다하면 행운이 따를지도 몰라."
    "천릿길도 한 걸음부터라고. 그럼 시부터 써봐야겠지?"

    stop music fadeout 2.0
    scene black with dissolve_scene_full
    $ config.skipping = False
    $ config.allow_skipping = False
    $ allow_skipping = False

    call screen confirm("특별한 시가 해금되었습니다.\n읽어보시겠습니까?", Return(True), Return(False))
    if _return:
        call expression "poem_special_" + str(persistent.special_poems[0]) from _call_expression_18
    else:
        pass

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
