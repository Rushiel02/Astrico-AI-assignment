import React, { useState, useEffect } from 'react';
import SummaryReport from './SummaryReport';
import { Link } from 'react-router-dom';

const Dashboard = () => {
  const [summary, setSummary] = useState({
    total_learners: 0,
    total_assessors: 0,
    total_institutions: 0,
  });

  const [activities, setActivities] = useState([]);

  useEffect(() => {
  const storedActivities = sessionStorage.getItem('activityLog');
  if (storedActivities) {
    setActivities(JSON.parse(storedActivities));
  }
}, []);

  // Update summary from window variable set by SummaryReport
  const handleSummaryUpdate = (data) => {
    setSummary(data);

    // Check if session flag exists
    const activityType = sessionStorage.getItem('recentActivity');
    if (activityType) {
      const newActivity = {
        type: activityType,
        timestamp: new Date().toLocaleString(),
      };

      setActivities(prev => {
        const updated = [newActivity, ...prev].slice(0, 5);
        sessionStorage.setItem('activityLog', JSON.stringify(updated));
        return updated; 
      });

      sessionStorage.removeItem('recentActivity');
    }
  };

  const totalRecords =
    summary.total_institutions +
    summary.total_learners +
    summary.total_assessors;

  return (
    <div className="space-y-8">
      <div className="border-b border-blue-100 pb-4 mb-6">
        <h1 className="text-3xl font-bold text-gray-800">Admin Dashboard</h1>
        <div className="mt-6 flex flex-wrap gap-4">
          <Link
            to="/institutions/new"
            onClick={() => sessionStorage.setItem('recentActivity', 'Institution added')}
            className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors"
          >
            New Institution
          </Link>
          <Link
            to="/learners/new"
            onClick={() => sessionStorage.setItem('recentActivity', 'Learner added')}
            className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors"
          >
            New Learner
          </Link>
          <Link
            to="/assessors/new"
            onClick={() => sessionStorage.setItem('recentActivity', 'Assessor added')}
            className="bg-blue-600 hover:bg-blue-700 text-white font-medium py-2 px-4 rounded transition-colors"
          >
            New Assessor
          </Link>
        </div>
      </div>

      <div className="bg-white shadow-md rounded-lg overflow-hidden">
        <div className="bg-blue-50 px-6 py-4 border-b border-blue-100">
          <h2 className="text-xl font-semibold text-blue-800">Summary Report</h2>
        </div>
        <div className="p-6">
          <SummaryReport onSummaryLoad={handleSummaryUpdate} />
        </div>
      </div>

      <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <div className="bg-blue-50 px-6 py-4 border-b border-blue-100">
            <h2 className="text-lg font-semibold text-blue-800">Recent Activities</h2>
          </div>
          <div className="p-6 space-y-2">
            {activities.length > 0 ? (
              activities.map((act, index) => (
                <div key={index} className="text-gray-700 text-sm">
                  • {act.type} at {act.timestamp}
                </div>
              ))
            ) : (
              <div className="text-center text-gray-500">No recent activities to display</div>
            )}
          </div>
        </div>

        <div className="bg-white shadow-md rounded-lg overflow-hidden">
          <div className="bg-blue-50 px-6 py-4 border-b border-blue-100">
            <h2 className="text-lg font-semibold text-blue-800">Quick Stats</h2>
          </div>
          <div className="p-6 space-y-4">
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
              <span className="text-gray-600">Total Records</span>
              <span className="text-blue-600 font-medium">{totalRecords}</span>
            </div>
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
              <span className="text-gray-600">System Status</span>
              <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-green-100 text-green-800">
                Online
              </span>
            </div>
            <div className="flex justify-between items-center p-3 bg-gray-50 rounded-lg">
              <span className="text-gray-600">Last Updated</span>
              <span className="text-gray-600 text-sm">{new Date().toLocaleString()}</span>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;
