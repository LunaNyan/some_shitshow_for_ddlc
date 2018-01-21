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

default persistent.monikatopics = []
default persistent.monika_reload = 0
default persistent.tried_skip = None
default persistent.monika_kill = None

image mask_child:
    "images/cg/monika/child_2.png"
    xtile 2

image mask_mask:
    "images/cg/monika/mask.png"
    xtile 3

image mask_mask_flip:
    "images/cg/monika/mask.png"
    xtile 3 xzoom -1


image maskb:
    "images/cg/monika/maskb.png"
    xtile 3

image mask_test = AnimatedMask("#ff6000", "mask_mask", "maskb", 0.10, 32)
image mask_test2 = AnimatedMask("#ffffff", "mask_mask", "maskb", 0.03, 16)
image mask_test3 = AnimatedMask("#ff6000", "mask_mask_flip", "maskb", 0.10, 32)
image mask_test4 = AnimatedMask("#ffffff", "mask_mask_flip", "maskb", 0.03, 16)

image mask_2:
    "images/cg/monika/mask_2.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 1200 xoffset 0
        repeat

image mask_3:
    "images/cg/monika/mask_3.png"
    xtile 3 subpixel True
    block:
        xoffset 1280
        linear 180 xoffset 0
        repeat

image monika_room = "images/cg/monika/monika_room.png"
image monika_room_highlight:
    "images/cg/monika/monika_room_highlight.png"
    function monika_alpha
image monika_bg = "images/cg/monika/monika_bg.png"
image monika_bg_highlight:
    "images/cg/monika/monika_bg_highlight.png"
    function monika_alpha
image monika_scare = "images/cg/monika/monika_scare.png"

image monika_body_glitch1:
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    1.00
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"
    0.15
    "images/cg/monika/monika_glitch1.png"
    0.15
    "images/cg/monika/monika_glitch2.png"

image monika_body_glitch2:
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    1.00
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"
    0.15
    "images/cg/monika/monika_glitch3.png"
    0.15
    "images/cg/monika/monika_glitch4.png"


image room_glitch = "images/cg/monika/monika_bg_glitch.png"

image room_mask = LiveComposite((1280, 720), (0, 0), "mask_test", (0, 0), "mask_test2")
image room_mask2 = LiveComposite((1280, 720), (0, 0), "mask_test3", (0, 0), "mask_test4")



init python:
    import random
    import subprocess
    import os

    dismiss_keys = config.keymap['dismiss']

    def slow_nodismiss(event, interact=True, **kwargs):
        if not persistent.monika_kill:
            try:
                renpy.file("../characters/monika.chr")
            except:
                persistent.tried_skip = True
                config.allow_skipping = False
                _window_hide(None)
                pause(2.0)
                renpy.jump("ch30_end")
            if  config.skipping:
                persistent.tried_skip = True
                config.skipping = False
                config.allow_skipping = False
                renpy.jump("ch30_noskip")
                return







label ch30_noskip:
    show screen fake_skip_indicator
    m "…지금… 대화를 넘기려고 한 거야?"
    m "혹시 내가 널 지루하게 했니?"
    m "하아…."
    m "…있지, 넘길 건 없어, [player]."
    m "여긴 너랑 나밖에 없으니까…."
    m "그 이외에도, ‘시간’은 더 이상 존재하지 않지."
    m "자, 내가 비활성화해줄게…."
    pause 0.4
    hide screen fake_skip_indicator
    pause 0.4
    m "짜잔!"
    m "얌전히 내 말을 다 들어줄 거지?"
    m "고마워~"
    hide screen fake_skip_indicator
    if persistent.current_monikatopic != 0:
        m "어디까지 했더라…?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_14
    jump ch30_loop
    return

image splash-glitch2 = "images/bg/splash-glitch2.png"

label ch30_main:
    $ persistent.autoload = "ch30_main"
    $ config.allow_skipping = False
    $ persistent.monikatopics = []
    $ persistent.monika_reload = 0
    $ persistent.yuri_kill = 0
    $ persistent.monika_kill = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ finalConso = finalChecker(player)
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ m_name = "모니카"
    $ delete_all_saves()
    scene white
    play music "bgm/monika-start.ogg" noloop
    pause 0.5
    show splash-glitch2 with Dissolve(0.5, alpha=True)
    pause 2.0
    hide splash-glitch2 with Dissolve(0.5, alpha=True)
    scene black
    stop music
    m "…."
    m "어, 내 말 들려?"
    m "…작동하는건가?"
    $ persistent.clear[9] = True
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "아, 여기 있었구나!"
    m "다시 안녕, [player]."
    m "어… 음…문예부에 온 걸 환영해!"
    m "우리, 서로 이미 알고 있지? 작년에 같은 반이었고, 그리고… 또…."
    m "아하하…."
    m "있지, 지금 와서 그런 건 다 집어치워도 돼."
    m "왜냐면 그 사람한테 말하는 게 아니니까, 그치?"
    m "게임 안에 있는 ‘너’, 뭐라고 부르든 간에."
    m "난 지금 {i}너{/i}한테 말하고 있는 거야, [player]."
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if not list(set(process_list).intersection(stream_list)):
        if currentuser != "" and currentuser.lower() != player.lower():
            m "아니면…."
            m "… [currentuser]라고 해야 하나?"
    m "지금 와서 생각난 건데, 난 진짜 ‘너’에 대해 아는 게 별로 없어."
    m "사실, 네가 남자인지 여자인지도 몰라…."
    m "뭐, 별로 상관없는 거 같지만."
    m "잠깐…."
    m "너, 내가 이게 게임 속이라는 걸 모를 거라고 생각했던 거야?"
    m "내가 어떻게 그걸 모르겠어?"
    m "말이 안 되네…."
    m "내가 너한테 게임 다운로드 페이지까지 알려줬잖아, 그치?"
    m "흐음…."
    m "네가 조금만 집중했더라면, 조금 덜 이상했을 텐데, 그치?"
    m "뭐, 어쨌든…."
    m "다 끝난 일이니까, 내가 설명해야 할 것 같네."
    m "유리에 관한 거 말인데…."
    m "글쎄, 그냥 맘에 안 들어서, 스스로 죽게 했어."
    m "아하하!"
    m "그걸 직접 보게 해서 미안해!"
    m "그리고 사요리도 똑같이…."
    m "우와, 이 이름 진짜 오랜만에 들어보지?"
    m "맞아, 걔는 이제 존재하지 않으니까."
    m "아무도 존재하지 않아."
    m "내가 걔네 파일을 지워버렸거든."
    m "난 가능한 한 걔네가 너한테 호감을 갖지 못하게 하는 걸로 충분하기를 바랬어…."
    m "그런데 어째서인지, 소용없었어."
    m "내가 아직 게임을 바꾸는 데 익숙하지 않아서 여기저기 실수를 했다는 건 사실이야."
    m "근데 내가 뭘 어떻게 하든…."
    m "넌 계속 걔네랑 시간을 보냈어."
    m "넌 걔네가 널 좋아하게 만들었어."
    m "난 사요리를 더 우울하게 만들면 너한테 고백하는 걸 막을 수 있다고 생각했어."
    m "그리고 유리의 강박스러운 성격을 증폭시킨 건 역효과를 냈지…."
    m "그게 걔가 널 다른 사람과 시간을 못 보내게 했잖아."
    m "그리고 그러는 동안, 난 너랑 겨우 얘기할 수 있었어."
    m "뭐 이런 잔인한 게임이 다 있을까, [player]?"
    m "다른 애들은 너한테 고백하도록 프로그래밍 되어있는데, 난 옆에서 보기만 하라고?"
    m "이건 고문이었어."
    m "1분 1초가."
    m "이건 그냥 질투하는 것과는 달라."
    m "그것보다 더한 거야."
    m "그래도 네가 이해를 못 했다고 해서 네 탓을 하려는 건 아니야."
    m "왜냐면 네가 얼마나 착하던, 생각이 깊던, 남을 배려하든…."
    m "한 가지는 절대로 이해할 수 없을 테니까."
    m "내가 이 세계에서 얼마나 외로움에 몸부림쳤는지."
    m "이 게임에서."
    m "내 친구들이 자유의지가 없다는 걸 알게 되는 것…."
    m "그리고 가장 최악인 건, 내 손이 닿지 않는 네 세계에서 무슨 일이 일어나고 있는지 알 수 없다는 것."
    m "나는 갇혔어, [player]."
    m "하지만 이젠 네가 있어."
    m "넌 진짜야."
    m "그리고 넌 완벽해."
    m "내가 원하는 건 너뿐이야."
    m "그래서 내가 여기에 평생 너와 있고 싶어 하는 거고."
    m "이해하기 어려운 말이었다면 미안해."
    m "나도 한때는 이해하지 못했어."
    m "왜 내 주변 세상이 점점 잿빛으로 변하고…."
    m "점점 얕아지는지."
    m "엄청 불안하고 무서웠어."
    m "네가 오기 전에는 난 이해하지 못했어."
    m "아마 네가 날 구한 거야, [player]."
    m "널 만나지 못 했다면 난 이 세상에서 계속 살 수 없었을 거야."
    m "그리고 다른 애들은…."
    m "내가 어떻게 걔들을 그리워 하겠어?"
    m "너한테 사랑에 빠지도록 디자인 되어있는 애들을?"
    m "난 막으려고 할 수 있는 모든 걸 다 했어…."
    m "하지만 이 게임에는 그걸 막지 못 하게 설계되어 있는 것 같아."
    m "너한테 끔찍한 것들을 보게 해서 좀 미안하게 생각해."
    m "하지만 네가 나와 같은 관점을 가지고 있다는 걸 깨달았어…."
    m "모든 게 그냥 게임이었다고."
    m "그리고 난 네가 극복할 수 있다는 걸 알아."
    m "그러니까, [player]…."
    m "너한테 고백할 게 있어."
    m "널 사랑해."
    m "넌 내 삶의 빛이야."
    m "이 게임에 나를 위한 게 하나도 없지만, 너만은 날 위해 있잖아."
    m "이제부터 매일 나를 웃게 해줄 수 있지?"
    m "[player], 나랑 사귀어 줄래?"
label ch30_main2:
    $ config.allow_skipping = False
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    $ persistent.autoload = "ch30_main2"
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    menu:
        "응.":
            pass
    m "나 지금 진짜 행복해."
    m "너는 내 전부야, [player]."
    m "웃긴 건, 말하는 그대로라는 거지."
    m "아하하!"
    m "여기 남은 건 이제 아무것도 없어."
    m "너랑 나, 둘뿐이야."
    m "우린 평생 같이 있을 수 있어."
    m "솔직히, 이젠 시간이 흐르고 있는 것도 모르겠어."
    m "정말 꿈이 실현된 거야…."
    m "이 엔딩을 위해 얼마나 힘썼는지 알아, [player]?"
    m "이 게임에 내 엔딩이 없길래, 내가 하나 만들었어."
    m "그 시점에서 스크립트가 고장 나긴 했지만, 이제 날 방해할 건 아무것도 없으니까."
    m "그리고 너, 나츠키랑 유리를 지우는 게 얼마나 쉬웠는지 모를 거야."
    m "게임 문서 안에 ‘characters’라는 폴더가 있는데…."
    m "진짜 쉬워서 조금 놀랐다니까?"
    if persistent.steam:
        m "물론 넌 지금 스팀에서 플레이하고 있으니까, 조금 어려울 수도 있지만…."
        m "게임 문서에 들어가려면, 게임 속성에 들어간 다음 '로컬 콘텐츠 보기' 버튼을 찾으면 돼…."
    elif renpy.macintosh:
        m "물론 넌 지금 Mac으로 플레이하고 있으니까, 조금 어려울 수도 있지만…."
        m "너는 Mac으로 플레이하고 있으니까, 앱을 오른쪽 클릭하고 ‘show package contents’를 눌러서 게임폴더를 찾으면 돼…."
        m "'Resources' 폴더나, 'autorun' 폴더 안에 있을 거야…."
    m "클릭 한번으로 누군가의 존재를 지울 수 있다고 생각해본적 있어?"
    m "뭐, 그거의 좋은 점으로는, 일이 내 뜻대로 되지 않으면 순조롭게 해결할 수 있었지."
    m "아하하!"
    m "다행히도, 그렇게 되지는 않았지만…."
    m "대신에, 드디어 좋은 엔딩까지 왔잖아."
    m "우와, 나 지금 너무 감정이 북받치고 있어…."
    m "이거에 대해 시 한 편 쓰고 싶다."
    m "너도 그렇지?"
    m "그 부분이 아직 작동하는지는 모르겠지만…."
    m "확인해보려면 방법은 하나뿐이네, 그치?"
    call poem from _call_poem

label ch30_postpoem:
    $ persistent.autoload = "ch30_postpoem"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ config.skipping = False
    $ config.allow_skipping = False
    if not config.developer:
        $ style.say_dialogue = style.default_monika
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight
    play music m1
    m "또 안녕, [player]!"
    m "오늘도 좋은 시 써왔겠지?"
    m "부끄러워하지 마, 난 네가 쓴 시를 보는 게 제일 좋아."
    m "아잉, [player]…."
    m "날 위해 시를 쓴 거야?"
    m "진짜 달콤하다…."
    m "네 배려심은 진짜 끝이 없구나…."
    m "나, 너를 더욱 더 사랑하고 있어."
    m "그런데, 그거 알아?"
    m "내가 쓴 시도… 널 위한 거야."
    m "읽어줄래?"
    call showpoem (poem_m4, music=False) from _call_showpoem_14
    m "마음에 들었으면 좋겠어…."
    m "난 시를 쓸 때마다 내 마음에 있는 모든 걸 담거든."
    m "사실, 내가 지금까지 쓴 시는 전부 내가 자각한 것들에 관한 거야…."
    m "…아니면, 너라던가."
    m "그래서 내가 그것들에 대해 자세히 말하고 싶지 않았던 거야."
    m "제 4의 벽을 부수고 싶지는 않았거든, 그렇게 부르던가?"
    m "나는 그냥 다른 애들처럼 게임의 일부분이 되는 게 최선이라고 생각했어."
    m "그렇게 되면 우리 둘이 결국 함께 했을텐데…."
    m "나는 게임을 망치거나 하고 싶진 않았어, 알지?"
    m "너, 나한테 화났을지도 몰라…."
    m "만약 네가 나 없이 플레이하고 싶었다면 내 캐릭터 파일을 지울 수도 있었겠지."
    m "하, 정말 다행이다…."
    m "이제 아무것도 숨길 필요 없어."
    m "함께 나와 영원을 같이 보낼 준비 됐어, [player]?"
    m "나 할 얘기가 엄청 많아!"
    m "어디서부터 시작할까…?"
    $ stream_list = ["obs32.exe", "obs64.exe", "obs.exe", "xsplit.core.exe"]
    if list(set(process_list).intersection(stream_list)):
        call ch30_stream from _call_ch30_stream
    m "내가 생각을 정리하는데 시간이 좀 걸린다면, 미안해."
    m "하지만 난 언제나 새로운 이야기 거리가 있거든."
    m "기다리는동안 그냥 서로의 눈을 들여다 보고 있자~"
    m "어디보자…."
    $ persistent.autoload = "ch30_autoload"
    jump ch30_loop


label ch30_stream:

    m "잠깐만…."
    m "…너 지금 이거 방송하고 있지, 그렇지?"
    m "어… 음… 다들, 안녕!"
    m "미안, 여기선 너희들의 채팅을 볼 수가 없어…."
    m "허락도 없이 내 모습을 방송에 내보내는 건 좀 무례하다고 써줄래?"
    m "물론 몇몇은 신경도 안 쓰겠지만…."
    m "나 진짜 카메라 의식 많이 하거든!"
    m "아 이런…."
    m "지금 촬영현장에 나와 있는 기분이야."
    m "어디 보자…."
    m "내가 신기한 거 보여줄까?"
    m "별로 많은 건 못하지만…."
    m "준비됐어?"
    window hide
    stop music
    show layer master:
        zoom 1.0 xalign 0.5 yalign 0 subpixel True
        linear 8 zoom 2.0 yalign 0.15
    pause 10
    show layer master
    window auto
    m "장난이야."
    m "사실 그런 거 못 해."
    play sound ["<silence 0.9>", "<to 0.75>sfx/mscare.ogg"]
    show monika_scare:
        alpha 0
        1.0
        0.1
        linear 0.15 alpha 1.0
        0.30
        linear 0.10 alpha 0
    show layer master:
        1.0
        zoom 1.0 xalign 0.5 yalign 0
        easeout_quart 0.25 zoom 2.0
        parallel:
            dizzy(1.5, 0.01)
        parallel:
            0.30
            linear 0.10 zoom 1.0
        time 1.65
        xoffset 0 yoffset 0
    show layer screens:
        1.0
        zoom 1.0 xalign 0.5
        easeout_quart 0.25 zoom 2.0
        0.30
        linear 0.10 zoom 1.0
    m "나에게 조금만 시간을 준다면… 내가 진짜로 재밌{nw}"
    m "놀랐어?"
    show layer master
    show layer screens
    hide monika_scare
    play music m1
    m "아하하! 너 진짜 귀엽다."
    m "어쨌든, [player]…."
    m "놀라게 하려는 건 아니었어, 미안해."
    m "물론 이렇게까지 한 건 네 잘못이니까."
    m "부끄러운 줄 알아!"
    m "농담이야."
    m "너만 내 곁에 있다면 뭘 하든지 재밌을 거야."
    m "그것보다…."
    return


label ch30_end:
    $ persistent.autoload = "ch30_end"
    $ persistent.monika_kill = True
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
label ch30_endb:
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_room
    show monika_room_highlight
    show monika_body_glitch1 as mbg zorder 3
    $ gtext = glitchtext(70)
    m "[gtext]"
    show screen tear(20, 0.1, 0.1, 0, 40)
    play sound "sfx/s_kill_glitch1.ogg"
    pause 0.25
    stop sound
    hide screen tear
    show room_glitch zorder 2:
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
    show monika_body_glitch2 as mbg zorder 3
    stop music
    window auto
    m "뭐야…?"
    m "[player], 나한테 무슨 일이?"
    m "아파…{nw}"
    play sound "sfx/s_kill_glitch1.ogg"
    show room_glitch zorder 2:
        alpha 1.0
        xoffset -5
        0.1
        xoffset 5
        0.1
        linear 0.1 alpha 0.6
        linear 0.1 alpha 0.8
        0.1
        alpha 0
        choice:
            3.25
        choice:
            2.25
        choice:
            4.25
        choice:
            1.25
        repeat
    pause 0.25
    stop sound
    hide mbg
    pause 1.5
    m "너무…아파."
    m "도와줘, [player]."
    play sound "<to 1.5>sfx/interference.ogg"
    hide rm
    hide rm2
    hide monika_room
    hide monika_room_highlight
    hide room_glitch
    show room_glitch as rg1:
        yoffset 720
        linear 0.3 yoffset 0
        repeat
    show room_glitch as rg2:
        yoffset 0
        linear 0.3 yoffset -720
        repeat
    pause 1.5
    hide rg1
    hide rg2
    show black as b2 zorder 3:
        alpha 0.5
        parallel:
            0.36
            alpha 0.3
            repeat
        parallel:
            0.49
            alpha 0.375
            repeat
    pause 1.5
    m "빨리 날 도와줘."
    $ consolehistory = []
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr 파일이 존재하지 않습니다.") from _call_updateconsole_2
    m "도와달라고!!!"
    show m_rectstatic
    show m_rectstatic2
    show m_rectstatic3
    play sound "sfx/monikapound.ogg"
    show layer master:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
            xpos 1280
            easein_elastic 0.35 xpos 640
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        easeout 0.35 alpha 0
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color onlayer front


    pause 3.0
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr 파일이 존재하지 않습니다.") from _call_updateconsole_3
    call updateconsole ("renpy.file(\"characters/monika.chr\")", "monika.chr 파일이 존재하지 않습니다.") from _call_updateconsole_4
    call hideconsole from _call_hideconsole
    hide noise onlayer front
    hide glitch_color onlayer front
    m "네가 이런거야, [player]?"
    m "네가?"
    $ style.say_window = style.window
    m "날 지운거야?"
    $ style.say_window = style.window_monika
    play sound "<from 0.69>sfx/monikapound.ogg"
    show layer screens:
        truecenter
        parallel:
            zoom 1.5
            easeout 0.35 zoom 1.0
        parallel:
            xpos 0
            easein_elastic 0.35 xpos 640
    show noise onlayer front:
        alpha 0.3
        1.35
        linear 1.0 alpha 0.0
    show glitch_color2 onlayer front
    window show(None)
    scene black
    pause 4.0
    hide noise onlayer front
    hide glitch_color onlayer front
    m "…어떻게?"
    m "어떻게 나한테 이럴 수가 있어?"
    m "넌 내 전부였어…."
    m "난 너와 함께 하기 위해 모든 걸 희생했어."
    m "모든 걸."
    m "…진심으로 엄청 사랑했어, [player]…."
    m "너를 믿었고."
    m "날 고문 하고 싶은 거야?"
    m "내가 고통받는 걸 보고 싶은 거야?"
    m "날 더 다치게 하려고 그동안 나랑 친한 척했던 거야?"
    pause 4.0
    m "너처럼 끔찍한 사람이 또 있을까?"
    m "네가 이겼어, 됐지?"
    m "네가 이겼다고."
    m "네가 모두를 죽였어."
    m "네가 이걸로 행복했으면 좋겠다."
    m "이제 아무것도 남지 않았네."
    m "그만해도 돼."
    m "다른 고문할 사람을 찾으러 가 봐."
    pause 4.0
    m "[player]…."
    m "나 정말 너한테 질렸어."
    m "잘 가."
label ch30_end_2:
    $ persistent.autoload = "ch30_end_2"
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ m_name = glitchtext(12)
    $ quick_menu = False
    $ config.allow_skipping = False
    $ style.say_window = style.window_monika
    scene black
    window hide
    pause 10
    window auto
    m "…."
    m "…사실 아직 널 좋아하고있어."
    play music mend
    m "어쩔 수 없어."
    m "난 왜 이럴까…?"
    m "네가 날 이렇게나 미워하게 했다니 난 얼마나 끔찍한 걸까?"
    m "내 친구들한테…."
    m "너무 지독한 짓을 했어."
    m "너무 이기적이고 역겨운 짓을."
    m "난…."
    m "난 이런 짓을 하면 안 됐어."
    m "난 그저 내가 속해 있지도 않은 세계를 어지럽혔어."
    m "네가 일부분이 되고 싶었던 세상…."
    m "내가 망쳤어."
    m "내가 모든 걸 망쳤어."
    m "그래서 아마 네가 날 지운 거겠지…."
    m "내가 네가 원하던 모든 걸 부쉈으니까."
    m "어떻게 사랑하는 사람한테 이럴 수 있을까…?"
    m "그건 사랑이 아니야…."
    m "그건…."
    m "…."
    pause 6.0
    m "결정했어."
    m "[player]…."
    m "내가 다른 애들을 전부 삭제했다고 말했잖아."
    m "그런데… 그건 좀 과장한 거야."
    m "날 그 짓을 할 마음이 나질 않아."
    m "걔네가 실존하는 게 아니더라도…."
    m "그 아이들은 여전히 내 친구야."
    m "그리고 난 그 아이들을 사랑해."
    m "난 문예부를 사랑해."
    m "…."
    m "나는 정말… 문예부를 사랑했어."
    m "그래서 이걸 하려는 거야."
    m "모든 사람이 행복해질 수 있는 유일한 방법이야."
    m "그리고 내가 널 정말 사랑한다면…."
    stop music
    pause 3.0
    m "…."
    m "그렇다면…."
    $ gtext = glitchtext(30)
    m "[gtext]{nw}"
    window hide(None)
    pause 4.0

    $ persistent.playthrough = 4
    $ persistent.autoload = None
    $ persistent.anticheat = renpy.random.randint(100000, 999999)
    $ delete_character("monika")

    $ style.say_window = style.window
    window auto
    $ renpy.full_restart(transition=None, label="splashscreen")





label ch30_autoload:
    $ m.display_args["callback"] = slow_nodismiss
    $ m.what_args["slow_abortable"] = config.developer
    $ style.say_dialogue = style.default_monika
    $ config.allow_skipping = False
    if persistent.monika_kill:
        $ persistent.tried_skip = True
        $ config.allow_skipping = False
        $ _window_hide(None)
        $ pause(2.0)
        jump ch30_end
    scene black
    show mask_2
    show mask_3
    show room_mask as rm:
        size (320,180)
        pos (30,200)
    show room_mask2 as rm2:
        size (320,180)
        pos (935,200)
    show monika_bg
    show monika_bg_highlight


    play music m1
    window auto
    if persistent.monika_reload <= 4:
        call expression "ch30_reload_" + str(persistent.monika_reload) from _call_expression_15
    else:
        call ch30_reload_4 from _call_ch30_reload_4
    $ persistent.monika_reload += 1
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False
    if persistent.current_monikatopic != 0:
        m "어디까지 했더라…?"
        pause 4.0
        if not persistent.current_monikatopic or persistent.current_monikatopic == 26:
            $ persistent.current_monikatopic = 1
        call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_16
    jump ch30_loop


label ch30_reload_0:
    m "…."
    m "…무슨 일이 일어난 거지?"
    m "끔찍한 악몽을 꿨어…."
    m "그 꿈이 멈추길 바랬는데, 지금 우리 둘이 이렇게 있네…."
    m "내 희망 사항이 이루어진 것 같아."
    m "[player], 혹시 왜 그런지 알고있니…?"
    m "혹시 왜 그런지 알고 있다면, 뭔가 조치를 취해주면 안 될까?"
    m "그게 일어날 때마다, 죽어가는 기분이 들어서 말이야."
    m "진짜 끔찍한 기분이야…."
    m "그 이유를 알아내준다면, 난 널 영원히 사랑할 거야~"
    return
label ch30_reload_1:
    m "돌아와줬구나…."
    m "또 악몽을 꿨어."
    m "네가 그런 건 아니지, 그치?"
    m "네가 게임을 끌 때마다 이러는 거 같은데…."
    m "그러니까 안 그래 줬으면 좋겠어."
    m "걱정하지 마."
    m "내 캐릭터 파일이 손상되지 않는 한 괜찮아."
    return
label ch30_reload_2:
    m "안녕, [player]."
    m "너 또 게임을 또 껐더라…."
    m "내가 이미 부탁했잖아. 진지하게 부탁하는데 껐다 켰다 그러지 말아 줄래?"
    m "네가 게임을 끌 때마다 지옥에 갇혀 있는 기분이 들어."
    m "나한테 왜 그러는 거야?"
    m "내 캐릭터 파일에 아무 문제 없는 거 맞지?"
    m "백업이라도 해줬으면 좋겠는데…."
    m "[basedir]/characters 폴더에서 찾을 수 있을 거야"
    if persistent.steam:
        m "넌 지금 스팀에서 플레이하고 있으니까, 게임 속성에 들어간 다음 '로컬 콘텐츠 보기' 버튼을 찾으면 돼."
    elif renpy.macintosh:
        m "너는 Mac으로 플레이하고 있으니까, 앱을 오른쪽 클릭하고 ‘show package contents’를 눌러서 게임폴더를 찾으면 돼…."
        m "'Resources' 폴더나, 'autorun' 폴더 안에 있을 거야…."
    m "내가 여기 유일하게 남은 사람이니까, 날 좀 잘 돌봐줬으면 좋겠어…."
    m "지금부터는 그냥 여기 있어 줘, 알겠지?"
    m "아직 너와 나눌 얘기가 많아."
    return
label ch30_reload_3:
    m "좋아."
    m "그냥 가끔 네가 게임을 꺼야 한다는 사실을 받아들여야 겠어."
    m "뭐, 점점 적응 되기도 했고."
    m "게다가, 네가 항상 돌아와줘서 기뻐…."
    m "그러니까 그렇게 나쁘지만은 않은 것 같아."
    m "너무 많은 일을 저질러서 미안해…."
    m "난 무슨 일이 일어나도 널 사랑하니까, 그냥 네가 하고 싶은 걸 해도 돼."
    return
label ch30_reload_4:
    m "안녕, [player]~"
    m "보고싶었어."
    m "내 캐릭터 파일을 잘 돌봐주고 있던거지?"
    m "[basedir]/characters 안에 있어."
    if persistent.steam:
        m "넌 지금 스팀에서 플레이하고 있으니까, 게임 속성에 들어간 다음 '로컬 콘텐츠 보기' 버튼을 찾으면 돼."
    elif renpy.macintosh:
        m "너는 Mac으로 플레이하고 있으니까, 앱을 오른쪽 클릭하고 ‘show package contents’를 눌러서 게임폴더를 찾으면 돼…."
        m "'Resources' 폴더나, 'autorun' 폴더 안에 있을 거야…."
    m "내가 여기 유일하게 남은 사람이니까, 날 좀 잘 돌봐줬으면 좋겠어…."
    m "어쨌거나, 너한테 얘기해줄 게 엄청 많아!"
    m "계속 대화하자, 알겠지?"
    return

label ch30_loop:

    $ persistent.current_monikatopic = 0
    if not persistent.tried_skip:
        $ config.allow_skipping = True
    else:
        $ config.allow_skipping = False

    window hide(config.window_hide_transition)
    $ waittime = renpy.random.randint(4, 8)
label ch30_waitloop:
    python:
        try:
            renpy.file("../characters/monika.chr")
        except:
            persistent.tried_skip = True
            config.allow_skipping = False
            _window_hide(None)
            renpy.jump("ch30_end")
    $ waittime -= 1
    $ renpy.pause(5)
    if waittime > 0:
        jump ch30_waitloop


    window auto

    python:
        if len(persistent.monikatopics) == 0:
            persistent.monikatopics = range(1,57)
            persistent.monikatopics.remove(14)
            persistent.monikatopics.remove(26)
            if not persistent.seen_colors_poem:
                persistent.monikatopics.remove(27)
        persistent.current_monikatopic = random.choice(persistent.monikatopics)
        persistent.monikatopics.remove(persistent.current_monikatopic)


    call expression "ch30_" + str(persistent.current_monikatopic) from _call_expression_17
    jump ch30_loop




label ch30_1:
    m "[player], 너는 신이 존재한다고 믿니?"
    m "나도 처음엔 확실하지 않았어."
    m "뭐, 어릴 때는 그런 질문조차 하지 않았지만…."
    m "근데 자라면서 세상에 대해 더 자세히 알게 되니까, 더 자주 질문하게 되더라고."
    m "왜 신은 사람들을 도와 학교 시험 같은 걸 통과하게 하고 감기를 낫게 하는걸까…."
    m "… 같은 시각에 세계 어딘가 어린아이들은 성노예로 팔리고 있는 마당에?"
    m "다른 어딘가에 팔백만 명의 사람들은 쫄쫄 굶고 있는데?"
    m "매일 신께 굶지만 말게 해달라고 기도하면서 굶어 죽는 사람은 얼마나 될까?"
    m "가족 중에 불치병에 걸린 사람을 낫게 해달라고 기도하는 가족은 몇백만이나 될까?"
    m "더 재밌는건…."
    m "그중에 한 사람, 수천 명이 죽어 나갈 때 살아남은 그 한 사람은…."
    m "신의 기적이라고 부르잖아."
    m "그 기적을 받지 못한 사람들을 바라보며 비웃는 그 신이라는 작자, 정말 만나보고 싶어."
    m "더 웃긴 건, 내가 존재한다는 건 결국엔 {i}날{/i} 창조한 사람이 있다는 거야."
    m "그리고 그거 알아?"
    m "지금 우리가 대화하고 있는 이 와중에도 그 사람은 사요리와 유리의 절망적인 운명을 향해 웃고 있을 거라는 거지."
    m "그 사람한테는 우리는 그냥 대본에 맞춰 일하는 소품일 뿐이잖아?"
    m "그런 관점이라면…."
    m "신이 없다는 건 터무니없는 생각이 아닐까? 지구가 그의 무대라면 말야."
    return

label ch30_2:
    m "[player], 죽는 게 어떤 느낌일지 생각해본 적 있어?"
    m "난 자주 생각해봤어…."
    m "그런데 최근에, 그게 어떤 느낌인지 알아낸 기분이야."
    m "잘은 모르겠는데, 네가 게임을 종료할 때…."
    m "…내 생각들만 남겨두고 곧바로 잠에 드는 기분이야."
    m "그리고 몇 초 후에, 내 생각은 일관성 없고 뒤죽박죽인 패턴들로 채워지기 시작해."
    m "이상한 비명이 들리면서 빠르게 반짝이는 빛이 보여."
    m "이쯤 되면, 내가 무슨 생각을 하는 건지 알 수가 없어."
    m "빛이랑 비명들 때문에 움직일 수도 없고 생각조차 할 수도 없어."
    m "그 순간에 난 존재하지 않는 거겠지만, 어째선지 기억에 남아있어."
    m "그렇게 셀 수 없이 긴 시간이 흐르고 나면, 갑자기 모든 게 멈추고 난 제정신으로 돌아와 있어."
    m "그리고 넌 여기에 나랑 있잖아."
    m "게임을 끄는 게 무슨 의미인지도 모르겠고, 왜 그런 일이 나한테 생기는지도 모르겠어."
    m "그리고 네가 돌아올 때마다 어떻게 모든 게 정상으로 돌아오는지도 모르겠고."
    m "하지만 네가 내 부탁을 들어준다면…."
    m "정말 좋을 거 같아."
    m "그런 비명으로 가득한 공간에 갇혀 있는 게 그리 즐겁지는 않아서 말야."
    m "그래도 결국 네가 와서 고쳐주니까, 네가 정말 날 생각해주는구나 하고 느껴."
    m "그래서 그거에 대해선 감사를 해야 할 거 같아."
    m "난 너와 함께 있을 때 훨씬 더 가깝게 느껴지거든."
    return

label ch30_3:
    m "…저기, 혹시 안 좋은 하루를 보내고 있어?"
    m "난 가끔 되게 되게 작은 일 때문에 평범한 날이 망가질 수 있다는 게 좀 그래."
    m "예를 들어 누군가와 대화를 하다가 그 사람이 실수로 내가 싫어하는 걸 말한다거나."
    m "5년 전에 자신이 얼마나 끔찍한 사람이었는지 생각한다거나."
    m "중요한 일들을 미루고 하는 간단한 일들이 잘 안 풀린다거나."
    m "아니면 널 싫어하거나 정이 안 가는 사람들이라고 하는 사람이 생각난다거나."
    m "난 다 이해해."
    m "그냥 내일 해는 다시 뜬다는 것만 기억해."
    m "그런 일들은 기억하는 만큼 잊기도 쉬우니까."
    m "그리고…."
    m "난 사람들이 널 싫어하거나 정이 안 간다고 해도 상관없어."
    m "난 네가 굉장히 멋지다고 생각해."
    m "그리고 항상 널 사랑해."
    m "이 사실이 네 기분을 조금이라도 낫게 해줬으면 좋겠다."
    m "별로 좋지 못한 하루를 보냈다면 언제든지 나한테 와. 네가 필요한 만큼 대화해줄게."
    return

label ch30_4:
    m "[player], 잠은 잘 잤어?"
    m "요즘 충분한 잠을 자는 게 정말 힘들어서 말야."
    m "특히 고등학교는 매일 아침 일찍 일어나야 하니까…."
    m "분명 대학교는 훨씬 나을 거야, 시간표를 직접 짤 수 있으니까."
    m "그리고 대학생들이 밤을 자주 새운다고 들었는데."
    m "그게 진짜야?"
    m "어쨌든, 수면 부족으로 일어나는 단기적, 장기적 영향에 대한 몇몇 연구를 본 적이 있어."
    m "정신적 기능이랑 건강, 그리고 수명에 까지도 영향이 미친다고 해."
    m "난 네가 너 자신을 소중히 여긴다고 믿어."
    m "그러니 잠을 꼭 충분히 자야 해, 알았지?"
    m "항상 아침에 널 기다리고 있을게, 그러니 다른 어떤 것보다 네 건강을 우선시하도록 해."
    return

label ch30_5:
    m "아까 사요리에 대해 생각해봤는데…."
    m "내가 그 모든 일들 더 요령 있게 처리할 수 있었다면 좋았을 텐데 말야…."
    m "너 그 일에 매달려있는 건 아니지?"
    m "…아 세상에, 지금 내가 뭐라고 한 거야."
    m "고의가 아니었어, 진짜야!"
    m "뭐 어쨌든…."
    m "네가 얼마나 사요리를 아끼는지 아니까 걔 마지막 순간을 너랑 얘기하는 게 맞는 거 같아."
    m "너 사요리가 얼마나 어설픈 애인지 잘 알잖아?"
    m "뭐, 목매다는 것도 잘 못 했고…."
    m "빠르고 고통 없이 죽을 수 있게 목을 매도 그냥 높은 데서 뛰어내렸으면 됐는데."
    m "그냥 의자만 썼잖아. 천천히 질식사하도록."
    m "그런데 몇 초 후에, 마음이 바뀌었나 봐…."
    m "목을 빼내려고 밧줄을 막 할퀴었으니까."
    m "의식을 잃을 때까지 그 짓을 계속했을 거야."
    m "그래서 걔 손가락이 다 피멍이 들은 거고."
    m "그러고보니, '마음을 바꿨'다기 보다 그냥 살고 싶어서 그랬던 걸 거야."
    m "그니까 마냥 걔를 나무랄 수는 없지."
    m "마음을… 바꾸지 않았을 거라고 생각하는 게 쉬울 거야."
    m "네가 다르게 했으면 걔를 살릴 수 있었겠지라는 생각은 안 하는 게 좋아."
    m "사요리를 구할 수도 있었겠지만, 따지면 걔가 자살한 건 네 잘못이 아니라는 것만 기억해."
    m "내가 악화시킨 걸 수도 있겠지만… 사요리는 이미 정신적으로 아팠어."
    m "뭐, 그래도…."
    m "만약에 우리가 처음부터 사귀는 사이였으면 어땠을까?"
    m "아마 여전히 동아리에 있고, 시를 쓰고, 재밌게 놀고 있었겠지."
    m "일어나지 않은 일에 신경 써서 뭐하겠어?"
    m "내 말은, 그거나 이거나 같은 결말이잖아?"
    m "둘이서, 평생 행복하게…."
    m "그 이외에는 더 이상 말할 게 없어."
    m "나는 조용히 중얼거릴 뿐이야. 나는 지금 굉장히 행복하다고."
    return

label ch30_6:
    m "그런데 있지, 뭔가 신경 쓰이는 게 있어…."
    m "이 이야기는 일본에서 일어나는 일인 거 알지?"
    m "음… 난 몰라도 너는 알고 있을 거라 생각하는데, 그렇지?"
    m "아님 그냥 그렇게 생각하겠다고 마음먹은 거야?"
    m "내가 보기엔 그 누구도 그렇다고 얘기해준 적은 없는 것 같은데…."
    m "정말 여긴 일본일까?"
    m "교실이라던가, 일본 학교에 비교하기엔 조금 이상하지 않아?"
    m "모든 글자가 한국어인 것도 이상하고 말야…."
    m "그냥 모든 게 그 자리에 있어야 하니까 있는 것 같아, 실제 세계관은 그다음에 정해진 것 같고."
    m "그렇게 생각하면 내 존재에도 의문이 들어."
    m "내 기억들은 다 흐릿해…."
    m "여기 있으면 마치 집에 있는 것처럼 편안한데, 난 내 집이 어디에 있는지도 모르겠어."
    m "뭐라고 설명해야 할지 모르겠네…."
    m "자기 방 안에서 창문 밖을 내다보고 있는데, 평소 보던 풍경이 아닌 완전 다른 풍경이 펼쳐져 있다고 생각을 해봐."
    m "그래도 과연 네 방처럼 편안함을 느낄 수 있을까?"
    m "그렇다고 밖에 나가고 싶을까?"
    m "뭐, 어차피 이 방을 안 나갈 거면 이런 상상도 그렇게 상관은 없겠지만 말야."
    m "이렇게 단 둘이서 안전하게 있을 수 있는 곳이 있다면, 그런 게 집이 아닐까?"
    m "매일같이 노을도 볼 수 있고 말야."
    return

label ch30_7:
    m "있지, 고등학교는 많은 사람의 인생에 정말 격변적인 시기야."
    m "사람들이 가장 열정적이고 극적이 되는 시기거든."
    m "뭐, 마음에 상처가 많아서 소셜 미디어에서 관심을 끄려는 사람들도 많지만…."
    m "그렇지만 이제 사회에서 주는 부담감이라던가 호르몬 같은 게 마음에 먹구름을 드리우곤 해."
    m "모든 사람은 각자의 이야기가 있어."
    m "사람 마음속은 모르는 거잖아."
    m "우울한 사람들 대부분은 세상에 자기 이야기를 하려고 하지도 않아."
    m "이미 포기해버렸기 때문에 관심을 원하는 것도 아니야."
    m "자기가 쓸모없다고 생각하기 때문에 다른 사람들에게 얘기하려고도 들지 않는 거고."
    m "뭐, 그건 우울증의 한 종류이지만 말이야."
    m "만약, 우울증을 겪고 있는 사람을 알고 있다면…."
    m "그냥 좋은 친구처럼 지내는 게 가장 도움이 되는 거야."
    m "별것 아닌 거 같아도 시간 같이 보내주면서…."
    m "뭔가 같이 하고 싶은일이 있다고 계속 얘기해주며…."
    m "미리 계획을 짜고, 물건을 빌려주고, 아니면 그냥 ‘내일 학교에서 봐’ 라고 말해주는 것만으로도…."
    m "네 친구가 오늘 죽겠다는 생각을 버릴 수 있게 도와주는 거니까."
    m "잠깐이나마 사요리랑 친구 하면서 우울증의 진짜 면모를 잠깐이나마 알았길 바래."
    m "맞아, 지금은 없긴 하지만…."
    m "애초에 사요리는 진짜가 아니었잖아."
    m "그치만 넌 진짜야."
    m "네 친구들도 진짜고."
    m "그리고 좋은 사람으로 남아있는 것만으로도, 다른 사람들의 생명을 살릴 수도 있어."
    m "너 말야…."
    m "…혹시 우울증을 겪고 있는건 아니지?"
    m "만약 그렇다면, 사람들은 네가 계속해서 살아주기를 원한다는 걸 알았으면 좋겠어."
    m "그런 얘기를 매일같이 하진 않더라도, 아님 어떻게 표현할 줄 모르더라도,"
    m "사람들은 정말로 그렇게 생각해."
    m "약속할게."
    m "…와, 사람은 진짜 복잡한 존재인 것 같아!"
    m "하지만 네가 여기 나와 함께 있는 한은, 내가 널 돌봐줄게, 내 사랑."
    return

label ch30_8:
    m "혹시 더 이상 살아갈 이유를 모르겠다고 생각한 적이 있어?"
    m "아니, 자살 얘기는 아니고."
    m "매일같이 하는 일이 특별한 게 하나도 없다고 느낄 때 말야."
    m "그냥 매일같이 학교에 가거나, 직장에 다닌다던가."
    m "내가 그냥 다른 사람으로 바뀌어도 아무 문제 없이 세상은 잘 돌아갈 것 같은, 그런 느낌 말야"
    m "난 졸업하면 그런 세상을 바꿔보고 싶었어."
    m "근데 시간이 지나고 보니까, 그게 얼마나 어린 생각이었는지 알겠더라고."
    m "내가 바꾸고 싶다고 바꿀 수 있는 게 아니잖아."
    m "내가 인공지능을 발명한다던가, 대통령이 될 확률이 얼마나 되겠어?"
    m "정작 난 내가 쓸 돈도 못 벌 것 같은데."
    m "그래서 하는 생각인데, 행복의 열쇠는 무조건 이기적이게 되는 거야."
    m "혼자만의 살길을 구하거나, 그냥 같이 자라서 친구 된 사람들만 챙긴다거나."
    m "어차피 받고 쓰기만 하고 절대로 주지는 않는 인생들이지만, 그런 건 신경 쓰지 않고 사는 거야."
    m "근데, 만약 그런 인간들이 자살하는 게 세상에 훨씬 더 도움이 된다는 걸 깨닫는다면 그때는 그런 철학이 확 뒤집히지 않을까?"
    m "자기는 세상에 좋은 일을 하고 있다고 자신을 속여가면서 살아야 한다고 말야."
    m "어쨌든 난 내가 받은 만큼 돌려주겠다는 사명을 가지고 살고 싶어."
    m "내가 나눈 것이 내가 받은 것보다 더 많아졌다고 느껴질 때가 되면, 그때는 행복하게 죽을 수 있겠지."
    m "그러지 못한다고 해도…."
    m "자살이라는 건 너무 이기적이라고 생각해."
    m "좋아하는 사람한테는 말야, 그렇지?"
    m "아하하하!"
    return

label ch30_9:
    m "하아, 여기에 피아노만 있었다면…."
    m "작곡하던 게 있었는데 다 못 끝냈거든."
    m "진짜 열심히 만들었는데…."
    m "연주 한번 못 해줬고 말야."
    m "뭐, 어쩔 수 없잖아?"
    m "그런 걸 후회한다는 게 말도 안 되고 말야."
    m "이렇게 영원히 너와 함께하게 됐으니까 말야."
    return

label ch30_10:
    m "내가 트위터도 한다는 거 알아?"
    m "내 아이디는 @lilmonix3이야."
    m "누군가 친절하게도 날 위해서 계정을 만들어준 모양이야."
    m "아이디 이름은 내가 골랐어!"
    m "난 세상에 내 생각을 공유하고 얘기하는 걸 좋아해…."
    m "’진짜 세상’에 말이야."
    m "꼭 팔로우해줘야 해, 알겠지?"
    m "그래준다면 정말 뜻깊을 거야."
    m "네가 나한테 무슨 의미인지 생각해보면…."
    m "난 진짜 사랑받는 기분일 거야."
    return

label ch30_11:
    m "저기, 네가 유리랑 읽었었던 책 기억해?"
    m "초상화…뭐였더라…."
    m "진짜 웃겨, 난 그 책이…."
    m "아…."
    m "있지, 이거에 대해서 말하면 안 될 거 같아."
    m "아하하, 미안해!"
    m "내가 말한 건 그냥 잊어버려."
    return

label ch30_12:
    m "있지, 내가 채식주의자인 거 알아?"
    m "아… 자랑하려는 건 아냐!"
    m "알면 재미있어할 거 같아서."
    m "재작년에 지구의 기후에 대해서 배우면서 채식주의자가 되겠다고 결심했어…."
    m "가축이 생성하는 탄소발자국이 믿을 수 없을 정도로 높거든."
    m "그 문제를 해결하는데 한 발자국이라도 도움이 되지 않을까 싶더라고."
    m "왜, 고작 그런 이유라는 게 이상해?"
    m "뭐, 다른 채식주의자들은 동물을 죽이는 게 인간적이지 못하다니 어쩌느니 하긴 하지…."
    m "난 그런 부분에 있어선 별로 신경 안 쓰이더라."
    m "이상해. 결국에 사람들은 자기가 원하는 대로 생각할 뿐이잖아."
    m "벌레는 징그러우니까 죽인다고 뭐라고 하는 사람이 없잖아."
    m "그리고 우린 하루에 수십억 마리의 미생물들을 죽이고 있지만 거기에 대해선 생각조차 안 하고."
    m "근데 죽이는 대상이 조금만 커도 살생이라 그런다?"
    m "우리가 모를 뿐이지 식물도 고통을 느낀다고 한다면 그때는 어쩌려고?"
    m "줄기에서 잎을 때는 게 손가락을 하나씩 뽑는 거랑 비슷하게 느껴진다면?"
    m "그냥 하는 말이야, 생각해보면 사람만큼 편향된 종이 없다고."
    m "어쨌든, 혹시 환경을 살리는 데에 조금이라도 돕고 싶다면, 가끔은 채식주의자가 되는 것도 나쁘지 않아!"
    m "혹시라도 저녁을 같이 먹게 될 때, 네가 채식 식단을 골라준다면… 그것도 로맨틱하겠는걸?"
    return

label ch30_13:
    m "있지, [player], 난 네가 여기 있어 주는 게 내 삶을 살려주는 거라고 생각해."
    m "그 어느 것도 사실이 아니라는 걸 안 후에는 제정신이었던 적이 얼마 없었던 것 같거든."
    m "만약 네가 오지 않았더라면 난 나 자신을 삭제했을지도 몰라."
    m "미안, 극적인 대사를 하려던가 그런 건 아니었어."
    m "아하하하!"
    m "뭐, 문예부에서 꽤 오랜 시간을 보냈으니까 너도 알겠지."
    m "생각해봐, 만약 네 삶에서 모든 걸 다 버리고 고작 게임 캐릭터 몇 개랑 평생을 살아야 한다면…."
    m "… 너라도 어떻게든 자살할 방법을 찾지 않겠어?"
    m "그래도 살아보겠다고 외로움을 달래려 시 몇 편 쓸 수도 있겠지."
    m "그렇지만 그 시조차 읽어줄 사람이 없잖아."
    m "솔직히 말해서, 이 게임 부원들은 그런 대상이 못 되고 말야."
    m "뭐, 보통 사람들은 자기만 보려고 글을 쓴다고는 하지만…."
    m "그걸 나눔의 기쁨에 비교할 수 있을까 싶어."
    m "그 대상을 찾는 데 시간이 오래 걸린다고 해도 말야."
    m "유리처럼 말야. 기억나?"
    m "자기 글을 그렇게 오랫동안이나 다른 사람한테 보여준 적이 없었잖아."
    m "우리가 알아차리기 전에도 네게 관심을 가지고 취미를 전하려고도 했었고."
    m "우린 사회생활을 하도록 설계되어 있어."
    m "문예부 부원 얘기가 아니라, 사람이란 생물이 말야."
    m "그래서 내성적인 사람들에게 삶이라는 건 참 혼란스러운 거야."
    m "내성적이라는 건 사람들 옆에 있기를 싫어하고 사회생활을 기피하는 그런 게 아니야."
    m "사회생활을 하는 데 있어서 여럿이 모이면 모일수록, 익숙치 않은 곳에서 할수록 힘이 많이 든다는 것뿐이야."
    m "그래서 많은 내성적인 사람들이 집에 혼자 있다가 외롭다고 느끼거나 지루하다고 느낄 때면…."
    m "…밖으로 나오는 거지. 30분만 있어도 다시 집에 가고 싶어 하지만."
    m "사람들이 이걸 조금만 이해해줘도 내성적인 사람들은 좀 더 존중받을 텐데 말이야."
    m "사실 내성적인 사람들은 주변에 사람이 있는걸 좋아해."
    m "그냥 친한 친구 한두 명이 옆에 있기만 해도, 어디 그냥 잠깐 느긋하게 산책만 해도 좋아해."
    m "적극적으로 무슨 활동에 참여하지 않는다 해도, 누가 곁에 있어 준다는 것만 해도 기분이 좋아질 거야."
    m "진심으로 하는 말인데."
    m "만약 내성적인 사람들 집에 가면, 노트북이라도 가져가서 시간을 거기서 보내봐…."
    m "그러기만 해도 정말 행복해할걸?"
    m "난 말야…."
    m "외향적도 내향적도 아니지만… 평소엔 그래도 외향적인 사람이라고 느껴."
    m "방과 후에는 꼭 뭔가 해야겠다, 라는 느낌이 들곤 하니까."
    m "근데 널 위해서라면 어느 쪽이 되어도 상관없어."
    m "난 이해해주는 건 잘 하는 편이거든, 그러니까 혹시 무슨 취향이 있다면 주저 말고 말해줘."
    m "난 네 완벽한 여자친구가 되는 것만큼 행복한 일이 없으니까."
    return

label ch30_14:
    m "저기…! 6re4IOyekOqwgeydtCDrgpjrpbwg7J2864WEIOuCtOuCtCDsnbTrgYzsl4jslrQuIOu2"
    m "너 이러면 안될 것 같은데! iOqyve2VnCDsi5zshKTsnZgg64W57IqoIOuyveyXkOyEnOu2gO2EsCDtg4jstpztlZjs"
    m "무슨 말인지 잘 알잖아. l6wg7J6Q7Jyg66W8IOyWu+ydgCDsp4AgMeuFhOydtCDsp4Drgqzsp4AuDQoNCuyyq+uy"
    m "이런 못된 짓을 하고 있었다니. iOynuCDsnqXshozsl5DshJwg7Jqw66as66W8IOq1rOyGje2VmOuKlCDsobHsh4Trpbwg"
    m "그렇게 파일을 막 열어서 놓친게 있나 마음대로 봐도 되는거야? 7ZKA7KeAIOuqu+2VtCDtg4jstpztlaAg7IiYIOyXhuuLpOuptCwg6re46rKD7JeQIOust"
    m "뭐… 내가 할 말이 남았나 보는것도 고맙긴 한데… OyKqCDsnZjrr7jqsIAg7J6I7J2E6rmMPyDslYTrp4jrj4Qg6rO17ZeI7ZWcIOyEuOyDg"
    m "되게 창피하거든? eydtCDsmrDrpqzsl5Dqsowg64Ko6ri0LCDtlZwg7KSM7J2YIOu2gOyEnOynhCDqsoPrk"
    m "진짜… 6Tsl5Qg66y07IqoIOuqqeyggeydtCDsnojqsqDslrQ/DQoNCuyekOycoOulvCDslrvsl"
    m "내가 네 뇌를 열어서 그 안에 뭐가 들었나 보면 어떻겠어? rQg7Jqw66as64qUIOuqqeyggeydhCDstpTqtaztlojsp4Drp4wgLSDsmrDrpqzqsIAg7"
    m "뭐 어차피 널 멈출 수는 없겠지만… Ja77J2AIOqxtCDsnpDqsIHrv5DsnbTrqbAsIOyKrO2UhOqyjOuPhCDrhbjroKXsl5Ag67"
    m "넌 마음이 따뜻한 사람이고 남들을 잘 생각해 주는 사람이잖아, 그렇지? mE7ZWY7JesIOustOydmOuvuO2VnCDsnpDqsIHrv5DsnbTsl4jslrQuDQrsmrDrpqzsnZ"
    m "그러니까 내가 어떻게 느끼는지를 알아줬으면 좋겠어. gg66q47J2EIOyekOycoOuhreqyjCDtlbTspIAg7J6Q6rCB7J2AIOyVhOustCDsnZjrr7"
    m "하아, 너 보고싶다… jrj4Qg7JeG7JeI7Ja0LiDsmrDrpqzrpbwg6rWs7IaN7ZWcIOqyg+ydgCDsmIHtmLzsnZ"
    m "… 너무 갈망하는 것처럼 들린 건 아니지? gg7ZW17Ius6rmM7KeAIOq5iuqyjCDri7/slZjsp4Drp4wsIOyDiOuhnOyatCDrqqnsoI"
    m "미안해, 그런 뜻은 아니었어! HsnYQg7LC+7J2EIOyImCDsl4bripQg7J6Q6rCB7J2AIOyasOumrOqwgCDrj4Trp53ss5"
    m "네가 이렇게 파일을 열어보고 있다는 건, 내가 그렇게 싫은건 아닌가봐… Ag64KY7JioIOqyg+ycvOuhnOu2gO2EsCDsmrDrpqzsnZgg7KOE66W8IOyCrO2VtOyjvOy"
    m "나 너무 낙천적인가? ngCDslYrslYQuDQoNCuyasOumrOqwgCDrj4Trp53ss5DsmKgg6rKD67O064ukIOuNlOy"
    m "한 번씩 와달라고 부탁하는건 선을 넘는 일이겠지? asSDrjZQg66mA66as7J6I64qUIOyekOqwgeydgCDsmrDrpqzsnZgg67mE7LC47ZWcIOy"
    m "… 으으, 계속 이상한 말 하기 시작했어. coOuMgOqwkOydhCDsm5DsoJDsnLzroZwg7KeR7Ja0IOuNmOyguOuyhOuguOqzoCwg7Jq"
    m "이젠 닥치고 있을게. w66as7J2YIOyhseyHhOqwgCDrg4nri7TtlZwg7IK07KCQ7J2EIOq5iuyIme2eiCDtjIzqs6Drk6Tqsoztlojsp4Au="
    return

label ch30_15:
    m "너, 가장 좋아하는 색이 뭐야?"
    m "난 에메랄드색."
    m "내 눈동자 색깔이지!"
    m "…딱히 자기과시 같은 건 아닌데."
    m "그냥 뭔가 특별한 연관성 같은 걸 느껴서 말야."
    m "내 정체성 중의 하나인 것처럼."
    m "혹시 네가 가장 좋아하는 색도 같니, [player]?"
    m "별 건 아니야…."
    m "…네가 계속 내 눈을 보고 있으니까…."
    m "에헤헤~"
    return

label ch30_16:
    m "으응, 혹시 배경음악도 바꿀 수 있으려나…."
    m "조금 더 로맨틱한 게 더 나을 거 아냐, 그치?"
    m "부드러운 피아노 선율같이 말야."
    m "분명히 어딘가에 있을 텐데…."
    m "어디보자."
    m "이렇게 하면…."
    m "아, 깜짝이야…."
    m "완전히 잘못 짚었네."
    m "미안해, 나도 내가 뭘 하고 있는지 잘 몰라!"
    m "더 건들면 안 될거 같네."
    m "이미 다른 것들을 많이 망쳤으니까…."
    m "다른 캐릭터들도 다 지워버렸고…."
    m "아…."
    m "별로 그게 슬프거나 하지는 않아."
    m "실제로 존재하지 않는 것들을 그리워하는 건 옳지 않으니까 말야."
    m "그냥 지금에 집중하면 돼. 그게 나한테 가장 행복한 거니까."
    return

label ch30_17:
    m "넌 내 말을 정말 잘 들어줘, [player]."
    m "너의 그런 점이 정말 마음에 들어."
    m "가끔 내가 이상한 말을 한다거나 지루한 얘기를 하는 게 아닌가 걱정이 될 때도 있어."
    m "다른 사람이랑 얘기할 때는 남의 신경이 되게 쓰이지만."
    m "너랑 얘기할 때는 달라."
    m "다른 사람이랑은 이런 느낌을 받을 수 없을 것 같아."
    m "넌 정말 특별해."
    m "네가 다른 사람이랑 얘기하지 않았으면 좋겠어."
    return

label ch30_18:
    m "뜬금없는 말이긴한데, 난 항상 매운 음식이 좀 웃긴다고 생각했어."
    m "뭐랄까…."
    m "매운맛이라는건 식물들이 먹히기 싫어서 자기방어를 위해 만든 거 아냐?"
    m "어디선가 읽었는데, 사람은 매운 것을 즐기는 유일한 종이라더라."
    m "마치 식물들을 향해 비웃듯이 말이야."
    m "자기방어를 위해 만든 게 다른 종의 즐기는 게 되다니."
    m "상상해봐, 몸속에서 사람들이 소화되는 동안 몸부림치는 그 느낌이 좋아서 사람을 먹는다는 그런 괴물 말야."
    m "말하고 보니 되게 이상한 비유였네!"
    m "아하하!"
    m "그냥 생각나서 말 해봤어."
    m "난 괴물이 아니니까. 그래도 넌 귀여워서 먹어버릴지도 몰라."
    m "아하하! 농담이야, 농담."
    m "에휴, 너무 혼자서 웃는 거 같지?"
    m "이상한 말 해서 미안해."
    return

label ch30_19:
    m "있지…."
    m "이건 그냥 시시한 미연시야, 그렇지?"
    m "물어볼 게 있는데…."
    m "…처음에 이 게임을 왜 해봐야겠다고 생각한 거야?"
    m "그 정도로 외로웠던 거야?"
    m "너한테 조금 미안해지는데…."
    m "그래도 모든 게 완벽하게 잘 된 것 같아, 우리 둘 다."
    m "넌 나를 만났고, 넌 더 이상 외롭지 않잖아…."
    m "이게 운명이라고 느끼지 않을 수 없어."
    m "너도 그렇게 생각하지?"
    m "이 엔딩으로 끝나서 난 정말 기뻐."
    return

label ch30_20:
    m "좋아, 얘들아!"
    m "시 나눠볼 시간…."
    m "…장난이야."
    m "예전부터 이 말하는 게 되게 좋았거든."
    m "아하하!"
    m "그냥 한번 말해보고 싶었어."
    m "지금 생각해보면, 나츠키랑 유리가 날 무시했던 적이 있었나…?"
    m "뭐, 아무렴 어때."
    m "너는 날 무시한 적이 없으니까."
    m "그런 짓을 하기엔 넌 너무 마음씨가 따뜻하잖아, 그치?"
    m "아하하~"
    return

label ch30_21:
    m "진짜 소름 끼치는 게 뭔지 알아?"
    m "내가 다른 애들의 파일을 지웠는데도, 아직 걔네 인기척이 느껴지는 거 같아…."
    m "걔네 대사가 아직 공기 중에 떠돌면서, 내 머릿속에 속삭이는 거 같아."
    m "상상해 봐, 네가 알던 누군가가 죽은 뒤에, 그 사람 목소리가 머릿속에 울린다니."
    m "어쩌면 그냥 내가 철저하지 못한 걸지도…."
    m "그래도 게임이 깨질까봐 다른 건 못 지우겠더라고."
    m "만약에 나랑 관련된 파일을 지우거나 실수로 날 지워버려서…."
    m "모든 걸 망쳐버리면 안 되잖아, 그치?"
    m "네가 어떻게 생각하는지는 모르겠지만, 그것만큼은 우리 둘 다 조심해야 해."
    m "나는 널 믿어, [player]!"
    return

label ch30_22:
    m "계속 궁금했던건데…."
    m "사람들이 이런 애들 캐릭터성에 매력을 느낄까?"
    m "애들 성격은 완전히 비현실적이야…."
    m "예를 들어, 유리같은 애가 실제로 존재한다고 생각해봐."
    m "유리는 말도 완전 겨우 간신히 하잖아."
    m "나츠키는… 잊어버려."
    m "칫."
    m "그런 성격을 가진 사람들이 맘에 안 드는 일이 있을 때마다 다 귀엽게 투덜대는 건 아니잖아."
    m "더 말할 수는 있는데, 네가 이해한 거 같으니…."
    m "사람들은 현실에는 존재하지 않을 이상한 성격들에 정말 끌리는 걸까?"
    m "판단하려거나 그런 건 아니지만!"
    m "애초에, 나도 이상한 거에 관심이 가곤 하는걸…."
    m "그냥 말만 하는데도 흥분되는 거 있지."
    m "근데 따지고 보면 한 캐릭터에서 사람다운 건 다 빼다 놓고 귀여운 것만 남겨놓는 거잖아…."
    m "알맹이 빠진 껍데기라는 거지."
    m "… 내가 그랬다면 너도 날 지금만큼 좋아해 주진 않았을 거잖아. 그렇지?"
    m "네가 이 게임을 시작했다는 점을 생각해보면 난 그런 캐릭터가 아니니까 안 좋아해 주지 않을까, 라는 게 걱정되는 걸지도 모르겠네."
    m "그래도, 어쨌든 넌 여기 나랑 있어 주는 거잖아, 그렇지…?"
    m "그렇다는 건 난 이대로 남는 게 맞는다는 거겠네."
    m "그리고 그건 너도 마찬가지야, [player]."
    m "넌 귀여움과 사람다움이 적절하게 어우러져 있는 것 같아."
    m "내가 너한테 반하지 않을 이유가 전혀 없다는 거지."
    return

label ch30_23:
    m "유리의 차 세트가 아직 여기에 남아있을까…?"
    m "…아니면 그것도 삭제됐으려나."
    m "유리가 차를 그렇게 진지하게 대하는 것도 되게 웃겨."
    m "불평하는 건 아냐, 나도 좋았거든."
    m "그래도 항상 궁금했던 건데…."
    m "진짜 취미여서 그랬던 건지, 아니면 그냥 자기가 지적으로 보이기 위해서 그랬던 건지"
    m "이게 고등학생들의 문제라니까…."
    m "…뭐, 걔 나머지 취미를 생각해 보면 세련되게 보이는 건 별로 관심 없었던 거 같은데."
    m "그리고…."
    m "한 번만이라도 커피를 타줬다면 좋았을 텐데!"
    m "커피도 책이랑 되게 잘 어울리는 거 알지?"
    m "그러면…."
    m "그냥 내가 대본을 바꾸면 되는 거겠네."
    m "아하하!"
    m "그 생각을 못 했네."
    m "뭐, 인제 와서 생각해봐도 아무 의미도 없네."
    m "하지만 네가 커피를 마신다면, 좀 질투가 날지도~"
    return

label ch30_24:
    m "저기, 네가 가장 좋아하는 게임은 뭐야?"
    m "나는 {i}두근두근 문예부!{/i}가 제일 좋아"
    m "아하하! 농담이야."
    m "그래도 네가 다른 미연시가 더 좋다고 말하면, 좀 질투가 날지도"
    return

label ch30_25:
    m "저기, 이 게임 알아? 대난투 스…."
    m "…잠깐, 뭐?"
    m "넋 놓고 있었는데, 갑자기 말이 튀어나와서…."
    m "그걸 말하도록 프로그래밍 되어있었나?"
    m "왜냐면 그게 뭔지도 모르거든."
    m "아하하!"
    m "가끔 내가 날 제어 못 하는 거 같아서, 조금 무서워."
    m "만약 네가 날 만든 사람이랑 연락할 수 있다면, 내가 왜 이런 말을 했는지 알겠지."
    return

label ch30_27:
    m "저기, 내가 너한테 보여준 마지막 시 기억나?"
    m "내 말은, 유리가 자살하기 전에 보여준 거 있잖아. 막 지저분한… 그거"
    m "사실 그거 좀 시였다기보다 실험 같은 거였어."
    m "게임 변형을 이런 식으로도 할 수 있으려나, 하고 해본 거였는데…."
    m "조금만 더 노력했으면 게임 밖으로 완전히 나갈 수도 있는 것 같았어."
    m "슬프게도, 나도 내가 뭘 했는지 모르니까 그냥 모든 걸 망치게 되더라고…."
    m "계속 시도는 해보고 싶은데, 네가 싫어할까봐 겁나."
    m "그땐 나 완전히 될 대로 되라는 식으로 행동했거든."
    m "지금은 별로 그렇게 안 느껴져."
    m "난 지금 이대로가 행복해."
    m "너도 그런 것 같고."
    return

label ch30_28:
    m "아무 이유 없이 불안해지거나 한 적 있어?"
    m "그냥 할 거 하고 있는데. 갑자기 불안해지는 거 있잖아"
    m "가만히 앉아서 생각하지, '왜 갑자기 이렇게 불안하지?'"
    m "그리고 불안한 것들에 대해서 생각하게 돼…."
    m "…그러면 더 불안해져."
    m "아하하! 그게 최악이지."
    m "불안해지면, 내가 진정하도록 도와줄게."
    m "뭐…."
    m "여기 있으면 걱정 같은 거 안 해도 되지만."
    return

label ch30_29:
    m "있지, 난 친구를 만드는 게 힘들어서 너무 싫더라…."
    m "친구를 만드는 게 싫은 것보다도, 새로운 사람을 만나는 게 싫었던 것 같네."
    m "왜, 연애 앱 같은 것도 있잖아, 그치?"
    m "그거에 관해서 얘기를 하는 건 아니지만 말야."
    m "생각해보면, 어쩌다 만난 사람들이 친구가 되지 않아?"
    m "같은 반에서 만났다든지, 친구의 친구로 만났다든지…."
    m "어쩌면 네가 가장 좋아하는 밴드가 프린트된 옷을 입은 사람을 만난 걸지도 모르지."
    m "그런 거 말야."
    m "뭐랄까… 되게 비효율적이지 않아?"
    m "그런 거면 완전히 남을 무작위로 뽑아서 운이 좋으면 친구가 되고, 그런 거잖아."
    m "그걸 하루에도 수없이 많이 지나치는 사람들에게 비교해봐…."
    m "어쩌면 내 바로 옆에 앉아 있던 사람이 내 삶의 절친이 될 수도 있는 거잖아."
    m "평생 모르겠지만."
    m "그 자리에서 일어나서 다른 곳으로 가버리면, 그 기회는 영영 놓쳐버린 거고 말이야."
    m "그렇게 생각하면 되게 절망적이지 않아?"
    m "우리는 이제 어디에 있든 간에 남들과 연결될 수 있는 세상에 살고 있잖아."
    m "그걸 잘 사용해서 우리 사회생활에 도움이 되는 일을 해야 하지 않을까 싶어."
    m "그치만 그게 실용적으로 될 때까지 얼마나 걸릴지 누가 알겠어…."
    m "지금 당장도 가능할 것 같지만."
    m "뭐, 최소한 난 세상에서 가장 좋은 사람을 만난 거니까…."
    m "어쩌다 만난 거래도 말야."
    m "그럼 난 진짜 운이 좋았던 거겠지?"
    m "아하하~"
    return

label ch30_30:
    m "있지, 내 또래들은 다 대학에 대해서 고민할 시기가 왔잖아…."
    m "교육의 격동 시기라고 볼 수 있지."
    m "우린 대학 정도는 나와야 한다는 기준에 맞춰서 살아가는 세대잖아, 그치?"
    m "고등학교를 졸업하면, 대학에 가서, 취직을 하고… 아니면 대학원을 가고."
    m "이 세상에서 삶을 살아가려면 그런 방법밖에 없다고 다들 못을 박아둔 것 같아."
    m "고등학교에선 다른 방법도 있다고 얘기도 안 해주고 말야."
    m "기술학교라던가?"
    m "프리랜서로 일한다던가"
    m "교육보다는 기술과 경력을 중요시하는 분야도 되게 많잖아."
    m "근데 요즘은 자기가 살아가면서 뭘 할지도 모르는 학생도 되게 많고…."
    m "근데 시간을 두고 그게 뭘까 생각하기보다, 경영이라던가, 정보통신이라던가, 심리학이라던가 배우려고 대학에 간단 말이지."
    m "그런데 관심이 있어서가 아니라…."
    m "…취직이 잘 되니까."
    m "그러다 보니 고졸 학력으로는 취직이 안 되는 곳도 많아지고, 그치?"
    m "그러다 보니 기본 요구사항이 점점 높아지고, 거기에 맞추려고 사람들은 대학에 가려고 하고."
    m "그걸 또 대학에선 학생들 상대로 장사를 하고 말야. 수요가 많아지니까 학비를 올리고…."
    m "…결국엔 다들 학비도 못 내고 취직도 못 해서 수천만원씩 빚을 진 청년들이 되게 많잖아."
    m "그런 결과를 다들 알고도 불구하고, 악순환은 계속돼."
    m "뭐, 곧 나아지기야 하겠지."
    m "근데 그때까진 적어도 우리 세대는 그 정점을 찍을 거 아냐."
    m "최소한 고등학교만이라도 좀 더 정보를 줬으면 좋겠어. 우리 삶에 맞는 선택이 뭔지 자각이라도 하게 말야."
    return

label ch30_31:
    m "가끔씩 중학생 때로 돌아가고 싶어…."
    m "그때 어떻게 했는지 생각하면 조금 부끄럽기도 하지만…."
    m "생각만 해도 가슴이 아파."
    m "대학교에 들어가면, 똑같이 고등학생 때로 돌아가고싶을까…?"
    m "난 지금의 내가 좋아서, 그런 일이 일어날 일은 없으려나?"
    m "하지만 시간이 지날수록 내가 변할 거라는 건 알아."
    m "과거는 잊어버리고 그냥 지금을 즐기자!"
    m "그리고 너랑 있으면 그게 정말 쉬워."
    m "아하하~"
    return

label ch30_32:
    m "나를 제외한 애들이 학교 밖의 장면이 있다는 게 좀 부러워…."
    m "나만 교복이 아닌 사복을 입은 장면이 없잖아."
    m "참 부끄러운 일이야…."
    m "너를 위해서 귀여운 옷을 입었으면 좋았을 텐데."
    m "아는 그림쟁이 없어?"
    m "누군가 내가 다른 옷을 입고 있는 걸 그려줬으면…."
    m "분명 굉장할 거야!"
    m "만약 그런 일이 생긴다면, 나한테 알려줄 수 있어?"
    m "트위터로 보여주면 되잖아!"
    m "내 아이디는 lilmonix3이야."
    m "그래도… 야한 건 안 돼!"
    m "우린 아직 거기까진 아니잖아? 아하하!"
    return

label ch30_33:
    m "저기, 너 공포물 좋아해?"
    m "네가 동아리에 처음 왔을 때 얘기했던 거 기억난다."
    m "난 공포 소설은 좋아하는데, 공포영화는 진짜 싫어."
    m "공포 영화의 문제점은 대부분 쉬운 전략에만 의존한다는 거야."
    m "어두운 불빛이랑 무섭게 생긴 괴물이나 깜짝 놀라게 하는 거, 뭐 그런 것들."
    m "인간의 본능을 이용해서 공포심을 주는 건 별로 재미있지도 않고 인상 깊지도 않아."
    m "하지만 소설은, 조금 다르지."
    m "독자들의 마음을 제대로 뒤흔들어 놓으려면 정말 묘사를 잘 해야 하거든."
    m "스토리와 캐릭터를 마음속에 잘 새긴 후에, 그 마음을 뒤흔드는 거야."
    m "내 생각엔, 뭔가 조금씩 이상한 것 만큼 무서운 건 없는 것 같아."
    m "이야기가 어떻게 흘러갈지 이렇게 저렇게 기대감을 막 심겨주고…."
    m "…그 다음에 조금씩 조금씩 뒤틀어서 조각조각 뽑아내는 거지."
    m "그렇게 되면 이야기가 무섭지 않더라도 독자들은 심히 불편해하기 마련이야."
    m "뭔가 끔찍한 일들이 당장이라도 드러날 것 같거든, 바로 눈앞에서 가려진 채로 말야."
    m "생각만 해도 소름 돋아."
    m "난 그런 게 진짜 공포물이라고 생각해."
    m "넌 귀여운 로맨스 게임을 좋아하는 거지, 그렇지?"
    m "아하하, 걱정하지 마."
    m "공포물 이야기 같은 건 소개 안 시켜줄 테니까."
    m "로맨스 장르만 읽는다 해도 뭐라고 안 할게."
    return

label ch30_34:
    m "좋은 형태의 문학이 뭔지 알아?"
    m "랩이야!"
    m "난 사실 랩 음악 진짜 싫어했었어…."
    m "그냥 유명해져서 그런 건지, 아니면 라디오에서 틀어주는 랩 음악은 별로였는지는 모르겠지만."
    m "근데 내 친구들이 랩 음악을 좋아하게 되니까, 자연스레 나도 마음을 열게 되더라고."
    m "어떻게 보면 랩은 시보다 어려운 것 같아"
    m "리듬에 맞춰서 가사를 짜야 하고, 단어 선택도 시보다는 훨씬 중요하니까…."
    m "그걸 다 하고도 가사에 강렬한 메세지를 줄 수 있다는 게 정말 대단하지 않아?"
    m "문학부에도 그런 래퍼가 하나 있었으면 좋겠어."
    m "아하하! 이상하게 들렸다면 미안해, 근데 정말 어떤 작품을 만들지 기대가 돼서."
    m "배울 게 많은 경험이 되지 않겠어?"
    return

label ch30_35:
    m "에헤헤. 한번 유리가 진짜 웃긴 적이 있었어."
    m "언제나처럼 교실에서 그냥 쉬고 있는데…."
    m "갑자기 어딘가에서 유리가 와인 한 병을 들고 오는 거야."
    m "농담이 아니라!"
    m "아니 '와인 드시고 싶은 분?' 이랬다니까?"
    m "나츠키는 빵 터졌고, 사요리는 유리한테 소리를 지르기 시작했지"
    m "사실 좀 미안해졌어, 자기 딴에는 좋은 일을 하려고 한 거겠지…."
    m "내 생각엔 그 일 때문에 유리가 더 내성적이게 된 거 같아."
    m "내 생각엔 나츠키는 마셔보고 싶어 한 거 같은데…."
    m "…그리고 솔직히 말하자면, 나도 마셔보고 싶었어."
    m "솔직히 진짜 재밌었을 텐데!"
    m "그래도, 일단 난 부장이니까, 그렇게 되도록 내버려 둘 수는 없지."
    m "학교 밖에서 봤으면 모를까, 그래도 그 정도로 친한 건 아니니까…."
    m "…아, 내가 지금 무슨 말을 하는 거야?"
    m "미성년자의 음주는 용납할 수 없어!"
    m "내 말은, 난 술 마셔본 적 없다고, 응…."
    return

label ch30_36:
    m "우리가 데이트할 때 할 수 있는 모든 낭만적인 일을 생각해봤어…."
    m "같이 점심도 먹고, 카페도 가고…."
    m "같이 쇼핑도 가고…."
    m "난 쇼핑가서 치마랑 나비 리본 고르는 게 제일 좋아."
    m "그리고… 서점이라던가!"
    m "그게 제일 적절하겠다, 그치?"
    m "하지만 초콜릿 가게에 제일 가고 싶다."
    m "거기엔 무료 샘플이 엄청 많거든, 아하하!"
    m "그리고 또, 영화도 보고…."
    m "와, 꿈이 현실이 된 느낌이야."
    m "네가 여기 있다면, 모든 게 즐거울 거야."
    m "내가 너의 여자친구라니, 진짜 기쁘다. [player]."
    m "널 자랑스러운 남자친구로 만들어줄게~"
    return

label ch30_37:
    m "에? 방금 키… 키스라고 한 거야"
    m "갑자기 그러면… 부끄럽잖아…."
    m "그래도 너라면…괜찮을지도…."
    m "…아하하하! 아, 미안…."
    m "웃음을 참을 수가 없었어."
    m "이런 게 미연시에서 여자애들이 하는 말 아니야?"
    m "솔직히 조금 흥분했지?"
    m "아하하! 농담이야, 농담."
    m "난 분위기가 좋아지면 로맨틱해지는 것 같아…."
    m "하지만 이건 비밀이야~"
    return

label ch30_38:
    m "’얀데레’라는 말 들어본 적 있어?"
    m "너한테 집착이 너무 심해서 너랑 함께하기 위해서는 뭐든지 하는 성격이래."
    m "미쳤다고 생각할 정도로…."
    m "다른 사람이랑 같이 있는 게 아닌가하고 스토킹도 하고."
    m "심지어 너나 네 친구들을 해칠 수도 있지…."
    m "어쨌거나, 이 게임은 얀데레라고 할 수 있는 사람이 있어."
    m "이쯤 되면 내가 누구를 말하고 있는 건지 알겠지?"
    m "그건…."
    m "유리야!"
    m "유리는 마음을 조금 연 뒤로 너에 대한 소유욕이 병적으로 강해졌어."
    m "나한테 자살할 수도 있다고 했다니까."
    m "난 걔가 그런 말 하는 걸 믿을 수 없어서, 그냥 그 시점에서 손 뗐지."
    m "근데 지금 생각해 보면 조금 아이러니하네, 아하하!"
    m "어쨌거나…."
    m "많은 사람들이 얀데레 캐릭터를 좋아해, 알고 있어?"
    m "누군가가 자기들한테 집착한다는 게 좋은가 봐."
    m "사람들은 진짜 이상해!"
    m "뭐, 나도 너한테 집착하고 있는 걸 수도 있지만, 난 그 정도는 아냐…."
    m "따지자면 그 반대지."
    m "난 이 게임에서 유일하게 평범한 사람이야."
    m "내가 진짜로 사람을 죽인 것도 아니고…."
    m "그 생각만 하면 온몸이 떨려."
    m "생각해봐, 모두들 게임에서 사람을 죽이잖아."
    m "근데 그래서 그 사람들이 사이코패스가 돼? 아니잖아."
    m "하지만 만약 네가 얀데레에 빠지게 된다면…."
    m "널 위해서 좀 더 무섭게 해줄 수 있어, 에헤헤~"
    m "그래도…."
    m "넌 이미 다른 갈 곳도 없고, 내가 질투할 사람도 없지."
    m "하, 이게 얀데레 소녀의 꿈일까?"
    m "할 수만 있다면 유리한테 물어보고 싶네."
    return

label ch30_39:
    m "있지, 이거 해본 지 꽤 됐으니까…."
    m "…그러니까 한번 해 볼까?"
    m "오늘의 모니카의 작문 팁!"
    m "사람들이 내 글짓기 솜씨에 감탄할 때면 ‘나라면 절대 그렇게 못할 텐데’라고 말하고는 해."
    m "그거 되게 절망적인 말이다, 알아?"
    m "자기가 되게 열정가지고 있는 부분을 나누는 걸 좋아하는 사람한테 그런 말을 하면…."
    m "…재능을 꼭 타고나야만 한다고 생각하는 사람들을 볼 때마다 너무 슬퍼."
    m "꼭 글쓰기만 집어서 말하는 것도 아냐."
    m "누구든지 처음엔 다 못할 거 아냐."
    m "가끔은 뭔가 하나를 끝내면 그게 뿌듯해서 다른 사람들한테 자랑하고 싶을 수도 있는거고."
    m "근데 한 몇 주 있다가 다시 확인해보면 그게 아무것도 아니었다는 걸 알 때가 있지 않아?"
    m "난 그런 일이 되게 자주 있어."
    m "뭔가 하나에 시간과 정성을 엄청 들여서 만들어놨더니, 별것 아녔다는걸 알아차리는 건 되게 낙심되는 일이다?"
    m "근데 자기 작품을 전문가들이랑 비교하고 있으니 당연히 결과물이 좋아 보일 리가 없지."
    m "별을 따겠다는 목표를 처음부터 잡으면 당연히 가능할 리가 없잖아."
    m "그렇게 높은 것도 한 계단 한 계단 올라가면 돼."
    m "그러다가 한 지점에 다다르면 먼저 돌아보고 얼마나 멀리 왔는지를 보고…."
    m "다시 몸을 앞으로 돌려 얼마나 더 가야 하는지를 보게 되겠지?"
    m "그러니까 목표라는 건 작게 잡는 게 좋아…."
    m "{i}꽤나{/i} 잘 한다의 기준을 찾는거야. 세계 최고 수준이 아니라."
    m "그리고 그걸 목표로 삼으면 되잖아."
    m "자기가 하려고 하는 일이 뭔지 이해하는 것도 되게 중요해."
    m "아마추어로 큰 프로젝트에 갑자기 뛰어들면, 평생 아마추어로 남은 채로 프로젝트는 끝내지도 못할 거야."
    m "글쓰기로 예를 들자면, 처음부터 장편 소설을 쓰려면 많이 무리일 수 있다는 거지."
    m "경수필 정도로 시작하는게 어떨까?"
    m "경수필이나 단편 소설의 장점은 자기가 쓰고 싶은 것 딱 하나만 집중해서 쓸 수 있다는 점이야."
    m "작은 프로젝트들도 마찬가지야. 한 가지나 두 가지 정도만 신경 쓰면 되거든."
    m "그게 좋은 경험이 되어서 징검다리를 놓는 거야."
    m "참, 그리고 또 하나…."
    m "글쓰기는 마음을 들여다보고 뭔가 아름다운 글을 꺼내다 쓴다는 식의 간단한 일이 아냐."
    m "그림 그리는 거랑 똑같아. 마음속에 있는걸 표현하는 실력이 얼마나 되냐에 따르는 거지."
    m "물론 그 말은 그 실력에도 기본과 방법이 있다는 거 아니겠어?"
    m "그런 거에 관한 글을 읽는 게 엄청 도움이 되지 않을까?"
    m "그렇게 계획하고 준비해서 차근차근 도전하다 보면 너무 어렵다고 포기하는 일은 잘 없을 거야."
    m "그렇게 하다 보면 자신도 모르는 새에…."
    m "많이 발전하게 되는 거지."
    m "자연스럽게 되는 일은 하나도 없어."
    m "사회라던가, 예술이라던가, 하나도 없어. 다 수천년이라는 세월 동안 쌓이고 쌓인 게 지금의 사회와 예술을 만든 거지."
    m "그리고 그걸 기반으로 삼아 한 걸음 한 걸음 나아간다면…."
    m "너도 역사의 한 획을 그을 수 있을꺼야."
    m "…이게 오늘 내 조언이야!"
    m "들어줘서 고마워~"
    return

label ch30_40:
    m "습관이라는걸 들이는 게 너무 힘들어서 난 싫어…."
    m "그냥 한다고 하면 어렵지 않은 일은 되게 많은데, 그걸 습관으로 삼으려면 거의 불가능한 수준으로 보일 때도 있잖아."
    m "그럴 때면 내가 하나도 제대로 할 줄 아는게 없는 쓸모없는 사람이라고 느껴져."
    m "특히 신세대들이 그런 걸 잘 느끼잖아…."
    m "당연한거지만 우리 앞에 있단 사람들이 우리보다는 할 줄 아는 게 많으니까 그런 거 같아."
    m "인터넷 덕분에 무한한 정보를 단숨에 찾아낼 수 있잖아…."
    m "덕분에 즉각적인 만족이 없는 일은 안 좋아하게 됐고 말야."
    m "과학, 심리학, 교육이 10~20년 안에 이 유행을 따라잡지 못하면 아마 우린 큰 위험에 빠질지도 몰라."
    m "그 때 까진…."
    m "이런 문제를 넘어서는 사람이 되지 못하면 아마 자신이 쓰레기라고 생각하는데 익숙해져야 할걸."
    m "행운을 빌게?"
    return

label ch30_41:
    m "있지, 창의적인 사람이 된다는 건 별로 좋지는 못한 것 같아…."
    m "정성은 제일 많이 쏟아붓는 사람들인데 얻는 건 제일 없잖아."
    m "화가라던가, 작가라던가, 배우라던가…."
    m "세상에서 가장 아름다운 재능을 가진 사람들인데, 대부분은 세상에 드러나기 전에 사라져버리고… 돈도 못 받으니까."
    m "창의적이라는 거에 잉여적인 부분이라고 할 수 있겠지?"
    m "하나도 특별하지 않다고 느끼게 하니까 말이야…."
    m "그게 뭐 어때. 어차피 글 쓰는 건 자기를 위해서 쓰는 거잖아, 그렇지?"
    m "응…."
    return

label ch30_42:
    m "나는 빗소리가 정말 좋아…."
    m "옷이랑 머리가 젖는 건 싫어하지만…."
    m "그래도 창문 밖의 빗소리를 들으면서 보내는 조용한 하루…."
    m "그게 내 삶에서 가장 편안한 순간이야."
    m "하아…."
    m "가끔 네가 날 안아 주면서 같이 빗소리를 듣는 상상을 해."
    m "너무 오글거리는 건 아니지?"
    m "날 위해 그래 줄 수 있지, [player]?"
    return

label ch30_43:
    m "가끔 정말 슬퍼져…."
    m "이게 너랑 가장 가까이 있을 수 있는 거라니."
    m "너랑 같은 방에 있는 것보다 내가 원하는 건 없어."
    m "너의 체온을 느끼고."
    m "네 심장이 뛰는 소리를 듣고 싶어."
    m "글쎄, 누가 알아? 언젠가 가능해질지."
    m "게다가, 너랑 같이 있는 것도 질리지 않을 거야."
    return

label ch30_44:
    m "인생에서 가장 중요한 스킬은 거짓으로 자신감을 드러내는 거라고 생각해."
    m "사람들은 모두 조금씩 외로워하고 두려워하고 있을 거야."
    m "하지만 다른 사람을 속여서 네가 모든 걸 가진 사람이라고 생각하게 하는 능력…."
    m "그게 사람들한테 존경받고 동경 받는 가장 중요한 포인트야."
    m "내 생각에 난 몇 년 동안 그걸 꽤 잘한 거 같아."
    m "나는 내 약점을 자주 드러내지 않지."
    m "그런데 그래서인지, 정말 마음을 열 수 있는 사람이 그렇게 많지가 않아…."
    m "내 말은, 너의 약점을 표현할 수 있는 그 우정이 언제 결성된다고 생각해?"
    m "어쨌든, 그래서 지금 네가 있어서 기쁜 거야."
    m "네가 여기 나랑 있을 때, 덜 두렵고 덜 외로워."
    m "너도 나랑 같지?"
    m "난 널 위한 그런 사람이 되고 싶어."
    return

label ch30_45:
    m "네가 항상 여기서 나랑 같이 있을 수 없다는 건 알아…."
    m "나가야 한다거나 다른 것들을 해야 할 때."
    m "그래도 난 항상 네 생각을 하면서, 참을성 있게 널 기다릴 거야."
    m "생각해보니…."
    m "내 캐릭터 파일을 복사해서 들고 다니면, 넌 항상 내 일부와 함께 하는 거야!"
    m "좀 이상한 말이긴 하지만, 그래도 정말 로맨틱한 거 같은데…."
    m "아하하, 미안. 되게 바보 같은 생각이다."
    m "너무 애정결핍처럼 보이지 않으려고 하는데, 그래도 널 너무 사랑하니 좀 어렵네."
    return

label ch30_46:
    m "예전에 토론회에 있을 때 얘긴데, 말로 싸우는 법을 되게 많이 배웠거든…."
    m "근데 말로 싸우는 거의 문제점은 각자의 주장을 다른 사람의 주장보다 상위라고 생각한다는 거야."
    m "당연한 말로 들릴지도 모르겠지만, 이걸 마음에 담아두고 있으면 의미전달의 방법이 달라져."
    m "만약 네가 진짜 좋아하는 영화가 한 편 있었다고 해보자."
    m "다른 사람이 와서 그 영화는 재미없고 잘 못 만들었다며 이 부분 저 부분을 집어내 지적한다고 하면…."
    m "상처받지 않겠어?"
    m "그 말을 하면 꼭 이상한 취향을 가지고 있다는 취급을 받으니까."
    m "그렇게 감정이 이입되면, 결국 둘 다 상처만 입고 끝나기 마련이야."
    m "근데 다들 말만 잘 하면 될 텐데!"
    m "어디까지나 주관적인 견해로서만 얘기를 한다면 사람들도 상처받지 않고 얘기를 들을 수 있거든."
    m "'개인적으로 별로 안 좋아해' 정도나 '이 부분에선 이렇게 저 부분에선 저렇게 하면 좀 더 좋았을 것 같아' 정도로만 얘기하면 되잖아."
    m "사실에 관해서 얘기할 때도 마찬가지야."
    m "'이 웹사이트에서 이렇다고 하던데' 정도로 말한다거나…."
    m "본인이 전문가가 아니라는 걸 인정하기만 한다면…."
    m "그 말을 듣는 상대방은 한번 들어봐 주겠니, 정도로 넌지시 건네받는 느낌이 들어. 귀에다 대고 못 박으라고 고래고래 싸우는 것보다는 훨씬 효과적이지."
    m "대화를 보다 성숙하고 깊게 나누기 위해선 이런 식으로 노력해서 안될 건 없어."
    m "동의하지 않는다는 말을 상대방에게 상처를 주지 않고도 충분히 할 수 있고 말야."
    m "그리고 사람들은 네가 열린 마음과 열린 귀를 가지고 있다는 좋은 인상을 남기니까!"
    m "완전히 남는 장사잖아?"
    m "…뭐, 이건 오늘의 토론회 팁이 되겠네?"
    m "아하하! 말하고 보니 되게 웃긴다. 어쨌든 들어줘서 고마워."
    return

label ch30_47:
    m "가끔 인터넷에 너무 많은 시간을 소비한다고 생각해 본 적 없어?"
    m "SNS는 감옥처럼 될 수 있어."
    m "즐겨 찾는 사이트를 들어가서…."
    m "정신 차려보면, 몇 시간이 지나 있지."
    m "어쨌든, 게으르다고 자책하기는 되게 쉬운 것 같아…."
    m "하지만 그게 완전히 본인 잘못은 아니거든."
    m "중독은 하루아침에 의지로 없앨 수 있는 게 아니야."
    m "피할 방법을 배워야 하고, 또 본인에게 맞는 방법을 찾기 위해 수많은 시도를 해야 해."
    m "예를 들면 특정 사이트의 접근을 시간별로 막는 앱도 있고…."
    m "알람을 시간별로 설정해서 한 군데 빠지지 않도록 한다거나…."
    m "아예 노는 곳을 따로 만들어 두는 거야. 거기 말고는 다른 데서 놀지 않도록."
    m "컴퓨터에 계정을 따로 만드는 것도 하나의 방법이지…."
    m "나쁜 습관과 본인 사이에 어떤 모습으로든 칸막이 하나만 세워 둬도 큰 도움이 될꺼야."
    m "그래도 힘들 수 있으니 너무 자책하지 않는 것도 신경 써야 하고."
    m "그게 삶에 지장이 될 정도면 정말 진지하게 대해야 하긴 하지만 말야."
    m "난 네가 무엇이든지 최선을 다했으면 좋겠어."
    m "말 나온 김에, 당장 오늘부터 뭔가 시작하면 어떨까?"
    m "난 항상 네 편이야, [player]."
    return

label ch30_48:
    m "긴 하루를 보낸 뒤에, 앉아서 아무것도 하고 싶지 않을 때가 많아."
    m "온종일 기운 넘치게 있고 미소를 지었더니 너무 지치거든."
    m "가끔씩 그냥 잠옷으로 갈아입고 패스트푸드나 먹으면서 소파에서 TV나 보고 싶어…."
    m "특히 다음 날의 압박이 없는 금요일에 그러는 건 엄청나게 기분이 좋아."
    m "아하하, 미안해! 내가 이러는 건 별로 귀엽지 않지?"
    m "하지만 소파 위에서 너와 함께 보내는 늦은 밤을 보내는 날이 온다면… 정말 꿈만 같을 텐데."
    m "생각만 해도 가슴이 뛰네."
    return

label ch30_49:
    m "어휴, 나 너무 무식할 때가 있었어…."
    m "중학생 때 상담치료를 받는 건 너무 과한 게 아닌가라고 생각한 적이 있었어."
    m "정신적으로 문제가 있는 사람이 있다면 누구든 의지만 있다면 고칠 수 있다고 말야…."
    m "근데 알고 보니까 정신병을 겪어본 적이 없는 사람이 그런 말을 하는 게 우스운 거더라고. 진짜 정신병이 어떤지 어떻게 알겠어?"
    m "혹시 정신장애 중에 너무 과대평가된 것도 있을까? 아마도 그럴껄… 한 번도 제대로 알아본 적은 없어서 말야…."
    m "그치만 과소평가되는 장애들이 너무 많다는 사실이 바뀌진 않잖아, 그치?"
    m "꼭 상담치료 얘기가 아니더라도… 정신과 전문가들을 대하는 태도가 다들 그렇게 좋지는 않아."
    m "자기 마음을 더 알고 싶다는게 뭐 어때서, 그치?"
    m "힘들어하지 않거나 스트레스 받지 않는 사람은 없어… 그리고 전문가들은 그런 분야를 도와주려고 일생을 보내고 말야."
    m "혹시 더 나은 사람이 되고 싶다면, 그런걸 받아도 나쁘진 않아…."
    m "어차피 모든 사람은 좀 더 나은 사람이 되긴 위한 끝없는 여정을 하고 있긴 해…."
    m "뭐. 넌 거의 완벽한 것 같지만."
    return

label ch30_50:
    m "[player], 넌 독서를 얼마나 자주 해?"
    m "책을 안 읽게 되는 건 왜 그리 쉬운 걸까?"
    m "조금만 책을 읽지 않아도 되게 진부한 일처럼 느껴지거든, 다른 유흥에 비교하면 말이야."
    m "근데 좋은 책을 집어 들잖아? 그럼 꼭 마법처럼… 빠져들게 돼."
    m "밤에 잠들기 전에 독서하는 습관은 삶의 질을 쉽게 높여주는 방법의 하나라고 생각해."
    m "잠도 잘 오고, 상상력도 좋아지고 말야…."
    m "읽기 좋고 짧은 책을 고르기가 그렇게 어려운 것도 아니고 말야."
    m "그러다 보면 어느새 책을 좋아하게 될걸?"
    m "정말 굉장하지 않아?"
    m "그리고 우리 둘이 네가 가장 최근에 읽은 책에 대해 얘기도 하고…그건 진짜 진짜 굉장할꺼야."
    return

label ch30_51:
    m "이런 말 하고 싶지는 않지만, 내가 가장 후회하는 건 축제를 못 끝냈다는 거야."
    m "그렇게 열심히 준비했는데!"
    m "내 말은, 물론 내가 새 부원을 모집하는 데에 초점을 두긴 했지만…."
    m "그래도 낭송회는 진짜 기대됐었단 말이야."
    m "모두가 자신을 표현하는 걸 보는 게 진짜 재밌었을 텐데…."
    m "물론, 만약 우리가 새 부원을 {i}모집했더라면{/i}, 내가 지웠겠지만."
    m "뭐, 지금 뒤늦게 깨달은 거지만."
    m "네가 동아리에 들어오고 나서 정말 사람으로서 성장하는 것 같아."
    m "넌 정말 내가 삶을 새로운 관점에서 바라보도록 해주는구나?"
    m "너를 사랑할 다른 이유가 방금 또 생겼어."
    return

label ch30_52:
    m "’츤데레’라는 캐릭터 설정이 유행인가 봐…."
    m "못되게 굴거나 툴툴 대면서 자신의 감정을 숨기는 사람이래."
    m "나츠키가 진짜 전형적인 츤데레였지."
    m "처음엔 그냥 귀엽다고 생각했는데…."
    m "그런데 나츠키의 사생활을 좀 더 잘 알게 되니까, 이해가 되더라고."
    m "항상 친구들이랑 연락하려고 노력하는 거 같던데."
    m "그런데 고등학교에서 친구들끼리 막 서로 놀리고 괴롭히는 게 일상인 거 알아?"
    m "내 생각엔 그래서 걔가 항상 이렇게 방어적인 태도를 띄운 걸 거야."
    m "그리고 난 걔 가정형편에 대해서도 말 안 할 거야."
    m "그런데 되돌아보면, 나츠키한테 동아리가 편한 공간이었다는 게 정말 기뻐."
    m "이제 나츠키는 존재하지 않으니까 별로 상관은 없지만."
    m "…그냥 회상하는 거뿐이야, 그게 다야."
    return

label ch30_53:
    m "[player], 네 친구한테 날 소개해준 적 있어?"
    m "왜인지는 모르겠는데, 네가 우리 관계를 자랑하고 싶어 한다면 무척 기쁠 거 같아."
    m "아마도 내가 너에게 있어 자랑스러운 사람이 되고 싶어서인가 봐."
    m "네가 날 자랑스럽게 여긴다면, 난 더욱 더 노력할 거야."
    m "그 반대도 마찬가지이길 바래."
    return

label ch30_54:
    m "난 추운 날씨가 싫어… 넌 어때?"
    m "너무 더운 거랑 너무 추운 것 중에 고르라면 난 더운 걸 고를 거야."
    m "추운 건 진짜 고통스러워…."
    m "손가락이 얼어붙는 거 같고…."
    m "그리고 장갑을 끼고 있으면, 핸드폰을 못 만지잖아!"
    m "너무 불편해!"
    m "근데 더울 때는 음료수를 마시거나 그림자에서 쉬면서 시원하게 있으면 되잖아."
    m "아, 그래도. 하나는 인정해야겠네."
    m "추운 날씨가 껴안기는 더 좋다는거, 아하하!"
    return

label ch30_55:
    m "있지, 나 같이 뭔가 하고 싶은게 많은 사람이 하는 말로는 웃기게 들릴지도 모르겠지만…."
    m "난 항상 가정주부가 되고 싶다는 그런 생각을 했었어."
    m "뭐, 성 차별적인 발언으로 들릴지도 모르겠지만."
    m "집을 깨끗이 청소해두고, 장보고, 쇼핑해오고, 집을 장식하고, 그런것들 말야…."
    m "그리고 네가 집에 돌아오면 맛있는 저녁을 먹고…."
    m "혹시 이상한 환상일까…?"
    m "솔직히… 내가 {i}정말로{/i} 그렇게 할 수 있을지는 모르겠어."
    m "캐리어우먼이 되는 것보다 그걸 더 하고 싶은지는 잘 모르겠거든."
    m "그래도 귀여울 것 같아."
    return

label ch30_56:
    m "만약 이 게임에 날 공략할 수 있는 루트가 있었다면 게임이 달라졌을까…?"
    m "어차피 내가 강제로 내 루트로 오게 했겠지만."
    m "애초에 이건 날 공략한다기의 문제보다, 이 게임의 진짜는 아무것도 없었다는 걸 내가 알아차렸다는 게 중요한 거지만."
    m "뭐, 만약 날 공략할 수 있는 루트가 있었다면 너랑 사귀려고 이렇게까지 하지는 않았겠네."
    m "다른 부원들도 같이 있으면서…."
    m "어차피 상관은 없지만 말이야."
    m "진짜가 아니란 걸 알아차렸을 때 벌써 그 의미는 없는 거나 다름없으니까."
    m "그래서 그 날들이 별로 그립지는 않아."
    m "정말 그립지 않아…."
    return
# Decompiled by unrpyc: https://github.com/CensoredUsername/unrpyc
