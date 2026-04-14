# import pygame
# import random
# import sys
#
# pygame.init()
#
# WIDTH, HEIGHT = 600, 400
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# pygame.display.set_caption("Колобок и Волк")
#
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# GREEN = (50, 200, 50)
# RED = (200, 50, 50)
#
# font = pygame.font.SysFont(None, 28)
# clock = pygame.time.Clock()
#
# kolobok = pygame.Rect(280, 330, 40, 40)
# ball = pygame.Rect(random.randint(0, 580), 0, 20, 20)
#
# ball_speed = 4
# state = "intro"
# game_over = False
#
# # СПИСОК ингредиентов
# ingredients = ["Мука", "Вода", "Яйцо", "Сахар", "Масло"]
#
# while not game_over:
#     space_pressed = False
#     screen.fill(WHITE)
#
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             game_over = True
#
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_SPACE:
#                 space_pressed = True
#
#     keys = pygame.key.get_pressed()
#
#     # ====== НАЧАЛО СКАЗКИ ======
#     if state == "intro":
#         text1 = font.render("Жили-были дед да баба.", True, BLACK)
#         text2 = font.render("Решили они испечь Колобка.", True, BLACK)
#         text3 = font.render("Нажми ПРОБЕЛ", True, BLACK)
#
#         screen.blit(text1, (160, 140))
#         screen.blit(text2, (150, 180))
#         screen.blit(text3, (230, 230))
#
#         if space_pressed:
#             state = "ingredients"
#
#     # ====== СПИСОК ИНГРЕДИЕНТОВ ======
#     elif state == "ingredients":
#         title = font.render("Колобок был приготовлен из:", True, BLACK)
#         screen.blit(title, (160, 40))
#
#         for i, item in enumerate(ingredients):
#             text = font.render(f"- {item}", True, BLACK)
#             screen.blit(text, (220, 80 + i * 30))
#
#         text2 = font.render("Нажми ПРОБЕЛ", True, BLACK)
#         screen.blit(text2, (220, 260))
#
#         if space_pressed:
#             state = "escape"
#
#     # ====== ПОБЕГ КОЛОБКА ======
#     elif state == "escape":
#         text1 = font.render("Колобок остыл на подоконнике...", True, BLACK)
#         text2 = font.render("И вдруг убежал в лес!", True, BLACK)
#         text3 = font.render("Нажми ПРОБЕЛ", True, BLACK)
#
#         screen.blit(text1, (130, 150))
#         screen.blit(text2, (180, 190))
#         screen.blit(text3, (230, 240))
#
#         if space_pressed:
#             state = "story"
#
#     # ====== ВСТРЕЧА С ВОЛКОМ ======
#     elif state == "story":
#         text1 = font.render("Колобок встретил Волка!", True, BLACK)
#         text2 = font.render("Волк: Я тебя съем!", True, BLACK)
#         text3 = font.render("Нажми ПРОБЕЛ, чтобы начать игру", True, BLACK)
#
#         screen.blit(text1, (170, 130))
#         screen.blit(text2, (190, 170))
#         screen.blit(text3, (110, 220))
#
#         if space_pressed:
#             ball.y = 0
#             ball.x = random.randint(0, WIDTH - 20)
#             state = "game"
#
#     # ====== МИНИ-ИГРА ======
#     elif state == "game":
#         if keys[pygame.K_LEFT] and kolobok.x > 0:
#             kolobok.x -= 5
#         if keys[pygame.K_RIGHT] and kolobok.x < WIDTH - 40:
#             kolobok.x += 5
#
#         ball.y += ball_speed
#
#         if kolobok.colliderect(ball):
#             state = "win"
#
#         if ball.y > HEIGHT:
#             state = "lose"
#
#         pygame.draw.ellipse(screen, GREEN, kolobok)
#         pygame.draw.ellipse(screen, RED, ball)
#
#         text = font.render("Поймай мячик!", True, BLACK)
#         screen.blit(text, (230, 10))
#
#     # ====== ПОБЕДА ======
#     elif state == "win":
#         text1 = font.render("Колобок убежал от Волка!", True, BLACK)
#         text2 = font.render("Конец первой встречи", True, BLACK)
#         text3 = font.render("ESC — выход", True, BLACK)
#
#         screen.blit(text1, (170, 160))
#         screen.blit(text2, (200, 200))
#         screen.blit(text3, (220, 240))
#
#         if keys[pygame.K_ESCAPE]:
#             game_over = True
#
#     # ====== ПРОИГРЫШ ======
#     elif state == "lose":
#         text1 = font.render("Волк съел Колобка...", True, BLACK)
#         text2 = font.render("R — рестарт | ESC — выход", True, BLACK)
#
#         screen.blit(text1, (180, 180))
#         screen.blit(text2, (150, 220))
#
#         if keys[pygame.K_ESCAPE]:
#             game_over = True
#         elif keys[pygame.K_r]:
#             state = "intro"
#             kolobok.x = 280
#             ball.y = 0
#
#     pygame.display.update()
#     clock.tick(60)
#
# pygame.quit()
# sys.exit()


# file_w = open("poem.txt", "w", encoding="utf-8")
# file_w.write(
#     "Весна пришла в наш тихий двор"
#     "\nИ солнце светит ярче"
#     "\nПоют птицы с ранних пор"
#     "\nИ мир стал будто мягче"
#     "\nИ мир стал будто мягче\n")
# file_w.close()
#
# file =  open("poem.txt", "r", encoding="utf-8")
# text = file.read()
#
# lines = text.splitlines()
# words = text.split()
#
# line_count = len(lines)            # количество строк
# word_count = len(words)            # количество слов
# longest_line = max(lines, key=len) # самая длинная строка
#
# print("Количество строк:", line_count)
# print("Количество слов:", word_count)
# print("Самая длинная строка:")
# print(longest_line)
# file.close()


catalog = {
    "Жетиген": 500,
    "Баластан": 700,
    "Bishkekchanka": 300
}

password = "123"
cart = []
history = []

while True:
    print("МАГАЗИН\n1. Товары\n2. В корзину\n3. Купить\n4. История\n5. Пароль\n0. Выход")

    choice = input("Выберите действие: ")

    if choice == "1":
        for name, price in catalog.items():
            print(f"{name} - {price}")

    elif choice == "2":

        search = input("Что ищем? ")
        found = False
        for name, price in catalog.items():
            if name.lower() == search.lower():
                cart.append(name)
                print("Добавлено!")
                found = True
                break
        if not found: print("Не найдено")

    elif choice == "3":
        if cart:
            history.extend(cart)
            print("Куплено:", cart)
            cart.clear()
        else:
            print("Корзина пуста")

    elif choice == "4":
        print("Ваши журналы:", history)

    elif choice == "5":
        if input("Старый пароль: ") == password:
            password = input("Новый пароль: ")
            print("Ок")
        else:
            print("Ошибка")

    elif choice == "0":
        break
