define f = Character("Fred")
define g = Character("Gary")
define n = Character("Narrator")

default correct = 0
default repaired = False
default choice_1_done = False
default choice_2_done = False
default choice_3_done = False
default choice_repair_done = False
default choice_4_done = False
default choice_5_done = False
default choice_6_done = False

label start:

    scene bg_cafeteria with fade

    n "It's a Thursday evening at the SUTD canteen."
    n "The dinner rush has long thinned out, most people have retreated to their rooms, their deadlines, their screens."
    n "The overhead lights cast everything in a warm, slightly tired glow."
    n "Somewhere nearby, a ceiling fan hums at a speed that doesn't quite cool anything."
    
    # show gary_neutral at left with moveinleft

    n "You are Gary. Term 5 EPD student."
    n "You've been meaning to catch up with Fred for weeks, tonight was the first window either of you could find."
    n "You grab your mixed rice, half a sugarcane juice and spot Fred already at the corner table."
    n "You weave past a few lingering students and slide into the seat across from him."

    # show fred_distant at right with moveinright
    # hide gary_neutral with dissolve

    n "He doesn't look up when you sit down."
    n "You arrange your tray. Unwrap your cutlery. Take a slow sip of your drink. Still nothing from him."
    n "You've known Fred since Term 1."
    n "You've pulled all-nighters together, complained about the same professors, split delivery fees more times than you can count."
    n "This quietness is not like him at all."

    # show gary_neutral at left with moveinleft

    g "Hey. Didn't see you in the library today."

    # hide fred_distant
    # show fred_faintsmile at right

    f "Yeah... sorry. I've just been... I don't know. Out of it lately."
    n "He looks back down at his plate. The food is barely touched."
    n "You watch him push a piece of tofu to the side and leave it there."
    n "His phone buzzes on the table. Once, twice. He doesn't even glance at it. Fred checks his phone the way most people breathe, automatically, constantly."
    n "The fact that he's ignoring it now tells you more than anything he's said."
    n "Something is off. Not in an obvious, dramatic way, more like the quiet wrongness of a room where a window has been left open in the rain. You can't see it, but you feel the draft."

    # show gary_concerned...

    g "Hey. You okay? You don't really seem like yourself."
    n "It's a simple question. Maybe even an obvious one. But you mean it and somehow that makes it land differently than small talk would."

    # show fred_tired...

    f "I'm just really tired, Gary."
    n "He says it quietly. Flatly. Like the words have been sitting at the back of his throat all day and finally found their way out."
    n "Another pause. Longer this time. He opens his mouth, closes it again. Like he's weighing something. Deciding whether to put it down or keep carrying it."
    f "...like, actually tired. Not just 'I need sleep' tired. More like, I don't even know where to start."
    f "I almost didn't come tonight, honestly. I kept thinking you'd just tell me to talk to them or something, and I'd feel worse."
    n "He says it quickly, like he's bracing for you to do exactly that."
    n "There it is. The edge of something much bigger."
    n "There's a beat of silence. Fred is halfway through a door that took something to open. The question is whether you walk through it with him, or pull it the rest of the way because you can't stand the waiting."

label choice_1:

    menu:
        "What do you say?"

        "Take your time. I'm not going anywhere.":
            if not choice_1_done:
                $ choice_1_done = True
                $ correct += 1
                n "You lean back. Relaxed. No pressure."
            jump choice_1a

        "What happened? Just tell me.":
            if not choice_1_done:
                $ choice_1_done = True
                n "You lean forward. Eager to get to the problem."
            jump choice_1b

label choice_1a:

    n "Fred looks at you for a moment. Like he's checking whether you mean it."
    n "Apparently you do."
    n "Something in his shoulders shifts, barely perceptible, like a door that was held closed by one finger and the finger just let go."

    # show fred_neutral...

    f "...It's the group project. Well, my group, specifically."
    n "He says it like he's been holding those words in his chest for days. Maybe longer."
    jump merge_point1

label choice_1b:

    n "Fred blinks. Something in him pulls back slightly, like a hand that reached out and found the air a little too cold."
    n "This is exactly what he said he was afraid of. You don't realise it yet. But he does."
    
    # show fred_distant...

    f "It's... okay, yeah. It's just group project stuff."
    n "He gives you the surface version. The polished, nothing-to-worry-about version. You can't quite put your finger on it, but you get the sense you moved too fast."
    jump merge_point1

label merge_point1:

    n "You don't say anything yet. Just wait."
    f "You know how it is with group projects here, right? Everyone's always swamped, everyone's got their own stuff going on..."
    n "He stops. Rubs the back of his neck."

    # show fred_sad...

    f "My teammates just... aren't doing anything. Like, at all."
    f "I've been the one handling everything. The research, the slides, the writeup, the coordination, chasing everyone down."
    f "All of it. By myself."
    n "The words come out flat. Not dramatic. Just tired. Like he's past the point of frustration and arrived somewhere much quieter and worse."
    f "And the submission is in four days."

    # show gary_thinking...

    n "Four days. You feel that in your gut. You know exactly what that countdown feels like, the specific dread of a deadline sprinting toward you while the work barely moves."
    n "He's not exaggerating. You can see it on him, the dark circles, the way he's sitting like his body is already bracing for impact. Like he's been in survival mode for a while now and simply forgot to stop."
    f "Have they said anything? Like... do they even know how much you've been carrying?"

    # show fred_sad

    f "They know. I've messaged them multiple times. They either leave me on read or say 'yeah I'll get to it' and then just... don't."
    n "He looks out toward the canteen entrance for a moment. Not at anything in particular. Just away."
    n "There's a fork in the road here, and you can feel it. One direction leads deeper into what Fred is going through. The other leads to a solution, clean, fast, and completely beside the point."

label choice_2:

    menu:
        "What do you say?"

        "Have you tried going to your prof about it?":
            if not choice_2_done:
                $ choice_2_done = True
                n "Practical. Reasonable. The kind of thing someone says when they want to be helpful without having to sit in the mess."
            jump choice_2a

        "How long has it been like that?":
            if not choice_2_done:
                $ correct += 1
                n "An open question. You want to understand the shape of the thing before you touch it."
            jump choice_2b

label choice_2a:

    n "It's the kind of question that sounds like caring but functions as escaping."
    n "'Have you tried...' is never really a question. It's a suggestion wearing a question mark. And Fred can tell."

    # show fred_distant...

    f "Yeah, I've thought about it."
    n "He doesn't elaborate. The conversation narrows, like a corridor that was wide a moment ago and now has walls on both sides."
    n "The subtext is clear even if he doesn't say it: 'I know that option exists. I've already thought about every option. That's not what I need from you right now.'"
    n "But he won't say that, because saying it would require more energy than he has. So he just goes quiet, and the moment passes."
    jump merge_point2

label choice_2b:

    n "A simple question. No advice attached. No hidden agenda. Just... tell me more."
    n "It's the kind of question that most people skip over, because it doesn't solve anything."
    n "But it does something else: it tells Fred that you're not bored yet. That you're willing to hear the whole thing, not just the summary."
    
    # show fred_sad...

    f "Honestly? Since the start of term. I thought it'd get better once everyone settled in, but it just... didn't."
    f "At first I thought maybe they were just busy. Midterms, whatever. But then I saw one of them post an Instagram story from East Coast at 2am on a weekday, and I just... I don't know."
    f "It's not about the free time. It's about the fact that they have it and they're choosing to spend it on everything but this."
    n "He's not just venting. He's making sense of something that hasn't made sense to him, and your question gave him room to do that. You didn't fix anything. You just held the door open a little wider."
    jump merge_point2

label merge_point2:

    f "I keep thinking maybe I'm messaging them wrong. Maybe I came across too uptight, or too naggy, or..."
    n "He stops himself mid-sentence. Shakes his head slightly."
    f "I mentioned it to Wei Ling last week. Just, you know, casually. And she was like 'that sucks bro' and then immediately started talking about her own midterms."
    f "And I know she didn't mean anything by it. But it kind of just... confirmed something I was already feeling. Like nobody actually wants to hear it. They just want you to be fine."
    n "He says 'be fine' like it's a performance he's been giving for weeks. Like it's a costume he can't take off."
    f "I don't know. I just feel like no matter what I do, I'm still going to end up being the one who has to fix everything."
    n "The cafeteria hums quietly around you. Somewhere behind you, two people burst out laughing at something on a phone screen. It feels very far away from this table."
    n "You look at Fred. Really look at him. The exhaustion isn't just in his eyes. It's in the set of his jaw, the slope of his shoulders, the way he's barely touched his food despite being here for twenty minutes."
    n "This has been building for a while."

label choice_3:

    menu:
        "What do you say?"

        "Well, you know how some people are. Don't take it personally.":
            if not choice_3_done:
                $ choice_3_done = True
            jump choice_3a

        "That's not on you. You're the only one who's been showing up, and the fact that they make you feel like you're the problem? That's on them.":
            if not choice_3_done:
                $ choice_3_done = True
                $ correct += 1
            jump choice_3b

label choice_3a:

    # show fred_distant...

    f "Yeah... I mean. Sure."
    n "'Don't take it personally' sounds like comfort. It's the kind of thing people say when they want to make you feel better."
    n "But it's actually a redirect, it tells Fred that his pain isn't really about him, when the whole problem is that it IS. He's the one carrying it. He's the one who can't put it down."
    n "Saying 'don't take it personally' doesn't lighten his load. It just tells him he's wrong to feel it."
    n "He agrees. But it's the kind of agreement that means 'I'll stop talking about this now.'"
    n "You said the sensible thing. But somewhere between your mouth and his ears, it landed wrong, like a hand held out to someone drowning, but just out of reach."
    jump repair_check

label choice_3b:

    # show fred_opening_up...

    f "I don't know if it says something good about me. Mostly it just feels like I can't stop, because if I do, everything falls apart."
    g "That's not the same as not being allowed to feel how heavy it is, though."
    n "Fred is quiet for a moment. He looks down at the table, then back at you."
    f "...yeah. I guess not."
    jump merge_point3

label repair_check:

    n "Fred is already moving on. But you felt it, the way the air changed. Like a window that was open a crack just got pulled shut."
    n "And here's the thing: you can feel it too. That tightness in your chest, that's not guilt, exactly. It's something else."
    n "It's the discomfort of knowing you just made someone feel dismissed, and the urge to pretend it didn't happen so you don't have to sit with that feeling."
    n "Psychologists call it empathic distress, when someone else's pain makes YOU so uncomfortable that you respond in ways that protect yourself, not them. The reflex is to move on, smooth it over, act like it didn't land wrong."
    n "You have a choice now. Not a comfortable one."
    jump choice_repair

label choice_repair:

    menu:
        "What do you say?"

        "Actually, wait. Can I take that back?":
            if not choice_repair_done:
                $ choice_repair_done = True
                $ repaired = True
            jump choice_repair_a

        "(Let it go. The moment passed.)":
            if not choice_repair_done:
                $ choice_repair_done = True
            jump choice_repair_b

label choice_repair_a:

    # show gary_concerned...

    g "Actually, wait..."

    # show fred_tired...

    f "...what?"
    g "That thing I just said. 'Don't take it personally.' I don't... that's not what I meant. I just..."
    n "Fred looks at you for a long moment. Something complicated moves across his face, not quite relief, not quite suspicion. More like recalibrating."
    n "Re-assessing whether you're someone who can be trusted to stay in the hard part, or whether this is another dead end."
    
    # show fred_opening_up...

    f "...it's fine. I know what you meant."
    n "He doesn't sound like he's dismissing it. He sounds like he's giving you another chance. Not because you said the right thing, you didn't. You said an incomplete thing. But you came back. And that's different."
    jump merge_point3

label choice_repair_b:

    n "You let it go. The moment passes. And the conversation continues, but something in its texture has changed."
    n "Fred is still here. Still talking. But he's editing himself now. Choosing his words more carefully. Measuring what he says before he says it."
    n "You can't hear the editing. But you can feel it, like a radio signal that was clear a moment ago and now has just a little static underneath."
    jump merge_point3

label merge_point3:

    n "The food on both your trays has gone lukewarm. Neither of you have noticed."

    # show fred_sad...

    f "I think what gets me the most is that I haven't been sleeping properly in like, two weeks? Maybe more."
    f "I keep waking up at 3am and immediately thinking about what's left to do."
    f "And every morning I open the shared doc and see that no one's touched it, and I just sit there and feel..."
    n "He pauses."
    f "I don't even know how to describe it. Like falling, but slowly. And you're the only one who noticed."
    n "There is a particular kind of loneliness in what he's describing."
    n "Not the loneliness of being friendless, but the loneliness of feeling responsible for something bigger than you can hold, while the people around you seem unbothered."
    n "Like you're standing in the rain and everyone else somehow isn't getting wet."
    n "Your phone buzzes in your pocket. You know what it is without looking. A deadline reminder for the EPD report due next week. The one you haven't started."
    n "For a second, your mind splits. One half here, with Fred, and the other half already reaching for the exit, already composing the mental list of everything you need to do tonight."
    n "You silence it. Put the phone away. But the ghost of that impulse lingers, the pull of your own responsibilities, the cost of staying."
    n "Somewhere behind you, a staff member starts stacking chairs at a nearby table. The canteen is closing, not urgently yet, but the rhythm of the place is shifting."
    n "The warm light feels a little less warm. The hum of the fan a little more noticeable."
    f "And the worst part, everyone else manages fine. I'm the only one who can't handle this."
    n "There it is. Not sadness anymore, something sharper. A story Fred is telling himself about himself."
    n "'Everyone else is fine. I'm the one who can't cope.' It's not true, you know it's not true. His teammates aren't fine, they're just not showing it. And Fred's situation IS genuinely harder than most."
    n "But here's the trap: both agreeing and disagreeing will shut him down."
    n "Agree and you're colluding with his self-blame. Disagree and you're correcting him, which tells him his feelings are wrong."
    n "The move is different. It's not about the content of what he said. It's about the source."

label choice_4:
    
    menu:
        "What do you say?"

        "That's not true. You're being way too hard on yourself.":
            if not choice_4_done:
                $ choice_4_done = True
                n "Supportive. But still a correction, it tells Fred his self-assessment is wrong."
            jump choice_4a

        "I know. It really isn't fair.":
            if not choice_4_done:
                $ choice_4_done = True
                n "Solidarity on the surface. But agreeing with someone's self-blame narrative isn't empathy, it's collusion. It confirms the spiral."
            jump choice_4b

        "Do you actually believe that, or is that the exhaustion talking?":
            if not choice_4_done:
                $ choice_4_done = True
                $ correct += 1
                n "A challenge, but aimed at the mechanism of the thought, not the person. It says: I know you well enough to tell the difference between Fred and Fred-at-3am."
            jump choice_4c

label choice_4a:

    n "You're trying to be supportive. And on paper, you are. 'You're being too hard on yourself' is a kind thing to say."
    n "But it's still a correction. It tells Fred his self-assessment is wrong, which means he has to argue with you about it or swallow the disagreement. Either way, the vulnerability just got harder."
    n "He asked you to stay in the hard part with him. Instead, you told him the hard part was wrong."

    # show fred_distant...

    f "I guess. Maybe."
    jump merge_point4

label choice_4b:

    n "You agreed with him. You meant it as solidarity. Yes, it's unfair, you're right to feel that way."
    n "But what Fred heard was confirmation. The problem is external. Everyone else is fine. I'm the exception. There's nothing to be done about any of this."
    n "That's not comfort. That's the 3am story. And you just endorsed it."
    
    # show fred_sad...
    
    f "Yeah. Exactly."
    n "He said 'exactly' like it was a door closing."
    jump merge_point4

label choice_4c:

    n "It's a risk. Every instinct tells you not to challenge someone who's already down, what if they take it as dismissal? What if it lands as 'stop feeling that way'?"
    n "But this isn't that. You're not telling him his feelings are wrong. You're asking him to check whether the voice in his head is actually his, or whether it's the version of him that's been running on empty for three weeks."
    n "It's a challenge that comes from knowing someone. Not from wanting to fix them."

    # show fred_opening_up...

    f "...I don't know."
    n "He doesn't have an answer. But something about the question makes him pause, genuinely pause, not the performed kind, and you can see him turning the thought over like something he hasn't looked at from this angle before."
    f "Maybe both? I don't... I can't tell anymore. Which is probably not a great sign."
    n "He says it with something that's almost a laugh. Not because it's funny. But because naming the confusion out loud makes it slightly smaller."
    n "This is different from every other moment tonight. You didn't validate him. You didn't agree with him. You just asked him to look at what he was saying more carefully, and trusted that he could."
    n "That's a kind of respect that 'you're being too hard on yourself' doesn't offer."
    jump merge_point4

label merge_point4:

    n "You feel an urge to say something. Something helpful. Something with steps."
    n "Your fingers twitch toward your phone, maybe you could look up something, send him a link, a framework, anything that would make this feel solvable."
    n "You don't do it. But the urge is there. And sitting with that urge, not acting on it, is harder than you expected."
    
    # show gary_warm...

    g "Fred... that sounds genuinely exhausting. Not just the project. All of it. The sleep, the carrying it alone, of course you're struggling."

    # show fred_sad...

    f "I've been telling myself it's fine for so long. Like if I just keep going, keep pushing, eventually it'll sort itself out."
    n "He exhales slowly."
    f "But I think I've just been really, really not fine for a while now."
    n "Saying it out loud seems to cost him something. But it also seems to take a weight with it, small, but real."
    n "Like the first crack in something that's been sealed too tight for too long."
        n "There's a silence. Not the heavy kind from before, something rawer."
    n "Like Fred just set down something he's been carrying with both hands, and his arms are trembling from the relief of it."
    n "Every instinct you have is telling you to fill this silence."
    n "To say something warm."
    n "To make the moment softer."
    n "To prove you were listening by showing you understood."
    n "But that impulse, the need to demonstrate that you understand, is actually about you. Not him."
    n "Behind you, the staff member has moved to the table right next to yours."
    n "She's wiping it down slowly, deliberately, the universal canteen code for 'we're closing and you should leave.'"
    n "You have maybe five minutes. Maybe less. The instinct is to use them, to say the thing, give the comfort, make this silence worth something."
    n "But worth something to who? To Fred? Or to you?"

label choice_5:

    menu:
        "What do you say?"

        "It'll pass. You always push through.":
            if not choice_5_done:
                $ choice_5_done = True
            jump choice_5a

        "(Say nothing. Let the silence hold.)":
            if not choice_5_done:
                $ correct += 1
                $ choice_5_done = True
            jump choice_5b

label choice_5a:

    n "You can see it land, the way Fred's face does something complicated in the space of a second. Gratitude and something else."
    n "'It'll pass' is meant as comfort. But what Fred heard was: this isn't real. It's temporary. It's small. You'll get over it."
    n "And maybe that's true. Maybe it will pass. But that's not what he needs to hear right now."
    n "He needs to hear that what he's feeling is allowed to be big. Even if it's temporary. Especially if it's temporary."

    # show fred_distant...

    f "...yeah. I guess."
    n "He wanted you to stay in the hard part with him. Instead, you showed him the exit. And he took it, because that's what he's been doing all along. Running from the hard part."
    n "You just made it easier."
    jump merge_point5

label choice_5b:

    n "You don't say anything."
    n "Five seconds. Maybe ten. Long enough that you can feel the canteen around you again, the fan, the distant clatter of a staff member stacking cups."
    n "Fred looks down at his hands. Takes a slow breath. And something shifts, not a smile, not relief, just... a loosening. Like a knot that's been pulled tight for weeks and just got a quarter-turn looser."
    n "You didn't do anything. That was the point."

    # show fred_opening_up...

    f "...thanks. For not... yeah. Thanks."
    jump merge_point5

label merge_point5:

    n "You sit with that for a moment."
    n "The staff member glances at your table. Not rudely. Just a look. You have maybe three minutes now, if that."
    n "Fred notices too. You can see him register it, the way his eyes flick toward the staff, then back. Something about the external pressure seems to make a decision for him."
    f "Sorry. I don't mean to dump all of this on you."
    g "You're not dumping anything. Keep going."
    n "He looks at you. Then, quietly..."
    f "I think what scares me most is that I want to confront them about it."
    f "I really do. But every time I start typing a message, I think about how it might come across."
    f "What if they think I'm being difficult?"
    f "What if it makes the dynamic weird for the rest of the project?"
    f "So I just… delete it. And go back to doing everything myself."
    n "A short, self-deprecating exhale. Almost a laugh, but not quite."
    f "It's stupid, right."
    n "He says it like a statement. Like he's already decided the answer."
    f "I already tried opening up about it once. To Wei Ling. And that just, it didn't go well. She meant well, but she kind of made me feel like I was making a big deal out of nothing."
    f "And I thought, okay, maybe I am. Maybe this is just me being dramatic."
    f "And if I bring it up again, to anyone, they'll think the same thing."
    n "There it is. The real shape of the fear. It's not about the teammates. It's not even really about the project."
    n "It's that Fred tried to ask for help once, and the person he asked, however unintentionally, made him feel like the asking was the problem."
    n "And now every time he thinks about reaching out, he hears Wei Ling's voice underneath his own. 'That sucks bro.' Then nothing."
    n "One bad experience. That's all it took to teach him that vulnerability doesn't work."
    
    # show fred_distant...
    
    f "Actually you know what, never mind."
    f "It's not even... it's fine."
    n "There it is. The retraction. He's gathering the words back up, putting them away, taping the box shut."
    n "It's the most honest he's been all evening and he's trying to take it back."
    n "This is the moment that matters most. Not because of what he said, but because of what happens right now, when he gives you permission to let him off the hook."
    n "The staff member is literally two tables away now. The canteen is about to close. Part of you wants to take the out, it's late, he's tired, the moment is over, why push it?"
    n "But that 'why push it' voice? That's the same voice Fred has been hearing every time he thinks about confronting his team. It's the voice that says: don't make it weird. Don't be difficult. Let it go."
    n "The question is whether you listen to it."

label choice_6:

    menu:
        "What do you say?"

        "Wait! Don't do that. Don't pack it back up. It's not stupid. I'm right here. Keep going.":
            if not choice_6_done:
                $ correct += 1
                $ choice_6_done = True
            jump choice_6a

        "Yeah, don't sweat it. We don't have to talk about it if you don't want to.":
            if not choice_6_done:
                $ choice_6_done = True
            jump choice_6b

label choice_6a:

    n "You don't yell it. You don't even raise your voice. You just, don't let him leave. Not physically. But you don't make it easy for him to retreat either."
    n "There's a difference between pushing someone to open up and refusing to pretend they didn't just open up. You're doing the second one."
    n "And Fred can feel the difference."

    # show fred_opening_up...

    f "I just hate feeling like the difficult one. Like everyone else is somehow fine and I'm the only one who has a problem."
    g "You're not the difficult one for having a limit. You're the one who cared enough to keep going when the others checked out."
    n "Fred stares at you."
    n "Like that sentence landed in a place it wasn't expected to reach."
    f "...I hadn't thought of it like that."
    g "Most people don't, when they're in the middle of it."
    n "A beat. Quiet, but not uncomfortable. The first quiet of the evening that doesn't feel heavy."
    jump path_check

label choice_6b:

    n "You let him off the hook. It feels like kindness, giving him an exit, not pushing, respecting his boundary."
    n "But Fred wasn't asking for permission to stop. He was testing whether you'd still be there if he showed you something ugly."
    n "And you said: no, put it away. I'll wait until you're presentable again."
    
    # show fred_distant...
    
    f "...yeah. You're right."
    n "He agrees. And then goes quiet in that specific way that means the conversation is gently, firmly over."
    n "You said the gentle thing. But he wasn't asking for gentle. He was asking to not feel stupid for struggling, and you accidentally confirmed that he should."
    jump path_check

label path_check:

    if correct >= 4 or (correct == 3 and repaired):
        jump good_ending
    elif correct >= 3:
        jump mixed_ending
    else:
        jump bad_ending

label good_ending:

    # show fred_relieved...

    n "Fred sits back in his chair. Not fixed. Not solved. But somehow less braced."
    f "I think I just needed to say it out loud. I've been running all of this through my head on a loop for weeks and it just... it gets louder every time, you know?"
    f "Saying it to someone makes it feel like an actual problem instead of just this cloud I'm living inside."

    # show gary_warm...

    g "It is an actual problem. A hard one. But an actual, solvable one."
    f "Yeah."
    n "He finally picks up his fork. Takes a proper bite of his food. Chews slowly."
    f "Thanks for actually listening, Gary."
    f "Like... actually."
    f "I half expected you to say 'just talk to them bro' and move on."
    g "I mean... I do think you should talk to them."

    # show fred_relieved

    f "Yeah, yeah. I know."
    n "And there it is. The real Fred, briefly. The one who laughs easily, who doesn't disappear inside his own head."
    n "Still tired. Still anxious. But present. Here. With you."
    g "Do you want to figure out how to approach them? Like actually think it through, what to say, what tone to take, what you're asking for."
    f "Not tonight, I think. I just want to... I don't know. Sit with it for a bit. But not alone. Not this time."
    n "He says it like he's discovering something about himself as the words come out."
    n "Like the idea that he's allowed to sit with a problem without fixing it,  and that he doesn't have to do that alone, is genuinely new to him."
    n "The staff member is at the table next to yours now. She clears her throat, just barely."
    n "Fred looks at you. You look at him. Neither of you want to leave. But neither of you needs to, not the way you would have twenty minutes ago."
    n "Sometimes knowing someone is willing to stay is enough. You don't have to solve the clock."
    n "The two of you stay at the corner table for another hour. The canteen empties out around you."
    n "A staff member starts stacking chairs nearby, the universal signal, and you both finally pack up and leave."
    n "By the end of it, Fred has a plan. A small one, a message to draft, a meeting to propose, a line he's decided he's allowed to draw."
    n "It's not a solution. Not yet. But it's a beginning."
    n "And sometimes, that's everything."

    # show fred_relieved at right
    # show gary_warm at left

    n "Fred gathers his tray. He looks lighter, not fixed, not solved, but lighter. Like something has been set down, even temporarily."
    f "Seriously. Thank you."
    g "Anytime. And I mean that. Not just tonight."

    # show fred_relieved...

    f "I know."

    # hide fred...
    # show gary_warm...

    n "You sit alone for a moment after he leaves. The canteen is almost empty now. The ceiling fan still hums, uselessly."
    n "You didn't solve his problem. You didn't give him a five-step plan or make his teammates suddenly care."
    n "You just stayed. And listened. Really listened."
    n "And it turned out that was exactly what he needed."
    n "Your phone buzzes. A message from Fred:"
    n "'hey. i don't feel better exactly. but i feel like i'm allowed to not feel better? if that makes sense. anyway thanks. see you tomorrow.'"
    n "It makes sense. It makes more sense than anything you could have told him."

    # scene bg_black...
    # GOOD ENDING BLABLABLA...
    jump post_game_survey

label mixed_ending:

label bad_ending:

label post_game_survey:

    return