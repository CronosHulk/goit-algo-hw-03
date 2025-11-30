import turtle
import argparse

def koch_curve(t, order, size):
    if order == 0:
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_curve(t, order - 1, size / 3)
            t.left(angle)

def draw_koch_snowflake(order, size=300):
    window = turtle.Screen()
    window.bgcolor("white")
    window.title(f"Сніжинка Коха (рівень {order})")

    t = turtle.Turtle()
    t.speed(0)
    t.penup()
    t.goto(-size / 2, size / (2 * 3**0.5))
    t.pendown()
    t.color("blue")

    for _ in range(3):
        koch_curve(t, order, size)
        t.right(120)

    window.mainloop()

def main():
    parser = argparse.ArgumentParser(description="Малює сніжинку Коха заданого рівня рекурсії.")
    parser.add_argument("--level", type=int, default=4, help="Рівень рекурсії для сніжинки Коха (за замовчуванням: 3)")
    args = parser.parse_args()

    if args.level < 0:
        print("Рівень рекурсії не може бути від'ємним.")
        return

    draw_koch_snowflake(args.level)

if __name__ == "__main__":
    main()
