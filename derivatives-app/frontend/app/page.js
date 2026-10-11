"use client";
 //https://official-joke-api.appspot.com/random_joke
import { useEffect, useState } from "react";

export default function Home() {
    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    
    const [text, setText] = useState("");
    const [result,setResult] =useState("Hallo");
    const [received,setReceived]=useState(false);
    const [connected,setConnected]=useState("finding connection...");
    
 
  
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
    const data = await res.json()
    if (data){
      setConnected("connecteed")
    }
  }
  catch{
    setConnected("nix")
  }
    
  }, 1000);

  return () => clearInterval(interval);
}, []);

  
  return (
    <html>
      <head>
        <meta charSet="UTF-8" name="viewport" content="width=device-width, initial-scale=1.0" />
        
      </head>
      <body>
        <div >
          
          <h1 className="bg-gray-900 text-2xl font-bold text-cyan-800 outline-2 outline-cyan-800  hover:outline-offset-4 my-4 mx-auto w-64 text-center rounded-xl hover:bg-gray-800 hover:outline">Video from FastAPI</h1>
          <p className=" bg-gray-900 text-xl px-1 font-bold text-cyan-800 outline-2 outline-cyan-800 rounded-md absolute m-10 right-0 top-0  ">{connected}</p>
          
          
          <form onSubmit={handleSubmit} className="flex flex-col md:flex-row">
            <input className=" bg-gray-900"
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Type something"
            />
            <button type="submit" className="bg-gray-900">Send</button>
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
      </body>
    </html>
  );}
