from os import system
system('clear')
S = "Spam"
print(len(S))

print(S[0])
print(S[-1])
print(S[len(S)-1])
print(S[1:3])
print(S[1:])
print(S[0:3])
print(S[:3])
print(S[:-1])
print(S[:])

print(S + "murciegalo")
print(S * 15)

# S[0] = 'z' # Can't do that becasue strings
# But we can do this
print('Z' + S[1:])

S = "albondiga"
L = list(S)
print(L)
L[2] = 'f'
print(''.join(L))

B = bytearray(b"spam")
B.extend(b"eggs")
print(B)
print(B.decode())

S = "Spam"
print(S.find("pa"))

print(S.replace("pa", "io"))

print(dir(S))

print()