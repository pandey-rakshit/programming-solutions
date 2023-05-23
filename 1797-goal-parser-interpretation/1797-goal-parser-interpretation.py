class Solution:
    def interpret(self, command: str) -> str:
        nwStr = ''
        for i in range(len(command)):
            if command[i] == '(' and command[i+1] == ')':
                nwStr += 'o'
            elif command[i] == '(':
                pass
            elif command[i] == ')':
                pass
            else:
                nwStr += command[i]

        return nwStr