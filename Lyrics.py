Okayu = """There’s a trap over there. I’ve gotta get caught in it for you.
I act all bothered. Say it, say it, say it, say it.
Sweet things are fruit, and shame lies within bitterness.
I just try to dance. Yay, yay, yay!
Tangling and untangling is life. I’m not serious, so what of it?
Through your ethics, what do you think? I could hear you!
Hesitation and doubt is a warning. It’s unfortunate you didn’t listen to them.
Taking sly clumsiness in hand, yay, yay, yeah.
Play the game without breaking the rules.
Place a veil over the liars.
Make a mistake, thinking it’s just a misunderstanding.
This is the dead’s cultivated island. This world is paradise lost.
Adultery, pleasure, and decadence. The sandcastle looks over the wasteland.
This is the saints’ march. Surrounding the ghetto is paradise lost.
I gulp and make love.
It was exposed a long, long time ago. I’ve gotta return it to you.
I pretended to laugh. Say it, say it, say it, say it.
The gift is innocence, eyes that stared too hard.
You won’t come and stay at my house, house, house.
I devour the meal set before me to the plate itself. When I command them, it’ll be a holy war.
What was your birthplace called again? Tell me.
Are regrets and lingering attachments just chatter? Is it more fortunate to be antisocial?
I’m cowardly towards good and evil. No, no, no.
Play the game without dirtying the sheets.
Slovenly put a suit on.
Put fragrance on and grant a reward, an eye for an eye.
This is the dead’s cultivated island. They use force, yet it’s paradise lost.
The fools clad in pessimism are ashamed of their nudity.
This is the saints’ march. Losing its composure, this is paradise lost.
We deceive each other and then it’s all over.
Draw a spade from the deck of cards.
Once it’s broken
there’ll be nothing left, so much so you’d find it beautiful.
This is the dead’s cultivated island. This world is paradise lost.
Adultery, pleasure, and decadence. The sandcastle looks over the wasteland.
This is the saints’ march. Surrounding the ghetto is paradise lost.
I gulp and make love.
The one who understands and an X. I’m with you forever in paradise lost.
The children, fed up with peace, gnawed at corruption.
Karma and retribution. Now, let’s dive head-first into paradise lost!
I lose sight of those days, which were so fun. Farewell."""

print(len(Okayu))

in1 = input("Vad vill du byta ut inom texten: ")

in2 = input("Vad vill du byta ut denna andra gång inom texten: ")

in3 = input ("Vad vill du byta ut denna andra gång inom textenx3: ")

in4 = input("Vad vill du byta ut det till: ")

in5 = input("Vad vill du byta ut det till x2: ")

in6 = input("Vad vill du byta ut det till x3: ")

Okayu1 = Okayu.upper().replace(in1, in4)

Okayu2 = Okayu1.replace(in2, in5)

Okayu3 = Okayu2.replace(in3, in6)

Okayu4 = Okayu3.splitlines()

for line in Okayu4:
    print(line)