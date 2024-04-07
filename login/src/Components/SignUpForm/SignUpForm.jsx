import React, { useEffect } from 'react';
import './SignUpForm.css';
import { FaUser, FaLock } from "react-icons/fa";
import { MdEmail } from "react-icons/md"
import { useNavigate } from "react-router-dom";

const SignUp = () => {
    const navigate = useNavigate();

    return (
        
        <div className='wrapper'>
            <form action="">
                <h1>Sign Up</h1>
                <div className="input-box">
                    <input type="text" placeholder='First Name' required />
                    <FaUser className='icon'/>
                </div>

                <div className="input-box">
                    <input type="text" placeholder='Last Name' required />
                    <FaUser className='icon'/>
                </div>

                
                <div className="input-box">
                    <input type="text" placeholder='Age' required />
                    <FaUser className='icon'/>
                </div>

                
                <div className="input-box">
                    <input type="text" placeholder='Email' required />
                    <MdEmail className='icon'/>
                </div>

                <div className="input-box">
                    <input type="text" placeholder='Username' required />
                    <FaUser className='icon'/>
                </div>

                <div className="input-box">
                    <input type="password" placeholder='Password' required />
                    <FaLock className='icon'/>
                </div>

                <div className="input-box">
                    <input type="password" placeholder='Re-enter Password' required />
                    <FaLock className='icon'/>
                </div>

                <button 
                    type="submit"
                    onClick={() => {navigate("/chat")}}
                >
                    Sign Up
                </button>
            </form>

        </div>
    );
};

export default SignUp;