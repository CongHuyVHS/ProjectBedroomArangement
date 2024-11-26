// src/components/Bedroom.jsx

import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Bedroom.css'


const Bedroom = () => {
  const [name, setName] = useState('');
  const [width, setWidth] = useState('');
  const [length, setLength] = useState('');
  const [height, setHeight] = useState('');
  const [freeSpace, setFreeSpace] = useState('');
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  const handleLogout = () => {
    localStorage.removeItem('token'); // Remove token from localStorage
    navigate('/login'); // Redirect to login page
  };

  const handleSubmit = async (e) => {
  e.preventDefault();

  const bedroomData = {
    name,
    size: {
      width: parseFloat(width),
      length: parseFloat(length),
      height: parseFloat(height),
    },
    freeSpacePercentage: parseFloat(freeSpace)
  };

  try {
    const response = await axios.post('http://localhost:5000/api/bedroom', bedroomData,{
      headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`
          }
    });
    localStorage.setItem('bedroom_id', response.data.bedroom_id);
    localStorage.setItem('room_width', width);
    localStorage.setItem('room_length', length);

    console.log(localStorage.getItem('token'));

    setMessage(response.data.message);
    navigate('/furniture');
  } catch (error) {
    console.error('Error submitting bedroom information:', error);
    setMessage('Error saving bedroom information.');
  }
};


  return (
      <div className="bedroom-container">
        <button className="back-arrow" onClick={() => navigate('/dashboard')}>
          &#8592; Back
        </button>
        <button className="logout-button" onClick={handleLogout}>
          Log Out
        </button>

        <div className={"bedroom-header"}>
          <h1>Add Bedroom Information</h1>
        </div>
        <form onSubmit={handleSubmit}>
          <div className={'input-box'}>
            <label>
              Bedroom Name:
              <input
                  type="text"
                  value={name}
                  className="input-field"

                  onChange={(e) => setName(e.target.value)}
                  required
              />
            </label>
            <br/>
            <label>
              Width (feet):
              <input
                  type="number"
                  step="10"
                  className="input-field"

                  value={width}
                  onChange={(e) => setWidth(e.target.value)}
                  required
              />
            </label>
            <br/>
            <label>
              Length (feet):
              <input
                  type="number"
                  step="10"
                  className="input-field"

                  value={length}
                  onChange={(e) => setLength(e.target.value)}
                  required
              />
            </label>
            <br/>
            <label>
              Height (feet):
              <input
                  type="number"
                  step="10"
                  className="input-field"

                  value={height}
                  onChange={(e) => setHeight(e.target.value)}
                  required
              />
            </label>
            <br/>
            <label>
              Free Space Percentage (%):
              <input
                  type="number"
                  step="1"
                  className="input-field"
                  max={100}
                  value={freeSpace}
                  onChange={(e) => setFreeSpace(e.target.value)}
                  required
              />
            </label>
            <br/>
            <div className={'input-submit'}></div>
            <button type="submit" className={'submit-btn'}>
              <label>Save bedroom</label>
            </button>
          </div>
        </form>
        {message && <p>{message}</p>}
      </div>
  );
};

export default Bedroom;
