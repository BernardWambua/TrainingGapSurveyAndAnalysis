from django.db import models

class Region(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Gender(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class AgeGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class ServiceAgeGroup(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class EmployeeLevel(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Department(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class Division(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class JobType(models.Model):
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
    
class SoftSkill(models.Model):
    modeofdelivery_choices = [
        ('Classroom (in-person)',  'Classroom (in-person)'),
        ('Virtual (instructor led)', 'Virtual (instructor led)'),
        ('E-learning (self paced)', 'E-learning (self paced)'),
        ('Coaching', 'Coaching'),
        ('Mentoring', 'Mentoring'),
        ('Job/project assignment', 'Job/project assignment'),
    ]
    trained_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    skilltype_choices = [
        ('Entrepreneurship', 'Entrepreneurship'),
        ('Leadership', 'Leadership'),
        ('Leading Change', 'Leading Change'),
        ('Business Acumen', 'Business Acumen'),
        ('Building Coalitions', 'Building Coalitions'),
        ('Financial Skills', 'Financial Skills'),
        ('Leading People', 'Leading People'),
        ('Personal Effectiveness', 'Personal Effectiveness'),
        ('Results Driven', 'Results Driven'),
        ('Fundamental Competencies', 'Fundamental Competencies'),
    ]
    name = models.CharField(max_length=100)
    employeelevel = models.ForeignKey(EmployeeLevel, on_delete=models.CASCADE)
    skilltype = models.CharField(max_length=100, choices=skilltype_choices, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class TechnicalSkill(models.Model):
    modeofdelivery_choices = [
        ('Classroom (in-person)',  'Classroom (in-person)'),
        ('Virtual (instructor led)', 'Virtual (instructor led)'),
        ('E-learning (self paced)', 'E-learning (self paced)'),
        ('Coaching', 'Coaching'),
        ('Mentoring', 'Mentoring'),
        ('Job/project assignment', 'Job/project assignment'),
    ]
    trained_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    name = models.CharField(max_length=100)
    department = models.ForeignKey(Department, on_delete=models.CASCADE, null=True, blank=True)
    division = models.ForeignKey(Division, on_delete=models.CASCADE, null=True, blank=True)
    jobtype = models.ForeignKey(JobType, on_delete=models.CASCADE, null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
    
class StrategyDeliverySkill(models.Model):
    modeofdelivery_choices = [
        ('Classroom (in-person)',  'Classroom (in-person)'),
        ('Virtual (instructor led)', 'Virtual (instructor led)'),
        ('E-learning (self paced)', 'E-learning (self paced)'),
        ('Coaching', 'Coaching'),
        ('Mentoring', 'Mentoring'),
        ('Job/project assignment', 'Job/project assignment'),
    ]
    trained_choices = [
        ('Yes', 'Yes'),
        ('No', 'No'),
    ]
    name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name

class Questionnaire(models.Model):
    employeename = models.CharField(max_length=100, null=True, blank=True)
    staffno = models.CharField(max_length=100, unique=True)
    region = models.ForeignKey(Region, on_delete=models.CASCADE)
    gender = models.ForeignKey(Gender, on_delete=models.CASCADE)
    agegroup = models.ForeignKey(AgeGroup, on_delete=models.CASCADE)
    serviceagegroup = models.ForeignKey(ServiceAgeGroup, on_delete=models.CASCADE)
    employeelevel = models.ForeignKey(EmployeeLevel, on_delete=models.CASCADE)
    department = models.ForeignKey(Department, on_delete=models.CASCADE)
    division = models.ForeignKey(Division, on_delete=models.CASCADE)
    jobtype = models.ForeignKey(JobType, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.employeename or "Unnamed Questionnaire"

class QuestionnaireSoftSkill(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='softskill_entries')
    softskill = models.ForeignKey(SoftSkill, on_delete=models.CASCADE)
    trained = models.CharField(max_length=100, choices=SoftSkill.trained_choices)
    modeofdelivery = models.CharField(max_length=100, choices=SoftSkill.modeofdelivery_choices)

    def __str__(self):
        return f"{self.questionnaire} - {self.softskill.name}"

class QuestionnaireTechnicalSkill(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='technicalskill_entries')
    technicalskill = models.ForeignKey(TechnicalSkill, on_delete=models.CASCADE)
    trained = models.CharField(max_length=100, choices=TechnicalSkill.trained_choices)
    modeofdelivery = models.CharField(max_length=100, choices=TechnicalSkill.modeofdelivery_choices)

    def __str__(self):
        return f"{self.questionnaire} - {self.technicalskill.name}"

class QuestionnaireStrategyDeliverySkill(models.Model):
    questionnaire = models.ForeignKey(Questionnaire, on_delete=models.CASCADE, related_name='strategydeliveryskill_entries')
    strategydeliveryskill = models.ForeignKey(StrategyDeliverySkill, on_delete=models.CASCADE)
    trained = models.CharField(max_length=100, choices=TechnicalSkill.trained_choices)
    modeofdelivery = models.CharField(max_length=100, choices=TechnicalSkill.modeofdelivery_choices)

    def __str__(self):
        return f"{self.questionnaire} - {self.strategydeliveryskill.name}"


