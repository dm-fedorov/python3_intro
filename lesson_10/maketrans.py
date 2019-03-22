# Разбираемся, как работает метод maketrans

# In[6]:

trantab = str.maketrans({'i': '1', 'e': None})
print(trantab)

s = "this is string example....wow!!!"
print(s.translate(trantab))


# In[7]:

intab = "aeiou"
outtab = "12345"
trantab = str.maketrans(intab, outtab)
print(trantab)

s = "this is string example....wow!!!"
print(s.translate(trantab))


# In[8]:

trantab = str.maketrans("", "", "sw")
print(trantab)

s = "this is string example....wow!!!"
print(s.translate(trantab))

