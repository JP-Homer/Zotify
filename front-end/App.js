import logo from './logo.svg';
import {Route, Routes } from 'react-router-dom';

import './App.css';
import About from './About'
import { useState, useEffect } from 'react'; //two functions provided by React
//Navigation Module and Introduction Page

// let show = false;
function App() {
  const [songs, setSongs] = useState('---');

  const [show, setShow] = useState(true);

  function clik() {
    setShow(!show)
    setSongs(<h1>test</h1>)
  }
  // useEffect(function(){
  //   let backendData = 'the less'
  // }, []);

  return (
    <Routes>
    
      <Route path="/" element={<About songs={songs} setSongs={setSongs}/>} />
      <Route path="/hi" element={<h1>{songs}</h1>} />
    </Routes>
  );
}

export default App;
