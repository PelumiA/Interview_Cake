
def reverse_words(message):

    # Decode the message by reversing the words
    
    if not message: return []
    
    rev_char(message,0,len(message)-1)
    
    start = 0
    
    #for i,c in enumerate(message):
    for i in range(len(message)+1):  
        if i == len(message) or message[i] == ' ':
            rev_char(message,start,i-1)
            start = i+1
            



def rev_char(s,start,end):
    while start < end:
        s[start],s[end] = s[end], s[start]
        start += 1
        end -= 1
