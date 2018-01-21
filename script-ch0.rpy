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

label ch0_main:
    stop music fadeout 2.0
    scene bg residential_day
    with dissolve_scene_full
    play music t2

    python:
        try: renpy.file("../characters/monika.chr")
        except: renpy.jump("ch0_kill")

    $ restore_all_characters()
    $ finalConso = finalChecker(player)
    s "기다려어어어어어!!"
    "저 멀리서 성가신 여자아이가 주변 사람들 시선은 아랑곳하지 않은 채 팔을 허공에 흔들며 달려온다."
    "저 여자애는 옆집에 사는 아주 어릴 때부터 알고 지낸 소꿉친구 사요리다."
    "왜, 요즘에는 만들기 힘든 그런 친구지만 그냥 서로 너무 오래 알고 지내서 친해진, 그런 사이?"
    "매일같이 학교에 같이 가곤 했는데, 사요리가 고교 시절 들어서 늦잠이 부쩍 느는 바람에 기다려주기가 힘들어졌다."
    "그런데 이런 식으로 쫓아와 버리면 모르는 척 도망가버리는 게 나을지도."
    "…라고 생각은 했지만 결국 한숨을 내쉬며 사거리에서 기다려준다."
    $ s_name = "사요리"
    show sayori 4p zorder 2 at t11
    s 4p "하아아… 하아아…"
    s "또 늦잠 자 버렸어."
    s "그래도 이번엔 따라잡았네!"
    mc "그러네. 이번엔 내가 기다려줬으니까."
    show sayori at s11
    s 5c "에에에에에? 나 무시하고 그냥 가려고 했던 거야?"
    s "[player], 너무해!"
    mc "아니, 네가 그런 식으로 달려오면 사람들이 이상하게 보니까. 나까지 엮어서 이상하게 생각하면 어떡해."
    show sayori zorder 2 at t11
    s 1a "알았어, 알았어."
    s "그래도 날 기다려준 건 사실이잖아?"
    s "너, 말은 그렇게 하면서도 되게 자상하다?"
    mc "마음대로 생각해라…"
    s 1q "에헤헤~"
    show sayori zorder 1 at thide
    hide sayori
    "사거리를 지나 학교로 함께 걸어간다."
    "학교로 가까워지면 가까워질수록, 거리엔 일상적인 대화를 나누며 떠드는 학생들이 하나둘씩 늘어간다."
    show sayori 3a zorder 2 at t11
    s "맞다, [player]야…"
    s "혹시 동아리는 정했어?"
    mc "동아리?"
    mc "전에 말했잖아, 동아리 같은 거엔 관심 없다고."
    mc "그래서 알아보지도 않았는데."
    show sayori at s11
    s 4h "에? 거짓말!"
    s "이번 해에는 동아리 들어가겠다고 했잖아!"
    mc "내가…?"
    "분명 가능성은 있다. 귀찮아서 아무렇게나 대답해버린 말 중에 하나라면."
    "사요리는 사소한 것 하나까지도 나에 대한 것이라면 걱정한다. 난 적당히 애니를 보거나 게임을 하면서 지내는 것으로 만족하지만."
    s 4j "응응!"
    s "대학교 들어가서 사회생활 적응 못 하거나 뭐 하나 재능이라도 없으면 어떡하냐고 걱정된다고 했을 때 말야."
    s "네가 행복한 게 나한텐 가장 중요하다고 말 했었잖아!"
    s "지금도 행복하다는 건 알겠는데, 나중에 진짜 사회생활 할 때 적응 못 해서 백수가 되는 상상만 해도 죽을 거 같단 말이야!"
    s 4g "무슨 말인지 알지?"
    s "언제까지 날 걱정하게 만들 거야…"
    mc "알았어, 알았어…"
    mc "네가 원한다면 동아리 정도야 알아볼게."
    mc "물론 장담은 못해."
    s 1h "최소한 노력은 해 보겠다고 약속해 줄 수 있어?"
    mc "그래, 그 정도는 약속해줄게."
    show sayori zorder 2 at t11
    s 4r "예에에~!"
    "왜 이런 속 편한 여자애한테 설교나 듣고 앉아있냐고?"
    "사요리 말이 아주 틀린 건 아니니까."
    "사요리가 상상을 좀 지나치게 하는 편이지만, 이렇게까지 나를 걱정해주면 그런 마음을 조금이나마 풀어주고 싶은 걸지도 모른다."

    scene bg class_day
    with wipeleft_scene

    "정신을 차려보니 여느 때와 다름없는 학교생활이 벌써 끝나있었다."
    "가방을 다 싸고, 이제는 뭘 해야 할까 생각하며 멍때리고 있었다."
    mc "동아리라…"
    "사요리가 동아리 알아보라고 했었지."
    "역시 애니메이션 동아리부터 찾아보는게…"

    s "저기이?"
    show sayori 1b zorder 2 at t11
    mc "사요리…?"
    "멍때리고 있던 사이 우리 반 교실에 들어왔나보다."
    "그러고 보니 교실에 남은건 나와 사요리 뿐이다."
    s 1a "교실 밖에서 기다릴까 했는데, 가만히 앉아서 멍때리고 있더라, 그래서 들어왔어."
    s "가끔보면 너 나보다 더하다니까… 대단해."
    mc "너 동아리 늦지 않아? 이렇게까지 기다려줄 필요는 없었는데."
    s 1y "그게, 아무래도 너가 혼자 동아리를 알아볼 것 같진 않아서, 그래서 생각해봤는데…"
    mc "봤는데?"
    s 1a "으응, 영 못찾겠으면 우리 동아리로 오면 되잖아!"
    mc "사요리…"
    s 4r "응??"
    mc "…내가 네 동아리에 갈 리가 없잖아."
    show sayori at s11
    s 5d "에에에에에에?! 나빴어어!"
    "사요리는 문예부의 부부장이다."
    "문학에는 개미 눈꼽만큼도 관심이 없던 애가 어떻게 부부장이 된걸까."
    "99%% 확신하는데, 그냥 동아리를 새로 만든다는 게 재밌을 거 같아서 참여한거겠지."
    "동아리를 건의한 사람 바로 다음에 들어가서 \"부부장\"이 된거고."
    "그런 문예부라면 나는 개미 눈꼽 반만큼도 관심이 없다."
    mc "그래. 어쨌든 애니메이션 동아리에 찾아가 볼 거니까."
    show sayori zorder 2 at t11
    s 1g "그러지말구, 웅?"
    mc "근데 왜 그렇게 집착하는 거야?"
    s 5b "그게…"
    s "어제 부원들에게 새 부원 꼭 데려오겠다고 했거든…"
    s "그랬더니 나츠키가 컵케이크 만들어온다고 해서…"
    s "에헤헤…"
    mc "못 지킬 거면 약속을 처음부터 하지 말던가!"
    "정말 머리가 비어서 용감한건지, 아님 처음부터 다 계산하고 이러는지 모르겠다."
    "한숨만 길게 내쉴 뿐."
    mc "알았어… 컵케이크이라도 먹으러 간다. 됐지?"
    show sayori at h11
    s 4r "응응! 가자~!"

    stop music fadeout 2.0

    scene bg corridor
    with wipeleft_scene

    "그렇게, 오늘 난 컵케이크에 내 영혼을 팔았다."
    "마지못해 사요리를 따라나서 계단을 따라 윗층으로 올라간다. 3학년 교실과 방과후 활동이 이뤄지는 곳이라 매일같이 학교에 와도 잘 오지 않는 곳이다."
    "사요리가 힘차게 교실 문을 열었다."

    scene bg club_day
    with wipeleft
    play music t3
    show sayori 4 at l41
    s "모두들 인사해! 새 부원이야~!"
    mc "아니, '새 부원' 이라니? 아직 들어간다고 한 적은 없는…"
    show sayori at lhide
    hide sayori
    "어라라? 교실에 들어서자 내 눈에 들어온 것은…"
    show yuri 1a zorder 2 at t11
    y "문예부에 오신걸 환영해요. 만나서 반가워요."
    y "사요리씨에게서 얘기 많이 들었어요."
    show yuri zorder 2 at t22
    show natsuki 4c zorder 2 at t21
    n "진심이야? 남자를 데려왔어?"
    n "분위기를 깨도 정도가 있지."
    show yuri zorder 2 at t33
    show natsuki zorder 2 at t32
    show monika 1k zorder 2 at t31
    m "어라, [player]? 진짜 오랜만이다!"
    m "문예부에 온걸 환영해!"
    show monika 1a
    mc "…"
    "할 말을 잃었다."
    "이 동아리…"
    "{i}…엄청나게 귀여운 여자애만 모여있잖아!!{/i}"

    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 3 at f32
    hide monika
    hide yuri

    n 2c "왜 그런 눈으로 보는거야?"
    n "하고 싶은 말이 있으면 그냥 해."
    mc "미, 미안…"
    show natsuki zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "나츠키 씨…"
    $ n_name = '나츠키'
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f32
    n 5s "흥."
    show natsuki zorder 2 at t32

    "나츠키라고 불린 이 까칠한 여자애는 처음 보는 얼굴이다."
    "순간 1학년으로 착각했을 정도로 몸집이 작다."
    "사요리에 말에 의하면, 얘가 컵케이크를 만든다고 했었지."

    show sayori 2q zorder 3 at f31
    s "나츠키가 저렇게 툴툴거릴땐 무시해도 돼~"
    "그렇게 사요리가 귓속말로 짧게 전한 후 다른 여자애들을 향해 몸을 돌린다."
    s 1x "어쨌든! 이쪽은 나츠키, 항상 밝은 친구구."
    s "이쪽은 유리, 우리 중 가장 똑똑한 친구야!"
    $ y_name = '유리'
    show sayori zorder 2 at t31
    show yuri zorder 3 at f33
    y 4b "그…그런 말씀은…"
    "성숙한 분위기를 풍기는 유리는 소심한 성격을 가진 것 같다. 사요리나 나츠키 같은 활발한 애들과 어울리기엔 많이 피곤할텐데."
    show yuri zorder 2 at t33
    mc "아… 어, 둘 다 만나서 반가워."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    hide yuri
    hide natsuki
    show sayori zorder 3 at f31
    s 1a "그리고 모니카랑은 벌써 아는 사인거 같던데?"
    $ m_name = '모니카'
    show sayori zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "맞아."
    m "이렇게 다시 보니 반갑다, [player]."
    show monika 5a at hop
    "모니카가 기분 좋은 미소를 보낸다."
    "아는 사이 맞다. 뭐, 얘기는 얼마 나누지 않았지만 일단은 작년에 같은 반이었으니까."
    "똑똑하고, 예쁘고, 운동신경이 좋기까지 한 모니카는 반에서 가장 인기있는 여학생이었다."
    "줄여서 나랑은 전혀 다른 세계에 사는 사람 정도일까."
    "그래서 그렇게 따뜻한 미소를 보내시면 나 같은건 어떻게 해, 해야…"
    mc "나, 나도, 모니카."
    show monika zorder 1 at thide
    hide monika
    show sayori zorder 3 at f31
    s 4x "[player]야, 와서 앉아! 네 자리 벌써 마련해뒀으니까. 모니카 옆에 앉으면 돼."
    s "내가 컵케이크 가져올께~"
    show sayori zorder 2 at t31
    show natsuki 1e zorder 3 at f32
    n "야! 내가 만든거거든, 내가 가져올거야!"
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 5a "미안, 너무 들떠서~"
    show sayori zorder 2 at t31
    show yuri 1a zorder 3 at f33
    y "그럼 전 차라도…"
    hide sayori
    hide natsuki
    hide yuri
    with wipeleft
    "여자애들이 책상 몇 개를 하나의 큰 탁자처럼 붙여 놓았다."
    "앞서 사요리가 말했듯 모니카와 사요리의 자리 사이에 한 자리가 비어있었다."
    "나츠키와 유리는 한 쪽 구석으로 가더니 나츠키는 뭔가로 덮힌 쟁반을, 유리는 벽장을 연다."
    "아직도 어색하기만 한 분위기 속에, 난 사요리의 옆자리에 앉는다."
    "나츠키가 위풍당당한 걸음으로 손에는 쟁반을 들고 책상으로 돌아온다."
    show natsuki 2z zorder 2 at t32
    n "그럼 공개합니다…"
    n "…짜잔!"
    show sayori 4m zorder 2 at t31
    show monika 2d zorder 2 at t33
    s "우와아아아!"
    "나츠키가 쟁반을 덮고있던 은박지를 벗기자 고양이 모양으로 장식된 열 두개의 컵케이크가 눈에 들어왔다."
    "아이싱으로 수염을 그려놓았고, 귀는 초콜릿 조각으로 되어있었다."
    show sayori zorder 3 at f31
    s 4r "진짜 귀엽다아아아~!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f33
    m 2b "너 제빵 실력 대박인데? 나츠키, 너 이런 면이 있는지 몰랐는걸?"
    show monika zorder 2 at t33
    show natsuki zorder 3 at f32
    n 2d "에헤헤. 있잖아."
    n "얼른 드시기나 하셔!"
    "사요리가 먼저 하나를 집고, 모니카가 하나를 집었다. 그렇다면 나도."
    show natsuki zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "완전 맛있어어!"
    "입안에 컵케이크를 가득 문 채로 사요리가 말했다. 다른 사람은 먹지도 않았는데 아이싱이 입가에 가득하다."
    "나는 손가락으로 컵케이크를 이리저리 돌리며 어디부터 먹어야할지 고민한다."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    show natsuki 1c zorder 2 at t32
    "나츠키가 조용하다."
    "자꾸만 내 눈치를 보는게 신경이 쓰인다."
    "내가 먹기를 기다리고 있는걸까?"
    "마침내 한 입 물었다."
    "아이싱이 참 달콤하고 풍미가 가득하다. 혹시 직접 만든걸까?"
    mc "이거 진짜 맛있다!"
    mc "고마워, 나츠키."
    n 5h "왜, 왜 나한테 고마워 하는거야? 따, 딱히….!"
    "{i}(이런 장면 어디서 많이 본 것 같은데…?){/i}"
    show natsuki at s32
    n 5s "…널 위해 만들었다거나 그런건 아닌데."
    mc "에? 결과적으로 그런게 아닐까? 사요리가 분명히…"
    show natsuki zorder 2 at t32
    n 12c "뭐, 그럴지도 모르지!"
    n "그, 그러니까, {i}널{/i} 위해 만든게 아니라고 멍청아…"
    mc "네, 네, 알겠습니다…"
    show natsuki zorder 1 at thide
    hide natsuki
    "나츠키의 이상한 논리에 할 말이 없어서 말을 끝내버렸다."
    "유리가 티 세트를 들고 돌아온다."
    "조심스럽게 각자에게 찻잔을 나눠주고 쟁반 옆에 주전자를 놓는다."
    show yuri 1a zorder 2 at t21
    mc "설마 교실에 찻잔 세트 전부를 가져온거야?"
    y "선생님들께서 허락하셨어요."
    y "책을 읽을때 차 한 잔 만한게 없으니까요. 안 그런가요?"
    mc "아… 그, 그럴지도…"
    show monika 4a zorder 2 at t22
    m "에헤헤, 그렇게 기죽지 마, 유리가 너한테 잘 보이려고 그러는거니까."
    show yuri at h21
    y 3n "에에?! 전, 전 그저…"
    "유리가 시선을 돌렸다."
    y 4b "저, 전 그, 그저…"
    mc "뭐, 책 읽을 때 차를 마시는 편은 아니지만, 차는 좋아해."
    y 2u "다행이네요…"
    "다행이라는 듯이 유리가 희미하게 웃는다."
    "모니카가 한 쪽 눈썹을 치켜올리고 나를 향해 미소짓는다."
    show yuri zorder 1 at thide
    hide yuri
    show monika zorder 2 at t11
    m 1 "그래서, 문예부는 어떻게 들어오게 된거야?"
    mc "그게…"
    "안 그래도 이런 질문 받을까 걱정했었는데."
    "그냥 사요리에게 끌려왔다고 말하면 큰일날꺼라고 본능이 얘기한다."
    mc "아니 뭐, 아직 동아리에 안 들어갔고, 사요리가 되게 즐거워하는 것 같아서, 뭐…"
    m 1j "괜찮아, 괜찮아! 창피하면 얘기 안해도 돼!"
    m 1b "우리도 최선을 다할테니까 너무 어색해 하지말고, 알았지?"
    m "문예부의 부장으로서 부원들에게 재밌는 동아리를 만들어가야 하는 건 당연한 의무니까!"
    show monika 1a
    mc "모니카, 너 대단하다."
    mc "어떻게 새 동아리를 만들 생각을 한거야?"
    mc "너라면 웬만한 동아리에 들어가도 임원정도는 쉽게 할텐데 말야."
    mc "당장 작년만 해도 너 토론회 회장이었잖아."
    m 5 "아하하, 으음, 뭐랄까…"
    m "솔직히 큰 동아리들 분위기가 감당이 안되더라구."
    m "예산을 얼마 받아야 한다느니, 선전은 어떻게 해야 한다느니, 축제는 어떻게 준비해야 하겠다느니 맨날 싸우는 일 말곤 하는 게 없는 것 같아서"
    m "그런거 할 바에야 내가 좋아하는 일을 해서 뭔가 특별한 걸 해내는 게 낫겠더라구."
    m 1b "그러다 다른 친구들이 문학에 관심을 가지게 된다면, 그게 내 꿈을 이룬 거니까 말야!"
    show monika 1a
    show sayori 3q zorder 2 at t31
    s "모니카만큼 멋진 부장이 또 어디있다구 그래!"
    show yuri 1 zorder 2 at t33
    "모니카의 말에 유리가 고개를 끄덕인다."
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide yuri
    mc "그렇게 열심히 하는데 부원이 얼마 없다는 게 놀랍네."
    mc "역시 새 동아리를 만든다는 건 어려운 건가봐."
    m 3b "그렇다고 볼 수 있지."
    m "사람들은 아예 새로운 걸 시작하는데에는 별로 관심이 없거든…"
    m "별로 인기가 없는 문학이라면 더더욱 그렇고."
    m "문예부에서의 활동이 재미가 있고 가치가 있다는 걸 알기 위해선 꽤나 공을 많이 들여야 해."
    m "그래서 학교 축제같은 중요한 행사들이 더더욱 중요해지는거고."
    m 2k "그러다 보면 우리가 졸업하기 전에는 동아리도 꽤나 키울 수 있을거야!"
    m "그치?"
    show monika 2a zorder 2 at t22
    show sayori 4r zorder 2 at t21
    s "응!"
    show monika zorder 2 at t33
    show sayori zorder 2 at t32
    show yuri 1a zorder 2 at t31
    y "최선을 다 해볼게요."
    show monika zorder 2 at t44
    show sayori zorder 2 at t43
    show yuri zorder 2 at t42
    show natsuki 4d zorder 2 at t41
    n "잘 알잖아!"
    "모두가 열정적으로 동의한다."
    "성격이 이렇게나 다른데도 같은 목표를 향해 나아간다니…"
    "이런 부원들을 찾는데에는 모니카의 상당한 노력이 있었겠지."
    "그렇기에 새 부원을 찾았다는 말에 다들 그렇게 기뻐하는지도 모르겠다."
    "과연 내가 이 여자애들만큼이나 문학에 관심을 가질 수 있을지는 모르겠지만…"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 2 at t32
    hide sayori
    hide monika
    hide natsuki
    y "저어, [player] 씨는 어떤 책을 읽는 걸 좋아하세요?"
    mc "어… 그게…"
    "최근 몇년 동안 읽은 책이 얼마 없어서 뭐라 할 말이 없는데…"
    mc "…만화…"
    "반 농담으로 조용히 얼버무린다."
    show natsuki 1c zorder 2 at t41
    "나츠키의 표정에 갑자기 활기가 넘친다."
    "뭔가 말하고 싶어 하는것 같은데, 끝내 말하지 않는다."
    show natsuki zorder 1 at thide
    hide natsuki
    y 3u "벼, 별로 책 읽는 쪽은 아닌가보네요…"
    mc "…아니, 뭐, 그거야 지금부터 바꾸면 되니까…"
    "내가 무슨 얘길 하고 있는거야?"
    "유리가 슬픈 미소를 짓자 나도 모르게 말해버렸다."
    mc "너는 어떤 책을 좋아하는데?"
    y 1l "으응, 전…"
    "찻잔 가장자리를 손가락으로 훑으며 유리가 말을 잇는다."
    y 1a "전 복잡한 세계관을 자세하게 그려내는 소설들을 좋아하는 편이에요."
    y "작가들의 창의력이나 글 솜씨에 감명을 받곤 하거든요."
    y 1f "그런 이국적인 세계에서 좋은 이야기를 그려내는 솜씨도 마찬가지구요."
    "그러고도 한참이나 좋아하는 책에 대해서 이야기를 계속한다."
    "내성적이고 소심한 성격인줄은 알았지만 책에 대해 얘기할 때 눈빛을 보아하니 역시 사람들과 관계하는 것보다는 독서를 더 좋아하는 모양이다.."
    y 2m "솔직히 좋아하는 장르는 많아요."
    y "심리적인 요소가 담긴 이야기에 푹 빠지곤 해요."
    y 2a "독자의 상상력 부족을 고의적으로 이용해 심기를 툭툭 건드리는 작가의 실력이 놀랍지 않나요?"
    y "요즘은 공포물을 자주 읽는 편이긴 하지만…"
    mc "아, 나도 공포물을 읽어본 적 있어…"
    "겨우겨우 나랑 연관 지을만한 부분을 찾아냈다."
    "이대로 가다간 유리는 돌이랑 얘기하는 꼴 날 뻔 했어."
    show monika 1d zorder 3 at f33
    m "진짜? 유리 너 진짜 의외다."
    m "순한 줄로만 알았더니…"
    show monika zorder 2 at t33
    show yuri zorder 3 at f32
    y 1a "그렇게 생각할 수도 있겠네요."
    y "깊은 생각을 가지게 한다던가, 완전히 다른 세계로 날 보내준다던가, 그런 책은 손에서 놓을 수가 없어요."
    y "특히 공포물 같은 경우에는 세상을 보는 관점을 완전히 바꿔주거든요. 설령 그게 아주 잠깐뿐이라도 말이에요."
    show yuri zorder 2 at t32
    show natsuki 5q zorder 3 at f31
    n "난 공포물같은 거 싫어…"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f32
    y 1f "응? 왜요?"
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5c "으응, 난 그냥…"
    "나츠키가 또 내 눈치를 본다."
    n 5q "별 이유는 없어."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1a "뭐, 나츠키는 귀여운 거 쓰는 걸 좋아하니까. 안 그래, 나츠키?"
    show monika zorder 2 at t33
    show natsuki 1o zorder 3 at f31
    n "뭐, 뭐라고?"
    n "누가 그래?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 3b "저번 모임 때 놔두고 간 종이 말이야."
    m "거기에 너가 쓰던 시가 있던데? 제목이…"
    show monika zorder 2 at t33
    show natsuki 1p zorder 3 at f31
    n "시끄러워!!"
    n "그리고 그거 내놔!"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f33
    m 1j "알았어, 알았어~"
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    hide monika
    hide yuri
    show natsuki 1r zorder 2 at t42
    show sayori 4q behind natsuki at l41
    s "에헤헤, 컵케이크라던가, 시라던가…"
    s "역시 나츠키답게 다 귀여워~"
    show sayori behind natsuki at t21
    "사요리가 나츠키에게 다가가 어께에 손을 올린다."
    show natsuki at h42
    n 1v "{i}난 안 귀엽거든!!{/i}"
    show natsuki zorder 2 at t11
    show sayori zorder 1 at thide
    hide sayori
    mc "나츠키, 너 시도 써?"
    n 1c "에? 응, 가끔."
    n "네가 무슨 상관이야?"
    mc "아니 그냥 멋있어서."
    mc "보여준다던가, 그럴 생각 없어?"
    n 5q "시, 싫거든!"
    "나츠키가 눈을 피한다."
    n "별로… 맘에 안 들어할껄…"
    mc "아~ 아직은 별로 자신 없는 거야?"
    show yuri 2f zorder 2 at t31
    y "나츠키의 마음을 알 것도 같아요."
    y "자기가 쓴 글을 남에게 보여준다는 건 자신감의 문제가 아니거든요."
    y 2k "진정한 글짓기는 자신에게 글을 쓸 때 나타나요."
    y "독자에게 자기 자신의 취약점들을 드러내고 속마음 깊숙히 있는 것들을 꺼내 보여줄 수 있는 용기가 있어야 해요."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 2a zorder 2 at t33
    m "유리, 너도 글 같은 거 써?"
    m "네 걸 먼저 보여주면 나츠키도 용기가 나지 않을까?"
    show yuri at s31
    y 3o "…"
    mc "유리도 자신 없긴 마찬가지인 것 같은데…"
    show sayori 2g zorder 2 at t32
    s "우우우… 나 너희들 시 읽어보고 싶은데…"
    show sayori zorder 1 at thide
    show yuri zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide yuri
    hide monika
    "잠깐, 침묵이 돈다."
    show monika 5a zorder 3 at f32
    m "좋아!"
    m "나 좋은 생각이 떠올랐어~"
    show yuri 3e zorder 2 at t31
    show natsuki 2k zorder 2 at t33
    ny "…?"
    "나츠키와 유리가 궁금하다는 표정으로 모니카를 바라본다."
    m 2b "각자 집에 가서 시를 하나씩 써 오는 거야!"
    m "다음 모임 때 각자 쓴 시를 서로에게 보여주는 거지."
    m "그럼 모두 공평한거잖아!"
    show monika 2a zorder 2 at t32
    show natsuki zorder 3 at f33
    n 5q "으…으음…"
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f31
    y "…"
    show natsuki zorder 2 at t44
    show monika zorder 2 at t43
    show yuri zorder 2 at t42
    show sayori 4r at l41
    s "좋아 좋아! 하자 하자!"
    show monika zorder 3 at f43
    m 1a "게다가 새 부원도 들어왔으니까, 어색한 것도 풀고 서로 친해질 좋은 기회가 될 수 있을 거야."
    m "그치, [player]야?"
    show monika zorder 2 at t43
    "모니카가 또다시 나에게 따뜻한 미소를 보낸다."
    mc "잠깐 잠깐… 그건 좀."
    show monika zorder 3 at f43
    m 1d "에? 뭔데?"
    "새 부원 얘기로 돌아왔으니 이제 직설적으로 얘기할 필요가 있다."
    show monika zorder 2 at t43
    mc "나 아직 이 동아리 들어온다고 안 했는데."
    mc "사요리가 들려보라고 해서 들린 것뿐이고, 아직 들어온다는 결정은 안했으니까."
    mc "아직 다른 동아리들도 들려볼꺼고, 그리고… 어…"
    show monika 1g
    show sayori 1g
    show natsuki 4g
    show yuri 2e
    "머릿속이 새하얘진다."
    "그렇게 실망한 눈빛으로 쳐다보면 전 어떻게 해야 합니까."
    show monika at s43
    m 1p "그, 그치만…"
    show yuri at s42
    y 2v "죄, 죄송해요, 전 또…"
    show natsuki at s44
    n 5s "흥."
    show sayori at s41
    s 1k "[player]…"
    mc "어, 그러니까…"
    "나…난 틀렸어."
    "그런 눈으로 쳐다보면 냉정하게 판단을 내릴 수가 없잖아…"
    "그, 그래. 시 몇 편 쓰는 것 만으로도 이 여자애들과 함께할 수 있다면…"
    mc "…그래."
    mc "좋아, 결정했어."
    mc "문예부에 들어갈게."
    show monika 1e zorder 2 at t43
    show yuri 3f zorder 2 at t42
    show natsuki 1k zorder 2 at t44
    show sayori 4b zorder 2 at t41
    "한 명, 한 명, 표정이 서서히 밝아진다."
    show sayori at h41
    s 4r "예에에! 행복해~"
    "사요리가 날 감싸 안고 방방 뛴다."
    mc "어, 어이!"
    show yuri zorder 3 at f42
    y 1m "정말! 놀랐잖아요…"
    show yuri zorder 2 at t42
    show natsuki zorder 3 at f44
    n 5q "진짜 컵케이크 먹으려고만 온 거였으면 정말 화냈을 거야."
    show natsuki zorder 2 at t44
    show monika zorder 3 at f43
    m 5 "자 그럼 정해진 거다?"
    m "문예부에 온 걸 환영해!"
    show monika zorder 2 at t43
    mc "아아, 고마워."
    show yuri zorder 1 at thide
    show natsuki zorder 1 at thide
    show sayori zorder 1 at thide
    show monika zorder 2 at t11
    hide yuri
    hide natsuki
    hide sayori
    m 3b "자 그럼, 여러분!"
    m "이것으로 오늘의 모임은 마치겠습니다."
    m "모두 오늘 숙제 잊지마! 시 써오는거 말야."
    "모니카가 다시 나를 바라본다."
    m 1a "[player], 난 네 시가 기대되는걸."
    show monika 5 at hop
    m "에헤헤~"
    mc "그, 그래…"
    show monika zorder 1 at thide
    hide monika
    "과연 평범하기 짝이 없을 게 뻔한 내 글쓰기 실력으로 모니카의 기대를 만족시킬 수 있을지 모르겠다."
    "벌써부터 부담이 팍팍 든다."
    "유리와 나츠키는 먹은 것을 치우면서도 다른 여자애들과 계속 수다를 떨고 있다."
    show sayori 1a zorder 2 at t11
    s "있지 [player]야, 다른 일 없으면 집에 같이 가지 않을래?"
    "그러고 보니 사요리가 부 활동 하면서 학교에 오래 남아있는 바람에 요새 집으로 같이 간 적이 없다."
    mc "그래, 그러자."
    s 4q "에에에~"

    scene bg residential_day
    with wipeleft_scene

    "그렇게 우리는 교실을 나서 집으로 돌아온다."
    "돌아오는 길에도 내 마음은 네 명의 소녀들 생각으로 가득 차 있다."
    show sayori 1 zorder 2 at t41
    "사요리,"
    show natsuki 4 zorder 2 at t42
    "나츠키,"
    show yuri 1 zorder 2 at t43
    "유리,"
    show monika 1 zorder 2 at t44
    "그리고 모니카까지."
    "과연 내가 매일 방과 후 시간을 문예부에서 보내는 걸 좋아할 수 있을까?"
    "어쩌면 여자애들 중 하나와 더 가까워질 수 있는 계기가 될 수도…"
    hide sayori
    hide natsuki
    hide yuri
    hide monika
    with wipeleft
    "좋아!"
    "어차피 하기로 한 거, 최선을 다하면 행운이 따를지도 몰라."
    "천릿길도 한 걸음부터라고. 그럼 시부터 써봐야겠지?"


    return

label ch0_kill:
    $ s_name = "사요리"
    show sayori 1b zorder 2 at t11
    s "…"
    s "…"
    s "뭐, 뭐야…"
    s 1g "…"
    s "이게…"
    s "이게 다 뭐야…?"
    s "아아…"
    s 1u "아…"
    s "이거 꿈이지?"
    s "이거 사실 아니지?"
    s 4w "이거 뭐야?"
    s "난 뭐야?"
    s "멈춰줘!"
    s "제발 그만해!"

    $ delete_character("sayori")
    $ delete_character("natsuki")
    $ delete_character("yuri")
    $ delete_character("monika")
    $ renpy.quit()
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
