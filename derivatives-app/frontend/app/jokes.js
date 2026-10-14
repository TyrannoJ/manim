"use client";
 //https://official-joke-api.appspot.com/random_joke
import { useEffect, useState } from "react";

export default function HandleVideo() {
    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    
    const [joke,setJoke] = useState("");
    const [setup,setSetup] = useState("");
    const [punchline,setPunchline] = useState("");
    async function get_joke() { //get joke form API on button press
        
        const res = await fetch("https://official-joke-api.appspot.com/random_joke", {
            method: "GET",
            
            });
        const data=await res.json();
        setPunchline(data.punchline);
        setSetup(data.setup);

    }
    
 
  
  

  

 

  
  return (
    
      
      
        <div className="mb-4">
          
          <div className="w-9/10 md:w-2/3 mx-auto">
          
            <h1 className="text-xl md:text-4xl text-cyan-800 font-bold mb-2">Jokes</h1>
            <div className="flex flex-col">
                
                
                <button 
                    onClick={get_joke}
                    type="submit" 
                    className="bg-gray-950 text-cyan-800 text-xl rounded-md px-2 outline-2 outline-cyan-800 hover:outline-offset-1 hover:outline-3 hover:font-bold active:text-cyan-600 active:outline-cyan-600 w-25 mb-2"
                    >
                    get joke
                </button>
                

                

                <p className="text-lg md:xl text-cyan-800  mb-2">{setup}</p>
                <p className="text-lg md:xl text-cyan-800  mb-2">{punchline}</p>
            </div>
            
          </div>
        </div>
      
    
  );}