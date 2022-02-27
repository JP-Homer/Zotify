import {Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
import './About.css';
import peterImage from './clipart338064.png'
function About({songs,setSongs}) {

    function handleClick() {
        fetch('http://3d67-169-234-40-216.ngrok.io/happy').then(response => response.json()).then(response => {
            console.log(response);
            let url = 'https://open.spotify.com/playlist/' + response.ID;
            window.location = url;
        })
    }

    function handleClick2() {
        fetch('http://3d67-169-234-40-216.ngrok.io/angsty').then(response => response.json()).then(response => {
            console.log(response);
            let url2 = 'https://open.spotify.com/playlist/' + response.ID;
            window.location = url2;
        })
    }

    function handleClick3() {
        fetch('http://3d67-169-234-40-216.ngrok.io/sad').then(response => response.json()).then(response => {
            console.log(response);
            let url3 = 'https://open.spotify.com/playlist/' + response.ID;
            window.location = url3;
        })
    }

    function handleClick4() {
        fetch('http://3d67-169-234-40-216.ngrok.io/chill').then(response => response.json()).then(response => {
            console.log(response);
            let url4 = 'https://open.spotify.com/playlist/' + response.ID;
            window.location = url4;
        })
    }


    // function change() {
    //     setSongs(<h2>Changed</h2>)
    // }
    return (
        // <div>
        // <h1 className='bn'>{songs}</h1>
        // <button onClick={change}>Button</button>
        // <Link to="/tester">ghjy</Link>
        // </div>
        <>
        <div id="mytitle">
        <img src= {peterImage} alt="Peter"></img>
            <span > Zotify</span>
        </div>

        <div>
            <h6 id="undertitle">Zotfeels: How are you feeling?</h6>
        </div>

        <div class="wrapper">
            <button onClick={handleClick}type="button" class="rounded">Happy</button>
            <button onClick={handleClick2} type="button" class="rounded">Angsty</button>

            <button onClick={handleClick3} type="button" class="rounded">Sad</button>
            <button onClick={handleClick4} type="button" class="rounded">Chill</button>
        </div>
        {/* <div id="body2"> */}
           
            {/* <div id= "title">
                <h1>Zotify</h1>
            </div>

            <div id = "words">
                <p>Zotfeels: How are you feeling?</p>
            </div>

            <div id="buttons3">
                <button type="button" class="rounded">Happy</button>
                <button type="button" class="rounded">Angry</button>
            </div>

            <div id="buttons4">
                <button type="button" class="rounded">Sad</button>
                <button type="button" class="rounded">Chill</button>
            </div>

        </div> */}
        </>
    )
}

export default About;