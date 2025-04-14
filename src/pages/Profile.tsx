import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';

interface SolvedProblem {
  id: string;
  title: string;
  type: 'Case Study' | 'Guesstimate' | 'Example';
  solvedDate: string;
}

const Profile: React.FC = () => {
  const navigate = useNavigate();
  const [showSettings, setShowSettings] = useState(false);

  // Mock user data - in a real app, this would come from your backend
  const userData = {
    name: 'John Doe',
    email: 'john.doe@example.com',
    problemsSolved: 12,
    solvedProblems: [
      {
        id: 'market-entry',
        title: 'Market Entry Strategy',
        type: 'Case Study',
        solvedDate: '2024-04-14'
      },
      {
        id: 'coffee-market',
        title: 'Coffee Market Size',
        type: 'Guesstimate',
        solvedDate: '2024-04-13'
      },
      {
        id: 'retail-expansion',
        title: 'Retail Chain Expansion',
        type: 'Example',
        solvedDate: '2024-04-12'
      }
    ] as SolvedProblem[]
  };

  const handleLogout = () => {
    // Add logout logic here
    navigate('/');
  };

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-4xl mx-auto">
          {/* Settings Bar */}
          <div className="relative mb-8">
            <div className="flex justify-between items-center">
              <h1 className="text-3xl font-bold text-gray-900">Profile</h1>
              <button
                onClick={() => setShowSettings(!showSettings)}
                className="text-gray-600 hover:text-gray-900"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M10.325 4.317c.426-1.756 2.924-1.756 3.35 0a1.724 1.724 0 002.573 1.066c1.543-.94 3.31.826 2.37 2.37a1.724 1.724 0 001.065 2.572c1.756.426 1.756 2.924 0 3.35a1.724 1.724 0 00-1.066 2.573c.94 1.543-.826 3.31-2.37 2.37a1.724 1.724 0 00-2.572 1.065c-.426 1.756-2.924 1.756-3.35 0a1.724 1.724 0 00-2.573-1.066c-1.543.94-3.31-.826-2.37-2.37a1.724 1.724 0 00-1.065-2.572c-1.756-.426-1.756-2.924 0-3.35a1.724 1.724 0 001.066-2.573c-.94-1.543.826-3.31 2.37-2.37.996.608 2.296.07 2.572-1.065z" />
                  <path strokeLinecap="round" strokeLinejoin="round" strokeWidth={2} d="M15 12a3 3 0 11-6 0 3 3 0 016 0z" />
                </svg>
              </button>
            </div>
            
            {/* Settings Dropdown */}
            {showSettings && (
              <div className="absolute right-0 mt-2 w-48 bg-white rounded-lg shadow-lg py-2 z-10">
                <button
                  onClick={handleLogout}
                  className="w-full px-4 py-2 text-left text-gray-700 hover:bg-gray-100 flex items-center gap-2"
                >
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M3 3a1 1 0 011 1v12a1 1 0 11-2 0V4a1 1 0 011-1zm7.707 3.293a1 1 0 010 1.414L9.414 9H17a1 1 0 110 2H9.414l1.293 1.293a1 1 0 01-1.414 1.414l-3-3a1 1 0 010-1.414l3-3a1 1 0 011.414 0z" clipRule="evenodd" />
                  </svg>
                  Logout
                </button>
              </div>
            )}
          </div>

          {/* User Info Card */}
          <div className="bg-white rounded-lg shadow-sm p-8 mb-8">
            <div className="flex items-center space-x-4 mb-6">
              <div className="bg-gray-200 rounded-full p-4">
                <svg xmlns="http://www.w3.org/2000/svg" className="h-12 w-12 text-gray-600" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M10 9a3 3 0 100-6 3 3 0 000 6zm-7 9a7 7 0 1114 0H3z" clipRule="evenodd" />
                </svg>
              </div>
              <div>
                <h2 className="text-2xl font-bold text-gray-900">{userData.name}</h2>
                <p className="text-gray-600">{userData.email}</p>
              </div>
            </div>
            <div className="border-t border-gray-200 pt-6">
              <div className="text-center">
                <p className="text-4xl font-bold text-gray-900">{userData.problemsSolved}</p>
                <p className="text-gray-600">Problems Solved</p>
              </div>
            </div>
          </div>

          {/* Solved Problems List */}
          <div className="bg-white rounded-lg shadow-sm p-8">
            <h3 className="text-xl font-bold text-gray-900 mb-6">Solved Problems</h3>
            <div className="space-y-4">
              {userData.solvedProblems.map((problem) => (
                <div
                  key={problem.id}
                  className="flex justify-between items-center p-4 bg-gray-50 rounded-lg"
                >
                  <div>
                    <h4 className="font-semibold text-gray-900">{problem.title}</h4>
                    <p className="text-sm text-gray-600">{problem.type}</p>
                  </div>
                  <div className="text-sm text-gray-500">
                    {new Date(problem.solvedDate).toLocaleDateString()}
                  </div>
                </div>
              ))}
            </div>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Profile; 