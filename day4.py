#Write a program that takes a sentence as input and extracts the substring between the 5th and 10th characters (inclusive).
#Print the extracted substring.
str=input("Enter a string: ")
ex_str=str[4:10]
print(f"the extracted substring is {ex_str}")

#Write a program to reverse a string
str1=input("Enter a string")
rev=str1[::-1]
print("The reverse of",str1,"is",rev)

#Write a program to check for alpha numeric characters
str=input("Enter a string: ")
ans=str.isalnum()
if ans:
    print("Yes, the string contains alphanumeric characters.")
    
else:
    print("No, the string does not contains alphanumeric characters.")
 
    
#Write a program to find how many times abra has occurred in the string ‘abracadabracobra’
str='abracadabracobra'
no_of_abra=str.count('abra')
print(f"the no. of times abra occurs in {str} is {no_of_abra}")