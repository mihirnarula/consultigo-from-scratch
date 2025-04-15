import React, { useState, useEffect } from 'react';
import axios from 'axios';

interface Guesstimate {
  id: number;
  title: string;
  description: string;
  min_value: number;
  max_value: number;
  actual_value?: number;
  created_at: string;
}

const GuesstimateDashboard: React.FC = () => {
  const [guesstimates, setGuesstimates] = useState<Guesstimate[]>([]);
  const [newGuesstimate, setNewGuesstimate] = useState({
    title: '',
    description: '',
    min_value: 0,
    max_value: 0,
  });

  useEffect(() => {
    fetchGuesstimates();
  }, []);

  const fetchGuesstimates = async () => {
    try {
      const token = localStorage.getItem('token');
      const response = await axios.get('http://127.0.0.1:8000/api/v1/guesstimates/', {
        headers: { Authorization: `Bearer ${token}` }
      });
      setGuesstimates(response.data);
    } catch (error) {
      console.error('Error fetching guesstimates:', error);
    }
  };

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    try {
      const token = localStorage.getItem('token');
      await axios.post(
        'http://127.0.0.1:8000/api/v1/guesstimates/',
        newGuesstimate,
        { headers: { Authorization: `Bearer ${token}` } }
      );
      setNewGuesstimate({
        title: '',
        description: '',
        min_value: 0,
        max_value: 0,
      });
      fetchGuesstimates();
    } catch (error) {
      console.error('Error creating guesstimate:', error);
    }
  };

  return (
    <div className="space-y-6">
      <div className="bg-white shadow px-4 py-5 sm:rounded-lg sm:p-6">
        <div className="md:grid md:grid-cols-3 md:gap-6">
          <div className="md:col-span-1">
            <h3 className="text-lg font-medium leading-6 text-gray-900">New Guesstimate</h3>
            <p className="mt-1 text-sm text-gray-500">
              Create a new guesstimate by providing a title, description, and your estimated range.
            </p>
          </div>
          <div className="mt-5 md:mt-0 md:col-span-2">
            <form onSubmit={handleSubmit}>
              <div className="grid grid-cols-6 gap-6">
                <div className="col-span-6 sm:col-span-4">
                  <label htmlFor="title" className="block text-sm font-medium text-gray-700">
                    Title
                  </label>
                  <input
                    type="text"
                    name="title"
                    id="title"
                    value={newGuesstimate.title}
                    onChange={(e) => setNewGuesstimate({ ...newGuesstimate, title: e.target.value })}
                    className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                  />
                </div>

                <div className="col-span-6">
                  <label htmlFor="description" className="block text-sm font-medium text-gray-700">
                    Description
                  </label>
                  <textarea
                    id="description"
                    name="description"
                    rows={3}
                    value={newGuesstimate.description}
                    onChange={(e) => setNewGuesstimate({ ...newGuesstimate, description: e.target.value })}
                    className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                  />
                </div>

                <div className="col-span-6 sm:col-span-3">
                  <label htmlFor="min_value" className="block text-sm font-medium text-gray-700">
                    Minimum Value
                  </label>
                  <input
                    type="number"
                    name="min_value"
                    id="min_value"
                    value={newGuesstimate.min_value}
                    onChange={(e) => setNewGuesstimate({ ...newGuesstimate, min_value: Number(e.target.value) })}
                    className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                  />
                </div>

                <div className="col-span-6 sm:col-span-3">
                  <label htmlFor="max_value" className="block text-sm font-medium text-gray-700">
                    Maximum Value
                  </label>
                  <input
                    type="number"
                    name="max_value"
                    id="max_value"
                    value={newGuesstimate.max_value}
                    onChange={(e) => setNewGuesstimate({ ...newGuesstimate, max_value: Number(e.target.value) })}
                    className="mt-1 focus:ring-indigo-500 focus:border-indigo-500 block w-full shadow-sm sm:text-sm border-gray-300 rounded-md"
                  />
                </div>
              </div>
              <div className="mt-5">
                <button
                  type="submit"
                  className="inline-flex justify-center py-2 px-4 border border-transparent shadow-sm text-sm font-medium rounded-md text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  Create Guesstimate
                </button>
              </div>
            </form>
          </div>
        </div>
      </div>

      <div className="bg-white shadow overflow-hidden sm:rounded-md">
        <ul className="divide-y divide-gray-200">
          {guesstimates.map((guesstimate) => (
            <li key={guesstimate.id}>
              <div className="px-4 py-4 sm:px-6">
                <div className="flex items-center justify-between">
                  <h3 className="text-lg leading-6 font-medium text-gray-900">{guesstimate.title}</h3>
                  <p className="mt-1 max-w-2xl text-sm text-gray-500">
                    Range: {guesstimate.min_value} - {guesstimate.max_value}
                  </p>
                </div>
                <div className="mt-2">
                  <p className="text-sm text-gray-500">{guesstimate.description}</p>
                </div>
                {guesstimate.actual_value && (
                  <div className="mt-2">
                    <p className="text-sm font-medium text-gray-500">
                      Actual Value: {guesstimate.actual_value}
                    </p>
                  </div>
                )}
                <div className="mt-2 text-sm text-gray-500">
                  Created: {new Date(guesstimate.created_at).toLocaleDateString()}
                </div>
              </div>
            </li>
          ))}
        </ul>
      </div>
    </div>
  );
};

export default GuesstimateDashboard; 