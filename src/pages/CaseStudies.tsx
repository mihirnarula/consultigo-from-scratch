import React, { useState } from 'react';
import DifficultyBadge from '../components/DifficultyBadge';

interface CaseStudy {
  id: string;
  title: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  description: string;
}

const CaseStudies: React.FC = () => {
  const [selectedCase, setSelectedCase] = useState<CaseStudy | null>(null);

  const caseStudies: CaseStudy[] = [
    {
      id: 'market-entry',
      title: 'Market Entry Strategy',
      difficulty: 'Medium',
      description: 'A leading tech company is considering entering the smart home market. How would you evaluate this opportunity?'
    },
    {
      id: 'cost-reduction',
      title: 'Cost Reduction Analysis',
      difficulty: 'Hard',
      description: 'A manufacturing company needs to reduce operational costs by 25%. How would you approach this challenge?'
    }
  ];

  if (selectedCase) {
    return (
      <div className="min-h-screen bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-3xl mx-auto">
            <div className="mb-6 flex items-center">
              <button 
                onClick={() => setSelectedCase(null)}
                className="text-gray-600 hover:text-gray-900 flex items-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clipRule="evenodd" />
                </svg>
                Back to Case Studies
              </button>
            </div>
            <div className="bg-white rounded-lg shadow-sm p-8">
              <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold text-gray-900">{selectedCase.title}</h1>
                <DifficultyBadge level={selectedCase.difficulty} />
              </div>
              <p className="text-gray-600 text-lg mb-8">
                {selectedCase.description}
              </p>
              <div className="space-y-6">
                <textarea
                  className="w-full h-64 p-4 border-2 border-gray-200 rounded-lg focus:ring-2 focus:ring-blue-500 focus:border-transparent"
                  placeholder="Type your solution here..."
                />
                <button className="w-full py-3 bg-gray-600 hover:bg-gray-700 text-white rounded-lg flex items-center justify-center space-x-2 transition-colors duration-200">
                  <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                    <path fillRule="evenodd" d="M10 18a8 8 0 100-16 8 8 0 000 16zm3.707-8.707l-3-3a1 1 0 00-1.414 0l-3 3a1 1 0 001.414 1.414L9 9.414V13a1 1 0 102 0V9.414l1.293 1.293a1 1 0 001.414-1.414z" clipRule="evenodd" />
                  </svg>
                  <span>Submit Solution</span>
                </button>
              </div>
            </div>
          </div>
        </div>
      </div>
    );
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-4 py-8">
        <div className="max-w-3xl mx-auto">
          <div className="mb-8">
            <h1 className="text-3xl font-bold text-gray-900">Case Studies</h1>
          </div>
          <div className="space-y-4">
            {caseStudies.map((study) => (
              <button
                key={study.id}
                onClick={() => setSelectedCase(study)}
                className="w-full p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 text-left"
              >
                <div className="flex justify-between items-center">
                  <h3 className="text-xl font-semibold text-gray-900">{study.title}</h3>
                  <DifficultyBadge level={study.difficulty} />
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default CaseStudies; 