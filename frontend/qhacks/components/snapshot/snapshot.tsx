"use client";
import Image from "next/image";
import React from "react";
import LeafUpload from "./leafUpload";

function Snapshot() {
  return (
    <LeafUpload>
      <div className="shadow-2xl cursor-pointer w-[50px] h-[50px] rounded-[50%] border-[2px] bg-themeBtns flex justify-center items-center hover:scale-[1.1] transition-all fixed bottom-[20px] right-[20px]">
        <Image src="/camera.svg" alt="camera" height={30} width={30} />
      </div>
    </LeafUpload>
  );
}

export default Snapshot;
