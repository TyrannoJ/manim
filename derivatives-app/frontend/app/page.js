"use client";
 //https://official-joke-api.appspot.com/random_joke
 //https://github.com/saishreyansh28-ux/Slack-Bot-Stardance
import { useEffect, useState } from "react";
import Video from "./video";
import Picture from "./picture";
import Jokes from "./jokes";
import Help from "./help";

export default function Home() {
    const API_URL = process.env.NEXT_PUBLIC_API_URL;

    
    const [connected,setConnected]=useState("finding connection...");
    const [connectedColor,setConnectedColor]=useState("text-cyan-800");
    
 
  
  

  useEffect(() => { 
  const interval = setInterval(async () => { //call method every second
    
    try{
    const res = await fetch(`${API_URL}`, { //get connection status
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
          
          <Picture connected={connected} />
          <Video connected={connected} />
          <Jokes />
          <Help />
        </div>
      
    
  );}
