
import React, { useState, useEffect } from 'react';
import { Tab, Tabs, TabList, TabPanel } from 'react-tabs';
import axios from 'axios';
import 'react-tabs/style/react-tabs.css';
import './ModifyFurniture.css';
import {useNavigate} from "react-router-dom";

const ModifyFurnitureTab = () => {
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
  const [isLoading, setIsLoading] = useState(true);
  const navigate = useNavigate();


  useEffect(() => {
    fetchExistingFurniture();
  }, []);

  const fetchExistingFurniture = async () => {
    try {
      const bedroom_id = localStorage.getItem('bedroom_id');
      const response = await axios.get(`/api/${bedroom_id}/modify-furniture`, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });

      // Update state with existing furniture
      setBeds(response.data.beds.map(bed => ({
        id: bed.id,
        type: bed.type
      })));

      setNightStands(response.data.nightStands.map(stand => ({
        id: stand.id,
        type: stand.type
      })));

      setOfficeTables(response.data.officeTables.map(table => ({
        id: table.id,
        type: table.type
      })));

      setClosets(response.data.closets.map(closet => ({
        id: closet.id,
        type: closet.type
      })));

      setDrawers(response.data.drawers.map(drawer => ({
        id: drawer.id,
        type: drawer.type
      })));

      setIsLoading(false);
    } catch (error) {
      console.error('Error fetching furniture data:', error);
      setIsLoading(false);
    }
  };

  const handleFurnitureCountChange = (setFunction, count, defaultType = 'small', currentItems) => {
    if (count > currentItems.length) {
      // Adding new items
      const newItems = Array.from({ length: count - currentItems.length }, (_, index) => ({
        id: Math.max(...currentItems.map(item => item.id), 0) + index + 1,
        type: defaultType
      }));
      setFunction([...currentItems, ...newItems]);
    } else {
      // Removing items
      setFunction(currentItems.slice(0, count));
    }
  };

  const handleFurnitureTypeChange = (setFunction, id, type, furnitureArray) => {
    setFunction(furnitureArray.map((item) => (item.id === id ? { ...item, type } : item)));
  };

  const handleSubmitFurnitureChoices = async () => {
    const bedroom_id = localStorage.getItem('bedroom_id');
    const furnitureData = { beds, nightStands, officeTables, closets, drawers };

    console.log("Bedroom ID:", bedroom_id);
    console.log("Token:", localStorage.getItem('token'));
    console.log("Furniture Data:", JSON.stringify(furnitureData, null, 2));

    try {
      // Use PUT request to update existing furniture
      const response = await axios.put(`/api/${bedroom_id}/modify-furniture`, furnitureData, {
        headers: {
          Authorization: `Bearer ${localStorage.getItem('token')}`,
        },
      });

      setPlacements(response.data.placements);
      setSpaceStatus("Furniture updated successfully!");

    } catch (error) {
      console.error('Error updating furniture:', error);
      setSpaceStatus("Error updating furniture. Please try again.");
    }
  };

  if (isLoading) {
    return <div>Loading furniture data...</div>;
  }
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
        <h1>Modify Furniture for Your Bedroom</h1>
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
            <h2>Modify Your Beds</h2>
            <label>
              Number of Beds (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={beds.length}
                  onChange={(e) => handleFurnitureCountChange(setBeds, Number(e.target.value), 'single', beds)}
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
            <h2>Modify Your Night Stands</h2>
            <label>
              Number of Night Stands (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={nightStands.length}
                  onChange={(e) => handleFurnitureCountChange(setNightStands, Number(e.target.value), 'small', nightStands)}
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
            <h2>Modify Your Office Tables</h2>
            <label>
              Number of Office Tables (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={officeTables.length}
                  onChange={(e) => handleFurnitureCountChange(setOfficeTables, Number(e.target.value), 'small', officeTables)}
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
            <h2>Modify Your Closets</h2>
            <label>
              Number of Closets (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={closets.length}
                  onChange={(e) => handleFurnitureCountChange(setClosets, Number(e.target.value), 'small', closets)}
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
            <h2>Modify Your Drawers</h2>
            <label>
              Number of Drawers (Max: 3):
              <input
                  type="number"
                  min="0"
                  max="3"
                  value={drawers.length}
                  onChange={(e) => handleFurnitureCountChange(setDrawers, Number(e.target.value), '3 drawers', drawers)}
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
                <label>Update Furniture Arrangement</label>
              </button>
            </div>

            {spaceStatus && (
                <div>
                  <p>Status: {spaceStatus}</p>
                </div>
            )}

            {placements.length > 0 && (
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

export default ModifyFurnitureTab;