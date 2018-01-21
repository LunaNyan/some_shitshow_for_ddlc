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

label ch2_main:
    scene bg club_day
    with dissolve_scene_half
    play music t2
    $ finalConso = finalChecker(player)
    "또 하루가 지나고, 벌써 동아리 시간이 돌아왔다."
    "지난 이틀보단 이 곳이 좀 더 편해진 것 같다."
    "부실을 들어서니 익숙한 장면이 날 반겨준다."
    show sayori 2x zorder 2 at t11
    s "안녕, [player]~"
    mc "여, 사요리."
    mc "오늘 기분 좋아보이네."
    s 1q "에헤헤~"
    s "그냥 네가 문예부에 있다는 게 익숙하지가 않아서."
    mc "그렇구나…."
    mc "…그렇게 싱글벙글 하다기엔 꽤 간단한 이유인걸."
    mc "뭐, 너는 간단한 거로도 기분이 좋아지곤 했으니까."
    s 1d "말이 나와서 말인데…."
    s "나 배고파…."
    s "과자 좀 사다 줄 수 있어?"
    mc "싫은데."
    s 4h "에??"
    s "별로 너답지 않아!!"
    mc "이유가 있어."
    mc "한번 네 지갑을 볼까, 사요리?"
    s 4l "에… 에?"
    show sayori at s11
    s "왜… 갑자기?"
    mc "딱히 이유는 없는데."
    mc "그냥 갑자기 보고 싶어졌달까."
    s 1l "아, 아…."
    show sayori zorder 2 at t11
    "사요리는 긴장하며 동전 지갑을 꺼냈다."
    "걸쇠를 풀고 지갑을 연다."
    "그러고는 지갑을 뒤집어 내용물을 책상 위에 쏟아낸다."
    "작은 동전 두 개가 책상 위에 떨어진다."
    s 5a "아하하…."
    mc "그럴 줄 알았다…."
    mc "사요리, 네가 하는 짓은 뻔할 뻔 자야."
    s 5c "불공평해!"
    s "어떻게 안 거야!"
    mc "간단해."
    mc "네가 돈이 있었다면, 과자 정도는 오기 전에 사고 왔겠지."
    mc "그럼 결국 배는 고프지 않았지만, 같이 걷고 싶어서 변명거리를 찾았다거나."
    mc "용돈을 다 써버렸다는 걸 깜빡했다며 나한테 돈을 빌리려고 한 거겠지!"
    mc "그리고 한 가지 더…."
    mc "… 넌 항상 배고프잖아!"
    mc "그럼 결론은 딱 하나!"
    s 4p "우에엥~!"
    s "항복, 항복!"
    s "더 이상 얘기하지 말아줘! 죄책감 든단 말이야…."
    mc "죄책감이 들 만한 짓을 했으니까 그렇지…."
    show yuri 1c zorder 2 at t33
    y "아하하."
    "유리는 갑작스레 웃었다."
    show sayori 4g
    mc "응?"
    "듣고 있었던 건가?"
    "언제나 그랬듯 책에 코를 박고 있긴 한데."
    show yuri 3n at h33
    y "아…!"
    y "듣고 있었던 건 아니에요!"
    y 3o "그냥… 책에 재밌는 내용이 있어서…."
    show sayori zorder 3 at f32
    s 1h "유리이…."
    s "[player]이한테 돈 좀 빌려달라고 해줘…."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "그건…!"
    y "저를 그런 식으로 끌어들이지 마세요, 사요리 씨…."
    y "그것보다도…."
    y 1k "돈은 본인이 감당할 수 있는 선에서 쓰는 거예요…."
    y "그리고 솔직히, 그런 잔머리로 남을 속이려고 하다니 응보를 받죠."
    show sayori 1b
    mc "…."
    y 3n "아…!"
    y "제가 방금…."
    y 4c "그… 그런 말은 아니었어요!!"
    y "책에 너무 집중하다 보니…."
    y "우으…."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1r "아하하!"
    s 3x "난, 유리 네가 속마음을 말할 때가 좋더라…."
    s "가끔 있는 일이지만 인간적인 느낌이 들어서!"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3v "그건…."
    y "그렇게 생각하시면…."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1x "근데 맞는 말이긴 해…."
    s "잘못을 했으니까 음보를 받아야지."
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y 3h "응보요…."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1l "내 말이 그 말이야!"
    show sayori zorder 2 at t32
    show yuri zorder 3 at f33
    y "근데, 사요리 씨가 그런 짓을 할 정도면…."
    y 1a "모든 사람 속엔 작은 악마가 있다는 말이 사실이긴 한가 봐요?"
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1q "에헤헤…."
    show sayori zorder 2 at t32
    mc "조심해."
    mc "사요리는 생각보다 간사하거든."
    mc "애초에 날 문예부로 끌어들인 것도 너희들에게 새 부원이 들어올 거라고 말한 후니…."
    show sayori zorder 3 at f32
    s 1h "그치만…!"
    s "컵케이크라도 없었으면 너 아예 안 왔을 거잖아…."
    s "그래서 나츠키를 꼬드길 구실을 만들어야 했단 말야!"
    show sayori zorder 2 at t32
    mc "사요리, 내가 아예 안 갔으면 어쩌려고 그래…."
    show sayori zorder 3 at f32
    s 1l "에헤헤…."
    play sound "sfx/slap.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 4p zorder 3 at hf32
    "{i}쫘악!{/i}"
    hide white
    s 4p "꺄아!"
    "갑자기 무언가가 날아와 사요리의 얼굴을 때리고 책상 위에 떨어졌다."
    s 4j "아야야야…."
    s "도대체 뭐가…."
    s 4n "에??"
    s "쿠…쿠키다!"
    "플라스틱으로 포장된 커다란 쿠키였다."
    "사요리는 주변을 둘러보았다."
    s 4m "기적인가??"
    s "앙모 받아서 일어난 거야!"
    show sayori zorder 2 at t32
    mc "응보겠지…."
    show sayori 4n
    show yuri zorder 3 at f33
    y 1u "말이 될 뻔도 했지만요…."
    show yuri zorder 2 at t33
    show natsuki 3z zorder 3 at f31
    n "아하하하!"
    n "{i}원래{/i}는 그냥 주려고 했는데."
    n 3d "들어오다 컵케이크 얘기를 들어서 말야."
    n "네가 네 얼굴을 봐야 했는데, 아하하하!"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 4m "나츠키!"
    s "진짜 진짜 고마워!"
    s 4s "행복해애…."
    "나츠키는 쿠키를 품에 안았다."
    show sayori zorder 2 at t32
    mc "좀, 그냥 먹어…."
    "사요리는 빠르게 봉지를 열어 쿠키를 크게 한 입 베어물었다."
    show sayori zorder 3 at f32
    s 4q "너므 마시써…."
    show sayori zorder 3 at hf32
    s 4o "으윽…!"
    "사요리는 손으로 급히 입을 가렸다."
    s 4p "혀 깨물어셔…."
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3a "에헤헤."
    n "쿠키 하나 정도로는 안 될 거 같네."
    "나츠키는 자신의 쿠키를 한입 물었다."
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1c "아, 나츠키. 네 것도 맛있어 보인다!"
    s "먹어봐도 돼?"
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4e "뭐…?"
    n "얻어먹는 거면 조용히 해!"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1h "하지만 네 건 초코인걸…."
    show sayori zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4c "응, 내가 왜 이걸 안 주고 그걸 줬겠어?"
    show natsuki zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "알았어…."
    s 1q "그래도 정말 고마워."
    s "에헤헤~"
    show sayori behind natsuki zorder 2 at t21
    "사요리가 자리에서 일어나더니 나츠키를 뒤에서 끌어안는다."
    n 12c "아… 정말…."
    n "알겠어, 알겠다고."
    "나츠키가 쿠키는 손에 든 채 그대로 사요리를 살살 밀어낸다."
    show sayori 1n at h21
    s "…{i}냠.{/i}"
    "사요리는 허리를 굽혀 나츠키의 쿠키를 한입 베어 물었다."
    n 1p "{i}야…야!{/i}"
    n "방금 진심으로 그런 거야?!"
    s 1q "우후후!"
    show sayori at lhide
    hide sayori
    "입안 가득 쿠키를 머금고 사요리가 도망간다."
    show yuri 1c
    "유리와 나는 조용히 웃는다."
    show yuri 1a
    show natsuki zorder 3 at f31
    n 1w "정말! 가끔 보면 그냥 어린애 같다니까!"
    n 1h "모니카, 사요리한테 좀…."
    n 1c "… 에?"
    "나츠키는 주변을 둘러보았다."
    "모니카는 부실에 없었다."
    n 4q "어…."
    n "모니카는 어디 있는 거야?"
    show natsuki zorder 2 at t31
    show yuri 2f zorder 3 at f33
    y "그러게요…."
    y "오늘 모니카 씨가 늦는다던가… 혹시 들은 거 있으세요?"
    show sayori 1b zorder 3 at f32
    show yuri zorder 2 at t33
    s "난 몰라…."
    show sayori zorder 2 at t32
    mc "응, 나도 못 들었어."
    show yuri zorder 3 at f33
    y 2l "으응…."
    y "모니카 씨가 늦을 때도 있네요…."
    show yuri zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "별일 아니겠지…?"
    show sayori zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "당연히 별일 아니겠지."
    n "뭔가 할 일이 있어서일 거야."
    n 3t "유명하니까… 걔는…."
    show natsuki zorder 2 at t31
    show sayori 4m zorder 3 at f32
    s "에?"
    s "혹시…."
    s "혹시 나… 나… 남…!"
    show sayori zorder 2 at t32
    show yuri 1a zorder 3 at f33
    y "아하하. 놀랄 일은 아닌걸요."
    y "저희 셋 인기를 다 합쳐도 모니카 씨가 더 인기 많을걸요."
    show yuri zorder 2 at t33
    show sayori 1r zorder 3 at f32
    s "에헤헤, 그렇긴 해…."
    show sayori zorder 2 at t32
    show natsuki 1p zorder 3 at f31
    n "뭐어어?!"
    hide natsuki
    hide sayori
    hide yuri
    with wipeleft
    "그때, 부실 문이 열렸다."
    show monika 1g at l41
    m "미안해! 진짜 미안해!"
    mc "아, 왔어?"
    m "늦으려고 한 건 아니었는데…."
    m "걱정하게 만들었다면 정말 미안해!"
    show sayori 4n zorder 3 at f42
    s "에?"
    s "그럼 모니카는 남자친구보다 동아리를 더 중요하게 생각하는 거네!"
    s "역시 대단해!"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m 1l "나…남자친구…?"
    m "무슨 소리 하는 거야…?"
    "모니카가 무슨 소리냐는 눈빛으로 날 쳐다본다."
    show monika zorder 2 at t41
    mc "아, 별거 아냐. 신경쓰지 마…."
    mc "무슨 일이라도 있던 거야?"
    show monika zorder 3 at f41
    m 1e "아…."
    m "오늘 마지막 교시가 자습이었거든."
    m "정신 차려보니 시간이 벌써 이렇게 된 거 있지…."
    m "아하하…."
    show monika zorder 2 at t41
    show natsuki 2c zorder 3 at f43
    n "말이 안 되는데."
    n "적어도 수업 종료 종소리는 들었을 거 아냐."
    show natsuki zorder 2 at t43
    show monika zorder 3 at f41
    m 1m "피아노 연습하느라 못 들었던 거 같아…."
    show monika zorder 2 at t41
    show yuri 1e zorder 3 at f44
    y "피아노…?"
    y "모니카 씨, 악기도 다룰 줄 아셨었군요."
    show yuri zorder 2 at t44
    show monika zorder 3 at f41
    m 1l "그렇게 잘 하는 건 아냐…!"
    m "최근에 배우기 시작했어."
    m 1m "어릴 때부터 피아노를 쳐보고 싶었거든."
    show monika zorder 2 at t41
    show sayori 4x zorder 3 at f42
    s "멋지다!"
    s "나중에 연주 하나 해줘, 모니카!"
    show sayori zorder 2 at t42
    show monika zorder 3 at f41
    m "그게…."
    "모니카는 날 바라본다."
    m 1a "조금 더 잘 치게 되면 해줄게."
    show monika zorder 2 at t41
    show sayori zorder 3 at f42
    s 4q "야호~!"
    show sayori zorder 2 at t42
    mc "멋지네."
    mc "나도 기대하고 있을게."
    show monika zorder 3 at f41
    m 1b "그래?"
    m "그렇다면…."
    m "실망시키지 않을게, [player]."
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    show monika 5 zorder 2 at t11
    hide sayori
    hide natsuki
    hide yuri
    "모니카는 달콤한 미소를 지었다."
    mc "아…."
    mc "너무 부담 갖지는 마!"
    m 1a "아하하, 걱정하지 마."
    m "최근에 엄청 연습했거든."
    m "준비되면 꼭 보여줄 거니까."
    mc "그렇다면야."
    mc "행운을 빈다."
    m 1j "고마워~!"
    m 1a "혹시 내가 놓친 거라도 있어?"
    mc "아, 아니. 딱히."
    show monika zorder 1 at thide
    hide monika
    "사요리가 저지른 만행은 덮어주기로 했다."
    "어차피 나중에 나츠키가 불만을 토로하겠지."
    "그러고 보니, 다들 평소의 부 활동을 하고 있다."
    "사요리는 벌써 자기 쿠키를 다 먹었다."
    "유리는 읽던 책을 계속 읽고, 나츠키는 벽장으로 들어간다."




    $ nextscene = poemwinner[1] + "_exclusive_" + str(eval(poemwinner[1][0] + "_appeal"))
    call expression nextscene from _call_expression_25



    return


label ch2_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "좋아, 얘들아!"
    m "서로의 시는 다 나눠 보았겠지?"
    m "오늘은 할 얘기가 있으니까, 교실 앞쪽으로 와서 앉아 줄래?"
    show natsuki 3c zorder 3 at f31
    n "혹시 축제에 관한 거야?"
    show natsuki zorder 2 at t31
    show monika 1j zorder 3 at f32
    m "뭐, 그런 거지~"
    show monika 1a zorder 2 at t32
    show natsuki 1m zorder 3 at f31
    n "으, 축제 때 진짜로 뭔가를 해야 돼? 그럴 필요 없잖아."
    n "겨우 며칠 만에 다 준비할 수 있는 것도 아니고."
    n "새 부원을 모으기는커녕 창피만 당할 것 같은데."
    show yuri 2g zorder 3 at f33
    show natsuki zorder 2 at t31
    y "제 생각도 그래요."
    y "마지막 순간까지 기다렸다 준비하는 건 별로 제 스타일이 아니기도 하고…."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1b "너무 걱정하지 마!"
    m "간단하게 할 거니까, 알았지?"
    m 1a "그냥 장식 몇 개면 충분할 거야."
    m "사요리가 포스터는 거의 다 만들었고, 나는 행사때 나눠줄 팸플릿을 다 만들어 놓은 상태거든."
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "좋아, 그런 건 다 좋은데…."
    n "그래서 우리는 축제 때 뭐해?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1d "아 미안! 순간 얘기해줬다고 착각했지 뭐야."
    m 1b "낭송회를 할 거야!"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3h "낭송회?"
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "낭송…."
    y 3o "으응, 모니카 씨이…."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1k "그래! 축제 때 시 낭송회를 열거야."
    m 1b "각자 시 하나씩을 골라서 행사 때 시를 낭송하는 거야."
    m "그리고 만약 다른 사람이 낭송하고 싶은 시가 있으면 무대로 초대하는 거지!"
    m 1a "혹시나 준비가 필요한 사람이 있을 수도 있으니까 벌써 포스터를 만들어 둔 거고."
    show yuri zorder 2 at t44
    show monika zorder 2 at t43
    show natsuki zorder 2 at t42
    show sayori 4q at l41
    s "에헤헤~"
    "사요리가 칠하다 만 포스터를 들어 보인다."
    show natsuki 4w zorder 3 at f42
    n "모니카, 지금 나랑 농담하는 거지?"
    n "호, 혹시 포스터 벌써 붙여둔 건 아니지?!"
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1d "에? 달아뒀는데…."
    m "그럼 안 되는 거야…?"
    show monika zorder 2 at t43
    show natsuki 1s zorder 3 at f42
    n "아니."
    n "나쁜 생각은 아닌데…."
    n 1w "근데 내가 이러려고 여기 들어온 건 아냐, 알지?!"
    n 1x "내가 그런 걸 {i}많은 사람들{/i} 앞에서 할 수 있을 리가 없잖아!"
    show natsuki zorder 2 at t42
    show yuri zorder 3 at f44
    y 3r "저… 저도 나츠키 씨한테 동감이에요!"
    y 3w "그런 거… 살면서 해본 적도 없고…."
    "유리는 머리를 숙인 채 고개를 저었다."
    show yuri zorder 2 at t44
    show sayori 1g zorder 3 at f41
    s "얘들아…."
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 1g "사요리, 괜찮아…."
    m "이해해."
    m "당장 사흘전만 해도 시 쓰고 있다는 걸 숨기고 있었잖아…."
    m "그런데 갑자기 사람들 앞에서 자기 시를 낭송하라니…."
    m 1r "조금 무리한 부탁이긴 했어."
    m "미안해."
    show monika zorder 2 at t43
    show natsuki 5g zorder 3 at f42
    n "…."
    show natsuki zorder 2 at t42
    show monika zorder 3 at f43
    m 1i "그래도…!"
    m "이왕 하기로 한 거 최선을 다하자!"
    m 1d "어차피 문예부의 운명을 정하는 건 우리잖아."
    m "모두가 연습해서 시 낭송회 때 좋은 시작만 만들어주면…."
    m 3a "분명 다른 사람들도 편하게 행사에 참여할 수 있을 거야!"
    m "그럼 분명 문학이 얼마나 재미있는지 사람들도 알 수 있을 거야!"
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "응응!"
    s 1x "자기감정 표현하는 거랑…."
    s "자신을 더 잘 알아가는 거랑…."
    s "새로운 지평선을 발견한다거나…."
    s "재미있게 논다거나!"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m 4b "맞아!"
    m "바로 우리가 문예부에 들어온 이유이기도 하지."
    m 4e "그런 기분 나누고 싶지 않아?"
    m "너희가 문예부에 처음 발을 들였을 때 그 느낌을 전해주고 싶지 않아?"
    m 1e "안 그래?"
    m "그렇잖아?"
    m 1b "게다가 그게 그냥 사람들 앞에서 딱 2분만 시를 읽고 있는 거라면…."
    m "…딱히 못 할 것도 없잖아!"
    show monika 1a zorder 2 at t43
    show natsuki 5s zorder 3 at f42
    n "…."
    show natsuki zorder 2 at t42
    show yuri 4b zorder 3 at f44
    y "…."
    show yuri zorder 2 at t44
    show sayori 1g
    "나츠키와 유리는 그래도 입을 열지 않는다."
    "사요리는 걱정되는 눈빛이다."
    "그럼 어쩔 수 없지…."
    mc "나도 동의해…."
    mc "그렇게 무리한 부탁인것 같지도 않고 말이야."
    mc "사요리와 모니카가 저렇게 새 부원을 모으려고 노력 중인데."
    mc "조금이나마 도와줄 수 있다면…."
    show natsuki zorder 3 at f42
    n 5h "글쎄, 뭐…."
    n "…."
    "나츠키도 더 이상 거부할 생각은 없는 것 같다."
    n "우으…."
    n 1q "…그래, 좋아!"
    n "할 수밖에 없는 거 같네."
    show natsuki zorder 2 at t42
    show sayori zorder 3 at f41
    s 4r "좋아~!"
    show sayori 4a zorder 2 at t41
    show monika zorder 3 at f43
    m 1e "휴우…."
    m "고마워, 나츠키."
    m "너는 어때, 유리…?"
    show monika zorder 2 at t43
    show yuri zorder 3 at f44
    y "…."
    "유리는 모두의 눈치를 살폈다."
    y "에휴…."
    y "어쩔 수 없네요…."
    show yuri zorder 2 at t44
    show sayori zorder 3 at f41
    s 4r "아하하, 그럼 다들 하는 거네!"
    s "역시 유리는 최고야~"
    show sayori 4a zorder 2 at t41
    show yuri zorder 3 at f44
    y "이 동아리를 계속하다간 죽을지도 몰라요…."
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 1l "어머…."
    m 1n "아냐, 괜찮을 거야, 유리."
    m "그렇다면…."
    m 1b "가장 중요한 얘기를 해볼까!"
    m "너희가 지금까지 쓴 시중 하나를 골라."
    m "그걸 앞에서 발표해보면서 연습할 거야."
    show monika 1a zorder 2 at t43
    show natsuki zorder 3 at f42
    n 1p "마…말…말도 안 돼!!"
    show natsuki zorder 2 at t42
    show yuri 3n zorder 3 at f44
    y "모니카 씨…!"
    y "너무 갑작스러워요…!"
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "글쎄, 부원들 앞에서 할 수 없다면…, 다른 많은 사람들 앞에서 할 수 있을까?"
    show monika zorder 2 at t43
    show yuri 4c zorder 3 at f44
    show natsuki 1o
    y "아, 안돼…."
    show yuri zorder 2 at t44
    show monika zorder 3 at f43
    m 2a "걱정하지 마."
    m "내가 가장 먼저 할게."
    show monika zorder 2 at t43
    show sayori 1r zorder 3 at f41
    s "그 다음엔 내가 해도 돼?"
    show sayori zorder 2 at t41
    show monika zorder 3 at f43
    m "아하하, 물론이지."
    m 2d "자, 어디 보자…."
    "모니카는 자신의 공책에 쓰여있는 시 중에 가장 맘에 든다고 생각한 시를 골랐다."
    "그러더니 탁상 앞에 섰다."
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    show yuri zorder 1 at thide
    hide sayori
    hide natsuki
    hide yuri
    m 1a "이 시의 제목은 {i}그들이 나는 모습{/i}이야."
    m 1r "으흠…."
    show monika 1a
    "모니카는 자신의 시를 낭송하기 시작했다."
    "모니카의 깔끔하고 자신감 있는 목소리가 교실을 채운다."
    "그것보다는, 모니카의 순수한 어조가 눈에 띄었다."
    "어떤 부분에 어떤 감정을 넣어야 하는지 정확히 알고 있어서, 목소리가 글에 생명을 불어 넣어준다."
    "전에 이런 걸 해본 적이 있는 건지, 아니면 선천적으로 타고 난 건지…."
    "나는 내 주변을 둘러봤다."
    "모두의 눈은 모니카를 보고 있었다."
    "사요리는 놀란 것처럼 보인다."
    "유리는 의미를 알기 힘든 뭔가 강렬한 표정을 짓고 있다."
    show monika 1j
    "모니카는 낭송을 끝냈다."
    "우리 네 명은 박수를 쳤다."
    "모니카는 숨을 들이쉬고 미소 지었다."
    show monika 1a
    show sayori 4m zorder 3 at f33
    s "그거… 엄청 멋있었어, 모니카!"
    show sayori zorder 2 at t33
    show monika zorder 3 at f32
    m 1j "아하하, 고마워."
    m 1a "좋은 예시가 되었다면 좋겠네."
    m "사요리, 준비는 됐지?"
    show monika zorder 2 at t32
    show yuri 2r at l31
    y "제…제가 먼저 할게요!"
    show sayori at h33
    s 1n "우와아! 갑자기 유리가 열정을 드러내고 있어!"
    "유리는 긴장한 듯 손에 종이를 세게 움켜쥐고 서 있다."
    "머리를 숙인 채, 유리는 빠르게 교탁 앞으로 걸어갔다."
    show monika zorder 1 at thide
    show sayori zorder 1 at thide
    show yuri zorder 2 at t11
    hide monika
    hide sayori
    y 2v "이 시의 제목은…!!"
    "유리는 걱정스럽게 우리를 바라보았다."
    s "할 수 있어, 유리…."
    y "제목은… 제목은…{i}핏빛 눈의 잔상{/i}입니다."
    "시를 읽기 시작하면서 유리의 목소리는 떨리기 시작했다."
    "조금 전만 해도 그렇게 거부하더니."
    "갑자기 왜 저렇게 열심히 하는 걸까?"
    show yuri 2l
    "첫 두 행을 낭독하던 중, 목소리가 서서히 바뀐다."
    "마치 책에 집중하던 모습과 비슷하게."
    "긴장에 떨던 목소리는, 이내 한 음절, 한 음절 또박또박 읽어 내려가는 것이 마치 당당하고 강렬한 여성 같이 바뀐다."
    "시 내용은 반전으로 가득한 구조로 되어있는데, 유리의 알맞은 타이밍과 또렷한 목소리가 그 내용을 제대로 전달하고 있었다."
    "혹시 우리는 유리의 본 모습을 이렇게 부분이나마 보고 있는 게 아닐까…?"
    show yuri 2t
    "시가 끝이 났다."
    "잠깐동안의 정적이 흐른다."
    "마치 뭔가에 홀렸었다는 듯, 유리도 깜짝 놀라 원래의 모습으로 돌아온다."
    y 3o "저…."
    "…이럴 땐 내가 나서줘야겠지?"
    "나는 먼저 박수를 치기 시작했다."
    "모두들 내 뒤를 이어 박수를 치기 시작했고, 그제야 우리는 유리가 벌써 받아야 했을 할 환호를 보내준다."
    "박수를 치기 싫었다던가, 그런 거는 아니었고."
    "너무 놀란 나머지 그냥 깜빡했던 듯하다."
    "박수가 끝나자 유리는 품속에 시를 안고 자신의 자리로 달려갔다."
    show yuri at lhide
    hide yuri
    show monika 1a zorder 2 at t11
    m "유리, 엄청 대단했어."
    m "들려줘서 고마워."
    y "…."
    "반응이 없다…."
    show sayori 1q zorder 2 at t31
    s "좋아~"
    s "내가 다음인 거 같네!"
    "사요리는 의자에서 퐁하고 일어나서 교탁으로 힘차게 걸어갔다."
    show sayori zorder 2 at t11
    show monika zorder 1 at thide
    hide monika
    s 1x "제목은…{i}내 목초지{/i}."
    s "아…."
    s 1s "…아하하하!"
    s 4s "아 미안, 웃어버렸네…."
    s 4q "에헤헤…."
    mc "사요리…."
    s 1l "내가 생각했던 것보다 어렵다!"
    s "너희들 어떻게 그렇게 쉽게 한 거야?"
    show monika 3a zorder 2 at t31
    show sayori 1b
    m "음…."
    m "다른 사람한테 읽어준다고 생각하지 말고."
    m "너 자신한테 읽어준다고 생각해 봐. 거울 앞이나, 아니면 머릿속에서."
    m "네가 쓴 시니까, 그게 아마 제일 좋은 방법일 거야."
    show sayori 1i
    s "흠흠, 그렇구나…."
    s "좋아, 그러면…."
    show monika zorder 1 at thide
    hide monika
    show sayori 1c
    "사요리는 시를 낭송하기 시작했다."
    "왜인지는 모르겠지만, 사요리의 부드러운 목소리가 시와 찰떡궁합처럼 느껴진다."
    "마치 시가 사요리의 성격을 비추듯, 끝도 없이 밝기만 하다."
    "동시에 고요하고 달곰쌉쌀하다."
    "그냥 글로써 읽었으면 별생각 없었을 텐데…."
    "사요리가 읽어주자 감회가 새롭다."
    "사요리가 왜 내 시가 좋다는지 알 법도 하다."
    "내가 알던 사람을 더욱 깊이 알게 되는 것 같다는 느낌이 확 들게 하니 말이다."
    "낭송이 끝나자, 우리는 박수를 쳤다."
    s 3q "끝났다~!"
    mc "좋은데, 사요리."
    s "에헤헤, [player]가 좋아했으니."
    s "잘한 거겠지~"
    mc "그거 무슨 의미야…?"
    show monika 2b zorder 3 at f31
    m "잘 했어, 사요리."
    m "시의 느낌이 너랑 딱 맞았어."
    m "근데 모든 시가 그런 식으로 전해질 수 있는 건 아니야…."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1g "에? 무슨 말인지 모르겠어…."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "바꿔 말하자면 네 시 중에서도 부드럽게 읽으면 안 되는 시들이 있잖아?"
    m "어떤 시를 읽느냐에 따라서 때때론 목소리에 힘을 넣어 줄 필요가 있다는 거지…."
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1x "아, 무슨 말인지 알겠다!"
    s "그건… 음, 좀 연습하긴 했는데…."
    s 5 "너희들 앞에서 하려니까 좀 부끄러워서…."
    s "에헤헤…."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 4a "그럼 다음엔 조금 더 어려운 시를 고르라고 할 테니까."
    m "축제까지 얼마 안 남았잖아. 알겠지?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "알겠어어."
    show sayori zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "자, 다음은…?"
    m "나츠키?"
    show natsuki 5s zorder 3 at f33
    show monika zorder 2 at t31
    n "흥."
    n "[player]가 하기 전에는 하기 싫어."
    n "내 시는 너네들 것하고 비교하면 아무것도 아니잖아…."
    n "[player]가 먼저 해 주면 다들 기대치도 조금 낮아질 거 아냐."
    show natsuki zorder 2 at t33
    show sayori zorder 3 at f32
    s 1g "나츠키…."
    show sayori zorder 2 at t32
    mc "괜찮아, 괜찮아."
    mc "나도 빨리 끝내는 게 좋지 뭐."
    mc "뭐 어차피, 고를 수 있는 시가 많은 것도 아니고…."
    mc "난 그냥 오늘 쓴 걸 낭송할게."
    "난 일어나 탁상 앞으로 걸어갔다."
    show natsuki 2c zorder 2 at t44
    show sayori 1a zorder 2 at t43
    show monika 1a zorder 2 at t42
    show yuri 1e zorder 2 at t41
    "모두의 눈이 날 바라보기 시작했고, 난 심각하게 긴장되기 시작했다."
    "난 내 시를 낭송했다."
    "글에 자신이 없으니, 자연스럽게 목소리에도 힘이 들어가지 않는다."
    "그런데도 불구하고, 낭송이 끝나자 모두에게 박수를 받았다."
    mc "너희보단 잘 못 한 거 같아서 미안한데…."
    show monika zorder 3 at f42
    m 1a "너무 걱정 안 해도 돼"
    m "네 능력이라기보다, 글에 자신이 없어서 그러던 것 같던데 뭘."
    m "그건 시간이 지나면 자연스럽게 해결되는 거니까."
    show monika zorder 2 at t42
    mc "응… 아마도 그렇겠지."
    show monika zorder 3 at f42
    m 1j "좋아!"
    m 1a "나츠키, 이젠 네 차례네."
    show monika zorder 2 at t42
    show natsuki zorder 3 at f44
    n 2g "알겠어, 알겠다고."
    n "하면 되잖아."
    "나츠키는 마지 못해 자리에서 일어나 탁상 앞으로 갔다."
    show sayori zorder 1 at thide
    show monika zorder 1 at thide
    show yuri zorder 1 at thide
    show natsuki zorder 2 at t11
    hide sayori
    hide monika
    hide yuri
    n 2c "이 시의…."
    n 2q "제목은…."
    n 1x "뭐… 뭘 그렇게 보는 거야?!"
    m "그야 당연히 네가 발표하고 있으니까…."
    n 2x "흥…."
    n 2h "어쨌든… 이 시 제목은 {i}점프{/i}야."
    "나츠키는 심호흡을 했다."
    show natsuki 2c
    "나츠키가 시를 낭송하기 시작하자, 그녀의 까칠한 면모는 조금씩 사라지는 것 같았다."
    "나츠키가 살짝 강조할 때마다, 시의 운율이 강하게 전해졌다."
    "이건 나츠키의 전매특허인데, 말로 전해질 때의 효과가 굉장했다."
    "단어들이 주는 통통 튀는 느낌이, 시에게 생명을 불어넣는 듯했다."
    show natsuki 2s
    "나츠키가 낭송을 끝내자, 모두 박수를 쳤다."
    "나츠키는 투덜대며 자리로 돌아갔다."
    show monika 2a zorder 3 at f31
    m "그렇게 나쁘지만은 않았지, 그치?"
    show monika zorder 2 at t31
    show natsuki 5w zorder 3 at f32
    n "네가 그렇다면 그런 거겠지…."
    n "다시는 시키지 마."
    show natsuki zorder 2 at t32
    show monika 1d zorder 3 at f31
    m "음, 글쎄…."
    m "이제 적어도 다른 사람들 앞에서 할 때 괜찮을 거 같지?"
    show monika zorder 2 at t31
    show natsuki 2c zorder 3 at f32
    n "내 말은, 다른 사람들 앞에서 하는 게 더 쉬울 거란 거야."
    n "그땐 어떤 식으로 하든 상관없잖아."
    n 2q "그런데 너희들 앞에서 하니까…."
    n "그냥… 조금 부끄러워서…."
    show natsuki zorder 2 at t32
    show sayori 1b zorder 3 at f33
    s "나츠키 의외다…."
    s "나는 그 반대일 것 같은데."
    show sayori zorder 2 at t33
    show natsuki zorder 3 at f32
    n "난 그냥 그렇다고…."
    show natsuki zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "음, 그렇다면…."
    m "축제 때는 별로 걱정 안 해도 되겠네."
    m 2b "그래서 말인데, 모두들 와 줘서 고마워."
    m "좀 힘든 건 알지만, 어느 정도 감은 잡았겠지?"
    m 4b "너무 늦기 전에 다들 시 하나씩 골라서 축제 전까지 충분히 연습해둬."
    m "팸플릿도 만들어야 하니까 어떤 시를 골랐는지 미리미리 알려주고. 알았지?"
    show monika zorder 2 at t31
    mc "세상에…."
    mc "그러면 발표할만한 다른 시를 찾아봐야겠네."
    show monika zorder 3 at f31
    m 1j "그래도 좋아"
    m 1a "꼭 네가 쓴 게 아니어도 돼."
    m "난 이미 네가 이렇게나 활동에 적극적으로 참여해준다는 거에 고마워하고 있으니까."
    m 5 "정말 기뻐."
    show monika zorder 2 at t31
    mc "아니, 별거 아냐, 뭐…."
    play music t8 fadeout 1.0
    show monika zorder 2 at t11
    show sayori zorder 1 at thide
    show natsuki zorder 1 at thide
    hide sayori
    hide natsuki
    m 4b "좋아, 얘들아!"
    m "오늘은 여기까지."
    m "축제날이 다가오고 있긴 하지만, 그래도 내일 시를 써오도록 해."
    m "굉장히 잘 되고 있는 거 같아서, 계속해서 하고 싶어."
    m "축제에 관해선 내일 다 얘기를 끝내자. 그럼 주말에 준비하면 되니까."
    m "월요일은 중요한 날이 될 거야!"
    show sayori 4r zorder 2 at t31
    s "기대된다~!"
    show yuri 4b zorder 2 at t33
    y "할 수 있다… 할 수 있다…."
    mc "좋아."
    hide sayori
    hide monika
    hide yuri
    with wipeleft
    "난 자리에서 일어났다."
    "사요리나 모니카만큼 열정적으로 임할 수 있을지는 몰라도, 일단은 내 최선을 다해야겠다."
    "동아리를 위해서라면…."
    "또 모니카에게 잘 보이려면…."
    "열심히 할 수밖에 없다."
    show sayori 1a zorder 2 at t32
    mc "갈 준비 됐지, 사요리?"
    show sayori at h32
    s 1x "그럼!"
    show natsuki 2d zorder 3 at f33
    n "너희 둘, 요즘 맨날 집에 같이 가는 거 같네."
    show monika 5 zorder 3 at f31
    show natsuki zorder 2 at t33
    m "뭔가 귀엽지, 그치?"
    show monika zorder 2 at t31
    show sayori zorder 3 at f32
    s 1q "에헤헤~"
    show sayori zorder 2 at t32
    mc "에휴, 얘들아…."
    mc "막 대단한 것처럼 얘기하지 마…."
    show natsuki zorder 2 at t44
    show sayori zorder 2 at t43
    show monika zorder 2 at t42
    show yuri 1u zorder 3 at f41
    y "그래도 분명 좋을 거 같은데요…."
    show yuri zorder 2 at t41
    mc "글쎄…."
    mc "아…."
    "이럴 땐 뭐라고 반응을 해야 하는 거지?"
    show sayori zorder 3 at f43
    s 1d "괜찮아, [player]야. 굳이 대답 안 해도 돼."
    show sayori zorder 2 at t43
    mc "…뭐 어쨌든. 빨리 가자."
    scene bg residential_day
    with wipeleft_scene
    $ ch2_winner = poemwinner[1].capitalize()
    if ch2_winner == "Sayori":
        $ ch2_winner = "Yuri"
    "난 오늘도 사요리와 집에 간다."
    "며칠밖에 되지 않았지만, 이미 많은 것들이 바뀌었다."
    "근데 오늘… 사요리가 평소 집에 갈 때보다 조용한 것 같은데…."
    mc "저기, 사요리…."
    show sayori 1k at t11
    s "…."
    s 1n "…미안! 잠깐 넋 넣고 있었어!"
    mc "아, 그래…."
    s 1d "으음…."
    s "전부터 생각하고 있던 건데…."
    s "난 우리가 같이…."
    s 1y "내 말은…."
    "사요리는 조그마한 목소리로 중얼거렸다."
    if ch2_winner == "Yuri":
        s 1a "별 의미는 없는데… 만약 어느 날 유리가 집에 같이 가자고 한다면…."
    else:
        s 1a "별 의미는 없는데… 만약 어느 날 나츠키가 집에 같이 가자고 한다면…."
    mc "뭐어?!"
    s "어떻게 할 거야?"
    mc "무슨 질문이 그래…?"
    mc "정말 곤란하게 만드네…."
    s 1y "에헤헤…."
    if ch2_winner == "Natsuki":
        menu:
            "글쎄…."
            "나츠키와 집에 같이 간다.":
                call ch2_end_natsuki from _call_ch2_end_natsuki
            "계속 사요리와\n집에 같이 간다.":
                call ch2_end_sayori from _call_ch2_end_sayori
    else:
        menu:
            "글쎄…."
            "유리와 집에 같이 간다.":
                call ch2_end_yuri from _call_ch2_end_yuri
            "계속 사요리와\n집에 같이 간다.":
                call ch2_end_sayori from _call_ch2_end_sayori

    "그건 그렇고, 진짜 축제가 며칠밖에 남지 않았네…."
    "무슨 일이 벌어질까?"
    return
label ch2_end_sayori:
    mc "사요리…."
    if ch2_winner == "Yuri":
        mc "내가 널 버리고 유리를 고를 거라고 생각한 거야?"
    if ch2_winner == "Natsuki":
        mc "내가 널 버리고 나츠키를 고를 거라고 생각한 거야?"
    s 1e "에에?!"
    s "하… 하지만…."
    if ch2_winner == "Natsuki":
        s "나츠키는 귀엽고 같이 놀면 재밌으니까…."
    else:
        s "유리는 귀엽고 똑 부러지고…."
    mc "어휴…."
    mc "이미 동아리에서 맨날 보잖아."
    mc "그리고, 집은 항상 너랑 같이 갔었으니까…."
    mc "널 쉽게 버리지 않을 거야."
    s 1y "넌 정말 바보 같다, [player]…."
    s "넌 가끔 보면 날 너무 생각해준다니까."
    if ch2_winner == "Yuri":
        s "유리라면 그 정도는 해 줄 수 있지 않아…?"
    else:
        s "나츠키라면 그 정도는 해 줄 수 있지 않아…?"
    mc "사요리, 난 이미 결정했어."
    mc "가끔 보면 널 정말 이해할 수 없지만…."
    s "미안…."
    mc "게다가, 절대 일어날 리가 없는 일을 물어보는 이유가 뭐야?"
    s 1k "흐음…."
    show sayori at thide
    hide sayori
    "대화는 차츰 잦아들었다."
    "사요리가 이런 걸 물어보다니 좀 이상한데…."
    "그래도 난 사요리와 사요리의 행복을 지켜주고 싶으니까."
    return

label ch2_end_natsuki:
    mc "나츠키랑 같이 집에 간다니…."
    "왜 그 생각만으로 가슴이 뛰는 걸까…?"
    mc "내 말은…."
    mc "내가 만약 거절한다면 나츠키가 나한테 무슨 짓을 할지…."
    s 1x "나츠키, 진짜 귀엽고 재밌지 않아?"
    jump ch2_end_shared

label ch2_end_yuri:
    mc "유리랑 같이 집에 간다니…."
    "왜 그 생각만으로 가슴이 뛰는 걸까…?"
    mc "내 말은…."
    mc "유리한테 인간관계가 무슨 의미인지 아니까, 거절하기 좀 힘들겠는데…."
    s 1x "유리, 진짜 이쁘고 똑똑하지 않아?"
    jump ch2_end_shared

label ch2_end_shared:
    mc "내가 말한 거랑 아무 연관 없잖아!"
    s 4s "아하하! 결국, 인정한 거네!"
    mc "하아…."
    mc "절대 일어날 리가 없는 일을 물어볼 이유는 없잖아."
    s 1d "으음, 글쎄…."
    s "그냥 생각나서 물어봤어."
    s 1y "네가 날 더 이상 필요로 하지 않을 수도 있으니까…."
    mc "필요로 해…?"
    mc "사요리…."
    mc "지금 네가 머릿속으로 무슨 생각을 하는지는 모르겠지만…."
    s "미안…."
    mc "모두들 다 달라…."
    mc "그 어떤 다른 애들도 널 대신할 수는 없어."
    s 1k "으응…."
    s "네가 그렇다면야…."
    show sayori at thide
    hide sayori
    "그 얘기는 끝났지만, 난 기분이 썩 좋지 않았다."
    "이상한 질문으로 사람 곤란하게 만든 건 사요리 잘못이지만…."
    "그래도 거짓말은 할 수 없는걸."
    "하지만 네가 나랑 하교하는걸 좋아하는지 뻔히 아는데, 그걸 내가 앗아갈 리가 없잖아."
    "그래서 내가 일어날 리가 없는 일이라고 했던건데."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
