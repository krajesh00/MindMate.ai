import React from 'react';
import gptLogo from '../assets/chatgpt.svg';
import './ChatUI.css'
import addBtn from '../assets/add-30.png';
import msgIcon from '../assets/message.svg';
import home from '../assets/home.svg';
import saved from '../assets/bookmark.svg';
import rocket from '../assets/rocket.svg';
import sendBtn from '../assets/send.svg';
import userIcon from '../assets/user-icon.png';
import gptImgLogo from '../assets/chatgptLogo.svg';

const ChatUI = () => {

    

    return ( 
        
        <div className="appContainer">
            
            <div className="sidebar">
                <div className="upperSide">
                    <div className="upperSideTop"><img src={gptLogo} alt="Logo" className="logo" /><span className="brand">Mind Mentor</span></div>
                    <button className="midBtn"><img src={addBtn} alt="new chat" className="addBtn" />New Chat</button>
                    <div className="upperSideBottom">
                        <button className="query"><img src={msgIcon} alt="Query" />What is Programming?</button>
                    </div>
                </div>


                <div className="lowerSide">
                    <div className="listItems"><img src={home} alt="Home" className="listItemsImg" />Home</div>
                    <div className="listItems"><img src={saved} alt="Saved" className="listItemsImg" />Saved</div>
                    <div className="listItems"><img src={rocket} alt="Upgrade" className="listItemsImg" />Upgrade to Pro</div>

                </div>
            </div>

            <div className="main">
                <div className="chats">
                    <div className="chat">
                        <img className="chatImg" src={userIcon} alt="" /> <p className="txt"> Blah Blah Blah</p>
                    </div>
                    <div className="chat">
                        <img className="chatImg" src={gptImgLogo} alt="" /> <p className="txt"> Blah Blah Blah</p>
                    </div>
                </div>
                <div className="chatFooter">
                    <div className="inp">
                        <input type="text" placeholder='Send a message'/><button className="send"><img src={sendBtn} alt="Send" /></button>
                    </div>
                    <p className="txt"> May Give you Wrong stuff. We not responsible. Don't sue </p>
                </div>
            </div>
        </div>
    );

};

export default ChatUI;