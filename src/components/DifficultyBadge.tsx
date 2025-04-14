import React from 'react';

interface DifficultyBadgeProps {
  level: 'Easy' | 'Medium' | 'Hard';
}

const DifficultyBadge: React.FC<DifficultyBadgeProps> = ({ level }) => {
  const colors = {
    Easy: 'bg-green-50 text-green-700',
    Medium: 'bg-yellow-50 text-yellow-700',
    Hard: 'bg-red-50 text-red-700'
  };

  return (
    <span className={`inline-block px-2 py-1 rounded-md text-sm font-medium ${colors[level]}`}>
      {level}
    </span>
  );
};

export default DifficultyBadge; 