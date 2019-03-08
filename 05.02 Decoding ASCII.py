# Reid Harry
# 03/06/2019
# This program's function is to encode and decode a message

def main():
    code = []
    message = ""

    for n in "We choose to go to the Moon in this decade and do the other things, not because they are easy, but because they are hard. -JFK":
        code.append(ord(n))

    print(code)
    print("")

    for n in code:
        message += chr(n)

    print(message)
main()