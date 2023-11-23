from time import sleep

new = ""
alphabet = [' ','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','_']
message = input("Enter a word: ")

for i in range(len(message)):
    for j in range(len(alphabet)):
        print(new + alphabet[j])
        sleep(0.1)
        if alphabet[j] == message[i]:
            new += message[i]
            sleep(0.1)
            break