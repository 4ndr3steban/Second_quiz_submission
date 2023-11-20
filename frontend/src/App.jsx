import React, { useState } from 'react';
import Home from './components/Home';

const App = () => {
  const [res, setRes] = useState([]);

  const handleViewChange = (view) => {
    setCurrentView(view);
  };

  return (

    <Home/>

  );
};

export default App;