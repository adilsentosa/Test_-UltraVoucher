def are_anagrams(word1, word2):
    # Mengecek apakah panjang kedua kata sama
    if len(word1) != len(word2):
        return False
    
    char_count = {}

    # Menghitung jumlah karakter dalam kata pertama
    for char in word1:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Membandingkan jumlah karakter dalam kata kedua dengan kata pertama
    for char in word2:
        if char not in char_count or char_count[char] == 0:
            return False
        char_count[char] -= 1
    
    return True

def group_anagrams(words):
    grouped_anagrams = []

    for word in words:
        added_to_group = False

        # Iterasi melalui grup-grup yang sudah ada
        for group in grouped_anagrams:
            # Mengecek apakah kata merupakan anagram dari kata dalam grup
            if all(word.count(char) == group[0].count(char) for char in word):
                group.append(word)
                added_to_group = True
                break
        if not added_to_group:
            # Jika kata tidak cocok dengan grup manapun, maka membuat grup baru
            grouped_anagrams.append([word])

    return grouped_anagrams

#penggunaan
input_array = ['cook', 'save', 'taste', 'aves', 'vase', 'state', 'map']
result = group_anagrams(input_array)
print(result)
