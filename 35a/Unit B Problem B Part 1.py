'''
Magnus Chiu
CIS 41A Spring 2022
Unit B, Problem B Script 1
'''
string = str(input("Enter a string: "));
print(string.isupper());
print(string.isdigit());
print(string.isalpha());

text = "Type, type, type away. \nCompile. Run. Hip hip hooray! \nNo error today!";
print(text);

quote = "And now for something completely different";
print(quote[0:6]);
print(quote[-4:]);
print(quote[::2]);
print(quote[::-1]);

pattern1 = ".~*'";
pattern2= pattern1 + pattern1[::-1];
print(pattern2+pattern2+pattern2+pattern2+pattern2);

'''
Execution results:
Enter a string: ABC123
True
False
False
Type, type, type away. 
Compile. Run. Hip hip hooray! 
No error today!
And no
rent
Adnwfrsmtigcmltl ifrn
tnereffid yletelpmoc gnihtemos rof won dnA
.~*''*~..~*''*~..~*''*~..~*''*~..~*''*~.
'''