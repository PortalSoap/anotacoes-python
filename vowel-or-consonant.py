letter = input("Insira uma letra: ")
vowels = ['A', 'a', 'E', 'e', 'I', 'i', 'O', 'o', 'U', 'u']

if len(letter) > 1:
    print("Você inseriu uma palavra ou sentença, e não uma letra.")
elif letter in vowels:
    print("A letra inserida é uma vogal.")
else:
    print("A letra inserida é uma consoante.")