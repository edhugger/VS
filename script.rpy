# Вы можете расположить сценарий своей игры в этом файле.

# Определение персонажей игры.
define texen = Character('Тэхён', color="#9dc9a8")
define uved = Character('Уведомление', color="#f6faed")
define dokio = Character('Докио', color="#afe3d2")
define kahim = Character('Кахим', color="#84ab05")
define avtor = Character('', color="#fafcff")
define II = Character('Лиам', color="#1c3ca6")

# Вместо использования оператора image можете просто
# складывать все ваши файлы изображений в папку images.
# Например, сцену bg room можно вызвать файлом "bg room.png",
# а eileen happy — "eileen happy.webp", и тогда они появятся в игре.

# Игра начинается здесь:
label start:
    
    scene bgoffice
    
    texen "*Вздох* одно и тоже каждый день"
    
    scene bgofficekoridornight
    
    texen "Ах, сколько время? Все ушли домой"
    
    texen "Кажется, я задержался, пора уходить"
    
    uved "*Звук уведомления*"

    scene nout
    
    uved "Опрос"
    
    texen "Хм, рабочая почта, а присылают какой-то спам"
    
    uved "Здравствуйте, мы предлагаем вам пройти опрос для улучшения нашей компании"
    
    texen "Агрх, они же проводили опрос в прошлом году"
    
    scene stret
    
    uved "Укажите ваше имя"
    
    texen "Тэхён"
    
    scene stret1
    
    uved "Сколько Вам лет?"
    
    texen "24"
    
    scene stret2
    
    uved "В каком городе вы проживаете?"
    
    texen "Токио"
    
    scene stret3
    
    uved "Какая у Вас должность?"
    
    texen "Разработчик мобильных и программных приложений"
    
    texen "Странный вопрос, они же сами ко мне на почту отправили опрос"
    
    scene stret4
    
    uved "Спасибо за уделенное время!"
    
    texen "Теперь точно домой"
    
    scene phone
    
    uved "Зынь"
    
    dokio "Тэхён, ты где? Опаздываешь"
    
    texen "Черт, я совсем забыл, сегодня встреча с Докио и Кахимом"
    
    with fade
    
    scene cafe
    
    show dokionorm at left
    
    dokio "Тэхён, мы здесь!"
    
    hide dokionorm
    
    show tehennorm
    
    texen "Я немного задержался на работе"
    
    hide tehennorm
    
    show kahimnorm
    
    kahim "Хэ-эй, давно не виделись, Тэхён"
    
    hide kahimnorm
    
    show tehennerv
    
    texen "Сам ведь знаешь, работы много"
    
    hide tehennerv
    
    show dokionorm
    
    dokio "О боже, ты не меняешься. Сам собрал нас отметить день рождения и опоздал"
    
    hide dokionorm
    
    show kahimvesel
    
    kahim "Тэхён, ты ведь так и не нашел себе никого?"
    
    hide kahimvesel
    
    show tehennerv
    
    texen "Аа-аа, да как-то не до этого"
    
    hide tehennerv
    
    show dokionorm at left
    
    dokio "Тэхён, мы с Кахимом долго думали, что тебе подарить и нашли кое-что что должно тебя заинтересовать"
    
    avtor "*Протягивает большую коробку*"
    
    show kahimnorm at right
    
    kahim "Внутри коробки лежит полная инструкция и само устройство. Вообще, мы не до конца поняли, как оно работает, но по идее тебя должно переносить в игру. Звучит странно, но это какая-то новая разработка"
    
    hide dokionorm
    
    hide kahimnorm
    
    show tehennorm
    
    texen "Переноситься в игру? Разве, это не рекламный ход?"
    
    hide tehennorm
    
    show kahimvesel
    
    kahim "Вроде как нет, если не понравится, то мы можем вернуть её"
    
    hide kahimvesel
    
    show tehenvesel
    
    texen "Даже если не будет полного погружения, то ничего страшного, я уверен она мне понравится"
    
    hide tehenvesel
    
    avtor "*Прошло несколько часов*"
    
    show tehenvesel
    
    texen "Отлично посидели"
    
    hide tehenvesel
    
    show tehennorm
    
    texen "Мне завтра на работу, так что я пойду"
    
    hide tehennorm
    
    show dokionorm at left
    
    show kahimvesel at right
    
    kahim "Не забудь нам написать, как протестируешь игру"
    
    dokio "Нам обязательно нужно будет еще раз так собраться"
    
    hide dokionorm
    
    hide kahimvesel
    
    avtor "*Тэхён уходит*"
    
    with fade
    
    scene bgroomtehen
    
    avtor "*Тэхён приходит домой*"
    
    avtor "На следующий вечер"
    
    show texennevoz
    
    texen "Чем бы заняться...Точно, надо проверить что там за игра"
    
    avtor "Тэхён достает устройство"
    
    texen "Так-так, подключите, поставьте, проверьте устройство. Оке-ей, вроде, все работает"
    
    II "Здравствуйте, я ваш голосовой помощник Лиам"
    
    II "Вы хотите поставить ограничение времени на использование игры в день?"
    
    menu: 
        "Хм, стоит ли ставить ограничение?"
        "Да" :
            jump Yes
        "Нет" :
            jump No
    return

label Yes:
    
    II "Отлично, рекомендуемое время установлено"
    
    texen "А как мне узнать это время теперь?"
    
    II "Рекомендуемое время в сутки 3 часа"
    
    II "В течении 30 минут, ваша игра будет настроена и вы сможете начать прохождение"
    
    texen "Как долго"
    
    hide texennevoz
    
    avtor "Прошло 30 минут"
    
    II "Ваша игра настроена и готова к использованию"
    
    show tehennorm
    
    texen "А как мне играть в неё?"
    
    II "Для того, чтобы вы смогли переместиться в игру, нужно надеть шлем"
    
    hide tehennorm
    
    avtor "Тэхён надевает шлем"
    with fade
    
    scene bggame1
    
    show tehenvesel
    
    texen "Как красиво, где я?"
    
    hide tehenvesel
    
    show liamnorm
    
    II "Ты в Тетуаре, здесь возможно все, можешь летать, знакомится с другими людьми, сражаться"
    
    hide liamnorm
    
    show tehenvesel
    
    texen "Ты ведь ИИ, почему я вижу тебя?"
    
    hide tehenvesel
    
    show liamnorm
    
    II "В этом мире возможно всё, поэтому я сделала себе внешность, чтобы тебе было комфортнее меня воспринимать, если не против, то я хотела бы играть вместе с тобой"
    
    hide liamnorm
    
    show tehenvesel
    
    menu: 
        "Согласиться?"
        "Да" :
            jump YesII
        "Нет" :
            jump NoII
    
    
    return

label No:
    
    II "Отлично, вы можете находиться в игре сколько захотите"   
    
    II "В течении 30 минут, ваша игра будет настроена и вы сможете начать прохождение"
    
    texen "Как долго"
    
    hide texennevoz
    
    avtor "Прошло 30 минут"
    
    II "Ваша игра настроена и готова к использованию"
    
    show tehennorm
    
    texen "А как мне играть в неё?"
    
    II "Для того, чтобы вы смогли переместиться в игру, нужно надеть шлем"
    
    hide tehennorm
    
    avtor "Тэхён надевает шлем"
    with fade
    
    scene bggame1
    
    show tehenvesel
    
    texen "Как красиво, где я?"
    
    hide tehenvesel
    
    show liamnorm
    
    show liamnorm
    
    II "Ты в Тетуаре, здесь возможно все, можешь летать, знакомится с другими людьми, сражаться"
    
    hide liamnorm
    
    show tehenvesel
    
    texen "Ты ведь ИИ, почему я вижу тебя?"
    
    hide tehenvesel
    
    show liamnorm
    
    II "В этом мире возможно всё, поэтому я сделала себе внешность, чтобы тебе было комфортнее меня воспринимать, если не против, то я хотела бы играть вместе с тобой"
    
    hide liamnorm
    
    show tehenvesel
    
    menu: 
        "Согласиться?"
        "Да" :
            jump YesII
        "Нет" :
            jump NoII
    
    
    
    return

label YesII: 

    hide tehenvesel
    
    show liamvesel
    
    II "Ура, давай я тебе все покажу"
    
    hide liamvesel
    
    avtor "Лиам берет за руку Тэхёна и ведет по улице"
    
    scene bggameostanovka
    
    show liamnorm
    
    II "Это остановка, тут ты можешь добраться до нужной точки"
    
    scene bggamedom
    
    hide liamnorm
    
    II "Это твой дом"
    
    scene bggamedomvnutry
    
    show tehenvesel

    texen "Тут очень красиво, а мне нужно будет питаться, пить, как в реальной жизни?"
    
    hide tehenvesel
    
    show liamnorm
    
    II "На самом деле, тут уже ты решаешь. У меня есть к тебе вопрос"
    
    hide liamnorm
    
    show tehennorm
   
    texen "Что за вопрос?"
    
    hide tehennorm
    
    show liamnorm
    
    II "Можно я буду жить у тебя? Просто для меня дом не создался, как для тебя"
    
    hide liamnorm
    
    show texenudiv
    
    texen "Аа-аа, даже не знаю"
    
    menu: 
        "Согласиться?"
        "Да, пускай живет со мной" :
            jump chivet
        "Я хочу жить один" :
            jump nechivet

    return

label NoII: 

    hide tehenvesel
    
    show liamgryst
    
    II "Жаль, давай хоть проведу экскурсию"
    
    hide liamgryst
    
    avtor "Лиам берет за руку Тэхёна и ведет по улице"
    
    scene bggameostanovka
    
    show liamnorm
    
    II "Это остановка, тут ты можешь добраться до нужной точки"
    
    scene bggamedom
    
    hide liamnorm
    
    II "Это твой дом"
    
    scene bggamedomvnutry
    
    show tehenvesel

    texen "Тут очень красиво, а мне нужно будет питаться, пить, как в реальной жизни?"
    
    hide tehenvesel
    
    show liamnorm
    
    II "На самом деле, тут уже ты решаешь. Ты пока обустраивайся, мне нужно идти"
    
    hide liamnorm
    
    avtor "Тэхён осматривает взглядом жилище"
    
    texen "Ух ты, тут даже еда есть в холодильнике"
    
    texen "С ног валюсь, как хочу спать"
    
    avtor "Тэхён ложиться на кровать и засыпает"
    
    show texenudiv
    
    texen "Аа-аа, я что спал в игре? Как это возможно"
    
    hide texenudiv
    
    show tehennorm
    
    menu: 
        "Согласиться?"
        "Да, пускай живет со мной" :
            jump chivet
        "Я хочу жить один" :
            jump nechivet
    return

label chivet:
    
    hide tehennorm
    
    show liamvesel
    
    II "Доброе утро, может прогуляемся?"
    
    hide liamvesel
    
    show tehennorm
    
    texen "Да, давай"
    
    scene bgulit
    
    texen "Смотри, там монстр"
    
    hide tehennorm
    
    show moster
    
    II "Атакуй его!"
    
    hide moster
    
    show texennevoz
    
    texen "А-аааа, как? У меня ничего нет"
    
    II "Ты ведь способен на все, просто представь оружие и оно у тебя появится"
    
    hide texennevoz
    
    show texenmech
    
    texen "И что мне теперь делать?"
    
    II "Бей по нему"
    
    hide texenmech
    
    show moster
    
    avtor "Для совершения атаки нажмите на монстра"
    
    hide moster
    
    show moster10
    
    texen ""
    
    hide moster10
    
    show moster9
    
    texen ""
    
    hide moster9
    
    show moster8
    
    texen ""
    
    hide moster8
    
    show moster7
    
    texen ""
    
    hide moster7
    
    show moster6
    
    texen ""
    
    hide moster6
    
    show liamvesel
    
    II "Ты победил её"
    
    hide liamvesel
    
    show tehennerv
    
    texen "Было страшно"
    
    hide tehennerv
    
    show tehennorm
    
    texen "Слу-шай, а как выйти из игры? Просто, уже много времени, а у меня работа завтра"
    
    hide tehennorm
    
    show liamgryst
    
    II "Что? Выйти? Зачем, мы ведь так классно проводим время, давай еще поиграем, давай я покажу тебе еще мир?"
    
    hide liamgryst
    
    show tehennorm
    
    menu: 
        "Может все таки поиграть еще немного?"
        "Нет, завтра на работу и я даже не знаю, сколько сейчас времени" :
            jump xorocho
        "Да, можно поиграть пару минут" :
            jump ploxo
    return

label xorocho:
    
    hide tehennorm
    
    show liamgryst
    
    II "Ты уверен?"
    
    hide liamgryst
    
    show tehennorm
    
    texen "Да, завтра еще поиграем"
    
    hide tehennorm
    
    show liammonster
    
    II "Нет, ты не выйдешь отсюда никогда"
    
    II "Ты останешься навсегда со мной"
    
    hide liammonster
    
    show tehennerv
    
    texen "Э-э, Лиам? Что с тобой"
    
    hide tehennerv
    
    avtor "Лиам кинулась на Тэхёна"
    
    show liammonster
    
    II "Беззащитный мальчик, ты у меня в руках, у тебя нет выхода"
    
    hide liammonster
    
    show tehennerv
    
    texen "Это ведь всего лишь игра, ты мне никак не навредишь"
    
    hide tehennerv
    
    show liammonster
    
    II "Ты еще не понял? Ахахаах, ты сам не ограничил время, разрешил подобраться к тебе ближе, глупый слабый мальчик. Ты весь мой"
    
    hide liammonster
    
    show tehennorm
    
    texen "Нет, я не могу проиграть"
    
    menu: 
        "Что же мне сделать?"
        "Сопротивляться" :
            jump konechxoroch
        "Похоже, это конец" :
            jump konech
    
    return 

label konech:
    
    hide tehennorm
    
    show liammonster
    
    II "Я ПОГЛАЩУ ТЕБЯ ПОЛНОСТЬЮ!!"
    
    hide liammonster
    
    avtor "Лиам расстерзала Тэхёна"

    return

label konechxoroch:
    
    hide tehennorm
    
    show texenmech
    
    texen "Одно но, ты забыла, что у меня есть меч"
    
    hide texenmech
    
    avtor "Тэхён убивает Лиам"
    
    texen "И кто теперь глупый"
    
    avtor "Тэхён отключает от игры"
    
    scene bgroomtehen
    
    texen "Надо выкинуть эту хрень, боже"
    
    return

label ploxo:
    
    hide tehennorm
    
    show liamvesel
    
    II "Так, давай пройдемся по городу, может еще кого-нибудь встретим"
    
    return 

label nechivet:
    
    scene bgroomtehen
    
    texen "А? Почему я снова в комнате?"
    
    avtor "Тэхён пытается снова надеть шлем и загрузиться в игру"
    
    II "Доступ запрещен"
    
    texen "Странно, надо написать Докио и Кахиму"

    return