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

label yuri_exclusive2_1:
    scene bg club_day
    with wipeleft_scene
    "유리와 조금 더 대화하고 싶다…."
    "그래도 책 읽는 걸 방해하고 싶지는 않아."
    "난 잠깐 유리가 읽고 있는 책의 표지를 보았다."
    "나한테 빌려줬던 책이랑 같은 책이다…."
    "그것보다, 책의 페이지를 보아 읽은 지 얼마 안 된 것 같다."
    play music t6 fadeout 1.0
    show yuri 4a zorder 2 at t11
    y "아…."
    "젠장…."
    "내가 자기를 보고 있다는 걸 눈치챈 것 같다…."
    "유리는 나를 흘낏 보더니, 우리의 눈동자는 잠깐 몇 초 동안 마주쳤다."
    y 4b "…."
    "그러나 그건 책 속으로 유리의 얼굴을 더 파묻게 할 뿐이었다."
    mc "미안…."
    mc "그냥 잠시 넋 놓고 있었어…."
    "뭔가 유리의 기분을 언짢게 만든 것 같은데."
    y oneeye "아…."
    y "괜찮아요…."
    y "눈치채지 못 한건 제 잘못이니까요…."
    y "무슨 일이신가요…?"
    mc "그거, 나한테 빌려줬던 책이네, 그치?"
    y "네."
    y "몇 군데를 다시 읽고 싶어져서…."
    y 2q "다른 이유는 아니에요…!!"
    mc "그냥 궁금해서 그런데, 왜 같은 책을 두 권이나 갖고 있는 거야?"
    y "아…."
    y "어제 잠시 서점에 들렀다가…."
    y 3o "아, 그게 아니라…."
    y "그게…."
    y 1w "어쩌다보니… 두 권을 사게됐어요."
    mc "아, 그렇구나."
    "분명히 유리가 나한테 말하지 않은 게 있겠지만, 신경 쓰지 않기로 했다."
    mc "조만간 꼭 읽기 시작할게!"
    y 2u "좋아요…."
    y "한번 읽기 시작하면, 계속 읽게될 거에요."
    y 2c "스토리가 굉장히 매력적이거든요."
    mc "그래?"
label yuri_exclusive2_1_ch22:
    mc "뭐에 관한 스토리야?"
    y 1f "그게…."
    y "음…."
    "난 책의 표지를 보았다."
    "책의 제목은 \"마르코프의 초상화\"."
    "앞표지에는 불길해 보이는 커다란 눈이 인쇄되어있었다"
    y 1a "기본적으로 인체실험소로 바뀐 종교집단 얘기인데요…."
    y "거기 갇힌 사람들은 죄다 피에 미친 살인 기계로 변했어요."
    y 1m "거기다 시설은 점점 나빠져서, 팔다리를 잘라서 사람들에게 먹이기 시작했고 그것들을 붙여…."
    y 1q "아, 이 뒤는 스포일러라서…."
    y 3q "어쨌든, 전 이거에 엄청 푹 빠져있어요"
    y 3n "…아, 물론 책이요!"
    y 3q "팔 자르거나 하는 거에 빠진 게 아니라…."
    mc "그건 너무…!"
    "그건 너무 무거운 스토리 아냐?"
    "뭔가 무난한 스토리일 거라고 생각해서인지, 공포감이 갑작스레 찾아왔다."
    y 1s "아…."
    y "이런 거 별로 안 좋아하시나 봐요, [player] 씨?"
    mc "아니, 그런 건 아닌데…."
    mc "이런 걸 좋아하게 될 수도 있으니까… 뭐."
    y 2u "그랬으면 좋겠네요…."
    "그래… 유리가 이런 장르를 좋아한다는 걸 잊고 있었다"
    "유리는 외견상으로는 수줍음 많고 겁이 많아 보이지만, 속은 그렇지 않다는 걸."
    y "뭐, 그런 스토리에요…."
    y 1a "자신의 인생을 새로운 관점에서 보라고 도전장을 내미는 것과 같죠."
    $ style.say_dialogue = style.normal
    y "끔찍한 일은 꼭 누군가가 악을 자청해서 일어나는 게 아니라…."
    $ style.say_dialogue = style.edited
    y "어쨌든 세상은 끔찍한 사람들로 가득하고, 우린 아무 짝에도 쓸모 없어요."
    $ style.say_dialogue = style.edited_nobreak
    y "그런데, 갑자기ㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣㅣ{nw}"
    $ style.say_dialogue = style.normal
    y 3v "저, 저 지금 또 횡설수설하면서…!"
    y "또 이러다니…."
    y 4b "죄송해요…."
    mc "아냐, 사과하지 않아도 돼…!"
    mc "흥미를 잃었다든가 한 건 아니니까."
    y "그런가요…."
    y "그렇다면 괜찮겠지만…."
    y 4a "그래도 한 가지 알아주셨으면 해요…."
    $ style.say_dialogue = style.normal
    y "책이나 글로 제 생각들을 채울때…."
    $ gtext = glitchtext(24)
    $ style.say_dialogue = style.edited_nobreak
    y "제 몸 전체가 흥[gtext]{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()
    y "다른 사람이랑 얘기하고 있었다는 걸 금방 잊어버리는 버릇이 있어서…."
    y 3t "제가 만약 이상한 소리를 했다면 사과드릴게요!"
    y "그리고 제가 너무 말을 많이 한다 싶으면 말씀해주세요…!"
    mc "흐음."
    mc "내 생각엔 별로 걱정할 필요 없을 거 같아."
    mc "그걸 다르게 얘기하면 그만큼 독서에 열정이 있다는 얘기니까."
    mc "난 그걸 들어주는거고."
    mc "결국 여기는 문예부니까…."
    y 4a "아…."
    y "그건…."
    y "맞는 말이네요…."
    mc "그럼 그냥…."
    mc "내가 읽어보면 되는 거잖아?"
    play sound "sfx/glitch3.ogg"
    y dragon "네, 맞아요!"
    y 3n "아니 제 말은… 그러실 필요까지는 없어요!"
    mc "아하하, 무슨 말이야?"
    y 3o "…."
    mc "책 좀 잠시만…."
    "난 가방 안에 들어있던 책을 꺼내들었다."
    mc "좋아… 여기 앉아도 되는 거지?"
    "나는 유리의 옆 자리에 앉았다."
    y 3n "아…!"
    y "네…."
    mc "괜찮아"
    mc "조금 불편해 보이는데…."
    y "그게…."
    y 4b "죄송해요…."
    y "불편한 게 아니라…."
    y "단지 누군가와 같이 책을 읽는다는 게…."
    y "익숙치가 않아서요…."
    mc "그래…."
    mc "내가 방해가 된다거나 그럼 얘기해줘."
    y "네…."
    show yuri zorder 1 at thide
    hide yuri
    "난 책을 열고 프롤로그를 읽기 시작했다."
    "난 유리가 말하는 책을 같이 읽는 것의 의미를 바로 알 수 있었다."
    "책을 읽고있지만 어깨 너머로 유리의 존재가 느껴진다는 것."
    "그건 딱히 나쁜 것은 아니다."
    "조금 불편할 수도 있지만, 오히려 편안함이 느껴진다."
    "유리는 내 옆에 있다."
    "나는 유리가 책을 보고있는 게 아니란 걸 알 수 있었다."
    "나는 슬쩍 유리를 바라보았다."
    "유리는 지금 책 대신에 다른 걸…."
    show yuri 3n zorder 2 at t11
    y "죄… 죄송해요."
    $ style.say_dialogue = style.normal
    y "전 그냥{nw}"
    $ style.say_dialogue = style.edited
    y "전 그냥{fast} 당신의 체온에 목ㄱㄱㄱㄱㅇㅇㅇㅇ{nw}"
    $ style.say_dialogue = style.normal
    $ _history_list.pop()

    mc "너 진짜 사과 많이 하는구나?"
    y "그런가요?"
    y 4a "저는… 그게…."
    y "죄송해요…."
    y 4c "또 사과해버렸어요…."
    mc "아하하."
    mc "여기, 이러면 되겠지?"
    "난 내 책상을 유리의 책상 옆에 붙였다."
    y 2v "아…."
    y "된 거 같네요…."
    "유리는 소심하게 자기 책을 덮었다."
    "난 몸을 살짝 기울일때마다 유리의 어깨가 닿는 걸 느낄 수 있었다."
    "내 왼쪽 팔이 방해되는 것 같아서 나는 내 오른손으로 책을 폈다."
    mc "아, 페이지 넘기는 게 좀 불편한데…."
    y "이러면…."
    $ persistent.clear[2] = True
    scene y_cg1_base with dissolve_cg
    "유리는 왼팔로 책의 왼쪽을 잡았다."
    mc "아…."
    "나는 오른팔로 책의 오른쪽을 잡았다."
    "내가 페이지를 넘길 때마다, 유리는 엄지손가락으로 페이지를 받아 눌렀다."
    "이러고 있으니까…."
    "전보다 더 유리와 가까워진 느낌이 든다."
    "괜히 긴장되는데…!"
    "유리의 체온이 여기까지 느껴지는 것 같다…."
    show y_cg1_exp1 at cgfade
    y "…괜찮나요?"
    mc "어?"
    y "다음 페이지…."
    mc "아… 미안!"
    mc "잠시 다른 생각을 하고있었어…."
    "내가 다시 유리의 얼굴을 보자, 우리의 눈은 마주쳤다."
    "내가 어쩌다 유리와 이렇게까지 됐을까…."
    y "아…."
    show y_cg1_exp2 at cgfade
    y "괜찮아요."
    y "독서를 잘 안 해봤다고 하셨죠?"
    y "조금 오래 걸리셔도 기다릴게요…."
    y "이게 아마 제가 할 수 있는 최선이겠죠…."
    y "저도 기다려주셨으니…."
    mc "응…."
    mc "고마워."
    hide y_cg1_exp1
    hide y_cg1_exp2
    "우리는 계속 읽어나갔다."
    "유리는 내가 다음 페이지로 넘겨도 되겠냐는 말을 더는 하지 않았다."
    "그 대신 난, 유리가 나보다 먼저 읽었다고 가정하고 페이지를 넘겼다."
    "우리는 침묵속에 첫 장을 다 읽었다."
    "페이지 한장 한장 넘기는 게 친근한 대화같이 느껴진다…."
    "난 엄지로 부드럽게 페이지를 넘겼다"
    mc "저기, 유리…."
    mc "조금 바보같이 들릴 수 있겠지만…."
    mc "이 주인공이 너랑 좀 닮은 거 같아."
    show y_cg1_exp3 at cgfade
    y "에??"
    y "아, 아니에요!! 전 이 주인공이랑 관련이 하나도 없어요!"
    y "절대 아니에요!"
    mc "정말…?"
    mc "그냥 이 주인공이 말할 때 조심히 말하는 걸 얘기하려는 거였는데…."
    show y_cg1_exp1 at cgfade
    y "아, 아…."
    y "그런 얘기였군요…."
    hide y_cg1_exp3
    hide y_cg1_exp1
    show y_cg1_exp2 at cgfade
    y "죄송해요…."
    y "그녀의 다른 점을 얘기하는 줄 알았어요."
    mc "다른 점…?"
    hide y_cg1_exp2
    show y_cg1_exp3 at cgfade
    y "시, 신경쓰지 마세요!"
    y "저희 아직 거기까진 안 읽었으니까…."
    y "왜 갑자기 머릿속에 떠올랐는지 모르겠네요…."
    y "아하하!"
    mc "유리, 괜찮아?"
    hide y_cg1_exp3
    show y_cg1_exp1 at cgfade
    y "에…?"
    "읽기 시작했을 때부터 유리가 안절부절못하는 것 같은데…."
    mc "아프거나 힘들면 쉬어도 돼."
    mc "네 숨소리가 좀…."
    y "제 숨소리요…?"
    hide y_cg1_exp1
    "유리는 자신의 가슴에 손을 얹어 심장박동을 확인하는 듯 했다."
    y "아……모르고 있었네요…."
    show y_cg1_exp3 at cgfade
    y "…어쨌든, 괜찮아요!"
    y "물 좀 마시고 올게요…!"
    mc "알았어…너무 무리 하지는 마."
    scene bg club_day
    with dissolve_cg
    "유리는 자리를 박차고 일어나 교실에서 뛰쳐나갔다."
    mc "방금 도대체 뭐지…?"
    show monika 1d zorder 2 at t11
    m "[player]?"
    m "지금 무슨 일이 일어난거야?"
    mc "응?"
    mc "모르겠어…."
    mc "유리가 좀 이상한 거 같아서…."
    m 1r "아무것도 모른다는 거지…."
    mc "응, 모르겠어…."
    mc "걱정되는 거야?"
    m 1a "아, 아니. 그런 건 아냐."
    m "네가 유리한테 아무것도 안 했나 물어보는거야."
    mc "아냐, 아무것도 안 했어!"
    m 5 "아하하, 걱정하지 마… 난 널 믿어, 바보야."
    m "유리는 가끔 이러니까, 너무 안 놀라도 돼."
    mc "알았어…네가 그렇다면 그런거겠지."
    m 2b "그것보다, 서로 시 나눠보지 않을래?"
    mc "응?"
    mc "유리 안 기다려도 돼?"
    m 2a "뭐, 좀 걸릴테니까, 그래서 없이 해도 될 거 같아."
    m "괜찮지?"
    mc "응, 그냥 물어본 거였어…."
    "나는 일어났다."
    "나는 내가 책을 어디까지 읽었는지 머릿속에 기억해두고 책을 가방에 넣었다."
    $ y_ranaway = True
    return

label yuri_exclusive2_2:
    $ y_exclusivewatched = True
    play music t6 fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    mc "여, 유리."
    show yuri 2f zorder 2 at t11
    y "네?"
    mc "아…."
    "유리가 읽고있는 책이 우리가 같이 읽었던 책이 아닌 다른 책이였다는 걸 알 수 있었다."
    mc "아, 미안! 방해하려고 했던 건 아닌데…."
    y 2m "아니에요…."
    y "기다리고 있었을뿐이에요…."
    show yuri 2a
    mc "아, 그렇다면…."
    mc "자, 그럼 시작해볼까?"
    y 2c "네, 그러죠!"
label yuri_exclusive2_2_ch22:
    y 3a "사실, 부탁이 있는데요…."
    y "… 그 전에 차를 내와도 될까요?"
    mc "그래, 좋아."
    y 1c "고마워요"
    y 1a "책 읽는데는 따뜻한 차 한 잔만한 게 없으니까요."
    y "어디 보자…."
    show yuri zorder 1 at thide
    hide yuri
    "유리는 일어나 벽장 앞으로 갔다."
    "난 유리가 선반에서 작은 물 주전자를 찾는 것을 지켜보았다."
    show yuri 1f zorder 2 at t11
    y "잠시만 기다려 주시겠어요?"
    mc "응…."
    "유리는 나에게 물 주전자를 건네주고, 커피포트를 가져왔다."
    y "이걸 선생님 책상에 꽂고 올 테니, 그때 같이 물을 받으러 가죠."
    show yuri zorder 1 at thide
    hide yuri
    "유리는 내 앞을 지나 탁상 위에 주전자를 올려놓았다."
    "나는 간단하게 유리의 행동을 지켜봤다."
    "놀랍게도, 유리의 행동거지는 평소 유리의 말투와는 정반대였다."
    "특히나, 유리의 긴 다리 때문인지, 유리는 우아하고 성숙해보였다."
    show yuri 1f zorder 2 at t11
    y "좋아요, 주전자 좀 건네주시겠어요?"
    y 1a "금방 다녀올게요"
    mc "저, 같이 가도 돼?"
    y 1q "괜찮아요…!"
    y "여기 계세요…."
    y "얼마 안 걸려요."
    show yuri zorder 1 at thide
    hide yuri
    "주전자를 손에 들고, 유리는 급하게 교실을 나갔다."
    show monika 2i zorder 2 at t11
    m "아…."
    m "또 유리가 널 혼자 둔거야?"
    mc "아냐 , 이번엔 그렇지 않아."
    mc "주전자에 물을 채우러 나갔어."
    m 5 "아하, 알겠어!"
    m "오해해서 미안해~"

    scene bg club_day
    with wipeleft_scene

    "…."
    "10분이 지났다."
    "얼마 안 걸릴 거라고 했는데…."
    "뭔가 문제라도 생긴걸까?"
    "마냥 기다리기도 지루해서, 유리를 따라가기로 마음 먹었다."
    scene bg corridor
    with wipeleft_scene
    $ currentpos = get_pos()
    play music "<from " + str(currentpos) + " loop 10.893>bgm/6o.ogg"
    mc "어디 보자…."
    "유리가 있을 만한 가장 상식적인 곳은 수돗가겠지…."
    $ y_name = "유리"
    "난 복도를 따라 쭉 걸어갔다."
    $ y_name = "???"
    y "하아……하아…."
    y "….하아……하아…."
    "…무슨 소리지?"
    "구석에서 나는 소리인가…?"
    "숨소리가 나는 것 같은데."
    y "쓰읍…."
    "누군가 자신의 치아 사이로 숨을 들이쉬는 듯한 날카로운 숨소리가 났다."
    "누군가 다친 건가…?"
    "나는 구석 쪽으로 가 주변을 둘러봤다."
    mc "유리…?"
    $ y_name = "유리"
    show yuri cuts zorder 2 at t11
    y "꺄아…!"

    $ currentpos = 45.264 - (get_pos() / 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " to 39.817 loop 0>bgm/6r.ogg"
    play music t6r
    show yuri zorder 1 at thide
    hide yuri
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    $ y_name = "???"
    mc "{cps=*3}유리…?{/cps}{nw}"
    "{cps=*3}나는 구석쪽으로 가 주변을 둘러봤다.{/cps}{nw}"
    "{cps=*3}누가 다친건가…?{/cps}{nw}"
    "{cps=*3}누군가 자신의 치아 사이로 숨을 들이쉬는듯한 날카로운 숨소리가 났다.{/cps}{nw}"
    y "{cps=*3}쓰읍…{/cps}{nw}"
    "{cps=*3}숨소리가 나는 것 같은데.{/cps}{nw}"
    "{cps=*3}구석에서 나는 소리인가…?{/cps}{nw}"
    "{cps=*3}…무슨 소리지?{/cps}{nw}"
    y "{cps=*3}….하아……하아…{/cps}{nw}"
    y "{cps=*3}하아……하아….{/cps}{nw}"
    $ y_name = "유리"
    "{cps=*3}난 복도를 따라 쭉 걸어갔다.{/cps}{nw}"
    "{cps=*3}리가 있을만한 가장 상식적인 곳은 수돗가겠지…{/cps}{nw}"
    mc "{cps=*3}어디 보자…{/cps}{nw}"
    window hide(None)
    window auto
    scene bg club_day
    show noise zorder 100 at noise_alpha
    show vignette zorder 100 at vignetteflicker(-2.030)
    show layer master at rewind
    "{cps=*3}마냥 기다리기도 지루해서, 유리를 따라가기로 마음 먹었다.{/cps}{nw}"
    "{cps=*3}뭔가 문제라도 생긴걸까?{/cps}{nw}"
    "{cps=*3}얼마 안 걸릴 거라고 했는데….{/cps}{nw}"
    "{cps=*3}10분이 지났다.{/cps}{nw}"
    "{cps=*3}…{/cps}{nw}"

    $ del _history_list[-37:]
    if poemwinner[0] == "yuri" and chapter == 3:
        jump yuri_exclusive2_2_ch23
    $ currentpos = 90.528 - (get_pos() * 2.0)
    $ audio.t6r = "<from " + str(currentpos) + " loop 10.893>bgm/6.ogg"
    play music t6r
    hide noise
    hide vignette
    show layer master
    show yuri 1a zorder 2 at t11
    y "다녀왔어요."
    y "기다려주셔서 고마워요."
    y "[player] 씨, 우롱차 좋아하세요?"
    mc "아, 응."
    mc "뭐든 괜찮아."
    y "알겠어요."
    "유리는 물의 온도를 100도로 맞췄다."
    y 1f "자, 이제 찻주전자를 가져올 시간이네요."
    mc "정말 성의를 다 하는구나?"
    y 1u "물론이죠…."
    y "남한테 차를 끓여줄 때는 하나라도 놓치면 안 돼요."
    mc "내가 차 매니아가 아니어도…?"
    y 2m "후후."
    y 2a "그렇다면 더 감명 받으시겠네요."
    mc "응… 그럴 것 같네!"
    show yuri zorder 1 at thide
    hide yuri
    "유리는 잔에 물을 붓고 찻잎을 우리기 시작했다."
    "조용히 콧노래까지 부르기까지 시작했다."
    show yuri 1c zorder 2 at t11
    mc "기분 좋아 보이네…."
    y 1a "그런가요?"
    y "그냥 보여주고 싶었어요…."
    y "그리고 알아주길 바랬어요."
    y 2u "생각해봤는데…."
    y "자기 자신을 좀 더 표현해야겠다고 생각했거든요."
    y "그렇게 어려운 일은 아니니까요…."
    y 1c "당신이 곁에 있을 때는 말이에요."
    show yuri 1a
    mc "아…."
    mc "그거 좋네!"
    mc "너무 무리하지는 마."
    y 3u "[player] 씨는 항상 제 걱정을 해주시네요."
    y "정말 사랑스러워요."
    mc "그건…."
    "농담하는 것 같지가 않다…."
    "이렇게까지 될 거라곤 생각도 못 했는데…!"
    "유리는 각각의 잔에 차를 따랐다."
    y 1a "[player] 씨, 부탁이 한 가지 더 있는데요…."
    y "오늘은 바닥에 앉는 게 어때요?"
    mc "응? 갑자기 왜?"
    y 1h "등에 무리가 덜 가거든요…."
    y "책상에 앉아서 읽는 거보다 벽에 등을 기대고 앉아서 읽는 게 더 좋아요."
    mc "아, 미안. 몰랐어."
    y 1a "괜찮아요."
    y "요새 등이 자주 아파서 관리하는 데 최선을 다하고 있어요."
    mc "그래?"
    mc "왜 그럴까나…."
    y 1f "왜냐하면 제…."
    y 1n "아…."
    y 1o "ㅈ, 제…."
    mc "자세?"
    mc "하긴 항상 웅크리고 앉아있으니까…."
    y 2p "네!"
    y 2q "제 독서 자세가 진짜 나쁘거든요!"
    y "그래서 바닥에 앉자고 얘기한거에요…."
    mc "알겠어."
    mc "책 좀 가져올게."
    show yuri zorder 1 at thide
    hide yuri
    "난 책을 찾으려 가방을 뒤졌다."
    mc "아, 초콜릿도 있었지…."
    "작은 초콜릿 가방이다."
    "차랑 잘 어울릴 것도 같아, 가져갔다."
    "유리랑 나는 벽을 등지고 앉았다"
    "우리는 저번에 그랬던 것 처럼 서로 책의 양쪽 부분을 잡고 앉았다."
    "딱 한 가지만 빼고…."
    "서로의 거리가 굉장히 가깝다는 것."
    show yuri 2h zorder 2 at t11
    y "잘 안보이는데…."
    mc "…!"
    show yuri 2e at d11
    "유리는 어깨가 닿을 때까지 내 옆으로 왔다."
    "이러면 어떻게 집중을 하겠어…?!"
    "유리는 항상 귀엽지만…."
    "가끔식 주체가 안될정도로 부주의해!"
    y 2f "[player] 씨, 여기…."
    "유리는 찻잔을 건네주었다."
    "난 책을 들고 있지 않은 손으로 찻잔을 들었고, 결국 더 집중하기 힘들게 됐다."
    "실수로 가슴을 건드리기라도 했다간…!"
    "반면, 유리는 아무것도 모르는듯했다."
    "유리의 표정으로 보아 책 이외의 것은 보이지 않는 듯했다."
    "난 내 모든 집중력을 끌어모아 책을 읽는데 쏟아부었다."
    "…."
    "몇 분 후, 조금씩 편안해지기 시작했다."
    "난 다리 사이에 찻잔을 놓고 초콜릿 포장지를 만지작거렸다."
    mc "아, 미안…."
    "포장지를 열기 위해 난 책에서 손을 놨다."
    mc "먹고 싶은 만큼 먹어도 돼."
    y 2s "아, 그건…."
    y "괜찮아요…."
    mc "응? 괜찮아?"
    y 2v "…."
    y "제가 초콜릿을 만지면 책에 자국이 남을 테니까요…."
    mc "아, 그렇네…."
    mc "거기까진 미처 생각 못했네."
    mc "미안…."
    y 2a "사과하실 필요 없어요."
    y "전 그냥 책을 들고 있을게요."
    mc "진짜…?"
    y "물론이죠."
    $ persistent.clear[3] = True
    scene y_cg2_bg
    show y_cg2_base
    show y_cg2_details
    show y_cg2_nochoc
    show y_cg2_dust1
    show y_cg2_dust2
    show y_cg2_dust3
    show y_cg2_dust4
    with dissolve_cg
    "유리는 양손으로 책을 펼쳤다."
    "유리가 책을 들고 있어서 난 읽는 데에 불편함은 없었다."
    "그 결과, 유리의 왼팔이 내 다리에 닿고있었다."
    mc "음, 이러면…."
    "유리는 이미 책 읽는데 정신이 팔려있다."
    "난 초콜릿 한 조각을 입에 던져넣었다."
    "그리고 다른 조각은…."
    "유리에게 줘야겠지."
    "유리는 책에서 눈을 떼지 않고 있었다."
    "가만히 입을 닫고있었다."
    "그렇다고 여기서 멈출 순 없지!"
    hide y_cg2_nochoc
    "난 조심스레 초콜릿을 유리의 입술에 가져다댔다."
    "그러자, 유리는 무의식적으로 초콜릿을 물었다."
    y "에…?"
    show y_cg2_exp2
    "유리의 표정이 갑자기 흔들리기 시작했다."
    y "방금…."
    y "저 방금…."
    "유리는 방금 무슨 일이 일어난건지 모르겠다는 눈빛으로 날 바라봤다."
    show y_cg2_exp3
    show y_cg2_nochoc:
        alpha 0
        linear 0.5 alpha 1
    hide y_cg2_exp2
    y "어, 음…."
    y "[player] 씨…."
    mc "미, 미안!"
    mc "그런 짓은 하지말았어야 했는데…."
    stop music
    y "아, 아아…."
    "유리의 숨이 거칠어지기 시작했다."
    y "저…."
    y "저, 더는…."
    y "[player] 씨…."
    "갑자기 유리는 내 팔을 온 힘을 다해 붙잡았고 갑자기 내 위에 올라탔다."
    "내 찻잔은 굴러갔다."
    scene bg closet
    show yuri 2t zorder 2 at t11
    with wipeleft
    y "[player] 씨…."
    play sound closet_close
    show dark zorder 100
    with wipeleft
    y "제 심장이…."
    y 2y6 "제 심장의 두근거림이 멈추질 않아요, [player] 씨…."
    y "진정할 수가 없어요."
    y "이제 아무것도 집중할 수가 없어요…!"
    y "느낄 수 있나요, [player] 씨?"
    "유리는 갑자기 내 손을 자신의 가슴에 갖다댔다."
    play music hb
    show layer master at heartbeat
    y 3t "왜 이럴까요?"
    y "정신을 잃는 기분이에요…."
    y 3y4 "멈출 수 없어요."
    y 3y6 "책같은 건 이제와서 필요없어요…."
    y "전 그냥…."
    y 3s "…당신만…."
    y "…보고싶어요."
    hide yuri
    show yuri eyes
    pause 3.0
    y "…하아…."
    pause 3.0
    y "…하아…."
    pause 3.0
    y "…하아…."
    pause 3.0
    play sound closet_open
    stop music
    show layer master
    hide yuripupils
    show yuri 1n at face
    with None
    show yuri 3n at t32 with None
    hide dark
    show monika 3l zorder 3 at f31
    with wipeleft
    m "어, 음…."
    m "시 나눠볼 시간이야…."




    return

label yuri_exclusive2_2_ch23:
    $ config.skipping = False
    scene black
    with None
    $ audio.t6g = "<loop 10.893>bgm/6g.ogg"
    play music t6g
    pause 4.62
    scene bg corridor
    show yuri eyes_base
    pause 1.0
    show bg glitch:
        yoffset 480 ytile 2
        linear 0.25 yoffset 0
        repeat
    show yuri glitch at i11
    $ gtext = glitchtext(80)
    $ currentpos = get_pos()
    play music g1
    y "[gtext]{nw}"
    stop music
    scene bg corridor
    show yuri 2n at i11
    y "음…."
    y "잠시만요…."
    y 2o "저 어떻게…."
    y 2y6 "…죄송해요, 이상한 데자뷰를 느낀 거 같아요…."
    y "이런 일이 전에도 있진 않았었죠… 그렇죠?"
    y 2t "머리가 조금 어지러워서…."
    y 3t "그게 보여졌다거나 그런 게 아니었으면 좋겠네요…!"
    y "저희가 함께 시간을 보내기 시작한지 얼마 안 됐는데 제가 이상하다고 생각하시는 건 정말 싫어요…."
    y "그러니까…."
    show bg corridor:
        xoffset 0
        parallel:
            0.36
            xoffset 1
            repeat
        parallel:
            0.49
            xoffset 0
            repeat
    show black zorder 5:
        alpha 0.5
        parallel:
            0.36
            alpha 0.5
            repeat
        parallel:
            0.49
            alpha 0.475
            repeat

    play music t9
    y "모든 사람은 특이한 점을 가지고있죠."
    y 1v "그런데 만난지 얼마 안된 사람에게 그걸 보여준다는 것은 부적절하죠… 아니면 비호감이라던가."
    y "그게 제가 알아낸 거에요."
    y "제가 어렸을 때, 제 생각에 전 되게 사람들한테 참견하기 좋아하는 아이였던 거 같아요…."
    y "그래서 사람들이 제 주변에서 하나 둘씩 사라진 거 같아요."
    y 2w "그래서 전 제 자신의 그런 것들을 증오하기 시작했어요."
    y "취미들에 대한 제 집착이요."
    y "그리고 무언가에 흥분했을 때 자기 자신을 통제할 수 없다는 것."
    y "그렇게…."
    y 1v "결국 사람들이랑 대화하는 걸 그만뒀어요."
    y "만약 저에게 가장 큰 문제 때문에 사람들이 절 좋아하지 않는다면…."
    y 1u "…그럼 그냥 벽을 쌓으면 되는 거겠죠."
    y 1h "그런데 최근 들어서 뭔가가 잘못됐어요."
    y "뭔지는 잘 모르겠는데…."
    y 2y6 "그런데 우리가 동아리에 들어올때마다, 제 심장이 미친듯이 뛰기 시작해요."
    y "가슴을 뚫고 나올 듯이요."
    y "떨쳐 낼 수 없는 에너지와 감정들이 흘러넘쳐요."
    y "그게 절 이상한 짓을 하게 만들었어요."
    y 2t "왜 이런 일이 일어나는지 모르겠어요!"
    stop music
    y 1t "[player] 씨…."
    y "모니카 씨가 요즘 조금 이상한데, 저만 그렇게 느끼는 거 아니죠?"
    y 1v "제가 동아리에 들어왔을 때만 해도 엄청 다정다감했는데…."
    y "그런데 최근에 모니카 씨가 근처에 있을 때마다 뭔가 쎄한 느낌이 들어요."
    y 2y4 "제가 미친 게 아니죠?"
    y 2y1 "아니라고 해줘요!"
    y "전에는 모니카 씨가 항상 듣고 있었으니까 전에는 아무 말도 못 했지만…."
    y 2y3 "드디어, 저희 둘밖에 없네요…."
    y "잠깐 여기서 쉴까요?"
    y 1m "좋아요…."
    y "…."
    play music hb
    show layer master at heartbeat
    show yuri as yuri_eyes zorder 4:
        "yuri/eyesfull.png"
        i11
        alpha 0.0
        block:
            2.012 * 4 - 1.49
            alpha 1.0
            0.52
            alpha 0.0
            1.49
            repeat
    pause 2.0
    $ ad = 40.0
    $ ac = 1.0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "전 그냥 여기 있고 싶어요."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "단 둘이서만요."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y "문예부가 끝날 때 까지 기다리고 나면."
    $ ac += 0
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "교실 전체가 우리 세상이 되는거에요."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "저희 독서 시간을 방해하는 사람은 전혀 없겠죠."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "목에 칼을 꽂고 싶은 느낌을 주는 사람은 하나도 없이요."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1q "아하하…."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "농담이에요!"
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "농담."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1i "제가 칼을 좋아하긴 하지만…."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y "이상하게 들릴 수는 있지만, 그게 얼마나 아름다울지 이해하지 못 할거에요."
    $ ac += 0.5
    show monika 1 onlayer front at malpha(ac / ad)
    y 1f "아, 좋은 생각이 났어요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "가끔씩 저희 집에 오는 게 어때요?"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "제 컬렉션을 보여드릴게요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "여러 장인들이 만든 걸로 많이 모아놨어요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "모두 골고루 많이 썼어요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "그 칼들이 외로워하면 안되니까…."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "그 누구도 외로워서는 안돼요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "누구도."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1c "그래서 당신이 문예부에 들어온 게 전 정말 기뻐요, [player] 씨."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "우린 더 이상 외롭지 않아도 돼요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "왜냐하면 우린 서로가 있잖아요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "매일."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "그게 우리한테 필요한거죠"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y6 "그거 알아요?"
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "문예부같은 거 관두죠."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "모니카같은 년은 이제 볼 필요없게."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1y4 "다른 애들은 말할 것도 없고…."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "매일 방과 후 집에 같이 가도록 해요."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "그리고 같이 책도 보고."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1m "같이 먹고."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y "같이 자고."
    $ ac += 1
    show monika 1 onlayer front at malpha(ac / ad)
    y 1s "정말 굉장하지 않나요?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "전부 우리가 원했던 거 잖아요."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y 1a "그게 당신이 이 동아리에 온 이유 아니에요?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "이건 운명이에요."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "우리 둘이 만날 운명."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "이제 우리는 제가 몇년동안 기다려온 해피 엔딩을 맞이하는거죠."
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    y "그렇게 해줄 수 있죠, [player]?"
    $ ac += 2
    show monika 1 onlayer front at malpha(ac / ad)
    $ gtext = glitchtext(200)
    y "그렇게{space=60}[gtext]{nw}"

    hide monika onlayer front
    window hide(None)
    $ poemsread = 0
    $ y_gave = False
    play music t5
    scene bg club_day
    window show(None)
    window auto

    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
