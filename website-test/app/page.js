"use client";
 
import { useEffect, useState } from "react";

export default function Home() {
    const [text, setText] = useState("");
    
 
  
  async function handleSubmit(e) 
    {
    e.preventDefault();

    const res = await fetch("http://localhost:8000/send-text", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();
    //setResult(`Backend received: "${data.received}" (length: ${data.length})`);
  }
  return (
    <html>
        <head></head>
        <body>
             <div>
              <h1>Video from FastAPI</h1>
              <form onSubmit={handleSubmit}>
                <input
                  value={text}
                  onChange={(e) => setText(e.target.value)}
                  placeholder="Type something"
                />
                <button type="submit">Send</button>
              </form>
              <video controls width={640}>
                <source src="http://localhost:8000/video/Derivatives.mp4" type="video/mp4" />
                Your browser does not support the video tag.
              </video>
            </div>
        </body>
    </html>
  );}
