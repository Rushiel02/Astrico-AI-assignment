import axios from 'axios';

const API_URL = 'http://localhost:5000/api';

// Institution API calls
export const createInstitution = async (institutionData) => {
  try {
    const response = await axios.post(`${API_URL}/institutions/`, institutionData);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to create institution' };
  }
};

export const getInstitutions = async () => {
  try {
    const response = await axios.get(`${API_URL}/institutions/`);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to fetch institutions' };
  }
};

// Learner API calls
export const createLearner = async (learnerData) => {
  try {
    const response = await axios.post(`${API_URL}/learners/`, learnerData);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to create learner' };
  }
};

export const getLearners = async () => {
  try {
    const response = await axios.get(`${API_URL}/learners/`);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to fetch learners' };
  }
};

// Assessor API calls
export const createAssessor = async (assessorData) => {
  try {
    const response = await axios.post(`${API_URL}/assessors/`, assessorData);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to create assessor' };
  }
};

export const getAssessors = async () => {
  try {
    const response = await axios.get(`${API_URL}/assessors/`);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to fetch assessors' };
  }
};

// Report API calls
export const getSummaryReport = async () => {
  try {
    const response = await axios.get(`${API_URL}/reports/summary`);
    return response.data;
  } catch (error) {
    throw error.response?.data || { error: 'Failed to fetch summary report' };
  }
};