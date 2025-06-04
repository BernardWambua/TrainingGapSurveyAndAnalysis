import { useState, useEffect } from 'react';
import api from '../api';

function StrategyDeliverySkillsMultichoice({ value, onChange }) {
    const [strategyDeliverySkills, setStrategyDeliverySkills] = useState([]);
    const [selectedStrategyDeliverySkills, setSelectedStrategyDeliverySkills] = useState({});

    const modeOfDeliveryOptions = [
        { value: '', label: 'Please select' },
        { value: 'Classroom (in-person)', label: 'Classroom (in-person)' },
        { value: 'Virtual (instructor led)', label: 'Virtual (instructor led)' },
        { value: 'E-learning (self paced)', label: 'E-learning (self paced)' },
        { value: 'Coaching', label: 'Coaching' },
        { value: 'Mentoring', label: 'Mentoring' },
        { value: 'Job/project assignment', label: 'Job/project assignment' }
    ];

    const handleStrategyDeliverySkillChange = (skillId, isChecked) => {
        if (isChecked) {
            // Add the skill with empty mode of delivery
            const newSelectedSkills = {
                ...selectedStrategyDeliverySkills,
                [skillId]: {
                    trained: 'Yes',
                    modeofdelivery: ''
                }
            };
            setSelectedStrategyDeliverySkills(newSelectedSkills);
            onChange(newSelectedSkills);
        } else {
            // Remove the skill
            const newSelectedSkills = { ...selectedStrategyDeliverySkills };
            delete newSelectedSkills[skillId];
            setSelectedStrategyDeliverySkills(newSelectedSkills);
            onChange(newSelectedSkills);
        }
    };

    const handleModeOfDeliveryChange = (skillId, value) => {
        const newSelectedSkills = {
            ...selectedStrategyDeliverySkills,
            [skillId]: {
                ...selectedStrategyDeliverySkills[skillId],
                modeofdelivery: value
            }
        };
        setSelectedStrategyDeliverySkills(newSelectedSkills);
        onChange(newSelectedSkills);
    };

    const isOptionSelected = (skillId) => {
        const skill = selectedStrategyDeliverySkills[skillId];
        return skill && skill.modeofdelivery;
    };

    useEffect(() => {
        // Only fetch technical skills if jobtypeId is provided

        api.get("/api/strategy-delivery-skills/")
            .then(response => setStrategyDeliverySkills(response.data))
            .catch(error => console.error('Error fetching strategy delivery skills:', error));
    }, []);

    return (
        <div className="soft-skills-container">
            <h1 className="soft-skills-title">Select critical skills for the delivery of the organization's Strategy that you have been trained on and the mode of delivery</h1>
            <div className="soft-skills-list">
                {strategyDeliverySkills.map(skill => (
                    <div key={skill.id} className="soft-skill-item">
                        <div className="skill-selection">
                            <input 
                                type="checkbox" 
                                value={skill.id} 
                                checked={skill.id in selectedStrategyDeliverySkills} 
                                onChange={(e) => handleStrategyDeliverySkillChange(skill.id, e.target.checked)} 
                                className="skill-checkbox"
                            />
                            <span className="skill-name">{skill.name}</span>
                        </div>
                        {skill.id in selectedStrategyDeliverySkills && (
                            <div className="skill-options">
                                <div className="option-group">
                                    <label className="option-label">Mode of Delivery: <span className="required">*</span></label>
                                    <select 
                                        value={selectedStrategyDeliverySkills[skill.id].modeofdelivery}
                                        onChange={(e) => handleModeOfDeliveryChange(skill.id, e.target.value)}
                                        className={`option-select ${!selectedStrategyDeliverySkills[skill.id].modeofdelivery ? 'required-field' : ''}`}
                                        required
                                    >
                                        {modeOfDeliveryOptions.map(option => (
                                            <option key={option.value} value={option.value}>
                                                {option.label}
                                            </option>
                                        ))}
                                    </select>
                                </div>
                                {!isOptionSelected(skill.id) && (
                                    <div className="validation-message">
                                        Please select the mode of delivery
                                    </div>
                                )}
                            </div>
                        )}
                    </div>
                ))}
            </div>
            <style jsx>{`
                .soft-skills-container {
                    padding: 20px;
                    background-color: #f5f5f5;
                    border-radius: 8px;
                }
                .soft-skills-title {
                    font-size: 1.5rem;
                    color: #333;
                    margin-bottom: 20px;
                }
                .soft-skills-list {
                    display: flex;
                    flex-direction: column;
                    gap: 15px;
                }
                .soft-skill-item {
                    background-color: white;
                    padding: 15px;
                    border-radius: 6px;
                    box-shadow: 0 2px 4px rgba(0,0,0,0.1);
                }
                .skill-selection {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                    margin-bottom: 10px;
                }
                .skill-checkbox {
                    width: 18px;
                    height: 18px;
                    cursor: pointer;
                }
                .skill-name {
                    font-size: 1.1rem;
                    color: #444;
                }
                .skill-options {
                    display: flex;
                    flex-direction: column;
                    gap: 10px;
                    margin-left: 28px;
                    padding-top: 10px;
                    border-top: 1px solid #eee;
                }
                .option-group {
                    display: flex;
                    align-items: center;
                    gap: 10px;
                }
                .option-label {
                    min-width: 120px;
                    color: #666;
                    font-weight: 500;
                }
                .required {
                    color: #ff4444;
                    margin-left: 2px;
                }
                .option-select {
                    flex: 1;
                    padding: 8px;
                    border: 1px solid #ddd;
                    border-radius: 4px;
                    background-color: white;
                    font-size: 0.9rem;
                    color: #333;
                    cursor: pointer;
                }
                .option-select.required-field {
                    border-color: #ff4444;
                }
                .option-select:hover {
                    border-color: #999;
                }
                .option-select:focus {
                    outline: none;
                    border-color: #4a90e2;
                    box-shadow: 0 0 0 2px rgba(74,144,226,0.2);
                }
                .validation-message {
                    color: #ff4444;
                    font-size: 0.9rem;
                    margin-top: 5px;
                }
            `}</style>
        </div>
    );
}

export default StrategyDeliverySkillsMultichoice;
