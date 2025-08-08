# A spam comment is definded as a text containsing
# foflowing Reywords:
# make a lot of money, buy now,
# subscribe this
# "click this" Write a propram to deteet these spams.

comment = input("Enter your comment: ").lower()

spam_keywords = [
    "make a lot of money",
    "buy now",
    "subscribe this",
    "click this"
]

for s in spam_keywords:
    if s in comment:
        print("🚨 This is a SPAM comment.")
        break
else:
    print("✅ This is NOT a spam comment.")