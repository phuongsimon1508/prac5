def main():


    text= int(input("enter a text"))
    wordCount = {}



    for word in wordCount.split():
        wordCount[word]= wordCount.get(word, 0) +1

    max_len= len(max(wordCount, key=len))

    for word in sorted(wordCount):
        print
