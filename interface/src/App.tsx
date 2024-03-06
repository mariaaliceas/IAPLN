import React, { useState, useEffect } from 'react';
import './App.css';
import jsonData from './datafile.json';
import { setupInputValidation } from './inputValidator';


function App() {
  const [articleData, setArticleData] = useState(jsonData);
  const [inputValue, setInputValue] = useState('');
  const [inputObjective, setInputObjective] = useState('');
  const [inputProblem, setInputProblem] = useState('');
  const [inputMethod, setInputMethod] = useState('');
  const [inputContribution, setInputContribution] = useState('');
  const [inputName, setInputName] = useState('');
  const [inputFrequence, setInputFrequence] = useState([] as any);
  const [inputReferences, setInputReferences] = useState({} as any);

  const handleInputChange = (event: any) => {
    setInputValue(event.target.value);
  };

  function findArticle() {
    const article = articleData.find((a: any) => {
      return a.data.arqName === `articles/${inputValue}.pdf`
    })


    //setInputBagWords(article?.data.bag_of_words ?? {})
    setInputObjective(article?.data.objective ?? '')
    setInputProblem(article?.data.problem ?? '')
    setInputMethod(article?.data.method ?? '')
    setInputContribution(article?.data.contribution ?? '')
    setInputName(article?.data.name ?? '')
    setInputFrequence(article?.data.frequency ?? [])
    setInputReferences(article?.data.references ?? {})

    console.log(inputFrequence)

    console.log(article?.data.frequency)
  }

  
  setupInputValidation()

  return (
    <div className="App">
      <h1>Buscador</h1>
      {articleData && (
        <div>
          <div className='.App-line'>
            <h2 className='App-tittleH2'>Informe número do artigo para busca:</h2>
            <input type='text' value={inputValue}
              onChange={handleInputChange} className='App-input' id="search-article" name="article">
            </input>

          </div>
          <button className='App-button' onClick={findArticle}>Pesquisar</button>
          <h2>Título do artigo:</h2>
          <p>{inputName}</p>
          <h2>Objetivo:</h2>
          <p>{inputObjective}</p>
          <h2>Problema:</h2>
          <p>{inputProblem}</p>
          <h2>Metodo:</h2>
          <p>{inputMethod}</p>
          <h2>Contribuição:</h2>
          <p>{inputContribution}</p>
          <h2>Frequência de palavras:</h2>
          <ul>
            {inputFrequence.map((frequency: any) => 
              (<li key={frequency[0]}>{`${frequency[0]}: ${frequency[1]}`}</li>)
            )
            }
          </ul>
          <h2>Referências:</h2>
          <p>{inputReferences.join("\n")}</p>
        </div>
      )}
    </div>
  );
}

export default App;
