import re                               #importing to receive only specific kinds of string
import pandas as pd                     #imorting to read csv files

def solver(listreview):                        #This function generates a list that stores words from the tweets.txt such as not-so-happy in the
    listchecker = re.findall(r'\w+-.+', listreview)    #Regex function that stores text contents in a list(ignores the value of coordinates)
    newlist = []                                       #List declared to store text contents that would generated after the execution of this function
    punctuation = "!@#$%^&*()_=+[{]}\\|;:\'\'',<.>/?"  #List of punctuations to be stripped from the tweets
    listchecker[0] = listchecker[0].split()             #Splitting the contents in a list
    length = len(listchecker[0])                        #Stores the length of the list

    for p in range(0, length):                          #Loop traverses through whole list
        leng = len(listchecker[0][p])                   #Store lenth of individual word in a list
        for q in range(0, leng):                        #Loop traverses through the pth word's length
            if listchecker[0][p][q] in punctuation:     #Checks whether the word contains the punctuation

                listchecker[0][p] = listchecker[0][p].replace(listchecker[0][p][q], " ")        #Replacing the punctuation with space
                word = re.findall(r'\w+', listchecker[0][p])    #Stores the words in a list after the punctuations are removed

                lengt = len(word)                               #Stores the number of elements in the word


                for i in range(0, lengt):                       #Loop goes till on till all the elements are read
                    newlist.append(word[i])                     #Append the modified words in a newlist

        newlist.append(listchecker[0][p])                       #If there were no punctuations,the word is appended outside the loop

    return(newlist)                                             #Returns the refined list


def formatInput(textLine):              #function that returns capital letters into small letters
    textLine = textLine.lower().strip()
    wordList = textLine.split()
    textLine = " ".join(wordList)
    return textLine



def compute_tweets(filewithtweets,filewithkeywords):        #Function that gets the file with tweets file and the file with keywords file from main.py
#1)Name of the file with the tweets ,2)name of the file with the keywords

    emptylist=[]            #If any one of the files does not exist,then the program fill return an empty list
    try:                    #Continues if both the files exist
        # Importing keywords
        datasetkey = pd.read_csv(filewithkeywords, names=['Review', 'Score'], index_col=None,header=None,encoding="utf‐8")  # Opening the file in CSV(Comma Seperated Value) mode
        dictkey = list(datasetkey['Review'].tolist())  # Column 1
        dictkey2 = list(datasetkey['Score'].tolist())  # Column 2
        dictkeylength = len(dictkey)  # No of elements in keywords file


        store = []    #Stores the count of the words in the tweets that match with the keywords
        storescore = []  # Stores the score of thr words in the tweets that match with the keywords
        listreview = []  # Stores the text
        listreviewsizeach = []  # Stores the length of each text in the tweets file

        readtweets = open(filewithtweets, "r",encoding="utf‐8")  # Opening the file as a text file
        for line in readtweets:
            size = len(line)
            listreview.append(line)  # Stores the text
            listreviewsizeach.append(size)  # Stores the length of   each text in the tweets file

        listreviewsize = len(listreviewsizeach)  # Total Number of elements in the tweets file)

        for j in range(listreviewsize):                         #loop goes through the all tweets(elements) in the tweet file
            count = 0                                           #Stores the count
            score = 0                                           #Store the score

            for i in range(dictkeylength):                      #Loop goes through all keywords in the Keywords File
                listreview[j] = formatInput(listreview[j])      #Function formatInput is called that return WORDS as words
                newlist=solver(listreview[j])                   #function to read "#word" as word where # can be any punctuation,and "not-so-happy" as "not-so-happy"
                if dictkey[i] in newlist:                   #Checks if the keyword matches with any of the words in the tweet
                    count = count + 1                           #Increments the value of count
                    score = score + dictkey2[i]                 #Increases the value of count as per the score mentioned in the keywords file
                    print("Count:",count)
                    print("Line Number:",j)
                    print("Word:",dictkey[i])
                    print("Score:",score)
                    print("#"*100)
            if count != 0:                                      # So that score does not get divided by zero
                store.append(count)
                storescore.append(score)

            else:
                store.append(0)
                storescore.append(0)



        print(store)
        print(storescore)

        listavg=[]
        for i in range (0,len(store)):
            if store[i]!=0:
                listavg.append(storescore[i]/store[i])
            else:
                listavg.append(0)
        print(listavg)
    except IOError:
        print("Error")


compute_tweets('tweets.txt','keywords.txt')