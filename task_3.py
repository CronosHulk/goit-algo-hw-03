def hanoi(n, source, destination, auxiliary, rods):
    if n == 1:
        disk = rods[source].pop()
        rods[destination].append(disk)
        print(f"Перемістити диск з {source} на {destination}: {disk}")
        print(f"Проміжний стан: {rods}\n")
        return

    hanoi(n - 1, source, auxiliary, destination, rods)

    disk = rods[source].pop()
    rods[destination].append(disk)
    print(f"Перемістити диск з {source} на {destination}: {disk}")
    print(f"Проміжний стан: {rods}\n")

    hanoi(n - 1, auxiliary, destination, source, rods)

if __name__ == "__main__":
    try:
        num_disks = int(input("Введіть кількість дисків: "))
        if num_disks <= 0:
            print("Кількість дисків має бути додатним числом.")
        else:
            rods = {
                'A': list(range(num_disks, 0, -1)),
                'B': [],
                'C': []
            }
            print(f"Початковий стан: {rods}\n")
            hanoi(num_disks, 'A', 'C', 'B', rods)
            print(f"Кінцевий стан: {rods}")
    except ValueError:
        print("Будь ласка, введіть ціле число.")
