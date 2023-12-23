from utils import Utils
from api import APIMethods

# Solution class
class Solution:
    # Map of available functions
    MACROS = {
        "!": lambda self: self.repeat,
        "^": lambda self: self.reverse,
        "%": lambda self: self.encrypt,
    }

    def __init__(self, challenge):
        self.challenge = challenge
        self.solution = []

    # Decode all sequences in challenge
    def solve(self):
        for sequence in self.challenge:
            decoded = self.decode(sequence)
            self.solution.append(decoded)
        return self.solution
    
    # Decode a single sequence
    def decode(self, sequence):
        tokens = self.get_tokens(sequence)
        if not tokens:
            return ''
        tokens[0] = self.clean_token(tokens[0])
        for i in range(1, len(tokens)):
            tokens[i-1], tokens[i] = self.process_token(tokens[i-1], tokens[i])
        decoded = "".join(tokens)
        return decoded

    # Clean a token of all special characters
    def clean_token(self, token):
        cleaned = ""
        for char in token:
            if char.isdigit():
                cleaned += char
        return cleaned
    
    # Process a token and its macro functions
    def process_token(self, prev, curr):
        new_curr = ""
        new_prev = prev
        for char in curr:
            if char in self.MACROS:
                new_prev, new_curr = self.MACROS[char](self)(prev, new_prev, new_curr)
            else:
                new_curr += char
        return new_prev, new_curr
    
    # Get token list from string sequence
    def get_tokens(self, sequence: str):
        return sequence.split("#")[1:-1]


    # ------ MACROS ------
    # Repeat original version of previous token 
    def repeat(self, old_prev, curr_prev, curr):
        return curr_prev, curr + old_prev

    # Reverse previous token
    def reverse(self, old_prev, curr_prev, curr):
        return curr_prev[::-1], curr
    
    # Encrypt previous token
    def encrypt(self, old_prev, curr_prev, curr):
        new_prev = ""
        for char in curr_prev:
            doubled = int(char) * 2
            new_char = str(doubled)[-1]
            new_prev += new_char
        return new_prev, curr



def main():
    data = Utils.load_challenge()
    challenge = data['challenge']
    solver = Solution(challenge)
    solution = solver.solve()
    APIMethods.submit_solution(solution)

main()
