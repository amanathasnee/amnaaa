def emoji_replacer(message):

    emoji_set={
        "happy":"😊",
        "thump up":"👍",
        "love":"❤️",
        "sad":"😔",
        "angry":"😤"
              }
    
    words=message.split()
    result = []

    for word in words:
        emoji = emoji_set.get(word.lower(),word)
        result.append(emoji)
    return " ".join(result)

msg=input("Enter the message to be converted:")
print("converted message is :",emoji_replacer(msg))