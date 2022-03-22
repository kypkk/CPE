import math

# # Vito's family
# datas = int(input())
# for i in range(datas):
#     data = input()
#     fam = list(map(int, data.split()))
#     fam_num = fam.pop(0)
#     dis = 0
#     fam.sort()
#     num = fam[math.floor(fam_num/2)]
#     for j in range(fam_num):
#         if(fam[j] < num):
#             dis = dis + (num - fam[j])
#         else:
#             dis = dis + (fam[j] - num)
#     print(dis)

# # 2 the 9s
# while True:
#     n = input()
#     if n == '0':
#         break
#     if int(n) % 9 != 0:
#         print(f"{n} is not a multiple of 9.")
#     else:
#         a = n
#         sum = 0
#         degrees = 0
#         while sum != 9:
#             if degrees != 0:
#                 n = str(sum)
#                 sum = 0
#             degrees += 1
#             for i in n:
#                 sum += int(i)
#         print(f"{a} is a multiple of 9 and has 9-degree {degrees}.")

# # You can say 11
# while True:
#     n = input()
#     if n == '0':
#         break
#     length = len(n)
#     sum_odd = 0
#     sum_even = 0
#     i = 0;
#     while i < length:
#         sum_odd = sum_odd + int(n[i])
#         i += 2
#     i = 1
#     while i < length:
#         sum_even = sum_even + int(n[i])
#         i += 2
#     if sum_odd >= sum_even:
#         dif = sum_odd - sum_even
#         if dif % 11 == 0:
#             print(f"{n} is a multiple of 11.")
#         else:
#             print(f"{n} is not a multiple of 11.")
#     if sum_odd < sum_even:
#         dif = sum_even - sum_odd
#         if dif % 11 == 0:
#             print(f"{n} is a multiple of 11.")
#         else:
#             print(f"{n} is not a multiple of 11.")

# # Primary Arithmetic
# while True:
#     string = input()
#     if string == "0 0":
#         break
#     numbers = string.split()
#     length1 = len(numbers[0])
#     length2 = len(numbers[1])
#     carryCount = 0
#     num1 = numbers[0]
#     num2 = numbers[1]
#     out = 0

#     if length1 < length2:
#         length = length1
#         for i in range(length):
#             if(int(num1[length1 - i - 1]) + int(num2[length2 - i - 1]) + out) > 9:
#                 carryCount += 1
#                 if(i == length - 1) and (int(num1[length1 - i - 1]) + int(num2[length2 - i - 1]) + out > 9) and (1 + int(num2[length2 - i - 2]) > 9):
#                     carryCount += 1
#                 out = 1
#             else:
#                 out = 0

#     if length1 > length2:
#         length = length2
#         for i in range(length):
#             if(int(num1[length1 - i - 1]) + int(num2[length2 - i - 1]) + out) > 9:
#                 carryCount += 1
#                 if(i == length - 1) and (int(num1[length1 - i - 1]) + int(num2[length2 - i - 1]) + out > 9) and (1 + int(num1[length1 - i - 2]) > 9):
#                     carryCount += 1
#                 out = 1
#             else:
#                 out = 0
#     if length1 == length2:
#         length = length2
#         for i in range(length):
#             if (int(num1[length1 - i - 1]) + int(num2[length2 - i - 1]) + out) > 9:
#                 carryCount +=1
#                 out = 1
#             else:
#                 out = 0
#     if carryCount == 0:
#         print("No carry operation.")
#     elif carryCount == 1:
#         print(f"{carryCount} carry operation.")
#     else:
#         print(f"{carryCount} carry operations.")

# #  3n + 1 problem
# def cl(n):
#     if n == 1:
#         return 1
#     elif n % 2 == 1:
#         return cl(3 * n + 1) + 1
#     else:
#         return cl(n / 2) + 1

# while True:
#     a,b=input().split()
#     a=int(a)
#     b=int(b)
#     mx=0
#     l = min(a, b)
#     r = max(a, b)
#     for i in range(l,r+1):
#         mx=max(mx,cl(i))
#     print(a,b,mx)

# # brick wall problem
# def wall(n):
#     if n == 1:
#         return 1
#     if n == 2 :
#         return 2
#     a = 1
#     b = 2
#     for i in range(1, n - 1):
#         x = b
#         b = a + b
#         a = x
#     return b

# while True:
#     wall_length = int(input())
#     if wall_length == 0:
#         break
#     print(wall(wall_length))


# # tex quotes
# k=0
# while True:
#     try:
#         a=input()
#         for i in range(len(a)):
#             if a[i]=='"':
#                 if k%2==0:
#                    print("``",end="")
#                 else:
#                     print("''",end="")
#                 k += 1
#             else:
#                 print(a[i],end="")
#         print()
#     except:
#         break

# # dangerous dive
# while True:
#     try:
#         num_1,num_2 = input().split()
#         people = input().split()
#         s = ""
#         a = []
#         for i in range(int(num_1)):
#             a.append(int(i) + 1)
#         for i in people:
#             a.remove(int(i))
#         if a:
#             for i in a:
#                 if s == "":
#                     s += str(i)
#                 else:
#                     s = s + ' ' + str(i)
#         else:
#             s = "*"
#         print(s)
#     except:
#         break

# # bangla number
# i = 0
# while True:
#     try:
#         i += 1
#         number = int(input())
#         x = [0,0,0,0,0,0,0,0,0,0]
#         str = "" 
#         x[9] = number % 100
#         x[8] = math.floor(number / 100) % 10
#         x[7] = math.floor(number / 1000) % 100
#         x[6] = math.floor(number / 100000) % 100
#         x[5] = math.floor(number / 10000000) % 100
#         x[4] = math.floor(number / 1000000000) % 10
#         x[3] = math.floor(number / 10000000000) % 100
#         x[2] = math.floor(number / 1000000000000) % 100
#         x[1] = math.floor(number / 100000000000000) % 100
#         x[0] = math.floor(number / 10000000000000000) % 100
#         str += f"{i}. "
#         if x[0] != 0:
#             str += f"{x[0]} shata "
#         if x[1] != 0:
#             str += f"{x[1]} kuti "
#         elif x[0] != 0:
#             str += f"kuti "
#         if x[2] != 0:
#             str += f"{x[2]} lakh "
#         if x[3] != 0:
#             str += f"{x[3]} hajar "
#         if x[4] != 0:
#             str += f"{x[4]} shata "
#         if x[5] != 0:
#             str += f"{x[5]} kuti "
#         elif x[0] != 0 or x[2] != 0 or x[3] != 0 or x[4] != 0 or x[1] != 0:
#             str += f"kuti "
#         if x[6] != 0:
#             str += f"{x[6]} lakh "
#         if x[7] != 0:
#             str += f"{x[7]} hajar "
#         if x[8] != 0:
#             str += f"{x[8]} shata "
#         if x[9] != 0:
#             str += f"{x[9]}"
#         if x[0] == 0 and x[1] == 0 and x[2] == 0 and x[3] == 0 and x[4] == 0 and x[5] == 0 and x[6] == 0 and x[7] == 0 and x[8] == 0 and x[9] == 0:
#             str += f"0"
#         print(str)

#     except:
#         break    

# # tex quote
# a = 0
# while True:
#     try:
#         s = input()
#         ans = ""
#         for i in range(len(s)):
#             if s[i] == '"' and a == 0:
#                 ans += "``"
#                 a = 1
#             elif s[i] == '"' and a == 1:
#                 ans += "''"
#                 a = 0
#             else:
#                 ans += s[i]
#         print(ans)
#     except:
#         break


# # list of conquest
# num = int(input())
# countries = {} # 宣告一個 countries dictionary
# for i in range(num):
#     country = input().split()[0] # 獲得每次輸入的第一個字 也就是國家名字
#     if countries.__contains__(country): # 如果我的 dictionary 中已經存在這個國家那麼就將他的 value += 1
#         value = countries[country] + 1
#     else:                       # 如果沒有那麼他的 value 就是 1
#         value = 1
#     country = {country: value}  # 將名字與 value 合成一個 key value pair
#     countries.update(country)   # 將新增的 key value pair update 至 dictionary 中
# country_name = sorted(countries) #將 dictionary 中的 key 排序存入 country_name
# for i in country_name:
#     print(f"{i} {countries[i]}") # 印出 country name 以及 它在 dictionary 中的 value
    
# # Decode the Mad man
# while True:
#     try:
#         s = input()
#         ans = ""
#         for i in s:
#             if i == 'd':
#                 ans += 'a'
#             elif i == 'm':
#                 ans += 'b'
#             elif i == 'b':
#                 ans += 'c'
#             elif i == 'g':
#                 ans += 'd'
#             elif i == 't':
#                 ans += 'e'
#             elif i == 'h':
#                 ans += 'f'
#             elif i == 'j':
#                 ans += 'g'
#             elif i == 'k':
#                 ans += 'h'
#             elif i == 'p':
#                 ans += 'i'
#             elif i == 'l':
#                 ans += 'j'
#             elif i == ';':
#                 ans += 'k'
#             elif i == "'":
#                 ans += 'l'
#             elif i == '.':
#                 ans += 'm'
#             elif i == ',':
#                 ans += 'n'
#             elif i == '[':
#                 ans += 'o'
#             elif i == ']':
#                 ans += 'p'
#             elif i == 'e':
#                 ans += 'q'
#             elif i == 'y':
#                 ans += 'r'
#             elif i == 'f':
#                 ans += 's'
#             elif i == 'u':
#                 ans += 't'
#             elif i == 'o':
#                 ans += 'u'
#             elif i == 'n':
#                 ans += 'v'
#             elif i == 'r':
#                 ans += 'w'
#             elif i == 'v':
#                 ans += 'x'
#             elif i == 'i':
#                 ans += 'y'
#             elif i == 'c':
#                 ans += 'z'
#             elif i == '3':
#                 ans += '1'
#             elif i == '4':
#                 ans += '2'
#             elif i == '5':
#                 ans += '3'
#             elif i == '6':
#                 ans += '4'
#             elif i == '7':
#                 ans += '5'
#             elif i == '8':
#                 ans += '6'
#             elif i == '9':
#                 ans += '7'
#             elif i == '0':
#                 ans += '8'
#             elif i == '-':
#                 ans += '9'
#             elif i == '=':
#                 ans += '0'
#             elif i == '/':
#                 ans += ','
#             elif i == "\\":
#                 ans += '['
#             elif i == "2":
#                 ans += '`'
#             else:
#                 ans += ' '
#         print(ans)
#     except:
#         break

# # Summing Digits
# def summing_digits(n):
#     if n < 10:
#         return n
#     else:
#         sum = 0
#         while n != 0:
#             sum += n % 10
#             n = math.floor(n / 10)
#         return summing_digits(sum) 
# while True:
#     number = int(input())
#     if number == 0:
#         break
#     else:
#         print(summing_digits(number))

# # common permutation
# while True:
#     try:
#         line1 = input()
#         line2 = input()
#         a = {}  # create a dictionary for the first string
#         b = {}  # create a dictionary for the second string
#         ans = "" # create a string for my answer
#         # the first for loop stores the characters in the first string to a dictionary
#         for i in line1:
#             if a.__contains__(i):
#                 value = a[i] + 1
#                 a.update({i: value})
#             else :
#                 a.update({i: 1})
#         # the second nested for loop store the same characters in to the b dictionary
#         for i in a:
#             for j in line2:
#                 if j == i:
#                     if b.__contains__(i):
#                         value = b[i] + 1
#                         b.update({i: value})
#                     else :
#                         b.update({i: 1})
#         bname = sorted(b) # sort the sames characters in alphbetical order
#         # see whether the character appear in a or b less then add to the answer string
#         for i in bname:
#             if(b[i] < a[i]):
#                 ans += i * b[i]
#             else:
#                 ans += i * a[i]
#         print(ans)
#     except:
#         break

# # dooms day
# # 運用每個月的 dooms day 計算當個月的 dooms day 距離星期一是多少
# # 然後就將日期平移多少 %7 得出來是 1 就是星期一 2 就是星期二......
# datas = int(input())
# for i in range(datas):
#     month, date = input().split()
#     if int(month) == 1:
#         date = (int(date) + 5) % 7
#         if date == 1:
#             print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 2:
#         date = (int(date) + 1 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 3:
#         date = (int(date) + 1 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 4:
#         date = (int(date) + 4 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 5:
#         date = (int(date) + 6 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 6:
#         date = (int(date) + 2 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 7:
#         date = (int(date) + 4 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 8:
#         date = (int(date)) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 9:
#         date = (int(date) + 3 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 10:
#         date = (int(date) + 5 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 11:
#         date = (int(date) + 1 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")
#     if int(month) == 12:
#         date = (int(date) + 3 ) % 7
#         if date == 1:
#              print("Monday")
#         elif date == 2:
#             print("Tuesday")
#         elif date == 3:
#             print("Wednesday")
#         elif date == 4:
#             print("Thursday")
#         elif date == 5:
#             print("Friday")
#         elif date == 6:
#             print("Saturday")
#         elif date == 0:
#             print("Sunday")

# # jolly jump
# while True:
#     try:
#         inp = input().split()
#         s = int(inp[0])
#         arr = []
#         sub = []
#         count = 0
#         for i in range(s):
#             arr.append(int(inp[i+1]))
#         for i in range(s - 1):
#             if arr[i] < arr[i+1]:
#                 sub.append(arr[i+1] - arr[i])
#             elif arr[i] > arr[i+1]:
#                 sub.append(arr[i] - arr[i+1])
#         for i in range(1, s):
#             if sub.__contains__(i):
#                 count += 1
#                 sub.remove(i)
#         if count == s - 1:
#             print("Jolly")
#         else:
#             print("Not jolly") 
#     except:
#         break

# # what is the probability
# datas = int(input())
# for i in range(datas):
#     n, p, i = input().split()
#     n = int(n)
#     p = float(p)
#     i = int(i)
#     ans = p * ((1 - p) ** (i - 1))/(1 - ((1 - p) ** n))
#     ans = str(round(ans,4))
#     while len(ans) < 6:
#         ans += '0'
#     print(ans)

# # the hotel with infinite room
# while True:
#     try:
#         s, d = input().split()
#         s = int(s)
#         d = int(d)
#         c = ((2 * d) + (s ** 2) - s)
#         i = (-1 + math.sqrt(1 - 4 * (-c)))/2
#         i = math.ceil(i)
#         print(i)
#     except:
#         break

# # 498
# while True:
#     try:
#         number = int(input())
#         coefficient = input().split()
#         leng = len(coefficient)
#         sum = 0
#         coefficient.reverse()
#         for i in range(1, leng):
#             sum += int(coefficient[i]) * i * (number ** (i - 1))
#         print(sum)
#     except:
#         break

# # beat the spread
# datas = int(input())
# for i in range(datas):
#     n,m = input().split()
#     n = int(n)
#     m = int(m)
#     if (n + m) % 2 == 1 or (n - m) % 2 == 1 or n - m < 0:
#         print("impossible")
#         continue
#     x = int((n + m) / 2)
#     y = int((n - m) / 2)
#     print(x, y)

# # Symmetric Matrix
# # 要判斷是否為一個對稱矩陣
# # 只要看第1個元素是否等於第n個元素 count 加 1
# # 第二個元素是否等於第n-1個元素...... count 再加 1
# # 一直判斷到最中間 n為矩陣的大小
# # 若其中有一個元素小於零則說明這也不是個對稱矩陣因此讓 count 減 1
# # 若最後count 等於矩陣大小的一半說明這是對稱矩陣 
# # 不是則不是
# datas = int(input())
# for i in range(datas):
#     line1 = input()
#     rows = int(line1.split()[2])
#     size = int(line1.split()[2]) ** 2
#     arr = []
#     count = 0
#     for j in range(rows):
#         mat = input().split()
#         for k in mat:
#             k = int(k)
#             if k < 0:
#                 count -= 1
#             arr.append(k)
#     half = math.floor(size / 2)
#     for j in range(half):
#         if arr[j] == arr[size - j - 1]:
#             count += 1
#     if count == half:
#         print(f"Test #{i + 1}: Symmetric.")
#     else:
#         print(f"Test #{i + 1}: Non-symmetric.")

# # Square Numbers
# # 欲判斷兩整數之間有多少完全平方數
# while True:
#     a, b = input().split()
#     if a == '0' and b == '0':
#         break
#     a = math.ceil(int(a) ** 0.5)
#     b = math.floor(int(b) ** 0.5)
#     print(b - a + 1)

# # B2-Sequence
# case = 0
# while True:
#     try:
#         case += 1
#         datas = int(input())
#         numbers = input().split()
#         numbers = list(map(int, numbers))
#         leng_n = len(numbers)
#         sums = []
#         b2 = 1
#         for i in range(leng_n):
#             for j in range(i, leng_n):
#                 sums.append(numbers[i] + numbers[j])

#         leng_s = len(sums)
#         for i in range(leng_s):
#             for j in range(i + 1, leng_s):
#                 if sums[i] == sums[j]:
#                     print(f"Case #{case}: It is not a B2-Sequence.")
#                     b2 = 0
#                     break
#             if b2 == 0:
#                 break
#         if b2 == 1:
#             print(f"Case #{case}: It is a B2-Sequence.")
#     except:
#         break

# # Back to High School Physics
# while True:
#     try:
#         v, t = input().split()
#         v = int(v)
#         t = int(t)
#         print(2 * v * t)
#     except:
#         break

# # an easy problem
# def isN(number_str):
#     count_zero = 0
#     x = 0
#     N = 0
#     for i in number_str:
#         if i == '0':
#             count_zero += 1
#     if count_zero == len(number_str):
#         return 2
#     for i in number_str:
#         if '1' <= i <= '9':
#             x = int(i) + 1
#         elif 'A' <= i <= 'Z':
#             x = ord(i) - 54
#         elif 'a' <= i <= 'z':
#             x = ord(i) - 60
#         if x > N:
#             N = x
#     value = 0
#     for i in range(N, 62):
#         for j in range(len(number_str)):
#             if '0' <= number_str[j] <= '9':
#                 value += int(number_str[j]) * (i ** (len(number_str) - j - 1))
#             if 'A' <= number_str[j] <= 'Z':
#                 value += (ord(number_str[j]) - 55) * (i ** (len(number_str) - j - 1))
#             if 'a' <= number_str[j] <= 'z':
#                 print(ord(number_str[j]) - 61)
#                 value += (ord(number_str[j]) - 61) * (i ** (len(number_str) - j - 1))
#         if value % (i - 1) == 0:
#             return i
# while True:
#     try:
#         number = input()
#         print(isN(number))
#     except:
#         break

# # Fibonaccimal Base
# fibo = [1, 2]
# for i in range(2,40):
#     fibo.append(fibo[i-1] + fibo[i-2])

# datas = int(input())
# for i in range(datas):
#     number = int(input())
#     value = number
#     ans = ""
#     switch = 0
#     for i in range(39, -1, -1):
#         if number // fibo[i] == 1:
#             ans += '1'
#             number -= fibo[i]
#             switch += 1
#         elif switch > 0 and number // fibo[i] == 0:
#             ans += '0'
#     print(f"{value} = {ans} (fib)")

# # fourth point
# while True:
#     try:
#         g = []
#         a = input()
#         g = a.split()
#         gx = 0
#         gy = 0
#         gx_arr = []
#         gy_arr = []
#         #print(len(g)//2)
#         for i in range(len(g) // 2):
#             gx += float(g[i * 2])
#             gx_arr.append(float(g[i * 2]))
#             gy += float(g[i*2+1])
#             gy_arr.append(float(g[i * 2+1]))
#         for i in range(4):
#             for j in range(i+1,4):
#                 if gx_arr[i] == gx_arr[j] and gy_arr[i] == gy_arr[j]:
#                     gx -= 3 * gx_arr[i]
#                     gy -= 3 * gy_arr[i]
#         print(f"{gx:.3f} {gy:.3f}")
#     except:
#         break

# # Funny Encryption Method
# datas = int(input())
# for i in range(datas):
#     number = input()            # the input
#     decimal_value = int(number) # the decimal value of the input
#     hexa_value = 0              # the variable to save the hexadecimal value of the input 
#     decimal_binary = ""         # the variable to save the binary representation of the decimal value of the input
#     hexa_binary = ""            # the variable to save the binary representation of the hexadecimal value of the input
#     a = 0                       # the counter of the 1s of the binary representation of the decimal value of the input
#     b = 0                       # the counter of the 1s of the binary representation of the hexadecimal value of the input
#     for j in range(len(number)):# the for loop is use to compute of the hexadecimal value of the input 
#         hexa_value += int(number[j]) * 16 ** (len(number) - j - 1)
#     while decimal_value > 0:    # this while loop is use to compute the binary representation of the decimal value of the input 
#         decimal_binary = str(decimal_value % 2) + decimal_binary
#         decimal_value = decimal_value // 2
#     while hexa_value > 0:       # this while loop is use to compute the binary representation of the hexadecimal value of the input
#         hexa_binary = str(hexa_value % 2) + hexa_binary
#         hexa_value = hexa_value // 2
#     for i in decimal_binary:    # this for loop is use to compute the 1s in the binary representation of the decimal value of the input 
#         if i == '1':            
#             a += 1
#     for i in hexa_binary:       # this for loop is use to compute the 1s in the binary representation of the hexadecimal value of the inpur 
#         if i == '1':
#             b += 1
#     print(a, b)                 # print the answer

# # Parity
# while True:
#     a = int(input())
#     a_binary = ""
#     counter = 0
#     if a == 0:
#         break
#     while a > 0:
#         a_binary = str(a % 2) + a_binary
#         a = a // 2
#     for i in a_binary:
#         if i == '1':
#             counter += 1
#     print(f"The parity of {a_binary} is {counter} (mod 2).")

# # Cheapest Base
# cases = int(input())                                # how many cases
# for i in range(cases):                              # for each cases
#     cost = []                                       # the array use to save the costs for each cases
#     for j in range(4):                              # input costs for each cases
#         a = input().split()
#         for k in a:
#             cost.append(int(k))
#     print(f"Case {i + 1}:")                         # print case {i}
#     datas = int(input())                            # input how many datas for each cases
#     for j in range(datas):                          # for each datas                                    
#         a = int(input())                            # input data
#         a_val = a                                   # save the value of the data
#         min_cost = 999999999                        # use a very large number to save the cost 
#         ans = ""                                    # the answer
#         for k in range(35):                         # from 2 to 36
#             rep = ""                                # the variable save each representation from 2 to 36
#             temp_cost = 0                           # temp cost of each representation from 2 to 36
#             a = a_val                               # reset a to it initial value since a will become 0 after the computation of each representation
#             while a > 0:                            # compute the representation of base 2 to 36
#                 char = a % (k + 2)
#                 a = a // (k + 2)
#                 if char > 9 :
#                     char = chr(char + 55)
#                 else:
#                     char = str(char)
#                 rep = char + rep
#             # print(rep)
#             for l in rep:                           # compute temp_cost for representation from 2 - 35
#                 if '0' <= l <= '9':
#                     temp_cost += cost[int(l)]
#                 if 'A' <= l <= 'Z':
#                     temp_cost += cost[ord(l)-55]
#             if temp_cost < min_cost:                # if the temp_cost smaller than min_cost    
#                 ans = ""                            # make ans become a new empty string
#                 min_cost = temp_cost                # make the min_cost = temp_cost
#                 ans = ans + str(k + 2)              # and add the base to ans
#             elif temp_cost == min_cost:             # else if the temp_cost == min_cost
#                 ans = ans + ' ' + str(k + 2)        # add the base to ans
#         print(f"Cheapest base(s) for number {a_val}: {ans}") # print the answer 

# # can you solve it
# datas = int(input())
# for i in range(datas):
#     x1, y1, x2, y2 = input().split()
#     x1 = int(x1)
#     x2 = int(x2)
#     y1 = int(y1)
#     y2 = int(y2)
#     first_sum = 0
#     second_sum = 0
#     for j in range(x1 + y1 + 1):
#         first_sum += j
#     for j in range(x2 + y2 + 1):
#         second_sum += j
#     first_sum += x1
#     second_sum += x2
#     print(f"Case {i+1}: {second_sum - first_sum}")


# # Hartals
# datas = int(input())
# for i in range(datas):
#     days = int(input())
#     partys = int(input())
#     d = []
#     hartialDays = []
#     for j in range(partys):
#         d.append(int(input()))
#     for i in d:
#         a = i                       # save the initial i so that every time we only add the initial i
#         while i <= days:
#             if i % 7 == 6 or i % 7 == 0 or hartialDays.__contains__(i):
#                 i += a
#                 continue
#             hartialDays.append(i)   # append the days that are hartial
#             i += a
#     # print(hartialDays)
#     print(len(hartialDays))

# # largest squares
# def isN(square, a, b, counter, row, col):
#     m = a - (counter // 2)
#     n = b - (counter // 2)
#     if m < 0 or n < 0:
#         print(counter - 2)
#         return
#     x = 0
#     for i in range(counter):
#         for j in range(counter):
#             if m + i > (row - 1) or n + j > (col - 1):
#                 print(counter - 2)
#                 return
#             elif square[m + i][n + j] == square[a][b]:
#                 x += 1
#     if x == counter ** 2:
#         isN(square, a, b, counter + 2, row, col)
#     else:
#         print(counter - 2)

# datas = int(input())
# for i in range(datas):
#     m, n, q = input().split()
#     m = int(m)
#     n = int(n)
#     q = int(q)
#     square = []
#     print(m, n, q)
#     for j in range(m):
#         square.append(input())
#     for j in range(q):
#         a ,b = input().split()
#         a = int(a)
#         b = int(b)
#         isN(square, a, b, 3, m, n)

# # all you need is love
# # 將兩數換成十進位用輾轉相除找出最大公因數
# # 若最大公因數為 1 則為第二種情況
# datas = int(input())
# for i in range(datas):
#     a = input()
#     b = input()
#     a_value = 0
#     b_value = 0
#     for j in range(len(a)):
#         a_value += int(a[j]) * 2 ** (len(a) - j - 1)
#     for j in range(len(b)):
#         b_value += int(b[j]) * 2 ** (len(b) - j - 1)
#     while a_value > 0 and b_value > 0:
#         if a_value > b_value:
#             a_value = a_value % b_value
#         else:
#             b_value = b_value % a_value
#     if (a_value == 0 and b_value != 1) or (b_value == 0 and a_value != 1):
#         print(f"Pair #{i+1}: All you need is love!")
#     else:
#         print(f"Pair #{i+1}: Love is not all you need!")

# # Divide, But Not Quite Conquer!
# while True:
#     try:
#         a, b = input().split()
#         a = int(a)
#         b = int(b)
#         arr = []
#         ans = 1
#         output = ""
#         if b == 1 or b == 0:
#             print("Boring!")
#             ans = 2
#             continue
#         while a != 1:
#             if a % b != 0:
#                 print("Boring!")
#                 ans = 2
#                 break
#             else:
#                 arr.append(a)
#                 a = a / b
#         if ans == 1:
#             for i in arr:
#                 output = output + str(int(i)) + ' ' 
#             output += '1'
#             print(output)
            
#     except:
#         break

# # Simply Emirp
# while True:
#     try:
#         number = int(input())
#         value = number
#         is_p = 1
#         is_e = 1
#         for i in range(2, int(number ** 0.5) + 1):
#             if number % i == 0:
#                 is_p = 0
#                 print(f"{value} is not prime. ")
#                 break
#         if is_p == 1:
#             new_number = ""
#             while number > 0:
#                 x = number % 10
#                 new_number += str(x)
#                 number = int(number / 10)
#             new_number = int(new_number)
#             if new_number == value:
#                 print(f"{value} is prime. ")
#             else:
#                 for i in range(2, int(new_number ** 0.5) + 1):
#                     if new_number % i == 0:
#                         print(f"{value} is prime. ")
#                         is_e = 0
#                         break
#                 if is_e == 1:
#                     print(f"{value} is emirp. ")
#     except:
#         break

# A mid-summer nights dream
while True:
    try:
        datas = int(input())
        arr = []
        for i in range(datas):
            x = int(input())
            arr.append(x)
        arr.sort()
        a = 0
        b = 0
        c = 0
        if len(arr) % 2 == 1:
            half = int(math.ceil(len(arr) / 2) - 1)
            a = arr[half]
            counter = 0
            for i in arr:
                if i == arr[half]:
                    counter += 1
            b = counter
            c = 1
        if len(arr) % 2 == 0:
            half = int(math.ceil(len(arr) / 2) - 1)
            a = arr[half]
            if arr[half + 1] == arr[half]:
                counter = 0
                for i in arr:
                    if i == arr[half]:
                        counter += 1
                b = counter
                c = 1
            else:
                counter = 0
                for i in arr:
                    if i == arr[half] or i == arr[half + 1]:
                        counter += 1
                b = counter
                c = arr[half + 1] - arr[half] + 1
        print(a,b,c)
    except:
        break