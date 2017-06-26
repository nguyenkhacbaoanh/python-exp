'''thuat toan de dao nguoc cac ky tu alphabet trong 1 chuoi string
con cac ki tu khac ko thay doi ky tu dac biet nhu: * $ % . @ '''

# reverse string
s = 'Hello World'
#by function
print(''.join(reversed(s)))
#by method string
print(s[::-1])

#handling string
st='example'
print(st.center(10,'*'))

a='Python\nString\nConcepts'
print(a.splitlines())

b="abefcd"
print(b.partition('cd'))

c='Welcome\tTo\tPython\tProgramming'
print(c.expandtabs())

d = ['Python', 'Python quiz', 'Python String', 'Python Interview', 'Python questions']
print("\n".join(d))

s = "a.b,c@d"