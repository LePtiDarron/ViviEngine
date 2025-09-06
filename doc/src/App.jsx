import { useState, useEffect } from 'react';
import Installation from "./composants/Installation";
import Home from "./composants/Home";
import Classes from './composants/Classes';
import './App.css';
import Functions from './composants/Functions';
import Tutorials from './composants/Tutorials';
import Variables from './composants/Variables';
import Search from './composants/Search';

const ViviEngineDocumentation = () => {
  const [activeSection, setActiveSection] = useState('');
  const [isMobileMenuOpen, setIsMobileMenuOpen] = useState(false);

  const showSection = (e, sectionName) => {
    e.preventDefault();
    history.replaceState(null, '', `#${sectionName}`);
    setActiveSection(sectionName);
    setIsMobileMenuOpen(false); // Fermer le menu mobile après sélection
  };

  const toggleMobileMenu = () => {
    setIsMobileMenuOpen(!isMobileMenuOpen);
  };

  useEffect(() => {
    const hash = window.location.hash ? window.location.hash.slice(1) : 'home';
    setActiveSection(hash);

    const handleHashChange = () => {
      const newHash = window.location.hash ? window.location.hash.slice(1) : 'home';
      setActiveSection(newHash);
    };

    const handleResize = () => {
      if (window.innerWidth > 992) {
        setIsMobileMenuOpen(false);
      }
    };

    window.addEventListener('hashchange', handleHashChange);
    window.addEventListener('resize', handleResize);
    
    return () => {
      window.removeEventListener('hashchange', handleHashChange);
      window.removeEventListener('resize', handleResize);
    };
  }, []);

  return (
    <div className='app'>
      <div className="container">
        <header>
          <h1>Vivi Engine</h1>
          <p>A Python 2D Game Engine</p>
        </header>

        <nav>
          <div className="nav-container">
            <button 
              className="mobile-menu-toggle"
              onClick={toggleMobileMenu}
              aria-label="Toggle navigation menu"
            >
              {isMobileMenuOpen ? '✕' : '☰'}
            </button>
            
            <div className={`nav-menu ${isMobileMenuOpen ? 'show' : ''}`}>
              <a href="#home" className={`nav-item ${activeSection === 'home' ? 'active' : ''}`} onClick={(e) => showSection(e, 'home')}>Home</a>
              <a href="#installation" className={`nav-item ${activeSection === 'installation' ? 'active' : ''}`} onClick={(e) => showSection(e, 'installation')}>Installation</a>
              <a href="#classes" className={`nav-item ${activeSection === 'classes' ? 'active' : ''}`} onClick={(e) => showSection(e, 'classes')}>Classes</a>
              <a href="#functions" className={`nav-item ${activeSection === 'functions' ? 'active' : ''}`} onClick={(e) => showSection(e, 'functions')}>Functions</a>
              <a href="#variables" className={`nav-item ${activeSection === 'variables' ? 'active' : ''}`} onClick={(e) => showSection(e, 'variables')}>Variables</a>
              <a href="#search" className={`nav-item ${activeSection === 'search' ? 'active' : ''}`} onClick={(e) => showSection(e, 'search')}>Search</a>
              <a href="#tutorials" className={`nav-item ${activeSection === 'tutorials' ? 'active' : ''}`} onClick={(e) => showSection(e, 'tutorials')}>Tutorials</a>
            </div>
          </div>
        </nav>

        <main className='main-content'>
          <Home activeSection={activeSection}/>
          <Installation activeSection={activeSection}/>
          <Classes activeSection={activeSection}/>
          <Functions activeSection={activeSection}/>
          <Tutorials activeSection={activeSection}/>
          <Variables activeSection={activeSection}/>
          <Search activeSection={activeSection}/>
        </main>

        <footer>
          <p>&copy; 2025 Vivi Engine Documentation. Built with passion for game development.</p>
          <p><a href="https://github.com/LePtiDarron/ViviEngine" style={{color: '#3498db'}} target="_blank">Visit GitHub Repository</a></p>
        </footer>
      </div>
    </div>
  );
};

export default ViviEngineDocumentation;