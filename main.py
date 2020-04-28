
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

    def __init__(self, lst):
        self.list = lst

    #проверка стека на пустоту. Метод возвращает True или False
    def isEmpty(self):
        if len(Stack.stack_list) == 0:
            return True
        return False
    
    #добавляет новый элемент на вершину стека. Метод ничего не возвращает.
    def push(self):
        if self.list:
            Stack.stack_list.append(self.list)
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
        return Stack.stack_list[-1]


    #возвращает количество элементов в стеке.
    def size(self):
        return len(Stack.stack_list)

   #проверка соответствия скобок
    def check_brackets(self, string):
        brackets_open = ('(', '[', '{', '<')
        brackets_closed = (')', ']', '}', '>')
        stack = []
        for i in string:
            if i in brackets_open:
                stack.append(i)
            if i in brackets_closed:    
                if len(stack) == 0:
                    return 'Небалансированно'
                index = brackets_closed.index(i)
                open_bracket = brackets_open[index]
                if stack[-1] == open_bracket:
                    stack = stack[:-1]  
                else: 
                    return 'Небалансированно'
        return 'Сбалансированно'



def main():
    #задача №1
    my_stack = Stack(15)
    my_stack2 = Stack(35)
    print(my_stack.isEmpty())
    my_stack.push()
    my_stack2.push()
    print(my_stack.peek())
    print(my_stack.size())
    print(my_stack.isEmpty())
    print(Stack.stack_list)
    print(my_stack.pop())
    print(Stack.stack_list)
    print(my_stack.pop())
    print(Stack.stack_list)
    print(my_stack.isEmpty())

    #задача №2
    str1 = '[{([[[<>]]])(<>)(){}}]' 
    str2 = ']()(){<>}[[()]]' 
    str3 = '[(sjd),"2"],{"name": "netology"}, [<>]'
    str4 = '{[[[[((()))]]<]>]}'

    print(my_stack.check_brackets(str1))
    print(my_stack.check_brackets(str2))
    print(my_stack.check_brackets(str3))
    print(my_stack.check_brackets(str4))

if __name__ == '__main__':
    main()