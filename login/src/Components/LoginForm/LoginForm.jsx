import React, { useEffect } from 'react';
import './LoginForm.css';
import { FaUser, FaLock } from "react-icons/fa";
import { useNavigate } from "react-router-dom";



const LoginForm = () => {
    const navigate = useNavigate();

    

    

    return (
        
        <div className='wrapper'>
            <form action="">
                <h1>Login</h1>
                <div className="input-box">
                    <input type="text" placeholder='Username' required />
                    <FaUser className='icon'/>
                </div>

                <div className="input-box">
                    <input type="password" placeholder='Password' required />
                    <FaLock className='icon'/>
                </div>


                <div className="remember-forgot">
                    <label><input type="checkbox" /> Remember me </label>
                    <a href="#">Forgot password?</a>
                </div>

                <button 
                    type="submit"
                    onClick={() => {navigate("/chat")}}
                >
                    Login
                </button>



                <div className="register-link">
                    <p>Don't have an account? <a href="#">Register</a></p>
                </div>

            </form>

        </div>
    );
};

export default LoginForm;