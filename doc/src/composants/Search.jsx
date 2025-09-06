import { useState, useMemo } from 'react';
import CodeBlock from './CodeBlock';
import { classes } from './classes';
import { functions } from './functions';
import { varialbes } from './variables';

const Search = ({ activeSection }) => {
  const [searchTerm, setSearchTerm] = useState('');
  const [selectedItem, setSelectedItem] = useState(null);
  const [showSuggestions, setShowSuggestions] = useState(false);

  const searchIndex = useMemo(() => {
    const index = [];

    // Add classes to search index
    classes.forEach(classItem => {
      index.push({
        type: 'class',
        name: classItem.name,
        description: classItem.description,
        data: classItem,
        searchText: `${classItem.name} ${classItem.description}`.toLowerCase()
      });

      // Add individual methods from classes to search index
      if (classItem.properties) {
        classItem.properties.forEach(propertyGroup => {
          if (propertyGroup.items) {
            propertyGroup.items.forEach(item => {
              // Only add methods (not properties) to main search
              if (propertyGroup.category.includes('Method') || 
                  propertyGroup.category.includes('methods') ||
                  propertyGroup.category.includes('Management') ||
                  propertyGroup.category.includes('Constructor') ||
                  propertyGroup.category.includes('Detection') ||
                  propertyGroup.category.includes('Collision')) {
                index.push({
                  type: 'method',
                  name: `${classItem.name}.${item.name}`,
                  description: item.description,
                  data: { ...item, className: classItem.name, category: propertyGroup.category },
                  searchText: `${item.name} ${item.description} ${classItem.name}`.toLowerCase()
                });
              }
            });
          }
        });
      }
    });

    // Add functions to search index
    functions.forEach(func => {
      index.push({
        type: 'function',
        name: func.name,
        description: func.description,
        data: func,
        searchText: `${func.name} ${func.description} ${func.prototype || ''} ${func.category}`.toLowerCase()
      });
    });

    // Add variable groups to search index
    varialbes.forEach(variableGroup => {
      index.push({
        type: 'variable',
        name: variableGroup.category,
        description: `${variableGroup.category} variables`,
        data: variableGroup,
        searchText: `${variableGroup.category} variables constants`.toLowerCase()
      });

      // Add individual variables to search
      if (variableGroup.items) {
        variableGroup.items.forEach(item => {
          const variableName = item.split(' ')[0]; // Extract variable name before color
          index.push({
            type: 'variable_item',
            name: variableName,
            description: `Constant from ${variableGroup.category}`,
            data: { name: variableName, category: variableGroup.category, item: item },
            searchText: `${variableName} ${variableGroup.category}`.toLowerCase()
          });
        });
      }
    });

    return index;
  }, []);

  const searchResults = useMemo(() => {
    if (!searchTerm.trim()) return [];
    
    const term = searchTerm.toLowerCase();
    return searchIndex
      .filter(item => 
        item.name.toLowerCase().includes(term) || 
        item.searchText.includes(term)
      )
      .sort((a, b) => {
        // Prioritize exact matches
        const aExact = a.name.toLowerCase().startsWith(term);
        const bExact = b.name.toLowerCase().startsWith(term);
        if (aExact && !bExact) return -1;
        if (!aExact && bExact) return 1;
        
        // Then sort by type priority: functions > classes > methods > variables
        const typePriority = { function: 0, class: 1, method: 2, variable: 3, variable_item: 4 };
        return (typePriority[a.type] || 5) - (typePriority[b.type] || 5);
      })
      .slice(0, 15);
  }, [searchTerm, searchIndex]);

  const handleSearchChange = (e) => {
    setSearchTerm(e.target.value);
    setShowSuggestions(true);
    setSelectedItem(null);
  };

  const handleSelectItem = (item) => {
    setSelectedItem(item);
    setSearchTerm(item.name);
    setShowSuggestions(false);
  };

  const handleInputBlur = () => {
    setTimeout(() => setShowSuggestions(false), 200);
  };

  const renderSelectedItem = () => {
    if (!selectedItem) return null;

    const { type, data } = selectedItem;

    switch (type) {
      case 'class':
        return (
          <div className="class-card">
            <div className="class-name">{data.name}</div>
            <p>{data.description}</p>
            
            {data.properties && data.properties.map((propertyGroup, propIndex) => (
              <div key={propIndex}>
                <h4>{propertyGroup.category}</h4>
                <div className={propertyGroup.category === 'Properties' || 
                               propertyGroup.category.includes('Properties') ? 
                               'parameter-list' : 'method-list'}>
                  {propertyGroup.items.map((item, itemIndex) => (
                    <div key={itemIndex} className={
                      propertyGroup.category === 'Properties' || 
                      propertyGroup.category.includes('Properties') ? 
                      'parameter-item' : 'method-item'
                    }>
                      <code>{item.name}</code> - {item.description}
                    </div>
                  ))}
                </div>
              </div>
            ))}

            {data.example && (
              <>
                <h4>Example</h4>
                <CodeBlock path={data.example}/>
              </>
            )}
          </div>
        );

      case 'method':
        return (
          <div className="class-card">
            <div className="class-name">{data.className}.{data.name}</div>
            <p><strong>Category:</strong> {data.category}</p>
            <p><strong>Description:</strong> {data.description}</p>
            
            <h4>Usage</h4>
            <div className="method-item">
              <code>{data.name}</code>
            </div>
            
            <p><em>This method is part of the <strong>{data.className}</strong> class. 
            Check the complete class documentation for more context.</em></p>
          </div>
        );

      case 'function':
        return (
          <div className="class-card">
            <div className="class-name">{data.name}</div>
            <p><strong>Category:</strong> {data.category}</p>
            
            <div className="function-content">
              <h4>Prototype</h4>
              <div className="function-signature">
                <code>{data.prototype}</code>
              </div>
              
              <h4>Description</h4>
              <p>{data.description}</p>
              
              <h4>Example</h4>
              <CodeBlock path={`code-snippets/functions/${data.name}.py`} />
            </div>
          </div>
        );

      case 'variable':
        return (
          <div className="class-card">
            <div className="class-name">{data.category}</div>
            <p>Predefined constants for {data.category}</p>
            
            <div className="parameter-list">
              {data.items.map((item, index) => (
                <Variable key={index} item={item} />
              ))}
            </div>
          </div>
        );

      case 'variable_item':
        return (
          <div className="class-card">
            <div className="class-name">{data.name}</div>
            <p><strong>Category:</strong> {data.category}</p>
            <p><strong>Type:</strong> Predefined constant</p>
            
            <div className="parameter-list">
              <Variable item={data.item} />
            </div>
            
            <p><em>This constant is part of the <strong>{data.category}</strong> group.</em></p>
          </div>
        );

      default:
        return null;
    }
  };

  const getTypeDisplayName = (type) => {
    switch (type) {
      case 'class': return 'Class';
      case 'method': return 'Method';
      case 'function': return 'Function';
      case 'variable': return 'Variables';
      case 'variable_item': return 'Constant';
      default: return type;
    }
  };

  return (
    <section id="search" className={`section ${activeSection === 'search' ? 'active' : ''}`}>
      <h2>Search</h2>
      <p>Search through Vivi Engine features: classes, methods, functions and constants.</p>

      <div className="search-container" style={{ position: 'relative', marginBottom: '2rem' }}>
        <input
          type="text"
          value={searchTerm}
          onChange={handleSearchChange}
          onFocus={() => setShowSuggestions(true)}
          onBlur={handleInputBlur}
          placeholder="Search for a class, function, method or constant..."
          style={{
            width: '100%',
            padding: '0.75rem',
            fontSize: '1rem',
            border: '2px solid #ddd',
            borderRadius: '8px',
            outline: 'none'
          }}
        />

        {showSuggestions && searchResults.length > 0 && (
          <div 
            className="search-suggestions"
            style={{
              position: 'absolute',
              top: '100%',
              left: 0,
              right: 0,
              backgroundColor: 'white',
              border: '1px solid #ddd',
              borderRadius: '8px',
              boxShadow: '0 4px 6px rgba(0,0,0,0.1)',
              zIndex: 1000,
              maxHeight: '400px',
              overflowY: 'auto'
            }}
          >
            {searchResults.map((result, index) => (
              <div
                key={index}
                onClick={() => handleSelectItem(result)}
                style={{
                  padding: '0.75rem',
                  cursor: 'pointer',
                  borderBottom: index < searchResults.length - 1 ? '1px solid #eee' : 'none'
                }}
                onMouseEnter={(e) => e.target.style.backgroundColor = '#f5f5f5'}
                onMouseLeave={(e) => e.target.style.backgroundColor = 'white'}
              >
                <div style={{ fontWeight: 'bold' }}>
                  {result.name} 
                  <span style={{ color: '#666', fontWeight: 'normal', marginLeft: '0.5rem' }}>
                    ({getTypeDisplayName(result.type)})
                  </span>
                </div>
                <div style={{ fontSize: '0.9rem', color: '#666', marginTop: '0.25rem' }}>
                  {result.description}
                </div>
              </div>
            ))}
          </div>
        )}
      </div>

      {selectedItem && renderSelectedItem()}

      {searchTerm && !selectedItem && searchResults.length === 0 && (
        <div className="class-card">
          <p>No results found for "{searchTerm}"</p>
          <p><em>Try searching for:</em></p>
          <ul>
            <li>A class name: Game, Scene, Entity</li>
            <li>A function name: draw_sprite, keyboard_check, entity_create</li>
            <li>A method name: create, step, draw, destroy</li>
            <li>A category: Drawing, Input, Audio, Math</li>
          </ul>
        </div>
      )}

      {!searchTerm && (
        <div className="class-card">
          <h3>💡 Search Tips</h3>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '1rem', marginTop: '1rem' }}>
            <div>
              <h4>🏗️ Classes</h4>
              <p>Search "Game", "Scene", or "Entity" to see the main classes</p>
            </div>
            <div>
              <h4>🎨 Drawing Functions</h4>
              <p>Type "draw" to see all graphics functions</p>
            </div>
            <div>
              <h4>⌨️ Input Handling</h4>
              <p>Search "keyboard" or "mouse" for controls</p>
            </div>
            <div>
              <h4>🎮 Entity Management</h4>
              <p>Type "entity" for object creation and management</p>
            </div>
          </div>
        </div>
      )}
    </section>
  );
};

const Variable = ({ item }) => {
  const parts = item.split(' ');
  const label = parts[0];
  const color = parts[1];

  return (
    <div className="variable-item" style={{ display: 'flex', alignItems: 'center', gap: '0.5rem', marginBottom: '0.25rem' }}>
      {color && (
        <span style={{
          backgroundColor: `rgb${color}`,
          border: '1px solid black',
          width: '1rem',
          height: '1rem',
          display: 'inline-block',
          borderRadius: '2px',
          flexShrink: 0
        }}/>
      )}
      <code>{label}</code>
    </div>
  );
};

export default Search;