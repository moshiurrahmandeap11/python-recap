# this is a simple word count program that counts the number of words in a given text file.

name = input("Enter the name of the text file (with extension): ")
print("Counting words in the file:", name)

# here open() function is used to open the file in your pc and allowing you to read, write or modify the contents you want. The 'r' is a argument that specifies the mode in which the file is opened. In this case, 'r' stands for read mode, which means you can only read the contents of the file and not modify it by accident. If you want to modify the contents of the file, you can use 'w' for write mode or 'a' for append mode. [append means adding new content to the end of the file without deleting the existing content.]
handle = open(name, 'r')
print("File opened successfully!")

# here read() function is used to read the contents of the file and store it in a variable called 'text'. The read() function reads the entire contents of the file and returns it as a string. If you want to read the file line by line, you can use the readline() function instead.

# declare a variable called
counts = dict()
print("Counts dictionary initialized:", counts)

# creating a for loop to iterate through each line in the file and split the line into words using the split() function. The split() function splits a string into a list of words based on whitespace by default. Then, we use another for loop to iterate through each word in the list and update the counts dictionary with the word as the key and its count as the value.

for line in handle:
    words = line.split()
    print("Words in the line:", words)
    # now we will iterate through each word in the list of words and update the counts dictionary with the word as the key and its count as the value.

    for word in words:
        print("Current word:", word)
        # here we are using the get() method of the dictionary to get the current count of the word. If the word is not present in the dictionary, it will return 0 as the default value. Then, we add 1 to the current count and update the counts dictionary with the new count.
        counts[word] = counts.get(word, 0) + 1
        print("Updated counts dictionary:", counts)

# finally, we will print the counts dictionary to see the final word count for each word in the file.
print("Final word counts:", counts)

bigcount = None
bigword = None
# here we are using a for loop to iterate through the counts dictionary and find the word with the highest count. We initialize two variables, bigcount and bigword, to None. Then, we check if bigcount is None or if the current count is greater than bigcount. If either condition is true, we update bigcount and bigword with the current count and word.

for word, count in counts.items():
    if bigcount is None or count > bigcount:
        bigcount = count
        bigword = word

# finally, we will print the word with the highest count and its count.
print("The word with the highest count is: ", bigword, "with a count of: ", bigcount)