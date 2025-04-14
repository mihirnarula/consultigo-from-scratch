import React from 'react';
import { Link } from 'react-router-dom';

interface CategoryCardProps {
  icon: React.ReactNode;
  title: string;
  description: string;
  to: string;
}

const CategoryCard: React.FC<CategoryCardProps> = ({ icon, title, description, to }) => {
  return (
    <Link
      to={to}
      className="block p-6 bg-gray-50 rounded-lg hover:bg-gray-100 transition-colors duration-200"
    >
      <div className="flex items-start space-x-4">
        <div className="p-2 bg-white rounded-lg shadow-sm">
          {icon}
        </div>
        <div>
          <h2 className="text-xl font-semibold text-gray-900 mb-1">{title}</h2>
          <p className="text-gray-600">{description}</p>
        </div>
      </div>
    </Link>
  );
};

export default CategoryCard; 