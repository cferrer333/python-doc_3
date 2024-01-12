
def shoppingList():
    shopping_list = []
    while True:
        item = input("Do you want to: Show/Add/Delete/Order/ or Quit? ")
        if item.lower() == 'show':
            print(shopping_list)
        elif item.lower() == 'add':
            add_item = input("What would you like to add to your shopping list? ")
            shopping_list.append(add_item)
        elif item.lower() == 'delete':
            del_item = input("What item do you want removed? ")
            if del_item in shopping_list:
                shopping_list.remove(del_item)
        elif item.lower() == 'order':
            print('The following items have been ordered: ')
            print(shopping_list)
        elif item.lower() == 'quit':
            print(shopping_list)
            break
        else:
            print('That is not a valid input')
