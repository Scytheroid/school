# Tuto funkci implementuj. Smaz prikaz 'pass' a pis telo funkce.
def word_frequency(text):
    freq_dict = {}
    text.lower()
    for char in text:
        print(char)

# testy (upravujte dle libosti)
print(word_frequency("Ksi, Ksa, Ksi, Kse"))       # {'ksi': 2, 'ksa': 1, 'kse': 1}
print(word_frequency("Informatika je nejlepsi"))  # {'informatika': 1, 'je': 1, 'nejlepsi': 1}
