from rest_framework import viewsets
from .models import Questionnaire, Gender, AgeGroup, ServiceAgeGroup,\
    EmployeeLevel, Department, Division, Region, SoftSkill, TechnicalSkill, \
    QuestionnaireSoftSkill, QuestionnaireTechnicalSkill, JobType, StrategyDeliverySkill, QuestionnaireStrategyDeliverySkill
from .serializers import QuestionnaireSerializer, GenderSerializer, \
    AgeGroupSerializer, ServiceAgeGroupSerializer, EmployeeLevelSerializer, \
        DepartmentSerializer, DivisionSerializer, RegionSerializer, \
            SoftSkillSerializer, TechnicalSkillSerializer, QuestionnaireSoftSkillSerializer, \
            QuestionnaireTechnicalSkillSerializer, JobTypeSerializer, StrategyDeliverySkillSerializer, \
            QuestionnaireStrategyDeliverySkillSerializer
import pandas as pd
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import JobTypeUploadForm, TechnicalSkillsUploadForm

def upload_jobtypes(request):
    if request.method == 'POST':
        form = JobTypeUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Read the Excel file
                df = pd.read_excel(file)

                # Ensure the required columns are present
                if 'Division' not in df.columns or 'JobType' not in df.columns:
                    messages.error(request, "The file must contain 'Division' and 'JobType' columns.")
                    return redirect('upload_jobtypes')

                # Process each row
                for _, row in df.iterrows():
                    division_name = row['Division']
                    jobtype_name = row['JobType']

                    # Get the Division object
                    try:
                        division = Division.objects.get(name=division_name)
                    except Division.DoesNotExist:
                        messages.warning(request, f"Division '{division_name}' does not exist. Skipping.")
                        continue

                    # Create or update the JobType
                    JobType.objects.get_or_create(division=division, name=jobtype_name)

                messages.success(request, "JobTypes uploaded successfully!")
                return redirect('upload_jobtypes')

            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
                return redirect('upload_jobtypes')
    else:
        form = JobTypeUploadForm()

    return render(request, 'upload_jobtypes.html', {'form': form})

def upload_technicalskills(request):
    if request.method == 'POST':
        form = TechnicalSkillsUploadForm(request.POST, request.FILES)
        if form.is_valid():
            file = request.FILES['file']
            try:
                # Read the Excel file
                df = pd.read_excel(file)

                # Ensure the required columns are present
                if 'Department' not in df.columns or'Division' not in df.columns or 'JobType' not in df.columns or 'TechnicalSkill' not in df.columns:
                    messages.error(request, "The file must contain 'Department', 'Division', 'JobType' and 'TechnicalSkill' columns.")
                    return redirect('upload_technicalskills')

                # Process each row
                for _, row in df.iterrows():
                    department_name = row['Department']
                    division_name = row['Division']
                    jobtype_name = row['JobType']
                    technicalskill_name = row['TechnicalSkill']

                    # Get the Division object
                    try:
                        department = Department.objects.get(name=department_name)
                    except Department.DoesNotExist:
                        messages.warning(request, f"Department '{department_name}' does not exist. Skipping.")
                        continue
                    try:
                        division = Division.objects.get(name=division_name)
                    except Division.DoesNotExist:
                        messages.warning(request, f"Division '{division_name}' does not exist. Skipping.")
                        continue
                    try:
                        jobtype = JobType.objects.get(name=jobtype_name, division=division) 
                    except JobType.DoesNotExist:
                        messages.warning(request, f"JobType '{jobtype_name}' does not exist. Skipping.")
                        continue

                    # Create or update the TechnicalSkill
                    TechnicalSkill.objects.get_or_create(department=department, division=division, jobtype=jobtype, name=technicalskill_name)

                messages.success(request, "Technical Skills uploaded successfully!")
                return redirect('upload_technicalskills')

            except Exception as e:
                messages.error(request, f"An error occurred: {e}")
                return redirect('upload_technicalskills')
    else:
        form = TechnicalSkillsUploadForm()

    return render(request, 'upload_technicalskills.html', {'form': form})

# Create your views here.
class QuestionnaireViewSet(viewsets.ModelViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

class GenderViewSet(viewsets.ModelViewSet):
    queryset = Gender.objects.all()
    serializer_class = GenderSerializer
    
class AgeGroupViewSet(viewsets.ModelViewSet):
    queryset = AgeGroup.objects.all()
    serializer_class = AgeGroupSerializer

class ServiceAgeGroupViewSet(viewsets.ModelViewSet):
    queryset = ServiceAgeGroup.objects.all()
    serializer_class = ServiceAgeGroupSerializer
    
class EmployeeLevelViewSet(viewsets.ModelViewSet):
    queryset = EmployeeLevel.objects.all()
    serializer_class = EmployeeLevelSerializer
    
class DepartmentViewSet(viewsets.ModelViewSet):
    queryset = Department.objects.all()
    serializer_class = DepartmentSerializer
    
class DivisionViewSet(viewsets.ModelViewSet):
    serializer_class = DivisionSerializer

    def get_queryset(self):
        department_id = self.request.query_params.get('department', None)
        if department_id:
            return Division.objects.filter(department_id=department_id)
        return Division.objects.none()
    
class JobTypeViewSet(viewsets.ModelViewSet):
    serializer_class = JobTypeSerializer

    def get_queryset(self):
        division_id = self.request.query_params.get('division', None)
        if division_id:
            return JobType.objects.filter(division_id=division_id)
        return JobType.objects.none()   
    
class RegionViewSet(viewsets.ModelViewSet):
    queryset = Region.objects.all()
    serializer_class = RegionSerializer 

class SoftSkillViewSet(viewsets.ModelViewSet):
    serializer_class = SoftSkillSerializer
    # filter by employeelevel       
    def get_queryset(self):
        employeelevel_id = self.request.query_params.get('employeelevel', None)
        if employeelevel_id:
            return SoftSkill.objects.filter(employeelevel_id=employeelevel_id)
        return SoftSkill.objects.none()
    
class TechnicalSkillViewSet(viewsets.ModelViewSet):
    serializer_class = TechnicalSkillSerializer
    # filter by jobtype      
    def get_queryset(self):
        jobtype_id = self.request.query_params.get('jobtype', None)
        if jobtype_id:
            return TechnicalSkill.objects.filter(jobtype_id=jobtype_id)
        return TechnicalSkill.objects.none()
    
class StrategyDeliverySkillViewSet(viewsets.ModelViewSet):
    queryset = StrategyDeliverySkill.objects.all()
    serializer_class = StrategyDeliverySkillSerializer 

class QuestionnaireSoftSkillViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionnaireSoftSkillSerializer
    
    def get_queryset(self):
        questionnaire_id = self.request.query_params.get('questionnaire', None)
        if questionnaire_id:
            return QuestionnaireSoftSkill.objects.filter(questionnaire_id=questionnaire_id)
        return QuestionnaireSoftSkill.objects.none()
    
class QuestionnaireTechnicalSkillViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionnaireTechnicalSkillSerializer

    def get_queryset(self):
        questionnaire_id = self.request.query_params.get('questionnaire', None)
        if questionnaire_id:
            return QuestionnaireTechnicalSkill.objects.filter(questionnaire_id=questionnaire_id)
        return QuestionnaireTechnicalSkill.objects.none()

class QuestionnaireStrategyDeliverySkillViewSet(viewsets.ModelViewSet):
    serializer_class = QuestionnaireStrategyDeliverySkillSerializer

    def get_queryset(self):
        questionnaire_id = self.request.query_params.get('questionnaire', None)
        if questionnaire_id:
            return QuestionnaireStrategyDeliverySkill.objects.filter(questionnaire_id=questionnaire_id)
        return QuestionnaireStrategyDeliverySkill.objects.none()


