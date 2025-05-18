import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Dashboard from './components/Dashboard';
import InstitutionForm from './components/InstitutionForm';
import LearnerForm from './components/LearnerForm';
import AssessorForm from './components/AssessorForm';

function App() {
  return (
    <Router>
      <div className="min-h-screen bg-gray-100">
        <Navbar />
        <div className="container mx-auto px-4 py-8 max-w-4xl">
          <Routes>
            <Route path="/" element={<Dashboard />} />
            <Route path="/institutions/new" element={<InstitutionForm />} />
            <Route path="/learners/new" element={<LearnerForm />} />
            <Route path="/assessors/new" element={<AssessorForm />} />
          </Routes>
        </div>
      </div>
    </Router>
  );
}

export default App;