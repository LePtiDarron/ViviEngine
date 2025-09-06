import { useEffect, useState } from "react";
import { Prism as SyntaxHighlighter } from "react-syntax-highlighter";
import { tomorrow } from "react-syntax-highlighter/dist/esm/styles/prism";

const CodeBlock = ({ path }) => {
  const [code, setCode] = useState("");
  const [copied, setCopied] = useState(false);

  useEffect(() => {
    fetch(path)
      .then((res) => res.text())
      .then((text) => setCode(text))
      .catch((err) => console.error(err));
  }, [path]);

  const handleCopy = async () => {
    try {
      await navigator.clipboard.writeText(code);
      setCopied(true);
      setTimeout(() => setCopied(false), 2000);
    } catch (err) {
      console.error('Failed to copy code:', err);
    }
  };

  let language = "text";
  if (path.endsWith(".py")) language = "python";
  else if (path.endsWith(".sh")) language = "bash";
  else if (path.endsWith(".txt")) language = "text";

  const customStyle = {
    ...tomorrow,
    'pre[class*="language-"]': {
      ...tomorrow['pre[class*="language-"]'],
      background: '#2d3748',
      borderRadius: '0 0 10px 10px',
      margin: 0,
      padding: '1.5rem',
      fontSize: '14px',
      lineHeight: '1.5',
    },
    'code[class*="language-"]': {
      ...tomorrow['code[class*="language-"]'],
      background: 'transparent',
      fontSize: '14px',
      fontFamily: "'Monaco', 'Consolas', 'Courier New', monospace",
    }
  };

  return (
    <div className="code-block-container">
      <button 
        className={`copy-button ${copied ? 'copied' : ''}`}
        onClick={handleCopy}
        title={copied ? 'Copied!' : 'Copy code'}
      >
        {copied ? (
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <polyline points="20,6 9,17 4,12"></polyline>
          </svg>
        ) : (
          <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2">
            <rect x="9" y="9" width="13" height="13" rx="2" ry="2"></rect>
            <path d="M5 15H4a2 2 0 0 1-2-2V4a2 2 0 0 1 2-2h9a2 2 0 0 1 2 2v1"></path>
          </svg>
        )}
      </button>
      
      <div className="code-content">
        <SyntaxHighlighter 
          language={language} 
          style={customStyle}
          customStyle={{
            margin: 0,
            background: 'transparent'
          }}
        >
          {code}
        </SyntaxHighlighter>
      </div>
    </div>
  );
};

export default CodeBlock;