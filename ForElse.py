"""官方文档：
>When the items are exhausted (which is immediately when the sequence is empty), the suite in the else clause,
if present, is executed, and the loop terminates.

>A break statement executed in the first suite terminates the loop without executing the else clause’s suite.
A continue statement executed in the first suite skips the rest of the suite and continues with the next item,
or with the else clause if there was no next item.


当迭代的对象迭代完并为空时，位于else的子句将执行，而如果在for循环中含有break时则直接终止循环，并不会执行else子句。

return 跳出函数
"""


print("\n1:--------------\n")

for i in range(10):
    if i > 5:
        print("find num bigger than 5")
        break
    print(1)
print("no bigger than 5")

print('\n2:---------', '\n')

for i in range(7):
    if i > 5:
        print("find num bigger than 5")
print("no bigger than 5")

print('\n3:---------', '\n')

for i in range(10):
    if i > 5:
        print("find num bigger than 5")
    print(1)

print("no bigger than 5")