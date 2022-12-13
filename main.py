# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def print_low(name):
    print(f'LOW, {name}')
def print_no(a):
    print(a +"less")


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

# 집합
a = set(['a', 'b', 'c'])
b = set(['a', 'k', 'l'])

#차집합
print (a - b)
#교집합
print (a & b)
#합집합
print (a | b)
# Press the green button in the gutter to run the script.

if __name__ == '__main__':
    print_no('common')
    print_low('welcome')
    print_hi('PyCharm')



# See PyCharm help at https://www.jetbrains.com/help/pycharm/
