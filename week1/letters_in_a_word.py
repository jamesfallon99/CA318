def sol(word, letter):
    return [l for l in word if letter != l]
print(sol("trendy", "e"))