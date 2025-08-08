def rev_string(s):
    if len(s)<=1:
        return s
    else:
        return s[len(s)-1] + rev_string(s[0:len(s)-1])
    
s = input("Enter a string: ")

rev_s = rev_string(s)

print(rev_s)

# check pallindrome

if s == rev_s:
    print(f"String {s} is Pallindrome.")
else:
    print(f"String {s} is not a Pallindrome")