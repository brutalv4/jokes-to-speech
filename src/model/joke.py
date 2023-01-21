class Joke:
    def __init__(self, joke: dict):
        self.type = joke['type']
        self.setup = joke['setup']
        self.punchline = joke['punchline']
    
    def __str__(self) -> str:
        return f'{self.setup} {self.punchline}'
