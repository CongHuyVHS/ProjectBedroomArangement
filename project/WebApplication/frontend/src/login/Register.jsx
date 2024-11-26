// src/components/Register.jsx

import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import axios from 'axios';
import './Register.css';

const Register = () => {
  const [username, setUsername] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [error, setError] = useState('');
  const [success, setSuccess] = useState(false);
  const navigate = useNavigate();

  const handleRegister = async (e) => {
    e.preventDefault();
    setError('');
    setSuccess(false);

    try {
      await axios.post('http://localhost:5000/api/register', { username, email, password });

      setSuccess(true);
      navigate('/login'); // Redirect to login page after registration
    } catch (err) {
      setError(err.response?.data?.msg || 'An error occurred');
    }
  };

  return (
    <div className="register-box">
      <div className="register-header">
        <header>Register</header>
      </div>
      {error && <p className="error">{error}</p>}
      {success && <p className="success">User registered successfully!</p>}
      <form onSubmit={handleRegister} className="input-box">
        <input
          type="text"
          value={username}
          onChange={(e) => setUsername(e.target.value)}
          placeholder="Username"
          className="input-field"
          required
        />
        <input
          type="email"
          value={email}
          onChange={(e) => setEmail(e.target.value)}
          placeholder="Email"
          className="input-field"
          required
        />
        <input
          type="password"
          value={password}
          onChange={(e) => setPassword(e.target.value)}
          placeholder="Password"
          className="input-field"
          required
        />
        <div className="input-submit">
          <button type="submit" className="submit-btn">
            <label>Register</label>
          </button>
        </div>
      </form>
      <div className="sign-in-link">
        <p>Already have an account? <a href="/login">Sign in here</a></p>
      </div>
    </div>
  );
};

export default Register;
