"use client";
import { useEffect, useState } from "react";



export default function Home() { 
    const API_URL = process.env.NEXT_PUBLIC_API_URL;
    const [helpThere,setHelpThere] = useState(false);
    async function get_help() {
        setHelpThere(!helpThere)
    }


  
  return (
    
      
      
        <div >
          
          <button 
            onClick={get_help}
            type="submit" 
            className="bg-gray-950 text-cyan-800 text-ml rounded-md outline-2 outline-cyan-800 hover:outline-offset-1 hover:outline-3 hover:font-bold active:text-cyan-600 active:outline-cyan-600 w-22 mb-2 absolute bottom-0 right-0 mr-2 "
            >
           need help?
           </button >
            {helpThere &&(
                <div className="text-s md:text-lg bg-gray-950 text-cyan-800 mb-2  rounded-xl absolute top-0 left-0 w-2/3 max-w-100 md:max-w-120 ml-3 mt-3 outline-2 outline-cyan-800 pl-2" >
                    <ul>
                        <li className="font-bold">Input style for functions: <button 
                            onClick={get_help}
                            type="submit" 
                            className="bg-gray-950 text-cyan-800 text-s rounded-md outline-1 outline-cyan-800 hover:outline-offset-1 hover:outline-3 hover:font-bold active:text-cyan-600 active:outline-cyan-600 w-10 mt-1 absolute top-0 right-0 mr-2 "
                            >
                        X
           </button > </li>
                        <li>coefficient x power+next-coefficient x next-power+...</li>
                        <li className="font-bold">A few examples:</li>
                        <li>1. 2x3</li>
                        <li>2. x3-4x2</li>
                        <li>3. 4.3x4+x</li>
                        <li>4. -2.5x6-x2+3</li>
                        <li className="font-bold">don't understand an output: </li>
                        <li><a href="https://github.com/TyrannoJ/manim" className="text-purple-800 underline hover:text-purple-700 active:text-purple-600">click to look at README</a></li>
                    </ul>
                </div>
            )

        }
            
        </div>
      
    
  );}
