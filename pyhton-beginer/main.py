'''from indeed import get_jobs as get_indeed_jobs
from so import get_so_jobs
from save import save_to_file'''


# indeed_jobs = get_indeed_jobs()
# so_jobs = get_so_jobs()
# jobs = indeed_jobs + so_jobs
# save_to_file(jobs)

class Car():
  def __init__(self, **kwargs):
    self.wheels = 4
    self.doors = 4
    self.color = kwargs.get("color", "black")
    self.price = kwargs.get("price", "40,000,000원")
  
  def __str__(self):
    return f"wheels: {self.wheels}, doors: {self.doors}, color: {self.color}, price: {self.price}"

class SubCar(Car):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)
    self.size = "mini"

  def __str__(self):
    return f"exetened wheels: {self.wheels}, doors: {self.doors}, color: {self.color}, price: {self.price}, size: {self.size}"

kia = Car(color = "red", price = "36,000,000원")
toyota = SubCar(color= "yellow", price= "1￥")


print(toyota)