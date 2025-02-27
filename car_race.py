import random

# create the car class\

class Car:
    # Create an initializer function
    def __init__(self, make, model, color, driver, max_speed, handling):
        self.make = make
        self.model = model
        self.color = color
        self.driver = driver
        self.max_speed = max_speed
        self.handling = handling
        self.miles_driven = 0

    def show_car_info(self):
        print(f"The {self.color} {self.make} {self.model} is driven by {self.driver}")
    
    def drive_car(self):
        self.miles_driven += random.randint(5,self.max_speed) + self.handling

    def show_stats(self, miles_to_win):
        print(f"{self.driver}'s car advanced {self.miles_driven}")
        print()
        if self.miles_driven > 100:
            print(f"{self.driver} won the race!!!")

    def hit_maxwell(self):
        hit = random.randint(1,3)
        if hit == 1:
            print(f"🎆🎆🙀🎆🎆 Maxwell was hit by {self.driver}")
            reduce_speed = random.randint(10,20)
            self.max_speed -= reduce_speed
            print(f"Max speed reduced by {reduce_speed}")
            print()
        else:
            print(f"Maxwell managed to save himself from {self.driver}")

def main():
    miles_to_win = 100

    # create a car object
    muskCar = Car("Mazda", "Miata", "Orange", "Elom musk", 60, 11)
    # create a car object
    bezosCar = Car("Toyota", "Supra", "Black", "Jeff bezos", 80, 12)

    print("The race is starting..........")


    # call the instance function show_car_info
    muskCar.show_car_info()
    print()
    bezosCar.show_car_info()

    while muskCar.miles_driven < 100 and bezosCar.miles_driven < 100:

        # drive both cars one time
        muskCar.drive_car()
        bezosCar.drive_car()

        # show the updated status of the car
        muskCar.show_stats(miles_to_win)
        bezosCar.show_stats(miles_to_win)

        # callthe hit maxwell mathod on both car objects
        muskCar.hit_maxwell()
        bezosCar.hit_maxwell()


if __name__ == "__main__":
    main()

