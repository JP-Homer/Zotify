import { render } from "react-dom";
import {
  BrowserRouter,
  Routes,
  Route,
} from "react-router-dom";
import App from './App';
// import your route components too

render(
  <BrowserRouter>
  

    <App />
  </BrowserRouter>,
  document.getElementById("root")
);