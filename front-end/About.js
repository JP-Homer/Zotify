import {Link } from 'react-router-dom';

function About({songs,setSongs}) {

    function change() {
        setSongs(<h2>Changed</h2>)
    }
    return (
        <div>
        <h1>{songs}</h1>
        <button onClick={change}>Button</button>
        <Link to="/hi">ghjy</Link>
        </div>
    )
}

export default About;