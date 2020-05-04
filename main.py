
class Stack:
    '''
    абстрактный тип данных, представляющий собой список элементов,
    организованных по принципу LIFO (англ. last in — first out,
    «последним пришёл — первым вышел»). Чаще всего принцип работы 
    стека сравнивают со стопкой тарелок: чтобы взять вторую сверху, 
    нужно снять верхнюю. Или с магазином в огнестрельном оружии
    (стрельба начнётся с патрона, заряженного последним).
    '''
    stack_list = []

    # def __init__(self, lst):
    #     self.list = lst

    #проверка стека на пустоту. Метод возвращает True или False
    def isEmpty(self):
        if len(Stack.stack_list) == 0:
            return True
        return False
    
    #добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self, data):
        self.data = data
        if self.data:
            Stack.stack_list.append(self.data)
            return self.data
        else:
            print('Trying to push an empty list')

    #удаляет верхний элемент стека. Стек изменяется. Метод возвращает верхний элемент стека
    def pop(self):
        try:
            last_el = Stack.stack_list.pop()
            return last_el
        except IndexError:
            return 'Trying to pop from empty list'

    #возвращает верхний элемент стека, но не удаляет его. Стек не меняется.
    def peek(self):
        try:
            return Stack.stack_list[-1]
        except IndexError:
            return 'Trying to peek from empty list'

    #возвращает количество элементов в стеке.
    def size(self):
        return len(Stack.stack_list)



#проверка соответствия скобок
def check_brackets(stack, string):
    brackets_open = ('(', '[', '{', '<')
    brackets_closed = (')', ']', '}', '>')

    for i in string:
        if i in brackets_open:
            stack.push(i)
        if i in brackets_closed:    
            if len(stack.stack_list) == 0:
                return 'Небалансированно'
            index = brackets_closed.index(i)
            open_bracket = brackets_open[index]
            if stack.stack_list[-1] == open_bracket:
                stack.pop()  
            else: 
                return 'Небалансированно'
    return 'Сбалансированно'



def main():
    #задача №1
    
    my_stack = Stack()
    my_stack2 = Stack()

    print(my_stack.isEmpty())

    my_stack.push('Bob')
    my_stack2.push(25)
    my_stack.push('777')

    print(my_stack.pop())
    print(my_stack.isEmpty())
    print(my_stack.size())
    print(my_stack.peek())
    print(my_stack.pop())
    print(my_stack.pop())

    #задача №2
    str1 = '[{([[[<>]]])(<>)(){}}]' 
    str2 = ']()(){<>}[[()]]' 
    str3 = '[(sjd),"2"],{"name": "netology"}, [<>]'
    str4 = '{[[[[((()))]]<]>]}'
 
    print()
    my_stack = Stack()
    print(check_brackets(my_stack, str1))
    print(check_brackets(my_stack, str2))
    print(check_brackets(my_stack, str3))
    print(check_brackets(my_stack, str4))



if __name__ == '__main__':
    main()