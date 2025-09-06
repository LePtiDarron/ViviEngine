const Tutorials = ({ activeSection }) => {
  return (
    <section id="tutorials" className={`section ${activeSection === 'tutorials' ? 'active' : ''}`}>
      <h2>Tutorials</h2>
      <p>Learn Vivi Engine step by step with these comprehensive tutorials:</p>
    </section>
  );
};

export default Tutorials;