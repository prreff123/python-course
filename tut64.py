def macthingword(sentence1, sentence2):
    words1 = sentence1.split(" ")
    words2 = sentence2.split(" ")
    score = 0

    for word1 in words1:
        for word2 in words2:
            # print(f"Matching {word1} with {word2}")
            if word1.lower() == word2.lower():
                score += 1 
    return score            

if __name__ == "__main__":
    print(macthingword("This is good", "Python is is good"))
    