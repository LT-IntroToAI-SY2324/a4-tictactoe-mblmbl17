# object oriented programming

# (define-struct dog [fur_color name age favorite_food])
class Dog:
    #functions tat start with a __ are not intended to be called directly
    def __init__(self, fc = "", a = 0, w = 0.0, n = "") -> None:
        pass
        

        self.furcolor=fc
        self.age=0
        self.weight=0.0
        self.name=n
        self.fetch=0

    def __str__(self) -> str:
        s="The dogs name is "+self.name +"\n"
        s+="the dogs color is " +self.furcolor+"\n"
        return s
    
    def playfetch(self, num_times):
        self.fetch_count += num_times



birdog=Dog("black",7,78.2,"logan")
ninadog=Dog("brown",8,100,"hobbes")

print(birdog)

birdog.playfetch(23)

print(f"{ninadog.name} has played fetch {ninadog}")