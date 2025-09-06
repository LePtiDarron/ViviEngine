import { useState } from 'react';
import CodeBlock from './CodeBlock';
import { functions } from './functions';

const Functions = ({ activeSection }) => {
  const [expandedFunction, setExpandedFunction] = useState(null);

  const toggleFunction = (functionName) => {
    setExpandedFunction(expandedFunction === functionName ? null : functionName);
  };

  const groupedFunctions = functions.reduce((acc, func) => {
    if (!acc[func.category]) {
      acc[func.category] = [];
    }
    acc[func.category].push(func);
    return acc;
  }, {});

  return (
    <section id="functions" className={`section ${activeSection === 'functions' ? 'active' : ''}`}>
      <h2>Core Functions</h2>
      <p>Vivi Engine provides a comprehensive set of utility functions for common game development tasks:</p>

      {Object.entries(groupedFunctions).map(([category, funcs], index) => (
        <div className="class-card" key={`category-${index}`}>
          <div className="class-name">{category}</div>
          <div className='functions-list'>
            {funcs.map((func) => (
              <div key={`func-${func.name}`} className="function-accordion">
                <div 
                  className={`function-header ${expandedFunction === func.name ? 'expanded' : ''}`}
                  onClick={() => toggleFunction(func.name)}
                >
                  <code className="function-signature">{func.name}</code>
                  <span className="accordion-icon">▶</span>
                </div>
                
                {expandedFunction === func.name && (
                  <div className="function-content">
                    <p className="function-description">{func.prototype}</p>
                    <p className="function-description">{func.description}</p>
                    <CodeBlock path={`code-snippets/functions/${func.name}.py`} />
                  </div>
                )}
              </div>
            ))}
          </div>
        </div>
      ))}
    </section>
  );
};

export default Functions;
