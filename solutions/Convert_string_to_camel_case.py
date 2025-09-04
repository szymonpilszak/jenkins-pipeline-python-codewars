def to_camel_case(text):
    mytext = ""
    capitalize_next = False

    if text and text[0].isupper():
        first_is_upper = True
    else:
        first_is_upper = False

    for char in text:
        if char == "-" or char == "_":
            capitalize_next = True
        else:
            if capitalize_next:
                mytext += char.upper()
                capitalize_next = False
            else:
                mytext += char

    if first_is_upper and mytext:
        mytext = mytext[0].upper() + mytext[1:]

    return mytext
