s = "python programming"
print("captalize :",s.capitalize())


print("title :",s.title()) # this command is used to change the caps  first letter in each every word.

print("count :",s.count("y"))
print("count with in range  :", s.count("o",0,8))

print("Endswith :",s.endswith("ing"))
print("Endswith :",s.endswith("ings"))

print("index:",s.index("y"))

print("find:",s.find("a"))
print("find within range :",s.find("a",1,13))
print("find within range :",s.find("a",1,8))

s1 = "PYThoN54453"
print("s1 = ",s1.isalnum())

s2 = "765"
print("s2 =",s2.isdigit())

s3 = "alpha"
print("s3 = ",s3.isalpha())

s4 = "alpha"
print("s4 = ",s4.islower())

s5 = "Good"
print("s5 = ",s5.isupper())

s6 = "a y "
print("s6 = ",s6.isspace()) # i don't understood

s6 = "pYtHoN"
print(s6.swapcase())

# strip,lstrip,rstrip

s7 = "*python*"
print(s7.strip("*"))
print(s7.lstrip("*"))
print(s7.rstrip("*"))
print(s7.strip("*p"))




