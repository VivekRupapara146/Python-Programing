# python program to remove a list element and stripping it at same time
def rem(l , w):
    n = []
    for items in l:
        if (items!=word):
            n.append(items.strip(w))
    return n

l = ["Vivek", "Ayran", "Mahek", "Kiran"]

word = input("Enter word to remove from the list and strip it form the list: ")

print(f"Updated list is {rem(l , word)}")

