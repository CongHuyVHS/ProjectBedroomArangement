import React, { useState } from 'react';
import { BrowserRouter as Router, Route, Routes, Navigate } from 'react-router-dom';
import Login from './login/Login';
import Register from './login/Register';
import Bedroom from './bedroom/Bedroom';
import Furniture from './furniture/Furniture'
import Dashboard from "./bedroom/Dashboard";
import ModifyBedroom from "./bedroom/modify/ModifyBedroom"
import ModifyFurnitureTab from "./furniture/modify/ModifyFurniture";
import './App.css';

function App() {
  const [isAuthenticated, setIsAuthenticated] = useState(false);

  const handleLoginSuccess = () => {
    setIsAuthenticated(true);
  };

  return (
    <Router>
      <Routes>
        {/* Redirect to bedroom if authenticated, otherwise to login */}
        <Route path="/" element={isAuthenticated ? <Bedroom /> : <Navigate to="/login" />} />

        {/* Login page */}
        <Route path="/login" element={<Login onLoginSuccess={handleLoginSuccess} />} />

        {/* Register page */}
        <Route path="/register" element={<Register />} />

        {/* bedroom page, protected route */}
        <Route path="/dashboard" element={isAuthenticated ? <Dashboard /> : <Navigate to="/login" />} />

        <Route path="/bedroom" element={isAuthenticated ? <Bedroom /> : <Navigate to="/login" />} />

        {/* Furniture tabs page, accessible only after bedroom creation */}
        <Route path="/furniture" element={isAuthenticated ? <Furniture/> : <Navigate to="/bedroom" />} />

        <Route path="/bedroom/modify/:bedroomId" element={isAuthenticated ? <ModifyBedroom /> : <Navigate to="/login" />} />

        <Route path="/furniture/modify/:bedroomId" element={isAuthenticated ? <ModifyFurnitureTab /> : <Navigate to="/login" />} />


      </Routes>
    </Router>
  );
}

export default App;