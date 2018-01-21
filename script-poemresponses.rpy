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

label poemresponse_start:
    $ finalConso = finalChecker(player)
    $ poemsread = 0
    $ skip_transition = False
    label poemresponse_loop:
        $ skip_poem = False
        if renpy.music.get_playing() and not (renpy.music.get_playing() == audio.t5 or renpy.music.get_playing() == audio.t5c):
            $ renpy.music.play(audio.t5, fadeout=1.0, if_changed=True)
        if skip_transition:
            scene bg club_day
        else:
            scene bg club_day
            with wipeleft_scene
        $ skip_transition = False
        if not renpy.music.get_playing():
            play music t5
    label poemresponse_start2:
        $ skip_poem = False
        if persistent.playthrough == 2:
            $ pt = "2"
        else:
            $ pt = ""
        if poemsread == 0:
            $ menutext = "누구에게 시를 먼저 보여줄까?"
        else:
            $ menutext = "다음은 누구에게 시를 보여줄까?"

        menu:
            "[menutext]"

            "사요리" if not s_readpoem and persistent.playthrough == 0:
                $ s_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "아무래도 사요리에게 먼저 보여주는게 편하다."
                    "친한 친구니까말야."
                call poemresponse_sayori from _call_poemresponse_sayori
            "나츠키" if not n_readpoem:
                $ n_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "어제 나츠키가 쓴 시가 궁금하다고 하기도 했고."
                    "내 시를 먼저 보여주는게 공평하겠지?"
                call poemresponse_natsuki from _call_poemresponse_natsuki
            "유리" if not y_readpoem and not y_ranaway:
                $ y_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "유리가 글 쓴 경험이 가장 많은거 같으니까 유리에게 먼저 물어봐야겠어."
                    "유리 의견이라면 믿을 수 있을지도."
                call poemresponse_yuri from _call_poemresponse_yuri
            "모니카" if not m_readpoem:
                $ m_readpoem = True
                if chapter == 1 and poemsread == 0:
                    "모니카에게 먼저 보여주는게 낫겠다."
                    "어제 보니 내가 쓴 시는 어떤가 보고싶어 했기도 하고, 문예부에 관심이 있다는 것도 보여줄 겸 말야."
                call poemresponse_monika from _call_poemresponse_monika
        $ poemsread += 1
        if poemsread < 3 or (persistent.playthrough == 0 and poemsread < 4):
            jump poemresponse_loop


    $ s_readpoem = False
    $ n_readpoem = False
    $ y_readpoem = False
    $ m_readpoem = False
    $ poemsread = 0
    return

label poemresponse_sayori:
    scene bg club_day
    show sayori 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if s_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif s_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_s_" + poemopinion
    call expression nextscene from _call_expression
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_s_end"
        call expression nextscene from _call_expression_1
    return

label poemresponse_natsuki:
    scene bg club_day
    show natsuki 1c zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if n_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif n_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_n_" + poemopinion
    call expression nextscene from _call_expression_2
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_n_end"
        call expression nextscene from _call_expression_3
    return

label poemresponse_yuri:
    scene bg club_day
    show yuri 1a zorder 2 at t11
    with wipeleft_scene
    $ poemopinion = "med"
    if y_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif y_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_y_" + poemopinion
    call expression nextscene from _call_expression_4
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_y_end"
        call expression nextscene from _call_expression_5
    return

label poemresponse_monika:
    scene bg club_day
    show monika 1a zorder 2 at t11
    with wipeleft_scene
    if m_poemappeal[chapter - 1] < 0:
        $ poemopinion = "bad"
    elif m_poemappeal[chapter - 1] > 0:
        $ poemopinion = "good"
    $ nextscene = "ch" + pt + str(chapter) + "_m_start"
    call expression nextscene from _call_expression_6
    if not skip_poem:
        $ nextscene = "ch" + pt + str(chapter) + "_m_end"
        call expression nextscene from _call_expression_7
    return

label ch1_y_end:
    call showpoem (poem_y1, img="yuri 3t") from _call_showpoem
    y 3t "…."
    y "손… 손 글씨 많이 나쁜 거 죄송해요!"
    mc "뭐?"
    mc "그런 생각한 적 없는데…."
    y 2v "읽는데 오래 걸리셔서…."
    mc "아아."
    mc "그런거라면 그냥 글 읽는데 익숙하지 않아서 그런거니까…."
    mc "그리고 손 글씨 예쁜데 왜."
    y 2t "에?"
    y 2u "그거… 다행이네요…."
    mc "그리고, 나 이 시 맘에 들어."
    mc "짧긴 해도, 되게 묘사적이고 말야."
    y 2t "너무 짧지 않나요?"
    y "평소엔 이것보다 더 길게 쓰거든요…."
    mc "전혀."
    y 1m "마… 마음에 드신다니 기쁘네요."
    y "솔직히 말해서…."
    y 1a "시 나눠 보는 거는 처음이라 조금 가볍게 써 봤어요."
    y "이해하기 쉬울 만한, 그런거요."
    mc "유령같은 거 좋아해?"
    y 1m "후후."
    y "있죠, [player], 그 시 유령이랑은 전혀 상관 없어요."
    mc "진짜?"
    mc "완전히 헛다리 짚은 모양이네…."
    y 1u "애초에 잠깐밖에 보지 않으셨으니까요…."
    y "하지만 시인들은 보통 시에 본인들의 생각이나, 감정, 경험 등을 담는다는 걸 생각하셔야해요."
    y 1a "경수필을 쓴다거나 그림을 한장 그리는 것보다는 더 많은 일을 하죠."
    y "당장 이 시만 해도 주제가 유령으로 빗대어 쓰인거거든요."
    y 2l "본인이 가장 편한 곳에 남고, 과거를 그냥 보내주지 못하고."
    y "결국엔 아무것도 가지지 못하고 떠나게 되는…."
    mc "…그렇게 말하니까 더 무게가 있네."
    mc "난 그런 생각 전혀 못해봤어…."
    mc "정말 대단한데."
    if poemopinion == "good":
        y 2f "에?"
        y 3v "벼, 별거 아닌걸요!"
        y "[player] 씨의 시도 대단했으니까요…."
        mc "에이…."
        mc "나야 네게 한 두 가지 정도 얻어가는 걸…."
        y 4a "…그렇게 생각하세요?"
        mc "응, 물론이지."
        y "아…."
        y 2s "있죠…."
        y "시를 나누는거 처음엔 되게 긴장했었는데."
        y "해보니까 재밌네요."
        y "[player] 씨를 위해 최선을 다할테니까요…."
        mc "아…."
        mc "응, 나도."
    else:
        y 1u "별 거 아니에요…."
        y "그렇게 생각해주시다니… 다행이네요."
        y 1a "제 생각엔 [player] 씨도 금방 이런 것 쯤은 하실거에요."
        mc "응, 그럴지도 모르지."
        mc "계속 시도해야겠지."
        y "기대되네요."
    return

label ch2_y_end:
    call showpoem (poem_y2) from _call_showpoem_1
    y 2m "으음…."
    y "어제보다 더 대담하게 써 봤어요…."
    mc "그런 것 같네."
    mc "확실히 더 은유적이고 말야…."
    "내 문제인지는 모르겠는데 무슨 내용인지 하나도 모르겠다."
    y 1a "맞아요."
    y "제가 쓰기 좋아하는 문체에 더 가깝거든요…."
    y "시를 캔버스 삼아 심상을 그려내고, 거기에 감정을 드러내는 거예요."
    mc "응, 그냥 겉만 봐서는 무슨 뜻인지 전혀 모르겠는걸…."
    y 2f "네…."
    y "제 생각에는 사람들마다 다르게 관련지을 수 있을 것 같아요."
    y "전 제 이상한 취미에 대해 느끼는 감정을 표현하고 싶었어요…."
    y 2v "남들에겐 말할 수 없는 그런 취미요."
    y "그래서 가끔 그거에 관한 시를 쓰곤 해요."
    if n_readpoem and (n_poemappeal[0] >= 0 or n_poemappeal[1] >= 0):
        mc "하, 그거 되게 웃긴다…."
        y 2e "…?"
        mc "나츠키도 같은 주제로 시를 쓰지 않았어?"
        mc "이상한 취향에 관해 말이야."
        y 2h "에?"
        y "나, 나츠키 씨가요?"
        mc "응…."
        mc "남을 다치게만 하지 않는다면 무슨 상관이냐는 식으로 말했거든."
        y 3r "마, 맞는 말씀이네요!"
        y 3o "제, 제말은…."
        y "정말로 그렇게 생각하신대요…?"
        mc "응."
        mc "둘 다 공통점이 있는 것 같네…."
        y 3h "그건… 글쎄요, 좀 흥미롭네요…."
        y "저한테는, 나츠키 씨는 제 취미를 비웃는 사람으로만 보였는데…."
        y "그건 그냥 제가 제멋대로 판단한 거겠죠…?"
        y 3p "아… 나츠키 씨한테 제가 이런 말 했다는 거 말하지 말아주세요!"
        mc "아하하. 걱정하지 마, 얘기 안 할 거니까."
        y 1l "네…."
        y 1a "말씀해주셔서 감사해요."
    else:
        mc "근데 왜 비밀로 하는거야?"
        y 3v "왜… 왜냐하면…."
        y "부끄러우니까요…."
        y "다들 비웃을걸요."
        y "[player] 씨는 그런 거 없으세요?"
        mc "글쎄…."
        mc "응, 있을지도 모르겠네…."
        y 2h "다들 그런거 한 가지 쯤은 있을거라 생각해요."
        y "그럼 최선의 방법은 서로의 다름을 존중해 주는 것이지요."
        y "그게 어떨 땐 어렵고, 불편할 때가 있을지라도요…."
    y 1a "애초에, 저도 제 이상한 점을 인정하지 않았더라면 저 자신이 엄청 싫었을 거예요."
    y 2u "너, 너무 쓸데 없는 말만 하는건 아닌지 모르겠네요…."
    y "…그래도 잘 들어주셔서 감사해요."
    if y_appeal >= 2:
        y 2s "잘 하시는게 정말 많네요…."
        y "글쓰기도 그렇고, 경청해주시는 것도 그렇고…."
        y 2u "세상에 [player] 씨 만한 사람 많지 않아요…."
        mc "그, 그건 좀 과장이 아닐까…."
        y 2v "전… 그렇게 생각해요."
        y "제 글을 이렇게 편안하게 나눌 수 있을지 몰랐어요…."
        y 2s "이젠, 기대가 될 정도니까 말이에요…."
        y 2m "정말… 좋은 것 같아요."
        y "다 [player] 씨 덕분이니까요."
        mc "별… 별거 아냐…."
        "유리가 진심이 담긴 미소를 보내온다…."
        "잠깐이지만, 유리 특유의 소심함이 사라졌다."
    return
label ch3_y_end:
    if y_appeal >= 3:
        jump ch3_y_end_special
    call showpoem (poem_y3, img="yuri 2v") from _call_showpoem_2
    y "음…."
    y "해변이 좀 어리석은 주제라는건 알고 있지만…."
    y "은유적으로 접근해봤어요."
    if not n_readpoem or n_appeal >= 3:
        mc "꼭 쓰기 싫었다는 것 처럼 말하네…."
        y 2e "아, 못 들으셨어요…?"
        y 2h "어제, 저랑 나츠키씨는… 어…."
        y "같은… 주제로 전혀 다른 시를 쓸 수 있다는게 놀랍다고 생각했거든요."
        y "그래서 나츠키 씨가 또 같은 주제로 시를 써 보는게 어떻겠냐고 제안하셔서…."
        if n_readpoem:
            mc "그랬구나…."
            "나츠키가 내게 보여준 시는 다른 사람들에게는 보여주지 않을 것 같은 기분이 든다…."
            "물론 유리에게는 말하지 않기로 했다."
    else:
        mc "응, 나츠키한테 들었어."
        y 3t "나츠키 씨가 말씀하셨나요…?"
        y "괜시리 이상한 말도 덧붙이시지는 않으셨나요?"
        y "그냥 같은 주제로 쓰는게 어떻겠냐고 제안하셔서…."
    y 2f "저희가 쓰는 방식이 어떻게 다른지… 생각하는 방식은 어떻게 다른지 비교할 수 있는 좋은 기회라고 생각해서요."
    y 2w "어쨌든, 제안한건 나츠키 씨에요…!"
    y "나츠키 씨라면 별로 놀랍지도 않지만요."
    y "그냥 잘났다고 자랑하고 싶으신 거겠죠."
    y 2v "제가 나츠키 씨의 문체에 관심이 있는것도 아니고…."
    y "그냥 제안하시니까 전…."
    y "그치만…."
    y 1s "간단한 주제로 글을 쓰는 것도 나쁘지 않을 것 같아요."
    y 1m "마음을 새롭게 하는 그런 시간이 되니까요."
    y "가끔은 이렇게 생각을 정리하는것도 좋을 것 같아요."
    mc "응… 그럴 것 같네."
    mc "얘기해 줘서 고마워."
    return
label ch3_y_end_special:
    call showpoem (poem_y3b, img="yuri 4b") from _call_showpoem_3
    "시를 다 읽고, 유리에게 돌려준다."
    "그런데 유리는 시를 받지 않고, 그냥 다른 곳을 보기만 한다."
    y "…."
    y "별로… 마음에 안 드시나요."
    mc "아, 아냐. 그런 건 아닌데."
    mc "그냥… 어떻게 반응을 해야할지 몰라."
    "유리의 시들은 대부분 수수께끼 같음에도 불구하고, 이번 건 무엇에 대한 시인지 알아내는 것이 그렇게 어렵지는 않았다."
    if n_readpoem:
        "그리고 나츠키가 쓴 시랑은 완전 딴판인데…."
        "…그럼 유리가 나한테만 다른 시를 보여줬다는 뜻이겠지."
    y 2v "제가 설명할 수 있을지 모르겠네요…."
    mc "괜찮아."
    mc "이해했으니까."
    y 4c "…."
    "유리는 평소보다 더 말하기 힘들어하는 듯했다."
    mc "이 시가 너한테 큰 의미가 있어?"
    "유리는 끄덕였다."
    mc "뭐라고 말을 해야할지 모르겠지만…."
    mc "네가 시를 나와 공유해줘서 기뻐."
    mc "그래서… 고마워."
    mc "계속 이런 식으로 같이 시간을 보낼 수 있었으면 좋겠다."
    show yuri 4e
    "나는 말할 때 눈을 마주치지도 못했지만, 유리의 입가에 희미한 미소가 지어졌다는 것만큼은 알 수 있었다."
    "나는 유리에게 시를 돌려주었다."
    show yuri 4a
    "하지만, 유리는 부드럽게 내 손을 잡고 시를 나에게 돌려준다."
    "난 유리의 따뜻한 손길에 어떻게 반응해야할지 주저하고 있다."
    y 1v "그 시…."
    y "어…."
    y "그 시, 그냥…."
    "다시 한번, 유리는 끝까지 말을 잇지 못한다."
    mc "내가 가져도 된다고?"
    "유리는 끄덕였다."
    mc "좋아."
    show yuri 1u
    "또 한번, 유리는 미소지었다."
    y "당신은 항상…."
    y "당신은 항상… 절 기쁘게 해주시는군요."
    y "제가 사람들과 잘 어울리지 못한다는 건 알지만…."
    y "언젠가는… 제가 그 은혜를 갚을 수 있었으면 좋겠네요."
    mc "응."
    mc "걱정하지 마."
    mc "너는 잘하고 있어."
    "그제야 다시 유리가 날 바라본다."
    y 1s "모니카 씨가 뭐라고 하기 전에 마저 해요."
    y "얘기는 나중에 해도 되니까요…."
    mc "응."
    mc "그러자."
    "그러고, 유리는 소심하게 내게 미소를 짓는다. 나는 내 자리로 돌아가 유리가 준 시를 가방에 넣는다."
    return

label ch1_n_end:
    call showpoem (poem_n1, img="natsuki 2s") from _call_showpoem_4
    n 2q "뭐…."
    n "안 좋아할 거라고 했지."
    mc "괜찮은데 왜."
    n 2h "뭐?"
    n "그냥 솔직히 말해!"
    mc "솔직하게 말한 거야."
    mc "왜 내가 안 좋아할 거라고 확신하는 거야?"
    n 5w "으응…."
    n "왜냐하면!"
    n "고등학교에 있는 사람들은 다 글을 복잡하게 써야 한다고 생각하니까…."
    n 5q "다들 내 글은 별로 진지하게 받아들이지 않더라고."
    mc "그럼 자기감정을 표현하는 시를 쓰는 의미가 없지 않아?"
    mc "글 쓰는 스타일이 다르다고 전하는 의미가 약해지는 것도 아니고."
    n 1k "맞아! 내 말이!"
    n "읽기는 쉬운데 의미깊은 시가 난 좋아."
    n 1c "이 시처럼 말야."
    n "주변 사람들이 다 잘하는 게 한 가지씩 있으면 마음에 상처가 될 수 있잖아…."
    n "그걸 주제로 이 시를 쓰기로 했어."
    mc "응, 이해해."
    n 2a "그리고 간단명료하게 쓰는 글이 좋은 점은 단어 선택으로 많은 의미를 부여할 수 있다는 거야."
    n "이 시의 끝음절들을 볼 때 다 똑같은데 마지막 줄 하나만 다르잖아."
    n "그게 마지막 줄에 감정을 끌어내는데 도움을 주거든."
    mc "그랬군…."
    mc "내가 못 알아봤지, 신경 쓴 점이 엄청 많네."
    n 4y "프로라면 이 정도는 해야지!"
    n "뭔가 배울 점이 있었다니 다행이네."
    n "가장 어린 사람한테서 이런 시가 나올 줄 몰랐지?"
    mc "으응… 그렇네."
    "정말로 예상 못 했다는 듯 놀리기로 했다."
    "어차피 다 같은 학년이라 나이 차는 몇 달 안 날 텐데, 그렇게 생각한다면야 부정하지는 않는 쪽이 좋겠지."
    return

label ch2_n_end:
    call showpoem (poem_n2) from _call_showpoem_5
    n 2a "나쁘지 않지?"
    mc "어제 것보다는 기네."
    n 2w "어제 건 너무 짧았어…."
    n "그리고 어제는 손 푸는 정도였으니까 말야!"
    n 2c "내 최선이 겨우 그정도라고 생각한 건 아니지?"
    mc "아니, 물론 아니지…."
    n 2a "뭐, 이 시가 말하고자 하는 바는 충분히 간결하다고 생각하니까."
    n "설명 해줄 필요는 없겠지."
    n 2c "가끔은 간단한 비유가 복잡한 문제를 설명할 수 있어…."
    n "그리고 사람이 얼마나 멍청한지를 알게도 해주고."
    n 2g "당장 이 시의 주인공만 봐도 얼마나 무식한 놈이야…."
    mc "그런 사람이 주변에 있는 거야?"
    n 2c "물론이지. 사람들이 내 시를…."
    n 5w "…그게 중요한게 아니잖아! 그건 누구든 될 수 있단 말야!"
    n 5h "내가 이걸 쓴 이유는 본인과 연관 짓기 쉽기 때문이야…."
    n "모두들 이상한 취미나 하면 안된다는 걸 알면서도 하는 그런 일들이 있잖아."
    n 5q "다른 사람들이 알면 비웃거나 깔볼 것 같아서 알리기 싫은, 그런 것들 말야."
    n 1e "…근데 그건 멍청한 사람들이나 하는 짓이야!"
    n "누가 뭘 좋아하든 자기들이 무슨 상관이야? 그게 남들을 다치게 하는 것도 아니면서 본인을 행복하게 해 준다면?"
    n 1q "다들 남들의 취향을 존중하는 자세가 필요해…."
    if y_readpoem and (y_poemappeal[0] >= 0 or y_poemappeal[1] >= 0):
        mc "흠, 그거 재밌네…."
        mc "유리도 오늘 비슷한 주제로 시를 썼거든."
        n 1h "응?"
        n "방금 유리라고 그랬어?"
        mc "응…."
        mc "자기가 가진 평범하지 않은 취미에 대해서 썼다고 했거든."
        mc "이해하기는 좀 힘들었지만, 비슷한 얘기였으니까…."
        mc "서로의 자존감을 떨어뜨리면 안된다는 식으로 말야."
        n 1q "진짜?"
        n "으응…."
        n 1t "으응, 내가 보기에도 유리는 꽤나 이상한 사람이긴 해서, 이상한 취미를 가지고 있다 해도 무리는 아니지만…."
        n "…그게 문제가 될건 아무것도 없잖아!"
        n 1u "으으…."
        n "내가… 막 판단하려는건 아니지만…."
        "나츠키는 단어 선택에 애를 먹고 있다."
        n 1q "너무 심한 말은 하지 말아야겠지…."
        n "본인 행동이 본인도 자신이 없다고 느낀다면…."
        n "있지, 난 사람들이 날 기죽일 때가 너무 싫더라…."
        n 1w "당장 어제만 해도 유리가 그랬잖아!"
        n 1s "근데 네가 말하는걸 들어보니까 유리도 반성하고 있는 것 같고…."
        mc "뭐, 나도 그렇게 생각해…."
        mc "문체가 서로 다를진 몰라도 분명 네 시에 담긴 의미엔 공감이 됐을거야."
    else:
        mc "뭐, 네 말이 맞는 것 같네."
        mc "나도 어느정도 그렇게 느꼈으니까."
        mc "다른 사람도 그렇게 느꼈을거고."
    if n_appeal >= 2:
        n 4h "있지…."
        n "내 문체를 존중해줘서 고마워…."
        n 4q "나도 어제 내가 이런 얘기 벌써 했다는건 알지만…."
        n "내 글을 너랑 나누는게 즐거우니까…."
        n 4w "…그러니까 행운인줄 알아."
        mc "아하하."
        mc "뭐, 솔직하게 얘기해줘서 고마워."
        n 1n "너 그거 무슨 의미야?"
        n "내가 솔직하지 않은적이 있었어?!"
        n 12b "어휴…."
        n "너도 내일 기대나 하셔, 알았지?"
        mc "응, 그럴게."
    else:
        n 4c "그게 내가 제일 자신있어 하는 일이기도 하고!"
        n "난 좋은 메시지가 떠오르지 않으면 글을 잘 안 쓰는 편이야."
        n "감정을 전달하는 게 중요하듯이…."
        n "하지만 난 느끼기만하는 것이 아니라, 생각하도록 하고 싶어."
        n 4b "그걸 기억해둬!"
        n "내일도 좋은 걸 써올 거니까. 기대하도록 해."
    return
label ch3_n_end:
    if n_appeal >= 3:
        jump ch3_n_end_special
    call showpoem (poem_n3) from _call_showpoem_6
    n 2a "그래…."
    n "계속 부정적인 것만 쓰고 있는 느낌이 들어서, 한번쯤은 긍정적인 글을 써보고 싶었어."
    n 2z "그리고… 해변은 좋잖아!"
    n 2j "해변에 대해서 부정적인 것을 쓴다니, 상상이 안 가지."
    if not y_readpoem or y_appeal >= 3:
        mc "해변이라는 주제를 먼저 정하고, 그 다음부터 쓰기 시작한 거야?"
        n 2c "뭐, 그렇지…."
        n "어제 있었던 일 때문이야."
        n 5q "유리랑 내가 서로 비슷한 글을 쓴다는 걸 알고…."
        n "걔가 같은 주제를 정하고 시를 써보자고 해서."
        if y_readpoem:
            mc "그렇구나…."
            "왠지 유리가 나에게 보여준 시는 다른 사람에게 보여준 시랑 다른 거였다는 느낌이 든다…."
            "물론, 나츠키에겐 비밀로 해야겠지."
    else:
        mc "뭐, 유리는 좀 더 엄숙하게 생각하던데."
        n 5h "뭐, 그야…."
        n 42c "어휴… 내 시에 대해 이상하게 말하지 않았어야 할텐데!"
        n "애초에, 같은 주제로 시를 쓰자고 한건 걔였으니까."
    n 1s "으윽, 뻔한 수에 걸려들다니."
    n "주제는 쉬운걸로 골라놓고, 일부러 멋지고 어렵게 써서 날 누르려는 속셈인거겠지."
    n 1w "뭐, 상관 없어."
    n "나도 그냥 한 거니까."
    n 1q "뭐, 내 것도좀 더 은유적으로 쓰이긴 했지만…."
    n "…가끔은 이런것도 나쁘지 않으니까!"
    n "적어도, 좋은 연습은 됐어."
    return
label ch3_n_end_special:
    call showpoem (poem_n3b) from _call_showpoem_7
    n 1q "…."
    n "…뭘 그렇게 쳐다봐?"
    n "마음에 안 들면 그냥 그렇다고 해."
    n 1u "화… 안 낼테니까."
    mc "아냐, 마음에 안 든다는 게 아니라…!"
    mc "그냥… 읽는데 좀 놀랐어."
    if y_readpoem:
        "유리가 보여준 거랑은 완전 다르다…."
        "…그럼 나츠키가 나한테만 다른 시를 보여줬다는 뜻이겠지."
    mc "어… 너한테서 이런 얘기를 들을줄은 몰랐는걸…."
    n 1h "그, 그런 말 하지마!"
    n 1n "바보야…."
    n "글쓰기의 요점이 뭐라고 생각해?"
    n 1u "말로는 못하는 말들을 표현하는거야…."
    mc "그래… 이해해."
    mc "가끔 그런 점들을 놓칠 때가 있어."
    mc "다 좋은 뜻에서 그러는건데…."
    mc "그리고… 이걸 보여줘서 고마워."
    mc "좋았어."
    n 1h "으… 으응…."
    n 1q "난… 난 프로니까…."
    "평소 자신감이 넘치던 목소리와는 다르게 말을 머뭇거린다."
    n "그냥…."
    n 12c "나도 가끔은 이럴 수 있다는걸 알아둬!"
    n "그렇게, 자상하게 대해주면… 그건…."
    n 12a "…."
    n "…꽤나 큰 의미니까."
    mc "아."
    "뭐, 나츠키가 만족했다니, 시를 돌려줘야겠지"
    "근데 시를 돌려주자 나츠키가 내 손을 잡고 다시 내 쪽으로 민다."
    "작고 부드러운 손에 난 놀란다…."
    n 12b "싫어."
    mc "에…?"
    mc "왜?"
    n 12c "싫으면 싫은거야!"
    n "어휴…."
    "그제서야 나츠키의 행동이 무엇인지 알았다."
    "솔직하게는 못하고, 나츠키는 지금 나에게 시를 주려는거다."
    mc "뭐… 그렇다면야, 내가 가질게."
    "이번에는 놀리지 않고 받아주기로 했다…."
    n 1t "…그래."
    n "만약 안그랬으면, 난 아마도…."
    n "…."
    n 1h "아냐…."
    n 1q "그냥… 네가 원한다니까."
    "나츠키가 무슨 말을 하려고 했는지는 몰라도, 말하지 않기로 한 것 같다."
    "표정을 숨기려는 노력과는 반대로, 작게나마 미소짓는것이 보인다."
    n "어쨌든, 그게 다니까…."
    n 1s "다른 사람들이 보기 전에 빨리 넣어, 알았지?"
    mc "아… 그래."
    mc "그럴게."
    "그 말을 끝으로, 난 내 자리로 돌아가 나츠키의 시를 가방에 넣었다."
    return

label ch1_s_end:
    call showpoem (poem_s1) from _call_showpoem_8
    mc "사요리…."
    mc "그냥 물어보는 건데…."
    mc "너 설마 오늘 아침에 이거 쓴 거야?"
    s 4h "아니야!"
    s 4l "아, 아주 약간만 썼어!"
    mc "’아주 약간’이라는 것도 뭐가 잘못된 거 아니냐…."
    s 5b "어젯밤에 하는 걸 까먹어서…."
    mc "뭐,덕분에 내 자신이 좀 괜찮은 사람이라는 걸 느꼈어…."
    s 1h "못됐어!"
    s "그래도 열심히 썼단 말이야…."
    mc "아, 응…."
    mc "나쁜 시라는 뜻은 아니였어."
    mc "좋은 시인데, 뭐라고 말을 해야되지…."
    mc "꼭 너처럼 들리네."
    s 1d "진짜?"
    mc "응."
    mc "특히 마지막 줄이…."
    s 4r "계란이랑 토스트를 만들어 먹었어!"
    mc "학교에 늦는 데도?"
    s 5d "아침을 거르는 건 좋지 않으니까!"
    s "아침을 못먹으면 짜증나고…."
    mc "뭐, 거기에 태클 걸 필요는 없겠지…."
    mc "어쨌거나, 보여줘서 고마워."
    s 1q "에헤헤~"
    s "이거 진짜 재밌다."
    s "모니카는 최고야!"
    mc "아… 응."
    s "다음엔 까먹지 않을 거야."
    s 4x "그리고 최고의 시를 쓰겠어!"
    mc "응, 기대하고 있을게."
    return

label ch2_s_end:
    call showpoem (poem_s2) from _call_showpoem_9
    mc "와, 뭐야…."
    mc "사요리, 이거 진짜 네가 쓴 거야?"
    s 2j "당연히 내가 썼지!"
    s "내가 어제 너한테 최고의 시를 쓸 거라고 말했잖아?"
    mc "맞아, 그런데…."
    mc "…이런 시가 너한테서 나올 줄은 몰랐네."
    s 4x "모니카가 많이 가르쳐줬어!"
    s "그리고 요즘 되게 감성적이게 되버려서 말야…."
    mc "그렇구나…."
    mc "뭔가 조금 소름끼치네."
    s 1b "소름끼쳐…?"
    mc "으응 그러니까…."
    mc "평소에 되게 발랄한 모습만 보다가…."
    mc "…아냐, 신경쓰지마."
    mc "괜한 생각인 것 같아."
    mc "내 말은, 잘 했으니까 자랑스러워해도 된다고."
    s 1y "고마워어~"
    s "마치…."
    s "원래부터 이렇게 날 표현했어야 했다는 생각이 들어."
    s "내 감정이 조금 더 이해가 잘 되는것 같기도 하고 말야…."
    s 1a "작문은 마법같아!"
    mc "꽤나 열정적인데?"
    mc "보기 좋다."
    s 4r "응응!"
    s "작문은 최고야!"
    s "죽을 때까지 시만 써야겠어!"
    mc "아하하… 너무 앞서가지는 말고."
    "사요리는 항상 뭔가에 미친듯이 열중하다가 1주일도 안되서 질려하는 경향이 있다."
    "과연 이번에도 그럴까?"
    "하지만 사요리의 눈의 열정을 보니 그런 걱정은 안 해도 될 것 같다."
    return
label ch3_s_end:
    return

label ch1_m_end:
    call showpoem (poem_m1) from _call_showpoem_10
label ch1_m_end2:
    m 1a "…어떤 것 같아?"
    mc "으음… 이건 자유시네… 맞나?"
    mc "미안, 나는 피드백을 주기엔 아직 초보자라…."
    m 2e "후후, 괜찮아."
    m 2b "요즘 그런 시가 되게 유행이거든."
    m "단어와 줄 사이에 간격을 줘서 원하는 부분을 강조하는 것 말야."
    m 2a "또 낭송하면 그 효과는 배가 돼."
    mc "이건 무슨 영감을 받아 쓴 거야?"
    m "아…."
    m 3d "음, 뭐라고 해야 할지 잘 모르겠네…."
    m 3a "요즘 뭔가 깨달은 게 있거든."
    m "그래서 내 시도 그런 영향을 좀 받았어."
    mc "깨달은 게 있다고?"
    m 1a "응… 뭐라고 말할지 잘 모르겠네."
    m "조금 복잡한 문제라 아직 얘기해야 할지 잘 모르겠어. 꽤나 강렬한 경험이었거든…."
    m "다들 더 친해지고 나면 말할까 싶어."
    m 1j "어쨌든…."
    m 3b "오늘의 모니카의 작문 팁!"
    m "가끔 시를 쓰거나, 이야기를 만들 때 어느 구간에서 막힐 때가 있을거야."
    m "너무 완벽하게 쓰려고 한다면, 진전을 보이기 힘들어."
    m "그냥 쓰이는 대로 쓰고, 나중에 정리해봐!"
    m "다르게 얘기하면 이렇게 얘기할 수 있겠지."
    m "같은 곳에 펜을 오래 두고 있으면, 그냥 큰 잉크 웅덩이만 생길 뿐이야."
    m "그러니까 손을 움직여서, 그냥 흐름에 맡겨!"
    m 3k "…이게 오늘 내 조언이야!"
    m "들어줘서 고마워~"
    return

label ch2_m_end:
    call showpoem (poem_m2) from _call_showpoem_11
    mc "흐음…."
    mc "저번보다 더 추상적이네?"
    m 5 "아하하…."
    m "내 문체가 그런가 봐…."
    m "마음에 안 든다면, 미안해."
    mc "아니야, 절대 그런 뜻이 아니야."
    mc "그냥, 이런 거는 본 적이 없어서."
    m 2a "난 종이의 공간을 갖고 노는 걸 좋아하거든…."
    m "단어를 어디에 어떻게 놓을지 고르는 건 시의 분위기를 완전히 바꿀 수도 있어."
    m 2b "거의 마법 같다고 할 수 있지."
    m "내가 각 행들을 짧게 쓴 것도 소음 속에서 소리치는듯한 느낌을 주기 위해서야."
    mc "그렇구나…."
    mc "그치만 그래도 시의 의미는 아직 잘 모르겠어…."
    m 2k "아하하."
    m 4a "시에 꼭 무슨 의미가 담겼다고 생각하지 않는 편이 좋아."
    m "그냥 감정이나 표정을 묘사하고 있을 수도 있는 거니까."
    m "독자와 얘기를 하려고 한다거나."
    m "그렇게 생각하면, 모든 시가 뭔가에 {i}관해{/i} 쓰인 것 만은 아니야."
    m "어쨌든…."
    m 3b "오늘의 모니카의 작문 팁!"
    m "가끔씩 힘든 결정을 내려야 할 때가 있을 거야…."
    m "그럴 때는, 꼭 게임을 저장하는 걸 잊지 마!"
    m "언제 또 네 마음이 바뀔지 모르고…."
    m "…예기치 못한 일이 일어날 수도 있으니까!"
    m 3d "잠시만… 이게 작문에 관한 팁인가…?"
    m 3k "내가 지금 무슨 말을 하고 있는 거지?"
    m "아하하!"
    m 3b "…이게 오늘 내 조언이야."
    m "들어줘서 고마워~"
    return
label ch3_m_end:
    call showpoem (poem_m3) from _call_showpoem_12
    m 1a "있지…."
    m "사람들은 답을 찾는 데에서 삶의 의미를 찾는게 아닌가 싶어."
    m 1e "철학 얘기를 하려는 건 아니지만…."
    m 1a "왠지 그런 생각이 자주 들어서, 그거에 대한 시를 쓴 거야."
    mc "그렇구나…."
    mc "그런 생각은 잘 못 해봤어."
    m 1d "어떻게 보면 모순이지."
    m "만약 우리가 모든 것에 대한 답을 알았다면, 이 세상은 의미를 잃어버리지 않을까?"
    mc "있지, 그러고보니까…."
    mc "동아리 부원들은 행복한 것보다는 슬픈 주제를 위주로 글을 쓰는 것 같아."
    m 1k "아하하. 놀랬어?"
    m 1a "만약 모든 게 괜찮았다고 생각하면…."
    m "그 때는 글 쓸 주제마저 없지 않았을까?"
    m "사람은 이차원 생물이랑은 거리가 멀어."
    m "누구보다 네가 더 잘 알 거라고 생각했는데."
    mc "일차원을 얘기하는거야…?"
    m 1l "아… 응 그거!"
    m 1a "어쨌든…."
    m 3b "오늘의 모니카의 작문 팁!"
    m "혹시 네가 쓴 글이 별로일까봐 남들과 공유하는데 두려웠던 적이 있니?"
    m "되게 열심히 썼는데, 돌아오는 반응이 그저 그러면 낙심하게 되지."
    m "하지만 글쓰기를 좋아하는 또 다른 사람을 찾으면, 공유하는 게 되게 쉬워질 거야!"
    m "왜냐면 네 글이 좋다, 괜찮다, 나쁘다고 평가를 하는 것 대신에…."
    m "네가 글 쓰던 과정을 이해해주고, 얼마나 노력했을지를 알아주거든."
    m "그렇게 하는 쪽이 훨씬 용기도 북돋아 주고, 네가 성장하는 데도 도움이 될거야."
    m "마치 너만의 작은 문예부를 갖는다는 기분이 들지않니?"
    m 3k "…이게 오늘 내 조언이야!"
    m "들어줘서 고마워~"
    return


label ch1_n_bad:
    n "…."
    mc "…?"
    if persistent.playthrough == 2 and renpy.random.randint(0, 2) == 0:
        $ currentpos = get_pos()
        stop music
        pause 2.0
        play sound "sfx/stab.ogg"
        show n_blackeyes zorder 3 at i11
        show n_eye zorder 3:
            subpixel True
            pos (660,250) xanchor 0.5 yanchor 0.5 zoom 0.8
            parallel:
                linear 2.0 rotate 720
            parallel:
                linear 2.0 xpos 1680
            parallel:
                easein 0.25 ypos 180
                easeout 1.0 ypos 1280
        show n_eye as n_eye2 zorder 3:
            subpixel True
            pos (580,260) xanchor 0.5 yanchor 0.5 zoom 0.8 rotate 180
            parallel:
                linear 2.0 rotate -560
            parallel:
                linear 2.0 xpos -440
            parallel:
                easein 0.10 ypos 240
                easeout 1.0 ypos 1280
        show blood zorder 3:
            pos (645,255)
        show blood as blood2 zorder 3:
            pos (575,260)
        pause 0.75
        hide n_blackeyes
        hide n_eye
        hide n_eye2
        hide blood
        hide blood2
        stop sound
        play music "<from " + str(currentpos) + " loop 4.444>bgm/5.ogg"
    n 2b "[player], 진지하게 임하지 않을꺼면, 그냥 집에 가."
    mc "무, 뭐??"
    mc "너무한 거 아냐…?"
    n 42c "뭐, 그 정도도 노력을 안해놓고 내가 그냥 넘어갈 거라고 생각한 거야?"
    n "내가 멍청이로 보여?"
    mc "나는 작가가 아니야!"
    mc "별로일 수도 있지만, 그래도 나름대로 노력했다고."
    mc "다들 처음부터 잘하는 건 아니잖아?"
    mc "만약 네가 처음 쓴 시가 {i}네가{/i} 보기에 아직도 자랑스럽다면, 꼭 한 번 읽게 해줘."
    n 1o "!!"
    mc "생각만 해도 고통스럽지?"
    n 1r "…."
    n 5q "그래."
    n "뭐, …미안해"
    n 5c "나아지겠지."
    n "고칠 점이 뭐라고 말해주고 싶지만, 그냥 계속하다 보면 나아질 거야."
    mc "알았어…."
    mc "뭐, 각자가 잘 해야 하는 거니까."
    n 5q "어쨌든, 내 시를 보여줄 차례네…."
    n "어차피 너라면 멍청하다고 생각하겠지만."
    return

label ch1_n_med:
    n "…."
    mc "…?"
    n 2k "…뭐, 딱 너 같은 애가 쓸 만한 시네."
    mc "그건 좀 너무한데…."
    n 2c "글쎄, 저기요."
    n "나쁘다는 얘기는 아니였어."
    n "시에서 어떤 감정도 느껴지지 않잖아."
    mc "그러니까, 네 귀여운 입맛에 별로 안 맞는다는 거야?"
    n 4f "맞고 싶다는 거야?"
    mc "아, 아니요…."
    n 42b "하아…."
    n 42c "뭐 어쨌든, 내 거를 보여줘야겠네."
    n 4q "네가 좋아할 만한 건 아니야."
    return

label ch1_n_good:
    n "…."
    mc "…?"
    n 1t "…좋아, 일단 내가 마음에 안 들었던 것부터 얘기해주지!"
    n "일단, …으음."
    mc "…."
    "나츠키는 내 시를 다시 읽어봤다."
    n 4c "돼, 됐어. 내 의견 따위 들려줄 기분 아니니까."
    mc "에? 그럼 애초에 시를 나누는 의미가 없잖아."
    mc "할 일 많은데도 열심히 써온 건데."
    n 4r "으으…."
    mc "그리고, 내가 네 시를 읽고 싶다 한 거 기억나?"
    mc "이 시를 쓸 때 그 생각을 하고 쓴 거야."
    mc "네가 네 시를 보여주기 편하도록 도우려고 하는 거잖아."
    mc "모니카가 말한 것처럼 말야."
    n 4x "으으으으…!"
    n 1h "네가 시를 못 써야 편한 거고!"
    n 1w "원래는 네가 이상한 시를 써 들고 와서 보여주면 난 ‘하, 그렇게 잘 쓰진 않았네, 내가 진짜 문학이 뭔지 몸소 보여주지!’ 라고 말해야 했던 거란 말이야!"
    n 1h "그리고 네가 다 망쳤잖아!"
    n "그래서 행복하냐?"
    mc "…."
    mc "…다른 말로 맘에 들었다는거야?"
    n 1o "으윽"
    "나츠키가 더 이상 반박하지 못한다…."
    n 1x "으으으으으으… 너…!"
    n "너, 너 아무것도 이해 못 하는구나?"
    n 5q "이미 말한걸 ‘나 잘났다’ 라며 이리저리 광고하고 다녀야겠어?"
    mc "별로 그렇다고 한 적은 없는 것 같지만 말야…."
    "나만 들리는 작은 목소리로 말한다…."
    "나츠키는 내가 그렇게 싫은걸까?"
    "이렇게 되면 내 시를 맘에 들어 했다는 걸 좋아해야할지 말아야 할지 모르겠다."
    mc "뭐, 어쨌든, 네 차례지 않아?"
    n 5s "끄응… 알았어."
    n "그렇다고 안 보여주면 분명 모니카가 뭐라고 할 테니까."
    return

label ch2_n_bad:

    if n_poemappeal[0] < 0:
        n "…흠."
        n 2k "뭐, 저번 시보다는 낫다는 걸 인정해주지."
        n "노력하는 모습이 보기는 좋아."
        mc "다행이네…."
        n 2c "그래도 하나도 맘에 안 들어."
        n "일부러 진지해지려고 하잖아."
        mc "에? 그게 무슨 뜻이야?"


        label ch2_n_bad_sharedwithch3:
            n 4c "시는 뭔가를 표현하기 위해 꼭 어려운 말을 집어넣을 필요는 없어."
            n "진짜로 못하는 게 아니라면 억지로 집어넣은 것처럼 보일 테니까."
            n 4w "솔직히… 유리 정도 실력이 되기 전까지는 이런 식으로 시를 쓰는건…."
            show natsuki 4o
            "나츠키는 갑자기 하던 말을 멈췄다."
            n 1o "너, 너 설마…."
            mc "응?"
            n "너 설마 유리한테 잘 보이려고 이러는 건 아니지?!"
            mc "무, 무, 무슨 소리 하는 거야?! 그리고 목소리 좀 낮춰…!"
            n 1x "유리가 이런 무서운 거 좋아할 거라는 거 너도 알잖아……!!"
            mc "유리가 글 쓰는데 재능이 있긴 하지만 그게 그런 뜻은… 그, 그러니까…."
            n 1o "우으…!!"
            "내 무덤을 내가 팠지."
            "내가 무슨 말을 했는지는 몰라도 제대로 신경을 건드린 모양이다."
            n 1c "너 진짜 질린다 질려."
            "나츠키는 내 시를 아무렇게나 밀어준다."
            n 5w "이 멍청한 시나 빨리 가져가. 남을 위해 쓴 거면 나한테 보여주지나 말던가!"
            mc "어우…."
            "처음부터 이렇게 한 방 먹을 운명이였겠지."
            "어차피 나츠키에게는 관심도 없었고…."
            $ skip_poem = True
            return
    else:

        n 1k "…흐음."
        n "저번에 쓴 게 더 마음에 드는데."
        mc "응? 진짜?"
        n 2c "응, 이번엔 뭔가 과감한 단어선택을 했다는 느낌이 들거든."
        n "그런데 아직은 그만한 실력이 별로 되지 못해서 시 느낌이 하나도 안사니까."
        mc "그럴지는 모르겠지만, 난 그냥 새로운 걸 시도해보던 것뿐이야."
        mc "아직 감이 안 잡혔을 뿐이지."
        n 2k "응, 난 너무 복잡하지 않은 시가 좋더라."
        n 2q "난 사람들이 괜스레 어려운 말로 복잡하고 멋지게 보이려는 시를 쓸 때가 싫더라."
        n 4b "간단하고, 귀엽고, 의미가 명확하게 만들어도 되잖아!"
        n 4y "유리의 머리속에 무슨 복잡한 말도 안 되는 게 들어있는지는 몰라도, 허튼소리라는 건 딱 봐도 알만하잖아. 하!"
        n 42a "깊은 의미를 담는답시고 복잡한 문체로 마구 도배해두는 건 그냥 아무 의미 없다는 걸 덮으려는 핑계밖에 더 돼?"
        mc "그렇게도 볼 수 있겠네."
        n 2d "뭐, 의견은 다들 있잖아."
        n "그치만 내가 말한 것만 한 의견이 또 없을걸? 너도 그렇게 생각하는 것 같은데?"
        mc "어어…."
        n 2a "어쨌든, 자 여기. 보고 배우셔."
        return

label ch2_n_med:

    if n_poemappeal[0] < 0:
        n "…흐음."
        n 2k "그래, 저번에 쓴 거보다 낫다는 건 인정할게."
        n "노력했다는 게 보이니까 얼마나 좋아."
        mc "다행이다…."
        label ch2_n_med_shared:
            n 2c "지금보니까, 어제 사요리가 썼던 시랑 비슷한 느낌이 드는데…."
            mc "응? 그래?"
            n 2j "응. 뭐, 오랫동안 친구로 지냈으니까, 생각이 비슷한 걸 수도 있고."
            n 2k "그래도 사요리형은 아니고 말야."
            mc "이젠 사요리가 종류로 취급받는 거야…?"
            n 42c "몰라! 근데 솔직히 말해서, 어떻게 사요리처럼… 어… 가벼운 사람이 너랑 그렇게 오랜 시간을 보낼 수 있는 거야?"
            n "완전 납덩어리를 들고 가는 꼴이잖아."
            mc "으윽… 그럴 말 할 필요는 없었잖아…."
            mc "그럼 이렇게 하자. 나 만한 납덩어리가 없었다면 너무 가벼워서 날아가 버렸을 거라고. 끈 풀린 풍선처럼 말이야."
            mc "그런 식으로 서로 돌봐준다고 보면 돼."
            n 2q "무슨 소린지 하나도 모르겠어…."
            n "…아, 맞아. 내 시도 보여줘야 하지?"
            n "자."
            return


    elif n_poemappeal[0] == 0:
        n "…흐음."
        n 2k "뭐, 저번 시보다 나쁘지는 않네."
        n "낫다고도 할 수 없지만."
        mc "휴우…."
        n 2c "뭐? ‘휴우’라니, 뭔데?"
        mc "아… 완전 엉망이 아니라면 나한텐 성공했다는 거니까."
        mc "그리고 셋 중에서 네가 가장 비판적인 것 같고."
        n 1p "야, 야! 도대체 그거 무슨…."
        n 1q "{i}(잠깐, 방금 그거 칭찬이었나…?){/i}"
        n 4y "아, 아하하! 드디어 내 진가를 알아보는 사람이 나왔네!"
        n "그럼 내 경지에 오르기까지 열심히 연습하라고!"
        mc "저기, 그건…."
        "나츠키 뭔가 제대로 헛다리 짚은 것 같은데…."
        jump ch2_n_med_shared
    else:


        n "…흠."
        n 2c "완전 못한 정도는 아닌데."
        n "저번 거에 비하면 조금 실망이네."
        n 2s "뭐, 저번만큼이나 잘 했으면 그건 그것대로 짜증 나겠지만 말야."
        mc "으응, 이렇게 하면 어떨까? 하고 쓴 거라 그럴지도."
        n 2c "이해해. 어차피 넌 글쓰기 한지 얼마 안 됐으니까. 본인 스타일 찾는 게 원래 제일 어려워."
        jump ch2_n_med_shared

label ch2_n_good:

    if n_poemappeal[0] != 1:
        n 1h "…."
        "나츠키는 내 시를 읽었다."
        "내 시와 나를 번갈아 가면서 힐끔거리고 있다."
        "이 정도 시간이면 두 번도 더 읽었을 텐데."
        n 1q "…너 원래 되게 못 쓰지 않았었어?"
        mc "…그거 칭찬이야?"
        n 1o "아, 아냐! 내 말은… 그러니까…."
        "나츠키는 원하는 단어를 찾기 위해 안간힘을 쓰고 있다."
        n 5w "어제 거 보고 조금 덜 기대했었는데… 이번엔 잘 썼다고."
        n "그게 다야."
        mc "뭐, 이번엔 운이 좋았나보네."
        n 4t "그래!! 그거야!"
        n "그냥 운이 좋았던 거라고!"
        n 4y "그러니까 너무 자만하지마."
        n "네가 항상 이런 귀여운 시를 쓰는 건 아니잖아. 아, 내 말은…!"
        n 1p "내 말은 잘 썼다고! 아냐, 내 말은…."
        mc "아, 그 얘기였구나. 내 시가 귀여운 거야?"
        n 1v "아니야! …왜 웃고 있는 거야?! 내가 귀여운 걸 좋아하는 것도 아닌데!"
        "나츠키는 내 시를 돌려주었다."
        n 4w "하, 하하! 다시 읽어보니까 별로 좋은 거 같지도 않네."
        n "너무 귀엽고 두근두근 거리잖아."
        n 4t "그런 거… 좋아하는 여자애들… 점수는 좀 딸 수 있겠네."
        n "아하하!"
        "왠지는 모르겠는데, 네 속마음이 훤히 보인다."
        n 1w "뭐, 어쨌든…!"
        n 1h "내 시도 읽어봐."
        n "네 입맛으로 보아하니, 분명 마음에 들 거야."
        n 2q "아마 보면 뭔가 배우게 될 거야. {i}누가{/i} 진짜 프로인지 잊지 마."
        return
    else:

        label ch2_n_good_sharedwithch3:
            n 1n "…."
            "나츠키는 내 시를 읽었다."
            "내 시와 나를 번갈아 가면서 힐끗거리고 있다."
            "이 정도 시간이면 두 번도 더 읽었을 텐데."
            n 1u "으어…."
            mc "…?"
            mc "별로야?"
            n 1r "아니야! 그런 게 아니야!"
            n "좋아. 좋다고, 알겠어?!"
            n 5w "자, 말해줬지!"
            n "으윽, 이렇게 되면 안되는건데…!"
            n 5s "왜 이럴 땐 글을 잘 쓰는거야?"
            n "원래 내 시를 보고 감명받을 건 {i}너{/i}란 말야, 그 반대가 아니라!"
            mc "네 시에 감명받게 하려고 했다고?"
            n 12c "당연하지! 네가 유리의 문체를 좋아하도록 내버려 둘 것 같아?"
            n "그만 좀 해."
            mc "으음…."
            mc "그러면, 내가 네가 좋아할 만한 시를 썼다는 건 뭐가 문제야?"
            n 1e "내가 말해줄게! 너…."
            n 1p "…."
            "나츠키는 무언가 깨달은 듯 얼어붙었다."
            n "너, 너… 너…."
            n "너가…{i}날?{/i}"
            show natsuki 1q
            "나츠키는 빠르게 내 시를 훑어보았다."
            "그러곤, 나츠키의 손에서 내 시가 적힌 종이가 스르르 빠져 바닥에 팔랑거리며 떨어진다."
            n 1p "….화장실 가야겠어!"
            show natsuki at lhide
            hide natsuki
            "얼굴을 붉인 채, 나츠키는 급하게 부실을 나갔다."
            show monika 1d zorder 2 at t11
            m "저기, [player]…."
            m "나츠키한테 무슨 일 있어?"
            m "어딘가 달려가는 걸 봤는데…."
            m 2g "무슨 나쁜 짓 한 거 아니지?"
            mc "아, 아냐!"
            mc "나는 그저…."
            "내 목소리는 목구멍 끝까지 차올랐지만…."
            "내가 나츠키를 위한 시를 썼다는 걸 모니카한테 말할 수 있을 리가 없잖아."
            m 2d "으응?"
            "모니카가 내 종이를 보고 재빠르게 주워 올린다."
            if m_readpoem:
                "종이를 다시 한번 훑어보더니, 모니카의 표정에서 미소가 떠나질 않는다."
                m 2a "그랬구나."
                m "처음엔 나츠키 문체가 맘에 들어서 그렇게 쓴 줄 알았는데…."
                m "너 이거, 나츠키를 {i}위해{/i} 쓴 거지, 그렇지?"
            else:
                "내 시를 읽어보더니, 얼굴에서 미소가 떠나질 않는다."
                m 2a "그런거구나."
                m "너 이거 나츠키를 위해 쓴 거지, 그렇지?"
            mc "그, 그게…."
            mc "그런건 아닌데…."
            m 2d "그러고보니 언젠가 나츠키가 네 시를 정말 좋아한 적이 있었지?"
            m "벌써 나츠키의 취향을 알아내다니."
            m 4a "찾아보거나 그런 건 아니지, [player]?"
            mc "찾아보다니…?"
            mc "그게 무슨 말이야?"
            m 5a "아니야, 그냥 농담한 거야. 아하하!"
            "나는 모니카의 농담을 이해하지 못 했다."
            m "어쨌든…."
            m 1a "나츠키가 너에 대해서 어떻게 생각하는 거 같아?"
            m "아, 대답할 필요는 없어."
            m "그냥 한번 생각해보라고 말한 거 였어."
            show monika zorder 2 at t22
            show natsuki 4e at l21
            n "야!"
            "나츠키가 다가와 모니카의 손에서 시를 빼앗아간다."
            "우리 둘 다 나츠키가 교실로 다시 들어왔다는 걸 알아채지 못했다."
            show natsuki zorder 3 at f21
            n "모니카, 너 이거 읽었어?"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 1j "당연하지! 엄청 맘에 들던데?"
            show monika 1a zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1r "으어…."
            n "넌 남의 걸 함부로 건드는 나쁜 버릇이 있더라."
            n "그거 진짜 ‘나쁜’ 습관이야."
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 1d "에?"
            m "그래도 이 시는 [player]가 쓴 거잖아."
            m 1a "그리고 모두랑 나눠보기로 했잖아, 그렇지?"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1x "우으…."
            "나츠키는 얼어붙었다."
            "엄밀히 따지면 내 시는 모두가 읽어야 했다는 사실을 잊어버린 듯했다."
            n 42c "그래, 좋아, 내 생각엔 [player]는 이미 다 나눠본 거 같아."
            n "어차피 읽고 싶어 하는 사람도 없는 것 같고…."
            n 4h "그러니까, 이건 그냥 내가 갖고 있겠어."
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m 5 "네가 그렇다면~"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 1i "뭐야?"
            n "왜 그런 식으로 쳐다보는 거야?"
            show natsuki zorder 2 at t21
            show monika zorder 3 at f22
            m "어떻게 봤는데?"
            show monika zorder 2 at t22
            show natsuki zorder 3 at f21
            n 12b "으어…."
            n "아무것도 아냐."
            if not m_readpoem:
                $ poemsread += 1
                $ m_readpoem = True
            if poemsread >= 3:
                "이제 나츠키가 내 시를 가진 것 같네."
                "뭐, 내가 보관해두려는 건 아니였으니까."
            else:
                $ unfairto = "Sayori"
                if s_readpoem:
                    $ unfairto = "Yuri"
                show natsuki zorder 2 at t21
                mc "어, 나츠키…."
                if unfairto == "Yuri":
                    mc "시를 주는 건 괜찮은데, 그래도 유리한테는 좀 불공평한 거 아니야…?"
                if unfairto == "Sayori":
                    mc "시를 주는 건 괜찮은데, 그래도 사요리한테는 좀 불공평한 거 아니야…?"
                mc "…걔는 아직 내 시를 안 읽어봤잖아."
                show natsuki zorder 3 at f21
                n 2q "그래서 뭐?"
                show natsuki zorder 2 at t21
                show monika zorder 3 at f22
                m 2a "음… 나도 [player]한테 동의해, 나츠키…."
                m "모두가 읽지 못 한다면 공평하지 않지."
                show monika zorder 2 at t22
                show natsuki zorder 3 at f21
                n "…."
                n 2h "…그래."
                "나츠키는 내 시를 돌려줬다."
                n "읽고 좋아할 거 같지도 않은데."
            show monika zorder 1 at thide
            show natsuki zorder 2 at t11
            hide monika
            n 2h "어쨌든, 내 시 읽어봐."
            n 4h "미리 말해두는데, 주지는 않을 거야."
            n "한 장밖에 없거든."
            return

label ch3_n_bad:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        label ch3_n_bad12_shared:

            n 5x "네, 됐네요."
            mc "응? 너…."
            n 5w "{i}다음!{/i}"
            $ skip_poem = True
            return

    elif n_poemappeal[0] < 0 or n_poemappeal[1] < 0:
        n "…."
        n 2c "…하."
        n "아무것도 배운 게 없는 거 같네."
        n "솔직히, 내가 왜 처음에 희망을 가졌는지 모르겠다."
        mc "뭐? 이번 건 별로 나쁘지 않았다고 생각하는데…."
        mc "내가 뭘 잘못 한 걸까?"
        jump ch2_n_bad_sharedwithch3
    else:

        n "…."
        n 2r "저런."
        n "실력이 뒷걸음질 치고 있네."
        mc "어?"
        n 2c "이거보다 네가 저번에 쓴 두 개가 훨씬 낫다고."
        n 1k "내 말은…."
        n "네가 새로운 걸 시도해봤다는 건 좋아."
        n 1c "물론 네가 유리 점수 따려던 게 아니라는 전제하에."
        n 5x "…더러워."
        mc "알았어, 알았어."
        mc "네가 얘기했으니까, 새로운 걸 시도해도 되겠네."
        label ch3_n_shared:
            show natsuki 5g
            mc "그런데, 왜 그렇게 내 시를 감정적으로 평가하는 거야?"
            mc "그건 나한테 더 칭찬해주는 거 아니야?"
            n 1o "…에?"
            n 4x "아, 아냐! 더러워!"
            n 4w "내가 상관할 바가 아니잖아"
            n "적어도 부원 중에 {i}한 명{/i}은 네가 게으름 피우지 않도록 해야 하니까."
            mc "그래?"
            mc "그러다가 내가 낙담해서 시를 안 쓰게 되면 어쩌려고?"
            n 1t "그럼… 어…."
            n "…그럴리가 없잖아."
            mc "그렇긴 해."
            mc "너랑 있어야 한다고 하더라도, 여기 있는 건 되게 재밌어."
            show natsuki 1x
            mc "{i}으억…!!{/i}"
            "나츠키의 팔꿈치가 내 배에 꽂혔다."
            n 2y "호오?"
            n "널 겁줘서 도망가게 해도 상관없을 거 같은데?."
            mc "난 그냥…… 장난이었는데…."
            n 4z "아, 나도 알아!"
            n "걱정하지 마, 나도 장난이었으니까."
            n "아하하하!"
            show natsuki 4j
            mc "…."
            "어떻게 그게 장난일 수가 있는 거지?"
            "아파 죽겠는데…."
            "뭐, 나츠키가 재밌었다면…."
            "… 그럼 장난이 맞겠네."
            "나츠키 앞에선 정말 말조심해야겠다."
            n 2c "어쨌든…."
            "나츠키는 아무 일도 없었다는 듯, 나에게 시를 건네주었다."
            return

label ch3_n_med:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared
    elif n_poemappeal[1] != 0:
        n "…."
        n 2k "…이건 괜찮네."
        mc "그래?"
        n "뭐, 응."
        n "그냥 괜찮은 정도야."
        n "맘에 안 드는 부분은 딱히 없어."
        n "그냥 내 스타일이 아니야, 뭐, 상관없겠지만."
        jump ch2_n_med_shared
    else:
        n "…."
        n 2k "…이건 괜찮네."
        mc "그래?"
        n "뭐, 응."
        n "어제 시 만큼 괜찮은 거 같은데"
        n "네가 뭘 쓰고 싶은지는 알겠는데, 딱히 내 스타일은 아니다."
        n 2a "뭐, 상관없겠지만."
        n "네가 조금만 더 노력한다면 되게 기쁘겠는데…."
        mc "최대한 노력은 해볼게."
        jump ch3_n_shared

label ch3_n_good:

    if n_poemappeal[0] < 0 and n_poemappeal[1] < 0:
        jump ch3_n_bad12_shared

    elif n_poemappeal[0] > 0 and n_poemappeal[1] > 0:
        n 1l "어디 보자, 어디 보자!"
        mc "너 오늘 되게 열심이다?."
        n 2j "당연하지."
        n "내가 네가 쓴 시 좋아하는 거 알잖아."
        mc "놀랐어."
        mc "전에는 인정하기 되게 힘들어했던 거 같은데…."
        n 5w "뭐… 당연하지!"
        n 5q "네가 잘난 척 못 하게 하려고 그랬던 거야!"
        n "내가…."
        n "부끄러웠다거나 뭐 그런 바보 같은 게 아니라고."
        n 5t "아니면 질투했다거나!"
        n "별로 질투한 건 아니였어."
        n "네가 좋은 작가가 되어서 질투를 한다?"
        n 4y "진짜 질투하기에 되게 바보 같은 일이네."
        n "아하하!"
        mc "나츠키…."
        n 1h "왜?"
        mc "너 글 쓰는 게 별로 자신 없지?"
        n 1n "…에?"
        n "무, 무슨 소리 하는 거야?"
        n 1u "내가 쓰는 글이 최고인데…."
        n "…그렇지?"
        mc "…."
        "좀 시간이 걸리긴 했지만, 드디어 알아낸 것 같다…."
        "어쩌면 나츠키가 너무 거만하게 행동하는 이유는 자신의 불안감을 숨기기 위한 것일지도 모른다."
        "자기가 최고인 마냥 행동하면 다른 사람도 그렇게 생각할 거라는 생각에."
        n 1m "그렇지…?"
        n "[player]…."
        n "그냥 제발 내 시를 좋아한다고 말해줘."
        n 1u "네가 사실 싫어해도 상관없어."
        n "그냥 내가 최고라고 말해줘."
        n "난 그냥…."
        n 1q "누군가가 나한테 말해줬으면 좋겠어."
        n "멍청한 소리라는 거 알아."
        n "내가 이전까지 시를 공유하지 않았던 이유가 있어."
        mc "나츠키…."
        n "왜냐하면…."
        n 12c "아무도 나를 진지하게 생각 안 하잖아!"
        n "사람들이 그저 웃으면서 \"너무 귀엽다, 꼭 너같아, 나츠키!\"라고 말한다면 내 시를 공유하는 게 무슨 의미가 있겠어!"
        n "가끔은 나도 귀여워지고 싶지않아!"
        n 12d "그래도 아무도 그걸 알아주지 않는다고…!"
        n "나는 글을 쓸 때 엄청 열심히 써."
        n 12e "스타일은 상관없어."
        n "거기엔 감정이 있어."
        n 1n "왜 아무도 그걸 {i}봐주지{/i} 않는 거지…?"
        n 1u "나는 그냥…."
        "나츠키는 말을 잃었다."
        "나츠키의 입술이 떨리기 시작해서인 듯하다."
        "난 그저 바닥만 내려다볼 뿐이었다."
        "나츠키는 주먹을 정말 꽉 쥐고 있었다."
        mc "저기, 나츠키."
        mc "그러다가, 시 찢어지겠어."
        "난 나츠키가 들고 있던 종이를 집어 나츠키가 살살 놓도록 유도한다."
        "나츠키가 종이를 놓자, 난 책상 위에 종이를 두고 구겨진 부분을 핀다."
        n 1h "이, 읽지 마!"
        "다시 집어 들기도 전에, 나츠키가 시를 낚아채 간다."
        n 5q "별로 못 썼으니까."
        n "네가 내 시를 싫어하는 거 알아."
        n "그러니까 읽지 않아도 돼, 알았지?"
        mc "그래도 읽고 싶은데."
        n "왜, 왜?"
        mc "왜냐하면."
        mc "나는 네 시가 좋거든."
        mc "진심이야."
        show natsuki 5h
        mc "내가 왜 네 문체로 널 판단하겠어?"
        mc "내 문체도 막 그렇게 대단한 게 아닌데."
        mc "내가 네 시를 처음 읽었을 때, 그렇게 깊게 생각하지 않았다는 건 사실이야."
        mc "하지만 이젠 너를 잘 알잖아."
        mc "그리고 유리가 네 스타일이 자기 거보다 아마추어 같다고 생각하는 건 잘못된 거야."
        mc "그리고 사요리는… 걔는 착하니까…."
        mc "하지만 가끔 사요리는 그냥 단순한 행복에만 집착해서 사람들이 진짜 원하는 게 뭔지 모를 때도 있어."
        mc "…그래, 네가 얼마나 힘들었을까 생각해 본 적이 없는 것 같아."
        mc "내가 그 문제의 일부였다면 미안해."
        mc "지금 깨달았어."
        mc "넌 그냥 귀엽기만 한 게 아니라, 넌 그 이상의 사람이야."
        show natsuki 12d
        mc "아… 나츠키, 너 또 그런다…."
        "다시 한번, 나츠키는 시를 세게 꽉 쥐었다."
        "나츠키는 아래를 내려다보며 나에게 눈을 숨기고 있다."
        "이게 얼마나 나츠키에게 힘든 일이었을지 몰랐다."
        "하지만 결국, 나츠키는 팔을 뻗어 자신의 시를 테이블 위에 내려놓았다."
        n 12e "…읽어도 돼."
        n "저쪽으로 돌아서서 봐."
        n "지금… 내 얼굴 보지 말아줬으면 해."
        mc "응, 알았어."
        return


    elif n_poemappeal[0] > 0 or n_poemappeal[1] > 0:
        jump ch2_n_good_sharedwithch3
    else:

        n "…."
        n 2k "…드디어!"
        mc "응?"
        n 2l "이거. 되게 좋은데!"
        n "얼마나 걸렸을지 궁금해지는걸."
        mc "다행이네!"
        n 4y "응, 진짜."
        n "다른 사람이 뭐라 해도 신경 쓰지 마."
        n "특히 유리의 말은 말야."
        n 4a "그냥 이런 시만 써. 그럼 되잖아!"
        mc "저…."
        mc "그럼 결국 {i}네{/i} 말대로 하는 게 아닐까?"
        n 2h "저기요?"
        n "너 지금 프로랑 얘기하고 있는 거야."
        n "내 의견을 가장 믿어야 한다고 생각하지 않니?"
        mc "그야 그때그때 다르지."
        mc "너 지금 간단하고 귀여운 시에 편향된 쪽으로 얘기하고 있는 게 아냐?"
        n 2w "편향이라니?"
        n "당연히 아니지."
        n 4y "그냥 내 의견이 최고일 뿐이야."
        mc "…."
        "아직도 모르겠는 게 한 가지 있다면…."
        "나츠키는 자기 성격이 어떤지 알고나 있는 걸까?"
        "이 속도라면, 영원히 모를 것 같다…."
        mc "…그래, 그렇다면."
        mc "내 시가 좋았다니, 다행이네…."
        n 4z "아하하!"
        n 4j "드디어 이해하는구나."
        n "이런 식으로 하다 보면, 너도 언젠가 프로가 될 수 있을 거야."
        n "어쨌든, 자, 내가 쓴거…."
        return

label ch1_s_bad:
    s 1b "…."
    s "…와!"
    s "[player]…."
    s 4r "진짜 못 썼다!"
    s "아하하하!"
    mc "뭐?!"
    s 4a "괜찮아, 괜찮아~"
    s "오늘 처음 써본 거니까."
    s "애초에…."
    label ch1_s_shared:
        s 1a "난 그냥 네가 시를 썼다는 게 너무 기뻐."
        s "네가 정말 동아리의 일원이라는 생각이 들어~"
        "(당장 너랑 같은 교실에서 같은 부 활동을 하고 있는데…?)"
        mc "뭐… 음, 그렇지."
        mc "아직은 익숙치 않지만, 약속은 약속이니까."
        s 1d "그치?"
        s "내가 전에 말했듯이, [player]…."
        s "너 마음 깊은 곳에는 하나도 이기적이지 않은 거 알아?"
        s "다른 사람들이랑 새로운 걸 시도해 보는 거라던가…."
        s 2q "그런건 진짜 마음 착한 사람만 할 수 있는 거야!"
        mc "고마워… 사요리."
        "…사요리는 내 꿍꿍이를 조금이라도 눈치챌 수 있을까 싶다."
        "뭐 그래도…."
        "내가 문예부에 들어온 이유 중 하나가 사요리라는 걸 부정할 수는 없다."
        "이게 사요리한테 얼마나 큰 의미인지를 생각한다면…."
        s 1x "응."
        s "정말 즐거운 시간만 보내고 가게 해줄 테니까. 알겠지?"
        s "그게 너에게 보답하는 길이니까~"
        mc "그래, 그럼 기대할게."
        s 4r "예에에~!"
        s "이제 네가 내 시를 읽을 차례지, 그치?"
        s 1y "걱정 마, 나도 글쓰기는 못 하거든."
        s "에헤헤…."
        mc "뭐, 곧 알게 되겠지."
        return

label ch1_s_med:
    s "…."
    s 2x "오, 괜찮다. [player]!"
    s "처음 써보는 거 맞아?"
    mc "당연하지…."
    mc "별로 잘 쓴 것 같지는 않은데…."
    mc "내가 쉬는 시간에 글을 쓰는 사람은 아니잖아?"
    s 2q "에헤헤, 그것도 그렇네~"
    s 1q "그래서 내가 감명받은 거야!"
    s 1d "솔직히 말하면…."
    s "네가 진지하게 하지 않거나…."
    s "아니면 아예 안 써올까봐 걱정했어."
    jump ch1_s_shared

label ch1_s_good:
    s 1n "…."
    s "…와, 세상에!"
    s 4b "이거 지이인짜 좋다, [player]!"
    mc "어?"
    s 4r "엄청 마음에 들어~!"
    s "너 언제 이런 실력을 숨기고 있던 거야!"
    mc "사요리…."
    mc "너 분명 과장하는 거지."
    mc "애초에 내가 글을 써본 것도 아니고."
    mc "솔직히 뭘 어떻게 했는지 하나도 몰라."
    s 1x "으응…."
    s "그래서가 아닐까?"
    s "나도 내가 뭘 좋아하는지 모르거든!"
    s 1r "아하하하!"
    mc "어휴…."
    if y_readpoem:
        "유리가 더 적극적인 조언을 해 주던데…."
    else:
        "그것보단 적극적인 조언을 해 주면 좋을 텐데."
    if not n_readpoem:
        "나츠키도 말야…."
    mc "내가 써서 좋은 게 아니라?"
    s 1b "에?"
    s "뭐, 완전 아니라고는 못 하겠지만."
    s 1x "다른 사람들 보다는 내가 널 더 잘 이해해서가 아닐까?"
    s "네 시를 보면…."
    s "그냥 시가 아니라…."
    s 4q "[player]이의 시다 라는 느낌이 딱 오거든!"
    s "그래서 더 특별하다고 느끼는 것 같아!"
    s "네 감정이 바로 느껴지거든~"
    "사요리가 종이를 가슴에 비비고 있다…."
    mc "너 이상해, 사요리…."
    s "에헤헤…."
    jump ch1_s_shared


label ch2_s_bad:
    s "…."
    s 1q "에헤헤, 네 시 읽는거 완전 좋다~"
    s "전혀 예상 못 하겠어!"
    mc "별로였다는 거네."
    s 4c "아냐! 전혀 아냐!"
    s 4l "…아마도!"
    s 5a "조금은?"
    s "유리가 내 눈을 너무 높여놓은 게 분명해…."
    s "에헤헤…."
    mc "괜찮아, 괜찮아."
    mc "애초에, 난 네가 어떤 문체를 좋아하는지도 모르는걸."
    label ch2_s_shared:
        s 1q "응!"
        s "나도 그래!"
        mc "으윽…."
        mc "조금이라도 생각해보지 그래?"
        s 2d "우웅, 날 위해 뭐라도 써주려고 그러는 거야?"
        s "너 완전 자상하다~"
        mc "응, 그래."
        mc "넌 너무 다른 생각만 하는 것 같아."
        mc "가끔은 네 생각도 좀 해야 하지 않을까?"
        mc "안 그러면, 언젠가 크게 다칠지도 모르니까."
        s 1n "에에에?"
        s "뭐…."
        s 1o "무슨 말인지는 잘 모르겠지만, 기억해 둘게!"
        mc "뭐, 그래…."
        s 1b "어디보자…."
        s "흠…."
        s 4q "난… 행복한 시가 좋은 것 같아~"
        s 4i "잠깐, 난 슬픈 시도 좋은데…."
        s 1i "가끔은 둘 다…."
        s "둘 다 뜻하는 단어가 있지 않아…?"
        s "뭐였더라…."
        s 4r "…달곰씁쓸!"
        s "응응!"
        s 1x "난 행복하고 슬픈 그런 게 좋아."
        mc "행복하고 슬픈?"
        mc "네가 슬픈 게 좋다니, 되게 의외다 사요리…."
        s 1c "으응…."
        s "난 행복한 게 좋아!"
        s 1d "근데 가끔씩 머리 속에 먹구름이 잔뜩 낄 때면…."
        s "슬픈 시들이 먹구름들에게 작은 포옹을 해 주는거야…."
        s 4q "…그러고 행복한 무지개들을 만드는 거지!"
        mc "…사요리, 방금 그거 되게 시적이었어."
        s 4n "에? 그래?"
        s "내 감정표현을 더 잘하게 된 걸 거야!"
        s 2q "고마워, [player]!"
        s "까먹기 전에 적어놓아 둬야겠어~"
        s 2a "그동안 내 시 읽으면 되겠다."
        return

label ch2_s_med:

    if s_poemappeal[0] < 0:
        s "…."
        s 4x "오오!"
        s "나 이거 맘에들어, [player]!"
        s "좋은 감정도 들어가 있고~"
        mc "아, 다행이네."
        mc "그럼 어제보다는 잘 쓴 거네."
        s 1q "응응!"
        mc "그럼 이쪽이 나은 걸지도."
        label ch2_s_med_shared:
            s 1a "으응, 시가 좋고 나쁜지는 나도 잘 모르니까…."
            s "그래서 내 마음에 맡기는 편이야~"
            s "감정이 느껴지는 거면, 좋은 시인 거고!"
            "역시 무슨 얘긴지 하나도 모르겠다…."
            "…그래도 따지고 보면 감정을 표출하는 게 중요한 요소 중 하나긴 하겠지."
            mc "응, 그렇겠네…."
            mc "솔직히 네가 어떤 시를 좋아하는지는 전혀 모르니까."
            jump ch2_s_shared

    elif s_poemappeal[0] == 0:
        s "…."
        s 4x "오오!"
        s "나 이거 마음에 들어, [player]!"
        s "좋은 감정도 들어가 있고~"
        mc "아, 다행이네."
        mc "어제랑 비교하면 어때?"
        s 4b "으음, 잠깐만…."
        s 1q "잘 모르겠어!"
        s "둘 다 마음에 드는 것 같아!"
        s "에헤헤~"
        mc "별로 도움 안 되는 대답이라는 건 알지…?"
        jump ch2_s_med_shared
    else:

        s "…."
        s 4x "오오!"
        s "나 이거 마음에 들어, [player]!"
        s "좋은 감정도 들어가 있고~"
        mc "아, 다행이네."
        mc "그런데…."
        mc "목소릴 들어보니 어제 시가 나았던 모양이네."
        s 2l "에헤헤, 티 났어…?"
        s "가끔씩 보면 넌 날 너무 잘 안다니까!"
        mc "너무 잘해주려고 하지는 마."
        mc "뭔가 잘못하고 있는 게 있다면, 솔직한 답을 듣는 게 나으니까."
        s 1c "아냐, 아냐!"
        s "그래도 난 이게 좋았는걸, 진짜야!"
        s 1h "내가 너한테는 거짓말 안 한다는 거 잘 알잖아, [player]…!"
        s "절대 절대!"
        mc "응, 그렇네…."
        mc "그럼 어제의 시가 왜 더 좋았던 건지 얘기해 줄 수 있어?"
        s 1b "으응……."
        jump ch2_s_med_shared

label ch2_s_good:

    if s_poemappeal[0] < 1:
        s 1n "…."
        s "…세상에!"
        s 4r "이거 완전 짜아앙이다, [player]!"
        mc "에?"
        s "너무 좋아~!"
        s "특히 어제 거랑 비교하면 말야!"
        mc "으윽…."
        mc "가끔 너 너무 솔직하다니까, 사요리."
        s 4x "그치만 진짜로!!"
        s 1x "이거 벽에 걸고 싶어~"
        s "그래도 돼"
        mc "사요리…."
        mc "너무 과장하는 거 아냐?"
        mc "애초에 내가 글 쓰는것도 아니고."
        mc "솔직히 뭘 어떻게 했는지 하나도 몰라."
        s 1l "으응…."
        s "그래서가 아닐까?"
        s "나도 내가 뭘 좋아하는지 모르니까!"
        s 4r "아하하하!"
        mc "어휴…."
        "유리의 의견이 좀 더 적극적이었는데."
        "잘만 하면 나츠키 것도."
        mc "그냥 내가 써서 좋은 게 아니라?"
        s 4b "에?"
        s 1b "아예 아니라고는 못 하겠지만."
        s 1x "다른 사람들 보다는 내가 널 더 잘 이해해서가 아닐까?"
        s "네 시를 보면…."
        s "그냥 시가 아니라…."
        s 4q "[player]이의 시라는 느낌이 딱 오거든!"
        s "그래서 더 특별하다고 느끼는 것 같아!"
        s "네 감정이 바로 느껴지거든~"
        "사요리가 종이를 가슴에 비비고 있다…."
        mc "너 이상해, 사요리…."
        s "에헤헤…."
        jump ch2_s_med_shared
    else:

        s "…."
        s 1d "[player]…."
        s "나 네 시 완전 좋아."
        s "어째서 이런 실력을 숨기고 있던거야?"
        mc "에? 숨긴 적 없어!"
        s 1b "그치만…."
        s "네 시 엄청 좋은걸…."
        s "어제 것도, 오늘 것도!"
        s "솔직히 말해봐, 원래부터 시 썼지?"
        mc "으응…."
        mc "솔직히 말하자면 그렇게 생각하는 건 너 혼자니까…."
        s 4h "에?!"
        s "말도 안돼!!"
        s "나츠키도 그렇게 생각 안해…?"
        mc "나츠키야말로 제일 인정 안 할 것 같은데…."
        mc "그런 문제는 아닌 것 같아."
        s 1b "무슨 소리야?"
        mc "으음…."
        mc "솔직히 얘기할게."
        mc "네 생각을 하니까 시를 쓰기가 쉽더라고."
        s 4m "에, 에?!"
        s "뭐어어어?"
        mc "이상한 오해 하지 마, 바보야!"
        mc "그냥 네가… 되게 표현적인 사람이라는 거야."
        mc "내가 내 멍청한 삶에 대해 시를 쓸 수 있을 리가 없잖아."
        mc "근데 너는 네 삶을 모험하듯이 살잖아."
        mc "그게 아주 작은 거라도 말야."
        s 4o "마치 요리처럼!!"
        mc "그거 말고!"
        s 5a "에헤헤…."
        mc "응, 그러니까…."
        mc "내 관점에서 쓰기보다 네 관점에서 쓰는 게 더 도움이 된다, 이런 얘기야."
        mc "우린 약간 그런 이상한 연결점이 있는 것 같아."
        mc "네 삶에 내가 휘말려든게 잘못이고."
        s 1e "에에…?"
        s "무슨 말인지 모르겠어…."
        mc "어휴…."
        mc "어찌 말귀를 알아듣는 게 하나도 없냐, 사요리."
        "난 사요리의 머리를 쓰다듬었다…."
        s 4s "아하하! 야아아!"
        s "애 취급하는 게 어딨어!"
        mc "애인 게 아니라?"
        s 4l "으으음… 그럴지도 모르지~"
        "사요리가 손에 들고 있던 연필을 흔들기 시작했다."
        s "있지, [player]…."
        s 2d "이 시, 나 주면 안 돼?"
        s "가지고 싶어."
        mc "응? 왜?"
        s 1y "왜냐하면…."
        s "으음…."
        s "네가 날 위해 뭔가 써준 건 이번이 처음이니까…."
        s "에헤헤…."
        mc "!!"
        mc "사요리, 뭔가 단단한 착오가 있는 모양인데!"
        mc "나 이거 너한테 쓴 거 아니야!"
        s 5b "에헤헤헤헤…."
        mc "어휴…."
        mc "듣고는 있냐?"
        mc "뭐, 어쨌든."
        mc "…집에 갈 때 줄게."
        show sayori at h11
        s 4m "진짜?!"
        "{i}따악!{/i}"
        s 4p "아아!!"
        s "연필 부러뜨렸다…."
        "사요리는 급히 몸을 구부려 부러진 연필 조각들을 줍는다."
        "근데 성급하게 움직이는 바람에 나랑 부딪히고 만다."
        s 4l "미, 미, 미, 미안해!!"
        mc "괜찮아, 괜찮아."
        mc "내가 주울게."
        "난 몸을 구부려 부러진 연필 조각들을 줍는다."
        "사요리는 옆 걸상을 붙잡고 일어선다."
        s 5b "나 오늘 되게 덤벙댄다…."
        s "아하하하하…."
        mc "앉자. 사요리…."
        s 4y "으, 응…."
        "난 사요리의 팔을 부축해 의자에 앉힌다…."
        mc "있지, 아직 네 시 못 읽었는데…."
        s 4b "아차!"
        s "미안해, 완전히 까먹고 있었어~"
        s 1h "근데 너보다 못 썼으니까!!"
        mc "어휴, 걱정 마."
        mc "아마 마음에 쏙 들 거야…."
        return

label ch3_s_bad:
    $ currentname = "Yuri"
    if n_poemappeal[2] > y_poemappeal[2]:
        $ currentname = "Natsuki"
    s "…."
    s 1k "…흠."
    s "괜찮은 것 같아~"
    mc "야, 야. 별로라고 얼굴에 다 쓰여 있다."
    s 1d "으응…."
    s "내 생각은 별로 상관없을 것 같아."
    s 2y "애초에 이건 다른 사람을 위해 쓴 시 같은걸, 그치?"
    if currentname == "Yuri":
        s "아마도… 유리?"
    else:
        s "아마도… 나츠키?"
    mc "에??"
    mc "누구한테도 쓴 시 아니야!"
    s "그렇겠지…."
    s 1d "그치만 꼭 그런 뜻은 아니야."
    s "그래도 괜찮아."
    s "넌 내가 원했던 대로 새 친구를 사귀고 있는 거고."
    s 1q "그래서, 정말 행복해."
    s "너도 행복하지, 그치?"
    s 1a "이 문예부에서?"
    mc "응…."
    mc "당연하지."
    s 4q "좋아~"
    s "난 그거면 됐어."
    s 1d "고마워, [player]."
    mc "사요리…."
    mc "뭔가 문제라도 있어?"
    s 1b "응?"
    s 1k "아냐, 아무것도."
    s "그냥 조금 피곤하네."
    s 1l "에헤헤."
    mc "알았어…."
    mc "혹시라도 뭐가 필요하면 말해."
    s 1a "그럴게."
    s "내 걱정은 하지마."
    s "가서 다른 사람들이랑 놀아."
    mc "그렇게까지 말한다면야…."
    s 4q "예에에~"
    s 4a "있지, 나 먼저 집에 갈게."
    mc "사요리…?"
    s 1q "모니카한테 나 몸이 별로라 먼저 갔다고 말해줘, 알았지?"
    s "그럼 내일 봐~"
    "뭐라고 말하기도 전에, 사요리는 밝은 표정으로 콧노래를 부르며 교실 밖으로 나가버렸다."
    $ skip_poem = True
    return


label ch3_s_med:
    jump ch3_s_bad

label ch3_s_good:
    if poemwinner[0] != "sayori" and poemwinner[1] != "sayori":
        jump ch3_s_bad
    s 1d "…."
    s "이거 지금까지 쓴 것 중 최고야."
    s "정말 정말 잘 썼다, [player]~"
    mc "어어… 고마워."
    s 1q "응응~"
    mc "…."
    mc "사요리, 너 오늘 좀 조용하네."
    mc "무슨 일 있어?"
    s 4m "에에??"
    s "전혀!"
    s 4l "아무 문제 없어~"
    s "그냥 조금 피곤한 걸지도."
    s 1l "에헤헤."
    mc "혹시 낮잠이라도 자고 싶은 거야?"
    s 1h "아니? 이상해 !"
    s "내 걱정은 안해도 돼."
    s 1q "난 네 얼굴에 미소를 보고 싶을 뿐야~"
    mc "뭐, 알았어…."
    s 1b "있지, [player]…."
    s "조금 놀랐어."
    s "난 네 문체가 유리 쪽에 가까울거라 생각했거든…."
    s 1y "아님 나츠키 쪽이라던가…."
    s "근데…."
    mc "…응."
    mc "내 시를 가장 좋아하는 건 너인 것 같네."
    stop music fadeout 1.0
    s 1k "…왜?"
    s "다른 사람들이랑 친해지고 싶지 않아?"
    play music t9
    mc "뭐!"
    mc "당연히 친해지고 싶지!"
    mc "근데 그렇다고 내 시까지 그렇게 써야 한 다는 건 아니잖아."
    mc "내가 가장 많이 이해하는 것도 너고."
    mc "가끔은 네가 참는 것도 많고."
    mc "가끔은 내가 참는 것도 많지만."
    mc "우린… 뭔가 통하는 게 있는 것 같아."
    mc "그래서 우리 시도 비슷하게 나오는게 아닐까?."
    mc "가끔은 내 삶을 그나마 살만하게 만들어 주는 건 너라고 생각해."
    mc "그래서 그런지 널 생각하면 시가 잘 쓰여지는걸지도 몰라."
    mc "…사요리?"
    s 4v "아, 아니야…."
    s "[player]…."
    s "난… 이런 걸 받을 자격이 없어…."
    s "너 날 너무 잘 대해주잖아…."
    s "왜 그러는거야…?"
    "사요리의 목소리가 갑자기 떨린다."
    s "네가 다른 사람들과 좀 더 잘 지내기만 했어도…."
    s "훨씬… 쉬었을 텐데!"
    mc "사요리…!"
    "나는 다른 사람이 눈치채지는 않았는지 교실 안을 빠르게 둘러보았다."
    mc "사요리."
    mc "이런 말 처음이긴 한데, 난 네가 왜 그렇게 느끼는지 잘 모르겠어."
    mc "어떻게 하면 도와줄 수 있을지 얘기해 줘."
    "사요리가 고개를 흔든다."
    "훌쩍거리더니, 계속 고개를 흔든다."
    "끝내, 다시 안정을 되찾고 미소를 짓는다…."
    s 1y "별거 아냐, [player]."
    s "작은 먹구름일 뿐이야."
    s 4r "이상한 모습 보여서 미안해. 아하하하!"
    s "다시는 이런 모습 보여주지 않겠다고 약속할게."
    s 1a "다들 행복하면 되니까, 그치?"
    s "나는 그거면 돼."
    s "가서 다른 사람들이랑 놀아."
    s 4a "있지, 나 먼저 집에 갈게."
    mc "사요…."
    s 1q "모니카한테 나 몸이 별로라 먼저 갔다고 말해줘, 알았지?"
    s "그럼 내일 봐~"
    "뭐라고 말하기도 전에, 사요리는 밝은 표정으로 콧노래를 부르며 교실 밖으로 나가버렸다."
    $ skip_poem = True
    return

label ch1_y_bad:
    y 1g "…."
    y "음…."
    y "…."
    "유리가 시를 쳐다본다."
    "그렇게 일 분이 지났다. 시를 읽기에는 충분한 시간이었을 텐데."
    mc "저기…."
    y "아!"
    y 3n "죄, 죄송해요…!"
    y "말하는 걸 깜빡했어요…."
    y "어, 어…!"
    mc "괜찮아, 억지로 안해도 돼."
    y 2v "그런게 아니라…."
    y "생각을 말로 옮기기만 하면 돼요."
    y "잠시만요…."
    y "…좋아."
    y 1f "처음 쓰신 시죠, 그렇죠?"
    mc "어, 응…."
    mc "그건 왜 물어?"
    y "그냥 확인하는 거에요."
    y "한번 읽어보니 그런 생각이 들어서요."
    mc "아, 잘못 썼다는 거네."
    y 2p "아뇨!!"
    y 2o "…방금 제가 목소리를 높였나요…?"
    y 4c "으으… 죄송해요…."
    "유리가 손에 얼굴을 묻는다."
    "결국 아무것도 안 하고 몇 분이 지나버렸다."
    "유리같은 사람은 새 사람이랑 얘기하는데 적응하는 시간이 좀 필요하겠지…."
    mc "괜찮아, 말하기 전까진 몰랐어…."
    mc "근데 무슨 말 하던 거야?"
    y 2u "맞아요, 어…."
    label ch1_y_shared:
        y 1a "글쓰기를 처음 시작한 사람들이 하기 쉬운 버릇 같은 게 있어요"
        y "저도 그 과정을 겪었기에 잘 알고요."
        y 1i "제 생각에 그중 가장 알기 쉬운 건 문체를 너무 심사숙고해서 고른다는 점이죠."
        y "다른 말로는 주제에 맞지 않게 문체를 고르고, 둘 다 포기하지 못하는 경향이 있다는 거죠."
        y 1a "결국엔 문체와 주제 둘 다 본래 가지고 있는 성질보다 약해지고 말아요."
        "한번 말을 하기 시작하자, 하는 행동이 180도 바뀌었다."
        "말을 더이상 더듬지도 않고, 정말 전문가처럼 얘기를 한다."
        y 1k "물론, 그렇다고 해서 누가 뭐라 할 건 아니지만요."
        y "간단한 시에도 쓰이는 기술은 아주 많아요."
        y 1a "그런 기술들을 찾고 쌓는 것도 일이지만, 함께 조화를 이루도록 쓰는 게 정말 어려운 부분이에요."
        y "시간은 좀 걸리겠지만, 연습하면 충분히 소화해 내실 수 있을 거에요. 예제들을 보아가며, 새로운 것들을 써 보면서 말이에요."
        y "다른 부원분들께서도 좋은 피드백을 줄 수 있길 바랄게요…."
        y 1l "나츠키씨는 조금 편향된 생각을 드릴지도 몰라요…."
        mc "편향? 어떻게?"
        y 2j "으, 음…."
        y "어…."
        y "아무것도 아니에요…."
        y "그런 말은 하는게 아니었는데…."
        y "죄송해요…."
        mc "괜찮아."
        "본인에게 사과하는 것인지, 나에게 사과하는 것인지… 누구한테 사과하는지 전혀 모르겠다."
        mc "네 시 읽어봐도 될까?"
        y 3c "부탁드려요!"
        y "어떻게 썼는지 알려드리고 싶어요…."
        "유리가 꿈꾸듯 웃는다, 마치 자주 오지 않는 기회라는 것처럼."
        "조금 우습기도 하다…."
        "…문예부가 하는 일이 그런 게 아닌가?"
        return

label ch1_y_med:
    jump ch1_y_bad

label ch1_y_good:
    y 1e "…."
    "유리가 내 시를 읽어내려가자, 눈빛이 바뀌는 게 보인다."
    y 2f "…우수하네요."
    mc "에? 방금 뭐라고 그랬어?"
    y "…?"
    y 2n "제, 제가 방금 그걸 소리 내서 말했나요…?"
    "유리는 입을 가리려다, 결국 얼굴 전체를 두 손으로 가려버리고 만다."
    y 4c "저…!"
    y "으으…."
    y "{i}(분명 날 싫어할 거야…){/i}"
    mc "저…."
    mc "혹시나 하는 말이지만 너 아무것도 잘못한게 없는데…."
    y 4a "에…?"
    y "그게…."
    y 2q "그, 그런가요…."
    y "제가 왜 이렇게 긴장하는 걸까요?"
    y "아, 아하하…."
    show yuri 2l at t11
    "유리가 심호흡을 한다…."
    y "그럼…."
    y 1a "혹시 글은 얼마나 써 보셨어요?"
    y "비유나 묘사를 볼 때 시는 꽤 오랫동안 쓰신 것 같은데…."
    mc "정말…?"
    mc "네게서 그런 말을 듣다니, 그거 엄청난 칭찬인걸"
    mc "사실, 그게 처음이야."
    y 1e "네…?"
    "유리가 멍한 표정으로 날 바라보더니 다시 한번 시를 본다."
    y "…."
    y 2h "…저도 알아요!"
    y "제 말은… 그게…."
    "변명거리를 찾지 못했는지, 말을 잇지 못한다."
    "꼼꼼히 살펴보듯, 손으로 시를 따라 읽는다."
    y 2l "…그래."
    y "맞아요."
    y "이 부분을 볼 때 처음 쓴 거라고 생각했어요."
    jump ch1_y_shared


label ch2_y_bad:

    if y_poemappeal[0] < 0:
        y "…."
        y 2h "저…."
        y "…아직도 저한테 화나셨어요?"
        mc "에?!"
        y "나츠키 씨에 대해 나쁘게 말한 것 때문에 말이에요…."
        y "이 시를 읽어보니까…."
        y "아직 저에게 화나신 줄을 알겠더라고요."
        y "[player] 씨 께서…."
        y 3v "저보다 나츠키 씨의 문체를 더 좋아하니까요!"
        mc "아니, 아니야…!"
        y "그럼 나츠키 씨에 대해 나쁘게 말한 건…."
        y "[player] 씨에 대해도 나쁘게 말한 거네요?"
        y 4c "아아…."
        mc "유리…."
        mc "뭔가 단단한 오해가 있는 모양인데…."
        y "전 왜 이렇게 멍청한 걸까요…?"
        y "매번 이런식이에요…."
        y "말하기 전에 생각이 너무 길어서, 입 밖으로 나오는 말들은 모두 어색할 뿐이고 연결도 되지 않아요."
        y "그치만 생각을 안 하고 말해버리면, 속에 넣어두고 싶은 말들이 자기 멋대로 나와버려서 사람들이 날 싫어하게 해요."
        y 2v "그러니까, 제 곁에 있지 말아주세요."
        y "모니카 씨가 원하는 바는 아닐 테지만."
        y "나츠키 씨와 사유리 씨와 시간을 보내시는 게 더 나을 수 있으니까요."
        mc "유리…."
        y 4b "부탁이에요…."
        y "아무 말씀 안 하시는 게 제겐 나아요."
        y "그리고…."
        y "저에겐 책이 있으니까요."
        y 3u "전 그거면 되니까."
        mc "…."
        "유리가 슬프게 웃더니 앉은 자리에서 고개를 숙인다…."
        "난 화가 난다."
        "내가 뭘 잘못한것도 아닌데, 혼자만의 생각에 빠져 내 말은 전혀 듣지 못하니…."
        "난 한숨을 쉰다…."
        "원하는 대로 해 주는 게 맞는 거겠지."
        "혼자 있고 싶어하면, 혼자 있게 해주는 게 제일 좋은 방법이겠지."
        $ skip_poem = True
        return
    else:

        y 2a "아, 제 차례인가요?"
        y "어디보자, 어제에 비해선…."
        y "음…."
        y "그렇군요…."
        y "조금 다르네요."
        y 1a "[player] 씨, 다른걸 시도해보는 건 존중하지만요…."
        y "혹시 나츠키 씨의 시에서 영감을 받았나요?"
        y "아니면 사요리 씨의 시?"
        mc "뭐…."
        mc "그렇다고 할 수 있지…."
        y "그럴 거라고 생각했어요."
        y 2u "다행이네요."
        y "제 시에서 영감을 받지 않아서."
        y "절 위해 쓰는 글인걸요…."
        y 4b "…다른 사람이 아니라…."
        y "그래서 별로 좋아하지 않아도 상관없어요."
        mc "유리!"
        y 3t "에, 에?"
        mc "오지랖이면 미안한데, 너무 과하게 생각하는 것 같아서."
        mc "문체가 다르다고 해서 네 시가 싫은 건 아니야…."
        mc "사실 네 문체로도 시를 써보려고 했는데, 만족스러운 결과가 나오질 않았을 뿐이야."
        y 4a "그… 그렇군요…."
        y "죄송해요…."
        y "제가 멍청해서… 가끔 그러곤 해요."
        y "어쨌든…."
        label ch2_y_shared:
            y 2h "조금은 과감하게 글을 쓰셔도 될 것 같아요…."
            y "조금 더 비유를 쓰실 수도 있고요."
            y "기어 몇 개를 돌리듯 머리를 굴리려고 하시는 것 보다…."
            y 1m "감정에 마음을 한번 맡겨보세요…."
            y "그렇게 보고 들은 것들을 써 내려가면 되는 거예요."
            y "그럼 독자들이 시에 담긴 감정들을 보기가 쉬워지거든요."
            y 2u "잘 알려진 글쓰기 연습 방식이에요…."
            mc "그렇구나."
            mc "확실히 흥미로운 글쓰기 방법이긴 하네."
            mc "얘기해줘서 고마워."
            y 2v "저, 그게…."
            y "…어, 예제가 한가지 있어요, 읽어보고 싶으시다면요…."
            mc "물론이지."
            mc "오늘 쓴 시야?"
            "유리가 끄덕이고, 소심하게 시를 내민다."
            return

label ch2_y_med:

    if y_poemappeal[0] <= 0:
        y 1a "오늘은 어떤 시를 써오셨나 볼까요?"
        y "…."
        y "으음…."
        y 1c "잘 하셨어요, [player] 씨."
        y "점점 나아지고 계시는 게 느껴져요."
        mc "정말?"
        mc "고마워, 유리."
        mc "너한테서 들으니까, 되게 많은 의미가 느껴진다."
        y 3f "에?"
        y 3v "그, 그런 건 아니에요!"
        y "전 그냥 동료 작가들을 격려해주는 게 좋아서…."
        y "당신이 초보자인 걸 알고 있으니까, 시가 너무 완벽하지 않다고 생각되더라도 너무 걱정하지 마세요."
        jump ch2_y_shared
    else:


        y 1a "오늘은 어떤 시를 써오셨나 볼까요?."
        y "…."
        y "으음…."
        y "꽤 괜찮네요, [player] 씨."
        y "어제 다른 분들이 쓴 시를 보고 영향을 받으셨나요?"
        mc "그렇게 말할 수 있으려나…."
        y 1m "저도 모두가 쓰는 방식이 다 다르다는 게 조금 놀라웠어요."
        y "그래서 새로운 걸 시도하시는 거에 대해 존중해요."
        jump ch2_y_shared

label ch2_y_good:

    if y_poemappeal[0] < 1:
        y 1a "오늘은 어떤 시를 써오셨나 볼까요?"
        y "…."
        y 2e "……."
        "유리는 놀란 표정으로 시를 보고 있다."
        mc "마음에… 들어?"
        y "[player] 씨…."
        y "…어떻게 이렇게 빨리 성장하셨어요?"
        label ch2_y_good_shared:
            y 2v "바로 어제, 제가 실천할 가치가 있는 기술들을 말씀드렸는데…."
            mc "그래서 그런 게 아닐까…."
            mc "네가 잘 설명해준 덕분이야."
            mc "내용을 더 이미지화하고 싶었거든."
            show yuri 4b zorder 2 at t11
            "유리는 눈에 띄게 침을 삼켰다."
            "심지어 손도 땀에 젖은 듯했다."
            y "저는… 이런 것에 익숙하지 않아서…."
            mc "어떤 거에?"
            y 3o "저도 모르겠어요…!"
            mc "괜찮아, 진정해…."
            show yuri 3l at t11
            "유리는 심호흡을 하고 생각을 정리했다."
            "유리가 말하기 전에 오래 생각하는 성격이라는 걸 알고 있기 때문에, 조금 기다려주기로 했다."
            y 4a "네…."
            y "그냥…이런 식으로 누군가의 도움이 됐다는 것… 이려나요."
            y "아마 바보같이 들리실 수도 있겠지만…."
            y "하지만 제 글에 의해 동기부여가 된 누군가를 보면…."
            y "전 되게…."
            y "되게 행복해져요…."
            mc "혹시 그럼 이전에는 한 번도 글을 나눠본 적이 없다는 거야?"
            "유리는 끄덕였다."
            mc "진짜? 믿기지가 않네."
            y "전 오직 저 자신만을 위해 글을 쓰거든요…."
            y "그리고…."
            y 3w "…사람들은 절 비웃을 테니까요!"
            mc "진짜 그렇게 생각해…?"
            "유리는 다시 끄덕였다."
            mc "허어…."
            mc "네 친한 친구들도?"
            y 2v "…."
            "유리는 반응하지 않았다."
            "이유가 뭘까…."
            mc "어쨌든…."
            mc "오늘 네가 쓴 시를 읽어봐도 될까?"
            y "…네."
            y 3t "좋아요!"
            y "당신만 괜찮으시다면…."
            return
    else:

        y 1a "오늘은 어떤 시를 써오셨나 볼까요?"
        y "…."
        y 2e "……."
        "유리는 놀란 표정으로 시를 보고 있다."
        mc "마음에 들어?"
        y "[player] 씨…."
        y "이건 어제 거보다 훨씬 좋은데요…."
        y "…어떻게 이렇게 빠르게 성장하셨어요?"
        jump ch2_y_good_shared

label ch3_y_bad:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        label ch3_y_bad12_shared:
            y 4b "…."
            "유리가 나와 함께 시간을 보내는 것이 영 내키지 않아 보인다…."
            "마음이 바뀌면, 나한테 찾아오겠지."
            "하지만 지금은 그럴 때가 아니야."
            $ skip_poem = True
            return
    elif y_poemappeal[1] < 0 or y_poemappeal[0] < 0:
        y 1i "…."
        y "…그렇군요."
        y "전반적으로 글 쓰시는 능력이 나아지셨네요, [player] 씨."
        y 2i "하지만 약간 바보 같다고 느껴지는 게 있어요."
        mc "응? 뭐가?"
        y "그냥…."
        y "[player] 씨에게 계속 조언을 드리려고 노력하는데…."
        y "저와 선호하는 문체가 서로 다르시잖아요…."
        y 3w "제가 되게 좀 건방지게 보이셨을 수도 있겠네요!"
        y "전 진짜 멍청해요…."
        mc "유리, 그건 좀…."
        y 4b "아니에요…."
        y "당신은 이해 못 해요."
        y "저는 조금이라도 뭐가 더 좋고 뭐가 더 나쁠지 걱정하느라 굉장히 긴 시간을 보냈어요."
        y "당신뿐만 아니라…."
        y "나츠키 씨와, 사요리 씨도요…."
        y "이제 왜 다들 저와 대화할 때 재미없어하는지 알 것 같아요…."
        y "그러니까…."
        y 4c "…그냥 당신의 시에 대해선 입을 다물고 있을게요!"
        mc "…."
        "유리는 책상에 엎드려 얼굴을 팔 속에 묻었다."
        "유리가 이러는 걸 보는 건 이번이 처음이 아니다."
        mc "네가 생각하는 것만큼 그렇지는 않아…."
        y "…."
        mc "만약 사람들이 너와 대화하는 걸 정말 싫어했다면…."
        mc "그럼 훨씬 더 분명해지겠네."
        mc "네가 책을 깊게 읽는 걸 좋아한다는 건 알아."
        mc "하지만 어떤 것들은 그냥 액면 그대로 받아들여야 하는 것도 있어."
        y 4b "전 그냥…."
        y "그게 너무 익숙해져서…."
        y "…다른 방법이 있다는 게 저한테는 이해하기가 힘드네요."
        mc "뭐에 익숙해졌는데?"
        mc "깊게 읽는 거?"
        y "미움 받는 거요."
        mc "유리…."
        y 2v "저… 제가 지금 무슨 말을 하는 거죠?"
        y "죄송해요…."
        y "이런 얘기를 꺼낼 생각은 없었는데…."
        "유리는 날 등지고 섰다."
        y 4b "가세요…."
        mc "어…?"
        y "제발…."
        y "제발 지금은 저를 보지 말아주세요."
        y "생각하고 싶은 게 있어서…."
        mc "그래…?"
        "유리는 끄덕였다."
        mc "알겠어…."
        "나는 유리를 떠났다."
        "유리를 위로하거나 안심시키는 건 지금은 거의 불가능한 것 같다."
        "그래서 혼자 있고 싶어 하면, 혼자 있게 해주는 게 제일 좋은 방법이겠지."
        "기분이 영 좋지는 않지만, 나한테 화풀이하지 않았다는 건 고마운걸…."
        "유리의 기분이 나아질 때까지 기다리자."
        $ skip_poem = True
        return
    else:
        y 1a "…."
        y "…아."
        y "오늘은 뭔가 다른 걸 시도하려고 해보신 건가요?"
        mc "응."
        mc "괜찮아? 아니면 별로야?"
        y 2g "글쎄요. 둘 다 아니네요."
        y "전 제가 좋아하는 게 있어요."
        y "하지만 그걸 토대로 좋고 나쁜 것을 논하는 건 불공평한 짓이겠죠."
        label ch3_y_shared:
            y 1f "언제나 그랬듯이, 언제나 그랬듯이, 가장 중요한 건 자신을 탐색하고 발견하는 것이에요…."
            mc "다행이다."
            mc "난 네가 실망하지 않을까 되게 두려웠거든."
            y 2t "에…?"
            y "저요…?"
            mc "글쎄, 넌 항상 글 쓰는 것도 세련되고 좋은 조언도 많이 나눠주니까."
            y 4a "그런가요…?"
            y "…."
            "유리는 잠깐동안 생각했다."
            y 4c "…끔찍하네요."
            mc "어?"
            y "제 의견이 누군가에게 두려운 것이 되다니…."
            y "저도 제 자신이 참 호감이 안 가네요…."
            mc "유리…."
            mc "네가 생각하는 것만큼 나쁜 건 아니야."
            mc "난 그냥 네 의견을 존중한다는 뜻으로 말한 거야."
            y 2v "그런가요…."
            y "항상 지나치게 생각해서 그런 결론에 도달했다는 거에 사죄드릴게요."
            y "너무 익숙해서요…."
            mc "지나치게 생각하는 거?"
            y "미움받는 거요."
            mc "유리…."
            y 3w "제가…지금 무슨 말을 하는 거죠?"
            y "죄송해요…이 말을 꺼낼 생각은 없었는데…."
            y "넘어가죠…."
            mc "응…."
            mc "네가 쓴 시 읽어봐도 될까?"
            y 2i "네…."
            y "여기요."
            return


label ch3_y_med:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    elif y_poemappeal[0] < 1 or y_poemappeal[1] < 1:
        y "…."
        y 1a "잘 하셨어요, [player]."
        y "확실히 요 며칠 사이에 글 쓰는 솜씨가 좋아지셨네요."
        y "제 조언이 도움이 되었나요?"
        mc "응… 물론이야."
        y 2m "기쁘네요…."
        y "이렇게 서로의 글을 공유하는 것…."
        y 2a "기대했던 것보다 훨씬 재미있고 보람차네요."
        y "모니카 씨한테 고맙다는 말을 해야겠어요…."
        y "처음엔 다들 어색했던 거 같은데…."
        y 1a "하지만 이제 다들 서로가 어떻게 글을 공유하고, 다른 사람이 어떻게 생각하는지 보는 걸 즐기고 있는 것 같네요."
        mc "부정할 수 없겠는걸."
        mc "난 엄청 귀찮은 일이 될까봐 걱정했거든…."
        "하지만 나에겐 귀여운 여자아이들과 좋은 시간을 보낼 수 있는 좋은 수단이지."
        mc "하지만 다들 어떻게 글을 쓰는지 보는 게 되게 재미있어."
        mc "그리고 내가 직접 글을 쓰는 것도…."
        y 2a "으음…."
        y "뭔가 배우신 게 있나요, [player]?"
        mc "응?"
        y 2i "제가 글쓰기는 자기 자신과 접촉하기 위한 매우 개인적인 방법이라고 말씀드렸었죠…."
        y 1a "결국, 당신이 좋은 작가든, 나쁜 작가든 그건 크게 중요하지 않아요."
        y "그리고 제 의견도 그냥 의견일 뿐이에요."
        jump ch3_y_shared
    else:
        y 1e "…."
        y "…아."
        y "오늘은 뭔가 다른 걸 시도하려고 해보신 건가요?"
        mc "응."
        mc "괜찮아? 아니면 별로야?"
        y 2i "글쎄요. 둘 다 아니네요."
        y "전 제가 좋아하는 게 있어요."
        y "하지만 그걸 토대로 좋고 나쁜 것을 논하는 건 불공평한 짓이겠죠."
        jump ch3_y_shared

label ch3_y_good:
    if y_poemappeal[0] < 0 and y_poemappeal[1] < 0:
        jump ch3_y_bad12_shared
    if y_poemappeal[1] < 1:
        y "…."
        y 2u "[player] 씨…."
        y "…이건 정말 대단해요."
        y "당신이 여기에 감정을 쏟아부었다는 게 느껴져요."
        y "혹시 제가 어제 제안한 걸 시도해보셨나요?"
        mc "응, 맞아…."
        mc "네가 잘 설명해준 덕분이야."
        mc "감정을 더 넣는데 노력해봤거든."
        show yuri 4b zorder 2 at t11
        "유리는 눈에 띄게 침을 삼켰다."
        "심지어 손도 땀에 젖은 듯했다."
        play music t9 fadeout 1.0
        y "저는… 이런 것에 익숙하지 않아서…."
        mc "어떤 거에?"
        y 3o "저도 모르겠어요…!"
        mc "괜찮아, 진정해…."
        "유리는 심호흡을 하고 생각을 정리했다."
        "유리는 말하기 전에 오래 생각하는 성격이라는 걸 알고 있기 때문에, 조금 기다려주기로 했다."
        y 4a "네…."
        y "그냥…이런 식으로 누군가의 도움이 됐다는 것… 이려나요."
        y "아마 바보같이 들리실 수도 있겠지만…."
        y "하지만 제 글에 의해 동기부여가 된 누군가를 보면…."
        y "전 되게…."
        y "되게 행복해져요…."
        mc "혹시 그럼 이전에는 한 번도 글을 나눠본 적이 없다는 거야?"
        "유리는 끄덕였다."
        mc "진짜? 믿기지 않네."
        y "전 오직 저 자신만을 위해 글을 쓰거든요…."
        y "그리고…."
        y 3w "…사람들은 절 비웃을 테니까요!"
        mc "진짜 그렇게 생각해…?"
        "유리는 다시 끄덕였다."
        mc "허어…."
        mc "네 친한 친구들도?"
        y 2v "…."
        "어째서인지, 유리는 반응하지 않았다."
        mc "유리…?"
        label ch3_y_good_shared:
            if not renpy.music.get_playing(channel='music') == audio.t9:
                play music t9 fadeout 1.0
            "유리는 슬픈 미소를 지었다."
            y 1u "[player] 씨, 점심시간에 저는 혼자 밥을 먹어요."
            y "그거 알고 계세요?"
            y "조용한 곳을 찾아 책을 읽을 수 있는 아주 좋은 시간이죠."
            y "사실…."
            y 2s "저는 항상 책을 들고 다녀요."
            y "제가 책 읽는 걸 정말 좋아해서라고 말할 수 있겠지만…."
            y "…그렇게 말하는 게 낫겠네요."
            y "하지만…."
            y "책은 정말 놀랍고 영감을 주는 사람으로 가득해요."
            y "사랑에 빠지고 싶은 사람."
            y "친구를 잘 만드는 사람."
            y 1m "항상 얼굴에 미소를 잃지 않는 발랄한 사람…."
            y "아니면 생각이 깊은 사람이나 삶의 신비를 찾아 떠나는 사람들이 있죠."
            y "그래서 그렇게 생각해보면…."
            y "저는 매일 친구들에게 둘러싸여 있는거죠…."
            y "…그거 아세요?"
            y 2s "그리고 그 친구들은 저를 비웃지도 않죠…."
            y "항상 멍하니 있다고 놀리지도 않고…."
            y "제 체형에 대해 뭐라고 하지도 않고…."
            y "그리고…."
            y 3v "…제가 잘난 체한다며 싫어하지도 않죠!"
            mc "사람들이…너한테 그랬어?"
            y "저는 잘난 척한 적 없어요, [player] 씨!"
            y "오히려 반대에요, 저는 아무것도 아는 게 없어요!"
            y 4b "사람들에게 말 거는 법도 모르고."
            y "저를 정상적인 사람으로 보게 할 방법도 모르고."
            y "심지어 스스로 행복해지는 방법도 몰라요!"
            y "이 감정들을 가지고…."
            y "할 수 있는 건 읽고 쓰는 것뿐이었어요…."
            y "하지만 이젠 아니에요…."
            y 2s "당신과 공유하기 시작했잖아요…."
            y "…그동안 제가 뭘 놓친 건지 이해할 수 있게 됐어요."
            mc "근데 난 별로 한 게 없는데…."
            y "아니에요…."
            y "그건 아니에요."
            y "그저 인내심을 가지고 존중해주는 것…."
            y 3u "그게 정말… 저한테는 중요하거든요."
            y "제가 어려운 사람인 건 저도 알아요, [player] 씨…."
            y "말도 되게 느리게 하고…."
            y "항상 자신을 자책하고…."
            y "책을 너무 깊게 읽고…."
            y "하지만 매번…."
            y "당신은 저를 다른 사람들과 똑같이 대해줬죠."
            y "다른 사람과 이야기할 때 편안함을 느끼는 건 흔치 않은 일인데…."
            y "그래서 항상 당신과 얘기하면…."
            y 2s "…되게 행복해요."
            mc "그렇구나…."
            mc "나는 네가 마땅히 대접받아야 할 만큼 널 대할 거야."
            mc "만약 다른 사람이 그렇게 생각 안 한다면, 그냥 무시해버려."
            mc "솔직히, 나는 친구를 만들고 싶어서 이 동아리에 들어왔는데…."
            mc "적어도 한 명은 만든 거 같네."
            mc "그렇지?"
            y 4b "어, 음…."
            y "그렇게 말하시면…."
            y "…맞아요…."
            y 4e "저흰 이제 정말 친구죠, 그렇죠?"
            "유리는 머리에 손을 올린다."
            "하지만 이번엔, 밝은 미소를 짓고 있다."
            mc "네가 쓴 시, 봐도 될까?"
            y 3s "네."
            y "좋아요!"
            y "제가 가져다 드릴게요…."
        return
    else:
        y "…."
        y "[player] 씨."
        y 2s "며칠 만에 작문 실력이 나아지셨네요."
        y "지금까지 저한테 보여주신 모든 시가 다 굉장했어요."
        y "감정을 느낄 수가 있어요…."
        y 2m "심지어 조금 부럽기도 하네요…."
        y "저는 이런 식으로 자연스럽게 쓰지 못하거든요."
        mc "유리, 그렇게 말하면 안 돼."
        mc "이건 결코 나한테 자연스럽지 않아."
        mc "하지만 네 덕분에 많이 발전할 수 있었어."
        mc "내가 쫓던 본보기가 바로 너야."
        y 3u "그, 그런가요…?"
        "유리는 부드럽게 미소지었다."
        y "이 감정…."
        y "제 글을 공유할 기회가 있다는 게… 너무 기쁘네요."
        y 4e "이런 느낌일 줄은 몰랐는데…."
        mc "네가 어제 말했던 게 기억이 난다."
        mc "글 쓰는데 엄청 소질이 있는데 한 번도 다른 사람과 공유해본 적이 없다니."
        mc "그건 좀 애석한 일인 것 같아."
        y 2u "그럴지도 모르지만…."
        y "저한테 선택권이 있던 것도 아니였어요."
        mc "무슨 말이야…?"
        y "글쎄요…."
        jump ch3_y_good_shared


label ch1_m_start:
    m 1b "안녕, [player]!"
    m "좋은 시간 보내고 있니?"
    mc "아… 응."
    m 1k "좋아! 듣기 좋네!"
    m 4a "그나저나, 넌 아직 신입이니까…."
    m "새로운 활동이나, 어떻게 하면 좋겠다 등등… 동아리에 관해 제안할만한 게 있다면…."
    m 4b "언제든지 말해줘!"
    m "두려워하지 말고, 알았지?"
    show monika 4a
    mc "응… 기억해 둘게."
    "당연히 두렵지…."
    "익숙해질 때 까지는 가만히 있는 게 제일 좋은 거 같은데."
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
    $ nextscene = "m_" + poemwinner[0] + "_" + str(eval(poemwinner[0][0] + "_appeal"))
    call expression nextscene from _call_expression_8

    mc "난 여러가지를 시도해 보려고 해."
    mc "아직 확실한 걸 찾으려면 시간이 좀 걸릴 거 같거든."
    m 1k "그것도 괜찮아!"
    m 1b "네가 새로운 걸 시도하는 것도 보고 싶은걸."
    m "그게 너한테 맞는 스타일을 찾는 최고의 방법이야."
    m 3e "다들 자신의 스타일에 너무 편향되어 있을 수도 있지만…."
    m 3a "하지만 너한테 가장 맞는 걸 찾도록 항상 내가 도와줄게!"
    m "그러니까, 다른 사람의 스타일대로 쓰지 말고 너만의 스타일을 찾아봐."
    m "누군가에게 인상을 심어주거나 할 필요는 없으니까."
    m 5 "아하하!"
    mc "아하하…."
    m 1a "어쨌든, 내 시 읽어볼래?"
    m 1e "걱정하지 마, 나도 그렇게 잘 쓰는 건 아니라서…."
    mc "잘 쓰는 건 아니라는 사람치고는 꽤 자신감 있어 보이는데?"
    m 1j "음… 그건 내가 자신감 있도록 보여야 하기 때문이야."
    m 1b "그렇다고 해서 내가 항상 그렇다고 느끼는 건 아니야."
    show monika 1a
    mc "알겠어…."
    mc "뭐, 그럼 읽어볼까."
    return

label ch2_m_start:
    m 1b "안녕, [player]!"
    m "글 쓰는 건 어때?"
    mc "괜찮은 거 같은데, 아마도…."
    m 2k "그렇다면야 다행이고."
    m 2b "나빠지지만 않다면 상관없어~"
    m 2a "네가 점점 나아지고 있다는 게 되게 기뻐."
    m "조만간 명작을 쓰게 될지도 몰라!"
    mc "아하하, 설마…."
    m 2a "혹시 모르지!"
    m "오늘 쓴 거 나눠볼까?"
    mc "좋아, 여기."
    "난 모니카에게 내 시를 줬다."
    m "…."
    m "…좋아!"
    $ nextscene = "m_" + poemwinner[1] + "_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene from _call_expression_9

    m 1a "어쨌든…."
    m "내 시 읽어볼래?"
    m "난 되게 마음에 들던데, 너도 그랬으면 좋겠다~"
    mc "좋아, 한번 볼까."
    return

label ch3_m_start:
    m 2a "안녕, [player]~"
    m "축제 때 어떤 시로 낭송회에 나갈지 생각해본 적 있어?"
    mc "글쎄…."
    "동아리 애들 앞에서도 좀 그런데, 많은 사람 앞에서는…."
    mc "…조금 더 생각해봐야될 것 같아."
    m 2b "그래, 너무 부담 갖지는 말고!"
    m "네가 뭘 하든 간에, 분명히 잘 될 거야."
    m "내 맘에도 들거고."
    m 2k "아하하!"
    m 1a "어쨌든, 오늘의 시를 한번 볼까!"
    mc "응…."
    "나는 손에 들고 있던 시를 모니카에게 건네주었다."
    m "…."
    $ nextscene = "m_" + poemwinner[2] + "_" + str(eval(poemwinner[2][0] + "_appeal"))
    call expression nextscene from _call_expression_10

    m 1a "어쨌든…!"
    m "내 시를 보여줘야겠네."
    mc "으어…."
    mc "좋아…."
    return



label m_natsuki_1:
    m 2b "맘에 드는데, [player]!"
    mc "진짜…?"
    m 2e "내가 생각했던 것보다 훨씬 귀여운데?"
    m 2k "아하하하!"
    mc "하, 좀…."
    m 1b "아냐, 아냐!"
    m "나츠키 생각이 나는 시인데?"
    m "나츠키도 좋은 작가니까."
    m 5a "그러니까 칭찬으로 받아들여 줘!"
    mc "아하하…."
    mc "네가 그렇다면…."
    m "그럼!"
    m 1a "쉘 실버스타인이 쓴 책, 읽어본 적 있어?"
    mc "응?"
    mc "아마 엄청 오래전에…."
    m "어떤 이야기든 간단한 단어들로 풀어나가는 거로 유명해."
    m "그 사람의 시는 재밌고, 사랑스럽고, 심지어 슬프기도 하고…."
    m 3d "그리고 가끔은 그냥 몇 줄이 끝일 때도 있어."
    m "그냥 어린아이들을 위해 쓰인 시라고 생각할 수도 있지만, 생각해보면…."
    m "누구나 공감할 수 있는 세계관을 표현한 거지."
    mc "그렇구나…."
    mc "그럼 나츠키도 그런 부류란 말이야?"
    m 2a "비슷해."
    m "나츠키는 전문가는 아니지만…."
    m "아마 나츠키의 시가 별 의미 없어 보일 수도 있어."
    m "글을 쓰기에는 쉬워 보이지만, 그 의미를 이해하는 데는 엄청 어려워."
    m 2b "그렇게 시의 세계를 모험하는 거지!"
    return

label m_sayori_1:
    m 2a "이거 마음에 든다!"
    m "사요리가 좋아할 만할 거 같은데."
    mc "그래?"
    m 2d "너랑 사요리는 엄청 친한 친구잖아?"
    m "시 쓰는 것에도 비슷한 점이 있는게, 그렇게 놀랄 일은 아니긴 하네."
    mc "아, 글쎄…."
    mc "우리가 친한 친구긴 하지만, 나랑 사요리는 많이 다르거든."
    m "흐음…."
    m "글쎄, 그럴지도 모르지."
    m 3a "하지만 네가 모르고 있었던 비슷한 점들이 있을 거야."
    m "사요리가 너에 대해 말하는 방식을 보면…."
    m "너희 둘은 정말 서로에 대해 신경쓰는 것 같아"
    m "다른 방식으로 보인다고 해도, 끝맺음은 네가 생각하는 것보다 더 비슷할 거야."
    m 1a "그래서 내가 네 시를 읽을 때 그렇게 느낀 거 같아."
    mc "흐음…."
    mc "너무 깊게 생각하고 읽은 건 아니지?"
    m 5 "아하하! 그럴 수도 있겠네!"
    m "아, 나 유리같이 들리네…."
    m 2a "…뭐 어쨌든, 사요리의 시는 부드러운 느낌이 있어."
    m "분명 사요리가 행복이나 슬픔 같은 감정들을 탐험하는 걸 좋아한다고 할 수 있겠지."
    m "그렇게 행복해 보이는 아이가 슬픈 것들도 즐길 줄 누가 알았겠어?"
    mc "맞아… 완전 예상 밖이였지."
    m 2j "뭐, 사람마다 다른 거니까~"
    m 2a "너도, 실험적인 걸 너무 두려워하지 마."
    return

label m_yuri_1:
    m 1a "좋은데, [player]!"
    m "읽고 있는 동안 머릿속이 ‘우와’였어"
    m 1j "되게 은유적인데!"
    m 1a "네가 이렇게 감정이 깊은 시를 쓸 줄은 몰랐어."
    m 3b "내가 널 너무 과소평가했나 봐!"
    mc "모든 사람들이 기대 안 하게 만드는 게 내가 가장 잘 하는 일이야."
    mc "그렇게 하면, 조금만 노력해도 사람들에게 칭찬을 들을 수 있어."
    m 5a "아하하! 그건 좀 불공평한걸!"
    m "뭐, 잘된 건 알겠지만."
    m 2a "유리가 이런 글 좋아하는 거 알지?"
    m "막 이미지화되고 상징성으로 가득한 글."
    m 2d "행복과 슬픔을 묘사하기 위해 간단하고 직접적인 단어를 쓰는 사요리랑은 다르게…."
    m "유리는 독자들이 직접 자신만의 의미로 해석하도록 하는 걸 좋아해."
    m 4d "그리고 그걸 효과적으로 쓰는 건 굉장히 어려워."
    m "감정만으로 뭔가 느끼게 한다던가…."
    m "차근 차근 읽어 봐야 이해가 되게 한다던가."
    m "수년의 연습이 필요해. 유리는 벌써 하고 있지만 말야."
    m 1e "그러고 보니 딱히 물어본 적은 없지만."
    mc "그렇다면, 난 그 발끝에도 못 미치겠네…."
    m 2b "에이, 그런 말 하지마!"
    m "넌 네 걸 하면 되는 거잖아."
    m "계속 탐구하고, 새로운 걸 시도하면서 배우는 거야!"
    return

label m_natsuki_2:
    m 1j "좋은데~"
    m 1a "나츠키랑 시간을 좀 같이 보냈나봐?"
    m "나츠키의 문체와 비슷한데."
    mc "아, 응…."
    mc "이야기를 전개하는데 좋은 방법인 거 같아서."
    m 2a "음, 나도 동의해."
    m "나츠키가 쓴 시는 귀여워 보이지만, 의미가 깊기도 하지."
    m "네가 왜 그런 스타일에 빠졌는지 알 거 같기도 해."
    m "그 말인즉슨 넌 유리의 시는 별로 안 좋아한다는 뜻이겠지?"
    mc "아, 그런 뜻은 아닌데…."
    mc "난 모두의 시를 좋아해."
    m 2d "그러겠지만, 다른 사람들보다 훨씬 나츠키의 시가 좋잖아?"
    m "유리는 너무 복잡한 단어와 상징화를 쓰고…."
    m "사요리는 행복이나 슬픔을 표현하는데 굉장히 직설적인 방법을 쓰고."
    m 2a "너한테 마음에 드는 게 있지?"
    m 4l "뭐, 이게 대회나 그런 건 아니지만!"
    m 4a "그냥 궁금해서 그랬어, 그게 다야."
    return

label m_sayori_2:
    m 1j "꽤 좋은데~"
    m 1a "네가 썼던 다른 것처럼 사요리가 생각나는데?."
    m 4b "너희 진짜 환상의 콤비다!"
    mc "아하하… 그건 좀 과장이다."
    m 2a "뭐, 그럴지도 모르지."
    m "하지만 동아리에서도 사요리랑 많은 시간을 보내고 있잖아?"
    m 2j "뭐, 네가 수줍어한다고 해도 뭐라고 안 할게~"
    mc "ㅂ, 부끄럽지 않아! 난 그냥…."
    m 5 "아하하! 그냥 장난이었어."
    m "모든 사람하고 친구가 되려면 시간이 좀 걸릴 거야."
    m 2d "하지만 유리랑 나츠키는 재미있는 애들이니까, 너무 두려워하지 않아도 돼!"
    m "그리고 가끔씩 나한테 와서 말 걸어도 되고…."
    m 1e "뭐 나한테 접근할 수 없다거나 그런 건 아니니까… 아닌가?"
    mc "아, 아니. 그런 게 아니라…."
    mc "여기에 있는 게 좀 익숙해져야 할 거 같아서."
    m 1a "그래…."
    m 1l "내가 만약 압박을 줬거나 그랬다면 미안해!"
    m "그런 뜻은 아니였어."
    mc "아니야, 걱정하지 마."
    mc "무슨 말인지 알겠어."
    m 1a "그래, 좋아~"
    return

label m_yuri_2:
    m 2b "이거 괜찮다!"
    m "네 문체가 점점 안정적이 되는 것뿐이 아니라…."
    m "전에 읽었던 것보다 더 이미지화가 잘 되어있어!"
    m 2a "궁금해서 그러는데, 혹시 유리의 문체에서 영감을 얻었니?"
    mc "흐음…."
    mc "그런 거 같아."
    mc "유리한테 재능이 있다는 건 부정할 수 없을 거야."
    m 4k "응, 당연하지!"
    m 4a "내 생각엔 유리의 시가 가장…."
    m "…낭만적인 거 같아."
    m 1a "이렇게 말하는 게 가장 좋은 거 같아."
    m 1d "유리는 펜만 들면 완전히 다른 사람이 되니까…."
    mc "맞아, 그런 거 같아."
    mc "아니면 문학에 관해서 얘기할 때, 유리 마음속의 불이 켜지는 거 같아."
    m 2a "음!"
    m "안타깝게도, 유리와 사적인 대화를 많이하는 건 어렵지…."
    m 2m "믿어줘, 나도 시도해봤어…."
    m "유리의 머릿속에서 무슨 일이 일어나고 있는지 누가 알겠어?"
    mc "나쁜 뜻으로 얘기하는 건 아니지?"
    m 1g "아니지, 당연히 아니지!"
    m "난 그냥 유리가 너무 자신을 숨기는 게 아닌가해서…."
    m 1e "그래도, 그렇게 보호해주려는 거 보니까…."
    m 5 "꽤 푹 빠져있나보구나…."
    mc "뭐?!"
    mc "ㄴ, 너 지금 완전히 오해하고 있어!"
    m "아하하! 진정해, 농담이니까!"
    m 2a "그리고, 이미 남자친구 있을걸…."
    mc "잠깐, 진짜?"
    m 2k "응. 가상이겠지만."
    "모니카는 마지막 말은 거의 속삭였다."
    m 5 "그냥 예감일 뿐이지만…."
    mc "…뭐, 거기에 문제는 없는 거 같은데"
    m 1n "아, 나도 알지…!"
    m "그냥 말해본 거야~"
    return

label m_natsuki_3:
    m 2j "한 번 더 나츠키 스타일로? 그렇구나~"
    m 2d "흐음…."
    m "너, 진짜 나츠키를 좋아하나 보네?"
    mc "응? 그건…."
    m 5 "음, 제발 [player]."
    m "너 진짜 의심스럽거든?"
    m "매일 부실에서 나츠키랑 같이 있고…."
    m "나츠키가 빠져있는 만화를 좋아하는 척하고…."
    mc "ㄴ, 네가 나츠키에 대해 얼마나 잘 알아…!"
    mc "나츠키를 기쁘게 하지 않으면, 결국 걔는 날 싫어하게 될 걸."
    m 2e "에?"
    m 2a "아냐, 내 생각엔 네가 잘못 알고 있는 거 같아, [player]."
    m "나츠키는 자기가 원하는 걸 해주지 않는 사람을 싫어하는 건 아니야."
    m 2d "자기주장이 강하긴 하지만, 그렇게 이기적이진 않아…."
    m "사실, 나츠키를 제멋대로 하게 만든 건 너라고 생각하는데."
    mc "그런가…."
    "한편으로 알고 있기는 했지만, 인정 하고 싶지는 않았다."
    m "그러니까, 하나만 말해둘게…."
    m 1e "…제발, 조심해."
    m "나츠키는 예측할 수 없는 사람이야."
    m "대부분 자기가 뭘 원하는지도 모르고."
    m 1i "뭐가 됐든, 여기서 가장 어린아이니까."
    m "자신의 감정을 적절하게 조절하는 법을 모를 수도 있어."
    m "내가 무슨 말 하는 거냐면…."
    m 1m "만약 나쁜 일이 일어난다면, 그게 동아리에도 해가 될 수가 있어…."
    m 5 "나한테 그러진 않을 거지…?"
    mc "그건…."
    "모니카한테 어떻게 반응해야 할지 모르겠다."
    "내가 나츠키와 동아리에 관심이 있는데, 그런 말을 꺼내는 건 조금 불공평한 거 아닌가…."
    m "뭐, 너는 똑똑하니까."
    m "너는 옳은 일을 할 거라고 생각해."
    "모니카는 달콤하게 미소지었다."
    return

label m_sayori_3:
    m 1k "아하하."
    m "되게 웃기다…."
    mc "…그래?"
    m 1a "아니, 아냐. 시가 아니라…."
    m 2a "어떻게 날이 갈수록 네가 쓴 시랑 사요리가 쓴 시랑 이렇게 비슷해질 수가 있나 해서."
    m "네가 그렇게 사요리와 조화를 이룬다니 놀랍네."
    m 2d "그리고 최근에도 많은 시간을 보내고 있잖아, 그렇지?"
    mc "아, 그렇게 말할 수 있겠지…."
    mc "친한 친구로 자라왔지만, 작년에 그렇게 사요리를 많이 보지는 못 했거든…."
    mc "하지만 동아리에 들어온 이후로, 우린 다시 많은 시간을 보낼 수 있게 됐어."
    m 1a "응, 응~"
    m "아, 그걸 들으니까 생각난 건데…."
    m "사요리가 오늘 좀 안 좋아 보여서 말이야…."
    mc "그래? 걔가 뭔가 말해줬어?"
    m 1n "아…."
    m "글쎄…."
    m 2l "[player], 사요리를 함부로 대하거나 한 건 아니지?"
    mc "다, 당연히 아니지!"
    mc "난 늘 하듯이 대했는데."
    m 2a "알았어."
    m 5 "그냥 확실하게 하려고 한 거야~"
    m "네가 얼마나 사요리를 신경쓰는지…."
    m "사요리한테 나쁜 일이 생긴다면 아주 끔찍한 결과가 일어날 테니까, 잘 지켜보고 있어."
    m 2d "네가 동아리에 들어오고 나서 엄청 행복해했었는데."
    m "어쩌다 이렇게 된 걸까…?"
    mc "…."
    m 1l "…뭐, 신경쓰지 말자."
    m "지금은 이런 얘기를 할 때가 아니니까…."
    return

label m_yuri_3:
    m 2e "점점 시가 세련되지는데, [player]."
    m "유리가 많은 걸 가르쳐줬나 봐?"
    mc "글쎄…."
    mc "그런 거 같네."
    m 2a "그래… 네가 얼마나 유리랑 많은 시간을 보냈는지 알고 있으니까."
    m 2d "내 생각엔 내가 요 며칠 동안 유리가 말한 걸 들은 게 아마 1년 동안 말한 거보다 많을 걸."
    m "네가 어떻게 했는지는 잘 모르겠지만, 꽤 인상적이네…."
    mc "글쎄, 그냥 조금 기다려주고 생각할 시간을 줘서인 거 같은데…."
    mc "점점 요령을 터득하고 있는 거 같아."
    m 2a "흠…."
    m "정말 많은 노력을 하고 있구나."
    m 2e "유리를 진짜 좋아하나 보네."
    mc "응? 그건…."
    m 5 "아하하!"
    m "너 진짜 의심스럽거든?"
    m "매일 부실에서 유리랑 같이 있고…."
    m "그 신랄한 소설을 매일 같이 읽고…."
    mc "난…!"
    mc "난 그냥… 유리가 다른 사람과 어울리는 걸 힘들어하는 게 안쓰러워서…."
    mc "유리를 혼자 있게 두는 게 싫었거든."
    mc "게다가, 소설도 그렇게 나쁘지는 않고…."
    m 1k "알았어, 알았어~"
    m "나도 이해해."
    m 1a "그냥… 조심하라고."
    m "유리가 자기 자신을 여는 데 익숙하지 않다는 거 알아…."
    m 2d "유리는 연약하니까, 만약 나쁜 일이 생긴다면…."
    m "유리한테는 정말 힘들 거야."
    m 2i "책이 유리를 완전히 치료해주는 게 아니야."
    m "그냥 반창고일 뿐이야."
    mc "내가 유리를 해칠 거처럼 말하네…."
    m 1l "미안, 그런 뜻은 아니였는데~"
    m "혹시라도, 실수로 자기 자신을 다치게 할 수 있으니까."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
