"use client";
 //https://official-joke-api.appspot.com/random_joke
import { useEffect, useState } from "react";

export default function Home() {
    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    
    const [text, setText] = useState("");
    const [result,setResult] =useState("Hallo");
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

    const data = await res.json();
    setResult(`Backend received: "${data.received}" (length: ${data.length})`);
    setReceived(true);
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
      setConnected("connecteed");
      setConnectedColor("text-green-500");
    }
  }
  catch{
    setConnected("nix");
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
          <div className="md:w-2/3 md:mx-auto">
          
            <h1 className="text-xl md:text-4xl text-cyan-800 font-bold mb-2">Pictures</h1>
            <form onSubmit={handleSubmit} className="flex flex-row">
              <input 
                className=" bg-gray-950 text-cyan-800  placeholder-cyan-900 text-xl"
                value={text}
                onChange={(e) => setText(e.target.value)}
                placeholder="Put in your function"
              />
            <button 
                type="submit" 
                className="bg-gray-950 text-cyan-800 text-xl rounded-md px-2 outline-2 outline-cyan-800 hover:outline-offset-1 hover:outline-3 hover:font-bold active:text-cyan-700 active:outline-cyan-700"
                >
                  Send
            </button>
            </form>
            
            <p >{result}</p>
            <img src="dings.png"  className="aspect-16/9 rounded-2xl outline-3 outline-cyan-800 mx-auto"/>
            {received &&(
            <img src={`${API_URL}/video/${text}`} />
            
            //<video controls width={640}>
              
              //<source src={`http://localhost:8000/video/${text}`} type="video/mp4" />
              //Your browser does not support the video tag.
            //</video>
            )}
          </div>
        </div>
      
    
  );}
