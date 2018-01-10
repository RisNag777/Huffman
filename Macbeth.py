import heapq

Macbeth = open("Macbeth.txt", "r")
macbeth = Macbeth.read().lower() #Convert all text to lowercase

charfreq = {}
for i in range(ord('a'),ord('z')+1): #Store all letters in the dictionary
    charfreq[chr(i)] = 0
charfreq[' '] = 0
charfreq['.'] = 0
charfreq[','] = 0
charfreq['!'] = 0
charfreq['?'] = 0
charfreq['\''] = 0

for i in macbeth:
    if i in charfreq.keys():
        charfreq[i] += 1 #Store character count in the dictionary

n = 0
for i in macbeth:
    if (ord(i) >= ord('a') and ord(i) <= ord('z')) or i == ' ' or i == ',' or i == '.' or i == '!' or i == '?' or i == '\'':
        n += 1 #Find number of valid characters in the text
print("Macbeth had " + str(n) + " valid characters i.e., all letters of the alphabet along with space, period, comma, apostrophe, exclamation point and question mark")

heap = []
for value, key in charfreq.items():
    heap.append((key, value)) #Store characters and their frequencies in a heap
heapq.heapify(heap) #Min-heapify
code = {}
while len(heap) > 1:
    z = []
    x = heapq.heappop(heap) #Extract smallest element
    y = heapq.heappop(heap) #Extract second smallest element
    z = [x[0] + y[0], x[1] + y[1]] #Composite node obtained by merging x and y
    if len(x[1]) < 2: #If not a composite node
        code[x[1]] = '0' #Smallest element is always left child
    else: #If x is a composite node
        for i in code:
            if i[0] in x[1]: #Look for components of the composite node
                code[i] = '0'+code[i] #Append a 0 to the start of the components of the composite node as x is a left child
    if len(y[1]) < 2: #If not a composite node
        code[y[1]] = '1' #Second smallest element is always right child
    else: #If y is a composite node
        for i in code:
            if i[0] in y[1]: #Look for components of the composite node
                code[i] = '1' + code[i] #Append a 1 to the start of the components of the composite node as y is a right child
    heapq.heappush(heap, tuple(z)) #Push z into the heap
heapq.heappop(heap) #Pop out the final element leaving the heap empty

for i in code.keys(): #Loop through dictionary to print the character codes
    if i == ' ':
        print('space' + " - " + code[i])
    else:
        print(i + " - " +code[i])
print("\n")
print(charfreq)

tot = 0
for i in charfreq.keys():
    for j in code.keys():
        if i == j:
            tot += charfreq[i]*len(code[i]) #Find the number of bits used in encoding the text
print("Macbeth was encoded using " + str(tot) + " bits")

FLEtot = 0
for i in charfreq.keys():
    FLEtot += charfreq[i]*5 #Find the number of bits that would've been used in 5 bit fixed length encoding
print("Using a 5-bit fixed length encoding, this would have been " + str(FLEtot) + " bits long")
print("Using Huffman Coding, we saved " + str(FLEtot - tot) + " bits")