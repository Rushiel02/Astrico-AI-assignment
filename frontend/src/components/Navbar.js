import React from 'react';
import { Link, useLocation } from 'react-router-dom';

const Navbar = () => {
  const location = useLocation();
  
  const isActive = (path) => {
    return location.pathname === path ? 'bg-blue-700' : '';
  };

  return (
    <nav className="bg-blue-600 text-white shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex flex-col md:flex-row md:items-center md:justify-between py-3">
          <div className="flex items-center justify-between">
            <Link to="/" className="font-bold text-2xl">
              Astrico AI Portal
            </Link>
            <div className="md:hidden">
              <button className="focus:outline-none">
                <span className="block w-6 h-0.5 bg-white mb-1.5"></span>
                <span className="block w-6 h-0.5 bg-white mb-1.5"></span>
                <span className="block w-6 h-0.5 bg-white"></span>
              </button>
            </div>
          </div>
          <div className="md:flex md:items-center md:space-x-4 mt-3 md:mt-0">
            <Link 
              to="/" 
              className={`px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-700 transition-colors block md:inline-block ${isActive('/')}`}
            >
              Dashboard
            </Link>
            <Link 
              to="/institutions/new" 
              className={`px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-700 transition-colors block md:inline-block ${isActive('/institutions/new')}`}
              onClick={() => sessionStorage.setItem('recentActivity', 'Institution added')}
            >
              Add Institution
            </Link>
            <Link 
              to="/learners/new" 
              className={`px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-700 transition-colors block md:inline-block ${isActive('/learners/new')}`}
              onClick={() => sessionStorage.setItem('recentActivity', 'Learner added')}
            >
              Add Learner
            </Link>
            <Link 
              to="/assessors/new" 
              className={`px-4 py-2 rounded-md text-sm font-medium hover:bg-blue-700 transition-colors block md:inline-block ${isActive('/assessors/new')}`}
              onClick={() => sessionStorage.setItem('recentActivity', 'Assessor added')}
            >
              Add Assessor
            </Link>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navbar;