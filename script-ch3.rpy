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

label ch3_main:
    $ finalConso = finalChecker(player)
    scene bg club_day
    with dissolve_scene_half
    play music t3
    show monika 1g at l31
    m "아, 이런…."
    m "또 내가 마지막이네!"
    mc "아냐, 나도 방금 왔어."
    show yuri 1f zorder 3 at f32
    y "또 피아노 연습하다 오신 건가요?"
    show yuri zorder 2 at t32
    show monika zorder 3 at f31
    m 1l "응…."
    m "아하하…."
    show monika zorder 2 at t31
    show yuri zorder 3 at f32
    y 1m "정말 의지가 강한 분이시네요."
    y "동아리도 시작하시고, 이젠 피아노까지…."
    show yuri 1a zorder 2 at t32
    show monika zorder 3 at f31
    m 1a "글쎄, 의지가 아니라…."
    m "열정이야."
    m "너희가 아니었다면 동아리도 없었을 테니까."
    m 1b "그리고 너희가 축제를 위해 기꺼이 도와준다니 진짜진짜 기뻐!"
    show natsuki 1z zorder 3 at f33
    show monika zorder 2 at t31
    n "으아, 축제 진짜 기대된다!!"
    n "분명히 굉장할 거야!"
    show natsuki zorder 2 at t33
    show monika zorder 3 at f31
    m 1d "에?"
    m "나츠키, 어제만해도 투덜대지않았어?"
    show monika zorder 2 at t31
    show natsuki 2a zorder 3 at f33
    n "뭐, 그랬지만."
    n "난 지금 {i}우리가{/i} 축제에서 낭송회 하는 걸 얘기하는 게 아냐."
    n 4l "하지만 축제는 실컷 놀고 맛있는 걸 마음껏 먹을 수 있는 날이잖아!!"
    show natsuki zorder 2 at t33
    mc "말하는 게 꼭 사요리같네…."
    show natsuki zorder 3 at f33
    n 4a "모니카! 튀긴 오징어 같은 거도 있겠지?"
    show natsuki zorder 2 at t33
    show monika 2a zorder 3 at f31
    m "오징어…?"
    m "갑자기 웬 오징어…?"
    show monika zorder 2 at t31
    show natsuki 2k zorder 3 at f33
    n "아, 쫌."
    n "너 오징어 안 좋아해?"
    n "다른 사람도 아닌 네가?"
    show natsuki zorder 2 at t33
    show monika 1d zorder 3 at f31
    m "에? 안 좋아한다는 뜻은 아니었는데…."
    m "그건 그렇고 ‘다른 사람도 아닌 네가’는 무슨 뜻이야?"
    show monika zorder 2 at t31
    show natsuki 1d zorder 3 at f33
    n "왜냐하면!"
    n "네 이름엔 오징어가 들어가 있잖아!"
    n 4z "모ㄴ-이카!"
    show natsuki zorder 2 at t33
    show monika 5b zorder 3 at f31
    m "에?!"
    m "내 이름은 그렇게 읽는 게 아냐!"
    m "그리고, 그런 농담은 번역하면 성립이 안 되잖아!"
    show monika zorder 2 at t31
    show natsuki zorder 3 at f33
    n 4m "…?"
    show natsuki zorder 2 at t33
    show monika 4l zorder 3 at f31
    m "아, 아니야… 신경 쓰지 마!"
    m "일단은 축제가 중요하니까!"
    show monika zorder 2 at t31
    show natsuki 2a zorder 3 at f33
    n "에헤헤."
    n "알았어, 알았어."
    n "근데 유리나 사요리보다 반응이 재미없네, 넌."
    show natsuki zorder 2 at t33
    show yuri 2h zorder 3 at f32
    y "하아…."
    show yuri zorder 2 at t32
    mc "그런데, 사요리는 어딨는거지…?"
    mc "아, 저기 있구나."
    hide monika
    hide yuri
    hide natsuki
    with wipeleft
    "사요리는 교실 구석에 있는 책상에 멍하니 아래를 보며 앉아있다."
    "난 사요리에게 걸어갔다."
    mc "여, 사요리."
    show sayori 1k zorder 2 at t11
    "나는 사요리의 얼굴 앞에 손을 흔들었다."
    s 1n "에…?"
    mc "또 멍때리고있네."
    s "아, 아…."
    s 4l "에헤헤, 미안…."
    s "난 신경 쓰지 마."
    s 4y "다른 애들이랑 놀고 있어."
    mc "어…."
    mc "너 괜찮아?"
    s 1h "무, 물론이지!"
    s "근데 무슨 일이야?"
    mc "그냥 어디 안 좋나해서…."
    mc "괜히 단정 지어서 미안…."
    s "너, 나 너무 걱정하는 거 아냐?"
    s 4r "난 괜찮아."
    show sayori at h11
    "사요리는 큰 미소를 지어 보였다."
    s 1a "다들 재밌게 노는데 방해하고 싶진 않아."
    mc "그래 그럼…."
    mc "네가 그렇다면 그런 거겠지…."
    show sayori zorder 1 at thide
    hide sayori
    "나는 다른 아이들을 향해 돌아섰지만 걱정이 되어 사요리를 바라보았다."
    "그러나 대화는 이미 끝나있었고, 모두 각자 할 일을 하고 있었다."
    "모니카한테 최근에 사요리에게 무슨 일이 있었는지 물어봐야겠다…."
    "축제준비도 둘이 같이했고, 둘이 같이 있는 시간도 많았으니까."
    "나는 책상에 있는 종이들을 정리하고 있는 모니카에게 쭈뼛대며 다가갔다."
    show monika 2b zorder 2 at t11
    m "[player]! 무슨 일이야?"
    mc "있지, 좀 이상하게 들릴 수 있지만…."
    mc "최근에 사요리한테 무슨 일 있었어?"
    m 1d "무슨 일…?"
    m "어떤 일 말하는 거야?"
    mc "내가 좀 오바하는 걸 수도 있지만 사요리가 좀 우울해 보여서…."
    m "응? 그렇게 생각해?"
    m "별로 그런지 잘 모르겠는데…."
    "모니카가 눈을 들어 사요리를 바라보자, 그냥 책상에 대고 지우개를 문지르는 모습이 눈에 들어온다."
    m "마음속에 걸리는 게 있나 봐…."
    m 2a "나한테 물어보더니 좀 놀랐어, [player]."
    m "나보단 네가 사요리에 대해 잘 알 거 아냐."
    mc "응, 근데 이랬던 적은 없어서…."
    mc "안 좋은 일이 있으면 항상 나한테 제일 먼저 말해줬는데…."
    mc "이번에는 물어보니까 말을 안 해 주더라고."
    mc "…미안, 너랑 관련 있나 해서 물어본 건 아냐!"
    mc "그냥 뭔가 알고있는 게 있나 해서… 됐어. 고마워…."
    m 1g "아냐, 아냐…."
    m "나한테도 중요해."
    m 1e "내 말은, 나도 친구니까…."
    m "그리고 난 부원들의 행복도 책임져야하니까."
    m 1i "내가 한번 얘기해 볼게…."
    mc "에? 괜찮을까…?"
    mc "혼자 있고싶어하는 것 같던데…."
    m "그래?"
    m "혹시 마음에 담아두고 있는 사람 때문에 힘들어 하는 게 아닐까…."
    mc "마음에 담아두다니…?"
    mc "무슨 얘기를 하는 거야?"
    m 2e "으음… 지금 사요리 마음속에 있는 사람은 [player], 너라구."
    mc "나…?"
    mc "어떻게 그런 결론이 나오는 거야?"
    m 1j "글쎄…."
    m "확실하진 않아서 얘기 많이 안 하는 쪽이 좋을 것 같지만…."
    m 1a "사요리가 다른 것보다 너에 대해 많이 얘기하는 거 알아?"
    mc "어…?"
    m "네가 문예부에 들어오고 나서 더 행복해 보였어."
    m "마음속에 켜진 또 다른 빛이랄까…."
    mc "뭐?"
    mc "말도 안 돼…."
    mc "사요리…는 항상 그래왔는걸."
    mc "마음속에 햇빛 가득, 이런 느낌으로 말야."
    mc "평소와 전혀 다르지 않았는데."
    m 5 "에헤헤."
    m "너 진짜 재밌다, [player]."
    m "네가 사요리의 그런 모습만 봐 왔다는 건…."
    m "…네 주변에만 있으면 항상 그랬다는 게 아닐까?"
    mc "…."
    m 1n "아, 미안해. 역시 말 안 하는 쪽이 좋았으려나."
    m "미안해… 사람 관계 사이에 내가 뭘 알겠어."
    m 1a "그런 식으로 결론을 내리려던 건 아니야. 그냥 내가 말한 건 잊어버려."
    m "내가 한 번 얘기해 볼 테니까, 너무 신경쓰지 마."
    mc "아…."
    mc "그래…."
    "모니카가 걱정 말라는 듯 의미심장한 미소를 짓는다."
    "잊어버리라고 말은 했지만…."
    "그런 말을 잊을 수 있을 리가 없잖아."
    show monika zorder 1 at thide
    hide monika
    "모니카가 자리에서 일어나더니 사요리가 앉아있는 쪽으로 간다."
    "책상 옆에 무릎을 꿇고 앉더니 상냥하게 말을 건네는 모습이 보인다."
    "목소리가 너무 작아서 여기서 들리진 않는다."
    "나는 한숨을 내 쉬고 자리에 앉았다."
    "사요리가 걱정하지 말라고 했고, 다른 친구들과 재미있는 시간 보내라고 말은 했지만…."
    "사요리답지 않게 행동하니 그럴 수가 없다."
    "난 얼마나 사요리를 생각하고 있었길래 이렇게나 걱정이 되는 걸까?"
    "이렇게 보니 나도 나답지 않게 행동하는 것 같다…."
    "지금은 모니카를 기다리는 것 말고는 할 수 있는 게 없는 것 같다."





    if n_appeal == 0 and y_appeal == 0:
        jump ch3_start_none
    elif n_appeal > 1:
        jump ch3_start_natsuki
    elif y_appeal > 1:
        jump ch3_start_yuri
    elif poemwinner[1] == "natsuki":
        jump ch3_start_natsuki
    elif poemwinner[1] == "yuri":
        jump ch3_start_yuri
    elif poemwinner[0] == "natsuki":
        jump ch3_start_natsuki
    elif poemwinner[0] == "yuri":
        jump ch3_start_yuri
    else:
        jump ch3_start_none

label ch3_start_natsuki:
    play music t6 fadeout 1
    show natsuki 3c zorder 2 at t11
    n "야, 너."
    mc "에?"
    "고개를 돌려 나츠키를 본다."
    n "너 그냥 그러고 멍때리고 있을 거야?"
    n "축제까지 시간도 얼마 남지 않았는데…."
    mc "아, 미안해."
    mc "걱정하게 하려던 건 아니었어."
    n 1q "거, 걱정이라니 누가!"
    n "난 그냥…."
    "나츠키가 고개를 돌려 아래쪽을 바라본다…."
    "나츠키가 고개를 돌린 쪽의 손엔 만화책이 들려있다."
    mc "그렇네…."
    mc "마음에 걸리는 게 있어서, 근데 이젠 괜찮아."
    mc "지금 갈게."
    n 5n "어휴…."
    n "그렇게 말하면 내가 이상한 사람이 되잖아."
    n "마음에 걸리는게 있으면 혼자 있고 싶다고 얘기를 하던가."
    n 5u "내 말은…."
    n "별로 얘기를 하고 싶지 않다면 말야…."
    "마지막 부분은 중얼거리는 식으로 얘기한다."
    mc "아냐, 따지고 보면 별 일도 아닌데 뭐."
    mc "그냥 사요리 생각좀 하고 있었어."
    n 1p "사, 사요리…?"
    n "생각하고 있었다고…?"
    mc "응, 오늘 좀 기분 안좋아 보였거든."
    mc "근데 아니라고 발뺌하는 거 보고."
    mc "무슨 일 있나 걱정되더라고."
    n 1q "아아…."
    "나츠키가 참았던 숨을 내쉰다."
    n 4w "으응, 일단 좀 말야…."
    n "단어 선택에 좀 더 신경쓰란 말야!"
    n 4c "어쨌든…."
    n "너 걔 절친이잖아, 그렇지?"
    mc "응, 그렇겠지…."
    n "그럼."
    n 3k "걔를 좀 더 믿어줘 봐."
    n "다른 사람 도움이 필요했다면 분명히 다른 사람보다 너에게 갔을 거잖아, 그렇지?"
    mc "사실이긴 하지만…."
    n 3c "왜 왜, 다들 한 번씩은 그런 날 겪잖아."
    n "사요리도 그런 날을 피해갈 수 없었던거고."
    n "진짜로 무슨 일이 있다면, 별거 아니니까 네 걱정을 끼치기 싫은 거겠지"
    mc "응, 분명 그런 투로 얘기하긴 했어…."
    mc "네 말처럼 원하는 대로 혼자 내버려 두는 게 나을지도 모르겠네."
    n 3a "내 말이."
    n "네가 함께 고민해줬으면 하는 일이 있으면 분명히 얘기하겠지."
    mc "그렇네…."
    mc "처음부터 그렇게 생각해야 했는데."
    show natsuki 3q
    "나츠키가 손에 들고 있던 만화책을 만지작거린다."
    n 1q "너…."
    n "너 한테는 많이 중요한 사람인가 보지…?"
    mc "아…."
    mc "괜한 오해는 하지마…!"
    mc "그냥 오랫동안 친구로 지냈을 뿐이고."
    mc "친구가 걱정되는건 당연한 거니까."
    mc "뭐 너도 아까 나 걱정해주긴 했으…."
    n 4w "안 했다니까!!"
    n "어휴… 괜찮아졌으면 빨리 시작하자!"
    mc "네, 네, 알겠습니다…."


    if not n_exclusivewatched and poemwinner[2] == "natsuki":
        call natsuki_exclusive_2_ch3 from _call_natsuki_exclusive_2_ch3
    else:
        jump ch3_start_none
    return

label ch3_start_yuri:
    "왜 누군가 쳐다보고 있다는 느낌이 드는걸까…?"
    "교실을 둘러보았다."
    show yuri 2t zorder 2 at t11
    "유리가 책 위로 빼꼼 쳐다보고 있는 것을 발견했다."
    show yuri 4b
    "눈이 마주치자 얼굴이 빨개져서는 바로 책 뒤로 숨어버린다."
    "이러다간 사회생활은 어떻게 하려고 저러는걸까."
    "그러고 보니 유리가 혼자 누구에게 가서 먼저 말을 거는 걸 본 적은 한 번도 없는 것 같다."
    "그럼 내가 말을 먼저 걸어줘야 맞는거겠지?"
    "뭐, 이제. 말을 걸 수 있을정도로 편해졌기도 하고."
    "자리에서 일어나서 옆자리에 앉는다."
    play music t6 fadeout 1
    y 2v "…."
    y "벼… 별로 방해하려던 건 아니었어요…."
    mc "딱히 한 건 아무것도 없지만 말야."
    y "하지만…."
    y "딱 봐도 혼자서 곰곰이 생각에 잠겨있고 싶어하시던 것 같았는데요…."
    mc "혼자 곰곰이 생각에…?"
    mc "내가 그런 줄은 어떻게 안 거야?"
    y 1t "그게…."
    y "제가 자주 그러거든요…."
    y "그래서 자세나 표정을 볼때 그렇겠구나 생각을 했어요."
    y 3o "바, 바라보고 있었다거나 그런건 아니지만요…!"
    y "저는 그런 무서운 짓 안 해요…!"
    mc "어쨌든 간에, 네 말이 맞는 것 같아."
    mc "걱정 끼쳤다면 미안해."
    y 1s "사과하실 필요는 없어요…."
    y "다른 사람의 문제를 걱정해 주는 사람은 많이 없거든요."
    y "물론 혼자 고민하는 걸 편안하게 느끼는 사람도 있지만요…."
    y "그래도 혹시 원하신다면, 전 들어드릴 준비가 되어 있어요."
    mc "아, 근데 진짜로 별건 아냐…."
    mc "그냥 사요리 때문에 약간 마음이 불편해서."
    y 2t "사요리 씨요…?"
    mc "응… 오늘 조금 기분이 안 좋아 보여서 물어봤더니, 아무것도 아니라고 하더라고."
    mc "그래서 무슨 일 있나 걱정돼서 그래."
    y 3u "그래요?"
    y "그거 로맨틱한걸요…."
    mc "에…?"
    y 4c "죄, 죄송해요!"
    y "이상한 말하려던 건 아니었어요…!"
    mc "그런것보다도 오해는 하지 말아줬으면 해서."
    mc "사요리랑 난 그냥 오랜 친구일 뿐이야."
    y 2l "아… 그렇군요…."
    y 2f "그럼 이상하게 생각하실 법도 하네요…."
    mc "아니면 내가 너무 생각을 깊게 하는 걸지도 몰라…."
    y 1u "[player] 씨…."
    y "우리가 사는 세상은 생각보다 의미심장한 곳이에요. 보이는 게 다가 아니에요."
    y 1s "그리고 사람들은 남에게 보여주는 것보다 숨기는 이야기가 더 많아요. 사람 속을 알면 얼마나 알겠어요."
    mc "아…."
    mc "말 못하는 사정이 있다는 얘기야?"
    y 1l "네…."
    y "전 사요리 씨는 조금 복잡한 사람이라고 생각해요."
    y 1h "사요리 씨의 버릇을 볼 때 본인이 원하는 것과는 다르게 행동할 때가 많아요…."
    y "사요리 씨 본인도 자신이 원하는 게 뭔지 모를수도 있구요…."
    y "저도 오늘은 조금 이상하다고 생각했었으니까요…."
    y "걱정도 되고요."
    y 1f "근데 [player] 씨 같은 경우에는 사요리 씨 생각만 하고 있던 거죠?"
    mc "글쎄…."
    mc "아마도 그랬던 것 같은데."
    y 3u "사요리 씨 말인데요…."
    y "[player] 씨에겐 많이 중요한 사람이죠?"
    mc "아… 응, 그럴지도…."
    mc "그래도 그렇게 말하면 이상한걸!"
    mc "그냥 절친일 뿐이야…."
    y 2t "…."
    "갑자기 유리가 내 눈을 깊게 바라본다."
    "뭔가를 찾는 듯이 부드럽고 궁금하다는 표정을 짓는다."
    "난 부끄러워져서 눈빛을 피한다."
    y 2m "때로는요…."
    y "숨겨진 이야기는 본인에게도 숨겨져 있을 때가 있어요."
    y 2a "그리고 [player] 씨처럼 솔직하고 자상한 사람이라면…."
    y "본인이 몰랐던 감정을 발견하실지도 모르겠네요."
    y 4b "그, 그러니까…."
    y "제 말은…."
    y "사요리씨는 참 운이 좋으신 분 같아요…."
    y "[player] 씨가 있어서요. 저는 그렇게 생각해요."
    mc "유리…."
    mc "난 그렇게 대단한 사람이 아닌걸."
    mc "이렇게나 단순한 사람인데."
    mc "난 내 감정을 잘 알고 있다고 생각해."
    mc "난 너 처럼 복잡한 사람은 아니야."
    y 2t "아, 아…."
    y "방금 그 말…. 칭찬이였던 걸까요?"
    mc "칭찬이라면 칭찬이겠지."
    mc "뭐 어쨌든, 이렇게 같이 앉은 김에, 독서라도 하는 게 어떨까?"
    y 2s "으응…."
    y "괜찮으시다면요."
    mc "그래."
    mc "잠시 마음을 비울 게 필요해서 말야."


    if not y_exclusivewatched and poemwinner[2] == "yuri":
        call yuri_exclusive_2_ch3 from _call_yuri_exclusive_2_ch3
    else:
        jump ch3_start_none
    return

label ch3_start_none:
    if not renpy.music.get_playing(channel='music') == audio.t3:
        stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    "…."
    if not renpy.music.get_playing(channel='music') == audio.t3:
        play music t3
    show monika 4b zorder 2 at t11
    "…."
    show monika 4b zorder 2 at t11
    m "자, 모두들!"
    "조금 시간이 지나자 모니카가 모두의 주의를 집중시킨다."
    m "이제 시를 나누는 게 어떨까?"
    show monika zorder 1 at thide
    hide monika
    "정신을 차려보니 모든 게 정상으로 돌아와 있었다."
    "모두 시를 꺼내고 있어서, 나도 시를 꺼냈다."
    "모니카랑 눈이 마주쳤는데 모니카가 나를 향해 미소짓는다."
    "사요리와는 무슨 말을 나눈 걸까?"
    return


label ch3_end:
    stop music fadeout 1.0
    scene bg club_day
    show monika 4b zorder 2 at t32
    with wipeleft_scene
    play music t3
    m "…자, 너희 셋!"
    m "시는 다 나눠 봤겠지?"
    m "이제 축제에 관해서 얘기를…."
    show natsuki 3c zorder 3 at f31
    n "잠깐만!"
    n "내가 잘못 들은거야, 아니면 네가 말을 이상하게 한 거야?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 4d "에…?"
    show monika zorder 2 at t32
    show yuri 1e zorder 3 at f33
    y "모니카 씨가 뭔가 이상한 말을 하시긴 하셨어요…."
    y "맞아요."
    y 1f "부원들을 부를 때 평소와는 조금 다른 대사를 쓰셨어요."
    show yuri zorder 2 at t33
    show monika 1n zorder 3 at f32
    m "대, 대사?"
    m "난 평소 쓰는 대사 같은 거 없는데…?"
    show monika zorder 2 at t32
    show natsuki 4q zorder 3 at f31
    n "어휴…."
    n "오늘 분위기 왜 이래?"
    n "저것 봐, 유리마저 이상해 하잖아."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "우우…."
    y "침체된 분위기는 뭔가 끔찍한 일이 일어날 걸 예시하는 복선으로 잘 쓰여요…."
    show yuri zorder 2 at t33
    mc "{i}네{/i} 책 속이라면야 그렇겠지!"
    mc "봐봐, 다른 점이라면야 사요리가 없다는 것 뿐이야."
    show yuri 2g zorder 3 at f33
    y "아…."
    y "…그렇네요."
    show yuri zorder 2 at t33
    show monika 2r zorder 3 at f32
    m "하아…."
    m 2d "역시 사요리가 항상 분위기를 띄워주곤 했는데, 그치?"
    m "사요리가 없으니까 왠지 균형 자체가 안 맞는 것 같아…."
    show monika zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "근데 사요리는 대체 어디로 도망간 거야?"
    n "쉬 싸러 간 줄 알았는데."
    show natsuki zorder 2 at t31
    show yuri 1l zorder 3 at f33
    y "나츠키 씨, 품위를 지키시는 게…."
    show yuri zorder 2 at t33
    show natsuki 4w zorder 3 at f31
    n "에이."
    show natsuki zorder 2 at t31
    mc "아, 사요리라면 별로 몸이 안 좋은 것 같다며 아까 먼저 집에 갔어…."
    show yuri 2t zorder 3 at f33
    y "그런가요…?"
    y "괜찮으셔야 할텐데…."
    show yuri zorder 2 at t33
    show natsuki 5c zorder 3 at f31
    n "진심이야?"
    n "수많은 변명 거리 중에서, 몸이 안 좋은 것 같다는 핑계로 같이 안 가고 집에 먼저 보냈다는 게?"
    n "사랑싸움도 정도껏 하시지."
    show natsuki zorder 2 at t31
    mc "잠깐 잠깐!"
    mc "우선 나랑 사요리의 친구 관계를 오해하지 말아 줄래?"
    mc "그리고…."
    mc "사요리가 오늘 날 피하더라고, 그래서 별로 강요하고 싶지는 않았어."
    show yuri 1g zorder 3 at f33
    y "네에에에?"
    show yuri zorder 2 at t33
    mc "{i}다른 사람도 아니고 유리, 네가 그런 반응을 보이는 거야??{/i}"
    show monika 1r zorder 3 at f32
    m "진정해, 얘들아…!"
    m 1d "아까 얘기 같이 해봤고, 별일 아니니까 걱정하지 마."
    show monika zorder 2 at t32
    mc "뭐라고 했는데…?"
    show monika zorder 3 at f32
    show yuri 1e
    m 1a "어쨌든, 축제 준비 나머지는 어떻게 해야할지 정해야 하니까…."
    m "각자 주말동안 어떻게 준비해올지 생각해 보자."
    show monika zorder 2 at t32
    show natsuki 4l zorder 3 at f31
    n "{i}내가{/i} 할 일은 이미 정해져 있잖아!"
    show natsuki zorder 2 at t31
    show monika 2b zorder 3 at f32
    m "그렇네."
    m "나츠키는 컵케이크를 만들기로 했어."
    m "좀 양을 많이 만들어야 하기는 해, 맛도 다르게 말야…."
    m "근데 나츠키, 그 많은 걸 다 혼자서 할 수 있겠어?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4z "그 도전, 받아주지!"
    show natsuki 4a zorder 2 at t31
    show monika zorder 3 at f32
    m 1a "그리고 난…."
    m "시 팸플릿을 정리해서 인쇄할게."
    m "사요리는 팸플릿 디자인을 도와줄 거고."
    m "그리고 유리는…."
    m 1d "…."
    m 3n "유리는… …."
    m "어… 음…."
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "…?"
    show natsuki zorder 2 at t31
    show monika 5 zorder 3 at f32
    m "저, 얘들아…."
    m "유리는 뭘 해야 할지 같이 생각해주면 안될까…?"
    show monika zorder 2 at t32
    show yuri 4c zorder 3 at f33
    y "저…."
    y "전 무능한가봐요…."
    show yuri zorder 2 at t33
    show monika 1g zorder 3 at f32
    m "아, 아니야!"
    m "그런 뜻은 아니었어!"
    m "여기에 너만큼 재능있는 사람이 또 어디 있다고 그래!"
    show monika zorder 2 at t32
    show natsuki 5g zorder 3 at f31
    n "…."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1g "나, 나츠키 너 마저 삐진거야??"
    show monika zorder 2 at t32
    mc "에휴, 내 눈에도 훤하다…."
    mc "보통 사요리는 인정해주지 않는 편인데, 역시 사요리가 없으니 모니카도 고전하네."
    show monika zorder 3 at f32
    m "아…."
    m "그런 것 같네…."
    m 1i "그렇다고 여기서 포기하면 영원히 제자리걸음일 뿐이야."
    m 2i "그러니까, 유리…!"
    m 2a "우리 중에서 손 글씨 제일 예쁜 게 너잖아?"
    m "그럼 네가 현수막이라던가 장식 같은 것 등을 만들어서 이 교실의 분위기를 만들어주면 되겠다."
    show monika zorder 2 at t32
    show yuri 4a zorder 3 at f33
    y "분위기요…?"
    y "그거 말인데요…."
    y "저…."
    y 2r "저 분위기 완전 좋아해요!"
    show yuri 2l
    "책상을 바라보던 유리의 표정이 갑자기 확신의 찬 표정으로 바뀌어 혼자 고개를 끄덕이기까지 한다."
    show yuri zorder 2 at t33
    mc "벌써부터 신났구만…."
    show monika 2b zorder 3 at f32
    m "좋아!"
    m "정말 큰 도움이 될 거야."
    m 2a "그러면…."
    m "[player], 너만 남았네."
    show monika zorder 2 at t32
    mc "진짜 무능한 사람만 말이지."
    show monika 1k zorder 3 at f32
    m "아하하! 그런 얘기 하지 마."
    m 1b "그러고 보니…."
    m "나츠키랑 유리 둘 다 조금 일이 많아진 것 같은데."
    m "둘 중 한 명을 도우면 되겠다."
    m 1m "원한다면 나를 도와줘도 되고…."
    m 1a "분명 큰 도움이 될 거야."
    show monika zorder 2 at t32
    mc "아…."
    mc "그렇다는건…."
    "모니카 말대로라면 난 주말 내내 부원 중 하나랑 보내게 되는 건가?"
    "그런 건의를 부원들이 받아들일 리가 없잖아…?"
    show yuri 1u zorder 3 at f33
    y "아…."
    y "저야, 도와주면 감사하죠…."
    show yuri zorder 2 at t33
    show natsuki 3c zorder 3 at f31
    n "뭐, 제빵에 관한 지식이 전혀 없다고 해도 힘쓸 일은 많을 테니까."
    n 3q "모니카가 나에게 선택권을 줄 일은 없겠지만, 너도 그냥 가만히 앉아 있을 수는 없으니까…."
    "나츠키가 뭔가 막 변명을 지어내려는 것 같다."
    show natsuki zorder 2 at t31
    show yuri 2k zorder 3 at f33
    y "음…."
    y "있잖아요, 나츠키 씨…."
    y 2f "아까 그 정도 양은 어림도 없다는 투로 말씀하셨잖아요."
    y "그리고 언젠가 [player] 씨가 곁에 있기만 해도 멀미가 나시는 것 같다고 말씀하신 적도 있으니까요…."
    y 2i "그렇다면…."
    y "저랑 장식을 만드시는 게 훨씬 나을 것 같은데요."
    show yuri zorder 2 at t33
    show natsuki 4e zorder 3 at f31
    n "잠깐! 내가 언제 그랬어!"
    n 4h "그리고 장식 몇 개 만든다고 힘이 얼마나 든다고 그래?"
    n "너야말로 [player]이랑 함께하고 싶어서 변명을 만드는 거 아니야…?"
    show natsuki zorder 2 at t31
    show yuri 3n zorder 3 at f33
    y "무, 무슨 말씀 하시는거에요?!"
    y "얼마나 세세한 작업인데요…."
    show yuri zorder 2 at t33
    show natsuki 5w zorder 3 at f31
    n "제빵은 안 그렇고?"
    n "너 도대체 생각을…."
    show natsuki zorder 2 at t31
    show monika 2g zorder 3 at f32
    m "얘들아, 얘들아!"
    m "잠깐 좀 진정해봐…."
    m 2d "결국에 돕는 사람은 [player]인데, 무슨 일을 하고 싶을지는 [player]가 정해야 하는 거 아니야?"
    m "그리고…."
    m 5 "[player]는 나랑 같이 있는 시간이 별로 없었다는 거, 몰라?"
    m "분명 [player]이도 나랑 시간을 보내고…."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 4f "너 {i}말 그대로{/i} 방금 고백…."
    show natsuki zorder 2 at t31
    show yuri 2h zorder 3 at f33
    y "저, 저도 놀랐어요!"
    show yuri zorder 2 at t33
    show monika 1l zorder 3 at f32
    m "미안, 미안!"
    m "그냥 한 얘기야…."
    show monika zorder 2 at t32
    show natsuki 4x zorder 3 at f31
    n "어휴…."
    n "그냥 빨리 정하고 끝내면 안 될까?"
    show natsuki zorder 2 at t31
    show monika 1e zorder 3 at f32
    m "그래…."
    m "[player], 괜찮지?"
    m 1a "결국에 정하는 건 너니까."
    show monika zorder 2 at t32
    mc "아…."
    mc "물론."
    show natsuki 5g zorder 3 at f31
    n "흥."
    show natsuki zorder 2 at t31
    show yuri 1f zorder 3 at f33
    y "그렇군요…."
    show yuri zorder 2 at t33
    show monika 1a zorder 3 at f32
    m "그렇다면…."
    show monika zorder 2 at t32
    "모두가 날 똑바로 쳐다본다."
    menu:
        "물론 난 이 사람을 도울 거지만"
        "나츠키.":
            call ch3_end_natsuki from _call_ch3_end_natsuki
        "유리.":
            call ch3_end_yuri from _call_ch3_end_yuri
        "모니카.":
            call ch3_end_monika from _call_ch3_end_monika
        "사요리….":
            call ch3_end_sayori from _call_ch3_end_sayori
    scene bg residential_day
    with wipeleft_scene
    $ ch4_name = ch4_scene.capitalize()
    "말도 안돼!"
    if ch4_name == "Yuri":
        "진짜로 유리가 일요일 내 집으로 오는 거야…?"
    else:
        "진짜로 나츠키가 일요일 내 집으로 오는 거야…?"
    if help_sayori:
        "물론 사요리와 주말을 같이 보내고 싶었지만…."
        if ch4_name == "Yuri":
            "그래도 유리가 내 집으로 온다는 생각에 긴장감이 지붕 끝까지 차오른다."
        else:
            "그래도 나츠키가 내 집으로 온다는 생각에 긴장감이 지붕 끝까지 차오른다."
        "이쯤 되니 상대하기도 편해지기는 했지만…."
        "학교 밖에서 만나는 거니까, 무슨 일이 벌어질지 모르잖아?"
        "걔도 기대된다고 했었고…."
        "난 머리를 흔들어 생각들을 떨치려 노력해본다."
        "왜 사요리한테 들킬까 봐 걱정이 되는 걸까?"
        "서로에게 {i}그런{/i} 감정이 있는 것도 아니고…."
        "애초에 동아리 활동 때문에 만나는 건데."
        "걱정할 거 하나도 없어."
        "계획대로만 하면 되겠지."
    else:
        if ch4_name == "Yuri":
            "그래도 유리가 내 집으로 온다는 생각에 긴장감이 지붕 끝까지 차오른다."
        else:
            "그래도 나츠키가 내 집으로 온다는 생각에 긴장감이 지붕 끝까지 차오른다."
        "이쯤 되니 상대하기도 편해지기는 했지만…."
        "학교 밖에서 만나는 거니까, 무슨 일이 벌어질지 모르니까."
        "그것보다도, 걔도 기대된다고 했었고."
        "혹시 무슨 일이라도 벌어지는 게 아닐까?"
        "…아직은 너무 이른가?"
        "시간이 말해 주겠지…."
        "그때 까진 마음이 계속 쓰일 것 같은걸."
        "정말로 기대된다!"
    return

label ch3_end_sayori:
    $ help_sayori = True
    mc "으음…."
    mc "아무나 도와줄 수 있다면, 사요리를 돕고 싶어."
    mc "이웃이기도 하고,"
    show yuri 2f zorder 3 at f33
    y "하지만 모니카 씨가 방금…."
    show yuri zorder 2 at t33
    show natsuki 4w zorder 3 at f31
    n "방금 사요리는 모니카를 도와주기로 했다고 했잖아!"
    n "어휴…."
    n 4h "우리가 그렇게나 싫은 거야?"
    show natsuki zorder 2 at t31
    mc "아, 아냐!"
    show monika 1e zorder 3 at f32
    m "미안해, 곤란하게 하려던건 아니었는데…."
    show monika zorder 2 at t32
    menu:
        m "문예부를 생각해, 알았지?"
        "나츠키.":
            call ch3_end_natsuki from _call_ch3_end_natsuki_1
        "유리.":
            call ch3_end_yuri from _call_ch3_end_yuri_1
        "모니카." if help_monika == None:
            call ch3_end_monika from _call_ch3_end_monika_1
    return


label ch3_end_monika:
    $ help_monika = True
    mc "그럼 난 모니카를 도울게…."
    show monika 5 zorder 3 at f32
    m "날 선택했구나!"
    show monika zorder 2 at t32
    show natsuki 3e zorder 3 at f31
    stop music fadeout 1.0
    n "잠깐만!"
    show natsuki zorder 2 at t31
    show yuri 2r zorder 3 at f33
    y "마, 맞아요!"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    play music t7
    n "모니카, 우리 셋 중에 도움이 제일 필요 없는 건 너잖아!"
    show natsuki zorder 2 at t31
    show monika 1d zorder 3 at f32
    m "에? 그치만…."
    show monika zorder 2 at t32
    show yuri 1h zorder 3 at f33
    y "저도 나츠키씨랑 동감이에요."
    y 1l "이미 한 사람만 해도 충분한 일인 데다가…."
    y "사요리 씨도 돕기로 했잖아요."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 1p "하지만 선택한 건 [player]이였잖…."
    m "아…."
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "그게 상관 있는게 아니잖아."
    n "애초에 자기를 선택하라고 부담을 막 준 사람이 너였잖아."
    n 3e "모니카, 넌 문예부 부장이야."
    n "동아리 안에서 가장 합리적인 선택을 해야 하는 사람은 바로 너라고!"
    show natsuki zorder 2 at t31
    show yuri 2f zorder 3 at f33
    y "모니카 씨, 그런 속셈이 이런 선택을 불투명하게 만들어서는 안 돼요."
    show yuri zorder 2 at t33
    show monika 2i zorder 3 at f32
    m "속셈이라고?"
    m "유, 유리, 무슨 소리를 하는 거야?"
    m "것보다 마음속에 속셈이 가득 담긴 너희가 할 말은 아니지!"
    show monika zorder 2 at t32
    show natsuki 1x zorder 3 at f31
    n "{i}뭐라고{/i}?"
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m "아니라면 이렇게 별일 아닌 일이 싸움으로 번지지 않았을 거 아냐!"
    show monika zorder 2 at t32
    show yuri 3r zorder 3 at f33
    y "그건…. 사실이 아니에요, 모니카 씨!"
    show yuri zorder 2 at t33
    show natsuki 3e zorder 3 at f31
    n "맞아!"
    n "할 일이 많은 건 우리잖아, 너도 잘 알면서!"
    n "혼자서 하면 제대로 안 될지도 모른단 말야."
    show natsuki zorder 2 at t31
    show monika 1p zorder 3 at f32
    m "아… 그럴지도… 모르겠네…."
    show monika zorder 2 at t32
    show yuri 2l zorder 3 at f33
    y "문예부를 생각해요, 모니카 씨…."
    y "축제 행사를 성공적으로 이끌려면, 인력을 잘 배분해야 해요."
    show yuri zorder 2 at t33
    show monika 3n zorder 3 at f32
    m "음…."
    m "어…."
    show monika zorder 2 at t32
    show natsuki 4x zorder 3 at f31
    n "그래서 어떻게 하실 건가요, {i}부장{/i}님?"
    show natsuki zorder 2 at t31
    show monika 1p zorder 3 at f32
    m "알았어, 알았어!"
    m "알겠다고"
    stop music fadeout 1.0
    show natsuki 4g
    show yuri 2g
    m 1r "어휴…."
    m 1g "역시 [player]가 둘 중 하나를 돕는 게 가장 낫겠지."
    m "그러니까…."
    m 1c "그렇게… 하는 게 좋을 것 같아."
    show monika zorder 2 at t32
    play music t3
    menu:
        m "[player], 혹시 돕고 싶은 사람이 있어?"
        "나츠키":
            call ch3_end_natsuki from _call_ch3_end_natsuki_2
        "유리":
            call ch3_end_yuri from _call_ch3_end_yuri_2
        "사요리…." if help_sayori == None:
            call ch3_end_sayori from _call_ch3_end_sayori_1
    return

label ch3_end_natsuki:
    $ ch4_scene = "natsuki"
    mc "뭐, 제빵이 재밌을 것 같기도 하고…."
    mc "그리고 들어보니까 일이 많을 것 같은데. 두 사람은 필요하지 않겠어?"
    show natsuki 4l zorder 3 at f31
    n "걱정마!"
    n "제빵은 진짜 재밌으니까!"
    n "너도 분명 그렇게 생각할 걸!"
    show natsuki zorder 2 at t31
    show monika 1d zorder 3 at f32
    m "에?"
    m "나츠키 너 방금 전에 분명히…."
    show monika zorder 2 at t32
    show natsuki 1q zorder 3 at f31
    n "그, 그건!"
    n "…."
    n "…신경 안 써도 돼. 알겠지?"
    show natsuki zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "뭐, 어쨌든…."
    m "유리, 넌 혼자 괜찮겠어?"
    show monika zorder 2 at t32
    show yuri 1j zorder 3 at f33
    y "물론이죠."
    y "이미 익숙한걸요…."
    show yuri 1g zorder 2 at t33
    show monika 1e zorder 3 at f32
    m "…."
    show monika zorder 2 at t32
    mc "…."
    show monika zorder 3 at f32
    m 1n "그거… 다행이네…."
    "좀 과장된 반응이기는 하지만, 그러면 마음이 약해지잖아…."
    show monika 1m zorder 2 at t32
    show natsuki 3a zorder 3 at f31
    n "그럼 다 된 거지?"
    n "혹시 다른 얘기 남은 거 있어?"
    show natsuki zorder 2 at t31
    show monika 1a zorder 3 at f32
    m "아니, 아무래도 다 정해진 것 같은데…."
    m "어때? 기대되지 않아?"
    show monika zorder 2 at t32
    show natsuki 1z zorder 3 at f31
    n "응!"
    n "낭송회 빼고는 다 재밌을 것 같은데!"
    show natsuki 1a zorder 2 at t31
    mc "그런 말은 하나 마나인 것 같은데…."
    show monika zorder 3 at f32
    m "[player]야, 넌 어때?"
    show monika zorder 2 at t32
    mc "나?"
    mc "아, 결과가 기대되긴 하네…."
    show monika 2b zorder 3 at f32
    m "그럼 다행이네!"
    m "유리야, 넌 어때?"
    m 2d "…유리야?"
    show monika zorder 2 at t32
    show natsuki 3c zorder 3 at f31
    n "아직 부루퉁한 모양인데."
    show natsuki zorder 2 at t31
    show yuri 4b zorder 3 at f33
    y "…."
    show yuri zorder 2 at t33
    show natsuki 5n zorder 3 at f31
    n "…."
    "내가 볼 땐 그건 나츠키 너도 마찬가지인 것 같은데."
    n "어차피…."
    n 5m "내 말은, 그게 그렇게 큰일도 아니고…."
    show natsuki zorder 2 at t31
    mc "그렇게 간단한 문제는 아닌 거 같은데…."
    show natsuki zorder 3 at f31
    n "…?"
    show natsuki zorder 2 at t31
    mc "이래저래 인정받지 못했잖아. 그래서 꽤나 속상해하는 거 같은데."
    mc "뭘 잘하는지 몰라서 고민하고 고민해서 겨우 찾아낸 거라던가, 그렇게 찾아준 일을 도와주지 않는다던가."
    show natsuki zorder 3 at f31
    n 5q "그래도 그게…."
    n "…."
    n 5r "우우…."
    show natsuki 5u
    "나츠키는 걱정된 표정으로 모두를 번갈아 바라본다."
    n 1u "저어…."
    "나츠키가 유리 뒤로 가서 유리의 어깨에 손에 올린다."
    n 1h "유리."
    n "여기 너만한 사람 없는 거 알지."
    n "그리고…."
    n "이 행사를 재밌고 환영적인 분위기로 만들어 줄 사람이 너라는것도."
    n 1q "그러니까, 물론 컵케이크가 그런 분위기를 만드는 데 도움을 주긴 하겠지만…."
    n 3h "전체적인 장식은 네가 담당하는 거니까."
    n "행사 때 사람들이 어떤 느낌을 받을지 정하는 건 네가 되는 거니까."
    n "그러니까…."
    n 4w "바보처럼 굴지 말고 힘내란 말야!"
    "나츠키가 어깨에서 손을 떼 다른 쪽을 본다."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 4a "…."
    y "방금 그거… 진심 아니시죠?"
    show yuri zorder 2 at t33
    show natsuki 5u zorder 3 at f31
    n "으응…."
    n "그런건 아니지만…."
    show natsuki zorder 2 at t31
    "놀란 건 유리뿐만이 아니다."
    "나와 모니카도 나츠키의 말에 깜짝 놀랐다."
    "다른 사람도 아니고 나츠키가 그런 격려의 말을 하다니."
    "그래도, 상황이 조금씩 이해가 가기 시작한다."
    "나츠키는 사요리 흉내를 낸 거다."
    "제대로 되진 않은 모양이지만, 이럴 때 사요리라면 어떻게 말했을까 하고 생각해서 말한 거겠지."
    "왜냐하면 사요리는 항상 모두를 웃게 하고 격려해줬으니까."
    show yuri 2l zorder 3 at f33
    y "바보처럼 굴어서… 죄송해요."
    y 2i "저도 최선을 다할게요."
    y "모두 다 최선을 다해서 행사를 성공적으로 끝내는 거예요!"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 5j "응."
    show natsuki zorder 2 at t31
    show monika 2k zorder 3 at f32
    m "응!"
    m 2b "다들 정말 최선을 다했으면 좋겠네."
    m "그래도…."
    m "오늘은 이게 다야."
    m "다들 이제 집에 가도 돼."
    show monika zorder 2 at t32
    show natsuki 3k zorder 3 at f31
    n "알았어, 근데 난 좀 더 있을게."
    n "오늘 독서라곤 하나도 못했거든…."
    show natsuki zorder 2 at t31
    show monika 2a zorder 3 at f32
    m "응, 알았어. 문제 될 건 없으니까."
    hide natsuki
    hide monika
    hide yuri
    with wipeleft
    "다들 가방을 싼다."
    "모니카와 유리가 얘기하며 교실 문을 따라나서자, 나도 그 뒤를 따라간다."
    play music t6 fadeout 1
    show natsuki 4g zorder 2 at t11
    n "저기, 넌 어디가는거야?"
    mc "에…?"
    n 4c "언제 어떻게 만날지 아직 얘기도 안 했잖아."
    n "그러다 집에 가서 뒤늦게 연락할 방법이 없다는 걸 알면 그때는 어쩌려고."
    mc "아, 그렇네…."
    mc "왜 그 생각을 못했을까?"
    n 2c "어휴, 내가 멈춰 세웠으니 다행이지."
    n "자, 이거 내 번호니까."
    n 2q "괜히 번호 받았다고 이상한 생각하지 마!"
    mc "내가 왜 그러겠어…?"
    n 1s "흥…."
    "나츠키의 번호를 받았다."
    n 1c "좋아…."
    n "일요일 날 갈 테니까."
    n "재료는 내가 다 준비해 둘게."
    mc "잠깐만!"
    mc "지금 {i}내{/i} 집으로 온다고?"
    n 2c "응."
    n "무슨 문제라도 있어?"
    mc "아니 내 말은…."
    mc "도와주는 사람은 나니까, 내가 너희 집으로 가는 거라고 생각했거든…."
    n "그렇네."
    n 5x "근데 내가 남자를 집에 데려가면…."
    n "아빠가 날 죽이려 들걸."
    mc "진짜?"
    mc "좀 엄격한 분이신가 보네."
    n 5r "그래, 내 기분이 어떨 거 같아?"
    n "집에 아빠가 있으면 아무것도 못 하겠어…."
    n 2q "그냥… 잠깐 불평 좀 하고 싶었어."
    n 2c "뭐 어쨌든 서로 번호교환 했으니까."
    n "볼일은 그게 다야."
    n "갈 때 되면 문자 보낼게."
    mc "알았어."
    n "그래."
    n 4a "내가 제빵을 왜 그렇게 좋아하는지 똑똑히 알려줄 테니까."
    n "기대하는 게 좋을 거야."
    mc "어?"
    mc "아까는 힘쓰는 일 맡긴다고 하지 않았어?"
    n 1r "그건 말야!"
    n "그냥… 한 말이야."
    n 1q "남들 앞에서… 티 내고 싶지 않아서…."
    n "이런 일 기대하고 있었다는 거."
    mc "뭐? 진짜??"
    n 5w "그냥 그렇다고!"
    n "그냥… 다른 사람이랑 제빵 해본 적 없으니까."
    n 5h "그게 다야, 그러니까…."
    mc "알았어."
    mc "오버해서 미안해."
    mc "어쨌든 난 이만 가니까."
    mc "일요일날 봐."
    n 5m "저기"
    n "…."
    n 5u "…아냐 아무것도."
    return

label ch3_end_yuri:
    $ ch4_scene = "yuri"
    mc "아무래도 유리를 도와주는 게 더 도움이 될 거 같은데…."
    show yuri zorder 3 at f33
    y 2n "저, 저요…?"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4e "진심이야?"
    n "도대체……."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "나츠키."
    m "그 다음에 무슨 말 할지 뻔히 알겠다."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5r "아, 아냐…."
    n "난 그저…."
    n "윽…."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 2a "그럼 [player]이는 유리를 돕는거네?"
    show monika zorder 2 at t32
    mc "응."
    mc "그러려고."
    show yuri zorder 3 at f33
    y 1u "기뻐요."
    y "전 뭐든지 너무 깊게 생각하는 버릇이 있거든요…."
    y "정말 큰 도움이 될 거에요."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "그렇다니 다행이네."
    m "나츠키, 혼자 괜찮겠어?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 3w "어."
    n "괜찮을거라고 했잖아."
    show natsuki zorder 2 at t31
    show monika zorder 3 at f32
    m 1i "좋아, 좋아…."
    "티 안 내려고 하지만 나츠키가 화가 났다는 건 누구라도 알 수 있었다."
    show monika zorder 2 at t32
    mc "그럼… 정할 건 이게 다야?"
    show monika zorder 3 at f32
    m 1a "응, 이게 다인 것 같네."
    m 2a "정말 막 들뜨지 않아?"
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 1i "'들뜨다' 라는 표현을 쓰기는 조금 그렇지만요…."
    y "조금 기대된다고는 할 수 있겠네요."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m "[player]야, 넌 어때?"
    show monika zorder 2 at t32
    mc "나?"
    mc "아, 결과가 기대되긴 하네…."
    show monika zorder 3 at f32
    m 2b "그럼 다행이네!"
    m 2a "나츠키, 넌 어때?"
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n 5s "…."
    show monika zorder 2 at t32
    show yuri zorder 3 at f33
    y 2h "나츠키 씨!"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1o "뭐!"
    n 1m "왜 다들 나한테 소리 지르는 거야?"
    n "내가 뭘 한 것도 아니고…!"
    show natsuki 1n zorder 2 at t31
    show yuri zorder 3 at f33
    y 3n "아, 아뇨!"
    y "전 그런 뜻이 아니었어요!"
    y 3o "아, 아…."
    "유리가 걱정스럽게 주변을 둘러본다."
    y 2w "죄송해요!"
    y 2v "[player] 씨가 왜 저를 돕기로 했는지는 저도 몰라요…."
    y "그리고…."
    y 2t "나츠키 씨가 만드는 컵케이크는 제가 먹어본 것 중에서 제일 맛있어요!"
    y "제 차와도 정말 잘 어울리는걸요!"
    y "제가 축제 준비하는 건 나츠키 씨 컵케이크에 비하면 아무것도 아닌걸요…."
    y 4b "그러니까…."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 3q "알겠어, 알겠어."
    n 3h "그냥 놀라서 그래…."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y "왜, 왜요?"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 3q "어…."
    n "아니, 내가 너무 어린애처럼 구는 것 같아서…."
    n "그거에 좀 속상해 하고 있었는데…."
    n 5h "근데 네가 갑자기 격려를 하려고 그러니까…."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y "벼, 별로 잘 못한다는건 알고 있어요…."
    y 2v "혹시 이상한 말 했으면 죄송해요!"
    "놀란건 나츠키 뿐 만이 아니다."
    "모니카와 나도 유리의 말에 깜짝 놀랐다."
    "말재주가 없고 수줍어하는 유리답지 않게 누구를 격려하려고 하니까."
    "그래도, 상황이 조금씩 이해가 가기 시작한다."
    "유리는 사요리 흉내를 낸 거다."
    "제대로 되진 않은 모양이지만, 이럴 때 사요리라면 어떻게 말했을까 하고 생각해서 말한 거겠지."
    "왜냐하면 사요리는 항상 모두를 웃게하고 격려해줬으니까."
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 1h "아냐…."
    n "고마워."
    n 1u "미안해… 괜히 큰일 난 것처럼 굴고."
    n 1m "그래도 이 말은 해야겠어."
    show natsuki zorder 2 at t31
    show yuri zorder 3 at f33
    y 2e "…?"
    show yuri zorder 2 at t33
    show natsuki zorder 3 at f31
    n 4e "축제에서 제일가는 컵케이크를 만들어 올 테니까!"
    show natsuki 4a zorder 2 at t31
    show yuri zorder 3 at f33
    y 2f "아…."
    y 1s "…믿을게요."
    show yuri zorder 2 at t33
    show monika zorder 3 at f32
    m 2b "응!"
    m "다들 정말 최선을 다했으면 좋겠네."
    m "그래도…."
    m "오늘은 이게 다야."
    m "다들 이제 집에 가도 돼."
    show monika zorder 2 at t32
    show natsuki zorder 3 at f31
    n "좋아, 그럼 가자."
    hide monika
    hide natsuki
    hide yuri
    with wipeleft
    "다들 가방을 싼다."
    "모니카와 나츠키가 떠들며 교실 문을 따라나서자, 나도 그 뒤를 따라간다."
    play music t6 fadeout 1
    show yuri 2t zorder 2 at t11
    y "저, 저기요!"
    mc "응?"
    "난 뒤돌아봤다."
    y "죄송해요…."
    y 2s "이번 주말에 연락할 방법이 없다는 걸 깨달아서…."
    mc "아, 그러네."
    mc "흠…."
    mc "내 전화번호 알려줄게."
    y 1a "네, 그게 가장 좋은 방법이겠네요."
    mc "좋아, 그럼…."
    "유리와 나는 서로 전화번호를 교환했다."
    y "좋아요."
    y "그러면, 일요일에 [player] 씨 집 앞에서 뵐게요…."
    mc "응?"
    mc "우리 집?"
    y 2t "무, 무슨 문제 있나요…?"
    mc "아니, 그런 건 아닌데…."
    mc "내가 널 도와주는 거니까, 당연히 너희 집에 간다고 생각했거든."
    y "아, 그 말도 맞긴한데…."
    y "하지만, 괜찮다면…."
    y 1u "[player] 씨 집에서 하는 게 좋을 것 같아서요."
    mc "좋아."
    mc "그럼 그렇게 하자."
    "난 굳이 유리에게 이유를 물어보지 않기로 했다."
    "누구 집에서 보든 상관 없었으니, 그냥 방 청소나 열심히 하기로 했다."
    mc "내가 도움이 됐으면 좋겠네…."
    mc "난 너처럼 별로 창의력이 풍부하지는 않거든."
    y 1a "너무 자신을 과소평가하지 마세요, [player] 씨."
    y "제 생각에 저희는 아주 잘 맞을 거에요."
    y 1u "혹시 절 고르셔서 기분이 나쁘거나 하신다면…."
    mc "잠깐…!"
    mc "진심으로 하는 소리야?"
    y 4b "…."
    y "잘… 모르겠어요."
    y "저를 고르신 이유가 잘 떠오르지 않는걸요…."
    mc "가장 평범한 이유를 잊고 있어!"
    mc "내가 널 고른 걸 단순히 널 돕고 싶어서야."
    y 2v "하, 하지만…."
    "유리는 과하게 긴장한 표정으로 생각하고있었다."
    mc "유리… 너무 많이 생각하지 마."
    mc "네가 그러고 있을 때 내가 지적해 주길 바랬던 거지, 그렇지?"
    y "에…?"
    y 4 "전 몰랐는데…."
    mc "내가 말했지, 내가 원해서야."
    mc "그게 전부야."
    mc "내 말 믿지?"
    y 1t "저는…."
    "다시 열심히 생각하고 있다."
    "유리는 내 눈을 긴 시간 동안 뚫어져라 쳐다봤다."
    y 3l "…저는 믿어요!"
    "유리는 엄청난 노력을 쏟아 그 말을 하고 그제야 표정을 풀었다."
    y 3s "그리고 일요일이 정말 기대되네요."
    mc "응…."
    mc "나도 그래."
    show yuri zorder 1 at thide
    hide yuri
    "번호교환을 끝내고, 난 문을 나서고 유리가 그 뒤를 따랐다."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
