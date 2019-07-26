class Solution:
    def asteroidCollision(self, asteroids: 'List[int]') -> 'List[int]':
        a_stack = []
        for ast in asteroids:
            if a_stack and a_stack[-1] > 0 and ast < 0:
                while a_stack and a_stack[-1] > 0 and abs(ast) > a_stack[-1]:
                    a_stack.pop()
                if a_stack and a_stack[-1] == abs(ast):
                    a_stack.pop()
                elif a_stack and a_stack[-1] > abs(ast):
                    continue
                else:
                    a_stack.append(ast)
            else:
                a_stack.append(ast)
        return a_stack