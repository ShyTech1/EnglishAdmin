import React, { useState } from "react";



function SearchBar() {
     const [input, setInput] = useState('');
    
     const handleInput = (e) => {
         setInput(e.target.value)
        }  

    return ( 
        <div>
           <div class="input-group mb-3">
                <span class="input-group-text" id="inputGroup-sizing-default">Default</span>
                <input type="text" 
                        onChange={handleInput}
                        class="form-control"  
                        aria-label="Sizing example input" 
                        aria-describedby="inputGroup-sizing-default"></input>
            </div>
        </div>
     );
}

export default SearchBar;