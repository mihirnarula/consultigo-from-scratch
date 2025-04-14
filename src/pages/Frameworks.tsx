import React, { useState } from 'react';

interface Framework {
  id: string;
  title: string;
  category: 'Strategy' | 'Operations' | 'Organization' | 'Analysis';
  description: string;
  content: string;
}

const Frameworks: React.FC = () => {
  const [selectedFramework, setSelectedFramework] = useState<Framework | null>(null);

  const frameworks: Framework[] = [
    {
      id: 'porter-five-forces',
      title: "Porter's Five Forces",
      category: 'Strategy',
      description: 'A framework for analyzing competitive forces that shape industry profitability.',
      content: `Porter's Five Forces Analysis Framework:

1. Competitive Rivalry
- Number and size of competitors
- Industry growth rate
- Fixed costs and exit barriers
- Product differentiation
- Switching costs

2. Threat of New Entrants
- Economies of scale
- Capital requirements
- Access to distribution
- Government regulations
- Brand loyalty

3. Bargaining Power of Suppliers
- Number of suppliers
- Uniqueness of input
- Switching costs
- Threat of forward integration
- Impact on costs

4. Bargaining Power of Buyers
- Number of customers
- Size of orders
- Price sensitivity
- Switching costs
- Threat of backward integration

5. Threat of Substitutes
- Price-performance trade-off
- Switching costs
- Buyer propensity to substitute
- Relative price performance`
    },
    {
      id: 'mckinsey-7s',
      title: 'McKinsey 7S Framework',
      category: 'Organization',
      description: 'A tool for analyzing organizational effectiveness and alignment.',
      content: `McKinsey 7S Framework Components:

1. Strategy
- Long-term planning
- Resource allocation
- Competitive advantage
- Business objectives

2. Structure
- Organizational hierarchy
- Reporting lines
- Decision-making process
- Coordination mechanisms

3. Systems
- Business processes
- Information systems
- Control mechanisms
- Performance measurement

4. Shared Values
- Corporate culture
- Core beliefs
- Company mission
- Ethical guidelines

5. Style
- Leadership approach
- Management behavior
- Communication patterns
- Corporate culture

6. Staff
- Human resources
- Employee profiles
- Training and development
- Motivation systems

7. Skills
- Core competencies
- Technical capabilities
- Employee abilities
- Organizational strengths`
    },
    {
      id: 'business-model-canvas',
      title: 'Business Model Canvas',
      category: 'Strategy',
      description: 'A strategic management template for developing new or documenting existing business models.',
      content: `Business Model Canvas Components:

1. Value Propositions
- Products and services
- Customer problems solved
- Customer needs met
- Unique selling points

2. Customer Segments
- Target markets
- User personas
- Customer characteristics
- Market size

3. Channels
- Distribution methods
- Communication channels
- Sales channels
- Customer touchpoints

4. Customer Relationships
- Relationship types
- Acquisition strategy
- Retention methods
- Growth strategy

5. Revenue Streams
- Revenue models
- Pricing strategy
- Payment methods
- Revenue sources

6. Key Resources
- Physical assets
- Intellectual property
- Human resources
- Financial resources

7. Key Activities
- Core processes
- Production
- Problem-solving
- Platform maintenance

8. Key Partnerships
- Strategic alliances
- Supplier relationships
- Joint ventures
- Coopetition

9. Cost Structure
- Fixed costs
- Variable costs
- Economies of scale
- Cost optimization`
    }
  ];

  if (selectedFramework) {
    return (
      <div className="min-h-screen bg-gray-50">
        <div className="container mx-auto px-4 py-8">
          <div className="max-w-3xl mx-auto">
            <div className="mb-6 flex items-center">
              <button 
                onClick={() => setSelectedFramework(null)}
                className="text-gray-600 hover:text-gray-900 flex items-center gap-2"
              >
                <svg xmlns="http://www.w3.org/2000/svg" className="h-5 w-5" viewBox="0 0 20 20" fill="currentColor">
                  <path fillRule="evenodd" d="M9.707 16.707a1 1 0 01-1.414 0l-6-6a1 1 0 010-1.414l6-6a1 1 0 011.414 1.414L5.414 9H17a1 1 0 110 2H5.414l4.293 4.293a1 1 0 010 1.414z" clipRule="evenodd" />
                </svg>
                Back to Frameworks
              </button>
            </div>
            <div className="bg-white rounded-lg shadow-sm p-8">
              <div className="mb-6">
                <h1 className="text-3xl font-bold text-gray-900 mb-2">{selectedFramework.title}</h1>
                <span className="inline-block px-3 py-1 bg-blue-50 text-blue-700 rounded-full text-sm font-medium">
                  {selectedFramework.category}
                </span>
              </div>
              <div className="space-y-8">
                <div>
                  <h2 className="text-xl font-semibold text-gray-900 mb-3">Overview</h2>
                  <p className="text-gray-600 text-lg">
                    {selectedFramework.description}
                  </p>
                </div>
                <div>
                  <h2 className="text-xl font-semibold text-gray-900 mb-3">Framework Details</h2>
                  <div className="bg-gray-50 p-6 rounded-lg">
                    <pre className="whitespace-pre-wrap text-gray-600 font-mono text-sm">
                      {selectedFramework.content}
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
            <h1 className="text-3xl font-bold text-gray-900">Frameworks</h1>
            <p className="text-gray-600 mt-2">Master essential consulting frameworks and methodologies</p>
          </div>
          <div className="space-y-4">
            {frameworks.map((framework) => (
              <button
                key={framework.id}
                onClick={() => setSelectedFramework(framework)}
                className="w-full p-6 bg-white rounded-lg shadow-sm hover:shadow-md transition-shadow duration-200 text-left"
              >
                <div className="flex justify-between items-center">
                  <div>
                    <h3 className="text-xl font-semibold text-gray-900 mb-1">{framework.title}</h3>
                    <span className="text-sm text-blue-600">{framework.category}</span>
                  </div>
                </div>
              </button>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Frameworks; 