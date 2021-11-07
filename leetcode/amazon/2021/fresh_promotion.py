import re


def has_match(idx_code, idx_cart, cart_lst, code_lst):


    if idx_code == len(code_lst):
        return True

    if idx_cart == len(cart_lst):
        return False

    idx_item = 0
    top_item = code_lst[idx_code][idx_item]
    match = top_item == 'anything' or top_item == cart_lst[idx_cart]

    current_idx_cart = idx_cart
    if match:
        for idx_item in range(len(code_lst[idx_code])):
            top_item = code_lst[idx_code][idx_item]
            match = top_item == 'anything' or top_item == cart_lst[idx_cart]

            # print(f"{top_item} == { cart_lst[idx_cart]}")
            # print(f"{match}")

            if not match:
                return False
            idx_cart += 1

    if match: # means all items in group appeared in order, go to next group
        return has_match(idx_code + 1, idx_cart, cart_lst, code_lst)
    else:
        return has_match(idx_code, current_idx_cart + 1, cart_lst, code_lst)


def fresh_promotion_rgx(codeList, shoppingCart):
    
    s = ' '.join(shoppingCart)
    print(s)
    reg = ''
    for code in codeList:
        c = ' '.join(code)
        c = ' ' + c
        c = c.replace('anything', '\w+')
        reg += c + '[\w\s]*'
    r = re.compile(reg)
    res = r.findall(s)
    return min(1, len(res))



def fresh_promotion(codeList, shoppingCart):
    code_stack = []





    result = has_match(0, 0, shoppingCart, list(codeList))

    return 1 if result else 0






    





    
            








    


    



codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["orange", "apple", "apple", "banana", "orange", "banana"]
# 1
# codeList contains two groups - [apple, apple] and [banana, anything, banana].
# The second group contains 'anything' so any fruit can be ordered in place of 'anything' in the shoppingCart. The customer is a winner as the customer has added fruits in the order of fruits in the groups and the order of groups in the codeList is also maintained in the shoppingCart.

#
print(fresh_promotion(codeList, shoppingCart))
print('')


#
codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["apple", "orange", "apple", "apple", "banana", "orange", "banana"]

print(fresh_promotion(codeList, shoppingCart))
print('')


codeList = [["apple", "apple"], ["banana", "anything", "banana"]]
shoppingCart = ["apple", "banana", "apple", "banana", "orange", "banana"]
# 0
# The customer is not a winner as the customer has added the fruits in order of groups but group [banana, orange, banana] is not following the group [apple, apple] in the codeList.

print(fresh_promotion(codeList, shoppingCart))
print('')


codeList = [["apple", "apple"], ["apple", "apple", "banana"]]
shoppingCart = ["apple", "apple", "apple", "banana"]
# 0
# The customer is not a winner as the first 2 fruits form group 1, all three fruits would form group 2, but can't because it would contain all fruits of group 1.


print(fresh_promotion(codeList, shoppingCart))
print('')
