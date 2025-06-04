from django.contrib import admin
from .models import Questionnaire, Gender, AgeGroup, ServiceAgeGroup, EmployeeLevel, Department, Division, Region,\
    SoftSkill, TechnicalSkill, QuestionnaireSoftSkill, QuestionnaireTechnicalSkill, JobType, \
    StrategyDeliverySkill, QuestionnaireStrategyDeliverySkill

# Register your models here.
admin.site.register(JobType)
admin.site.register(Gender)
admin.site.register(AgeGroup)
admin.site.register(ServiceAgeGroup)
admin.site.register(EmployeeLevel)
admin.site.register(Department)
admin.site.register(Division)
admin.site.register(Region)
admin.site.register(SoftSkill)
admin.site.register(TechnicalSkill)
admin.site.register(StrategyDeliverySkill)

class QuestionnaireSoftSkillInline(admin.TabularInline):
    model = QuestionnaireSoftSkill
    extra = 1

class QuestionnaireTechnicalSkillInline(admin.TabularInline):
    model = QuestionnaireTechnicalSkill
    extra = 1
    
class QuestionnaireStrategyDeliverySkillInline(admin.TabularInline):
    model = QuestionnaireStrategyDeliverySkill
    extra = 1

@admin.register(Questionnaire)
class QuestionnaireAdmin(admin.ModelAdmin):
    inlines = [QuestionnaireSoftSkillInline, QuestionnaireTechnicalSkillInline, QuestionnaireStrategyDeliverySkillInline]

