class Solution:
    def interpret(self, command: str) -> str:
        return command.replace('()', 'o').replace('(al)', 'al')


sol = Solution()
print(sol.interpret(command="G()(al)"))
print(sol.interpret(command="G()()()()(al)"))
print(sol.interpret(command="(al)G(al)()()G"))

# Problem - https://leetcode.com/problems/goal-parser-interpretation/description/
