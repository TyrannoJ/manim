"use client";
 //https://official-joke-api.appspot.com/random_joke
import { useEffect, useState } from "react";

export default function HandlePicture({connected}) {
    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    
    const [text, setText] = useState("");
    const [result,setResult] =useState("Put in a function (click help in the bottom right if you don't understand how)");
    const [received,setReceived]=useState(false);
    
    
 
  
  async function handleSubmit(e) 
    {
        e.preventDefault();
      if (connected=="connected"){
        setResult("your request is being handled...")
      }
      else {
        setResult("no connection to the backend, sorry :(")
      }
    
    setReceived(false);
    const res = await fetch(`${API_URL}/send-text`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });
    
    
    const data = await res.json();
    setResult("finished picture");
    setReceived(true);
  }
  
  async function textChange(e) {
    setText(e.target.value);
    setReceived(false);
    setResult("Put in a function (click help in the bottom right if you don't understand how)")
    
  }


  
  return (
    
      
      
        <div >
          
          <div className="w-9/10 md:w-2/3 mx-auto">
          
            <h1 className="text-xl md:text-4xl text-cyan-800 font-bold mb-2">Pictures</h1>
            <form onSubmit={handleSubmit} className="flex flex-row">
              <input 
                className=" bg-gray-950 text-cyan-800  placeholder-cyan-950 text-xl mr-3 outline-1 outline-cyan-800 w-1/2 md:w-1/4 hover:outline-2 focus:outline-cyan-700 focus:text-cyan-700 focus:outline-2"
                value={text}
                onChange={(e) => textChange(e)}
                
                placeholder="ex: 2x2+4x"
              />
            <button 
                type="submit" 
                className="bg-gray-950 text-cyan-800 text-xl rounded-md px-2 outline-2 outline-cyan-800 hover:outline-offset-1 hover:outline-3 hover:font-bold active:text-cyan-600 active:outline-cyan-600"
                >
                  Send
            </button>
            </form>
            
            <p className="text-xl text-cyan-800 mb-2 mt-2">{result}</p>
            
            
            {received &&(
            <img src={`${API_URL}/picture/${text}`} alt="currently no picture" className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/>
            
            //<video controls width={640}>
              
              //<source src={`http://localhost:8000/video/${text}`} type="video/mp4" />
              //Your browser does not support the video tag.
              //<img src="dings.png"  className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/> 
            //</video>
            )}
            
          </div>
          
        </div>
      
    
  );}
