# 40 broad-audience topics for Built by Agents

Researched 2026-10-25. AI topics: 3 of 40 (limit was 1 in 5).
Demand evidence: "Suggest" = real Google autocomplete returned for the query (suggestqueries endpoint, today). "Top videos" = top YouTube search results scraped today (title, channel, views as shown). Both are real but are signals, not search-volume numbers. Competition caveat: a big existing video proves demand AND means we need a fresher angle.
Sources: "V" = URL opened and returned 200 with matching title this session; "V*" = opened, but my fact claim beyond the page title comes from memory; "U" = could not open or not checked (bot-blocked, 404 or never tried), find a replacement before scripting. Claims marked [M] in a hook are from memory and must be checked in the cited source before use.

## Top 10 for the first month (ranked)

| # | Topic | Why it ranks |
|---|---|---|
| 1 | B6 What if the Sun vanished (gravity is not instant) | Vsauce 20.9M proves demand; one clean visual (8 min 20 s countdown); paper source is open and checkable |
| 2 | A1 How a QR code works | Veritasium 9.7M plus 1.36M in a plain explainer; Suggest shows 10 variants; very animatable (grid, error correction) |
| 3 | E5 Why every world map is wrong | Vox 23.8M; the whole video is one comparison animation (true size) |
| 4 | A3 How the internet crosses oceans | VISION 11.9M; physical mechanism, maps and ships; single source (submarinecablemap.com) |
| 5 | B1 GPS needs relativity | Counter-intuitive number (38 microseconds a day) from a verified page; low competition in animated form (top results under 1M except minutephysics 1.0M) |
| 6 | C3 The dress | AsapSCIENCE 29.9M; peer-reviewed survey (1,401 people) gives clean data; Short-friendly |
| 7 | E2 Leap years and the 10 deleted days | CGP Grey 7.5M proves appetite; our angle (1582 deletion) is distinct; easy timeline animation |
| 8 | C1 Why you can't tickle yourself | Perfect Short; peer-reviewed source; low long-form competition (top results under 350K) |
| 9 | G2 Tacoma Narrows: not the story you were told | Practical Engineering 1.75M, British Pathe 4.5M footage demand; strong myth-flip hook (check source before claiming) |
| 10 | F1 Why zebras have stripes | TED-Ed only 663K; open-access PLOS paper; hedged but concrete answer |

Suggested order: 1, 2 (long-form anchors), Shorts cut from each, then 3, 8, 5, 6, 4, 7, 9, 10.

---

## A. Everyday tech and the internet

**A1. How a QR code works.** Working title: "The Hidden Grid Inside a QR Code"
- Hook: a QR code can be scratched and still scan because extra error-correction data is built into the pattern.
- Cares because: everyone scans them daily and nobody knows why they survive damage.
- Demand: Suggest "how does a qr code work for payment / step by step / store data". Top: Veritasium 9.7M, History of Simple Things 1.36M.
- Sources: https://www.qrcode.com/en/history/ (V, Denso Wave history); Wikipedia QR code (U, not opened).
- Short: "A QR code can lose 30% of itself and still work. Here's the math trick." [M: confirm 30% for level H at qrcode.com]

**A2. What happens in the first second after you type google.com.** Working title: "The 1-Second Journey of a Web Page"
- Hook: your request hops through name lookup, handshakes and encryption before a single pixel arrives.
- Cares because: explains why pages are slow and what "the internet" physically is.
- Demand: Suggest returned "what happens when you type google.com in your browser". Top: ByteByteGo 480K, Hussein Nasser 150K (long, technical, so friendly version is open).
- Sources: RFC 1035 https://www.rfc-editor.org/rfc/rfc1035 (V); Cloudflare Learning DNS page (U, 403 to my fetch).
- Short: "Typing a web address starts a phone book lookup across the planet. 4 steps in 30 seconds."

**A3. How the internet crosses oceans.** Working title: "The Internet Is a Cable on the Seafloor"
- Hook: almost all intercontinental internet traffic runs through cables on the sea bed, not satellites. [M: commonly cited ~99%; verify]
- Cares because: it reframes "the cloud" as a physical thing that ships can cut.
- Demand: Suggest "how do undersea internet cables work". Top: VISION 11.9M, RealLifeLore2 1.74M, Fluctus 4.3M.
- Sources: https://www.submarinecablemap.com/ (V). Add TeleGeography/ITU for traffic share (U).
- Short: "Your Netflix crossed the Atlantic inside a cable as thick as a garden hose."

**A4. How Shazam recognises a song.** Working title: "How Shazam Hears a Song in 5 Seconds"
- Hook: it does not store songs as audio; it matches a sparse fingerprint of loud peaks.
- Cares because: everyone has used it; magic made simple.
- Demand: Suggest "how does shazam work so fast". Top: Real Engineering 2.75M, WSJ 358K.
- Sources: Wang 2003 paper https://www.ee.columbia.edu/~dpwe/papers/Wang03-shazam.pdf (V).
- Short: "Shazam matches dots, not sound. Watch the dots."

**A5. How websites store your password (they shouldn't).** Working title: "Your Password Isn't Stored. Here's What Is."
- Hook: a site can check your password without ever knowing it.
- Cares because: every login; safe, non-political security literacy. Avoid giving personal security advice beyond the cited cheat sheet.
- Demand: Suggest "how does hashing passwords work". Top: Simply Explained 400K, Studying With Alex 338K, Seytonic 281K.
- Sources: OWASP Password Storage Cheat Sheet https://cheatsheetseries.owasp.org/cheatsheets/Password_Storage_Cheat_Sheet.html (V).
- Short: "A one-way blender: put in a password, get a code, can't unblend."

**A6. How a touchscreen knows where your finger is.** Working title: "Your Screen Can Feel Electricity in Your Finger"
- Hook: a phone detects you by the tiny charge your body steals from the glass, which is why gloves fail. [M: capacitive sensing; confirm in source]
- Cares because: touched thousands of times a day; explains glove and wet-screen failures.
- Demand: Suggest "how does a touchscreen work". Top: Branch Education 4.06M, This. 2.1M.
- Sources: Wikipedia Touchscreen (U, not opened); add a manufacturer or IEEE source before scripting.
- Short: "Why your phone ignores gloves."

## B. Space and physics

**B1. GPS needs relativity.** Working title: "Your Phone Is Using Einstein Right Now"
- Hook: GPS satellite clocks gain about 38 microseconds a day compared with ground clocks, and the system is built to correct it.
- Cares because: relativity stops being abstract; you use it for navigation.
- Demand: Suggest "how does relativity affect gps". Top: minutephysics 1.0M (1:38), FlightInsight 50K. Little animated long-form competition.
- Sources: https://www.astronomy.ohio-state.edu/pogge.1/Ast162/Unit5/gps (V; gives 38 microseconds a day). Warning: that page and popular videos say errors would grow ~10 km a day uncorrected; that framing is disputed, so say "errors would pile up" unless a better source is found.
- Short: "GPS satellites run 38 microseconds fast every day. Engineers cancel it on purpose."

**B2. Why astronauts float.** Working title: "Astronauts Aren't Weightless. They're Falling."
- Hook: gravity at the space station is about 89% of Earth's surface gravity; astronauts float because they're in constant free fall around Earth.
- Cares because: kills one of the most common misconceptions.
- Demand: Suggest "why do astronauts float in space but not on earth". Top: Observable Universe 50K, AumSum 81K (small, so the animated bar is low).
- Sources: NASA "What is Microgravity?" https://www.nasa.gov/learning-resources/for-kids-and-students/what-is-microgravity/ (V; says 88.8% at about 250 miles, 17,500 mph).
- Short: "There's gravity on the ISS. They're just falling and missing the Earth."

**B3. Why is the night sky dark?** Working title: "If Space Is Endless, Why Isn't the Sky Bright?"
- Hook: in an infinite, unchanging universe every line of sight would hit a star, so the sky should glow; it doesn't.
- Cares because: a child's question with a deep answer (the universe has an age).
- Demand: Suggest "why is the sky dark at night paradox". Top: minutephysics 4.7M, StarTalk 788K.
- Sources: https://en.wikipedia.org/wiki/Olbers%27_paradox (V). Use a NASA/ESA source for the age-of-universe resolution (U).
- Short: "An endless universe should make night as bright as day. It doesn't. Why?"

**B4. Why we only see one side of the Moon.** Working title: "The Moon Spins. You Just Can't Tell."
- Hook: the Moon rotates exactly once per orbit, so the same face points at us.
- Cares because: obvious thing everyone has seen; most think the Moon doesn't spin.
- Demand: Suggest "why does the moon always show the same face". Top: MinuteEarth 4.2M.
- Sources: https://en.wikipedia.org/wiki/Tidal_locking (V*). Add NASA Moon facts (U).
- Short: "The Moon spins once per orbit, which is why you never see the far side."

**B5. How we measure the distance to stars.** Working title: "Measuring Stars With Your Thumb (Almost)"
- Hook: close one eye, then the other, and you've done the same trick astronomers use to measure the nearest stars.
- Cares because: answers "how do they know?", the most common skeptic question.
- Demand: Suggest "how do we measure distance to stars". Top: TED-Ed 3.7M, SciAm 133K.
- Sources: ESA Gaia https://www.esa.int/Science_Exploration/Space_Science/Gaia/Gaia_overview (V).
- Short: "Blink one eye, then the other. That's how we measure stars."

**B6. What if the Sun vanished?** Working title: "The Sun Disappears. Earth Doesn't Notice for 8 Minutes."
- Hook: gravity travels at the speed of light, so Earth would keep orbiting for about 8 minutes 20 seconds. [M: figure; check]
- Cares because: pure thought experiment with a surprising reversal.
- Demand: Suggest "what would happen if the sun disappeared gravity". Top: Vsauce 20.9M, Peekaboo Kidz 4.2M.
- Sources: Carlip, "Aberration and the Speed of Gravity" https://arxiv.org/abs/gr-qc/9909087 (V; abstract says gravity can propagate at c). 
- Short: "Delete the Sun and Earth keeps orbiting for 8 minutes."

## C. The human body and the brain (no health advice)

**C1. Why you can't tickle yourself.** Working title: "Your Brain Spoils the Tickle"
- Hook: your brain predicts your own touch and cancels it.
- Cares because: instantly testable, universal.
- Demand: Suggest "why cant you tickle yourself but others can". Top: SciShow 340K, BrainFacts 30K.
- Sources: Blakemore, Wolpert, Frith 1998, Nature Neuroscience https://doi.org/10.1038/2870 (V); Scientific American Q&A https://www.scientificamerican.com/article/why-cant-a-person-tickle/ (V).
- Short: "Your brain sends a spoiler before your finger moves."

**C2. You go blind when your eyes jump.** Working title: "You're Blind Several Times a Second"
- Hook: during quick eye movements your brain suppresses vision and edits the gap so you never notice.
- Cares because: it's a trick the viewer can test in a mirror.
- Demand: no Suggest returned. Top: small channels (74 to 72K views). Weak proof of demand, high novelty.
- Sources: https://en.wikipedia.org/wiki/Saccadic_masking (V). Do NOT use the "40 minutes a day blind" claim seen in a video title; unverified.
- Short: "Look at your eyes in a mirror, then shift your gaze. You can't see your eyes move."

**C3. The dress.** Working title: "Why Your Brain Saw a Different Dress"
- Hook: people saw the same photo as white-gold or blue-black because their brains guessed different lighting.
- Cares because: a shared memory; it teaches that perception is inference.
- Demand: Top: AsapSCIENCE 29.9M.
- Sources: Lafer-Sousa, Hermann, Conway 2015, Current Biology; open copy https://pmc.ncbi.nlm.nih.gov/articles/PMC4921196 (V; 1,401-person survey in the paper).
- Short: "Same pixels, different dress. Your brain assumed different light."

**C4. How the ear turns air into sound.** Working title: "The Snail in Your Ear"
- Hook: a fluid-filled spiral sorts pitches by position, like a piano laid inside a shell.
- Cares because: everyone hears; clean animation of vibration to signal.
- Demand: no Suggest. Top: NIH video 12.0M, Neuroscientifically Challenged 613K.
- Sources: NIDCD https://www.nidcd.nih.gov/health/how-do-we-hear (V). Anatomy only; no hearing-loss advice.
- Short: "Your ear is a piano made of fluid."

**C5. Your brain fills in the hole in your vision.** Working title: "There's a Hole in Your Vision. You've Never Seen It."
- Hook: each eye has a blind spot where the optic nerve exits; the brain paints over it.
- Cares because: a 10-second at-home test.
- Demand: not checked (U). Sources to find: NEI/NIH (U).
- Short: "Cover one eye, stare at the plus, move the dot: it vanishes."

## D. Money and economics (explanation only, no investing advice)

**D1. How banks create money.** Working title: "Where New Money Actually Comes From"
- Hook: most money in circulation is created when banks make loans, per the Bank of England.
- Cares because: demystifies the thing everyone uses.
- Demand: Suggest "how do banks create money out of thin air". Top: Jacob Clifford 1.24M, Five Minute Finance 474K.
- Sources: Bank of England 2014 https://www.bankofengland.co.uk/quarterly-bulletin/2014/q1/money-creation-in-the-modern-economy (V). Avoid policy opinions.
- Short: "A bank loan doesn't move money. It makes it."

**D2. What happens when you tap a card.** Working title: "The 2-Second Trip Your Card Payment Takes"
- Hook: your tap triggers an authorisation chain across several parties, but the money moves later in batches.
- Cares because: everyone pays by card.
- Demand: no Suggest. Top: Scotiabank 2.0M (ad), KingCademy 36K. Weak.
- Sources: not found. Needs a card-network or central-bank source (U).
- Short: "A card tap is a yes/no question asked across 4 companies."

**D3. Why two seats on the same plane cost different prices.** Working title: "Why Your Neighbor Paid Half"
- Hook: airlines sell the same seat in many price buckets and move them as the flight fills.
- Cares because: everyone has felt it.
- Demand: no Suggest. Top: small (under 10K). Low proof of demand.
- Sources: https://en.wikipedia.org/wiki/Yield_management (V*); find an academic or airline-industry source (U).
- Short: "One plane, 30 prices."

**D4. The Rule of 72.** Working title: "Double Your Money: The Mental Math Trick"
- Hook: divide 72 by a growth rate to estimate years to double.
- Cares because: reusable maths for loans, inflation and savings, with no advice given.
- Demand: Top: WhiteBoard Finance 409K, Alliance Group 253K.
- Sources: SEC Investor.gov compound interest calculator https://www.investor.gov/financial-tools-calculators/calculators/compound-interest-calculator (V*). Origin of rule [M]: do not claim.
- Short: "72 divided by the rate gives the years to double."

**D5. How the shipping container changed the world.** Working title: "The Steel Box That Rebuilt the Economy"
- Hook: a standard box cut loading costs so far that distance mattered less. [M: Levinson's The Box; verify figures]
- Cares because: explains why everything is cheap and far away.
- Demand: Suggest returned only the exact query. Top: WSJ 504K, TED-Ed 650K.
- Sources: Levinson, The Box, Princeton UP https://press.princeton.edu/books/paperback/9780691170817/the-box (U, 403 to bot); https://en.wikipedia.org/wiki/Shipping_container (V*).
- Short: "One steel box made the world smaller."

## E. History and how did we get here

**E1. How time zones were invented.** Working title: "Every Town Had Its Own Time Until Trains"
- Hook: railways forced towns to agree on clock time. [M: 1883 North American adoption; verify]
- Cares because: shows how a technology rewrote daily life.
- Demand: Top: History Matters 1.0M, TED-Ed 264K.
- Sources: https://en.wikipedia.org/wiki/Standard_time (V*). Better source needed (U).
- Short: "Why noon used to differ between neighbouring towns."

**E2. The leap year and the 10 deleted days.** Working title: "The Year Europe Skipped 10 Days"
- Hook: in 1582 the calendar jumped ahead 10 days to fix drift. [M: confirm exact dates]
- Cares because: explains why leap years exist and why a year is 365.2425 days.
- Demand: Top: CGP Grey 7.5M, StarTalk 881K.
- Sources: https://en.wikipedia.org/wiki/Gregorian_calendar (V*). Add a primary or Vatican/astronomy source (U).
- Short: "Every 100 years we skip a leap year, except every 400."

**E3. How the metre was defined.** Working title: "The Metre Was Supposed to Come From the Earth"
- Hook: France defined the metre as one ten-millionth of the distance from pole to equator, then the survey took seven years. [M detail; search found Delambre and Mechain survey 1792-1799 from secondary sources]
- Cares because: why most of the world uses one system.
- Demand: Top: Be Smart 1.63M. 
- Sources: NIST timeline https://www.nist.gov/document/museum-timelinepdf (V*); BIPM page (U, my URL 404'd).
- Short: "A metre was meant to be a slice of the planet."

**E4. QWERTY: the myth and the truth.** Working title: "Why Your Keyboard Isn't in ABC Order"
- Hook: the popular "slow typists down" story is disputed. [M: Liebowitz and Margolis argue against it; verify]
- Cares because: everyone types; fun myth flip.
- Demand: Top: Vox 3.4M, Peekaboo Kidz 4.9M.
- Sources: https://en.wikipedia.org/wiki/QWERTY (V*); Smithsonian article (U, bot-blocked).
- Short: "The reason for QWERTY you were told may be wrong."

**E5. Why every world map is wrong.** Working title: "Greenland Is Not That Big"
- Hook: flattening a sphere always distorts something; Mercator keeps angles and inflates size.
- Cares because: one overlay animation changes how people see the world.
- Demand: Top: Vox 23.8M, TED-Ed 1.0M.
- Sources: https://en.wikipedia.org/wiki/Mercator_projection (V*); Britannica (U, bot-blocked).
- Short: "Drag Greenland to the equator and it shrinks."

## F. Nature and animals

**F1. Why zebras have stripes.** Working title: "The Stripes Are Anti-Fly Armor"
- Hook: biting flies land less on striped coats, per a field experiment. Explanation is best-supported, not settled.
- Cares because: classic mystery with an unexpected answer.
- Demand: Suggest "why do zebras have stripes". Top: TED-Ed 663K, SciShow Kids 430K.
- Sources: Caro et al 2019 PLOS ONE https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0210831 (V).
- Short: "Flies are bad at landing on stripes."

**F2. How trees lift water with no pump.** Working title: "Trees Have No Pump. They Pull."
- Hook: water is pulled up as evaporation tugs a continuous chain of molecules, no heart needed. [cohesion-tension theory; widely taught, debated at edges]
- Cares because: how a 100-metre tree drinks.
- Demand: no Suggest; top results are new and small (under 50K). Low competition.
- Sources: https://en.wikipedia.org/wiki/Cohesion-tension_theory (V, redirected to Xylem article); find a plant-physiology source (U).
- Short: "A tree drinks by evaporating."

**F3. How an octopus changes colour.** Working title: "Skin That Thinks"
- Hook: thousands of colour sacs in the skin expand and shrink under muscle control. [M]
- Cares because: universal wow factor.
- Demand: Suggest "how does an octopus change color and texture". Top: Dive&Discover 1.04M, BBC 734K.
- Sources: my link https://www.mbl.edu/news/octopus returned an unrelated nervous-system article (not a valid colour source). Find Woods Hole or peer-reviewed source (U). Skip colour-blindness claims (contested).
- Short: "Octopus skin is a screen run by muscles."

**F4. How bats see with sound.** Working title: "Bats Draw With Echoes"
- Hook: bats build a picture from the delay and pitch of their own shouts.
- Cares because: easy to visualise with ripples.
- Demand: Suggest "how do bats use echolocation". Top: SciShow Kids 473K.
- Sources: https://en.wikipedia.org/wiki/Animal_echolocation (V*); add research source (U).
- Short: "A bat shouts and reads the echo like a map."

**F5. The banana that could disappear.** Working title: "Every Banana You Eat Is a Clone"
- Hook: the Cavendish is a clone, so one fungus strain can hit all of them; do NOT say "going extinct".
- Cares because: everyday fruit, food-security stakes.
- Demand: Suggest "what happened to the cavendish banana". Top: VICE 3.0M, Vox 245K.
- Sources: FAO CCP70 note https://www.fao.org/fileadmin/user_upload/bodies/CCP_70/CCP70-Banana_Fusarium_-7Oct.pdf (V, 200; contents not read; search snippet says TR4 was in 17 countries in 2019).
- Short: "Every Cavendish banana is the same plant."

## G. Food, materials and engineering

**G1. How planes really fly.** Working title: "The Wing Lift Story You Were Told Is Wrong"
- Hook: the "air must meet at the back" explanation is a misconception. [M: NASA page addresses it; confirm wording]
- Cares because: everybody flies.
- Demand: Top: TED-Ed 2.5M, Efficient Engineer 2.1M.
- Sources: NASA Glenn https://www.grc.nasa.gov/www/k-12/VirtualAero/BottleRocket/airplane/lift1.html (V*).
- Short: "A wing doesn't pull. It throws air downward."

**G2. Tacoma Narrows.** Working title: "The Bridge Collapse Textbooks Get Wrong"
- Hook: popular accounts blame resonance; engineers describe aerodynamic flutter. [M: Billah and Scanlan 1991, not verified]
- Cares because: iconic footage plus myth-flip.
- Demand: Suggest "tacoma narrows bridge why did it collapse". Top: British Pathe 4.5M, Practical Engineering 1.75M.
- Sources: https://en.wikipedia.org/wiki/Tacoma_Narrows_Bridge_(1940) (V*).
- Short: "The bridge didn't fall from resonance the way textbooks say." (confirm first)

**G3. Concrete doesn't dry.** Working title: "Concrete Doesn't Dry. It Cooks Itself Solid."
- Hook: concrete hardens by a chemical reaction with water; underwater it still sets.
- Cares because: everyday material, simple myth flip.
- Demand: Suggest "does concrete dry or cure". Top: History of Simple Things 149K, Civil Mentors 210K.
- Sources: American Cement Association https://www.cement.org/cement-concrete/how-cement-is-made (V, generic page); need a stronger source (U).
- Short: "Concrete needs water to harden."

**G4. How a microwave heats food.** Working title: "The Microwave Shakes Water"
- Hook: water molecules rotate in a fast oscillating field; thick food also heats outside-in through conduction, so "inside out" is a myth.
- Cares because: daily appliance.
- Demand: Suggest "how does a microwave oven work". Top: Sabin Civil 8.0M, engineerguy 5.4M.
- Sources: FDA https://www.fda.gov/radiation-emitting-products/resources-you-radiation-emitting-products/microwave-ovens (V). No safety advice beyond the FDA page.
- Short: "A microwave is a spinning-water machine."

**G5. How Taipei 101 stays still.** Working title: "The Giant Ball That Stops Skyscrapers Swaying"
- Hook: a huge pendulum inside the tower swings against the sway. [M: size]
- Cares because: skyline wonder with simple physics.
- Demand: Top: Practical Engineering 2.8M.
- Sources: official page https://www.taipei-101.com.tw/en/observatory-damper (V, title only; contents unread).
- Short: "A giant ball swings the other way."

## H. AI (3 of 40)

**H1. How a chatbot picks the next word.** Working title: "It's Just Autocomplete (Sort Of)"
- Hook: a chatbot writes by choosing one token at a time, then loops.
- Cares because: demystifies a tool people use daily.
- Demand: Suggest "does chatgpt just predict the next word". Top results small (under 25K).
- Sources: Vaswani et al 2017 https://arxiv.org/abs/1706.03762 (V).
- Short: "A chatbot writes one word at a time. Here's how it picks."

**H2. How image AI turns noise into pictures.** Working title: "Making a Picture by Removing Static"
- Hook: image generators start from random noise and learn to remove it step by step.
- Cares because: explains what AI art is.
- Demand: Top: Computerphile 1.07M, 3Blue1Brown with Welch Labs 2.19M.
- Sources: Ho et al 2020 https://arxiv.org/abs/2006.11239 (V).
- Short: "Start with TV static. Subtract 50 times. Get a cat."

**H3. How a feed decides what you see.** Working title: "How the Feed Picks Your Next Video"
- Hook: a two-stage system narrows millions of videos to a handful.
- Cares because: everyone scrolls.
- Demand: Suggest "how does tiktok recommendation algorithm work". Top results small (under 140K).
- Sources: Covington et al 2016 https://research.google/pubs/deep-neural-networks-for-youtube-recommendations/ (V). Describe the cited paper only; do not make claims about current YouTube/TikTok internals.
- Short: "Millions of videos in, ten out. Two filters."
