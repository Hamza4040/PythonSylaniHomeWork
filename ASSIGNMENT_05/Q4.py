def chkPal(string):
    if string[:]==string[::-1]:
        print("Given String ("+string.title()+") Is Palindrome")
    else:
        print("Given String Is ("+string.title()+") Not A Palindrome")

chkPal('Hamza'.lower())
chkPal('Madam'.lower())
