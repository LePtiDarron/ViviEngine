const Home = ({ activeSection }) => {
  return (
    <section id="home" className={`section ${activeSection === 'home' ? 'active' : ''}`}>
      <div className="hero">
        <h2>Welcome to Vivi Engine</h2>
        <p>A powerful yet simple 2D game engine built with Python and Pygame.</p>
        <a href="https://github.com/LePtiDarron/ViviEngine" className="btn" target="_blank">Get Started on GitHub</a>
        <a href="#installation" className="btn btn-secondary" onClick={() => showSection('installation')}>Quick Install</a>
      </div>

      <div className="feature-grid">
        <div className="feature-card">
          <h3>🎮 Game-Ready Components</h3>
          <p>Built-in Entity, Scene, and Game classes provide a solid foundation for any 2D game project. Start prototyping immediately with intuitive architecture.</p>
        </div>
        <div className="feature-card">
          <h3>🚀 Easy to Learn</h3>
          <p>Familiar syntax and concepts for developers, with Python's simplicity for newcomers. Comprehensive documentation gets you started quickly.</p>
        </div>
        <div className="feature-card">
          <h3>🎨 Rich Graphics Support</h3>
          <p>Sprite rendering, transformations, surfaces, cameras, and drawing utilities. Everything you need to bring your game world to life.</p>
        </div>
        <div className="feature-card">
          <h3>🎯 Input & Audio</h3>
          <p>Complete keyboard and mouse input handling, plus audio support for sound effects and music. Build interactive experiences effortlessly.</p>
        </div>
        <div className="feature-card">
          <h3>⚡ Performance Focused</h3>
          <p>Optimized rendering pipeline, entity management, and delta-time based movement for smooth gameplay across different frame rates.</p>
        </div>
        <div className="feature-card">
          <h3>🔧 Extensible Design</h3>
          <p>Clean, modular architecture makes it easy to extend the engine with custom functionality and integrate third-party libraries.</p>
        </div>
      </div>
    </section>
  );
};

export default Home;