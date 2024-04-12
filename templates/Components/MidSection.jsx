import React from "react";
import "./IntroSection.css";

const MidSection = () => {
  return (
    <section className="intro-section">
      <div className="intro-container">
        <div className="intro-text">
          <h1 className="intro-title">Welcome to Resume Detector</h1>
          <p className="intro-description">
            Resume Detector is a powerful tool designed to analyze text content in various file formats, such as PDF, DOCX, and TXT, to determine if it contains information typically found in a resume.
          </p>
          <div className="intro-buttons">
            <a href="#Contact" className="intro-button contact-btn">Contact Us</a>
            <a href="https://drive.google.com/file/d/your-resume-link" className="intro-button resume-btn" target="_blank">Download Resume</a>
          </div>
        </div>
        <div className="intro-image">
          <img src="/resume_detector_image.png" alt="Resume Detector" />
        </div>
      </div>
    </section>
  );
};

export default MidSection;
