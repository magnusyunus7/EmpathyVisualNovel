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
    return