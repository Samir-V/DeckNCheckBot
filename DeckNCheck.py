import os

import asyncio

from aiohttp import web

from aiogram import Bot, Dispatcher, types

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import FSInputFile


TOKEN = os.getenv("BOT_TOKEN")

WEBHOOK_HOST = os.getenv("WEBHOOK_HOST")  # https://your-app.onrender.com

WEBHOOK_PATH = "/webhook"

WEBHOOK_URL = f"{WEBHOOK_HOST}{WEBHOOK_PATH}"


bot = Bot(token=TOKEN)

dp = Dispatcher()


async def handle_webhook(request):

    data = await request.json()

    update = types.Update(**data)

    await dp.feed_update(bot, update)

    return web.Response()


async def healthcheck(request):

    return web.Response(text="OK")


# --- КНОПКИ ---


class_kb = ReplyKeyboardMarkup(

    keyboard=[

        [KeyboardButton(text="5-6 класс")],

        [KeyboardButton(text="7-9 класс")]

    ],

    resize_keyboard=True

)


mode_kb = ReplyKeyboardMarkup(

    keyboard=[

        [KeyboardButton(text="📘 Теория")],

        [KeyboardButton(text="📝 Практика")],

        [KeyboardButton(text="⬅️ Назад")]

    ],

    resize_keyboard=True

)


# --- ДАННЫЕ (сокращённые, ты можешь расширить) ---


user_class = {}

user_mode = {}

user_topic = {}

user_subtopic = {}

current_task = {}


topics = {

    "5-6": [

        "Article",

        "Present Continuous",

        "Comparisons",

        "Prepositions of time",

        "Future Simple",

        "Countable/Uncountable",

        "Question",

        "Modal verbs",

        "Present Simple",

        "Singular and plural",

        "Present Perfect",

        "Linking verbs"

    ],

    "7-9": [

        "Stative Verbs",

        "Passive Voice",

        "Conditionals",

        "Gerund vs Infinitive",

        "Past Perfect Continuous",

        "Past Perfect",

        "Past Perfect vs PPC",

        "Future Simple & Constructions",

        "The (exceptions)",

        "Reported Speech",

        "Past Simple vs Past Continuous",

        "Present Perfect",

        "Present Perfect Continuous",

        "Gerund/Infinitive both"

    ]

}


tasks_by_topic = {

    "Article": {

        "Вставь A или An": [

            {

                "question": "This is ___ apple",

                "options": ["a", "an"],

                "correct": "an"

            },

            {

                "question": "He is ___ honest man",

                "options": ["a", "an"],

                "correct": "an"

            },

            {

                "question": "I saw ___ elephant at the zoo",

                "options": ["a", "an"],

                "correct": "an"

            },

            {

                "question": "My dad has ___ new car",

                "options": ["a", "an"],

                "correct": "a"

            },

            {

                "question": "It's a present for ___ old friend",

                "options": ["a", "an"],

                "correct": "an"

            },

        ],

        "Найди и исправь ошибку": [

            {

                "question": "I have **a** Idea\n\nКакой артикль должен стоять вместо выделенного?",

                "options": ["a", "an", "the"],

                "correct": "an"

            },

            {

                "question": "He is **a** uncle of mine\n\nКакой артикль должен стоять вместо выделенного?",

                "options": ["a", "an", "the"],

                "correct": "an"

            },

            {

                "question": "She is eating **a** orange\n\nКакой артикль должен стоять вместо выделенного?",

                "options": ["a", "an", "the"],

                "correct": "an"

            },

            {

                "question": "He told **an** very long story\n\nКакой артикль должен стоять вместо выделенного?",

                "options": ["a", "an", "the"],

                "correct": "a"

            },

            {

                "question": "Can I have **a** egg for breakfast?\n\nКакой артикль должен стоять вместо выделенного?",

                "options": ["a", "an", "the"],

                "correct": "an"

            },

        ],

        "Выбери правильный артикль": [

            {

                "question": "I bought ___ nice dress yesterday.",

                "options": ["a", "an", "the", "–"],

                "correct": "a"

            },

            {

                "question": "I can see ___ sun in the sky.",

                "options": ["a", "an", "the", "–"],

                "correct": "the"

            },

            {

                "question": "My brother wants to be ___ engineer.",

                "options": ["a", "an", "the", "–"],

                "correct": "an"

            },

            {

                "question": "She has ___ orange for lunch.",

                "options": ["a", "an", "the", "–"],

                "correct": "an"

            },

            {

                "question": "They play ___ tennis every weekend.",

                "options": ["a", "an", "the", "–"],

                "correct": "–"

            },

            {

                "question": "This is ___ easiest exercise in the book.",

                "options": ["a", "an", "the", "–"],

                "correct": "the"

            },

            {

                "question": "She lives in ___ old house.",

                "options": ["a", "an", "the", "–"],

                "correct": "an"

            },

            {

                "question": "Look at ___ blackboard, please!",

                "options": ["a", "an", "the", "–"],

                "correct": "the"

            },

            {

                "question": "We usually play football at ___ school.",

                "options": ["a", "an", "the", "–"],

                "correct": "–"

            },

            {

                "question": "He has ___ big family.",

                "options": ["a", "an", "the", "–"],

                "correct": "a"

            },

        ],

    },

    "Present Continuous": {

        "Вставь правильную форму 'to be'": [

            {"question": "I __ doing my homework.", "options": ["am", "is", "are"], "correct": "am"},

            {"question": "She __ watching a funny cartoon.", "options": ["am", "is", "are"], "correct": "is"},

            {"question": "They __ playing in the garden.", "options": ["am", "is", "are"], "correct": "are"},

            {"question": "My brother __ sleeping right now.", "options": ["am", "is", "are"], "correct": "is"},

            {"question": "We __ having a great time!", "options": ["am", "is", "are"], "correct": "are"},

            {"question": "It __ raining outside.", "options": ["am", "is", "are"], "correct": "is"},

            {"question": "You __ learning English.", "options": ["am", "is", "are"], "correct": "are"},

            {"question": "The cat __ running after a mouse.", "options": ["am", "is", "are"], "correct": "is"},

        ],

        "Раскрой скобки": [

            {"question": "Look! The boys __ (run) in the park.", "options": ["run", "runs", "are running"], "correct": "are running"},

            {"question": "Be quiet! The baby __ (sleep).", "options": ["sleep", "sleeps", "is sleeping"], "correct": "is sleeping"},

            {"question": "__ your sister __ (listen) to music?\n\nВыбери правильную форму:", "options": ["Is ... listening", "Does ... listen", "Are ... listening"], "correct": "Is ... listening"},

            {"question": "They __ (build) a new house near the river.", "options": ["build", "builds", "are building"], "correct": "are building"},

            {"question": "He __ (read) this book right now.", "options": ["read", "reads", "is reading"], "correct": "is reading"},

        ],

        "Расставь слова в правильном порядке": [

            {"question": "playing / aren't / They / football\n\nВыбери правильное предложение:", "options": ["They aren't playing football", "Aren't they football playing", "They playing aren't football"], "correct": "They aren't playing football"},

            {"question": "you / are / Why / crying / ?\n\nВыбери правильное предложение:", "options": ["Why are you crying?", "Why you are crying?", "Are you why crying?"], "correct": "Why are you crying?"},

            {"question": "a letter / writing / I / am\n\nВыбери правильное предложение:", "options": ["I am writing a letter", "Am I writing a letter", "I writing am a letter"], "correct": "I am writing a letter"},

            {"question": "the birds / Are / singing / ?\n\nВыбери правильное предложение:", "options": ["Are the birds singing?", "The birds are singing?", "Is the birds singing?"], "correct": "Are the birds singing?"},

        ],

    },

    "Comparisons": {

        "Преврати прилагательные в нужную степень": [

            {"question": "My brother is __ (strong) than me.", "options": ["stronger", "more strong", "strongest"], "correct": "stronger"},

            {"question": "Jupiter is the __ (large) planet in our solar system.", "options": ["larger", "largest", "most large"], "correct": "largest"},

            {"question": "This path is __ (safe) than that one.", "options": ["safer", "more safe", "safest"], "correct": "safer"},

            {"question": "Monday is the __ (bad) day of the week.", "options": ["worse", "worst", "baddest"], "correct": "worst"},

            {"question": "Your idea is __ (good) than my idea.", "options": ["gooder", "best", "better"], "correct": "better"},

        ],

        "Выбери правильный вариант": [

            {"question": "This is the __ book I have ever read.", "options": ["interesting", "more interesting", "most interesting"], "correct": "most interesting"},

            {"question": "My bag is __ than your bag.", "options": ["heavy", "heavier", "heaviest"], "correct": "heavier"},

            {"question": "The weather today is much __ than yesterday.", "options": ["good", "better", "best"], "correct": "better"},

            {"question": "Who is the __ student in your class?", "options": ["tall", "taller", "tallest"], "correct": "tallest"},

            {"question": "I think maths is __ than English.", "options": ["difficult", "more difficult", "most difficult"], "correct": "more difficult"},

        ],

    },

    "Prepositions of time": {

        "Вставь предлог (in, on, at)": [

            {"question": "I have English lessons __ Monday.", "options": ["in", "on", "at"], "correct": "on"},

            {"question": "My birthday is __ May.", "options": ["in", "on", "at"], "correct": "in"},

            {"question": "We usually have lunch __ noon.", "options": ["in", "on", "at"], "correct": "at"},

            {"question": "The party is __ June 15th.", "options": ["in", "on", "at"], "correct": "on"},

            {"question": "I visit my grandparents __ the weekend.", "options": ["in", "on", "at"], "correct": "at"},

            {"question": "Birds fly south __ autumn.", "options": ["in", "on", "at"], "correct": "in"},

            {"question": "I do my homework __ the evening.", "options": ["in", "on", "at"], "correct": "in"},

        ],

        "Выбери правильный предлог": [

            {"question": "I always wake up early __ the morning.", "options": ["in", "on", "at"], "correct": "in"},

            {"question": "Let's meet __ Friday.", "options": ["in", "on", "at"], "correct": "on"},

            {"question": "The concert is __ March 10th.", "options": ["in", "on", "at"], "correct": "on"},

            {"question": "We have dinner __ 7 PM.", "options": ["in", "on", "at"], "correct": "at"},

            {"question": "They got married __ 2022.", "options": ["in", "on", "at"], "correct": "in"},

            {"question": "I usually relax __ the evenings.", "options": ["in", "on", "at"], "correct": "in"},

        ],

    },

    "Future Simple": {

        "Раскрой скобки": [

            {"question": "I __ (play) football tomorrow.", "options": ["play", "plays", "will play"], "correct": "will play"},

            {"question": "She __ (not go) to the party.", "options": ["doesn't go", "won't go", "isn't going"], "correct": "won't go"},

            {"question": "__ you __ (help) me with my homework?\n\nВыбери правильную форму:", "options": ["Will ... help", "Do ... help", "Are ... helping"], "correct": "Will ... help"},

            {"question": "They __ (visit) their grandparents next week.", "options": ["visit", "visits", "will visit"], "correct": "will visit"},

            {"question": "He __ (not watch) this film.", "options": ["doesn't watch", "won't watch", "isn't watching"], "correct": "won't watch"},

            {"question": "__ we __ (see) them at the cinema?\n\nВыбери правильную форму:", "options": ["Will ... see", "Do ... see", "Are ... seeing"], "correct": "Will ... see"},

        ],

        "Выбери правильный вариант": [

            {"question": "I think it __ tomorrow.", "options": ["will snow", "snows", "is snowing"], "correct": "will snow"},

            {"question": "__ you come to my birthday party?", "options": ["Will", "Do", "Are"], "correct": "Will"},

            {"question": "They __ finish their project today.", "options": ["won't", "don't", "aren't"], "correct": "won't"},

            {"question": "My brother __ 15 next month.", "options": ["will be", "is", "was"], "correct": "will be"},

            {"question": "__ she help us with the cleaning?", "options": ["Will", "Does", "Is"], "correct": "Will"},

        ],

        "Заполни пропуски": [

            {"question": "I __ to the city centre tomorrow.\n(go / study / clean / ride / play / call / wear / eat)", "options": ["will go", "will study", "will play"], "correct": "will go"},

            {"question": "We __ badminton in the evening.\n(go / study / clean / ride / play / call / wear / eat)", "options": ["will play", "will go", "will eat"], "correct": "will play"},

            {"question": "Nancy __ her room on Sunday.\n(go / study / clean / ride / play / call / wear / eat)", "options": ["will clean", "will study", "will wear"], "correct": "will clean"},

            {"question": "Kate __ her dress to the party.\n(go / study / clean / ride / play / call / wear / eat)", "options": ["will wear", "will clean", "will ride"], "correct": "will wear"},

            {"question": "I __ you in 15 minutes.\n(go / study / clean / ride / play / call / wear / eat)", "options": ["will call", "will speak", "will go"], "correct": "will call"},

            {"question": "He __ a bicycle in the afternoon.\n(go / study / clean / ride / play / call / wear / eat)", "options": ["will ride", "will go", "will play"], "correct": "will ride"},

            {"question": "For dinner we __ pasta.\n(go / study / clean / ride / play / call / wear / eat)", "options": ["will eat", "will clean", "will wear"], "correct": "will eat"},

        ],

    },

    "Countable/Uncountable": {

        "Вставь: much, many, a lot of, a few, a little": [

            {"question": "There are too __ students in this class.", "options": ["much", "many", "a little"], "correct": "many"},

            {"question": "We have __ time before the lesson starts.", "options": ["many", "a few", "a little"], "correct": "a little"},

            {"question": "I need __ help with my homework.", "options": ["many", "a few", "a little"], "correct": "a little"},

            {"question": "There are __ good films in the cinema now.", "options": ["much", "a few", "a little"], "correct": "a few"},

            {"question": "She has __ friends at school.", "options": ["much", "many", "a little"], "correct": "many"},

        ],

        "Выбери правильный вариант": [

            {"question": "Can I have __ water, please?", "options": ["a", "some"], "correct": "some"},

            {"question": "There are __ books on the table.", "options": ["much", "many"], "correct": "many"},

            {"question": "We don't have __ time.", "options": ["many", "much"], "correct": "much"},

            {"question": "I need __ new furniture for my room.", "options": ["a", "some"], "correct": "some"},

            {"question": "There is __ milk in the fridge.", "options": ["a few", "a little"], "correct": "a little"},

            {"question": "She has __ friends.", "options": ["a lot of", "much"], "correct": "a lot of"},

            {"question": "We bought __ bread for dinner.", "options": ["a", "some"], "correct": "some"},

            {"question": "There are __ apples in the basket.", "options": ["a few", "a little"], "correct": "a few"},

        ],

        "Выбери правильный вопрос": [

            {"question": "We have some milk.\n\nВыбери правильный вопрос:", "options": ["How much milk do you have?", "How many milk do you have?"], "correct": "How much milk do you have?"},

            {"question": "I need three apples.\n\nВыбери правильный вопрос:", "options": ["How much apples do you need?", "How many apples do you need?"], "correct": "How many apples do you need?"},

            {"question": "There is a lot of sugar in the kitchen.\n\nВыбери правильный вопрос:", "options": ["How much sugar is there?", "How many sugar is there?"], "correct": "How much sugar is there?"},

            {"question": "She has two brothers.\n\nВыбери правильный вопрос:", "options": ["How much brothers does she have?", "How many brothers does she have?"], "correct": "How many brothers does she have?"},

        ],

    },

    "Question": {

        "Выбери правильное начало вопроса": [

            {"question": "__ you play football or baseball?", "options": ["Do", "Does"], "correct": "Do"},

            {"question": "__ your favourite colour red or blue?", "options": ["Is", "Are"], "correct": "Is"},

            {"question": "__ they watch a film or read a book yesterday?", "options": ["Did", "Do"], "correct": "Did"},

            {"question": "__ his birthday in June or July?", "options": ["Am", "Is"], "correct": "Is"},

        ],

    },
    "Modal verbs": {

        "Выбери правильный вариант": [

            {"question": "I __ swim when I was 5 years old.", "options": ["can", "could", "should"], "correct": "could"},

            {"question": "You __ eat more vegetables.", "options": ["must", "should", "would"], "correct": "should"},

            {"question": "__ we go to the cinema today?", "options": ["Shall", "Can", "Must"], "correct": "Shall"},

        ],

        "Построй вопрос с модальным глаголом": [

            {"question": "you / speak / English\n\nВыбери правильный вопрос:", "options": ["Can you speak English?", "Do you speak English?", "You can speak English?"], "correct": "Can you speak English?"},

            {"question": "we / meet / tomorrow\n\nВыбери правильный вопрос:", "options": ["Shall we meet tomorrow?", "Do we meet tomorrow?", "We shall meet tomorrow?"], "correct": "Shall we meet tomorrow?"},

            {"question": "I / help / you\n\nВыбери правильный вопрос:", "options": ["Can I help you?", "Do I help you?", "I can help you?"], "correct": "Can I help you?"},

            {"question": "they / come / to the party\n\nВыбери правильный вопрос:", "options": ["Can they come to the party?", "Do they come to the party?", "They can come to the party?"], "correct": "Can they come to the party?"},

        ],

    },
    "Present Simple": {

        "Выбери правильный вариант": [

            {"question": "My brother __ the guitar.", "options": ["play", "plays"], "correct": "plays"},

            {"question": "They __ like pizza.", "options": ["don't", "doesn't"], "correct": "don't"},

            {"question": "__ she go to school every day?", "options": ["Does", "Do"], "correct": "Does"},

        ],

        "Раскрой скобки": [

            {"question": "He __ (to work) in a shop.", "options": ["work", "works", "worked"], "correct": "works"},

            {"question": "I __ (not to watch) TV in the morning.", "options": ["don't watch", "doesn't watch", "didn't watch"], "correct": "don't watch"},

            {"question": "__ (you to like) ice cream?\n\nВыбери правильную форму:", "options": ["Do you like", "Does you like", "Did you like"], "correct": "Do you like"},

        ],

        "Составь предложение из слов": [

            {"question": "usually / at 7 o'clock / I / get up\n\nВыбери правильное предложение:", "options": ["I usually get up at 7 o'clock.", "Usually I am get up at 7 o'clock.", "I get usually up at 7 o'clock."], "correct": "I usually get up at 7 o'clock."},

            {"question": "never / her room / She / cleans\n\nВыбери правильное предложение:", "options": ["She never cleans her room.", "Never she cleans her room.", "She cleans never her room."], "correct": "She never cleans her room."},

            {"question": "they / Do / often / to the cinema / go\n\nВыбери правильное предложение:", "options": ["Do they often go to the cinema?", "Do they go often to the cinema?", "Often do they go to the cinema?"], "correct": "Do they often go to the cinema?"},

        ],

    },
    "Singular and plural": {

        "Поставь во множественное число": [

            {"question": "There are many (cup) __ on the table.", "options": ["cups", "cupes", "cupps"], "correct": "cups"},

            {"question": "I have two (dog) __.", "options": ["dogs", "doges", "dogges"], "correct": "dogs"},

            {"question": "The (teacher) __ are in the classroom.", "options": ["teachers", "teacheres", "teachs"], "correct": "teachers"},

        ],

        "Преобразуй слово в скобках": [

            {"question": "Many European (city) __ are very old.", "options": ["citys", "cities", "cityes"], "correct": "cities"},

            {"question": "In the story, the (princess) __ lived in a big castle.", "options": ["princess", "princesses", "princessies"], "correct": "princesses"},

            {"question": "Their (army) __ always win.", "options": ["armys", "armies", "armyes"], "correct": "armies"},

        ],

        "Выбери правильный вариант": [

            {"question": "We saw 3 __ in the forest.", "options": ["foxs", "foxes"], "correct": "foxes"},

            {"question": "Mom bought fresh __ for the salad.", "options": ["tomatos", "tomatoes"], "correct": "tomatoes"},

            {"question": "Make a wish and blow out the __ on your birthday cake.", "options": ["candies", "candis"], "correct": "candies"},

        ],

    },
    "Present Perfect": {

        "Вставь have / has": [

            {"question": "I __ never been to Paris.", "options": ["have", "has"], "correct": "have"},

            {"question": "She __ already done her exercises.", "options": ["have", "has"], "correct": "has"},

            {"question": "They __ just finished dinner.", "options": ["have", "has"], "correct": "have"},

            {"question": "My brother __ bought a new bike.", "options": ["have", "has"], "correct": "has"},

        ],

        "Поставь глагол в V3": [

            {"question": "I have __ (finish) my work.", "options": ["finish", "finished", "finishing"], "correct": "finished"},

            {"question": "He has __ (write) a letter.", "options": ["write", "wrote", "written"], "correct": "written"},

            {"question": "They have __ (see) this film.", "options": ["see", "saw", "seen"], "correct": "seen"},

            {"question": "She has __ (break) her favourite cup.", "options": ["break", "broke", "broken"], "correct": "broken"},

        ],

        "Составь предложение в Present Perfect": [

            {"question": "I / lose / my keys\n\nВыбери правильное предложение:", "options": ["I have lost my keys.", "I lost my keys.", "I am losing my keys."], "correct": "I have lost my keys."},

            {"question": "He / not / do / his homework\n\nВыбери правильное предложение:", "options": ["He hasn't done his homework.", "He didn't do his homework.", "He doesn't do his homework."], "correct": "He hasn't done his homework."},

            {"question": "You / ever / be / to London?\n\nВыбери правильное предложение:", "options": ["Have you ever been to London?", "Did you ever go to London?", "Are you ever been to London?"], "correct": "Have you ever been to London?"},

        ],

    },
    "Linking verbs": {

        "Выбери правильный вспомогательный глагол": [

            {"question": "__ you like chocolate?", "options": ["Do", "Does", "Is", "Have"], "correct": "Do"},

            {"question": "__ they sleeping now?", "options": ["Do", "Are", "Was", "Have"], "correct": "Are"},

            {"question": "__ they at the cinema yesterday?", "options": ["Was", "Were", "Are", "Have"], "correct": "Were"},

            {"question": "She __ not finished her tour.", "options": ["do", "does", "is", "has"], "correct": "has"},

        ],

    },


    "Stative Verbs": {
        "Раскрой скобки": [
            {
                "question": "I **(like)** ice cream.",
                "options": ["like", "am liking", "likes"],
                "correct": "like"
            },
            {
                "question": "She **(have)** a shower now.",
                "options": ["has", "is having", "having"],
                "correct": "is having"
            },
            {
                "question": "They **(know)** the answer.",
                "options": ["know", "are knowing", "knows"],
                "correct": "know"
            },
            {
                "question": "Listen! He **(play)** the guitar.",
                "options": ["plays", "is playing", "play"],
                "correct": "is playing"
            },
            {
                "question": "I **(think)** it is a great idea.",
                "options": ["think", "am thinking", "thinks"],
                "correct": "think"
            }
        ]
    },
    "Passive Voice": {
        "Раскрой скобки": [
            {
                "question": "The new school **(build)** in our town next year.",
                "options": ["will be built", "is built", "will build"],
                "correct": "will be built"
            },
            {
                "question": "This beautiful song **(write)** by a famous composer in the 19th century.",
                "options": ["was written", "is written", "wrote"],
                "correct": "was written"
            },
            {
                "question": "Coffee **(grow)** in Brazil.",
                "options": ["is grown", "are grown", "grows"],
                "correct": "is grown"
            },
            {
                "question": "The keys **(lose)** by him yesterday.",
                "options": ["were lost", "was lost", "lost"],
                "correct": "were lost"
            },
            {
                "question": "The homework **(do)** by me every day.",
                "options": ["is done", "are done", "is do"],
                "correct": "is done"
            }
        ],
        "Выбери правильную форму": [
            {
                "question": "The window is ___ every morning.",
                "options": ["open", "opened"],
                "correct": "opened"
            },
            {
                "question": "Milk is ___ to make this cake.",
                "options": ["use", "used"],
                "correct": "used"
            },
            {
                "question": "These books are ___ in the library.",
                "options": ["sell", "sold"],
                "correct": "sold"
            },
            {
                "question": "I am ___ by my friends every day.",
                "options": ["call", "called"],
                "correct": "called"
            },
            {
                "question": "English is ___ in many countries.",
                "options": ["speak", "spoken"],
                "correct": "spoken"
            }
        ]
    },
    "Conditionals": {
        "Zero Conditional (feel, boil, get)": [
            {
                "question": "If you touch fire, you ___ burned.",
                "options": ["get", "gets", "got"],
                "correct": "get"
            },
            {
                "question": "If water reaches 100 degrees, it ___.",
                "options": ["boil", "boils", "boiling"],
                "correct": "boils"
            },
            {
                "question": "If you don't sleep well, you ___ tired.",
                "options": ["feel", "feels", "feeling"],
                "correct": "feel"
            }
        ],
        "Second Conditional": [
            {
                "question": "If I had a magic wand, I ___ **(become)** a superhero.",
                "options": ["would become", "become", "will become"],
                "correct": "would become"
            },
            {
                "question": "I ___ **(travel)** around the world if I had a lot of money.",
                "options": ["would travel", "traveled", "will travel"],
                "correct": "would travel"
            },
            {
                "question": "If I ___ **(can)** speak all languages, I would have friends everywhere.",
                "options": ["could", "can", "would can"],
                "correct": "could"
            }
        ]
    },
    "Gerund vs Infinitive": {
        "Вставь нужную форму": [
            {
                "question": "I want ___ **(buy)** a new phone.",
                "options": ["to buy", "buying", "buy"],
                "correct": "to buy"
            },
            {
                "question": "She enjoys ___ **(dance)** at parties.",
                "options": ["dancing", "to dance", "dance"],
                "correct": "dancing"
            },
            {
                "question": "He can ___ **(speak)** three languages.",
                "options": ["speak", "to speak", "speaking"],
                "correct": "speak"
            },
            {
                "question": "We decided ___ **(go)** to the cinema.",
                "options": ["to go", "going", "go"],
                "correct": "to go"
            },
            {
                "question": "Let me ___ **(help)** you.",
                "options": ["help", "to help", "helping"],
                "correct": "help"
            },
            {
                "question": "It is important ___ **(drink)** water.",
                "options": ["to drink", "drinking", "drink"],
                "correct": "to drink"
            },
            {
                "question": "I saw him ___ **(cross)** the street.",
                "options": ["cross", "to cross", "crossed"],
                "correct": "cross"
            }
        ],
        "Выбери вариант": [
            {
                "question": "I hope ___ you soon.",
                "options": ["to see", "seeing"],
                "correct": "to see"
            },
            {
                "question": "He suggested ___ to the museum.",
                "options": ["going", "to go"],
                "correct": "going"
            },
            {
                "question": "You must ___ your work.",
                "options": ["finish", "to finish"],
                "correct": "finish"
            },
            {
                "question": "She is good at ___.",
                "options": ["drawing", "to draw"],
                "correct": "drawing"
            },
            {
                "question": "They made us ___ for an hour.",
                "options": ["wait", "to wait"],
                "correct": "wait"
            }
        ]
    },
    "Past Perfect Continuous": {
        "Раскрой скобки": [
            {
                "question": "They ___ **(wait)** for the bus for 30 minutes when it finally arrived.",
                "options": ["had been waiting", "have been waiting", "were waiting"],
                "correct": "had been waiting"
            },
            {
                "question": "She was crying because she ___ **(watch)** a sad film.",
                "options": ["had been watching", "was watching", "has been watching"],
                "correct": "had been watching"
            },
            {
                "question": "How long ___ you ___ **(study)** English before you moved to London?",
                "options": ["had ... been studying", "have ... been studying", "did ... study"],
                "correct": "had ... been studying"
            }
        ]
    },
    "Past Perfect": {
        "Past Perfect vs Past Simple": [
            {
                "question": "She was sad because she ___ **(lose)** her favourite book.",
                "options": ["had lost", "lost", "has lost"],
                "correct": "had lost"
            },
            {
                "question": "They ___ **(not do)** their project, so the teacher was angry.",
                "options": ["had not done", "did not do", "haven't done"],
                "correct": "had not done"
            },
            {
                "question": "After the rain ___ **(stop)**, we ___ **(go)** for a walk.",
                "options": ["had stopped / went", "stopped / had gone", "had been stopping / went"],
                "correct": "had stopped / went"
            }
        ]
    },
    "Past Perfect vs PPC": {
        "Выбери правильный вариант": [
            {
                "question": "Her eyes were red because she ___.",
                "options": ["had been crying", "had cried"],
                "correct": "had been crying"
            },
            {
                "question": "They ___ the house for two years before they sold it.",
                "options": ["had been building", "had built"],
                "correct": "had been building"
            },
            {
                "question": "He was tired because he ___ in the garden all day.",
                "options": ["had been working", "had worked"],
                "correct": "had been working"
            },
            {
                "question": "She ___ three letters by 5 o'clock.",
                "options": ["had written", "had been writing"],
                "correct": "had written"
            }
        ],
        "Мини-история про Сару": [
            {
                "question": "Her friends were surprised because they ___ **(wait)** for her for an hour.",
                "options": ["had been waiting", "had waited", "were waiting"],
                "correct": "had been waiting"
            },
            {
                "question": "The room was very clean – her mum ___ **(clean)** it all evening.",
                "options": ["had been cleaning", "had cleaned", "was cleaning"],
                "correct": "had been cleaning"
            },
            {
                "question": "She felt bad because she ___ **(not / finish)** her homework.",
                "options": ["had not finished", "had not been finishing", "didn't finish"],
                "correct": "had not finished"
            },
            {
                "question": "She was happy to see that her best friend ___ **(make)** a card for her.",
                "options": ["had made", "had been making", "was making"],
                "correct": "had made"
            }
        ]
    },

    "Future Simple & Constructions": {
        "Present Continuous vs Be going to": [
            {
                "question": "A: What are your plans for the summer?\nB: I ___ **(travel)** to Italy. I've already booked the hotel.",
                "options": ["am travelling", "am going to travel"],
                "correct": "am travelling"
            },
            {
                "question": "A: Do you want to go to the cinema tonight?\nB: I can't. I ___ **(meet)** my friend for coffee at 7 p.m.",
                "options": ["am meeting", "am going to meet"],
                "correct": "am meeting"
            },
            {
                "question": "Look at that car! It's driving too fast! It ___ **(crash)**!",
                "options": ["is going to crash", "is crashing"],
                "correct": "is going to crash"
            },
            {
                "question": "I ___ **(learn)** how to drive. I've saved some money for the lessons.",
                "options": ["am going to learn", "am learning"],
                "correct": "am going to learn"
            }
        ],
        "Will vs Be going to": [
            {
                "question": "Look at those dark clouds! I think it ___ rain.",
                "options": ["is going to", "will"],
                "correct": "is going to"
            },
            {
                "question": "I don't have any plans for the weekend. Maybe I ___ read a book.",
                "options": ["will", "am going to"],
                "correct": "will"
            },
            {
                "question": "She has bought the tickets. She ___ visit her grandparents in Moscow next month.",
                "options": ["is going to", "will"],
                "correct": "is going to"
            },
            {
                "question": "The phone is ringing! I ___ answer it.",
                "options": ["will", "is going to"],
                "correct": "will"
            },
            {
                "question": "I'm sure you ___ enjoy the film.",
                "options": ["will", "are going to"],
                "correct": "will"
            }
        ],
        "Future Simple: формы (+, -, ?)": [
            {
                "question": "He **(to pass)** the exam. He didn't study at all. (-)",
                "options": ["won't pass", "will not to pass", "doesn't pass"],
                "correct": "won't pass"
            },
            {
                "question": "___ you **(to help)** me with this heavy box? (?)",
                "options": ["Will ... help", "Do ... help", "Will ... helping"],
                "correct": "Will ... help"
            },
            {
                "question": "They **(to arrive)** at 8 p.m. (+)",
                "options": ["will arrive", "arrives", "will arriving"],
                "correct": "will arrive"
            },
            {
                "question": "She **(to forget)** about your promise. (-)",
                "options": ["won't forget", "will not forgets", "isn't forget"],
                "correct": "won't forget"
            }
        ]
    },
    "The (exceptions)": {
        "Вставь артикль THE": [
            {
                "question": "___ Moon is bright tonight.",
                "options": ["The", "–"],
                "correct": "The"
            },
            {
                "question": "They play ___ tennis every weekend.",
                "options": ["the", "–"],
                "correct": "–"
            },
            {
                "question": "We visited ___ Hermitage Museum.",
                "options": ["the", "–"],
                "correct": "the"
            },
            {
                "question": "She speaks ___ Chinese very well.",
                "options": ["the", "–"],
                "correct": "–"
            },
            {
                "question": "___ Urals are between Europe and Asia.",
                "options": ["The", "–"],
                "correct": "The"
            }
        ],
        "Выбери правильный вариант": [
            {
                "question": "My brother is in ___ hospital with appendicitis.",
                "options": ["the", "–"],
                "correct": "–"
            },
            {
                "question": "___ poor need our help.",
                "options": ["The", "–"],
                "correct": "The"
            },
            {
                "question": "We crossed ___ Atlantic Ocean.",
                "options": ["the", "–"],
                "correct": "the"
            },
            {
                "question": "He became ___ president of the company.",
                "options": ["the", "–"],
                "correct": "–"
            },
            {
                "question": "I read ___ Times every morning.",
                "options": ["the", "–"],
                "correct": "the"
            }
        ]
    },
    "Reported Speech": {
        "Косвенная речь (Commands)": [
            {
                "question": "\"Please, help me with this bag.\" (he / to his friend)",
                "options": ["He asked his friend to help him.", "He asked his friend help him.", "He told his friend to help him."],
                "correct": "He asked his friend to help him."
            },
            {
                "question": "\"Don't run in the corridor!\" (The teacher / to the students)",
                "options": ["The teacher told the students not to run.", "The teacher told the students don't run.", "The teacher asked the students not run."],
                "correct": "The teacher told the students not to run."
            },
            {
                "question": "\"Call me tonight.\" (She / to him)",
                "options": ["She told him to call her.", "She asked him call her.", "She told him to call me."],
                "correct": "She told him to call her."
            },
            {
                "question": "\"Please, don't tell anyone my secret.\" (My sister / to me)",
                "options": ["My sister asked me not to tell anyone her secret.", "My sister told me to not tell anyone her secret.", "My sister asked me don't tell anyone her secret."],
                "correct": "My sister asked me not to tell anyone her secret."
            }
        ]
    },
    "Past Simple vs Past Continuous": {
        "Выбери правильный вариант": [
            {
                "question": "I ___ TV at 8 pm yesterday.",
                "options": ["was watching", "watched"],
                "correct": "was watching"
            },
            {
                "question": "They ___ tennis when it ___ to rain.",
                "options": ["were playing / started", "played / was starting", "were playing / was starting"],
                "correct": "were playing / started"
            },
            {
                "question": "While he ___ to work, he ___ an accident.",
                "options": ["was driving / had", "drove / was having", "was driving / was having"],
                "correct": "was driving / had"
            }
        ],
        "Раскрой скобки": [
            {
                "question": "When I ___ **(come)** home, my brother ___ **(do)** his homework.",
                "options": ["came / was doing", "was coming / did", "came / did"],
                "correct": "came / was doing"
            },
            {
                "question": "She ___ **(cook)** dinner while her children ___ **(play)** in the garden.",
                "options": ["was cooking / were playing", "cooked / played", "was cooking / played"],
                "correct": "was cooking / were playing"
            },
            {
                "question": "We ___ **(walk)** in the park when we ___ **(meet)** our friends.",
                "options": ["were walking / met", "walked / were meeting", "walked / met"],
                "correct": "were walking / met"
            },
            {
                "question": "He ___ **(break)** his leg while he ___ **(ski)** in the mountains.",
                "options": ["broke / was skiing", "was breaking / skied", "broke / skied"],
                "correct": "broke / was skiing"
            },
            {
                "question": "They ___ **(have)** dinner when the phone ___ **(ring)**.",
                "options": ["were having / rang", "had / was ringing", "were having / was ringing"],
                "correct": "were having / rang"
            }
        ]
    },
    "Present Perfect": {
        "Форма глагола": [
            {
                "question": "I ___ **(finish)** my homework.",
                "options": ["have finished", "has finished", "finished"],
                "correct": "have finished"
            },
            {
                "question": "She ___ **(not see)** this film yet.",
                "options": ["hasn't seen", "haven't seen", "hasn't saw"],
                "correct": "hasn't seen"
            },
            {
                "question": "They ___ **(buy)** a new car.",
                "options": ["have bought", "has bought", "have buyed"],
                "correct": "have bought"
            },
            {
                "question": "He ___ **(never visit)** London.",
                "options": ["has never visited", "have never visited", "never visited"],
                "correct": "has never visited"
            },
            {
                "question": "We ___ **(just eat)** dinner.",
                "options": ["have just eaten", "has just eaten", "have just ate"],
                "correct": "have just eaten"
            }
        ],
        "Маркеры времени": [
            {
                "question": "I have ___ done my exercises.",
                "options": ["already", "yet", "ever"],
                "correct": "already"
            },
            {
                "question": "Have you ___ been to Paris?",
                "options": ["ever", "never", "yet"],
                "correct": "ever"
            },
            {
                "question": "She hasn't called us ___.",
                "options": ["yet", "already", "just"],
                "correct": "yet"
            },
            {
                "question": "They have ___ returned from school.",
                "options": ["just", "yet", "ever"],
                "correct": "just"
            },
            {
                "question": "He has ___ tried sushi in his life.",
                "options": ["never", "ever", "yet"],
                "correct": "never"
            }
        ]
    },
    "Present Perfect Continuous": {
        "Утверждение": [
            {
                "question": "I ___ **(wait)** for the bus for 20 minutes.",
                "options": ["have been waiting", "has been waiting", "am waiting"],
                "correct": "have been waiting"
            },
            {
                "question": "She ___ **(study)** for her exam all week.",
                "options": ["has been studying", "have been studying", "was studying"],
                "correct": "has been studying"
            },
            {
                "question": "They ___ **(play)** football since 3 o'clock.",
                "options": ["have been playing", "has been playing", "were playing"],
                "correct": "have been playing"
            },
            {
                "question": "He ___ **(work)** at this company for five years.",
                "options": ["has been working", "have been working", "is working"],
                "correct": "has been working"
            }
        ],
        "Отрицание": [
            {
                "question": "I ___ **(wait)** for the bus for 20 minutes. (-)",
                "options": ["haven't been waiting", "hasn't been waiting", "don't been waiting"],
                "correct": "haven't been waiting"
            },
            {
                "question": "She ___ **(study)** for her exam all week. (-)",
                "options": ["hasn't been studying", "haven't been studying", "wasn't studying"],
                "correct": "hasn't been studying"
            },
            {
                "question": "They ___ **(play)** football since 3 o'clock. (-)",
                "options": ["haven't been playing", "hasn't been playing", "aren't playing"],
                "correct": "haven't been playing"
            },
            {
                "question": "He ___ **(work)** at this company for five years. (-)",
                "options": ["hasn't been working", "haven't been working", "doesn't been working"],
                "correct": "hasn't been working"
            }
        ]
    },
    "Gerund/Infinitive both": {
        "Выбери правильный перевод": [
            {
                "question": "Не забудь купить сладостей.",
                "options": ["Remember to buy sweets.", "Remember buying sweets."],
                "correct": "Remember to buy sweets."
            },
            {
                "question": "Я забыл, что оставил пальто у тебя.",
                "options": ["I forgot leaving my coat at your place.", "I forgot to leave my coat at your place."],
                "correct": "I forgot leaving my coat at your place."
            }
        ],
        "Определи верное значение": [
            {
                "question": "She stopped to talk.",
                "options": ["Она остановилась поговорить.", "Она замолчала."],
                "correct": "Она остановилась поговорить."
            },
            {
                "question": "Did you remember to water the flowers?",
                "options": ["Ты полил цветы? (вспомнил ли сделать это?)", "Ты поливаешь цветы?"],
                "correct": "Ты полил цветы? (вспомнил ли сделать это?)"
            },
            {
                "question": "The phone did not work, so I tried restarting it.",
                "options": ["Я попробовал перезапустить его (как способ).", "Я попробовал его перезапустить (приложил усилия)."],
                "correct": "Я попробовал перезапустить его (как способ)."
            }
        ]
    }
}


BASE_DIR = os.path.dirname(os.path.abspath(__file__))

theory_by_topic = {
    "Article": os.path.join(BASE_DIR, "images", "article.png"),
    "Present Continuous": os.path.join(BASE_DIR, "images", "pres_cont.png"),
    "Comparisons": os.path.join(BASE_DIR, "images", "comparison.png"),
    "Prepositions of time": os.path.join(BASE_DIR, "images", "prep_of_time.png"),
    "Future Simple": os.path.join(BASE_DIR, "images", "future_simple.png"),
    "Countable/Uncountable": os.path.join(BASE_DIR, "images", "quantity.png"),
    "Question": os.path.join(BASE_DIR, "images", "question.png"),
    "Modal verbs": os.path.join(BASE_DIR, "images", "modals.png"),
    "Present Simple": os.path.join(BASE_DIR, "images", "pres_simple.png"),
    "Singular and plural": os.path.join(BASE_DIR, "images", "singular.png"),
    "Present Perfect": os.path.join(BASE_DIR, "images", "pres_perfect.png"),
    "Linking verbs": os.path.join(BASE_DIR, "images", "linking.png"),
    "Stative Verbs": os.path.join(BASE_DIR, "images", "stative.png"),
    "Passive Voice": os.path.join(BASE_DIR, "images", "passive.png"),
    "Conditionals": os.path.join(BASE_DIR, "images", "conditionals.png"),
    "Gerund vs Infinitive": os.path.join(BASE_DIR, "images", "gerund_vs.png"),
    "Past Perfect Continuous": os.path.join(BASE_DIR, "images", "past_perf_cont.png"),
    "Past Perfect": os.path.join(BASE_DIR, "images", "past_perf.png"),
    "Past Perfect vs PPC": os.path.join(BASE_DIR, "images", "past_perf_vs.png"),
    "Future Simple & Constructions": os.path.join(BASE_DIR, "images", "fut_simple_const.png"),
    "The (exceptions)": os.path.join(BASE_DIR, "images", "the.png"),
    "Reported Speech": os.path.join(BASE_DIR, "images", "reported.png"),
    "Past Simple vs Past Continuous": os.path.join(BASE_DIR, "images", "past_simple_vs.png"),
    "Present Perfect": os.path.join(BASE_DIR, "images", "pres_perf.png"),
    "Present Perfect Continuous": os.path.join(BASE_DIR, "images", "pres_perf_cont.png"),
    "Gerund/Infinitive both": os.path.join(BASE_DIR, "images", "gerund_inf.png")
}



# --- ВСПОМОГАТЕЛЬНЫЕ ФУНКЦИИ ---


def get_topics_kb(class_name):

    buttons = [[KeyboardButton(text=t)] for t in topics[class_name]]

    buttons.append([KeyboardButton(text="⬅️ Назад")])

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)



def get_subtopics_kb(topic):

    """🆕 Клавиатура с подразделами для выбранной темы"""

    subtopics = list(tasks_by_topic.get(topic, {}).keys())

    buttons = [[KeyboardButton(text=s)] for s in subtopics]

    buttons.append([KeyboardButton(text="⬅️ Назад")])

    return ReplyKeyboardMarkup(keyboard=buttons, resize_keyboard=True)


async def send_task(message, user_id):

    topic = user_topic[user_id]

    subtopic = user_subtopic[user_id]

 

    tasks = tasks_by_topic.get(topic, {}).get(subtopic, [])

    if not tasks:

        await message.answer("Для этого раздела пока нет заданий")

        return

 

    task = tasks[current_task[user_id]]

    kb = ReplyKeyboardMarkup(

        keyboard=[[KeyboardButton(text=opt)] for opt in task["options"]] +

                 [[KeyboardButton(text="➡️ Следующее"), KeyboardButton(text="⬅️ Назад")]],

        resize_keyboard=True

    )

    await message.answer(task["question"], reply_markup=kb)





# --- ХЕНДЛЕРЫ ---

@dp.message(lambda message: message.text == "/start")

async def start(message: types.Message):

    await message.answer("Привет! 👋 Выбери класс:", reply_markup=class_kb)


# 1. ВЫБОР КЛАССА
@dp.message(lambda m: m.text in ["5-6 класс", "7-9 класс"])
async def choose_class(message: types.Message):
    user_id = message.from_user.id
    # Сбрасываем всё старое состояние при смене класса
    user_mode.pop(user_id, None)
    user_topic.pop(user_id, None)
    user_subtopic.pop(user_id, None)
    current_task.pop(user_id, None)
    user_class[user_id] = message.text.replace(" класс", "")
    await message.answer("Выбери режим:", reply_markup=mode_kb)
 
# 2. ВЫБОР РЕЖИМА
@dp.message(lambda m: m.text in ["📘 Теория", "📝 Практика"])
async def choose_mode(message: types.Message):
    user_id = message.from_user.id
    if user_id not in user_class:
        return
    # Сбрасываем тему и подраздел при смене режима
    user_topic.pop(user_id, None)
    user_subtopic.pop(user_id, None)
    current_task.pop(user_id, None)
    user_mode[user_id] = "theory" if "Теория" in message.text else "practice"
    await message.answer("Выбери тему:", reply_markup=get_topics_kb(user_class[user_id]))



# 3. НАЗАД

@dp.message(lambda m: m.text == "⬅️ Назад")
async def back(message: types.Message):
    user_id = message.from_user.id
    
    # ПРОВЕРКА: Если данных о пользователе вообще нет (сервер перезагрузился)
    if user_id not in user_class:
        await message.answer("Сессия истекла. Начни со старта!", reply_markup=class_kb)
        return

    if user_id in current_task:
        del current_task[user_id]
        user_subtopic.pop(user_id, None) # Используем pop вместо del для безопасности
        await message.answer("Выбери подраздел:", reply_markup=get_subtopics_kb(user_topic[user_id]))

    elif user_id in user_subtopic:
        del user_subtopic[user_id]
        await message.answer("Выбери тему:", reply_markup=get_topics_kb(user_class[user_id]))

    elif user_id in user_topic:
        del user_topic[user_id]
        # Безопасно получаем класс
        cls = user_class.get(user_id, "5-6") 
        await message.answer("Выбери тему:", reply_markup=get_topics_kb(cls))

    elif user_id in user_mode:
        del user_mode[user_id]
        await message.answer("Выбери режим:", reply_markup=mode_kb)

    else:
        # Если мы совсем запутались, возвращаем в начало
        await message.answer("Выбери класс:", reply_markup=class_kb)


# 4. СЛЕДУЮЩЕЕ ЗАДАНИЕ

@dp.message(lambda m: m.text == "➡️ Следующее")

async def next_task(message: types.Message):

    user_id = message.from_user.id

    if user_id not in current_task:

        return

 

    topic = user_topic[user_id]

    subtopic = user_subtopic[user_id]

    tasks = tasks_by_topic.get(topic, {}).get(subtopic, [])

 

    if not tasks:

        await message.answer("Для этого раздела пока нет заданий.")

        return

 

    current_task[user_id] += 1

 

    if current_task[user_id] >= len(tasks):

        # Задания в подразделе закончились → возврат к выбору подраздела

        del current_task[user_id]
        del user_subtopic[user_id]

        await message.answer(

            "🎉 Все задания в этом разделе выполнены!\n\nВыбери другой подраздел:",

            reply_markup=get_subtopics_kb(topic)

        )

        return

 

    await send_task(message, user_id)



# 5. ПРОВЕРКА ОТВЕТА

@dp.message(lambda m: m.from_user.id in current_task)

async def check_answer(message: types.Message):

    user_id = message.from_user.id

    topic = user_topic[user_id]

    subtopic = user_subtopic[user_id]

    index = current_task[user_id]

    task = tasks_by_topic[topic][subtopic][index]

 

    if message.text == task["correct"]:

        await message.answer("✅ Правильно!")

    elif message.text in task["options"]:

        await message.answer("❌ Неправильно")

 

 

# 6. ВЫБОР ТЕМЫ ИЛИ ПОДРАЗДЕЛА (должен быть последним!)

@dp.message()

async def choose_topic_or_subtopic(message: types.Message):

    user_id = message.from_user.id

 

    if user_id not in user_class:

        return

 

    class_name = user_class[user_id]

 

    # Тема ещё не выбрана → выбираем тему

    if user_id not in user_topic:

        if message.text not in topics[class_name]:

            return

        user_topic[user_id] = message.text

 

        if user_mode.get(user_id) == "theory":

            if message.text not in theory_by_topic:

                del user_topic[user_id]

                await message.answer("Теория пока не добавлена для этой темы.")

                return

            photo_path = theory_by_topic[message.text]
            
            # Создаем объект файла
            photo = FSInputFile(photo_path)
            
            del user_topic[user_id]

            # Отправляем фото вместо текста
            await message.answer_photo(photo=photo, caption=f"📘 Теория по теме: {message.text}")

        else:

            subtopics = list(tasks_by_topic.get(message.text, {}).keys())

            if not subtopics:

                del user_topic[user_id]

                await message.answer("Для этой темы пока нет заданий.")

                return

            await message.answer("Выбери подраздел:", reply_markup=get_subtopics_kb(message.text))

        return

 

    # Тема выбрана, но подраздел ещё не выбран → выбираем подраздел

    if user_id not in user_subtopic:

        topic = user_topic[user_id]

        subtopics = list(tasks_by_topic.get(topic, {}).keys())

        if message.text not in subtopics:

            return

        user_subtopic[user_id] = message.text

        current_task[user_id] = 0

        await send_task(message, user_id)

        return


# --- ЗАПУСК ---


async def on_startup(app):

    # удаляем старый webhook (на всякий)
    await bot.delete_webhook(drop_pending_updates=True)

    # ставим новый webhook

    await bot.set_webhook(WEBHOOK_URL)
    print(f"Webhook set to {WEBHOOK_URL}")


async def on_cleanup(app):
    await bot.delete_webhook()
    await bot.session.close()


app = web.Application()


# регистрируем маршрут webhook

app.router.add_get("/", healthcheck)
app.router.add_post(WEBHOOK_PATH, handle_webhook)


app.on_startup.append(on_startup)
app.on_cleanup.append(on_cleanup)


PORT = int(os.environ.get("PORT", 10000))
web.run_app(app, host="0.0.0.0", port=PORT)
