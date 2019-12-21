class Car():
    def __init__(self,name,company,model,color,transmission):
        self.name = name
        self.company = company
        self.model = model
        self.color = color
        self.transmission = transmission

car1 = Car("Aulto","Suzuki","2016","White","Manual")
print ("The detail of car is as follows\nCar Name: "+car1.name+"\nCompany: "+car1.company+"\nModel: "+car1.model+"\nColor: "+car1.color+"\nTransmission: "+car1.transmission+"\n")
car2 = Car("Corolla","Toyota","2017","Grey","Automatic")
print ("The detail of car is as follows\nCar Name: "+car2.name+"\nCompany: "+car2.company+"\nModel: "+car2.model+"\nColor: "+car2.color+"\nTransmission: "+car2.transmission+"\n")
car3 = Car("Mini","Tata","2018","White","Semi-automatic")
print ("The detail of car is as follows\nCar Name: "+car3.name+"\nCompany: "+car3.company+"\nModel: "+car3.model+"\nColor: "+car3.color+"\nTransmission: "+car3.transmission+"\n")
car4 = Car("Picanto","Hyundai","2019","Black","Automatic")
print ("The detail of car is as follows\nCar Name: "+car4.name+"\nCompany: "+car4.company+"\nModel: "+car4.model+"\nColor: "+car4.color+"\nTransmission: "+car4.transmission+"\n")
car5 = Car("Mira","Japan Automobile","2019","Silver","Automatic")
print ("The detail of car is as follows\nCar Name: "+car5.name+"\nCompany: "+car5.company+"\nModel: "+car5.model+"\nColor: "+car5.color+"\nTransmission: "+car5.transmission+"\n")
