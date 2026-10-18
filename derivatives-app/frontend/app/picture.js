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
      
    var correct_input=true;
    for(let i =0;i<text.length;i++){
      
        
      if (!(Number.isFinite(Number(text[i])) || text[i]=="+" || text[i]=="-" || text[i]=="x")){
        correct_input=false;
        break;
      }
        
      
    }
    if (correct_input){
      if (connected=="connected"){
          setResult("your request is being handled...")
        }
        else {
          setResult("no connection to the backend, sorry :(")
        }
      setReceived(false);
      const res = await fetch(`${API_URL}/send-text`, { //send text to backend
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
  else{
    setResult("wrong input");
  }
    
  }
  
  async function textChange(e) { //change text on typing
    setText(e.target.value);
    setReceived(false);
    setResult("Put in a function (click help in the bottom right if you don't understand how)")
    
  }
  async function copyImage(imageUrl) { //from perplexity/copilot
    try {
      const response = await fetch(imageUrl);

      if (!response.ok) {
        throw new Error(`Image request failed: ${response.status}`);
      }

      const blob = await response.blob();

      await navigator.clipboard.write([
        new ClipboardItem({
          [blob.type]: blob,
        }),
      ]);

      setResult("Image copied");
    } catch (error) {
      console.error("Could not copy image:", error);
      setResult(
        `Copy failed: ${error instanceof Error ? error.message : "Unknown error"}`
      );
    }
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
              <div>
              <button
              className="bg-gray-950 text-cyan-800 text-xl rounded-md px-2 outline-2 outline-cyan-800 hover:outline-offset-1 hover:outline-3 hover:font-bold active:text-cyan-600 active:outline-cyan-600 mb-3"
              onClick={() => copyImage(`${API_URL}/picture/${text}`)}
              
              >
                copy Image
              </button>
              <img src="dings.png"  className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/> 
              <img src={`${API_URL}/picture/${text}`} alt="currently no picture" className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/> 
            </div>
            //<video controls width={640}>
              
              //<source src={`http://localhost:8000/video/${text}`} type="video/mp4" />
              //Your browser does not support the video tag.
              //<img src="dings.png"  className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/> 
            //</video>
            )}
            
            {connected == "not connected" &&(
              <div>
              <button
              className="bg-gray-950 text-cyan-800 text-xl rounded-md px-2 outline-2 outline-cyan-800 hover:outline-offset-1 hover:outline-3 hover:font-bold active:text-cyan-600 active:outline-cyan-600 mb-3"
              
              onClick={() => copyImage("dings.png")}
              >
                copy Image
              </button>
              <img src="dings.png"  className=" aspect-video rounded-2xl outline-3 outline-cyan-800 mx-auto"/> 
             
            </div>
            )
          }
          </div>
          
        </div>
      
    
  );}
