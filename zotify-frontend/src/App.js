import logo from './logo.svg';
import {Route, Routes } from 'react-router-dom';

import './App.css';
import About from './About'
import Home from './Home'
import { useState, useEffect } from 'react'; //two functions provided by React
//Navigation Module and Introduction Page

// let show = false;
function App() {
  // const [songs, setSongs] = useState('---');

  // const [show, setShow] = useState(true);

  // function clik() {
  //   setShow(!show)
  //   setSongs(<h1>test</h1>)
  // }
  // useEffect(function(){
  //   let backendData = 'the less'
  // }, []);

  return (
    <Routes>
      <Route path="/" element={<Home/>} />
      {/* <Route path="/hello" element={<About songs={songs} setSongs={setSongs}/>} /> */}
      <Route path="/" element={<About/>} />
    </Routes>
  );
}

export default App;
