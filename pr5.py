def greet(bot_name, birth_year):
print("Hello! My name is {0}.".format(bot_name))
print("I was created in {0}.".format(birth_year))
def remind_name():
print(&#39;Please, remind me your name.&#39;)
name = input()
print("What a great name you have, {0}!".format(name))
def guess_age():
print(&#39;Let me guess your age.&#39;)
print(&#39;Enter remainders of dividing your age by 3, 5 and 7.&#39;)
rem3 = int(input())
rem5 = int(input())
rem7 = int(input())
age = (rem3 * 70 + rem5 * 21 + rem7 * 15) % 105
print("Your age is {0}; that&#39;s a good time to start programming!".format(age))
def count():
print(&#39;Now I will prove to you that I can count to any number you want.&#39;)
num = int(input())
counter = 0
while counter &lt;= num:
print("{0} !".format(counter))
counter += 1

def test():
print("Let&#39;s test your programming knowledge.")
print("Why do we use methods?")
print("1. To repeat a statement multiple times.")
print("2. To decompose a program into several small subroutines.")
print("3. To determine the execution time of a program.")
print("4. To interrupt the execution of a program.")
answer = 2
guess = int(input())
while guess != answer:
print("Please, try again.")
guess = int(input())
print(&#39;Completed, have a nice day!&#39;)
print(&#39;.................................&#39;)
print(&#39;.................................&#39;)
print(&#39;.................................&#39;)
def end():
print(&#39;Congratulations, have a nice day!&#39;)
print(&#39;.................................&#39;)
print(&#39;.................................&#39;)
print(&#39;.................................&#39;)
input()

greet(&#39;Sbot&#39;, &#39;2021&#39;) # change it as you need
remind_name()
guess_age()
count()
test()
end()