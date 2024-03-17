# return true for strings whose mirror images are same
word = input("Enter a word\n")

def mirror_img(word):
    sym = "AHIMOTUVWXYmouvwx"
    l = len(word)
    for i in range(l//2):
        if word[i] != word[l-i-1] or word[i] not in sym:
            return False
    return True

print(mirror_img(word))