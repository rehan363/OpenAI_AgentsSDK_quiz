class Agent:
    name1:str = "ahmed"
    def __init__(self, name: str):
        self.name = name
    def greet(self):
        return f"Hello, {self.name}!"
    
print(Agent.name1)
name = Agent("Ali")
print(name.greet())


