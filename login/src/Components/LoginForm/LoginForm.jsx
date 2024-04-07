import React, { useEffect, useState } from 'react';
import './LoginForm.css';
import { FaUser, FaLock } from "react-icons/fa";
import { useNavigate } from "react-router-dom";
import login from '../../openai.js'


const LoginForm = () => {
    const navigate = useNavigate();
    const [username, setUsername] = useState('');
    const [password, setPassword] = useState('');

    const handleLogin = () =>  {
        var res = login(username, password).then(data => setCookie("token", JSON.stringify(data), 7));
        console.log(res);

        if(res) {
            navigate("/chat");
        }

    }

    const setCookie = (name, value, days)  => {
        var expires = "";
        if (days) {
            var date = new Date();
            date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000));
            expires = "; expires=" + date.toUTCString();
        }
        document.cookie = name + "=" + (value || "")  + expires + "; path=/";
    }

    

    return (
        
        <div className='wrapper'>
            <form action="">
                <h1>Login</h1>
                <div className="input-box">
                    <input type="text" placeholder='Username' required 
                    onChange={(e) => setUsername(e.target.value)}/>
                    <FaUser className='icon'/>
                </div>

                <div className="input-box">
                    <input type="password" placeholder='Password' required 
                    onChange={(e) => setPassword(e.target.value)} />
                    <FaLock className='icon'/>
                </div>


                <div className="remember-forgot">
                    <label><input type="checkbox" /> Remember me </label>
                    <a href="#">Forgot password?</a>
                </div>

                <button 
                    type="submit"
                    onClick={() => {handleLogin()}}
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