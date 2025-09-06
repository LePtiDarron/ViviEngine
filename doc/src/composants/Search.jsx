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

    classes.forEach(classItem => {
      index.push({
        type: 'class',
        name: classItem.name,
        description: classItem.description,
        data: classItem,
        searchText: `${classItem.name} ${classItem.description}`.toLowerCase()
      });
    });

    functions.forEach(func => {
      index.push({
        type: 'function',
        name: func.name,
        description: func.description,
        data: func,
        searchText: `${func.name} ${func.description} ${func.prototype || ''}`.toLowerCase()
      });
    });

    varialbes.forEach(variableGroup => {
      index.push({
        type: 'variable',
        name: variableGroup.category,
        description: `Variables de ${variableGroup.category}`,
        data: variableGroup,
        searchText: `${variableGroup.category}`.toLowerCase()
      });
    });

    return index;
  }, []);

  const searchResults = useMemo(() => {
    if (!searchTerm.trim()) return [];
    
    const term = searchTerm.toLowerCase();
    return searchIndex
      .filter(item => item.name.toLowerCase().startsWith(term))
      .slice(0, 10);
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
                <div className={propertyGroup.category === 'Properties' ? 'parameter-list' : 'method-list'}>
                  {propertyGroup.items.map((item, itemIndex) => (
                    <div key={itemIndex} className={propertyGroup.category === 'Properties' ? 'parameter-item' : 'method-item'}>
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

      case 'function':
        return (
          <div className="class-card">
            <div className="class-name">{data.name}</div>
            <div className="function-content">
              <p className="function-description">{data.prototype}</p>
              <p className="function-description">{data.description}</p>
              <CodeBlock path={`code-snippets/functions/${data.name}.py`} />
            </div>
          </div>
        );

      case 'variable':
        return (
          <div className="class-card">
            <div className="class-name">{data.category}</div>
            <div className="parameter-list">
              {data.items.map((item, index) => (
                <Variable key={index} item={item} />
              ))}
            </div>
          </div>
        );

      default:
        return null;
    }
  };

  return (
    <section id="search" className={`section ${activeSection === 'search' ? 'active' : ''}`}>
      <h2>Search</h2>
      <p>Search in Vivi Engine features :</p>

      <div className="search-container" style={{ position: 'relative', marginBottom: '2rem' }}>
        <input
          type="text"
          value={searchTerm}
          onChange={handleSearchChange}
          onFocus={() => setShowSuggestions(true)}
          onBlur={handleInputBlur}
          placeholder="Search for a class, a function or a constant..."
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
              maxHeight: '300px',
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
                  {result.name} <span style={{ color: '#666', fontWeight: 'normal' }}>({result.type})</span>
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
          <p>Aucun résultat trouvé pour "{searchTerm}"</p>
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

export default Search;