#Q1
1.y
2.g
3.9
4.Myst
5.True
6.True
7.True
8.False
9.False

#Q2
prefixes = "JKLMNOPQ"
suffix = "ack"

for letter in prefixes:
    if letter == "O" or letter == "Q":
        print(letter + "u" + suffix)
    else:
        print(letter + suffix)

#Q3
def count_letters(s,l):
    count = 0
    for char in s:
        if char == l:
            count += 1
    return(count)

#Q5
v = """A last thing to note about key sentences is that academic readers expect them to be at the beginning of the paragraph. (The first sentence this paragraph is a good example of this in action!) This placement helps readers comprehend your argument. To see how, try this: find an academic piece (such as a textbook or scholarly article) that strikes you as well written and go through part of it reading just the first sentence of each paragraph. You should be able to easily follow the sequence of logic. When you’re writing for professors, it is especially effective to put your key sentences first because they usually convey your own original thinking. It’s a very good sign when your paragraphs are typically composed of a telling key sentence followed by evidence and explanation."""
lower = [' ','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','W','V','X','Y','Z']
def remove_punctuation(v):
    for char in v:
        if char not in lower:
            v = v.replace(char,'')
    l = v.split()
    print(l)
    count = 0
    y = len(v)
    for x in range(len(v)):
        if 'e' in l[x]:
            count = count + 1
    perc = (count/y)*100
    return("Your text contains",y,"words, of which",count,"(",perc,'%) contain an "e."')
print(remove_punctuation(v))

#Q7
def reverse(string):
    return(string[::-1])

#Q8
def reverse(string):
    v=(string[::-1])
    return(string+v)

#Q9
def remove_letter(l,s):
    for char in s:
        if char == l:
            s = s.replace(l,'')
    return(s)

#Q10
def is_palindrome(s):
    if s == s[::-1]:
        return("is palindrome")
    else:
        return("is not palindrome")

#Q11
def count(sub,main):
    return(main.count(sub))

#Q12
def remove(sub, main):
    main = main.replace(sub,"",1)
    return(main)

#Q13
def remove(sub, main):
    if sub in main:
        main = main.replace(sub,'')
    return(main)
