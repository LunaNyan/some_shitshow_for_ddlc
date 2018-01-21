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

init python:
    class RectCluster(object):
        def __init__(self, theDisplayable, numRects=12, areaWidth = 30, areaHeight = 30):
            self.sm = SpriteManager(update=self.update)
            self.rects = [ ]
            self.displayable = theDisplayable
            self.numRects = numRects
            self.areaWidth = areaWidth
            self.areaHeight = areaHeight
            
            for i in range(self.numRects):
                self.add(self.displayable)
        
        def add(self, d):
            s = self.sm.create(d)
            s.x = (random.random() - 0.5) * self.areaWidth * 2
            s.y = (random.random() - 0.5) * self.areaHeight * 2
            s.width = random.random() * self.areaWidth / 2
            s.height = random.random() * self.areaHeight / 2
            self.rects.append(s)
        
        def update(self, st):
            for s in self.rects:
                s.x = (random.random() - 0.5) * self.areaWidth * 2
                s.y = (random.random() - 0.5) * self.areaHeight * 2
                s.width = random.random() * self.areaWidth / 2
                s.height = random.random() * self.areaHeight / 2
            return 0

image n_rects_ghost1:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (580, 270)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost2:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (652, 264)
    size (20, 25)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost3:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (616, 310)
    size (25, 15)
    alpha 0.0
    8.0
    easeout 12 alpha 1.0

image n_rects_ghost4:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (735, 310)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -250

image n_rects_ghost5:
    RectCluster(Solid("#000"), 4, 15, 5).sm
    pos (740, 376)
    size (25, 20)
    0.5
    easeout 0.25 zoom 4.5 xoffset 250 yoffset -100

label natsuki_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    n "으윽…!"
    "벽장 안에서 서러움이 잔뜩 섞인 나츠키의 한숨이 흘러나온다…."
    "뭔가 짜증이 잔뜩 난 것 같은데."
    "혹시나 도움이 필요하지 않을까 싶어서 살펴본다."
    play music t6 fadeout 1
    scene bg closet
    show natsuki 4r zorder 2 at t11
    with wipeleft_scene
    $ style.say_dialogue = style.normal
    mc "뭔가 찾고있어?"
    $ style.say_dialogue = style.edited_nobreak
    n 4x "모니카 씨발년이ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ"
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "빌어먹을 모니카 때문에 말야…."
    n "자꾸 내 물건 제자리에 안 두고 이상한데 두잖아!"
    n "정리하는 사람 따로 있고, 어지르는 사람 따로 있고, 이러면 컬렉션을 정리해두는 의미가 없잖아!"
    "나츠키가 책 여러 개와 박스 몇 개를 선반 한쪽으로 민다."
    mc "만화…."
    n 2c "너 만화 읽지?"
    mc "아…."
    mc "…응, 가끔은…."
    "만화를 읽는 다는 것은 상대가 나와 같은 부류라는 걸 알기 전까지는 인정할 수 없는 것이다."
    mc "…어떻게 알았어?"
    n 2k "전에 말하는 거 들었고."
    n "네 얼굴에 다 쓰여 있으니까."
    "도대체 어딜 봐서…?"
    mc "으, 응…."
    "여러 책들이 쌓여있는 가운데, 유일하게 딱 한 권 만화가 끼워져있다."
    "괜히 궁금해져서 꺼내봤다."
    n 1b "{i}거기{/i} 있었네!"
    "나츠키는 책을 내 손에서 낚아채갔다."
    "그러더니 만화 상자로 몸을 돌려 가운데에 책을 넣었다."
    n 4d "아아, 편안하다!"
    n "딱 한 권 빠져있는 세트를 보는 건 아마도 세상에서 제일 짜증나는 일일 거야."
    mc "무슨 느낌인지 알아…."
    "난 나츠키가 그토록 좋아하는 상자 세트를 자세히 들여다 보았다."
    mc "파르페 걸스…?"
    "한 번도 들어본 적 없는 시리즈인데…."
    "아마 내 뇌 속 통계학에 정리되어있지 않은 것이거나, 망작이거나 둘 중 하나겠지."
    n 5g "평가를 내릴 거면, 그냥 저기 유리문 밖으로 나가면 돼."
    "나츠키는 교실 문을 가리켰다."
    mc "야, 야. 딱히 평가하려던 건 아니였어…!"
    mc "아무 말도 안 했잖아."
    n 5c "네 목소리 톤이 그랬어."
    $ style.say_dialogue = style.normal
    n "한 가지 알려줄게, [player]."
    n 4l "문예부가 주는 교훈:{nw}"
    $ _history_list[-1].what = "문예부가 주는 교훈: 표지만 보고 책을 판단하지 말아라!"
    $ style.say_dialogue = style.edited
    n "표지만 보고ㅗㅗㅗㅗㅗㅗㅗ ㅗㅗㅗ ㅗㅗㅗㅗㅗ ㅗㅗ{space=20}ㅗ{space=40}ㅗ{space=120}ㅗ{space=160}ㅗ{space=200}ㅗ"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    n "좋아…."
    "나츠키는 파르페 걸스 1권을 꺼냈다."
    n "내가 그 이유를 보여주지!"
    "나츠키는 내 손 안에 책을 밀어넣었다."
    mc "아…."
    "나는 표지를 바라보았다."
    "화려한 의상을 입은 네 명의 여성들이 생기넘치는 포즈를 취하고 있다."
    "이거… \"모에\"하다."
    n 4b "거기 서 있지만 말고!"
    mc "으아…."
    show natsuki zorder 1 at thide
    hide natsuki
    "나츠키는 내 팔을 붙잡고 나를 벽장 밖으로 끌어냈다."
    "그러더니 창문 아래 벽에 기대어 앉았다."
    "나츠키는 자기 옆을 손바닥으로 툭툭 치면서 나에게 여기 앉으라는 신호를 보낸다."
    show bg club_day
    show natsuki 2a zorder 2 at t11
    with wipeleft
    mc "의자에 앉는 게 더 편하지 않을까…?"
    "난 자리에 앉았다."
    n 2k "의자는 소용없어."
    n "의자에 앉으면 동시에 읽을 수가 없잖아."
    mc "응? 왜?"
    mc "아… 이러는 게 더 가까이 있기에 쉬워서 그렇구나…."
    n 2o "…!"
    n 5r "그, 그런 식으로 말하지 마!"
    n "이상한 기분이 들잖아!"
    "나츠키는 팔짱을 끼고 1미터 정도 떨어지면서 나에게 소리쳤다."
    mc "미안…."
    show natsuki 5g
    "이렇게 나츠키랑 가까이 있게 될 줄은 몰랐는데…."
    "그렇다고 이게 나쁜 일은 아니다."
    "난 책을 폈다."
    "나츠키는 내가 알아차리지 못하도록 천천히 나에게 다가왔다."
    "난 어깨 너머로 나츠키의 시선을 느낄 수 있었다."
    n 1k "와, 나 첫 부분 읽은 지 얼마나 오래된 거지…?"
    mc "음?"
    mc "그냥 전에 읽은 부분 다시 읽으면 되지 않아?"
    n 2k "글쎄."
    n "가끔 시리즈를 전부 다 읽은 다음에 읽어."
    n 2c "것보다, 집중하고 있는 거야?"
    mc "어…."
    "집중하고 있지만, 아직 아무런 흥미로운 일이 일어나지 않았으니 말이다."
    "내용은 그냥 고등학생들에 관한 이야기인 것 같아."
    "전형적인 일상물인 것 같은데…."
    "이런 것들은 대부분 줄거리가 허술해서 재미가 떨어지기 때문에, 읽지 않게 된 지 꽤 됐다."
    $ persistent.clear[0] = True
    scene n_cg1_bg
    show n_cg1_base
    with dissolve_cg
    mc "…지루하지 않은 거 확실해?"
    n "안 지루해!"
    mc "그냥 내가 읽는 걸 보는 건데도?"
    n "글쎄…!"
    n "괜찮아…."
    mc "뭐, 네가 그렇다면…."
    mc "…자기가 좋아하는 걸 다른 사람과 공유하는 건 재밌는 일이지."
    mc "난 내가 재밌게 보는 만화를 친구랑 같이 보면 되게 재밌던데."
    mc "무슨 말인지 알겠어?"
    n "…?"
    mc "으음?"
    mc "이해 못 했어?"
    show n_cg1_exp2 at cgfade
    n "음…."
    n "그게 아니라…."
    n "…맞아, 잘 모르겠어."
    mc "…그게 무슨 말이야?"
    mc "친구랑 같이 만화 읽어본 적 없어?"
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "그래, 없다."
    n "어쩔래…?"
    mc "아, 미안…."
    n "흐응."
    n "친구한테 추천해주면…."
    n "다들 만화는 애들이나 읽는 거라고 생각하더라고."
    n "그런 애들이랑은 말도 하기 싫더라…."
    n "'에에? 너 아직 어린 애니?'"
    n "진짜 얼굴에 주먹을 갈기고 싶다니까…."
    mc "으으, 나도 그런 부류들 알지…."
    mc "솔직히 그러지 않는 친구를 찾는 데에는 되게 큰 노력이 필요한 거 같아. 같은 만화 읽는 친구를 찾는 거는 더 어렵고."
    mc "나는 이미 패배자니까, 그래서 다른 패배자들한테 끌린 건 가봐."
    mc "아마 너 같은 사람한테는 더 힘들겠지…."
    hide n_cg1_exp3
    n "흠."
    n "맞아, 꽤 정확해."
    "{i}…잠깐, 어느 부분이??{/i}"
    $ style.say_dialogue = style.normal
    n "내 말은, 이 책들을 내 방에 놔둘 수도 없을 것 같아…."

    $ style.say_dialogue = style.edited
    n "만약 아빠가 발견한다면 날 죽여버릴지도 몰라."
    $ style.say_dialogue = style.normal
    $ _history_list[-1].what = "이런 게 내 방에 있는 걸 알면 아빠가 어떤 반응을 보일지 모르겠어…."
    n "적어도 여기에 있으면 안전하니까 괜찮아."
    show n_cg1_exp3 at cgfade
    n "''모니카가 좀 이상하게 놓는 거 빼면…."
    n "모니카는 이길 수가 없다니까…."
    mc "결국 성과가 있있잖아, 그렇지?"
    mc "내 말은… 지금 나도 이렇게 읽고 있고."
    n "뭐, 그렇다고 내 문제가 해결되는 건 아니야."
    mc "그렇지…."
    mc "그래도 넌 즐기고 있잖아."
    hide n_cg1_exp3
    show n_cg1_exp2 at cgfade
    n "…."
    n "…."
    n "…그래서?"
    mc "아하하."
    hide n_cg1_exp2
    show n_cg1_exp3 at cgfade
    n "아오, 됐어!"
    n "계속 읽을 거야, 말 거야?"
    mc "네, 네…."
    "난 페이지를 넘겼다."
    show black with dissolve_cg
    "…."
    "…."
    "……."
    "……."
    "………."
    "시간이 지났다."
    hide n_cg1_exp3
    show n_cg1_exp4 behind black at cgfade
    "나츠키가 이상하리만치 조용하다."
    "나는 나츠키를 바라보았다."
    hide black with dissolve_cg
    "잠들기 시작한 거 같은데…."
    mc "야, 나츠키…."
    hide n_cg1_exp4
    show n_cg1_exp5 at cgfade
    n "으, 응…?"
    "갑자기 나츠키가 내 쪽으로 쓰러졌다."
    play sound fall
    $ style.say_dialogue = style.normal
    mc "ㅇ, 야…."
    show n_cg1_exp5
    hide n_cg1_exp5

    show n_cg1b
    hide n_cg1_base

    $ currentpos = get_pos()
    $ audio.t6g = "<from " + str(currentpos) + " loop 10.893>bgm/6g.ogg"
    play music t6g
    $ ntext = glitchtext(96)
    $ style.say_dialogue = style.edited
    n "{color=#000}[ntext]{/color}"
    $ ntext = glitchtext(96)
    n "{color=#000}[ntext]{/color}"
    $ style.say_dialogue = style.normal

    stop music
    window hide(None)
    window auto
    scene bg club_day
    show monika 1r zorder 2 at t11
    m "오, 이런…."
    m 1d "나츠키, 괜찮아?"
    show monika zorder 2 at t21
    show natsuki 12b zorder 3 at f22
    n "…."
    show natsuki zorder 2 at t22
    show monika zorder 3 at f21
    m 1a "여기 있다…."
    show monika zorder 2 at t21
    "모니카는 가방에서 초코바를 몇 개 꺼냈다."
    "그러더니 나츠키가 있는 쪽으로 집어던졌다."
    "나츠키의 눈이 갑자기 번뜩이기 시작했다."
    "나츠키는 바닥에 있는 초코바를 잡아채고는 곧바로 포장지를 뜯어냈다."
    show natsuki zorder 3 at f22
    n 1s "내가 이런 거 주지 말라고음얌냠…."
    show natsuki zorder 2 at t22
    "나츠키는 말을 다 하기도 전에 음식을 입안에 쑤셔 넣었다."
    show natsuki zorder 1 at thide
    hide natsuki
    show monika 3b zorder 2 at t11
    m "걱정하지 마, [player]."
    m "괜찮으니까."
    m "가끔 있는 일이야."
    m 1a "이래서 내가 항상 간식을 가방에 두고 다니지."
    m 5a "어쨌든…!"
    m "이제 시를 나눠볼까?"

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
