def string_palindrome_check(s):
    s1 = s
    i = 0
    j = len(s)-1
    while i < j:
        s[i],s[j] = s[j],s[i]
        i += 1
        j -= 1 
    if s1 == s: 
        return True
    else:  
        return False 


    