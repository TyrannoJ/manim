"use client";
 
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
      <head></head>
      <body>
        <div>
            
          <h1>Video from FastAPI</h1>
          <p>{connected}</p>
          <p>{API_URL}</p>
          
          <form onSubmit={handleSubmit}>
            <input
              value={text}
              onChange={(e) => setText(e.target.value)}
              placeholder="Type something"
            />
            <button type="submit">Send</button>
          </form>
          <p>{result}</p>
          {received &&(
            <img src={`http://192.168.178.48:8000/video/${text}`}/>
          //<video controls width={640}>
            
            //<source src={`http://localhost:8000/video/${text}`} type="video/mp4" />
            //Your browser does not support the video tag.
          //</video>
          )}
        </div>
      </body>
    </html>
  );}
