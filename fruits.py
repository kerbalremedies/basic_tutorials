def playing_with_fruits():
    fruits = ['orange', 'apple', 'pear', 'banana', 'kiwi', 'apple', 'banana']
    print("The number of apples is ", fruits.count('apple'))
    print("The number of Tangerines is ", fruits.count('tangerine'))
    print("Banana is first found in position ", fruits.index('banana'))
    print("Banana is next found in position ", fruits.index('banana', 4))
    fruits.reverse
    fruits.append('grapes')
    fruits.sort()
    fruits
    fruits.pop()

playing_with_fruits()