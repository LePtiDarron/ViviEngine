import CodeBlock from "./CodeBlock";

const Instalation = ({ activeSection }) => {
  return (
    <section id="installation" className={`section ${activeSection === 'installation' ? 'active' : ''}`}>
      <h2>Installation & Usage</h2>
      
      <div className="install-section">
        <h3>🚀 Quick Start</h3>
        <p>Get Vivi Engine running in minutes with these simple steps:</p>
        
        <div className="install-steps">
          <div className="install-step">
            <h4>1. Prerequisites</h4>
            <p>Ensure you have Python 3.7+ installed on your system.</p>
          </div>
          <div className="install-step">
            <h4>2. Install Pygame</h4>
            <p>Vivi Engine is built on top of Pygame for graphics and input handling.</p>
          </div>
          <div className="install-step">
            <h4>3. Clone Repository</h4>
            <p>Download the latest version from GitHub and start building!</p>
          </div>
        </div>
      </div>

      <h3>Installation Commands</h3>
      <CodeBlock path="/code-snippets/install.sh" />

      <h3>Your First Game</h3>
      <p>Create a simple game with just a few lines of code:</p>
      <CodeBlock path="/code-snippets/use.py" />

      <h3>Project Structure</h3>
      <p>Organize your game project like this:</p>
      <CodeBlock path="/code-snippets/project_structure.txt" />

      <br></br>
      <a href="https://github.com/LePtiDarron/ViviEngine" className="btn w-100 d-flex justify-content-center" target="_blank">View Full Examples on GitHub</a>
    </section>
  );
};

export default Instalation;