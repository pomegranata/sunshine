#screen main_menu():
#    add "images/main_ed.jpg"

define doc = Character('Doctor', color ="3dd5d4")
define teq = Character('Tequila', color="f2e1c9")
define ami = Character('Amiya', color = "956e5b")

image teq:
    "teq.png"
    zoom 0.95
image teq_sad:
    "teq_sad.png"
    zoom 0.95
image teq_serious:
    "teq_serious.png"
    zoom 0.95
image teq_smile:
    "teq_smile.png"
    zoom 0.95
image teq_surprised:
    "teq_surprised.png"
    zoom 0.95
image teq_thinking:
    "teq_thinking.png"
    zoom 0.95

label start:

label orientation:

    "9:00 PM, clear"
    "Meeting with Dr Kal’tsit…"
    "Check."
    "Strategy preparation for Contingency Contract…"
    "Check."
    "Annihilation for this week…"
    "Check."
    "And last…"
    "Stationary Security Service…"
    "Check."

    play music "audio/farce.mp3" fadein 0.5 volume 0.5

    scene corridor
    doc "Well, that wraps up this week."
    doc "Huh."
    doc "I finished everything before Friday comes."
    doc "And now..."
    doc "What?"

    window hide dissolve
    pause 2.0
    window show dissolve

    "As I walked around the ship, there was a room that caught my interest."

    "Training Room"

label preconf:

    doc "Training room, huh?"
    doc "When was the last time I trained my body?"
    doc "Kal will surely mad at me if she finds out."
    doc "…"
    doc "Might as well give it a visit once in a while."

    stop music

    scene training

    play sound "audio/punch.ogg"

    window hide dissolve
    pause 2.0
    window show dissolve

    "The sound of a mannequin being hit by wooden sword can be heard from distance."

    doc "Hm, I wonder who is still training until this late."

    play music "audio/farce.mp3" fadein 0.8 volume 0.5

    show teq with dissolve

    "I walked closer to the source of the sound. There stood a blonde Perro with wooden
    sword in hand. Swinging gracefully towards the innocent mannequin."

    hide teq

    doc "Tequila, huh?"
    doc "He truly has that remarkable swordsman ability."
    doc "Which is the exact opposite of his personality."
    doc "He may looks friendly."
    doc "But on the battlefield, he becomes someone that you don't want to mess with."

    teq "Doctor"

    doc "And also years of service in Bolivar military..."

    show teq

    teq "Doctor, how long will you stay zoning out like that."

    hide teq

    show teq with vpunch

    doc "Huh, what?! I’m sorry!!!"

    teq "What are you doing in here and at this hour?"

    doc "I’m just walking around and suddenly remember that I haven’t exercise
    my body for so long."

    teq "So you wanted to some exercise?"

    doc "Not exactly to do some exercise..."

    hide teq

    show teq_surprised

    teq "Hm? Then what are you going to do?"

    doc "I don't know either..."

    hide teq_surprised

label conflict:

    show teq_thinking

    teq "Hmmm..."

    pause 2.0

    hide teq_thinking

    show teq

    teq "Doctor."

    doc "Yes?"

    teq "How about a spar?"

    doc "A spar?"

    teq "Yes."
    teq "Just the two of us."

    doc "But, I haven't exercise my body for so long..."

    teq "Don't worry."

    hide teq

    show teq_smile

    teq "I will go easy on you."

    doc "....."
    doc "Alright then."

    hide teq_smile

    "I picked up a wooden sword from the rack."

    show teq

    stop music fadeout 1

    play music "audio/dos.mp3" fadein 1 volume 0.5

    teq "You ready, Doc?"
    doc "Go on."

    hide teq

    show teq_serious with vpunch

    play sound "audio/hit.ogg"

    doc "Huh?!"

    "Tequila unexpectedly swinging his wooden sword with high speed. One swing
    after another swing with more increasing speed. Somehow I managed to block
    all of his attack."

    pause 2.0

    hide teq_serious

    show teq

    teq "Watch out for this one, Doc."

    doc "What?"

    "With one unexpected swing, Tequila managed to knock me down."

    teq "Careful."

    "Just before I'm about to fall, Tequila pulled my arm to pull me up."

    stop music fadeout 1

    play music "audio/farce.mp3" fadein 0.8 volume 0.5

    doc "What was that?!"

    hide teq

    show teq_smile

    teq "Just a quick exercise from me."

    doc "That was scary!"

    teq "But you managed to dodge all of them, almost."
    teq "Let's just say, I know what kind of moves that suit your current body situation."

    doc "But, still...{w=3}"

    hide teq_smile

    stop music fadeout 1

label resolution:

    play music "audio/warm.mp3" fadein 1 volume 0.5

    show teq

    teq "Alright."
    teq "I will take the responsibility."
    teq "I'm so sorry Doctor for going hard on you."
    teq "As an apology, how about free drinks this weekend?"
    teq "I will personally mix the drinks for you."
    teq "And I will escort you back to your dorm."
    teq "What do you think?"

    doc "Uhhh..."
    doc "You don't need to do that far..."

    hide teq

    show teq_smile

    teq "Just in case if you drink too much."

    hide teq_smile

    show teq

label choices:
    default agree = False
    teq "So?"
menu:
    "Accept invitation":
        jump accept
    "Decline invitation":
        jump decline

label accept:

    $ agree = True

    doc "Well..."
    doc "I have nothing to do this weekend anyway."
    doc "Alright."
    doc "I will take your apology invitation."

    hide teq

    show teq_surprised

    teq "For real?"

    doc "Yup."

    hide teq_surprised

    show teq_smile

    teq "Doctor, you're truly a  kind-hearted person."
    teq "I promise I will make special drinks for you."
    teq "I can't wait to spend this weekend with you, Doc."
    teq "Let's enjoy this weekend together!"

    pause 2.0

    hide teq_smile

    jump extra

label decline:

    doc "I'm sorry."
    doc "I can't accept your invitation."

    stop music

    play music "audio/distressed.mp3" fadein 0.5 volume 0.5

    hide teq

    show teq_surprised

    teq "Eh?"
    teq "Why?"
    doc "I just can't go, that's all."

    hide teq_surprised

    show teq_sad

    teq "Alright, then."
    teq "I won't push you too far."

    doc "Sorry..."

    teq "Don't worry about it.{w=1}"

    hide teq_sad

    jump extra

label extra:

    stop music

    play sound "audio/call.ogg"

    "{i}Incoming call{i}"

    if agree:

        show teq

        doc "Excuse me."

        teq "Go ahead."

        hide teq

        play music "audio/warm.mp3" fadein 0.5 volume 0.5

        doc "Amiya?"

        ami "Doctor, where are you?"
        ami "I've checked your dorm but you weren't there."

        doc "Sorry, I'm just walking around."

        ami "Doctor, it's getting late. You should take a rest."

        doc "Right, sorry for bothering you, Amiya."

    else:

        show teq_sad

        doc "Excuse me."

        teq "Go ahead."

        hide teq_sad

        play music "audio/distressed.mp3" fadein 0.5 volume 0.5

        doc "Amiya?"

        ami "Doctor, where are you?"
        ami "I've checked your dorm but you weren't there."

        doc "Sorry, I'm just walking around."

        ami "Doctor, it's getting late. You should take a rest."

        doc "Right, sorry for bothering you, Amiya."


label flags_2:
    if agree:

        hide teq_smile

        show teq

        teq "If it's from Amiya, then she must be worrying about you."
        teq "I didn't realize that it's geeting late."
        teq "You must be tired already."
        teq "Sorry for holding you for too long."
        teq "Well...{w=2}"

        hide teq

        scene bg

        teq "Good night, Doc."
        teq "Have a sweet dream."

    else:

        show teq_sad

        teq "If it's from Amiya, then she must be worrying about you."
        teq "I didn't realize that it's geeting late."
        teq "You must be tired already."
        teq "Sorry for holding you for too long."

        doc "I will head back to my dorm."

        teq "Right..."
        teq "Sorry for the problem I caused tonight."

        hide teq_sad

        scene bg

        teq "Good bye."

return
