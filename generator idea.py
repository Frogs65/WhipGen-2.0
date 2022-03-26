import random

#Rap generator functions (basic)

def load_raps():
    global rap_words
    rap_words = []
    rap_file = open("Raps.txt", "r")
    i = 0
    for line in rap_file:
        temp = line.split(",")
        while i < len(temp):
            rap_words.append(temp[i])
            i += 1
    rap_file.close()
    return rap_words


def add_rap_words(your_addition):
    #code for input from text box here

    file = open("Raps.txt", "r")
    temp = []
    for line in file:
        temp = line.split(",")
    file.close()
    second = open("Raps.txt","a")
    if len(temp) == 0:
        second.write(your_addition)
    else:
        second.write("," + your_addition)
    second.close()

def delete_word(your_addition):
    counter = 0
    for word in rap_words:
        if word == your_addition:
            rap_words.pop(counter)
            file = open("Raps.txt","w")
            print("Word succesfully deleted")
            text = ""
            for value in rap_words:
                text += value + ","
            file.write(text.rstrip(","))
            file.close()
            break
        else:
            counter+=1
    if (counter) == len(rap_words):
        print("That word is not in the list")

def generate_rap():
    outcome = random.choices(rap_words, k=4)
    rap = ""
    for i in range(0,len(outcome)):
        rap = rap + outcome[i] + " "
    return rap

#Whip generator functions (basic)

def load_whips():
    global whips
    whips = []
    whip_file = open("Whips.txt", "r")
    i = 0
    for line in whip_file:
        temp = line.split(",")
        while i < len(temp):
            whips.append(temp[i])
            i += 1
    whip_file.close()
    return whips

def add_whips(your_addition):
    #code for input from text box here

    file = open("Whips.txt", "r")
    temp = []
    for line in file:
        temp = line.split(",")
    file.close()
    second = open("Whips.txt","a")
    if len(temp) == 0:
        second.write(your_addition)
    else:
        second.write("," + your_addition)
    second.close()

def delete_whip(your_addition):
    counter = 0
    for word in whips:
        if word == your_addition:
            whips.pop(counter)
            file = open("Whips.txt","w")
            print("Whip succesfully deleted")
            text = ""
            for value in whips:
                text += value + ","
            file.write(text.rstrip(","))
            file.close()
            break
        else:
            counter+=1
    if (counter) == len(whips):
        print("That whip is not in the list")

def load_attributes():
    global whip_attributes
    whip_attributes = []
    att_file = open("Whip Attributes.txt", "r")
    i = 0
    for line in att_file:
        temp = line.split(",")
        while i < len(temp):
            whip_attributes.append(temp[i])
            i += 1
    att_file.close()
    return whip_attributes

def add_attributes(your_addition):
    #code for input from text box here

    file = open("Whip Attributes.txt", "r")
    temp = []
    for line in file:
        temp = line.split(",")
    file.close()
    second = open("Whip Attributes.txt","a")
    if len(temp) == 0:
        second.write(your_addition)
    else:
        second.write("," + your_addition)
    second.close()

def delete_attribute(your_addition):
    counter = 0
    for word in whip_attributes:
        if word == your_addition:
            whip_attributes.pop(counter)
            file = open("Whip Attributes.txt","w")
            print("Attribute succesfully deleted")
            text = ""
            for value in whip_attributes:
                text += value + ","
            file.write(text.rstrip(","))
            file.close()
            break
        else:
            counter+=1
    if (counter) == len(whip_attributes):
        print("That attribute is not in the list")

def generate_whip():
    #result = ""
    whip = random.choice(whips)
    att = random.choice(whip_attributes)
    if att == "Don't do the":
        return att + " " + whip
    if att == "continuous":
        x = random.randint(2,15)
        return "The " + att + " " + whip + " " + str(x) + " times"
    return "The " + att + " " + whip

def generate_double_whip():
    #result = ""
    whip = random.choice(whips)
    atts = random.choices(whip_attributes,k=2)
    #att_string = ""
    if atts[0] == "Don't do the" and atts[1] == "continuous":
        x = random.randint(2,15)
        return atts[0] + " " + atts[1] + " " + whip + " " + str(x) + " times"
    if atts[0] == "Don't do the":
        return atts[0] + " " + atts[1] + " " + whip
    if atts[0] == "un-" and atts[1] == "continuous":
        return "The Time Traveling " + whip
    if atts[0] == "un-":
        return "The " + atts[0] + atts[1] + " " + whip
    if atts[0] == "continuous" or atts[1] == "continuous":
        x = random.randint(2,15)
        return "The " + atts[0] + " " + atts[1] + " " + whip + " " + str(x) + " times"
    return "The " + atts[0] + " " + atts[1] + " " + whip

load_whips()
load_attributes()
print(generate_whip())
print(generate_double_whip())