import React, { useState } from 'react';
import DifficultyBadge from '../components/DifficultyBadge';

interface Example {
  id: string;
  title: string;
  difficulty: 'Easy' | 'Medium' | 'Hard';
  description: string;
  solution: string;
}

const Examples: React.FC = () => {
  const [selectedExample, setSelectedExample] = useState<Example | null>(null);

  const examples: Example[] = [
    {
      id: 'retail-expansion',
      title: 'Retail Chain Expansion',
      difficulty: 'Medium',
      description: 'A national retail chain is considering expanding into the European market. They need to decide which countries to enter first and how to approach the expansion.',
      solution: `Here's a structured approach to solve this case:

1. Market Assessment
- Analyzed market size and growth potential in key European countries
- Evaluated competitive landscape and market saturation
- Assessed regulatory environment and entry barriers

2. Target Market Selection
- Prioritized UK, Germany, and France based on:
  * Large market size and high disposable income
  * Cultural similarity and ease of doing business
  * Existing supply chain partnerships

3. Entry Strategy
- Recommended phased approach:
  * Phase 1: Enter UK market through acquisition of regional chain
  * Phase 2: Expand to Germany through joint venture
  * Phase 3: Enter France through organic growth

4. Implementation Plan
- Timeline: 3-year rollout plan
- Required Investment: €500M
- Expected ROI: 15% by year 5
- Key success metrics defined`
    },
    {
      id: 'digital-transformation',
      title: 'Digital Transformation',
      difficulty: 'Hard',
      description: 'A traditional manufacturing company needs to undergo digital transformation to remain competitive. How should they approach this change?',
      solution: `Strategic Approach to Digital Transformation:

1. Current State Assessment
- Legacy systems inventory
- Process efficiency analysis
- Digital maturity evaluation
- Skills gap analysis

2. Transformation Strategy
- Priority Areas:
  * Cloud migration of core systems
  * IoT implementation in production
  * Data analytics capabilities
  * Digital customer interface

3. Implementation Roadmap
- Phase 1: Foundation (6-12 months)
  * Cloud infrastructure setup
  * Basic data analytics
  * Employee training initiation

- Phase 2: Core Transformation (12-24 months)
  * IoT sensor deployment
  * Advanced analytics implementation
  * Digital customer portal

- Phase 3: Innovation (24-36 months)
  * AI/ML implementation
  * Predictive maintenance
  * Digital twin development

4. Change Management
- Structured training program
- Clear communication strategy
- Quick wins identification
- Regular feedback loops`
    }
  ];

  if (selectedExample) {
    return (
      <div className="min-h-screen bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-3xl mx-auto">
            <div className="mb-6 flex items-center">
              <button 
                onClick={() => setSelectedExample(null)}
                className="text-gray-600 hover:text-gray-900 flex items-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clipRule="evenodd" />
                </svg>
                Back to Examples
              </button>
            </div>
            <div className="bg-white rounded-lg shadow-sm p-8">
              <div className="flex justify-between items-center mb-6">
                <h1 className="text-3xl font-bold text-gray-900">{selectedExample.title}</h1>
                <DifficultyBadge level={selectedExample.difficulty} />
              </div>
              <div className="space-y-8">
                <div>
                  <h2 className="text-xl font-semibold text-gray-900 mb-3">Problem Statement</h2>
                  <p className="text-gray-600 text-lg">
                    {selectedExample.description}
                  </p>
                </div>
                <div>
                  <h2 className="text-xl font-semibold text-gray-900 mb-3">Sample Solution</h2>
                  <div className="bg-gray-50 p-6 rounded-lg">
                    <pre className="whitespace-pre-wrap text-gray-600 font-mono text-sm">
                      {selectedExample.solution}
                    </pre>
                  </div>
                </div>
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
            <h1 className="text-3xl font-bold text-gray-900">Examples</h1>
            <p className="text-gray-600 mt-2">Learn from detailed example cases and solutions</p>
          </div>
          <div className="space-y-4">
            {examples.map((example) => (
              <button
                key={example.id}
                onClick={() => setSelectedExample(example)}
                className="w-full p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 text-left"
              >
                <div className="flex justify-between items-center">
                  <h3 className="text-xl font-semibold text-gray-900">{example.title}</h3>
                  <DifficultyBadge level={example.difficulty} />
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Examples; 