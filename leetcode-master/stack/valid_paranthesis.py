# solution by rubix-coder
class SolutionValidParenthesis:
    def isValid( s: str) -> bool:
        stack = []
        bracket_map = {')': '(', '}': '{', ']': '['}
        print(f"Bracket map -> {bracket_map}")
        for char in s:
            print(f"Char in string -> {char}")
            
            if char in bracket_map:
                print(f"char in bracket map -> {char}")
                top_element = stack.pop() if stack else '#'
                print(f"top element -> {top_element}")
                if bracket_map[char] != top_element:
                    print(f"Return false as {bracket_map[char]} not in {top_element}")
                    return False
            else:
                stack.append(char)
                print(f"Updated stack -> {stack}")
        print("Return ! stack..")
        return not stack

result = SolutionValidParenthesis.isValid(s="((({{{[[]]}}}})))")
print(result)
