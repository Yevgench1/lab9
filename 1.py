from collections import Counter
websites = ("google.com", "yahoo.com", "youtube.com", "github.com")
letters = ''.join([char for website in websites for char in website if char.isalpha()])
letter_counts = Counter(letters)
print("Частота зустрічання літер в адресах веб-сайтів:")
for letter, count in letter_counts.items():
    print(f"{letter}: {count}")
