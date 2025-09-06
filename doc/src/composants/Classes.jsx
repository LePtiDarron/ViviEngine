import CodeBlock from "./CodeBlock";
import { classes } from "./classes";

const Classes = ({ activeSection }) => {
  return (
    <section id="classes" className={`section ${activeSection === 'classes' ? 'active' : ''}`}>
      <h2>Core Classes</h2>
      <p>Vivi Engine provides {classes.length} main {classes.length === 1 ? 'class' : 'classes'} that form the backbone of any game:</p>

      {classes.map((classItem, classIndex) => (
        <div key={classIndex} className="class-card">
          <div className="class-name">{classItem.name}</div>
          <p>{classItem.description}</p>
          
          {classItem.properties && classItem.properties.map((propertyGroup, propIndex) => (
            <div key={`${classIndex}-${propIndex}`}>
              <h4>{propertyGroup.category}</h4>
              <div className={propertyGroup.category === 'Properties' ? 'parameter-list' : 'method-list'}>
                {propertyGroup.items.map((item, itemIndex) => (
                  <div key={`${classIndex}-${propIndex}-${itemIndex}`} className={propertyGroup.category === 'Properties' ? 'parameter-item' : 'method-item'}>
                    <code>{item.name}</code> - {item.description}
                  </div>
                ))}
              </div>
            </div>
          ))}

          {classItem.example && (
            <>
              <h4>Example</h4>
              <CodeBlock path={classItem.example}/>
            </>
          )}
        </div>
      ))}
    </section>
  );
};

export default Classes;