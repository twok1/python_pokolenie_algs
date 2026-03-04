def snake(n):
    for i in range(n):
        if (i + 1) % 4 == 0:
            print(f"*{' ' * (n - 1)}")
        elif (i + 1) % 2 == 0:
            print(f"{' ' * (n - 1)}*")
        else:
            print(f"{'*' * n}")
        
