
class HelloWord:
    def __init__(self):
        self.message = "Hello, World!"

    def greet(self):
        return self.message
    
    def personalize_greeting(self, name):
        return f"Greetings {name} from HelloWord class!"
    
if __name__ == "__main__":
    hello = HelloWord()
    print(hello.greet())