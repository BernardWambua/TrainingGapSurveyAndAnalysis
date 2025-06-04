from django.urls import path
from .views import QuestionnaireViewSet, GenderViewSet, AgeGroupViewSet,\
        ServiceAgeGroupViewSet, EmployeeLevelViewSet, DepartmentViewSet, \
        DivisionViewSet, RegionViewSet, SoftSkillViewSet, TechnicalSkillViewSet, \
        QuestionnaireSoftSkillViewSet, QuestionnaireTechnicalSkillViewSet, \
        JobTypeViewSet, StrategyDeliverySkillViewSet, QuestionnaireStrategyDeliverySkillViewSet,\
        upload_jobtypes, upload_technicalskills
urlpatterns = [
    path('upload-jobtypes/', upload_jobtypes, name='upload_jobtypes'),
    path('upload-technicalskills/', upload_technicalskills, name='upload_technicalskills'),
    path('questionnaire/', QuestionnaireViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='questionnaire'),
    path('questionnaire/<int:pk>/', QuestionnaireViewSet.as_view({
        'get': 'retrieve',
        'put': 'update',
        'delete': 'destroy'
    }), name='questionnaire-detail'),
    path('genders/', GenderViewSet.as_view({
        'get': 'list'
    }), name='genders'),
    path('age-groups/', AgeGroupViewSet.as_view({
        'get': 'list'
    }), name='age-groups'), 
    path('service-age-groups/', ServiceAgeGroupViewSet.as_view({
        'get': 'list'
    }), name='service-age-groups'),
    path('employee-levels/', EmployeeLevelViewSet.as_view({
        'get': 'list'
    }), name='employee-levels'),
    path('departments/', DepartmentViewSet.as_view({
        'get': 'list'
    }), name='departments'),
    path('divisions/', DivisionViewSet.as_view({
        'get': 'list'
    }), name='divisions'),
    path('regions/', RegionViewSet.as_view({
        'get': 'list'
    }), name='regions'),
    path('soft-skills/', SoftSkillViewSet.as_view({
        'get': 'list'
    }), name='soft-skills'),
    path('technical-skills/', TechnicalSkillViewSet.as_view({
        'get': 'list'
    }), name='technical-skills'),
    path('questionnaire-soft-skills/', QuestionnaireSoftSkillViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='questionnaire-soft-skills'),
    path('questionnaire-technical-skills/', QuestionnaireTechnicalSkillViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='questionnaire-technical-skills'),
    path('job-types/', JobTypeViewSet.as_view({
        'get': 'list'
    }), name='job-types'),
    path('strategy-delivery-skills/', StrategyDeliverySkillViewSet.as_view({
        'get': 'list'
    }), name='strategy-delivery-skills'),
    path('questionnaire-strategy-delivery-skills/', QuestionnaireStrategyDeliverySkillViewSet.as_view({
        'get': 'list',
        'post': 'create'
    }), name='questionnaire-strategy-delivery-skills')
]

