def count_substring(string, sub_string):
    s=string
    count=0
    l=len(sub_string)
    for i in range(len(string)):
        n=i+l
        if s[i:n:1]==sub_string:
            count+=1
    return count


