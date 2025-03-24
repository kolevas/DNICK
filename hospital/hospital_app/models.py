from django.db.models import CASCADE,SET_NULL
from django.db import models
from django.contrib.auth.models import User

class Address(models.Model):
    street = models.CharField(max_length=100)
    number = models.PositiveIntegerField()

    def __str__(self):
        return self.street + " " + str(self.number)

class Hospital (models.Model):
    name = models.CharField(max_length=100)
    address = models.ForeignKey(Address,on_delete=SET_NULL, null=True)
    phone_number = models.CharField(max_length=20)
    email = models.EmailField()
    principal = models.CharField(max_length=100)
    num_patients = models.PositiveIntegerField()
    num_doctors = models.PositiveIntegerField()
    date_founded = models.DateField()
    added_by = models.ForeignKey(User,on_delete=SET_NULL, null=True)

    def __str__(self):
        return self.name

class Doctor (models.Model):

    SPECIALIZATION_TYPES =[
        ("G","General medicine"),
        ("F","Family medicine"),
        ("I","Internal medicine")
    ]

    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=20)
    specializes_at = models.CharField(max_length=100,choices=SPECIALIZATION_TYPES)
    hospital = models.ForeignKey(Hospital,on_delete=CASCADE)
    salary = models.PositiveIntegerField()
    added_by = models.ForeignKey(User,on_delete=CASCADE)
    def __str__(self):
        return self.name + " "+ self.surname

class Patient(models.Model):
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    ssn = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=20)
    added_by = models.ForeignKey(User,on_delete=SET_NULL, null=True)
    date_of_birth = models.DateField()
    diagnosis = models.TextField()
    hospital = models.ForeignKey(Hospital, on_delete=CASCADE)

    def __str__(self):
        return self.name + " "+ self.surname

class Drug (models.Model):
    DRUG_TYPES = [
        ("antibiotic","antibiotic"),
        ("antiseptic","antiseptic"),
        ("analgesic","analgesic"),
        ("vitamin","vitamin"),
        ("antihistamine", "antihistamine"),
    ]
    drug_type = models.CharField(max_length=100,choices=DRUG_TYPES)
    name = models.CharField(max_length=100)
    prescription_required = models.BooleanField()
    code = models.CharField(max_length=100,unique=True)

    def __str__(self):
        return self.name


class HospitalDrugs (models.Model):
    hospital = models.ForeignKey(Hospital,on_delete=CASCADE)
    drug = models.ForeignKey(Drug,on_delete=CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return str(self.drug) + " - "+ str(self.hospital) +": "+ str(self.quantity)