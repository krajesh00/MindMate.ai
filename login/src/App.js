
import React from 'react';
import './App.css';
import LoginForm from './Components/LoginForm/LoginForm';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import ChatUI from './Components/ChatUI/ChatUI.jsx';

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<LoginForm/>} />
          <Route path="/chat" element={<ChatUI />} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
