import React, { useState, useEffect } from 'react';
import jsonData from './datafile.json';

function App() {
  const [articleData, setArticleData] = useState(jsonData.data);

  useEffect(() => {
    setArticleData(jsonData.data);
  }, []);

  return (
    <div className="App">
      <h1>Informações do JSON</h1>
      {articleData && (
        <div>
          <h2>Objetivo:</h2>
          <p>{articleData.objective}</p>

          <h2>Problema:</h2>
          <p>{articleData.problem}</p>
          <h2>Bag of Words:</h2>
          <ul>
            {Object.entries(articleData.bag_of_words).map(([word, count]) => (
              <li key={word}>
                {word}: {count}
              </li>
            ))}
          </ul>
          
          <h2>Palavras Mais Comuns:</h2>
          <ul>
            {articleData.most_commons.map(([word, count]) => (
              <li key={word}>
                {word}: {count}
              </li>
            ))}
          </ul>
        </div>
      )}
    </div>
  );
}

export default App;
