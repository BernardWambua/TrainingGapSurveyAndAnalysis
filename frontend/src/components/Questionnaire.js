/* eslint-disable react/prop-types */
import { useState } from 'react';
import api from '../api';
import RegionDropdown from './RegionDropdown';
import GenderDropdown from './GenderDropdown';
import ServiceAgeGroupDropdown from './ServiceAgeGroupDropdown';
import AgeGroupDropdown from './AgeGroupDropdown';
import EmployeeLevelDropdown from './EmployeeLevelDropdown';
import DepartmentDropdown from './DepartmentDropdown';
import DivisionDropdown from './DivisionDropdown';
import SoftSkillsMultichoice from './SoftSkillsMultichoice';
import TechnicalSkillsMultichoice from './TechnicalSkillsMultichoice';
import JobTypeDropdown from './JobTypeDropdown';
import StrategyDeliverySkillsMultichoice from './StrategyDeliverySkillsMultichoice';
function QuestionnaireForm() {
  const [formData, setFormData] = useState({
    employeename: '',
    staffno: '',
    region: '',
    gender: '',
    agegroup: '',
    serviceagegroup: '',
    employeelevel: '',
    department: '',
    division: '',
    jobtype: '',
    softskills: {},
    technicalskills: {},
    strategydeliveryskills: {},
    id: ''
  });

  const handleInputChange = (e) => {
    const { name, value } = e.target;
    setFormData(prevState => ({
      ...prevState,
      [name]: value
    }));
  };

  const handleSubmit = async (e) => {
    e.preventDefault();
    try {
      // First create the questionnaire
      const questionnaireResponse = await api.post('/api/questionnaire/', {
        employeename: formData.employeename,
        staffno: formData.staffno,
        region: formData.region,
        gender: formData.gender,
        agegroup: formData.agegroup,
        serviceagegroup: formData.serviceagegroup,
        employeelevel: formData.employeelevel,
        department: formData.department,
        division: formData.division,
        jobtype: formData.jobtype
      });

      // Axios automatically throws for non-200 status codes, so if we get here, the request was successful
      const questionnaireData = questionnaireResponse.data;

      // Then create the soft skills entries with the new questionnaire ID
      const softSkillsEntries = Object.entries(formData.softskills).map(([skillId, skillData]) => 
        api.post('/api/questionnaire-soft-skills/', {
          questionnaire: questionnaireData.id,
          softskill: skillId,
          trained: skillData.trained,
          modeofdelivery: skillData.modeofdelivery
        })
      );
      
      if (softSkillsEntries.length > 0) {
        await Promise.all(softSkillsEntries);
      }

      // Then create the technical skills entries with the new questionnaire ID
      const technicalSkillsEntries = Object.entries(formData.technicalskills).map(([skillId, skillData]) => 
        api.post('/api/questionnaire-technical-skills/', {
          questionnaire: questionnaireData.id,
          technicalskill: skillId,
          trained: skillData.trained,
          modeofdelivery: skillData.modeofdelivery
        })
      );

      if (technicalSkillsEntries.length > 0) {
        await Promise.all(technicalSkillsEntries);
      }

      // Then create the technical skills entries with the new questionnaire ID
      const strategyDeliverySkillsEntries = Object.entries(formData.strategydeliveryskills).map(([skillId, skillData]) => 
        api.post('/api/questionnaire-strategy-delivery-skills/', {
          questionnaire: questionnaireData.id,
          strategydeliveryskill: skillId,
          trained: skillData.trained,
          modeofdelivery: skillData.modeofdelivery
        })
      );

      if (strategyDeliverySkillsEntries.length > 0) {
        await Promise.all(strategyDeliverySkillsEntries);
      }
      

      alert('Form submitted successfully!');
      setFormData({
        employeename: '',
        staffno: '',
        region: '',
        gender: '',
        agegroup: '',
        serviceagegroup: '',
        employeelevel: '',
        department: '',
        division: '',
        jobtype: '',
        softskills: {},
        technicalskills: {},
        strategydeliveryskills: {},
        id: ''
      });
    } catch (error) {
      console.error('Error:', error);
      alert('Error submitting form: ' + (error.response?.data?.message || error.message));
    }
  };

  return (
    <div className="box">
      <form onSubmit={handleSubmit}>
        
        <div className="field">
          <label className="label">Please enter your Employee Number e.g. 12345</label>
          <div className="control">
            <input 
              className="input" 
              type="number" 
              name="staffno"
              value={formData.staffno}
              onChange={handleInputChange}
              placeholder="Employee number"
              required
              min="0"
              pattern="[0-9]*"
              inputMode="numeric"
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please enter your Name</label>
          <div className="control">
            <input 
              className="input" 
              type="text" 
              name="employeename"
              value={formData.employeename}
              onChange={handleInputChange}
              placeholder="Name"
              required
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please select your Region</label>
          <div className="control">
            <RegionDropdown 
              value={formData.region}
              onChange={value => setFormData(prev => ({ ...prev, region: value }))}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please select your Gender</label>
          <div className="control">
            <GenderDropdown 
              value={formData.gender}
              onChange={(value) => setFormData(prev => ({ ...prev, gender: value }))}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please select your Age Group</label>
          <div className="control">
            <AgeGroupDropdown 
              value={formData.agegroup}
              onChange={(value) => setFormData(prev => ({ ...prev, agegroup: value }))}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please indicate how long you have worked in this organization</label>
          <div className="control">
            <ServiceAgeGroupDropdown 
              value={formData.serviceagegroup}
              onChange={(value) => setFormData(prev => ({ ...prev, serviceagegroup: value }))}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please select your supervisory responsibility</label>
          <div className="control">
            <EmployeeLevelDropdown 
              value={formData.employeelevel}
              onChange={(value) => setFormData(prev => ({ ...prev, employeelevel: value }))}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please select your Department</label>
          <div className="control">
            <DepartmentDropdown 
              value={formData.department}
              onChange={(value) => {
                setFormData(prev => ({ 
                  ...prev, 
                  department: value,
                  division: '' // Clear division when department changes
                }));
              }}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please select your Division</label>
          <div className="control">
            <DivisionDropdown 
              value={formData.division}
              onChange={(value) => setFormData(prev => ({ ...prev, division: value }))}
              departmentId={formData.department}
            />
          </div>
        </div>

        <div className="field">
          <label className="label">Please select your Job Type</label>
          <div className="control">
            <JobTypeDropdown 
              value={formData.jobtype}
              onChange={(value) => setFormData(prev => ({ ...prev, jobtype: value }))}
              divisionId={formData.division}
            />
          </div>
        </div>

        <div className="field">
          <div className="control">
            <SoftSkillsMultichoice 
              value={formData.softskills}
              onChange={(value) => setFormData(prev => ({ ...prev, softskills: value }))}
              employeelevelId={formData.employeelevel}
              questionnaireId={formData.id}
            />
          </div>
        </div>

        <div className="field">
          <div className="control">
            <TechnicalSkillsMultichoice
              value={formData.technicalskills}
              onChange={(value) => setFormData(prev => ({ ...prev, technicalskills: value }))}
              jobtypeId={formData.jobtype}
              questionnaireId={formData.id}
            />
          </div>
        </div>

        <div className="field">
          <div className="control">
            <StrategyDeliverySkillsMultichoice
              value={formData.strategydeliveryskills}
              onChange={(value) => setFormData(prev => ({ ...prev, strategydeliveryskills: value }))}
              questionnaireId={formData.id}
            />
          </div>
        </div>

        <div className="field is-grouped">
          <div className="control">
            <button type="submit" className="button is-link">Submit</button>
          </div>
          <div className="control">
            <button type="button" className="button is-text" onClick={() => setFormData({
              employeename: '',
              staffno: '',
              region: '',
              gender: '',
              agegroup: '',
              serviceagegroup: '',
              employeelevel: '',
              department: '',
              division: '',
              jobtype: '',
              softskills: {},
              technicalskills: {},
              strategydeliveryskills: {},
              id: ''
            })}>Cancel</button>
          </div>
        </div>
      </form>
    </div>
  );
}

export default QuestionnaireForm;
