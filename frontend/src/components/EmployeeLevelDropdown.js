/* eslint-disable react/prop-types */
import { useEffect, useState } from 'react';
import api from '../api';

function EmployeeLevelDropdown({ value, onChange }) {
  const [employeeLevels, setEmployeeLevels] = useState([]);

  useEffect(() => {
    const fetchAgeGroups = async () => {
      try {
        const response = await api.get('/api/employee-levels/');
        setEmployeeLevels(response.data);
      } catch (error) {
        console.error('Error fetching employee levels:', error);
      }
    };

    fetchAgeGroups();
  }, []);

  return (
    <div className="select is-fullwidth">
      <select value={value} onChange={(e) => onChange(e.target.value)} required>
        <option value="">Select your supervisory responsibility</option>
        {employeeLevels.map((employeeLevel) => (  
          <option key={employeeLevel.id} value={employeeLevel.id}>
            {employeeLevel.name}
          </option>
        ))}
      </select>
    </div>
  );
}

export default EmployeeLevelDropdown;
