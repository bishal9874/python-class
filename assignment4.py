#4.Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
def func(strings) :
    count = 0;
    for string in strings:
        if string[0] == string[len(string) - 1] and len(string) >= 2:
           count += 1;
        
    return count;  
print(func(["HH", "HeelH", "D","AytA"]))