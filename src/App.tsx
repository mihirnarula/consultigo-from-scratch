import React from 'react';
import { BrowserRouter as Router, Routes, Route } from 'react-router-dom';
import Navbar from './components/Navbar';
import Home from './pages/Home';
import CaseStudies from './pages/CaseStudies';
import Guesstimates from './pages/Guesstimates';
import Examples from './pages/Examples';
import Frameworks from './pages/Frameworks';
import Profile from './pages/Profile';

function App() {
  return (
    <Router>
      <div className="min-h-screen">
        <Navbar />
        <Routes>
          <Route path="/" element={<Home />} />
          <Route path="/case-studies" element={<CaseStudies />} />
          <Route path="/guesstimates" element={<Guesstimates />} />
          <Route path="/examples" element={<Examples />} />
          <Route path="/frameworks" element={<Frameworks />} />
          <Route path="/profile" element={<Profile />} />
        </Routes>
      </div>
    </Router>
  );
}

export default App; 