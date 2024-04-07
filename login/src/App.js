
import React from 'react';
import './App.css';
import LoginForm from './Components/LoginForm/LoginForm';
import ChatUI from './Components/ChatUI/ChatUI';
import SignUp from './Components/SignUpForm/SignUpForm';
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";

function App() {
  return (
    <div className="App">
      <Router>
        <Routes>
          <Route path="/" element={<LoginForm/>} />
          <Route path="/chat" element={<ChatUI/>} />
          <Route path="/login" element={<SignUp/>} />
        </Routes>
      </Router>
    </div>
  );
}

export default App;
