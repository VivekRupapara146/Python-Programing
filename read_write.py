with open("Input.txt", "r") as f_in:
    content = f_in.read()

modified_content = content.upper()

with open("Output.txt", "w") as f_out:
    f_out.write(modified_content)

with open("Output.txt", "r") as f_out:
    text = f_out.read()
    print(text)