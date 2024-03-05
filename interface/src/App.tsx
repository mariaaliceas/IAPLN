import React, { useState, useEffect } from 'react';
import './App.css';
import jsonData from './datafile.json';
import { setupInputValidation } from './inputValidator';


function App() {
  const [articleData, setArticleData] = useState(jsonData.data);

  useEffect(() => {
    setArticleData(jsonData.data);
  }, []);

  function findMostCommonWords(data: any) {
    const mostCommons = data?.most_commons;
    if (!mostCommons) {
      console.error('Atributo "most_commons" não encontrado no arquivo JSON.');
      return [];
    }
    return mostCommons.map(([word, count]: [string, number]) => ({ word, count }));
  }
  const [mostCommonWords, setMostCommonWords] = useState<{ word: string; count: number }[]>([]);

  useEffect(() => {
    const commonWords = findMostCommonWords(jsonData.data.most_commons);
    setMostCommonWords(commonWords);
  }, [mostCommonWords]);

  setupInputValidation()
  findMostCommonWords(jsonData.data.most_commons)

  return (
    <div className="App">
      <h1>Buscador</h1>
      {articleData && (
        <div>
          <div className='.App-line'>
            <h2 className='App-tittleH2'>Informe número do artigo para busca:</h2>
            <input type='text' className='App-input' id="search-article" name="article">
            </input>

          </div>
          <button className='App-button' onClick={findMostCommonWords}>Pesquisar</button>
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
