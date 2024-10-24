site_dict = {}
description_dict = {}
n = int(input("Скільки сайтів ви хочете додати? "))
for i in range(1, n+1):
    site = input(f"Введіть адресу сайту №{i}: ")
    description = input(f"Введіть опис сайту №{i}: ")
    site_dict[i] = site
    description_dict[i] = description
print("\n Записи з обох словників:")
for i in range(1, n+1):
    print(f"{site_dict[i]} - {description_dict[i]}")
