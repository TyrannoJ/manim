import Image from "next/image";

export default function Home() {
  return (
    <div className="flex flex-col flex-1 items-center justify-center bg-zinc-50 font-sans dark:bg-black">
     
        <p> cool stuff</p>
        <video>
          <source src='../../media/videos/useful_derivatives/1080p60/Derivatives.mp4'/>
        </video>
    </div>
  );
}
