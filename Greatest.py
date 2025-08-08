# greatest of four no.
a = 6 
b = 4
c = 5
d = 3

# status = (
#     "A is Greatest of all" if a>b>c>d else
#     "B is Greatest of all" if b>a>c>d else 
#     "C is Greatest of all" if c>b>a>d else
#     "D is greatest of all"
# )

# print(status)

maximum = max(a, b, c, d)

status = (
    "A is Greatest of all" if a == maximum else
    "B is Greatest of all" if b == maximum else 
    "C is Greatest of all" if c == maximum else
    "D is greatest of all"
)
