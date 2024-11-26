import React, { useState } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import axios from 'axios';
import 'react-tabs/style/react-tabs.css';
import './FurnitureTabs.css';
import {useNavigate} from "react-router-dom";

const FurnitureTabs = () => {
  const roomWidth = parseFloat(localStorage.getItem('room_width'));
  const roomLength = parseFloat(localStorage.getItem('room_length'));

  const [beds, setBeds] = useState([]);
  const [nightStands, setNightStands] = useState([]);
  const [officeTables, setOfficeTables] = useState([]);
  const [closets, setClosets] = useState([]);
  const [drawers, setDrawers] = useState([]);
  const [remainingSpace, setRemainingSpace] = useState(null);
  const [spaceStatus, setSpaceStatus] = useState(null);
  const [placements, setPlacements] = useState([]);
  const navigate = useNavigate();

  const handleFurnitureCountChange = (setFunction, count, defaultType = 'small') => {
    setFunction(Array.from({ length: count }, (_, index) => ({ id: index + 1, type: defaultType })));
  };

  const handleFurnitureTypeChange = (setFunction, id, type, furnitureArray) => {
    setFunction(furnitureArray.map((item) => (item.id === id ? { ...item, type } : item)));
  };


  const handleSubmitFurnitureChoices = async () => {
    const furnitureData = { beds, nightStands, officeTables, closets, drawers };
    try {
      const bedroom_id = localStorage.getItem('bedroom_id');
      const response = await axios.post(`/api/${bedroom_id}/calculate-space`, furnitureData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });

      setRemainingSpace(response.data.remaining_space);
      setSpaceStatus(response.data.has_enough_space ? 'Enough space available!' : 'Not enough space available.');
      setPlacements(response.data.placements);

    } catch (error) {
      console.error('Error submitting furniture data:', error);
      alert('There was an error saving your furniture data.');
    }
  };
    const handleLogout = () => {
    localStorage.removeItem('token'); // Remove token from localStorage
    navigate('/login'); // Redirect to login page
  };

  return (
      <div className="furniture-tabs">
        <button className="back-arrow" onClick={() => navigate('/dashboard')}>
          &#8592; Back
        </button>
        <button className="logout-button" onClick={handleLogout}>
          Log Out
        </button>
        <h1>Select Furniture for Your Bedroom</h1>
        <Tabs>
          <TabList>
            <Tab>Bed</Tab>
            <Tab>Night Stand</Tab>
            <Tab>Office Table</Tab>
            <Tab>Closet</Tab>
            <Tab>Drawer</Tab>
            <Tab>Final Result</Tab>
          </TabList>

          {/* Bed Tab */}
          <TabPanel>
            <h2>Choose Your Beds</h2>
            <label>
              Number of Beds (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={beds.length}
                  onChange={(e) => handleFurnitureCountChange(setBeds, Number(e.target.value), 'single')}
              />
            </label>
            {beds.map((bed) => (
                <div key={bed.id}>
                  <label>
                    Bed {bed.id} Type:
                    <select
                        value={bed.type}
                        onChange={(e) => handleFurnitureTypeChange(setBeds, bed.id, e.target.value, beds)}
                    >
                      <option value="single">single</option>
                      <option value="double">double</option>
                      <option value="queen">queen</option>
                      <option value="king">king</option>
                    </select>
                  </label>
                </div>
            ))}
          </TabPanel>

          {/* Night Stand Tab */}
          <TabPanel>
            <h2>Choose Your Night Stands</h2>
            <label>
              Number of Night Stands (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={nightStands.length}
                  onChange={(e) => handleFurnitureCountChange(setNightStands, Number(e.target.value), 'small')}
              />
            </label>
            {nightStands.map((stand) => (
                <div key={stand.id}>
                  <label>
                    Night Stand {stand.id} Type:
                    <select
                        value={stand.type}
                        onChange={(e) => handleFurnitureTypeChange(setNightStands, stand.id, e.target.value, nightStands)}
                    >
                      <option value="small">small</option>
                      <option value="medium">medium</option>
                      <option value="large">large</option>
                    </select>
                  </label>
                </div>
            ))}
          </TabPanel>


          {/* Office Table Tab */}
          <TabPanel>
            <h2>Choose Your Office Tables</h2>
            <label>
              Number of Office Tables (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={officeTables.length}
                  onChange={(e) => handleFurnitureCountChange(setOfficeTables, Number(e.target.value), 'small')}
              />
            </label>
            {officeTables.map((table) => (
                <div key={table.id}>
                  <label>
                    Office Table {table.id} Type:
                    <select
                        value={table.type}
                        onChange={(e) => handleFurnitureTypeChange(setOfficeTables, table.id, e.target.value, officeTables)}
                    >
                      <option value="small">small</option>
                      <option value="medium">medium</option>
                      <option value="large">large</option>
                    </select>
                  </label>
                </div>
            ))}
          </TabPanel>

          {/* Closet Tab */}
          <TabPanel>
            <h2>Choose Your Closets</h2>
            <label>
              Number of Closets (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={closets.length}
                  onChange={(e) => handleFurnitureCountChange(setClosets, Number(e.target.value), 'small')}
              />
            </label>
            {closets.map((closet) => (
                <div key={closet.id}>
                  <label>
                    Closet {closet.id} Type:
                    <select
                        value={closet.type}
                        onChange={(e) => handleFurnitureTypeChange(setClosets, closet.id, e.target.value, closets)}
                    >
                      <option value="small">small</option>
                      <option value="medium">medium</option>
                      <option value="large">large</option>
                    </select>
                  </label>
                </div>
            ))}
          </TabPanel>

          {/* Drawer Tab */}
          <TabPanel>
            <h2>Choose Your Drawers</h2>
            <label>
              Number of Drawers (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={drawers.length}
                  onChange={(e) => handleFurnitureCountChange(setDrawers, Number(e.target.value), '3 drawers')}
              />
            </label>
            {drawers.map((drawer) => (
                <div key={drawer.id}>
                  <label>
                    Drawer {drawer.id} Type:
                    <select
                        value={drawer.type}
                        onChange={(e) => handleFurnitureTypeChange(setDrawers, drawer.id, e.target.value, drawers)}
                    >
                      <option value="3 drawers">3 drawers</option>
                      <option value="4 drawers">4 drawers</option>
                    </select>
                  </label>
                </div>
            ))}
          </TabPanel>

          {/* Final Result Tab */}
          <TabPanel>
            <h2>Final Result</h2>
            <div className={'furniture-result'}>
              <button onClick={handleSubmitFurnitureChoices} className={'furniture-btn'}>
                <label>Submit Furniture Choices</label>
              </button>
            </div>

            {remainingSpace !== null && (
                <div>
                  <p>Remaining Space: {remainingSpace} sq. feet.</p>
                  <p>Status: {spaceStatus}</p>
                </div>
            )}

            {remainingSpace !== null && (
                <div className="room-layout">
                  <h3>Room Layout</h3>
                  <div className="room-grid">
                    {Array.from({length: roomLength}).map((_, rowIndex) => (
                        <div className="row" key={rowIndex}>
                          {Array.from({length: roomWidth}).map((_, colIndex) => {
                            const furniturePlacement = placements.find(
                                (placement) => placement.x === colIndex && placement.y === rowIndex
                            );
                            return (
                                <div
                                    key={colIndex}
                                    className={`cell ${furniturePlacement ? 'occupied' : ''}`}
                                >
                                  {furniturePlacement ? (
                                      <span>{furniturePlacement.type}</span>
                                  ) : null}
                                </div>
                            );
                          })}
                        </div>
                    ))}
                  </div>
                </div>
            )}
          </TabPanel>
        </Tabs>
      </div>
  );
};

export default FurnitureTabs;






