import React from 'react';
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom';
import MissionData from './components/MissionData';

const App: React.FC = () => {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<MissionData />} />
      </Routes>
    </Router>
  );
};

export default App;
