from rest_framework import serializers
from .models import Questionnaire, Gender, AgeGroup, ServiceAgeGroup, EmployeeLevel, Department, Division, Region, SoftSkill,\
    TechnicalSkill, QuestionnaireSoftSkill, QuestionnaireTechnicalSkill, JobType, StrategyDeliverySkill, QuestionnaireStrategyDeliverySkill

class GenderSerializer(serializers.ModelSerializer):
    gender_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = Gender
        fields = '__all__'

class AgeGroupSerializer(serializers.ModelSerializer):
    agegroup_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = AgeGroup
        fields = '__all__'

class ServiceAgeGroupSerializer(serializers.ModelSerializer):
    serviceagegroup_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = ServiceAgeGroup
        fields = '__all__'

class EmployeeLevelSerializer(serializers.ModelSerializer):
    employeetype_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = EmployeeLevel           
        fields = '__all__'

class DepartmentSerializer(serializers.ModelSerializer):
    department_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = Department
        fields = '__all__'          

class DivisionSerializer(serializers.ModelSerializer):
    dvision_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = Division
        fields = '__all__'

class RegionSerializer(serializers.ModelSerializer):
    region_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = Region
        fields = '__all__'
        
class SoftSkillSerializer(serializers.ModelSerializer):
    softskill_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = SoftSkill
        fields = '__all__'

class TechnicalSkillSerializer(serializers.ModelSerializer):
    technicalskill_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = TechnicalSkill
        fields = '__all__'
        
class StrategyDeliverySkillSerializer(serializers.ModelSerializer):
    strategydeliveryskill_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = StrategyDeliverySkill
        fields = '__all__'

class QuestionnaireSoftSkillSerializer(serializers.ModelSerializer):
    softskill_name = serializers.CharField(source='softskill.name', read_only=True)
    class Meta:
        model = QuestionnaireSoftSkill
        fields = '__all__'
        
class QuestionnaireTechnicalSkillSerializer(serializers.ModelSerializer):
    technicalskill_name = serializers.CharField(source='technicalskill.name', read_only=True)
    class Meta:
        model = QuestionnaireTechnicalSkill
        fields = '__all__'
        
class QuestionnaireStrategyDeliverySkillSerializer(serializers.ModelSerializer):
    strategydeliveryskill_name = serializers.CharField(source='strategydeliveryskill.name', read_only=True)
    class Meta:
        model = QuestionnaireStrategyDeliverySkill
        fields = '__all__'

class JobTypeSerializer(serializers.ModelSerializer):
    jobtype_name = serializers.CharField(source='name', read_only=True)
    class Meta:
        model = JobType
        fields = '__all__'

class QuestionnaireSerializer(serializers.ModelSerializer):
    softskill_entries = QuestionnaireSoftSkillSerializer(many=True, read_only=True)
    technicalskill_entries = QuestionnaireTechnicalSkillSerializer(many=True, read_only=True)
    strategydeliveryskill_entries = QuestionnaireStrategyDeliverySkillSerializer(many=True, read_only=True)
    gender_name = serializers.CharField(source='gender.name', read_only=True)
    agegroup_name = serializers.CharField(source='agegroup.name', read_only=True)
    serviceagegroup_name = serializers.CharField(source='serviceagegroup.name', read_only=True) 
    region_name = serializers.CharField(source='region.name', read_only=True)
    department_name = serializers.CharField(source='department.name', read_only=True)
    division_name = serializers.CharField(source='division.name', read_only=True)
    employeelevel_name = serializers.CharField(source='employeelevel.name', read_only=True)
    jobtype_name = serializers.CharField(source='jobtype.name', read_only=True)
    class Meta:
        model = Questionnaire
        fields = '__all__'