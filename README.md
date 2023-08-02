# TelegramBot

Телеграм бот с использованием Finite State Machine(FSM) и logging. Бот который может собирать статистику и делать рассылку, добавлять фото в галерею и отправлять их пользователю.

## Подробное описание:
После команды /start открывается меню из шести Keyboard-кнопок ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/91390637-60da-426a-8148-975e06e50938)

***- Статистика***
  - открывается сообщение с Inline-кнопками для выбора. Посмотреть статистику может только админ
    ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/8ab92cc5-0ae0-48fd-840d-1baaf2d760d9)

***- Информация***
  - информация о боте
    
    ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/a7f158c2-5faf-4a34-826f-1ed6513f5b2a)

***- Разработчик***
  - приходит сообение с id admina и текстом
   
***- Покажи пользователя***
  - открывается сообщение с Inline-кнопками (дальше зависит от выбора: "хочу увидеть id" - высылает номер, "вернуться обратно" - возвращает в главное меню)
    ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/b2f6ec3c-7a7c-4537-9a73-3cab8e4577f3)
    
***- Добавить фото***
  - добавляет прикрепленное изображение в галерею
    ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/bcc55c43-f782-46f4-91f9-5555d1810d5f)

    
***- Открыть фото из галереи***
  - отправляет пользователю все изображения из галереи
    ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/e4f5952c-657e-4f35-af65-a95ad3657721)
    ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/9e441b91-9b8e-4d3a-8f5d-03f215d7f44a)


 
    
## Команды для админа:

**-/me**

    При вводе команды /me, бот просит отправить ссылку на профиль и ждёт ответа. Он его записывает в текстовый 
  документ. Далее он просит указать нам текст, который так же записывает в наш файл.  
  ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/5a391708-8e75-4edf-b247-a88b275537fc)

**-/rassilka**

  Делаем рассылку пользователям - фотография с текстом. В коде реализовано так, чтобы бот рассылал текст, который написан через пробел к   команде. 
  
  ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/a984366c-e771-48ac-bbf1-b85c5ec24d6a)
  ![image](https://github.com/Nastassia2334/TelegramBot/assets/122525312/1d4a77e8-3492-4a47-a5d8-4cde7ffbd44e)

