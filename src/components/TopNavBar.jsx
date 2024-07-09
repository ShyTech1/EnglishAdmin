import React from 'react';
import 'bootstrap/dist/css/bootstrap.css';
import AppLogo from '../assets/AppLogo.png'

function TopNavBar() {

    const LOCALHOST= "http://localhost:3000/EnglishAdmin"

    return ( 
        <nav className="navbar navbar-expand-xl">
            <ul className="navbar-nav p-2 px-4">

                <li className="nav-item">
                    <a  href={LOCALHOST}>
                        <img src={AppLogo} alt="logo" className="navbar-brand w-40 h-50" />
                    </a>
                </li>

            </ul>
        </nav>
     );
}

export default TopNavBar;