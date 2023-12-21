import json
from utils import Utils
from api import APIMethods

class Solution:
    MACROS = {
        "!": lambda self: self.repeat,
        "^": lambda self: self.reverse,
        "%": lambda self: self.encrypt,
    }

    def __init__(self, challenge):
        self.challenge = challenge
        self.solution = []

    def solve(self):
        for i, sequence in enumerate(self.challenge):
            # print(i, sequence)
            decoded = self.decode(sequence)
            self.solution.append(decoded)
        return self.solution
    
    def decode(self, sequence):
        tokens = self.get_tokens(sequence)
        if not tokens:
            return ''
        tokens[0] = self.clean_token(tokens[0])
        for i in range(1, len(tokens)):
            prev, curr = tokens[i-1], tokens[i]
            tokens[i-1], tokens[i] = self.process_token(prev, curr)
        decoded = "".join(tokens)
        return decoded

    def clean_token(self, token):
        cleaned = ""
        for char in token:
            if char.isdigit():
                cleaned += char
        return cleaned
    
    def process_token(self, prev, curr):
        new_curr = ""
        for char in curr:
            if char in self.MACROS:
                prev, new_curr = self.MACROS[char](self)(prev, new_curr)
            else:
                new_curr += char
        return prev, new_curr
    
    def get_tokens(self, sequence: str):
        return sequence.split("#")[1:-1]

    def repeat(self, prev, curr):
        return prev, curr + prev

    def reverse(self, prev, curr):
        return prev[::-1], curr
    
    def encrypt(self, prev, curr):
        new_prev = ""
        for char in prev:
            doubled = int(char) * 2
            new_char = str(doubled)[-1]
            new_prev += new_char
        return new_prev, curr



def main():
    data = Utils.load_challenge()
    token, challenge = data['token'], data['challenge']
    print(challenge[0:5])
    solver = Solution(challenge)
    # print(solver.get_tokens("#12#34!#59^#67%#"))
    # print(solver.decode("#12#34!#59^#67%#"))
    solution = solver.solve()
    print(solution[0:5])
    # APIMethods.submit_solution(solution)

    print(solver.decode("#1%8%2^0^0!757%140#58#13641%9^7%8%4^755#30!87!79^1#2^1^9!64!5212!93!9#031#") == "182007571400455748791463130136419784755871364197847557912193013641978475587136419784755791643013641978475587136419784755791521230136419784755871364197847557919330136419784755871364197847557919031")

    print(solver.decode("#01#9999!^!%!%!%!9999^#"))
    print(solver.decode("##"))
    print(solver.decode("#0%#1%#2%#3%#4%#5%#6%#7%#8%#9%#"))
    print(solver.decode("###%#!!!#0987#"))

    print("hi")

main()
