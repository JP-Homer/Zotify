import {Link } from 'react-router-dom';
import { useNavigate } from "react-router-dom";
import './Home.css';

function Home(){

    // function Change() {
    //     let navigate = useNavigate();
    //     navigate('/moods'${newMoods.id}`);
    // }

    return (
        
        <div id="body">
            <div id="top">
                <span className='bn'>Welcome to Zotify</span>
            </div>

            <div id="bottom">  
                <Link to"/mood"><button type="button" class="rounded-pill">Get Started</button></Link>
            </div>
            
        </div>
        
    )

}

export default Home;