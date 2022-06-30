# Використовуючи Python напиши програму для шифрування і дешифрування тексту за допомогою шифру Цезаря
k=int(input('Для шифрування введіть 0, для дешифрування - 1: '))
a=str(input('Введіть текст: ').split())
a=a[2:len(a)-2]
key=3
b=''
a=a.lower()
if k==0:
    for i in range(len(a)):
        n=ord(a[i])
        if n>=97 and n<=122:
            n += 3
            if n>122:
                n-=26
            h = chr(n)
            b += h
        else:
            b+=a[i]

else:

    for i in range(len(a)):
        n=ord(a[i])
        if n >= 97 and n <= 122:
            n-=3
            if n<97:
                n=123-(97-n)
            h = chr(n)
            b += h
        else:
            b+=a[i]
print(b)