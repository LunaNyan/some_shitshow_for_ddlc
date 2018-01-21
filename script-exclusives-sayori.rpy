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

label sayori_exclusive_1:
    scene bg club_day
    with wipeleft_scene
    if not renpy.music.get_playing(channel='music') == audio.t2:
        play music t2 fadeout 1
    "하아…."
    "오늘은 누구에게도 방해받고 싶지 않다."
    "나는 가까운 책상에 앉아 엎드렸다."
    "어떻게 내가 이렇게 문학에 관련된 무언가를 직접 떠맡게 된 거지?"
    "유리가 준 책을 읽을까 하지만…."
    "…오늘은 읽기에는 너무 피곤하다."
    "금방 잠이 들어버릴 것 같다."
    "나는 눈을 감고 사요리와 모니카가 하는 대화를 엿들었다."
    show sayori 1g zorder 2 at t21
    s "우리, 다른 동아리에 비해서 진짜 게을러진 것 같아…."
    show monika 2r zorder 3 at f22
    m "흐음…."
    m 2b "글쎄, 아직 포기할 수는 없어."
    m "축제야말로 모두에게 문학이 뭔지 보여줄 기회니까!"
    m 2d "문제는 문예부라는 게 너무 복잡하고 지적으로만 보인다는 거지…."
    m "하지만 그렇지만은 않잖아, 그치?"
    m 2a "우린 그걸 사람들에게 보여줄 방법이 필요해…."
    m "사람들의 창의적인 마음을 깨우는 방법이…."
    show monika zorder 2 at t22
    show sayori zorder 3 at f21
    s 1i "으으으음……."
    s "그렇다고 문제는 해결되진 않아!"
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 2d "응? 그게 무슨 말이야?"
    show monika zorder 2 at t22
    show sayori zorder 3 at f21
    s 1c "우리가 재밌는 일을 한다고 해도…."
    s "그게 문학에 관련된 행사라면 아무도 안 올 거야."
    s "그러니까 사람들에게 좋은 첫인상을 각인시켜야 하는 방법을 찾아야 해."
    s 1a "그리고 그 사람들이 찾아오면, 창의적인 마음은 그때 가서 깨우면 되는 거야."
    "…뭐지?"
    "사요리가 진지하게 얘기하고 있다니…."
    "사요리가 이런 식으로 고민하는 건 굉장히 희귀한 일이다."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 2a "흠, 좋은 지적이야…."
    m "그러면, 음식이 효과가 있겠지?"
    show monika zorder 2 at t22
    show sayori zorder 3 at f21
    s 1n "어, 어떤 음식?!"
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 2b "글쎄… 아, 그러면…."
    show monika zorder 2 at t22
    show sayori 4r zorder 3 at f21
    s "컵케이크!"
    show sayori zorder 2 at t21
    show monika 1k zorder 3 at f22
    m "아하하. 좋은 생각이야."
    m 1a "나츠키가 좋아하겠네."
    show monika zorder 2 at t22
    show sayori zorder 3 at f21
    s 4x "아! 맞아!"
    s "나츠키는 엄청 맛있는 컵케이크를 만들지!"
    s "엄청 잘 됐다~"
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1d "그래서 제안한 거 아냐…?"
    show monika zorder 2 at t22
    show sayori zorder 3 at f21
    s 4q "컵케이크가 내 창의적인 위장에 말을 걸고 있어~"
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1l "…."
    m "그럼, 컵케이크로 하자."
    show monika zorder 2 at t22
    show sayori zorder 3 at f21
    s 1g "배고파아…."
    show sayori zorder 2 at t21
    show monika zorder 3 at f22
    m 1a "어쨌거나, 축제에 대해 자세히 얘기할 필요가 있어…."
    scene black
    with close_eyes
    "나는 웃었다."
    "얘기가 끝나자, 사요리는 평소의 자신으로 돌아왔다."
    "하지만 여기엔 내가 사요리를 존경할 수밖에 없는 이유가 있다."
    "나같이 동기 부여를 찾는 데 어려움을 겪고 있는 사람과는 다르게…."
    "사요리는 주어진 일에 마음을 쏟아부어, 그것이 살아나게 한다."
    "그래서 사요리가 이렇게 저렇게 끼어들어도 내가 가만히 있는 거고…."
    "사요리의 눈으로 보는 세상은 어떤 세상일까…."
    scene bg club_day
    show sayori 1b at face
    with open_eyes
    mc "으아악!"
    "눈을 뜨자 사요리의 얼굴이 내 시야를 꽉 채우고있었다."
    "난 거의 의자에서 떨어질 뻔했다."
    show sayori zorder 2 at t11
    s 4q "에헤헤, 미안~"
    s 4i "잠깐만!"
    s 1j "생각해보니, 별로 미안하지 않아!"
    s "이런 식으로 잔 건 네 잘못이지!"
    s "여긴 낮잠 동아리가 아니야!"
    mc "우리 학교에 낮잠 동아리도 있었나…?"
    s 1h "너 어제 또 늦게 잤지?"
    s "이제 동아리에 가입했으니까, 애니 같은 거 보는 시간 좀 줄여!"
    s "그러다 버릇된다!"
    mc "너, 너무 크게 말하지 마…!"
    "난 혹시 모니카가 듣지 않았을까 하고 슬쩍 눈치를 보았다."
    s 1g "그래도 사실이잖아…."
    mc "그래…."
    mc "알았어, 알았어."
    mc "넌 항상 내 걱정을 하는구나, 사요리."
    s 4q "에헤헤~"
    s "그게 가장 내가 열심히 하는 거지!"
    mc "…그게 문제야!"
    mc "네 생각도 좀 하라고."
    mc "넌 네 걱정보다 내 걱정을 더 많이 하잖아."
    mc "넌 매일 늦잠을 자잖아, 그렇지?"
    s 1l "에?"
    s "매일은 아니야!"
    mc "별로 설득력이 없는데…."
    mc "지난주에 제시간에 일어난 적이 얼마나 되는데?"
    s 1m "그건…."
    s 1o "…비밀이야!"
    mc "됐다…."
    s 5a "제바알!!"
    s "적어도 의심은 해줘…."
    mc "못 하겠는데."
    mc "사요리, 너한테 다 써있으니까."
    s 1b "에…?"
    "사요리는 자기 자신을 한번 훑어보았다."
    s "나한테 다 쓰여 있다고?"
    mc "너 오늘 아침에 분명 서둘렀겠지…."
    mc "봐봐, 네 머리가 다 뻗쳐있잖아."
    show sayori at h11
    s 1e "아…."
    "나는 사요리의 머리를 정리해주려고 손가락 끝으로 이리저리 움직여봤다."
    mc "야, 머리 좀 빗고 다녀라…."
    s 1y "내 머리는 원래 잘 정리가 안 돼…."
    mc "그런 핑계는 안 통해."
    mc "네 머리만 말하는 게 아냐."
    mc "리본도 정리되어있지 않잖아."
    mc "옷깃에는 치약 자국도 묻어있네."
    "나는 손가락으로 얼룩을 지워보려고 했다."
    show sayori at s11
    s "그래도 아무도 모를 텐데…."
    mc "당연히 알지."
    mc "그냥 네가 부끄러울까 봐 아무도 말 안 해주는 거야."
    mc "다행히도, 난 별로 신경 안 쓰니까."
    s 5c "진짜 못됐어…."
    mc "단추도 안 잠그고…."
    mc "진지하게, 사요리…."
    mc "왜 네가 아직도 남자친구 없다고 생각해?"
    show sayori 1h zorder 2 at t11
    s "에??"
    s "그건 {i}진짜{/i} 너무해!"
    mc "미안, 그래도 나중에 나한테 감사해야 할 걸…?"
    "난 아래에서부터 사요리의 단추를 잠궈줬다."
    mc "얼마나 깔끔해졌는지 보면, 마음이 바뀔 거야."
    $ persistent.clear[6] = True
    scene s_cg1
    with dissolve_cg
    s "에헤헤~"
    s "되게 웃기다."
    mc "뭐가?"
    s "글쎄…."
    s "이런 걸 해주는 친구가 있다는 게 얼마나 이상한 일인가 생각하고 있었어."
    mc "응?"
    mc "그런 말 하지 마!"
    mc "{i}내{/i} 기분이 이상해지잖아, 바보야…."
    s "괜찮아."
    s "난 우리가 이러는 게 되게 좋은 걸."
    s "넌 안 그래?"
    mc "아…."
    mc "아, 아마도…."
    s "야, 조심해…."
    s "단추 뜯어지겠다!"
    mc "이건 왜 이렇게 잠그기 힘들지…?"
    "난 사요리 가슴팍 쪽에 있는 단추와 씨름을 하고 있다."
    mc "이 옷, 너한테 맞기는 하는 거야?"
    s "에헤헤~"
    s "내가 살 때는 딱 맞던데."
    mc "하아…."
    mc "제대로 잠그기만 했어도, 안 맞는 옷이라는 걸 금방 알았을텐데."
    mc "…뭘 그렇게 웃고 있어?"
    s "내 가슴이 커졌다는 뜻이잖아!"
    mc "크, 큰소리로 말하지 마!!"
    s "에헤헤~"
    mc "어쨌든…."
    mc "보기 좋네…."
    mc "아…."
    "…사요리의 교복이 저렇게 단추가 채워져 있는 걸 보는 게 왜 이렇게 기분이 이상할까?"
    s "근데 너무 답답해…."
    s "우으…."
    s "불편하기만 하잖아!"
    "사요리는 재빠르게 단추를 전부 풀어헤쳤다."
    scene bg club_day
    show sayori 1q zorder 2 at i11
    with dissolve_cg
    s "휴우!"
    s "훨씬 낫네~"
    "사요리는 팔을 내밀고 몸을 이리저리 꼬았다."
    s 1a "그럼 계속 풀고 있으면 남자친구가 안 생긴다는 거네?"
    mc "그게 무슨 논리야?"
    mc "그리고 그게 왜 좋은 것처럼 말 하고 있어?"
    s "왜냐하면…."
    s 4h "…내가 남자친구가 생기면, 네가 이런 걸 하게 냅두지 않을 거 아냐!"
    s 4y "그리고 넌 날 가장 잘 챙겨주니까…."
    s "그래서 풀고 있을 거야!"
    mc "부끄러운 말 좀 하지 마!"
    s 1b "에?"
    s "별로 부끄러운 말 같은 거 안 했는데…."
    mc "이런…."
    mc "뭐 어쨌든, 일찍 일어나려고 노력해봐…."
    s 1j "네가 일찍 자려고 노력한다면!"
    mc "알았어, 알았어…."
    mc "약속이다."
    s 4q "에헤헤~"
    s 4x "내 생각엔 우리는 자기 자신을 챙기는 거보다 서로를 챙겨주는 걸 더 잘 하는 거 같아."
    mc "응, 그런 거 같네…."
    s 4y "그러니까 아침에 깨우러 와야 해!"
    mc "또 그런다, 사요리…."
    s 1h "하지만 그땐 장난친 거였어!"
    mc "하아, 가끔씩 너랑 얘기하는 건 진짜 불가능하다니까."
    show monika 3b behind sayori at l31
    m "좋아, 얘들아!"
    mc "어?"
    "모니카가 갑자기 튀어나왔다."
    m "이제 서로가 쓴 시 공유해볼까?"
    show sayori 4r at h11
    s "아싸!"
    s 4x "[player], 빨리 네 시 읽어 보고 싶다!"
    mc "응, 나도…."
    "나는 열정적으로 대답하는 데 실패했지만, 사요리는 자기의 시를 찾으러 총총 뛰어갔다."
    show sayori behind monika at thide
    return

label sayori_exclusive_2:
    if not renpy.music.get_playing(channel='music') == audio.t2:
        stop music fadeout 1.0
    scene bg club_day
    with wipeleft_scene
    if not renpy.music.get_playing(channel='music') == audio.t2:
        play music t2
    s "[player], [player]!"
    "사요리는 갑작스럽게 뛰어왔다."
    show sayori 1x zorder 2 at t11
    s "다른 교실에 재료 좀 가지러 갈 건데."
    s "같이 갈래?"
    mc "재료?"
    mc "어디에 쓸 건데?"
    s 2a "축제 준비 어떻게 할 건지 알지?"
    s "나랑 모니카는 포스터를 만들 거잖아."
    s "그래서 색연필이랑 마커펜이랑…, 또 풀이랑…."
    mc "아, 오케이."
    mc "같이 가자."
    s 4q "예이~"
    s 4x "모니카, 우리 금방 다녀올게!"
    show sayori zorder 2 at t22
    show monika 1a zorder 3 at f21
    m "아, [player]랑 재료 가지러 가는 거야?"
    m "일부러 수고할 필요는 없어."
    m "내가 [player]와 갈게."
    show monika zorder 2 at t21
    show sayori 1h at s22
    s "그래도 내가 가고 싶은 걸!"
    s "빈 교실 탐험하는 게 얼마나 재밌는데!"
    show monika zorder 3 at f21
    m 2j "후후, 알았어, 알았어."
    m 2a "그냥 물어본 거였어."
    m "포스터 종이도 있으면 가져와, 알겠지?"
    show monika zorder 2 at t21
    show sayori zorder 3 at f22
    s 1r "알겠어어~!"
    s 1a "준비됐지, [player]?"
    mc "응, 가자."
    scene bg corridor
    show sayori 4a zorder 2 at t11
    with wipeleft_scene
    "사요리와 나는 부실에서 나왔다."
    "나는 콧노래를 부르는 사요리 뒤를 따라서 복도를 쭉 걸어갔다."
    "솔직히 얘기하면…."
    "어린 아이를 백화점에 데리고 다니는 기분이다."
    "사요리는 엄청 단순한 것에도 행복을 느낀다니까."
    mc "저기, 사요리…."
    mc "우리 축제때 정확히 뭐 하는 거야?"
    mc "문학으로 행사를 진행한다니 잘 상상이 안 가서…."
    s 1q "에헤헤!"
    s 1x "나랑 모니카랑 계획해놓은 게 다 있어!"
    s "걱정 안 해도 돼~"
    mc "그래…?"
    s "응!"
    s "우린 시 낭송회를 할 거야!"
    mc "낭송회…?"
    mc "어떤 식으로?"
    s 1c "그게…."
    s "모두 순서에 맞게 무대에 올라가서…."
    s 1x "자기가 가장 좋아하는 시를 낭송하는 거야!"
    mc "아…."
    mc "그거 되게…."
    "…지루할 거 같은데?"
    s 1h "[player]!"
    s "네가 생각하는 그런 게 아냐!"
    s "시를 읽는다는 게 중요한 게 아니라…."
    s 1x "무대에서 선보인다는 게 중요한 거야!"
    s "예를 들어서, 시를 이런 식으로…."
    s 2j "{i}내 발 사이에…{/i}"
    s "{i}마지막 남은 꽃이 나에게 손짓한다.{/i}"
    s 1c "{i}난 줄기를 꺾어, 땅에 박힌 뿌리로부터 자유롭게 해준다…{/i}"
    s "{i}내 손가락 사이에 마지막 기쁨의 순간을 달래준다…{/i}"
    s 3g "{i}이 기쁨의 끝에는 뭐가 있을까?{/i}"
    s "{i}위를 둘러보자…{/i}"
    s 1j "{i}한 때는 아름답던 들판이…{/i}"
    show sayori at h11
    s 4m "{i}불모의 황무지가 되어버렸네!{/i}"
    s "…."
    s 1r "이런 식으로!!"
    mc "사요리…."
    "뭐라고 말을 꺼내지…."
    mc "나만 그런 건지는 모르겠지만, 네가 그렇게 얘기할 때는 진지하게 받아들이기 좀 그래…."
    show sayori 5c at s11
    s "에에에?"
    s "너무 해!"
    s "내가 엄청 열심히 하는 거 알잖아!"
    mc "아, 알지!"
    mc "그냥… 네 귀여운 모습이랑 좀 안 맞는다고 해야되나…."
    show sayori 4s zorder 2 at t11
    s "아하하! 그런 말 하지 마, 부끄럽잖아!"
    s 4y "그래도 내가 잘하고 있다는 뜻이겠지~"
    mc "응, 맞아…."
    show sayori at h11
    s 4r "아아, 너무 기대된다!"
    s "축제 진짜 재밌을 거야~"
    "사요리는 또다시 복도에서 돌고 있다."
    s 1x "[player], 여기 교실 비어있어!"
    s "임무를 시작하자!"
    show sayori zorder 1 at thide
    hide sayori
    mc "임무… 라고…?"
    "이런 식으로 사요리와 시간을 보내는 건 오랜만이다."
    "그래도 사요리는 하나도 변하지 않았다."
    "사요리는 행복한 분위기를 뿜어내는 한 줄기의 빛 같다."
    "이건 나에게 있어 꽤 그리운 감정이다."
    "시간이 지나면서, 나는 점점 더 내 방에 자신을 가두었으니까."
    "그래서 그런지 이런 식으로 사요리와 같이 있는 것은 내가 잊고 있었던 특별한 감정을 느끼게 해주는 것 같다."
    scene bg class_day
    with wipeleft_scene
    "우리 둘은 교실로 들어왔다."
    "사요리가 벽장 앞으로 가자, 나도 뒤따랐다."
    show sayori 1b zorder 2 at t11
    s "뭐가 있나 볼까…."
    s 4x "…색연필이다!!"
    "사요리는 색연필로 가득한 상자를 선반에서 꺼냈다."
    s "엄청 좋은 브랜드 꺼야!"
    s 1b "조금 더럽긴 하지만…."
    "사요리는 색깔 이름을 말하면서, 상자에서 색연필들을 마구 꺼내고 있었다"
    mc "좋아, 색연필은 됐네."
    mc "정신 팔리면 안 돼, 아직…."
    s 1a "잠깐만, 지금 가장 좋아하는 색을 찾고 있었단 말이야…."
    mc "알았어, 알았어…."
    mc "포스터 종이 찾아보게 잠시만 옆으로 비켜 봐."
    s 1b "아, 실수로 하나 떨어…."
    play sound "sfx/smack.ogg"
    show white zorder 4:
        alpha 0.6
        linear 0.25 alpha 0.0
    show sayori 2p at h11
    "{i}타악!{/i}"
    hide white
    s "꺄아…!"
    "사요리는 선반에 이마를 박았다."
    "사요리가 바닥에 쓰러지자 색연필들이 사요리의 무릎에 쏟아졌다."
    show sayori 4p at s11
    s "아야야야…."
    mc "괜찮아?"
    s "이마가…."
    "사요리는 이마를 감쌌다."
    mc "하아, 사요리…."
    mc "너 같은 짓 한다…."
    mc "잠깐 보자."
    "사요리가 바닥에 앉아 있어서, 나는 사요리의 허리를 잡고 벽장에서 꺼냈다"
    mc "사요리, 손을 떼야지…."
    s 4g "그래도 아픈 걸 어떡해…."
    mc "잠깐이면 돼."
    $ persistent.clear[7] = True
    scene s_cg2_base1
    show s_cg2_exp2
    with dissolve_cg
    "사요리는 천천히 이마에서 손을 뗐다."
    "난 부드럽게 사요리의 앞머리를 옆으로 넘겼다."
    show s_cg2_exp1 at cgfade
    show s_cg2_exp3 at cgfade
    s "아야…!"
    mc "ㅁ, 미안…."
    "이마 중앙에 커다랗게 빨간 표시가 났다."
    "혹도 생긴 것 같은데…."
    mc "으, 커지겠는데."
    mc "얼음을 좀 구해와야 할 거 같아…."
    hide s_cg2_exp3
    hide s_cg2_exp1
    s "[player]…."
    mc "이 근처에서 얼음을 구할 데가 있나…?"
    mc "아, 찬물도 괜찮을 거 같네…."
    s "안 그래도 돼…!"
    show s_cg2_exp2 at cgfade
    hide s_cg2_exp2
    s "이러니까 유니콘 같지?"
    "아파서 움찔거리면서도, 사요리는 바보 같은 장난을 친다."
    mc "아하하, 무슨 말 하는 거야."
    mc "금방 돌아올게, 알았지?"
    s "알겠어…."
    stop music fadeout 1.0
    scene bg corridor with wipeleft_scene
    "난 사요리의 어깨를 살짝 툭 치고 복도로 뛰어나갔다."
    "난 가까운 자판기를 찾았다."
    mc "뭘 사야 되지…?"
    "마시는 게 아니라 얼음팩 대용으로 쓸 거니까 상관없나."
    "그래도 사요리가 사과 주스를 좋아하니까, 그걸로 해야겠다."
    "잠시 후, 난 사요리가 있는 교실로 돌아갔다."
    scene s_cg2_base1
    show s_cg2_exp2
    with wipeleft_scene
    play music t9
    "한 손은 이마에 대고, 다른 한 손으로 서투르게 색연필들을 상자에 담고 있었다."
    s "내가 쏟기 전에도 이미 어질러져 있었네…."
    mc "사요리, 여기."
    show s_cg2_base2 behind s_cg2_exp2 at cgfade
    "난 사요리에게 사과주스를 건네주었다."
    show s_cg2_exp2 at cgfade
    hide s_cg2_exp2
    s "차갑고 좋다…."
    "사요리는 뚜껑을 따 마시기 시작했다."
    mc "사요리, 뭐하는 거야?!"
    mc "마시지 말고 이마에 대라고, 바보야!"
    show s_cg2_exp3 at cgfade
    s "아…."
    s "미안, 잊어버렸네~"
    s "아하하하!"
    mc "머리에 얼마나 세게 맞은 거야…?"
    "사요리는 사과 주스를 이마에 가져다 댔다."
    show s_cg2_exp1 at cgfade
    s "따끔거려…."
    mc "조금 참아, 금방 괜찮아질 거야."
    mc "거의 다 정리한 거 같네, 잘했어."
    hide s_cg2_exp1
    hide s_cg2_exp3
    s "저기, [player]…."
    s "이러니까 우리 어렸을 때 생각나지 않아…?"
    mc "응? 무슨 말이야?"
    s "우리가 늘 밖에서 놀았던 거 알잖아…."
    s "난 항상 널 따라다녔고."
    s "기억 잘 안 나나 보네…."
    s "난 보통 네가 하던 것들에 뒤쳐졌잖아, 나무를 오르는 거나…."
    s "그런데 가끔 따라하려고 하면, 나는 다치곤 했지."
    s "넘어져서 상처도 나고, 멍도 들고…."
    s "그러면 내가 엄청 크게 울기 시작하고…."
    show s_cg2_exp3 at cgfade
    s "아하하!"
    s "그러면 넌 엄청 빠르게 달려와줬어."
    hide s_cg2_exp3
    s "내가 울음을 그치도록 엄청 노력하면서 말이야."
    s "마치 네 자신을 탓하거나 누군가 이걸 보면 문제에 휘말릴 거 같아 두려워하는 거 같았어…."
    s "네 잘못은 아니지만 말이야."
    mc "내가 그랬나…?"
    s "응…기억 안 나?"
    mc "지금 생각해보니까, 조금 기억나는 거 같기도 해…."
    mc "내가 맨날 노는 데만 집중해서, 너를 잘 신경 써주지 못했던 것 같다."
    mc "어떤 면에서는 내 잘못이기도 해."
    mc "이번에도 비슷하고…."
    mc "내가 널 서둘러서 벽장에서 꺼냈다면 다치지 않았을텐데."
    s "[player]…."
    s "너는 모르겠지만, 넌 항상 다른 사람을 생각해줬어."
    s "최근 몇 년간에도…."
    s "내가 어설프더라도, 넌 항상 나를 도와줬지."
    show s_cg2_exp3 at cgfade
    s "넌 진짜 다정다감한 사람이야…."
    mc "벼, 별로 그렇지 않아!"
    mc "그리고 내가 항상 이런 일을 하는 건아냐…."
    mc "네가 관련된 일이라면, 그냥 자연스럽게 도와주는 거 같아."
    mc "내가 눈치채기 전에, ."
    mc "너랑 오랫동안 친구로 지내다 보니 그런 거 같아."
    hide s_cg2_exp3
    s "정말…?"
    s "네 말이 맞을 수도 있겠다…."
    s "[player]…."
    s "우리 사이에 변한 게 없어서 다행인 거 같아."
    s "너는 이게 평생 갈 거라고 생각해?"
    mc "평생…?"
    "솔직히 얘기하면…."
    "우리가 어디로 대학을 가게 될지, 그리고 그 뒤 미래도 어떻게 될지는 아무도 모른다."
    "그러니 어떠한 약속을 만드는 건 굉장히 불합리할지도 모른다…."
    "하지만…."
    mc "그랬으면 좋겠네."
    mc "벌써 이만큼 오래됐으니까, 그렇지?"
    mc "네가 변하는 건 상상이 안 되니까, 계속 보고싶네."
    s "너무 기쁘다…."
    "사요리는 엉뚱한 표정을 지었다."
    "우린 잠시동안 조용히 있었다."
    "사요리는 겉으로 보기에는 바보 같고 서투르지만, 가끔 이렇게 깊은 생각을 하는 걸 보면…."
    "믿을만한 사람인 것 같다."
    s "돌아가야 할 거 같네…."
    s "모니카가 걱정하는 건 싫으니까…."
    mc "잘 해봐."
    mc "어떻게든 네 이마를 보게 될 거니까."
    s "앞머리로 가리면 상관 없지롱~"
    play music t8 fadeout 1.0
    scene bg class_day
    show sayori 1a zorder 2 at i11
    with dissolve_cg
    "사요리는 가볍게 일어났다."
    show sayori 4p at s11
    s "아아아…!"
    "사요리는 다시 이마를 감쌌다."
    mc "다치고 나서 너무 빨리 일어나지 마!"
    s "우으…."
    mc "너무 늦은 거 같네…."
    mc "어쨌든, 가자."
    scene bg corridor
    with wipeleft_scene
    "나는 교실 밖으로 사요리를 따라나섰다."
    "사요리는 혹을 숨기려고 앞머리를 이리저리 만져보지만, 별로 소용 없는 것 같다."
    "잠시 후, 우리는 동아리실로 돌아왔다."
    scene bg club_day
    show sayori 1a zorder 2 at t21
    show monika 1b zorder 2 at t22
    with wipeleft_scene
    show monika zorder 3 at f22
    m "아, 왔구나!"
    m "좋은 타이밍이네, 막 시 나눠볼까 하던 참이었거든."
    m 1d "응? 사요리, 네 이마가…."
    show monika zorder 2 at t22
    mc "괜찮아, 너무 걱정…."
    show sayori 4r zorder 3 at f21
    s "색연필 가지고 놀다가 선반에 이마를 박아버렸어!"
    show sayori zorder 2 at t21
    mc "…."
    show monika 3m zorder 3 at f22
    m "…."
    m 3l "…뭐, 어쨌든!"
    m 1a "필요한 건 다 가져왔어?"
    show monika zorder 2 at t22
    show sayori 1x zorder 3 at f21
    s "당연하지! 여기…."
    s 1n "…에?"
    "사요리는 자기 주위를 둘러보았다."
    show sayori 4m zorder 3 at hf21
    s "다… 잃어버렸어!!"
    show sayori zorder 2 at t21
    mc "진정해, 사요리."
    mc "내가 다 가져왔으니까."
    mc "포스터 종이도 찾아왔어."
    show sayori 4b
    show monika 5a zorder 3 at f22
    m "아하하!"
    m "네가 다 가져온 것 같네, [player]."
    show monika zorder 2 at t22
    mc "아, 사요리는…."
    "난 사요리를 위한 변명거리를 찾지 못했다."
    show sayori 1q zorder 3 at f21
    s "난 모험을 하고 왔어!"
    show sayori 1a zorder 2 at t21
    mc "…그래, 뭐."
    show monika 1j zorder 3 at f22
    m "아하하, 알겠어."
    m 1a "어쨌든, 잘하고 왔어!"
    m "난 오늘 밤부터 작업 할게."
    show monika zorder 2 at t22
    show sayori 4x zorder 3 at f21
    s "나도!"
    show monika zorder 2 at t11
    show sayori behind monika at thide
    hide sayori
    m 4b "…좋아, 얘들아."
    m "시 나눠볼 준비는 됐지?"
    mc "내 시가 어딨지…."
    "색연필 상자가 잘 닫혀있는지 확인하고, 난 자리로 돌아왔다."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
