"use client";
 //https://official-joke-api.appspot.com/random_joke
import { useEffect, useState } from "react";

export default function Home() {
    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    
    const [text, setText] = useState("");
    const [result,setResult] =useState("Put in a function");
    const [received,setReceived]=useState(false);
    const [connected,setConnected]=useState("finding connection...");
    const [connectedColor,setConnectedColor]=useState("text-cyan-800");
    
 
  
  async function handleSubmit(e) 
    {
    e.preventDefault();
    setReceived(false);
    const res = await fetch(`${API_URL}/send-text`, {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });
    if (connected=="connected"){
      setResult("your request is being handled...")
    }
    else {
      setResult("no connection to the backend, sorry :(")
    }
    
    const data = await res.json();
    setResult("finished picture");
    setReceived(true);
  }
  
  async function textChange(e) {
    setText(e.target.value);
    setReceived(false);
    
  }
  useEffect(() => {
  const interval = setInterval(async () => {
    
    try{
    const res = await fetch(`${API_URL}`, {
      method: "GET",
      
    });
    if (!res.ok) {
      throw new Error(`HTTP error ${res.status}`);
    }
    const data = await res.json();
    if (data){
      setConnected("connected");
      setConnectedColor("text-green-500");
    }
  }
  catch{
    setConnected("not connected");
    setConnectedColor("text-red-500");
  }
    
  }, 1000);

  return () => clearInterval(interval);
}, []);

  
  return (
    
      
      
        <div >
          <div className=" bg-gray-950 outline-2 outline-cyan-800 flex justify-end">
            <p className=" text-base px-1  text-cyan-800   mt-1 md:mt-2"    >connection to backend:</p> 
            <p className= {`text-base px-1  ${connectedColor}  mr-1 md:mr-2 mt-1 md:mt-2 `}   >{connected}</p>
          </div>
          <h1 className=" text-2xl md:text-6xl font-bold text-cyan-800  hover:outline-offset-4 my-4 mx-auto text-center ">Manim Derivative Plotter</h1>
          <div className="w-9/10 md:w-2/3 mx-auto">
          
            <h1 className="text-xl md:text-4xl text-cyan-800 font-bold mb-2">Pictures</h1>
            <form onSubmit={handleSubmit} className="flex flex-row">
              <input 
                className=" bg-gray-950 text-cyan-800  placeholder-cyan-950 text-xl mr-3 outline-1 outline-cyan-800 w-1/2 md:w-1/4 hover:outline-2 focus:outline-cyan-700 focus:text-cyan-700 focus:outline-2"
                value={text}
                onChange={(e) => textChange(e)}
                
                placeholder="Put in your function"
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
            <img src={`${API_URL}/video/${text}`} alt="currently no picture" className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/>
            
            //<video controls width={640}>
              
              //<source src={`http://localhost:8000/video/${text}`} type="video/mp4" />
              //Your browser does not support the video tag.
              //<img src="dings.png"  className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/> 
            //</video>
            )}
          </div>
        </div>
      
    
  );}
