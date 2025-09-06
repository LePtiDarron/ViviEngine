import { varialbes } from "./variables";

const Variable = ({ item }) => {
  const parts = item.split(' ');
  const label = parts[0];
  const color = parts[1];

  return (
    <div className="variable-item">
      {color && (
        <span style={{
          backgroundColor: `rgb${color}`,
          border: '1px solid black',
          width: '1rem',
          height: '1rem',
          display: 'inline-block',
          borderRadius: '2px'
        }}/>
      )}
      <code>{label}</code>
    </div>
  );
};

const Variables = ({ activeSection }) => {
  return (
    <section id="variables" className={`section ${activeSection === 'variables' ? 'active' : ''}`}>
      <h2>Built-in Variables</h2>
      <p>Vivi Engine provides predefined constants for common game development needs:</p>

      {varialbes.map((variableGroup, groupIndex) => (
        <div key={`variable-group-${groupIndex}`} className="class-card">
          <div className="class-name">{variableGroup.category}</div>
          
          <div className="parameter-list">
            {variableGroup.items.map((item, itemIndex) => (
              <Variable 
                key={`${groupIndex}-${itemIndex}`}
                item={item}
              />
            ))}
          </div>
        </div>
      ))}
    </section>
  );
};

export default Variables;