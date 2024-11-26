import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { useParams, useNavigate } from 'react-router-dom';

const ModifyBedroom = () => {
  const { bedroomId } = useParams();
  const [bedroomData, setBedroomData] = useState(null);
  const [message, setMessage] = useState('');
  const navigate = useNavigate();

  useEffect(() => {
    const fetchBedroomData = async () => {
      try {
        const response = await axios.get(`http://localhost:5000/api/bedroom/${bedroomId}`, {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        });
        // Extract the bedroom data from the response
        setBedroomData(response.data.bedroom);
      } catch (error) {
        console.error('Error fetching bedroom data:', error);
        setMessage('Failed to load bedroom data.');
      }
    };
    fetchBedroomData();
  }, [bedroomId]);

  const handleSubmit = async (e) => {
    e.preventDefault();

    try {
      const response = await axios.put(
        `http://localhost:5000/api/bedroom/${bedroomId}`,
        bedroomData,
        {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        }
      );
      setMessage(response.data.message || 'Bedroom updated successfully!');
      navigate(`/furniture/modify/${bedroomId}`);
    } catch (error) {
      console.error('Error updating bedroom:', error);
      setMessage('Failed to update bedroom.');
    }
  };
    const handleLogout = () => {
    localStorage.removeItem('token'); // Remove token from localStorage
    navigate('/login'); // Redirect to login page
  };
  const handleChange = (e) => {
    const { name, value } = e.target;
    setBedroomData({
      ...bedroomData,
      [name]: name === 'freeSpacePercentage' ? parseFloat(value) : value,
      size: {
        ...bedroomData.size,
        [name]: ['width', 'length', 'height'].includes(name)
          ? parseFloat(value)
          : bedroomData.size[name],
      },
    });
  };

  if (!bedroomData) {
    return <p>Loading...</p>;
  }

  return (
      <div className={'modify-bedroom-container'}>
        <button className="back-arrow" onClick={() => navigate('/dashboard')}>
          &#8592; Back
        </button>
        <button className="logout-button" onClick={handleLogout}>
          Log Out
        </button>
        <div className={'modify-bedroom-header'}>
          <h1>Modify Bedroom</h1>
        </div>
        {message && <p>{message}</p>}
        <form onSubmit={handleSubmit}>
          <div className={'input-box'}>
            <label>
              Bedroom Name:
              <input
                  type="text"
                  name="name"
                  className={'input-field'}
                  value={bedroomData.name || ''}
                  onChange={handleChange}
                  required
              />
            </label>
            <br/>
            <label>
              Width (feet):
              <input
                  type="number"
                  name="width"
                  className={'input-field'}
                  value={bedroomData.size.width || ''}
                  onChange={handleChange}
                  required
              />
            </label>
            <br/>
            <label>
              Length (feet):
              <input
                  type="number"
                  name="length"
                  className={'input-field'}
                  value={bedroomData.size.length || ''}
                  onChange={handleChange}
                  required
              />
            </label>
            <br/>
            <label>
              Height (feet):
              <input
                  type="number"
                  name="height"
                  className={'input-field'}
                  value={bedroomData.size.height || ''}
                  onChange={handleChange}
                  required
              />
            </label>
            <br/>
            <label>
              Free Space Percentage (%):
              <input
                  type="number"
                  name="freeSpacePercentage"
                  className={'input-field'}
                  max="100"
                  value={bedroomData.freeSpacePercentage || ''}
                  onChange={handleChange}
                  required
              />
            </label>
            <br/>
            <div className="input-submit">
              <button type="submit" className="submit-btn">Save Bedroom</button>
            </div>
          </div>
        </form>
      </div>
  );
};

export default ModifyBedroom;