import {Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
import './About.css';

function About({songs,setSongs}) {

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
        <div>
            <h1 id="mytitle"> Zotify</h1>
        </div>

        <div>
            <h6 id="undertitle">Zotfeels: How are you feeling?</h6>
        </div>
            <button type="button" class="rounded">Happy</button>
            <button type="button" class="rounded">Angry</button>
        <div>
            <button type="button" class="rounded">Sad</button>
            <button type="button" class="rounded">Chill</button>
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