
#my_list = [Маргарита, Дмитрий, Антон, Юлия, Александр, Петровыч, Анастасия, Лев]
my_list = [1, 2, 3]

print("Здравствуйте, вас приветствует умный бот Samsung. ")
 

while True:
    data = input("Пожалуйста, скажите мне как Вас зовут и мы Вам поможем: ")
    if data.lower() == "y":
      continue  # продолжение цикла
    print("Рады знакомству,", data, ". Укажите код интересующей  Вас категории: ")
    print("Ваше имя будет использоваться для получения интернет-заказов и сервисного обслуживания")
    print("1. Приобретение товара")
    print("2. Сервисное обслуживание")
    print("3. Ничего из этого")
    data = input("")
    if data.lower() == "1":
      print("Для приобретения товара мы перенеправляем вас в наш интернет-магазин")
      print("1. Мобильные устройства")
      print("2. ТВ")
      print("3. Бытовая техника")
      print("4. IT")
      print("Для перехода к нужной категории напишите с клавиатуры код категории")
      data = input("")
      if data.lower() == "1":
       print("Вы находитесь в разделе Мобильные устройства, вот что мы Вам можем предложить")
       print("1. Galaxy S10")
       print("2. Galaxy NOTE 10")
       print("3. Galaxy S")
       print("4. Galaxy A")
       print("5. Galaxy J")
       data = input("")
       if data.lower() == "1":
         print("В данный момент в наличии 10 смартфонов Samsung Galaxy S10 в вашем городе.")
         print("Стоимость заказа 54990Р")
         print("1. Зарезервировать в ближайшем интернет-магазине Samsung")
         print("2. Отказаться от обслуживания")
         data = input("")
         if data.lower() == "1":
           print("Для Вас зарезервирован Samsung Galaxy S10 в магазине по адресу  Комсомольский просп., 13Б, Томск, для оформления скажите имя, которое вы указали в нашем боте") 
           break
         if data.lower() == "2":
           print("Благодарим вас за использование сервисов Samsung")
           break
       if data.lower() == "2":
         print("В данный момент в наличии 5 смартфонов Samsung Galaxy Note 10.")
         print("Стоиомсть заказа 69900Р")
         print("1. Зарезервировать в ближайшем интернет-магазине Samsung")
         print("2. Отказаться от обслуживания")
         data = input("")
         if data.lower() == "1":
           print("Для Вас зарезервирован Galaxy Note 10 в магазине по адресу  Комсомольский просп., 13Б, Томск,для оформления скажите имя, которое вы указали в нашем боте")
           break
         if data.lower() == "2":
           print("Благодарим Вас за использование сервисов Samsung")
           break 
       if data.lower() == "3":
         print("В данный момент в наличиии в магазине по адресу Комсомольский просп., 13Б, Томск:")  
         print("Samsung Galaxy S10 стоимсоть 54 990Р")
         print("Samsung Galaxy S10 Plus стоимость 64 990Р")
         print("Samsung Galaxy S9 стоимость 39 990Р") 
         print("Спасибо за использование сервисов Samsung.")
         break
       if data.lower() == "4":
         print("В данный момент в наличии в магазине по адресу Комсомолський просп., 13Б, Томск: ")
         print("Samsung Galaxy A10 стоимость 9 990Р")
         print("Samsung Galaxy A20 стоимость 11 990Р")
         print("Samsung Galaxy A30 стоимость 12 990Р")
         print("Samsung Galaxy A40 стоимость 14 990Р")
         print("Samsung Galaxy A50 стоимость 19 990Р")
         print("Samsung Galaxy A70 стоимость 24 990Р")
         print("Благодарим Вас за использование сервисов Samsung")
         break
       if data.lower() == "5":
         print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б, Томск: ")
         print("Samsung Galaxy J2 2018 стоимость 5 990Р")
         break    
      if data.lower() == "2":
       print("Вы находитесь в разделе TV, вот что мы Вам можем предложить")
       print("1. QLED TV")
       print("2. UHD TV")
       print("3. FULL HD TV")
       print("4. SMART TV")
       data = input("")
       if data.lower() == "1":
        print("В данный момент в наличиии в магазине по адресу Комсомольский просп., 13Б, Томск: ")
        print("1. Q900R 8K Smart QLED TV 2019 QE98Q900RBUXRU 4.3 13 стоимость 4 999 990₽")
        print("2. Q6F 4K Smart QLED TV QE75Q6FNAUXRU стоимость 299 000Р")
        print("3. Q67R 4K Smart QLED TV 2019 QE65Q67RAUXRU стоимость 149 990Р")
        print("Благодарим Вас за использование сервисов Samsung")
        break
       if data.lower() == "2":
        print("В даннный момент в наличии в магазине по адресу Комсомольский просп., 13Б, Томск: ")
        print("1. 65 UHD 4K Smart TV RU7470 Series 7UE65RU7470UXRU стоимость 109 990Р")
        print("2. 50 UHD 4K Smart TV NU7097 Series 7UE50NU7097UXRU стоимость 34 990Р")
        print("3. 50 UHD 4K Smart TV RU7410 Series 7UE50RU7410UXRU стоимость 43 990Р")
        print("Благодарим Вас за использование сервисов Samsung")
        break
       if data.lower() == "3":
        print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б., Томск: ")
        print("1. 49 FHD Smart TV N5570 Series 5UE49N5570AUXRU стоимость 35 990Р")
        print("2. 43 FHD Smart TV N5300 Series 5UE43N5300AUXRU стоимость 25 990Р")
        print("3. 49 FHD Smart TV N5500 Series 5UE49N5500AUXRU стоимость 35 990Р")
        print("Благодарим Вас за использование сервисов Samsung")
        break
       if data.lower() == "4":
        print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б., Томск: ")
        print("1. 50 UHD 4K Smart TV RU7410 Series 7 стоимость 49 990Р")
        print("2. 65 UHD 4K Curved Smart TV RU7300 Series 7UE65RU7300UXRU стоимость 79 900Р")
        print("3. 50 UHD 4K Smart TV NU7002 Series 7UE50NU7002UXRU стоимость 35 990Р")
        print("4. 55 QLED The Serif TV QE55LS01RBUXRU стоимость 99 990р")
        print("5. 50 UHD 4K Smart TV RU7410 Series 7UE50RU7410UXRU стоимость 54 990Р")
        print("6. 75 UHD 4K Smart TV RU7100 Series 7UE75RU7100UXRU стоимость 99 990Р")
        print("7. Q900R 8K Smart QLED TV 2019 QE98Q900RBUXRU 4.3 13 стоимость 4 999 990₽")
        print("8. Q6F 4K Smart QLED TV QE75Q6FNAUXRU стоимость 299 000Р")
        print("9. 32 HD Smart TV N4510 Series 4UE32N4510AUXRU стоимость 19 990Р")
        break

      if data.lower() == "3":
       print("Вы находитесь в разделе Бытовая техника, вот что мы Вам можем предложить")
       print("1. Холодильники")
       print("2. Стиральные машины")
       print("3. Пылесосы")
       print("4. Кондиционеры")
       data = input("")
       if data.lower() == "1":
         print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б Томск")
         print("1. RT3000, Холодильник с инверторным компрессором, 255 л RT25HAR4DWW/WT стоимость 29 990Р")
         print("2. RB7000 Холодильник с увеличенным полезным объёмом SpaceMax™, 410 л RB41J7861EF/WT стоимость 67 990")
         print("3. RB6000 Холодильник с увеличенным полезным объёмом SpaceMax™, 367 л RB37K63412A/WT стоимость 74 990Р")
         break
       if data.lower() == "2":
         print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б Томск")
         print("1. Стиральная машина WW6600R с AddWash, 7 кг WW70R62LVSXDLP стоимость 34 990Р")
         print("2. Стиральная машина с сушкой с AddWash WD5500K, 8/5 кг WD80K52E0ZX/LP стоимость 49 990Р")
         print("3. Стиральная машина WW6100R с EcoBubble, 8 кг WW80R62LAFWDLP стоимость 37 990Р")
         print("4.Стиральная машина WW6100R с EcoBubble, 8 кг WW80R62LAFWDLP стоимость 40 990Р ")
         break
       if data.lower() == "3":
         print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б Томск")
         print("1. C4100 Pet Care, пылесос с контейнером, с турбиной Anti-Tangle, 390 Вт VC15K4169HD/EV стоимость 10 990Р")
         print("2. VC5100, пылесос с контейнером, с турбиной Anti-Tangle, 440 Вт стоимость 12 990Р")
         break
       if data.lower() == "4":
         print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б Томск")
         print("К сожалению, на складе отстутствуют Кондиционеры")
         break
      if data.lower() == "4":
        print("Вы находитесь в разделе IT, вот что Мы Вам можем предложить")
        print("1. Мониторы")
        print("2. Память")
        print("3. Печатная техника") 
        data = input("") 
        if data.lower() == "1":
         print("1. Изогнутые мониторы")
         print("2. Игровые мониторы")
         print("3. Все мониторы")
         data = input("")
         if data.lower() == "1":
           print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б.,Томск: ")
           print("1. 27 LED-монитор C27F390FHILC27F390FHIXRU стоимость 8 900Р")
           print("2. 27 CURVED-монитор C27F591FDILC27F591FDIXRU стоимость 14 990Р")
           print("3. 23,5 GAMING-монитор C24RG50FQILC24RG50FQIXCI стоимость 13 990Р")
           print("4. 26,9 CURVED-монитор C27R500FHILC27R500FHIXCI стоимость 11 990Р")
           print("5. 27” GAMING-монитор C27RG50FQI (240 Гц) LC27RG50FQIXCI стоимость 24 990Р")
           break
         if data.lower() == "2":
           print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б. Томск: ")
           print("1. 27” GAMING-монитор C27RG50FQI (240 Гц)LC27RG50FQIXCI стоимость 29 990Р")
           print("2. 31,5 GAMING-монитор C32JG50QQILC32JG50QQIXCI стоимость 27 990Р")
           print("3. 31,5 GAMING-монитор C32JG51FDILC32JG51FDIXCI стоимость 21 990Р")
           print("4. 27 GAMING-монитор C27FG73FQILC27FG73FQIXRU стоимость 24 990Р")
           print("5. 23,5 GAMING-монитор C24RG50FQILC24RG50FQIXCI стоимость 13 990Р")
           break
         if data.lower() == "3":
           print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б.,Томск: ")
           print("1. 27 LED-монитор C27F390FHILC27F390FHIXRU стоимость 8 900Р")
           print("2. 27 CURVED-монитор C27F591FDILC27F591FDIXRU стоимость 14 990Р")
           print("3. 23,5 GAMING-монитор C24RG50FQILC24RG50FQIXCI стоимость 13 990Р")
           print("4. 26,9 CURVED-монитор C27R500FHILC27R500FHIXCI стоимость 11 990Р")
           print("5. 27” GAMING-монитор C27RG50FQI (240 Гц) LC27RG50FQIXCI стоимость 24 990Р")
           print("6. 31,5 GAMING-монитор C32JG51FDILC32JG51FDIXCI стоимость 21 990Р")
           print("7. 27 LED-монитор S27F358FWILS27F358FWIXCI стоимость 13 990Р")
           print("8. 27 LED-монитор S27E391HLS27E391HSX/CI стоимость 12 990Р")
           print("9. 31,5 UHD-монитор S32R750UEI (The Space) LS32R750UEIXCI стоимость 35 990Р")
           break
        if data.lower() == "2":
           print("1. Накопители SSD")
           print("2. Накопители USB")
           print("3. Карты памяти")
           data = input("")
           if data.lower() == "1":
             print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б., Томск: ")
             print("1. SSD Обьемом 4ТБ 860 PRO SATA 2.5 SSD 4TBMZ-76P4T0BW стоимость 39 990Р")
             print("2. SSD Обьемом 512ГБ 860 PRO SATA 2.5 SSD 512ГБ MZ-76P2T0BW стоимость 8990Р")
             print("3. SSD Обьемом 256ГБ 860 PRO SATA 2.5 SSD 256ГБ MZ-76P256BW стоимость 6 490Р")
             break
           if data.lower() == "2":
             print("В данный момент в наличии в магазине по адресу Комсомольский просп., 13Б., Томск: ")
             print("1. BAR Plus USB 3.1 Накопитель 64ГБ MUF-64BE4/APC стоимость 1 990Р")
             print("2. FIT Plus USB 3.1 Накопитель 256ГБ MUF-256AB/AP стоимость 7 990Р")
             print("3. DUO Plus USB Type-C Накопитель 32ГБMUF-32DB/APC стоимость 2 190Р")
             break
    if data.lower() == "2":
      print("Для получения сервисного обслуживания мы рекомендуем оставить заявку на сайте.")
      datacontinue = input("Перенаправить для оформления заявки? Напишите Да или Нет: ")
      if datacontinue.lower() == "Y":
       continue
      print("У вас нет выбора. Мы Samsung, а не xiaomi. Наши устройства не нуждаются в обслуживании. ")
      break  
    if data.lower() == "3":
      print("Сожалеем, что не смогли Вам помочь. Помощь это призвание, а если помощь хотите получить - идите в бизнес...")
      break  
    
    #print("1. Приобретение товара")
    #print("2. Сервисное обслуживание")
    #print("3. Ничего из этого")
   
  
      #print("Спасибо за ответ, мы перенаправляем Вас в наш магазин")


print("Всего вам доброго, ваш бот Samsung.")
