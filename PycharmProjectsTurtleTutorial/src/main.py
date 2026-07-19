import turtle
import random



# --- EKRAN AYARLARI ---
screen = turtle.Screen()
screen.title("Catch The Turtle!")
screen.bgcolor("light blue")
screen.setup(width=600, height=600)

# Oyun Değişkenleri
score = 0
time_left = 20  # Oyun süresi (saniye)
game_over = False

# --- SKOR YAZISI ---
score_turtle = turtle.Turtle()
score_turtle.hideturtle()
score_turtle.penup()
score_turtle.goto(0, 260)
score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

# --- TIMER (ZAMANLAYICI) YAZISI ---
timer_turtle = turtle.Turtle()
timer_turtle.hideturtle()
timer_turtle.penup()
timer_turtle.goto(0, 220)
timer_turtle.write(f"Time: {time_left}", align="center", font=("Arial", 24, "normal"))

# --- HEDEF TURTLE (YAKALANACAK OLAN) ---
target = turtle.Turtle()
target.shape("turtle")
target.shapesize(2, 2)  # Turtle'ı biraz büyüterek tıklamayı kolaylaştırıyoruz
target.color("dark green")
target.penup()


# --- FONKSİYONLAR ---

def move_turtle():
    """Her 2 saniyede bir turtle'ı rastgele bir yere ışınlar."""
    if not game_over:
        # Ekran sınırları içinde rastgele koordinat seç (-230 ile 230 arası güvenlidir)
        x = random.randint(-230, 230)
        y = random.randint(-230, 200)  # Skor yazısına çok yaklaşmaması için y üst sınırını biraz kıstık
        target.goto(x, y)

        # 2000 milisaniye (2 saniye) sonra bu fonksiyonu tekrar çağır (Bloklama yapmaz!)
        screen.ontimer(move_turtle, 2000)


def catch_turtle(x, y):
    """Turtle'a her tıklandığında skoru artırır ve turtle'ı hemen başka yere kaçırır."""
    global score
    if not game_over:
        score += 1
        # Skor yazısını güncelle
        score_turtle.clear()
        score_turtle.write(f"Score: {score}", align="center", font=("Arial", 24, "normal"))

        # Tıklandığı an beklemeden hemen yeni yere kaçsın (isteğe bağlı ama oyun zevkini artırır)
        new_x = random.randint(-230, 230)
        new_y = random.randint(-230, 200)
        target.goto(new_x, new_y)


def countdown():
    """Her 1 saniyede bir çalışarak süreyi azaltır."""
    global time_left, game_over
    if time_left > 0:
        time_left -= 1
        timer_turtle.clear()
        timer_turtle.write(f"Time: {time_left}", align="center", font=("Arial", 24, "normal"))

        # 1000 milisaniye (1 saniye) sonra countdown fonksiyonunu tekrar çağır
        screen.ontimer(countdown, 1000)
    else:
        # Süre bittiğinde oyunu sonlandır
        game_over = True
        target.hideturtle()  # Hedef kaplumbağayı gizle
        timer_turtle.clear()
        timer_turtle.write("GAME OVER!", align="center", font=("Arial", 24, "bold"))


# --- OYUNU BAŞLATAN TETİKLEYİCİLER ---

# Turtle'a tıklama olayını (onclick) dinliyoruz
target.onclick(catch_turtle)

# Zamanlayıcıyı başlat (1 saniyede bir çalışacak)
countdown()

# Turtle hareketini başlat (2 saniyede bir çalışacak)
move_turtle()

# Ekranın açık kalmasını sağlar
screen.mainloop()

