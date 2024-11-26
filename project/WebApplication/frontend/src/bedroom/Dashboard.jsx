import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';
import './Dashboard.css';


const Dashboard = () => {
  const [recentBedrooms, setRecentBedrooms] = useState([]);
  const navigate = useNavigate();
  const handleLogout = () => {
    // Remove the token from local storage
    localStorage.removeItem('token');
    navigate('/login');
  };

  const handleLogoClick = () => {
    navigate('/dashboard');
  };

  useEffect(() => {
    // Fetch recent items from the backend
    const fetchRecentBedrooms = async () => {
      try {
        const response = await axios.get('http://localhost:5000/api/recent-bedrooms', {
          headers: {
            Authorization: `Bearer ${localStorage.getItem('token')}`,
          },
        });
        setRecentBedrooms(response.data);
      } catch (error) {
        console.error('Error fetching recent bedrooms:', error);
      }
    };
    fetchRecentBedrooms();
  }, []);

  const handleCreateBedroom = () => {
    navigate('/bedroom'); // Navigate to the Bedroom page
  };

  const handleModifyBedroom = (bedroomId) => {
    navigate(`/bedroom/modify/${bedroomId}`); // Navigate to the Modify Bedroom page
  };

  return (
      <div className="dashboard-container">
        <aside className="sidebar">
          <h2>Dashboard</h2>
          <div className="input-create-bedroom">
            <button onClick={handleCreateBedroom} className="create-bedroom-button">
              <label>Create new bedroom</label>
            </button>
          </div>
        </aside>

        <main className="content">
          <h1>Welcome Back</h1>
          <div className="recent-items">
            <h2>Recent Bedrooms</h2>
            {recentBedrooms.length > 0 ? (
                <ul>
                  {recentBedrooms.map((bedroom) => (
                      <li key={bedroom.id}>
                        {bedroom.name} - {bedroom.width}x{bedroom.length}{' '}
                        <button
                            onClick={() => handleModifyBedroom(bedroom.id)}
                            className="modify-bedroom-button"
                        >
                          Modify
                        </button>
                      </li>
                  ))}
                </ul>
            ) : (
                <p>No recent items available.</p>
            )}
          </div>
        </main>
      </div>
  );
};

export default Dashboard;
