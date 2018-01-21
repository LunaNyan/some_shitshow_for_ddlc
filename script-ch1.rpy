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

label ch1_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    show monika 5 zorder 2 at t11
    $ finalConso = finalChecker(player)

    m "안녕, [player]!"
    m "도망가지 않았다니 다행이네. 하하하!"
    mc "에이, 그런 걱정은 하지도 마."
    mc "난 한다면 하는 사람이라, 적어도 약속은 지켜."
    show monika zorder 1 at thide
    hide monika
    "결국, 난 문예부에 돌아왔다."
    "내가 마지막에 들어온 사람이라, 모두 벌써 얘기를 나누고 있었다."
    show yuri 1a zorder 2 at t32
    y "약속을 지켜주셔서 고마워요, [player]."
    y "글에 익숙하지 않으실 텐데 이렇게 와 주시고."
    y 1u "저희가 괜히 너무 어려운 결정을 내리게 만든 건 아닌지…."
    show natsuki 4e zorder 2 at t33
    n "저기! 얘가 어떤 앤 줄은 알고 그러는 거야?"
    n "올해 네가 동아리 따위엔 관심 없었다는 걸 사요리가 말해줬어."
    n "그리고 작년에도!"
    n 4c "네가 그냥 놀러 온 건지는 잘 모르겠지만…."
    n "진지하게 임하지 않으면, 오래 못 갈 줄 알아."
    show monika 2b at l41
    m "나츠키, 문예부실에 만화 컬렉션을 넣고 다니는 사람이 할 말은 아닌 것 같은데…."
    n 4o "몬… 만……!!"
    show monika at lhide
    hide monika
    "나츠키는 \"모니카\" 와 \"만화\"를 동시에 말하려다 혀가 꼬여버렸다."
    show natsuki at h33
    n 1v "만화도 문학이야!!"
    show natsuki zorder 1 at thide
    hide natsuki
    "혼자 찌뿌둥해져서 꼬리를 말듯 자리에 앉는 나츠키."
    show yuri zorder 2 at t22
    show sayori 2x zorder 3 at f21
    s "얘들아, 걱정하지 마~"
    s "[player]는 자기 싫은 일만 아니면 항상 열심히 할 거야."
    s "내가 부탁하지 않아도 힘든 일도 도와줘."
    s "요리라던가, 내 방 청소라던가…."
    show sayori 2a zorder 2 at t21
    show yuri zorder 3 at f22
    y 2m "너무 믿음직하네요…."
    show yuri zorder 2 at t22
    mc "사요리, 그건 네 방이 너무 더러워서 그냥 넘어가기가 힘들어서 그랬던 거고."
    mc "그리고 한 번은 너 집에 불낼 뻔한 적이 있었으니까."
    show sayori at s21
    s 5 "그랬었지… 에헤헤…."
    show yuri zorder 3 at f22
    y 1s "두 분은 정말 친한 친구군요."
    y "조금 질투가 날지도…."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 1 "왜? 유리랑 [player]도 좋은 친구가 될 수 있어!"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 4b "으…음…."
    show yuri zorder 2 at t22
    mc "사…사요리."
    show sayori zorder 3 at f21
    s "응?"
    show sayori zorder 2 at t21
    mc "…."
    "언제나 그랬듯, 사요리는 또 다시 한번 나를 곤경에 빠뜨린다 ."
    show sayori zorder 3 at f21
    s 4x "아, 맞다! 있지, 오늘 유리가 너한테 줄 게 있다는데~"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y 3n "자… 잠깐만요! 사요리 씨…."
    show yuri zorder 2 at t22
    mc "응? 나한테?"
    show yuri zorder 3 at f22
    y 3o "어… 그게…."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 4r "부끄러워 하지 마~"
    show sayori zorder 2 at t21
    show yuri zorder 3 at f22
    y "별 건 아니지만요…."
    show yuri zorder 2 at t22
    mc "뭔데 그래?"
    show yuri zorder 3 at f22
    y 4c "아…아무 것도 아니에요!"
    y "진짜로 별 건 아닌데 사요리 씨가 굉장한 것처럼 말씀하셔서…."
    y "어… 어쩌지…."
    show yuri zorder 2 at t22
    show sayori zorder 3 at f21
    s 1g "응? 유리야, 미안해… 난 그런 뜻이…."
    show sayori zorder 1 at thide
    hide sayori
    show yuri zorder 2 at t11
    "이럴 땐 내가 나서야겠지?…."
    mc "저기, 걱정하지마."
    mc "애초에, 뭘 받을 거라고 기대하고 온 것도 아니고."
    mc "뭘 준비했든 간에 나에게는 깜짝 선물인걸."
    mc "그 성의만으로도 난 감동이야."
    y 3v "그… 그런가요…."
    mc "그래. 원하지 않는다면 나도 호들갑 떨지는 않을 테니까."
    y "알겠습니다…."
    y 1a "그럼, 여기요."
    "유리는 가방에서 책을 하나 꺼내어 건네주었다."
    y "소외감을 느끼시지 않게…."
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


    "이제 모두 왔으니 모니카가 준비해온 부 활동을 시작하겠지."
    "…라고 생각했건만 그게 아닌 것 같다."
    "사요리와 모니카는 한쪽 구석에서 수다를 떨고 있고."
    "유리는 책에 코를 박고 있다."
    "이때만을 기다렸다는 듯 긴장된 표정으로 책을 읽는 모습이 안 보려야 안 볼 수가 없다."
    "한편, 나츠키는 벽장 안을 뒤지고 있었다."


    $ nextscene = poemwinner[0] + "_exclusive_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_22


    show monika 1 zorder 2 at t21
    hide sayori
    hide natsuki
    hide yuri
    m "근데, 시 써오는 건 잊지 않았지?"
    mc "으… 응…."
    "맘 편히 놀던 시간이 끝이 나버렸다."
    "내가 이런 부끄러운 짓을 정말로 하기로 했다니."
    "한 번도 안 해봤던 짓이라 영감도 안 떠오르던데."
    m "그럼, 모두 준비가 된 것 같으니까, 네가 먼저 누구랑 시를 나눠볼지 선택하는 게 어때?"
    show sayori 4q zorder 2 at t22
    s "기대된다~!"
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    "사요리와 모니카가 주저 없이 각자의 시를 꺼낸다."
    "사요리는 스프링노트에서 방금 막 찢어낸 듯한 잔뜩 구겨진 종이를 들고 있고,"
    "반면에 모니카는 제대로 된 공책에 깔끔하게 쓴 모양이다."
    "깔끔한 모니카의 손글씨가 한눈에 들어온다."
    "나츠키와 유리도 마지못해 가방 속으로 손을 넣는다."
    return


label ch1_end:
    stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    play music t3
    mc "휴우…."
    "모두와 시를 나눠 보았다."
    "그리곤 잠시 교실을 둘러보았다."
    "지극히 평범한 내 글쓰기 실력을 평가받는 꼴이라니…."
    "생각했던 것보다 더 힘든 일이었다."
    "잘해주려고는 한다지만, 내가 봐도 내 시는 다른 애들 시에 비하면 그냥 낙서 수준이다."
    "하긴. 여기는 문예부니까."
    "나는 한숨을 쉬었다."
    "결국은 내가 자초한 일이니까."
    "교실 맞은편에는 사요리와 모니카가 웃으며 얘기하고 있었다."
    "내 눈은 유리와 나츠키에게 멈췄다."
    show yuri 2g zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "둘은 조심스레 서로의 시를 교환했다."
    show yuri 2i at t21
    "조용히 시를 읽어내려가는데, 표정이 바뀌는 게 눈에 보일 정도다."
    "나츠키는 답답해하며 눈썹을 찌푸리고."
    "유리는 슬프게 미소를 짓는다."
    show natsuki zorder 3 at f22
    n 1q "{i}(단어 선택이 왜 이래…?){/i}"
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
    y "전 그냥 좋은 말을 하려고 한 건데…."
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
    n "내가 의견을 듣고 싶은 거였다면, 이걸 좋아하는 사람한테 물어봤겠지."
    n "그리고 {i}너만 빼고{/i} 다 좋아했거든?"
    n 5e "사요리가 좋아했어."
    n "그리고 [player]이도!"
    n "그러니까, 내가 친히 너에게 내 의견을 말해주지."
    n "우선……."
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 2l "죄송해요…."
    y "말씀은 감사하지만, 전 제 문체를 정하는데 엄청난 시간을 썼어요."
    y 2h "특별한 영감이 떠오르지 않는다면 바꾸지는 않을 것 같아요."
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
    play music t7
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 1n "에…에?!"
    y "전 그런 게…!"
    y 1o "우…."
    y "나… 나츠키 씨야말로…."
    "유리도 일어섰다."
    y 2r "[player]씨가 나츠키 씨 조언보다 제 조언을 더 좋아하셨다고 질투하시는 거 아니에요?"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1e "참나! {i}내{/i} 조언을 더 좋아했는지 네 조언을 더 좋아했는지 네가 그걸 어떻게 알아?"
    n "네가 그렇게 잘났어?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3h "전…!"
    y "아뇨…."
    y "제가 그렇게 잘났으면…."
    y 1r "…제가 하는 짓마다 과하게 귀엽게 하고 다녔겠죠!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1o "으으으으으으으…!"
    show sayori 2l behind yuri, natsuki at l41
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    s "저…저!!"
    s "다들 괜찮아…?"
    show sayori 2 at lhide
    hide sayori
    show natsuki zorder 3 at f33
    n 1f "있지, 그거 알아?!"
    n "난 누구처럼 [player]가 나타나고 나서 마법같이 가슴이 커지거나 하진 않거든!"
    show yuri 3p at h32
    show natsuki zorder 2 at t33
    y "나… 나츠키 씨!!"
    show monika 3l behind yuri, natsuki at l41
    m "저기, 나츠키, 그건 좀…."
    show monika at h41
    show yuri 3p zorder 3 at f32
    show natsuki 1e zorder 3 at f33
    ny "너랑은 관련 없잖아!\n모니카 씨는 상관없잖아요…!"
    show monika at lhide
    hide monika
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show sayori 4p behind yuri, natsuki at l41
    s "싸우지 마, 얘들아…!"
    show sayori at lhide
    hide sayori
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "내가 옆에 있다는 걸 드디어 알아차린 두 명은 갑자기 날 바라보며 섰다."
    show yuri zorder 3 at f21
    y 2n "[player] 씨…!"
    y "나… 나츠키 씨는 그냥 절 나쁜 사람으로 만드려고…!"
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 4w "아니야!"
    n "유리가 먼저 시작했어!"
    n 4e "유리가 {i}간단 명료하게{/i} 글 쓰는 방법이 더 효과적이라는 걸 인정했으면…."
    n "이런 싸움같은 건 벌어지지도 않았을 거야!"
    n "이유도 없이 시를 이리저리 꼬아서 난해하게 만들어 놓으면 의미가 없잖아?"
    n "시는 내용을 독자에게 바로 전할 수 있어야 하는거야. 시험지처럼 계속 들여다봐야 이해할 수 있게 하는 게 아니라!"
    n 1f "[player]야, 쟤한테 설명 좀 해봐!"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 3o "잠, 잠깐만요!"
    y "언어에는 복잡하고 의미심장한 단어들이 있는 이유가 있어요!"
    y 3w "그게 복잡한 감정을 설명할 수 있는 유일한 수단이기 때문이죠."
    y "그런 단어들을 쓰지 않는다면 감정이 제한될 뿐만 아니라… 낭비잖아요!"
    y 1t "[player] 씨, 당신이라면 이해하시죠, 그렇죠?"
    show yuri zorder 2 at t21
    mc "어…."
    show yuri 1t zorder 3 at f21
    show natsuki 1e zorder 3 at f22
    ny "똑바로 말해!\n말씀해 보세요!"
    mc "…."
    show yuri zorder 2 at t21
    show natsuki 1g zorder 2 at t22
    "어쩌다 이게 이 지경까지 온 거지?!"
    "내가 글쓰기에 그렇게 대단한 것도 아니고…."
    "가만, 이거 점수 딸 기회가 온게 아닐까?"
    menu:
        "그렇다면야 나는…!"
        "나츠키를 고른다.":
            call ch1_end_natsuki from _call_ch1_end_natsuki
        "유리를 고른다.":
            call ch1_end_yuri from _call_ch1_end_yuri
        "사요리, 도와줘!":
            call ch1_end_sayori from _call_ch1_end_sayori

    scene bg club_day
    show monika 4b zorder 2 at t11
    with wipeleft_scene
    m "자, 그럼!"
    m "슬슬 갈 시간인 것 같네."
    m "서로의 시 공유하는 거, 다들 어땠어?"
    show monika 4a
    show sayori 4x zorder 2 at t31
    s "엄청 재미있었어!!"
    show sayori behind yuri at thide
    show yuri 1i zorder 2 at t31
    hide sayori
    y "글쎄요, 가치 있었다고나 할까요."
    show yuri behind natsuki at thide
    show natsuki 4q zorder 2 at t31
    hide yuri
    n "괜찮았어. 뭐, 대체적으로."
    show natsuki zorder 1 at thide
    hide natsuki
    m 1a "[player]야, 넌 어땠어?"
    mc "…그래, 나도 똑같았어."
    mc "모두랑 얘기를 나눈다는 건 참 좋은 일이네."
    m 1j "좋아!"
    m 1a "그렇다면 내일도 또 해볼까?"
    m "서로에게서 배운 점이 있었을 거라고 생각해."
    m 3b "그럼 네 시도 더 좋아지겠지?"
    mc "…."
    show monika zorder 1 at thide
    hide monika
    "뭐, 배운 점이 있기야 있지. 각자가 어떤 스타일의 시를 좋아하는지를 말야."
    "운이 좋다면 점수 딸 때 유용하게 쓸 수 있을지도 모르겠네."
    "…라고 생각하며 혼자 결연하게 고개를 끄덕인다."
    show sayori 1x zorder 2 at t11
    s "[player]!"
    s "집에 갈 준비는 됐어?"
    mc "응, 가자."
    s 4q "에헤헤~"
    "사요리는 나를 보며 웃었다."
    "그러고 보니 사요리와 이렇게 많은 시간을 같이 보낸 지도 꽤 되었다."
    "싫다는 건 아니지만."
    scene bg residential_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    mc "사요리…."
    mc "아까 일어난 일 말인데…."
    s 1b "에? 뭐 말하는 거야?"
    mc "있잖아, 유리랑 나츠키."
    mc "저런 일이 자주 일어나는 거야?"
    s 4j "아냐, 아냐, 아냐!"
    s "저 둘이 저렇게 싸우는 거 처음 봐…."
    s "둘 다 되게 멋진 친구들이야."
    show sayori at s11
    s 1g "너 혹시… 저 둘이 싫다거나 하는 건 아니지??"
    mc "아냐, 그렇지 않아!"
    mc "그냥 네 의견이 듣고 싶었던 것뿐이야."
    mc "좋은 사이인 것처럼 보여서."
    show sayori zorder 2 at t11
    s 1d "휴…."
    s "있지, [player]…."
    s "같은 동아리에서 시간 같이 보내니까 정말 좋은 거 같아."
    s "근데 너랑 다른 사람들이 어울리는 걸 보니까, 그게 더 좋은 것 같아."
    s 1x "그리고 모두 널 좋아한다고 생각해!"
    mc "그건……!"
    s 4q "에헤헤~"
    s "하루하루가 점점 재미있어지겠지~?"
    mc "하아…."
    "사요리는 아직도 내가 어떤 상황에 부닥쳐있는지 모르는 것 같다."
    "아니 뭐, 친구를 사귄다는 건 좋은 일이긴 한데…."
    "…거기서 그만둬야 하는 걸까?"
    mc "기다리면 미래는 와, 사요리."
    "나는 사요리의 어깨를 두드렸다."
    "사요리에게 말한다기보다, 나 자신에게 말한 거지만. 가끔 사요리는 독백에 도움이 된다니까."
    show sayori at h11
    s 1x "그래~!"
    "그래…."
    "한번 해 보자!"
    return

label ch1_end_natsuki:
    $ ch1_choice = "natsuki"
    stop music fadeout 1.0
    mc "음…."
    mc "유리!"
    mc "넌 정말 재능있어."
    show yuri 4a at s21
    y "에? 그… 글쎄요…."
    play music t8
    mc "하지만 나츠키의 말이 일리가 있어!"
    mc "그렇게 생각해…."
    show yuri zorder 2 at t21
    "난 무슨 변명거리라도 만들려고 뇌를 쥐어짰다."
    mc "난 단 몇 개의 단어로 감정을 표현할 수 있다는 게…."
    mc "되게 의미 있는 표현 방법이라고 생각해!"
    mc "독자들의 상상력을 자극해주잖아."
    mc "그리고 나츠키의 시는 그걸 완벽하게 해냈어."
    show natsuki zorder 3 at f22
    n 5y "…그래!!"
    n "맞아, 그렇지?!"
    n "아하하!"
    n "이제 {i}네{/i} 실력이 어느 정도인지 알겠어?"
    show natsuki zorder 2 at t22
    show yuri zorder 3 at f21
    y 4b "하, 하지만…."
    show yuri zorder 2 at t21
    mc "나츠키…."
    mc "그쯤 해 둬."
    show natsuki zorder 3 at f22
    n 1m "뭐?"
    n "나?"
    n "그치만 유리가 쏘아붙이는 거 못 봤어?"
    "나츠키가 울먹이며 말했다."
    show natsuki zorder 2 at t22
    mc "저기…."
    mc "아무래도 어제 했던 말이 맞다고 생각해."
    mc "글쓰기는 되게 개인적인 거라."
    mc "이렇게 서로 시 공유하기가 힘들다는건 잘 알아."
    mc "오늘 같은 일이 벌어지고는 하니까 말이야."
    mc "아주 작은 비판도 상대방은 민감하게 받아들일 수도 있어."
    "어깨너머 살짝 눈치를 봤다."
    "사요리는 힘차게 끄덕였다."
    mc "그러니까, 저…."
    mc "비판에 겁먹을 필요 없어."
    mc "어찌 됐든 넌 대단한 작가야, 나츠키."
    show natsuki zorder 3 at f22
    n 1h "아…."
    "나츠키는 예상치 못한 말을 들어서 놀랐는지 말을 더듬는다 ."
    n 1q "…알아줘서 고마워."
    "잘 들리지도 않는 목소리로 짧게 얼버무린다."
    show natsuki zorder 2 at t22
    mc "유리…."
    show yuri zorder 3 at f21
    y 4a "…?"
    "유리는 맥없이 날 바라보았다."
    "저기… 그런 표정 짓고 있으면 마음 약해지잖아."
    show yuri zorder 2 at t21
    mc "나츠키도 분명 본심이 아녔을 거야."
    mc "그러니까 너도 그렇게 신경쓰지 마."
    show yuri zorder 3 at f21
    y 2v "으응…."
    y "그렇게 말씀하신다면야…."
    show yuri zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1g "저기…!"
    n "나 {i}대신{/i} 사과할 필요 없거든?"
    n 1w "치."
    "나츠키가 짧게 숨을 들이마신다."
    n 1q "난…."
    n "있잖아…."
    n "으으…."
    "나츠키가 주변 눈치를 본다."
    show natsuki zorder 3 at hf22
    n 1x "{i}너희, 나 좀 그만 쳐다보면 안 될까??{/i}"
    "조금 전의 그 당당한 태도와는 다르게 의외로 힘들어하고 있다."
    "사요리와 모니카가 다른 곳을 본다."
    show natsuki zorder 3 at f22
    n 1i "흥."
    n "어쨌든…!"
    n 1q "아까 가슴에 대한 거. 진심이 아니었어, 알겠지?"
    n "그게 다야."
    "나츠키는 다른 사람들의 눈빛을 피하며 고개를 돌린다."
    show natsuki zorder 2 at t22
    show sayori 4x behind yuri at l41
    s "응응! 유리는 자연 미녀니까!!"
    mc "사요리?!"
    show yuri 4c zorder 3 at f21
    y "…."
    y "차, 차 끓여올게요…."
    show yuri at lhide
    hide yuri
    show sayori zorder 3 at f41
    s 4h "에에에?"
    s "난 그냥 도와주려고 했던 것뿐인데!"
    show sayori zorder 2 at t41
    mc "부끄러워서 고맙다고 말 못 하는 걸 거야."
    "나는 사요리의 어깨를 토닥토닥 두드렸다."
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show monika 4m zorder 2 at t11
    hide sayori
    hide natsuki
    m "그럼…."
    m 4b "모두 서로의 시는 읽어봤지?"
    m "가치 있는 시간이었으면 좋겠네!"
    m 5 "특히 [player]가 말야!"
    m "그리고 솔직히 말하자면…."
    m "평소 그냥 놀던 것보다는 훨씬 나은 것도 같고."
    m "아하하!"
    mc "아, 난 별로 그런 분위기를 깨려고 온 건…."
    m 1d "아냐, 그런 건 아냐, 그런 건 아냐!"
    m "아직 집 가기까진 시간이 좀 남으니까."
    m 1a "모두 좀 쉬었다 가자."
    m "물론, 수다 떠는 거 말고도 문학에 관한 일은 많으니까…."
    m "책을 읽는다던가, 글을 쓴다든가 하면서 시간을 보내면 돼."
    m 1b "애초에 그게 문예부가 하는 일이잖아!"
    show sayori 2j zorder 3 at f31
    s "난 다르게 생각해, 모니카!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f32
    m 1d "응? 어떤 걸?"
    show monika zorder 2 at t32
    show sayori zorder 3 at f31
    s 2i "그건 문예부에서 가장 중요한 게 아냐!"
    s "가장 중요한 건…."
    show sayori 4r zorder 3 at hf31
    s "즐기는 거지!"
    show sayori zorder 2 at t31
    show monika zorder 3 at f32
    m 2l "아하하, 그것도 그렇겠네…."
    m 2a "그래서 사요리가 부부장이 된 거기도 하고."
    show monika zorder 2 at t32
    show sayori zorder 3 at f31
    s 4q "에헤헤…."
    hide sayori
    hide monika
    with wipeleft
    "생각해보면 모니카의 말이 맞다."
    "문예부원이 되었다는 건 아마 아무것도 안 하면서 시간을 보낼 수는 없다는 거겠지."
    "따지고 보면…."
    "…그렇게 나쁘지만은 않았어."
    return

label ch1_end_yuri:
    $ ch1_choice = "yuri"
    stop music fadeout 1.0
    mc "나츠키."
    mc "내가 네 시를 좋아했다는 건 맞아."
    show natsuki zorder 3 at f22
    n 1e "봤지??"
    show natsuki 1g zorder 2 at t22
    play music t8
    mc "잠깐!"
    mc "그렇다고 상대방에게 못되게 굴어서도 안 돼!"
    mc "다른 사람과 의견이 다르다고 싸우는 건 옳지 않아."
    show natsuki zorder 3 at f22
    n 1m "그래서 싸움이 난 게 아니잖아!"
    n "유리가 내 시를 진지하게 받아들이지 않는 게 문제라고!"
    show natsuki zorder 2 at t22
    mc "음…."
    mc "알겠어."
    mc "유리."
    show yuri zorder 3 at f21
    y 2t "네?"
    show yuri zorder 2 at t21
    mc "진지하게 넌 글 쓰는데 재능이 있어."
    show yuri zorder 3 at f21
    y 2u "그, 그, 그런가요…."
    show yuri zorder 2 at t21
    mc "근데 있잖아."
    mc "문체가 복잡하건 간단하든 간에…."
    mc "글쓴이는 거기에 자기 감정을 담기 때문에 그건 다른 사람이 뭐라 할 수 없는 개인적인 게 되는 거야."
    mc "자기 본심을 담은 글을 귀엽다고 하니까 나츠키가 화가 날만도 하지."
    show yuri zorder 3 at f21
    y 2v "그… 그렇겠네요…."
    y "그… 그럴줄은…."
    show yuri zorder 2 at t21
    y 2w "죄송해요, 저…."
    show yuri at s21
    y "우우…."
    show natsuki zorder 2 at t11
    show yuri zorder 1 at thide
    hide yuri
    mc "근데 나츠키, 너도 말이 좀 심하잖아!"
    mc "유리도 유리 나름대로 칭찬한 거고…."
    mc "네가 마음에도 없는 말을 하니까 이렇게 일이 커진 거잖아."
    n 1e "지금 나랑 장난해?"
    n "내가 진심을 말했는지 아닌지 네가 어떻게 알아?!"
    n "애초에 시작한 건 {i}쟤{/i}야!"
    show natsuki zorder 2 at t22
    show monika 2i zorder 3 at f21
    m "나츠키, 그만하면 충분해."
    m "결국 화나서 둘 다 실수한 건 사실이잖아."
    m "유리가 사과했잖아. 너도 해야 한다고 생각하지 않아?"
    show monika zorder 2 at t21
    show natsuki zorder 3 at f22
    n 1x "…!"
    show natsuki zorder 2 at t22
    "나츠키는 주먹을 꽉 쥐었다."
    "결국 나츠키 편을 들어주는 사람은 아무도 없었다."
    "이렇게 되면 억울한 감정 때문에 화만 더 나겠지."
    "이러면 좀 미안해지는데…."
    show monika zorder 2 at t32
    show natsuki zorder 2 at t33
    show sayori 2h at l41
    s "에에… !"
    s "난 가끔 마음이 아플 땐…."
    s "걷는 게 머리를 비우는 데 도움이 되더라!"
    show sayori zorder 2 at t41
    mc "사요리, 그럴 필요까지는…."
    show natsuki zorder 3 at f33
    n 2q "아니?"
    n "할 거야."
    n 2w "지금 너희의 그 얼굴을 보는 것보다야 낫겠지."
    show natsuki zorder 1 at thide
    hide natsuki
    "뭐라고 말할 새도 없이, 나츠키는 책상 위에 있던 자신의 시를 움켜쥐고 뛰쳐나갔다."
    "나가면서 나츠키는 두 손으로 시를 구겨 쓰레기통에 던졌다."
    show sayori zorder 3 at f41
    s 1k "나츠키…."
    show sayori zorder 2 at t41
    show monika zorder 3 at f32
    m 1r "저럴 필요까진 없었는데…."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    hide sayori
    hide monika
    "고개를 들어보니 유리가 얼굴을 손에 묻고 고개를 떨구고 있었다."
    "나는 조심조심 다가가 옆자리에 앉았다."
    show yuri 4b zorder 2 at t11
    y "하아…."
    mc "괜찮아?"
    y "너무 부끄러워요…."
    y "왜 그렇게 행동했는지 모르겠어요."
    y "제가 싫으시죠…?"
    mc "아냐, 유리!"
    mc "이상한 사람 취급받고 화 안날 사람이 어디 있겠어?"
    mc "그게 평범한거야."
    mc "이상하게 생각한다던가 그러지 않아."
    y 2v "우우…."
    y "…알았어요, 믿을게요."
    y 2s "고마워요. [player] 씨는 정말 친절하시군요."
    y "당신이 이 동아리의 일원이 된다는 게 너무 기뻐요."
    mc "에, 뭐, 별거 아니니까."
    y 2v "그리고 한 가지 더요…."
    y "우우, 그러니까 나츠키 씨가 한 말 중에…."
    y 4c "그으…."
    y "저는 그런 부끄러운 짓 따위 하지 않으니까…."
    y "그러니까…."
    mc "…에?"
    mc "나츠키가 한 말 중에 뭐?"
    y 3n "……!"
    y "아아 그게!"
    y 3q "아니에요, 신경 쓰지 마세요…."
    y "저, 전 차라도 끓이러 갈게요…."
    mc "그래, 그럼."
    mc "좀 많이 끓여줄래? 다른 사람들도 다 같이 먹게"
    y "그, 그럴게요."
    return

label ch1_end_sayori:
    $ ch1_choice = "sayori"
    mc "나츠키…."
    show natsuki 5f
    "나츠키가 쏘아보니까 입안이 바싹바싹 마른다."
    "그래서 그 대신, 유리를 바라보았다."
    mc "유리…."
    y 4a "…."
    "근데 유리의 표정도 지금 무슨 말을 들을 수 있을 만한 표정이 아니다."
    stop music fadeout 1.0
    mc "…."
    mc "…사요리!"
    show sayori 4m behind yuri at l31
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    s "에?!"
    mc "…그래!"
    mc "너희가 싸우면 사요리가 불안해하잖아."
    mc "너희 친구의 기분을 안 좋게 만든다는 걸 알면서 계속 싸우는 거야?"
    show sayori zorder 3 at f31
    s 4d "[player]…."
    show sayori zorder 2 at t31
    show natsuki 4w zorder 3 at f33
    n "글쎄… 그건 걔 문제지! 그리고 이건 걔랑 연관 있는 것도 아니고."
    show natsuki zorder 2 at t33
    show yuri 2g zorder 3 at f32
    y "저, 저도 동감이에요…."
    y "저희 사이에 갈등을 남의 감정으로 막으려 하다니, 너무해요."
    show yuri zorder 2 at t32
    show natsuki zorder 3 at f33
    n 4c "맞아. 사요리가 유리는 얼마나 속 꼬인 멍청인지 말하고 싶었다면 얘기가 달라지지만."
    show natsuki zorder 2 at t33
    show yuri 3r zorder 3 at f32
    play music t7
    y "사요리 씨는 그런…!"
    y "애초에 사요리 씨의 기분을 망친 건 나츠키 씨의 부주의 때문이잖아요!"
    show yuri zorder 2 at t32
    show natsuki 1e zorder 3 at f33
    n "{i}뭐라고{/i}?"
    n "그게 네가 할 소리야?"
    n 1x "그러니까 사람들이…."
    n 1w "사람들이 널 안 좋아…."
    show natsuki zorder 2 at t33
    show sayori 4p at h31
    stop music
    s "{i}그만!!{/i}"
    show yuri 3f zorder 3 at f32
    show natsuki 1o zorder 3 at f33
    ny "……."
    show yuri zorder 2 at t32
    show natsuki zorder 2 at t33
    show sayori zorder 3 at f31
    play music t8
    s 1h "나츠키! 유리!"
    s "너희는 모두 내 친구야!"
    s 1v "난 모두 잘 어울리고 행복했으면 좋겠어!"
    s "내 친구들은 훌륭해…."
    s "그리고 각자 다 다르니까 더 좋아!"
    s 1g "나츠키의 시는…."
    s "몇몇 단어들로 많은 감정을 준다는 게 대단한 거 같아!"
    s "그리고 유리의 시는 읽으면 머릿속에 그림이 그려져서 대단한 거 같아!!"
    s 4k "모두 재능이 있는데…."
    s "…왜 싸우는 거야…?"
    show sayori zorder 2 at t31
    show natsuki zorder 3 at f33
    n 1r "왜… 왜냐하면…."
    show natsuki zorder 2 at t33
    show yuri 3v zorder 3 at f32
    y "글쎄요…."
    show yuri zorder 2 at t32
    show sayori zorder 3 at f31
    s 1j "그리고!"
    s "나츠키는 귀엽고 그게 잘못된 건 아니야!"
    s 1i "그리고 유리의 가슴은 예전 그대로야!"
    show sayori at hf31
    s 1j "크고 아름다워!!"
    show sayori 1i zorder 2 at t31
    show natsuki zorder 3 at f33
    n 1o "…."
    show natsuki zorder 2 at t33
    show yuri zorder 3 at f32
    y 3n "…."
    show yuri zorder 2 at t32
    mc "사요리…."
    "사요리는 의기양양하게 서 있다."
    "모니카는 당혹스러운 표정을 지으며 사요리의 뒤에 서 있다."
    show yuri at s32
    y 3q "저는… 차를 좀 타올게요…."
    show yuri behind sayori at lhide
    hide yuri
    "유리는 황급히 달려나갔다."
    show natsuki zorder 1 at thide
    hide natsuki
    "나츠키도 멍한 표정을 지은 채 자리에 앉는다."
    show sayori zorder 1 at thide
    show monika 1i zorder 2 at t11
    hide sayori
    mc "이래서 사요리가 부부장인 거구나…."
    "나는 모니카에게 속삭였다."
    "모니카는 끄덕인다."
    m 1d "솔직히…."
    m "부 활동 정하고 정리한다던가, 리더 역은 잘 할 수 있는데…."
    m 3e "사람 관계는 잘 못 하거든…."
    m "이런 일이 일어나면 내가 먼저 중재해야 하는데, 용기가 안 나."
    m 1m "부장으로서, 조금 부끄러운 거 있지."
    m 1l "아하하…."
    mc "아냐…."
    mc "내가 뭐라 할 처지도 아니고."
    mc "결국 나도 아무 말 못 했잖아."
    m "으응…."
    m 2a "그렇게 따지면 조금 독특하긴 해도 사요리도 대단한 면이 있어."
    mc "그렇다고 할 수 있지."
    mc "바보일지는 모르지만, 가끔 이상할 정도로 자기 역할을 잘 한다니까."
    m 5 "그렇구나~"
    m "사요리 잘 챙겨줘, 알았지?"
    m "걔가 다치는 걸 별로 보고 싶지 않으니까."
    mc "나도 마찬가지야…."
    mc "나한테 맡겨."
    "모니카는 나에게 달콤한 미소를 짓는데, 왜 난 창자가 꼬이는 느낌일까."
    "본인은 부족하다고 하지만, 모니카만 한 사람다운 부장이 또 있을까 싶다."
    "모니카랑 좀 더 대화할 기회만 있다면…."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
