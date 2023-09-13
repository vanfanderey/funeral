
define e = Character("Narrator")


label start:

    scene bg prolog_1
    with fade

    e "It was a calm and somber day. Fluffy clouds seemed to be veiling the entire blue summer sky. Birds were flying low, and the air felt so heavy that it seemed to pour slowly and densely into the lungs."

    e "The ringing of bells from the nearby church and its parking lot, filled with various family cars, suggested that the clock had just struck twelve."
    
    menu:
        "I think another mass might have just started. I hope I'm not too late to catch the ceremony":
            "..."

    scene main_menu
    with fade
   
    e "At that moment, a faint singing sound echoed from behind the gate. It seemed to come from afar, carried only by gentle gusts of wind. With each passing moment, the singing grew stronger, as more people seemed to join in the hymn."

    menu:
        "The ceremony is still going on, which is good, but I'll have to hurry if I want to make it in time. Not sure how quickly I'll find them.":
            "..."
    
    menu:
        "(pass through the gate)":
            "..."
    
    scene bg prolog_3
    with fade
    
    e "As you gently pushed open the gate, you half-expected it to protest with a creak or groan, but to your surprise, it swung open effortlessly and silently. At first glance, the cemetery appeared to be shrouded in neglect, with ivy creeping over tombstones and faded paint adorning the entrance."
    e "However, as you ventured deeper and observed the finer details, you noticed the meticulous care put into preserving this resting place."

    menu:
        "(continue)":
            "..."

    scene bg prolog_8
    with fade
   
    e "As you strolled along the cemetery, you noticed that each path seemed to be guarded by a different statue. One of them particularly caught your attention."

    e "A few steps from the gate, hidden behind bushes and slightly off the main path, there was a small alley filled with tiny tombstones. At the entrance to the alley, perched proudly on a slender column, a little boy."
    e "Despite the visible wear and tear on the statue, an aura of purity and tranquility emanated from it. Its white hue stood out distinctively against the surroundings."
    e "The boy had short curly hair, a faint smile on his face, and a loose sash around his waist. On his back were tiny angelic wings, and in his hands, he cradled a stunning lily."
    e "There was something in his expression, in his delicate stone gestures, that compelled you to linger, unable to tear your gaze away."

    menu:
        "The artist who made this sculpture must be incredibly talented. They've somehow captured the essence of this place, especially this hidden alley, in the most extraordinary way."
    
        "However, this sculpture unsettles me.":
            "I can't shake the feeling that the boy's eyes are fixed on me, no matter which direction I turn. There's something unsettling about his smile—it almost feels sinister, as if there's a hidden secret behind it."
            "I try to look away, but his gaze seems to penetrate my thoughts. Is it just my imagination, or is there something more to this innocent-looking statue?"

        "This sculpture evokes a melancholic mood in me.":
            "My heart aches as I stand before the little boy, his eyes filled with an innocent joy, unaware of the rows of tiny tombstones behind him."
            "Life can be so cruel and unjust, and it's moments like these that remind me of its harsh reality. No parent should ever have to bury their own child—it's a pain I can't even fathom."
            "I can't help but feel a sense of sorrow and empathy, knowing that so many families have endured this unbearable loss."
        
        "This sculpture fills me with hope and tranquility.":
            "There's something captivating in the boy's posture and the tender way he holds that lily. It all feels so delicate and serene, like a gentle dance frozen in time."
            "As I take a closer look, it's as if his curly hair and sash are gently swaying in an unseen breeze, adding to the ethereal aura. He seems to be guarding all the innocent souls laid to rest here, promising them eternal peace and protection."
            "It's as if he's whispering silent reassurances to them, and for a moment, I can't help but believe in the solace he brings."


    scene bg prolog_2
    with fade
    
    e "Just as you were lost in your thoughts, mournful singing and audible weeping break the silence, pulling you back to reality. The stunning scenery of the cemetery's entrance briefly made you forget why you came here and that you should hurry."

    e "..."
    

    return
