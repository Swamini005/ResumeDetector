// Header.jsx
import React from 'react';
import './Header.css';

const Header = () => {
  return (
    <header className="header">
      <div className="container">
        <h1 className="logo">Resume Detector</h1>
        <nav className="nav">
          <ul className="nav__list">
            <li className="nav__item"><a href="#about">About</a></li>
            <li className="nav__item"><a href="#features">Features</a></li>
            <li className="nav__item"><a href="#contact">Contact</a></li>
          </ul>
        </nav>
      </div>
    </header>
  );
}

export default Header;
