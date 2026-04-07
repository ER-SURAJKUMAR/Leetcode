class Robot:
    def __init__(self, width: int, height: int):
        self.x = 0
        self.y = 0
        self.dir = "East"
        self.width = width
        self.height = height
        self.perim = 2 * (width - 1) + 2 * (height - 1)

    def step(self, num: int) -> None:
        # Reduce to within one perimeter
        num %= self.perim
        
        # If num is 0 after modulo but was originally > 0, 
        # it means a full lap was completed. 
        # We must move 'perim' steps to update the direction correctly.
        if num == 0:
            num = self.perim

        while num > 0:
            if self.dir == "East":
                # Move right as much as possible
                steps = min(num, self.width - 1 - self.x)
                self.x += steps
                num -= steps
                if num > 0: self.dir = "North"
            elif self.dir == "North":
                # Move up as much as possible
                steps = min(num, self.height - 1 - self.y)
                self.y += steps
                num -= steps
                if num > 0: self.dir = "West"
            elif self.dir == "West":
                # Move left as much as possible
                steps = min(num, self.x)
                self.x -= steps
                num -= steps
                if num > 0: self.dir = "South"
            elif self.dir == "South":
                # Move down as much as possible
                steps = min(num, self.y)
                self.y -= steps
                num -= steps
                if num > 0: self.dir = "East"

    def getPos(self) -> list[int]:
        return [self.x, self.y]

    def getDir(self) -> str:
        # Special case for the very first call before any movement
        # (Technically handled by the fact that num=0 won't enter the loop)
        if self.x == 0 and self.y == 0 and self.dir == "East" and self.perim > 0:
            # We only return "East" at 0,0 if the robot hasn't moved a full lap
            # This logic is slightly implicit in your simulation.
            pass
        return self.dir