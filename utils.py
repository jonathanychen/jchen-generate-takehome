import json

class Utils:
    @staticmethod
    def load_challenge() -> dict:
        with open("challenge.txt", "r") as f:
            data = json.load(f)
        return data
    
    @staticmethod
    def write_solution(solution):
        if not solution:
            print("No solution to write yet!")
            return
        with open("solution.txt", "wb") as f:
            f.write(f"{solution}")
            f.close()
